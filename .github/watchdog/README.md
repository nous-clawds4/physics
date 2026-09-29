# Watchdog and merge gate

## Watchdog (`.github/workflows/watchdog.yml`)

Runs every 15 minutes (and on demand from the Actions tab). It looks for two things:

1. **Runner stall.** The most recent `runner: started <file>` comment on #146 has no later
   `runner: finished <file>` and is more than 45 minutes old.
2. **Quiet loop.** No commit on main, no PR opened or updated, and no issue or PR comment for
   more than 3 hours. A comment saying `parked until <ISO time>` (for example
   `parked until 2026-10-01T09:00-04:00`) silences this until that time, as long as it is the
   most recent comment in the repo. A time with no offset is read as Eastern time. The quiet
   check only alerts from 08:00 to 23:59 ET, or at any hour while the runner is mid-job.

When either is true, the watchdog keeps one open issue labelled `ops-alert`, comments there with
links to the evidence, and gives the issue a fresh assignment to nous-clawds4 (unassign, then
assign) so Chief of Staff wakes up. An ongoing, unacknowledged condition is re-posted at most once
an hour. To acknowledge, add the `ack` label or comment with the word "ack" after the alert.
If an alert stays unacknowledged for 30 minutes, it posts one comment mentioning @wds4.
When everything clears, it comments "cleared", removes `ack`, and closes the issue.

Only comments from the repo owner/collaborators or from wds4 count (for acks, park notes, runner
lines, and activity), because the repo is public. The watchdog's own comments never count as activity.

Thresholds are the `env:` values at the top of the workflow.

Tests with fake inputs: `python3 .github/watchdog/test_watchdog.py -v`.
Local dry run against the live repo (uses the `gh` login, changes nothing):
`WATCHDOG_DRY_RUN=1 python3 .github/watchdog/watchdog.py`.

## Merge gate (`.github/workflows/merge-gate.yml`)

The `merge-gate` check fails when a PR title or body contains "do not merge", "do-not-merge",
"not for merge" or "don't merge" (any case), or when the PR has the `hold` label.

A repository ruleset on the default branch (id 24215274, Settings > Rules > Rulesets) requires this
check from GitHub Actions (not strict, no bypass actors), so a PR
cannot be merged while it fails. A required check also rejects direct pushes to main (GitHub checks the
pushed commit, which has no passing check yet), so all changes to main now go through pull requests.
