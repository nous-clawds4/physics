# Claude exploratory-critique cover: the Path of 42 question-graph pilot

Author of cover: Physics Lead (for David Strayhorn / Chief of Staff)
Date: 2026-10-04
**Not a review.** A brief for an **exploratory critique** of `public-papers/observer-space-framework/question-graph/` (Claude queue 008). No verdict (PASS / HOLD / FAIL) is asked for.

Claim check: every factual claim in this cover was checked against `main` by Literature (not the cover's author) before it was queued (see the note at the end).

---

## What the target is

The folder is a **pilot retro-map** of the framework paper's versions v0.3 to v0.7.1 onto a Path of 42 question graph: 9 questions and 21 answers (7 accepted, 9 rejected, 5 open; 30 nodes), and six version files (`versions/v0.3.yaml` … `versions/v0.7.1.yaml`), each listing the accepted answers that version rests on. It was written by Ontology (#199) and merged as `33c06d2` after Geometry's math and selection check (#200, PASS with fixes) and Literature's citation check (#202, HOLD narrow; all fixes applied before merge). One wording follow-up, #206, scoped the a-real-a / a-real-b Kretschmann (a) wording to the instance.

Read `question-graph/index.md` first: it gives the method, the rating scale, the node table, the selections, the "Rejected options by layer" list, and a "Gaps and unclear record" section. The method follows the infinite-harness Path of 42 doc and the viewer's data format, both linked from `index.md`.

**Everything in the folder records; nothing decides.** Every rating (q, a) and every hold level above L3 is a proposal pending David's signature. Two items already wait for David and are not yours to decide: raising `q-observer-object` to L1, and a retroactive sign-off on the Option F demotion (`a-option-f`, "Record unclear": David adopted F in #104; the demotion was recommended by Geometry in #118 and made in the v0.5 outline, #119, with no David signature found).

## What to check

| # | Question | What would count as a finding |
|---|---|---|
| 1 | **Faithfulness.** Does each node's rationale say what its cited sources say? Check the rejected answers most closely: their "why" and `reopen_if`. | A rationale or reopen condition that misstates, strengthens or weakens the record; a source that doesn't support the sentence citing it. |
| 2 | **Selections.** Does each `versions/*.yaml` select exactly the accepted answers that version of the paper (`../versions/v0.N-prose.md`) rests on? | A selection that is missing or adds a node; a synopsis that misdescribes what changed. |
| 3 | **Structure.** Is the graph well formed as a record? Are parents right, are distinct decisions merged into one node or one decision split, and is there a decision in v0.3–v0.7.1 that deserves a node but is missing (beyond those the "not mapped" list already names)? | A wrong parent, a merged or split decision, a missing decision, with its location in the versions. |
| 4 | **Neutrality.** Do the open nodes (`a-real-a`, `a-real-b`, `a-m1`, `a-m2`, `a-kretschmann`) and their rationales stay undecided with costs on both sides? Does any node let a Hope or an Open item read as a result? | A sentence that leans, or a status that overstates. |

Label each finding Substantive (it changes what a reader would take the record to say), Clarification, or Nit. Give the node id and, where you can, an exact OLD -> NEW.

**Separate part (optional, but useful).** The graph stops at v0.7.1. Since then, v0.8 (#183) and v0.8.1 (#205, current since #213) and the law-of-R scoping note (`reviews/law-of-R-scoping.md`, #178/#187/#204) were merged. List the decisions from that later record that an extension would need as new or changed nodes. List only; don't write the nodes.

## Out of bounds

- No choice between (M1) and (M2), no law of $R$, no T1–T3, Q-D1–Q-D5 or #139 (a)–(e) answer. Where the folder names these, check only that they are stated honestly.
- No Born rule, $|a|^2$ or $1/N$, and no Einstein-equation claim.
- **The rating scale and hold levels are David's call.** You may observe structural effects (`index.md` already records two: rejected and open answers share a = low, and a rejected answer high in the graph can outrank an accepted one lower down), but don't propose values or hold levels as rulings.
- Don't decide the two items waiting for David (above).
- No edits to the paper versions, the essays, Paper 1, or the folder itself.

## Please file

- Write the critique to `public-papers/observer-space-framework/reviews/question-graph-pilot-claude-opus-5.5.md`, headed "Verdict: none (exploratory critique)". Give findings to questions 1–4 in order, then the separate part, then anything you could not check, then provenance.
- Open one pull request against main containing only that file, titled "Exploratory critique (Claude Opus 5.5): question-graph pilot". Do not merge it.

## Claim check

Literature, `reviews/question-graph-pilot-claude-cover-claim-check.md` (#219): PASS. Its recommended C1 and optional C2 are applied here verbatim; C3 and C4 are applied to the queue prompt.
