#!/usr/bin/env python3
"""Ops watchdog for this repo (stdlib only).

Signals
  stall : the latest "runner: started X" comment on the runner log issue has
          no later "runner: finished X" and is older than STALL_MINUTES.
  quiet : no commit on main, no PR opened/updated, and no issue/PR comment for
          more than QUIET_HOURS, unless the most recent issue comment contains
          "parked until <ISO time>" with that time still in the future.
          Only alerted between QUIET_WINDOW_START and QUIET_WINDOW_END (ET),
          or at any hour while the runner is mid-job.

On a signal it keeps one open issue labelled ALERT_LABEL, comments there with
evidence, and gives the issue a fresh assignment to ASSIGNEE. See README.md.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

# ---------------------------------------------------------------- settings --
def _env(name, default):
    v = os.environ.get(name, "")
    return v if v.strip() else default

REPO = _env("GITHUB_REPOSITORY", "nous-clawds4/physics")
RUNNER_ISSUE = int(_env("RUNNER_ISSUE", "146"))
STALL_MINUTES = float(_env("STALL_MINUTES", "45"))
QUIET_HOURS = float(_env("QUIET_HOURS", "3"))
QUIET_WINDOW_START = int(_env("QUIET_WINDOW_START", "8"))   # hour, ET, inclusive
QUIET_WINDOW_END = int(_env("QUIET_WINDOW_END", "24"))      # hour, ET, exclusive
REPEAT_MINUTES = float(_env("REPEAT_MINUTES", "60"))
ESCALATE_MINUTES = float(_env("ESCALATE_MINUTES", "30"))
ALERT_LABEL = _env("ALERT_LABEL", "ops-alert")
ACK_LABEL = _env("ACK_LABEL", "ack")
ASSIGNEE = _env("ASSIGNEE", "nous-clawds4")
ESCALATE_TO = _env("ESCALATE_TO", "wds4")
# Comments from these logins (plus OWNER/MEMBER/COLLABORATOR) are trusted for
# acks, park notes, runner lines and activity. The repo is public, so drive-by
# comments from strangers are ignored.
TRUSTED_USERS = {u.strip().lower() for u in _env("TRUSTED_USERS", "wds4").split(",") if u.strip()}
BOT_LOGINS = {"github-actions[bot]"}
TZ = ZoneInfo(_env("WATCHDOG_TZ", "America/New_York"))

MARK_ISSUE = "<!-- watchdog:issue -->"
MARK_ALERT_RE = re.compile(r"<!-- watchdog:alert (\{.*?\}) -->")
MARK_ESC_RE = re.compile(r"<!-- watchdog:escalation (\{.*?\}) -->")
MARK_CLEAR = "<!-- watchdog:cleared -->"
STARTED_RE = re.compile(r"^\s*runner:\s*started\s+(\S+)", re.I)
FINISHED_RE = re.compile(r"^\s*runner:\s*finished\s+(\S+)", re.I)
LIFECYCLE_RE = re.compile(r"^\s*runner:\s*(online|reached|weekly quota)", re.I)
PARK_RE = re.compile(
    r"parked until\s+`?(\d{4}-\d{2}-\d{2}(?:[T ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?)?"
    r"(?:\s?(?:Z|[+-]\d{2}:?\d{2}))?)", re.I)
ACK_RE = re.compile(r"\back(?:ed|s|nowledged?|nowledging)?\b", re.I)
TRUSTED_ASSOC = {"OWNER", "MEMBER", "COLLABORATOR"}


# ----------------------------------------------------------------- helpers --
def parse_ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))

def iso(dt):
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def et(dt):
    return dt.astimezone(TZ).strftime("%a %b %-d %H:%M ET")

def ago(now, dt):
    m = int((now - dt).total_seconds() // 60)
    return f"{m} min" if m < 120 else f"{m / 60:.1f} h"

def parse_park(text):
    """Return the aware datetime in a 'parked until <ISO>' note, else None.
    A time without an offset is read as ET; a bare date means 00:00 ET."""
    m = PARK_RE.search(text or "")
    if not m:
        return None
    raw = m.group(1).replace(" ", "T", 1) if len(m.group(1)) > 10 else m.group(1)
    raw = re.sub(r"T(\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?)\s+", r"T\1", raw)
    try:
        dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=TZ)
    return dt

def trusted(c):
    login = (c.get("user") or {}).get("login", "").lower()
    return c.get("author_association") in TRUSTED_ASSOC or login in TRUSTED_USERS

def is_watchdog_comment(c):
    b = c.get("body") or ""
    return bool(MARK_ALERT_RE.search(b) or MARK_ESC_RE.search(b) or MARK_CLEAR in b)


# ----------------------------------------------------------- signal logic --
def runner_state(comments, now):
    """comments: #146 comments (any order). Returns dict describing the
    latest started job and whether it has finished."""
    cs = sorted((c for c in comments if trusted(c)), key=lambda c: c["created_at"])
    last_start = None
    for c in cs:
        m = STARTED_RE.match(c.get("body") or "")
        if m:
            last_start = (c, m.group(1))
    if not last_start:
        return {"job": None, "mid_job": False, "stalled": False}
    sc, job = last_start
    started = parse_ts(sc["created_at"])
    finished = None
    later_lifecycle = []
    for c in cs:
        if c["created_at"] <= sc["created_at"] or c["id"] == sc["id"]:
            continue
        body = c.get("body") or ""
        fm = FINISHED_RE.match(body)
        if fm and fm.group(1) == job and finished is None:
            finished = c
        elif LIFECYCLE_RE.match(body) or STARTED_RE.match(body):
            later_lifecycle.append(c)
    unfinished = finished is None
    age_min = (now - started).total_seconds() / 60
    return {
        "job": job,
        "started_comment": sc,
        "started": started,
        "finished_comment": finished,
        # mid-job = job still open and the runner has not since said it went
        # offline/online (which would mean the job was abandoned).
        "mid_job": unfinished and not later_lifecycle,
        "later_lifecycle": later_lifecycle,
        "stalled": unfinished and age_min > STALL_MINUTES,
        "age_min": age_min,
    }


def evaluate(data, now):
    """Pure function. data keys:
      runner_comments: list of #146 comments
      last_commit:     {"sha","date","html_url"} or None (latest commit on main)
      last_pr:         {"number","updated_at","created_at","html_url"} or None
      recent_comments: repo issue/PR comments, newest first (raw API objects)
      alert_issue_numbers: set of ints (ops-alert issues; their comments are
                       not counted as loop activity)
    Returns (conditions, info). Each condition: key, kind, notify, title, lines.
    """
    conds = []
    rs = runner_state(data.get("runner_comments", []), now)
    info = {"runner": rs}

    if rs["stalled"]:
        sc = rs["started_comment"]
        lines = [
            f"Latest runner start on #{RUNNER_ISSUE}: [`runner: started {rs['job']}`]({sc['html_url']}) "
            f"at {et(rs['started'])} ({ago(now, rs['started'])} ago), with no later `runner: finished {rs['job']}`.",
            f"Threshold: {STALL_MINUTES:g} min (real jobs take about 8 to 18 min).",
        ]
        for c in rs["later_lifecycle"]:
            first = (c.get("body") or "").strip().splitlines()[0][:120]
            lines.append(f"Later runner line: [{first}]({c['html_url']}) at {et(parse_ts(c['created_at']))}. "
                         "The job looks abandoned rather than still running.")
        conds.append({"key": f"stall:{rs['job']}:{sc['id']}", "kind": "stall", "notify": True,
                      "title": f"Runner stall: {rs['job']} started {ago(now, rs['started'])} ago and has not finished",
                      "lines": lines})

    # ---- quiet
    alert_issues = set(data.get("alert_issue_numbers") or ())
    activity = []
    lc = data.get("last_commit")
    if lc:
        activity.append((parse_ts(lc["date"]), f"commit [{lc['sha'][:7]}]({lc['html_url']}) on main"))
    lp = data.get("last_pr")
    if lp:
        activity.append((parse_ts(lp["updated_at"]), f"PR [#{lp['number']}]({lp['html_url']}) opened/updated"))
    latest_comment = None
    for c in data.get("recent_comments", []):
        login = (c.get("user") or {}).get("login", "")
        num = int(c["issue_url"].rstrip("/").rsplit("/", 1)[-1])
        if login in BOT_LOGINS or is_watchdog_comment(c) or num in alert_issues or not trusted(c):
            continue
        latest_comment = c
        break
    if latest_comment:
        num = latest_comment["issue_url"].rstrip("/").rsplit("/", 1)[-1]
        activity.append((parse_ts(latest_comment["created_at"]),
                         f"[comment]({latest_comment['html_url']}) on #{num}"))
    info["activity"] = activity
    park = parse_park(latest_comment.get("body")) if latest_comment else None
    info["park"] = park
    if activity:
        last_ts, last_what = max(activity, key=lambda a: a[0])
        quiet_h = (now - last_ts).total_seconds() / 3600
        info["quiet_hours"] = quiet_h
        parked = park is not None and park > now
        hour = now.astimezone(TZ).hour
        in_window = QUIET_WINDOW_START <= hour < QUIET_WINDOW_END
        info.update(parked=parked, in_window=in_window)
        if quiet_h > QUIET_HOURS and not parked:
            lines = [f"No commit on main, PR activity, or issue/PR comment for {quiet_h:.1f} h "
                     f"(threshold {QUIET_HOURS:g} h). Most recent of each:"]
            for ts, what in sorted(activity, key=lambda a: a[0], reverse=True):
                lines.append(f"- {what} at {et(ts)} ({ago(now, ts)} ago)")
            if park is not None:
                lines.append(f"The latest comment has a park note that expired at {et(park)}.")
            else:
                lines.append('No active "parked until <ISO time>" note in the latest comment.')
            conds.append({"key": f"quiet:{iso(last_ts)}", "kind": "quiet",
                          "notify": in_window or rs["mid_job"],
                          "title": f"Loop quiet for {quiet_h:.1f} h (since {et(last_ts)})",
                          "lines": lines})
    return conds, info


def plan(conds, issue, issue_comments, issue_labels, now):
    """Pure function deciding what to do. issue is None or {"number",...}.
    Returns a list of action dicts executed in order by apply()."""
    notify = [c for c in conds if c["notify"]]
    actions = []
    if issue is None:
        if not notify:
            return actions
        actions.append({"op": "create_issue"})
        issue_comments, issue_labels = [], []

    alerts, escalations = [], set()
    for c in sorted(issue_comments, key=lambda c: c["created_at"]):
        b = c.get("body") or ""
        login = (c.get("user") or {}).get("login", "")
        if not (login in BOT_LOGINS or trusted(c)):
            continue
        m = MARK_ALERT_RE.search(b)
        if m:
            meta = json.loads(m.group(1))
            alerts.append({"at": parse_ts(c["created_at"]), "keys": meta.get("keys", []),
                           "run": meta.get("run"), "run_start": parse_ts(meta.get("run_start", c["created_at"]))})
        m = MARK_ESC_RE.search(b)
        if m:
            escalations.add(json.loads(m.group(1)).get("run"))

    if not conds:
        if issue is not None:
            actions.append({"op": "clear", "remove_ack": ACK_LABEL in issue_labels})
        return actions
    if not notify:
        return actions  # e.g. quiet overnight: keep issue open, stay silent

    last_alert = alerts[-1] if alerts else None
    ack_comments = [parse_ts(c["created_at"]) for c in issue_comments
                    if trusted(c) and not is_watchdog_comment(c)
                    and (c.get("user") or {}).get("login", "") not in BOT_LOGINS
                    and ACK_RE.search(c.get("body") or "")]
    acked = ACK_LABEL in issue_labels or (
        last_alert is not None and any(t > last_alert["at"] for t in ack_comments))

    seen = {k for a in alerts for k in a["keys"]}
    new_keys = [c["key"] for c in notify if c["key"] not in seen]
    post = None
    if new_keys:
        post = "new"
    elif last_alert and not acked and (now - last_alert["at"]).total_seconds() / 60 >= REPEAT_MINUTES:
        post = "repeat"

    run, run_start = (last_alert["run"], last_alert["run_start"]) if last_alert else (None, None)
    if post:
        if last_alert is None or acked:
            run, run_start = iso(now), now          # a new unacknowledged stretch
        actions.append({"op": "alert", "kind": post, "new_keys": new_keys,
                        "run": run, "run_start": iso(run_start),
                        "remove_ack": post == "new" and ACK_LABEL in issue_labels})
        actions.append({"op": "reassign"})
        acked = False

    if (not acked and run and run not in escalations
            and (now - run_start).total_seconds() / 60 > ESCALATE_MINUTES):
        actions.append({"op": "escalate", "run": run, "run_start": iso(run_start)})
    return actions


# ------------------------------------------------------------- rendering --
def render_alert(action, conds, now):
    notify = [c for c in conds if c["notify"]]
    head = "New alert" if action["kind"] == "new" else "Still active (hourly reminder, not yet acknowledged)"
    out = [f"### Watchdog: {head}", f"Checked at {et(now)}.", ""]
    for c in notify:
        tag = " **(new)**" if c["key"] in action["new_keys"] else ""
        out.append(f"**{c['title']}**{tag}")
        out += c["lines"]
        out.append("")
    held = [c for c in conds if not c["notify"]]
    for c in held:
        out.append(f"(Also true but outside the alert window: {c['title']}.)")
    out.append(f"To acknowledge, add the `{ACK_LABEL}` label or reply with a comment containing \"ack\". "
               f"If nobody acknowledges within {ESCALATE_MINUTES:g} min, @{ESCALATE_TO} gets pinged. "
               "This issue closes itself when the conditions clear.")
    meta = {"keys": [c["key"] for c in notify], "run": action["run"], "run_start": action["run_start"]}
    out.append(f"<!-- watchdog:alert {json.dumps(meta)} -->")
    return "\n".join(out)

def render_escalation(action, conds, now):
    notify = [c for c in conds if c["notify"]]
    start = parse_ts(action["run_start"])
    out = [f"@{ESCALATE_TO} escalation: this alert has gone unacknowledged since {et(start)} "
           f"({ago(now, start)}).", ""]
    for c in notify:
        out.append(f"- {c['title']}")
    out += ["", f"Details are in the comments above. Add the `{ACK_LABEL}` label or reply \"ack\" to acknowledge.",
            f"<!-- watchdog:escalation {json.dumps({'run': action['run']})} -->"]
    return "\n".join(out)

def render_clear(now):
    return (f"cleared\n\nWatchdog at {et(now)}: no active conditions (runner not stalled, loop not quiet). "
            f"Closing.\n{MARK_CLEAR}")


# ------------------------------------------------------------ GitHub I/O --
class GitHub:
    def __init__(self, repo, token):
        self.repo, self.token = repo, token

    def req(self, method, path, body=None, params=None, ok404=False):
        url = path if path.startswith("http") else f"https://api.github.com{path}"
        if params:
            url += ("&" if "?" in url else "?") + urllib.parse.urlencode(params)
        data = json.dumps(body).encode() if body is not None else None
        r = urllib.request.Request(url, data=data, method=method, headers={
            "Authorization": f"Bearer {self.token}", "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "physics-watchdog"})
        try:
            with urllib.request.urlopen(r, timeout=30) as resp:
                raw = resp.read()
                link = resp.headers.get("Link", "")
                return (json.loads(raw) if raw else None), link
        except urllib.error.HTTPError as e:
            if ok404 and e.code in (404, 422):
                return None, ""
            raise RuntimeError(f"{method} {url} -> {e.code}: {e.read()[:300]!r}")

    def get(self, path, params=None):
        return self.req("GET", path, params=params)[0]

    def get_all(self, path, params=None):
        params = dict(params or {}, per_page=100)
        out, url = [], f"https://api.github.com{path}?" + urllib.parse.urlencode(params)
        while url:
            page, link = self.req("GET", url)
            out += page
            m = re.search(r'<([^>]+)>;\s*rel="next"', link)
            url = m.group(1) if m else None
        return out

    # data gathering
    def gather(self):
        r = self.repo
        runner_comments = self.get_all(f"/repos/{r}/issues/{RUNNER_ISSUE}/comments")
        commits = self.get(f"/repos/{r}/commits", {"sha": "main", "per_page": 1})
        last_commit = None
        if commits:
            c = commits[0]
            last_commit = {"sha": c["sha"], "date": c["commit"]["committer"]["date"], "html_url": c["html_url"]}
        prs = self.get(f"/repos/{r}/pulls", {"state": "all", "sort": "updated", "direction": "desc", "per_page": 1})
        last_pr = None
        if prs:
            p = prs[0]
            last_pr = {"number": p["number"], "updated_at": p["updated_at"],
                       "created_at": p["created_at"], "html_url": p["html_url"]}
        recent = self.get(f"/repos/{r}/issues/comments", {"sort": "created", "direction": "desc", "per_page": 100})
        alert_issues = self.get(f"/repos/{r}/issues", {"labels": ALERT_LABEL, "state": "all", "per_page": 100})
        return {"runner_comments": runner_comments, "last_commit": last_commit, "last_pr": last_pr,
                "recent_comments": recent,
                "alert_issue_numbers": {i["number"] for i in alert_issues}}

    def find_issue(self):
        issues = self.get(f"/repos/{self.repo}/issues",
                          {"labels": ALERT_LABEL, "state": "open", "sort": "created", "direction": "asc"})
        issues = [i for i in issues if "pull_request" not in i and MARK_ISSUE in (i.get("body") or "")]
        return issues[0] if issues else None

    def ensure_label(self, name, color, desc):
        _, _ = self.req("POST", f"/repos/{self.repo}/labels",
                        {"name": name, "color": color, "description": desc}, ok404=True)


class GhCli(GitHub):
    """Local testing helper: same API calls, made through the `gh` CLI's own
    login instead of a token (used only when GITHUB_TOKEN is unset)."""
    def __init__(self, repo):
        self.repo = repo

    def _run(self, args, body=None):
        import subprocess
        p = subprocess.run(["gh", "api", "-H", "X-GitHub-Api-Version: 2022-11-28"] + args,
                           input=json.dumps(body) if body is not None else None,
                           capture_output=True, text=True)
        if p.returncode != 0:
            raise RuntimeError(f"gh api {args}: {p.stderr.strip()[:300]}")
        return json.loads(p.stdout) if p.stdout.strip() else None

    def req(self, method, path, body=None, params=None, ok404=False):
        if params:
            path += ("&" if "?" in path else "?") + urllib.parse.urlencode(params)
        args = ["-X", method, path.replace("https://api.github.com", "")]
        if body is not None:
            args += ["--input", "-"]
        try:
            return self._run(args, body), ""
        except RuntimeError:
            if ok404:
                return None, ""
            raise

    def get_all(self, path, params=None):
        params = dict(params or {}, per_page=100)
        import subprocess
        p = subprocess.run(["gh", "api", "--paginate", "--jq", ".[] | tojson",
                            f"{path}?{urllib.parse.urlencode(params)}"], capture_output=True, text=True)
        if p.returncode != 0:
            raise RuntimeError(f"gh api {path}: {p.stderr.strip()[:300]}")
        return [json.loads(line) for line in p.stdout.splitlines() if line.strip()]


def apply(gh, actions, conds, issue, now, dry_run=False):
    log = []
    def do(desc, fn):
        log.append(desc)
        print(("[dry-run] " if dry_run else "") + desc)
        return None if dry_run else fn()
    r = gh.repo if gh else REPO
    num = issue["number"] if issue else None
    for a in actions:
        op = a["op"]
        if op == "create_issue":
            if gh and not dry_run:
                gh.ensure_label(ALERT_LABEL, "b60205", "Automated watchdog alert")
                gh.ensure_label(ACK_LABEL, "0e8a16", "Alert acknowledged")
            notify = [c for c in conds if c["notify"]]
            title = "Ops alert: " + "; ".join(c["kind"] for c in notify)
            body = ("Automated alert issue opened by the watchdog workflow "
                    "(`.github/workflows/watchdog.yml`). Alerts are posted as comments below. "
                    f"Acknowledge with the `{ACK_LABEL}` label or an \"ack\" comment. "
                    "The watchdog closes this issue when the conditions clear.\n\n" + MARK_ISSUE)
            res = do(f"create issue '{title}' labelled {ALERT_LABEL}, assigned {ASSIGNEE}",
                     lambda: gh.req("POST", f"/repos/{r}/issues",
                                    {"title": title, "body": body, "labels": [ALERT_LABEL], "assignees": [ASSIGNEE]})[0])
            num = res["number"] if res else "NEW"
            a["_created"] = True
        elif op == "alert":
            if a.get("remove_ack"):
                do(f"remove label {ACK_LABEL} from #{num} (new alert needs a fresh ack)",
                   lambda: gh.req("DELETE", f"/repos/{r}/issues/{num}/labels/{ACK_LABEL}", ok404=True))
            body = render_alert(a, conds, now)
            do(f"comment on #{num} ({a['kind']} alert, keys={[c['key'] for c in conds if c['notify']]}):\n"
               + "\n".join("    | " + l for l in body.splitlines()),
               lambda: gh.req("POST", f"/repos/{r}/issues/{num}/comments", {"body": body}))
        elif op == "reassign":
            if any(x.get("_created") for x in actions):
                continue  # just created with the assignee: that is the fresh assignment
            do(f"unassign {ASSIGNEE} from #{num}",
               lambda: gh.req("DELETE", f"/repos/{r}/issues/{num}/assignees", {"assignees": [ASSIGNEE]}))
            do(f"assign {ASSIGNEE} to #{num}",
               lambda: gh.req("POST", f"/repos/{r}/issues/{num}/assignees", {"assignees": [ASSIGNEE]}))
        elif op == "escalate":
            body = render_escalation(a, conds, now)
            do(f"comment on #{num} (escalation):\n" + "\n".join("    | " + l for l in body.splitlines()),
               lambda: gh.req("POST", f"/repos/{r}/issues/{num}/comments", {"body": body}))
        elif op == "clear":
            do(f"comment 'cleared' on #{num}",
               lambda: gh.req("POST", f"/repos/{r}/issues/{num}/comments", {"body": render_clear(now)}))
            if a.get("remove_ack"):
                do(f"remove label {ACK_LABEL} from #{num}",
                   lambda: gh.req("DELETE", f"/repos/{r}/issues/{num}/labels/{ACK_LABEL}", ok404=True))
            do(f"close #{num}",
               lambda: gh.req("PATCH", f"/repos/{r}/issues/{num}", {"state": "closed", "state_reason": "completed"}))
    return log


def summarize(conds, info, now):
    rs = info["runner"]
    print(f"now: {et(now)}")
    if rs["job"]:
        print(f"runner: last start {rs['job']} at {et(rs['started'])}, "
              f"finished={'yes' if rs['finished_comment'] else 'no'}, mid_job={rs['mid_job']}, "
              f"stalled={rs['stalled']}")
    else:
        print("runner: no start lines found")
    if "quiet_hours" in info:
        print(f"activity: quiet {info['quiet_hours']:.2f} h, in_window={info['in_window']}, "
              f"parked={info['parked']} (park note: {et(info['park']) if info['park'] else 'none'})")
    print("conditions:", [(c["key"], "notify" if c["notify"] else "held") for c in conds] or "none")


def main():
    dry_run = "--dry-run" in sys.argv or os.environ.get("WATCHDOG_DRY_RUN") == "1"
    now = datetime.now(timezone.utc)
    if os.environ.get("WATCHDOG_NOW"):
        now = parse_ts(os.environ["WATCHDOG_NOW"])
    token = os.environ.get("GITHUB_TOKEN")
    gh = GitHub(REPO, token) if token else GhCli(REPO)
    data = gh.gather()
    conds, info = evaluate(data, now)
    summarize(conds, info, now)
    issue = gh.find_issue()
    comments, labels = [], []
    if issue:
        comments = gh.get_all(f"/repos/{REPO}/issues/{issue['number']}/comments")
        labels = [l["name"] for l in issue.get("labels", [])]
        print(f"open alert issue: #{issue['number']} labels={labels}")
    else:
        print("open alert issue: none")
    actions = plan(conds, issue, comments, labels, now)
    print("actions:", [a["op"] for a in actions] or "none")
    apply(gh, actions, conds, issue, now, dry_run=dry_run)


if __name__ == "__main__":
    main()
