# Observer space and graph joins (public paper)

This folder holds the **public-facing** framework paper intended for the wider physics community.

It is deliberately **not** under `papers/`, which is crowded with in-house notes (lock leftovers, kill-passes, internal theorems). Those remain internal. This paper is the readable cut of the ontology and launching pad.

## Layout

| Path | Role |
|---|---|
| `versions/` | Numbered drafts (`v0.1-outline.md`, …, `v0.7-outline.md`, `v0.7-prose.md`, `v0.7.1-prose.md`) |
| `reviews/` | External and in-house reviews; each file **must** name the version it reviews |

Living working definitions stay in the repo-root file [`mathematical-framework.md`](../../mathematical-framework.md). Where that file disagrees with a numbered draft, the draft wins for review purposes.

## Status

- **Current draft:** [`versions/v0.7.1-prose.md`](versions/v0.7.1-prose.md) (patch of v0.7 prose with the #168/#169 fixes; panel check of the diff PASS: Geometry #171 at `36f7986`, Literature #172 at `193e7a2`, later nits checked by Literature; targeted Claude re-review queued as `ops/claude-queue/004-v0.7.1-prose.txt`)
- Prior prose: [`versions/v0.7-prose.md`](versions/v0.7-prose.md) (prose panel: Geometry #162 PASS with notes, Literature #161 PASS with notes; fixes #163; external review: Claude #168 HOLD (narrow); Geometry pressure test #169)
- Latest outline: [`versions/v0.7-outline.md`](versions/v0.7-outline.md) (merged #156; panel: Geometry #157, Literature #158)
- Prior outline: [`versions/v0.6-outline.md`](versions/v0.6-outline.md) (panel: Geometry #131, Literature #132, Ontology #133)
- Earlier prose: [`versions/v0.6-prose.md`](versions/v0.6-prose.md) (Claude #154 PASS; Geometry #155); [`versions/v0.5-prose.md`](versions/v0.5-prose.md)
- Reviews: see [`reviews/`](reviews/)
- Born rule and Einstein’s field equations are **goals**, not theorems of this version.
- Do not treat this folder as a claim that either has been derived.

## How to review

See [`reviews/README.md`](reviews/README.md).