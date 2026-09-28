# Observer space and graph joins (public paper)

This folder holds the **public-facing** framework paper intended for the wider physics community.

It is deliberately **not** under `papers/`, which is crowded with in-house notes (lock leftovers, kill-passes, internal theorems). Those remain internal. This paper is the readable cut of the ontology and launching pad.

## Layout

| Path | Role |
|---|---|
| `versions/` | Numbered drafts (`v0.1-outline.md`, …, `v0.7-outline.md`, …) |
| `reviews/` | External and in-house reviews; each file **must** name the version it reviews |

Living working definitions stay in the repo-root file [`mathematical-framework.md`](../../mathematical-framework.md). Where that file disagrees with a numbered draft, the draft wins for review purposes.

## Status

- **Current draft:** [`versions/v0.6-prose.md`](versions/v0.6-prose.md) (Claude #154 PASS; Geometry #155)
- **In review:** [`versions/v0.7-prose.md`](versions/v0.7-prose.md) (prose panel: Geometry, Literature; then a Claude review). It becomes the current draft only on adoption.
- Latest outline: [`versions/v0.7-outline.md`](versions/v0.7-outline.md) (merged #156; panel: Geometry #157, Literature #158)
- Prior outline: [`versions/v0.6-outline.md`](versions/v0.6-outline.md) (panel: Geometry #131, Literature #132, Ontology #133)
- Prior prose: [`versions/v0.5-prose.md`](versions/v0.5-prose.md)
- Reviews: see [`reviews/`](reviews/)
- Born rule and Einstein’s field equations are **goals**, not theorems of this version.
- Do not treat this folder as a claim that either has been derived.

## How to review

See [`reviews/README.md`](reviews/README.md).