#!/usr/bin/env python3
"""Offline tests for watchdog.py with fake inputs. Run: python3 test_watchdog.py -v"""
import itertools
import unittest
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import watchdog as W

ET = ZoneInfo("America/New_York")
_ids = itertools.count(1000)
VERBOSE = True


def t(s):
    """'2026-09-29 14:00' in ET -> aware datetime."""
    return datetime.fromisoformat(s).replace(tzinfo=ET)


def cm(body, at, issue=146, login="nous-clawds4", assoc="OWNER"):
    i = next(_ids)
    return {"id": i, "body": body, "created_at": W.iso(at), "user": {"login": login},
            "author_association": assoc,
            "issue_url": f"https://api.github.com/repos/nous-clawds4/physics/issues/{issue}",
            "html_url": f"https://github.com/nous-clawds4/physics/issues/{issue}#issuecomment-{i}"}


def data(runner=(), commit_at=None, pr_at=None, comments=(), alert_issues=()):
    return {
        "runner_comments": list(runner),
        "last_commit": commit_at and {"sha": "abcdef1234567", "date": W.iso(commit_at),
                                      "html_url": "https://github.com/nous-clawds4/physics/commit/abcdef1"},
        "last_pr": pr_at and {"number": 187, "updated_at": W.iso(pr_at), "created_at": W.iso(pr_at),
                              "html_url": "https://github.com/nous-clawds4/physics/pull/187"},
        "recent_comments": sorted(comments, key=lambda c: c["created_at"], reverse=True),
        "alert_issue_numbers": set(alert_issues),
    }


class Sim:
    """Simulates the alert issue across successive watchdog runs."""
    def __init__(self):
        self.issue, self.comments, self.labels, self.log = None, [], [], []
        self.edits = []  # (op, new body) for issue body edits

    def run(self, d, now, label=""):
        conds, info = W.evaluate(d, now)
        actions = W.plan(conds, self.issue, self.comments, self.labels, now)
        if VERBOSE:
            print(f"\n--- {label} @ {W.et(now)}")
            W.summarize(conds, info, now)
            print("actions:", [a["op"] for a in actions] or "none")
            W.apply(None, [dict(a) for a in actions], conds, self.issue, now, dry_run=True)
        for a in actions:  # mirror effects into the fake issue
            if a["op"] == "create_issue":
                self.issue, self.comments, self.labels = {"number": 999, "body": "alert " + W.MARK_ISSUE}, [], ["ops-alert"]
            elif a["op"] == "status":
                lines, meta = W.render_status(a, conds, now)
                self.issue["body"] = W.with_status(self.issue["body"], lines, meta)
                self.edits.append(("status", self.issue["body"]))
            elif a["op"] == "alert":
                if a.get("remove_ack") and "ack" in self.labels:
                    self.labels.remove("ack")
                self.comments.append(cm(W.render_alert(a, conds, now), now, 999, "github-actions[bot]", "NONE"))
            elif a["op"] == "escalate":
                self.comments.append(cm(W.render_escalation(a, conds, now), now, 999, "github-actions[bot]", "NONE"))
            elif a["op"] == "clear":
                lines, meta = W.render_clear_status(now)
                self.edits.append(("clear", W.with_status(self.issue["body"], lines, meta)))
                self.issue = None
                self.comments, self.labels = [], []
        return [a["op"] for a in actions], conds


class TestStall(unittest.TestCase):
    def test_simulated_stall_lifecycle(self):
        s = Sim()
        start = t("2026-09-29 14:00")
        runner = [cm("runner: online at Tue 13:59 EDT, pid 1", t("2026-09-29 13:59")),
                  cm("runner: started 006-test.txt at Tue 14:00 EDT", start)]
        busy = dict(commit_at=t("2026-09-29 14:30"), pr_at=t("2026-09-29 14:30"))

        ops, _ = s.run(data(runner, **busy), t("2026-09-29 14:30"), "30 min into the job (normal)")
        self.assertEqual(ops, [])
        ops, conds = s.run(data(runner, **busy), t("2026-09-29 14:46"), "46 min, no finish -> stall")
        self.assertEqual(ops, ["create_issue", "alert", "reassign"])
        self.assertEqual(conds[0]["kind"], "stall")
        ops, _ = s.run(data(runner, **busy), t("2026-09-29 15:01"), "15 min later: no duplicate")
        self.assertEqual(ops, [])
        ops, _ = s.run(data(runner, **busy), t("2026-09-29 15:17"), "31 min unacked -> escalate")
        self.assertEqual(ops, ["escalate"])
        ops, _ = s.run(data(runner, **busy), t("2026-09-29 15:32"), "escalated once only")
        self.assertEqual(ops, [])
        n_comments = len(s.comments)
        ops, _ = s.run(data(runner, **busy), t("2026-09-29 15:47"), "61 min -> hourly status edit + reassign")
        self.assertEqual(ops, ["status", "reassign"])
        self.assertEqual(len(s.comments), n_comments, "hourly reminder must not add a comment")
        self.assertEqual(W.read_status(s.issue["body"])["count"], 1)
        ops, _ = s.run(data(runner, **busy), t("2026-09-29 16:17"), "no second escalation for same stretch")
        self.assertEqual(ops, [])
        ops, _ = s.run(data(runner, **busy), t("2026-09-29 16:32"), "45 min after the status edit: nothing")
        self.assertEqual(ops, [])
        ops, _ = s.run(data(runner, **busy), t("2026-09-29 16:47"), "next hour -> same status block edited again")
        self.assertEqual(ops, ["status", "reassign"])
        self.assertEqual(len(s.comments), n_comments)
        self.assertEqual(s.issue["body"].count(W.MARK_STATUS_BEGIN), 1)
        self.assertEqual(s.issue["body"].count(W.MARK_ISSUE), 1)
        self.assertEqual(W.read_status(s.issue["body"])["count"], 2)
        self.assertNotIn("@wds4", s.issue["body"])
        s.comments.append(cm("ack, looking at the runner", t("2026-09-29 16:20"), 999))
        ops, _ = s.run(data(runner, **busy), t("2026-09-29 17:02"), "acked -> silent")
        self.assertEqual(ops, [])
        fin = runner + [cm("runner: finished 006-test.txt at Tue 17:05 EDT, rc=0", t("2026-09-29 17:05"))]
        s.labels.append("ack")
        n_comments = len(s.comments)
        ops, _ = s.run(data(fin, **busy), t("2026-09-29 17:15"), "finished -> cleared")
        self.assertEqual(ops, ["clear"])
        self.assertEqual(s.edits[-1][0], "clear")
        self.assertIn(W.MARK_CLEAR, s.edits[-1][1])

    def test_only_one_mention_per_alert_issue(self):
        s = Sim()
        runner = [cm("runner: started 006-test.txt at x", t("2026-09-29 14:00"))]
        busy = dict(commit_at=t("2026-09-29 14:30"), pr_at=t("2026-09-29 14:30"))
        s.run(data(runner, **busy), t("2026-09-29 14:46"), "stall")
        s.run(data(runner, **busy), t("2026-09-29 15:17"), "escalate")
        s.comments.append(cm("ack", t("2026-09-29 15:20"), 999))
        # a new condition after the ack starts a new unacknowledged stretch
        runner2 = [cm("runner: started 007-test.txt at x", t("2026-09-29 15:30"))]
        for at in ("2026-09-29 16:16", "2026-09-29 16:50", "2026-09-29 17:20", "2026-09-29 18:20"):
            s.run(data(runner2, **busy), t(at), "new stall after ack, never re-escalated")
        mentions = [c for c in s.comments if "@wds4" in c["body"]]
        self.assertEqual(len(mentions), 1)
        self.assertEqual(len([c for c in s.comments if W.MARK_ESC_RE.search(c["body"])]), 1)
        for c in s.comments:
            if W.MARK_ALERT_RE.search(c["body"]):
                self.assertNotIn("@wds4", c["body"])

    def test_old_reminder_comments_still_parsed(self):
        """Issues opened before this change have reminders as comments."""
        cond = [{"key": "quiet:x", "kind": "quiet", "notify": True, "title": "q", "lines": []}]
        run = W.iso(t("2026-09-29 10:00"))
        mk = lambda kind, at: cm(W.render_alert({"kind": kind, "new_keys": [], "run": run, "run_start": run},
                                                cond, at), at, 999, "github-actions[bot]", "NONE")
        cs = [mk("new", t("2026-09-29 10:00")),
              cm(W.render_escalation({"run": run, "run_start": run}, cond, t("2026-09-29 10:31")),
                 t("2026-09-29 10:31"), 999, "github-actions[bot]", "NONE"),
              mk("repeat", t("2026-09-29 11:00"))]
        self.assertEqual(W.plan(cond, {"number": 999}, cs, ["ops-alert"], t("2026-09-29 11:30")), [])
        self.assertEqual([a["op"] for a in W.plan(cond, {"number": 999}, cs, ["ops-alert"], t("2026-09-29 12:00"))],
                         ["status", "reassign"])

    def test_clear_action_removes_ack(self):
        acts = W.plan([], {"number": 5}, [], ["ops-alert", "ack"], t("2026-09-29 12:00"))
        self.assertEqual(acts, [{"op": "clear", "remove_ack": True}])

    def test_finished_other_job_does_not_count(self):
        now = t("2026-09-29 15:00")
        r = [cm("runner: started 007-a.txt at x", t("2026-09-29 14:00")),
             cm("runner: finished 006-b.txt at x, rc=0", t("2026-09-29 14:10"))]
        rs = W.runner_state(r, now)
        self.assertTrue(rs["stalled"] and rs["mid_job"])

    def test_abandoned_job_still_stalls_but_not_mid_job(self):
        now = t("2026-09-29 15:00")
        r = [cm("runner: started 007-a.txt at x", t("2026-09-29 14:00")),
             cm("runner: reached Mon 20:00 ET stop time, exiting", t("2026-09-29 14:20"))]
        conds, info = W.evaluate(data(r, commit_at=now), now)
        self.assertFalse(info["runner"]["mid_job"])
        self.assertEqual([c["kind"] for c in conds], ["stall"])
        self.assertIn("abandoned", "\n".join(conds[0]["lines"]))

    def test_stranger_runner_line_ignored(self):
        now = t("2026-09-29 15:00")
        r = [cm("runner: started fake.txt at x", t("2026-09-29 13:00"), login="rando", assoc="NONE")]
        self.assertIsNone(W.runner_state(r, now)["job"])


class TestQuiet(unittest.TestCase):
    def test_simulated_quiet_period(self):
        s = Sim()
        last = t("2026-09-29 10:00")
        runner = [cm("runner: started 005.txt at x", t("2026-09-29 09:00")),
                  cm("runner: finished 005.txt at x, rc=0", t("2026-09-29 09:15"))]
        d = data(runner, commit_at=last, pr_at=t("2026-09-29 09:30"),
                 comments=[cm("working on v0.9", last, 150)])
        ops, _ = s.run(d, t("2026-09-29 12:59"), "2h59m quiet: fine")
        self.assertEqual(ops, [])
        ops, conds = s.run(d, t("2026-09-29 13:01"), "3h01m quiet -> alert")
        self.assertEqual(ops, ["create_issue", "alert", "reassign"])
        self.assertEqual(conds[0]["kind"], "quiet")
        s.labels.append("ack")
        ops, _ = s.run(d, t("2026-09-29 14:30"), "ack label -> no reminder, no escalation")
        self.assertEqual(ops, [])
        # a stall appears while quiet is acked: new condition -> new alert, ack removed, reassigned
        runner2 = runner + [cm("runner: started 006.txt at x", t("2026-09-29 13:50"))]
        d2 = dict(d, runner_comments=runner2)
        # the runner line is itself a comment, so quiet restarts from 13:50
        d2["recent_comments"] = [runner2[-1]] + d["recent_comments"]
        ops, conds = s.run(d2, t("2026-09-29 14:40"), "new stall while quiet acked")
        self.assertEqual(ops, ["alert", "reassign"])
        self.assertNotIn("ack", s.labels)
        # activity resumes and the job finishes -> cleared
        fin = runner2 + [cm("runner: finished 006.txt at x, rc=0", t("2026-09-29 14:45"))]
        d3 = data(fin, commit_at=t("2026-09-29 14:50"))
        ops, _ = s.run(d3, t("2026-09-29 15:00"), "all clear")
        self.assertEqual(ops, ["clear"])

    def test_parked_suppresses_until_expiry(self):
        s = Sim()
        last = t("2026-09-29 10:00")
        d = data([], commit_at=t("2026-09-29 09:00"),
                 comments=[cm("Loop idle; parked until 2026-09-29T18:00-04:00 waiting on David", last, 150)])
        ops, _ = s.run(d, t("2026-09-29 15:00"), "5h quiet but parked until 18:00")
        self.assertEqual(ops, [])
        ops, conds = s.run(d, t("2026-09-29 18:15"), "park expired -> alert")
        self.assertEqual(ops, ["create_issue", "alert", "reassign"])
        self.assertIn("expired", "\n".join(conds[0]["lines"]))

    def test_park_note_on_146_survives_later_runner_comment(self):
        """Issue #215: a runner line after the park note used to hide it."""
        runner = [cm("runner: started 007.txt at Wed 19:04 EDT", t("2026-09-30 19:04")),
                  cm("Physics Lead: v0.8.1 is up. parked until 2026-10-01T18:30-04:00", t("2026-09-30 19:05")),
                  cm("runner: finished 007.txt at Wed 19:08 EDT, rc=0", t("2026-09-30 19:08"))]
        d = data(runner, commit_at=t("2026-09-30 19:00"), pr_at=t("2026-09-30 19:21"),
                 comments=list(reversed(runner)))
        conds, info = W.evaluate(d, t("2026-10-01 08:15"))
        self.assertEqual(conds, [])
        self.assertTrue(info["parked"])
        self.assertEqual(info["park"], t("2026-10-01 18:30"))
        conds, _ = W.evaluate(d, t("2026-10-01 18:45"))
        self.assertEqual([c["kind"] for c in conds], ["quiet"])
        self.assertIn("expired", "\n".join(conds[0]["lines"]))

    def test_most_recent_park_note_wins(self):
        runner = [cm("parked until 2026-10-02T09:00-04:00", t("2026-09-30 19:00")),
                  cm("parked until 2026-10-01T06:00-04:00", t("2026-09-30 20:00")),
                  cm("runner: finished 007.txt at x, rc=0", t("2026-09-30 20:05"))]
        d = data(runner, commit_at=t("2026-09-30 19:00"), comments=list(reversed(runner)))
        conds, info = W.evaluate(d, t("2026-10-01 09:00"))
        self.assertEqual([c["kind"] for c in conds], ["quiet"])
        self.assertEqual(info["park"], t("2026-10-01 06:00"))

    def test_park_scan_window(self):
        old = cm("parked until 2026-10-10T09:00-04:00", t("2026-09-27 09:00"))
        filler = [cm(f"runner: started {i:03}.txt at x", t("2026-09-27 10:00") + timedelta(minutes=i))
                  for i in range(25)]
        d = data([old] + filler, commit_at=t("2026-09-29 08:00"))
        # older than 48 h and not among the last 20 comments on #146 -> ignored
        conds, info = W.evaluate(d, t("2026-09-30 12:00"))
        self.assertIsNone(info["park"])
        # within 48 h -> honoured even though more than 20 comments came after it
        conds, info = W.evaluate(d, t("2026-09-28 12:00"))
        self.assertTrue(info["parked"])
        # among the last 20 -> honoured even when older than 48 h
        d = data([old] + filler[:5], commit_at=t("2026-09-29 08:00"))
        conds, info = W.evaluate(d, t("2026-09-30 12:00"))
        self.assertTrue(info["parked"])

    def test_stranger_park_note_ignored(self):
        runner = [cm("parked until 2026-10-02T09:00-04:00", t("2026-09-30 19:00"), login="rando", assoc="NONE")]
        d = data(runner, commit_at=t("2026-09-30 08:00"))
        conds, info = W.evaluate(d, t("2026-09-30 13:00"))
        self.assertIsNone(info["park"])

    def test_park_must_be_latest_comment(self):
        d = data([], commit_at=t("2026-09-29 08:00"),
                 comments=[cm("parked until 2026-09-30T08:00Z", t("2026-09-29 09:00"), 150),
                           cm("unrelated note", t("2026-09-29 09:30"), 151)])
        conds, _ = W.evaluate(d, t("2026-09-29 13:00"))
        self.assertEqual([c["kind"] for c in conds], ["quiet"])

    def test_overnight_held_unless_mid_job(self):
        d = data([cm("runner: finished 005.txt at x", t("2026-09-29 18:00"))],
                 commit_at=t("2026-09-29 20:00"))
        s = Sim()
        ops, conds = s.run(d, t("2026-09-30 02:00"), "02:00 ET, 6h quiet, runner idle -> held")
        self.assertEqual(ops, [])
        self.assertFalse(conds[0]["notify"])
        d2 = data([cm("runner: started 008.txt at x", t("2026-09-30 01:40"))], commit_at=t("2026-09-29 20:00"))
        d2["recent_comments"] = []  # pretend the runner line is not visible as a comment
        ops, conds = s.run(d2, t("2026-09-30 02:00"), "02:00 ET, runner mid-job -> quiet alerts")
        self.assertEqual(ops, ["create_issue", "alert", "reassign"])

    def test_held_quiet_keeps_issue_open_overnight(self):
        conds = [{"key": "quiet:x", "kind": "quiet", "notify": False, "title": "q", "lines": []}]
        self.assertEqual(W.plan(conds, {"number": 5}, [], ["ops-alert"], t("2026-09-30 01:00")), [])

    def test_morning_alert_after_overnight_quiet(self):
        d = data([], commit_at=t("2026-09-29 22:00"))
        conds, _ = W.evaluate(d, t("2026-09-30 08:00"))
        self.assertTrue(conds[0]["notify"])

    def test_watchdog_bot_and_stranger_comments_are_not_activity(self):
        last = t("2026-09-29 09:00")
        d = data([], commit_at=last, comments=[
            cm("drive-by comment", t("2026-09-29 12:30"), 150, "rando", "NONE"),
            cm("Watchdog alert <!-- watchdog:alert {} -->", t("2026-09-29 12:40"), 999, "github-actions[bot]", "NONE"),
            cm("ack", t("2026-09-29 12:45"), 999)], alert_issues={999})
        conds, info = W.evaluate(d, t("2026-09-29 12:50"))
        self.assertEqual([c["kind"] for c in conds], ["quiet"])


class TestBody(unittest.TestCase):
    def test_status_block_replaced_in_place(self):
        body = "Automated alert issue.\n\n" + W.MARK_ISSUE
        b1 = W.with_status(body, ["one"], {"run": "r", "at": "2026-09-29T15:00:00Z", "count": 1})
        b2 = W.with_status(b1, ["two"], {"run": "r", "at": "2026-09-29T16:00:00Z", "count": 2})
        self.assertTrue(b2.startswith(body))
        self.assertNotIn("one", b2.replace(body, ""))
        self.assertEqual(b2.count(W.MARK_STATUS_BEGIN), 1)
        self.assertEqual(W.read_status(b2)["count"], 2)


class TestAck(unittest.TestCase):
    def setUp(self):
        self.now = t("2026-09-29 15:00")
        self.cond = [{"key": "stall:x:1", "kind": "stall", "notify": True, "title": "s", "lines": []}]
        a = {"kind": "new", "new_keys": ["stall:x:1"], "run": W.iso(t("2026-09-29 14:20")),
             "run_start": W.iso(t("2026-09-29 14:20"))}
        self.alert = cm(W.render_alert(a, self.cond, t("2026-09-29 14:20")), t("2026-09-29 14:20"), 999,
                        "github-actions[bot]", "NONE")

    def ops(self, extra, labels=("ops-alert",)):
        return [a["op"] for a in W.plan(self.cond, {"number": 999}, [self.alert] + extra, list(labels), self.now)]

    def test_unacked_escalates(self):
        self.assertEqual(self.ops([]), ["escalate"])

    def test_ack_comment_after_alert(self):
        self.assertEqual(self.ops([cm("Acknowledged, on it", t("2026-09-29 14:30"), 999)]), [])

    def test_ack_label(self):
        self.assertEqual(self.ops([], labels=("ops-alert", "ack")), [])

    def test_ack_before_alert_does_not_count(self):
        self.assertEqual(self.ops([cm("ack", t("2026-09-29 14:00"), 999)]), ["escalate"])

    def test_words_containing_ack_do_not_count(self):
        self.assertEqual(self.ops([cm("I'll get back to this, tracking", t("2026-09-29 14:30"), 999)]), ["escalate"])

    def test_stranger_ack_ignored_but_wds4_counts(self):
        self.assertEqual(self.ops([cm("ack", t("2026-09-29 14:30"), 999, "rando", "NONE")]), ["escalate"])
        self.assertEqual(self.ops([cm("ack", t("2026-09-29 14:30"), 999, "wds4", "NONE")]), [])


class TestPark(unittest.TestCase):
    def test_formats(self):
        cases = {
            "parked until 2026-09-30T08:00:00-04:00": t("2026-09-30 08:00"),
            "Parked until 2026-09-30T12:00Z (weekly quota)": t("2026-09-30 08:00"),
            "parked until 2026-09-30 08:00": t("2026-09-30 08:00"),
            "parked until `2026-09-30T08:00`": t("2026-09-30 08:00"),
            "parked until 2026-09-30": t("2026-09-30 00:00"),
            "Physics Lead parked until 2026-10-01T18:30-04:00 (re-posted)": t("2026-10-01 18:30"),
            "parked until 2026-10-01T18:30-0400": t("2026-10-01 18:30"),
            "parked until 2026-10-01T22:30:00Z": t("2026-10-01 18:30"),
            "parked until tomorrow": None,
        }
        for text, want in cases.items():
            got = W.parse_park(text)
            self.assertEqual(got, want, text)


if __name__ == "__main__":
    unittest.main()
