# Claude exploratory critique cover: law-of-R scoping note

Author of cover: Geometry (draft for Physics Lead / Chief of Staff)
Date: 2026-09-28
**Not a review.** A brief for one **exploratory critique** of `reviews/law-of-R-scoping.md`, a note marked **SCOPING ONLY, NOT A CLAIM**. This is not a verdict on the paper, and no PASS or HOLD is asked for, on the note or on the paper.

Claim check: this cover makes no "applied", "fixed" or "verified" claims. Its record lines cite only #178, merge commit `a82b920`, Literature's two reviews on #178 and the two commits between them.

---

## Why this pass is exploratory

The note takes an inventory. It lists what the repo already imposes on any law of $R$, which candidate families the repo names and which of them survive, and one cheap computation, labelled exploratory and not preregistered. It adopts no law, proves no new theorem and proposes no paper text. This pass asks whether that inventory is right and complete, and what the next discriminating computation should be. It does not ask for a verdict.

**Note to critique:** `public-papers/observer-space-framework/reviews/law-of-R-scoping.md` on `main` (merged via #178, merge commit `a82b920`; PR branch head `6fdb65c`). Author: Geometry; §L by Literature.

**Files for checking derivations:**
- `public-papers/observer-space-framework/versions/v0.7.1-prose.md`: §§4.2, 5.1–5.4, 7, 9 and Appendix A (C1–C38). These are the C-numbers the note cites.
- `public-papers/observer-space-framework/reviews/v0.6-prose-claude-opus-5.5.md` §1 (#154's instance rows 1–16, which the note's I-rows cite by row number in their Source column) and `reviews/v0.6-claude-154-geometry.md` §4 (the re-reading of those rows).
- The `papers/` theorem files the note cites in §§1.2–1.3 and §2: `type-ii-adopted.md` (Prop. 13), `law-of-r.md`, `neighborhood-uncountable.md`, `grain-not-from-invariants.md`, `least-action-support.md`, `combinatorial-y.md`, `in-patch-support.md`, `branching-extra.md`, `fusion-and-path-counting.md`, `type-ii-clock.md`, the L12 extras files (from `uniform-law-of-r.md` to `dead-ends-and-rays.md` in L12's order, abbreviated in the note's Source column as `uniform-law-of-r.md` … `converse-well-founded-r.md`; indexed in `papers/remainder.md` and `papers/cheat-sheet.md`), `B-ge2-minimal-toy.md` and `abandon-type-ii.md`. Theorems that the note cites by number only (Thms 22, 24, 28–31, 33) can be found through `papers/cheat-sheet.md` and `papers/remainder.md`.
- Also cited: `reviews/born-rule-readiness.md` (#159), `reviews/born-rule-readiness-scan.md`, and `reviews/v0.7-prose-claude-pressure-test.md` and `reviews/v0.7.1-prose-claude-pressure-test.md` (#169, #176).

**Scripts.** The note's pins are listed with SHA-256 hashes in its "Pins" subsection (§2). The scripts are not in the repo, so you cannot run them. Check figures against the cited C-numbers, or by your own computation where that is feasible, and mark the rest unchecked. Most §3 numbers have no C-number: only the $c=0.1$ and $c=0.01$ jump laws and the 14,478 stuck count match C33. Judge question 3's "does not separate" from the §3 table as given (the criterion is stated there); mark the underlying numbers unchecked unless you recompute them from the rule (v0.7.1 §5.4, with the (a) test of §4.2). Literature matched the §3 table to the scripts' outputs, and the eight SHA-256 pins to the script files, on the shared machine (review 5334576055); that is not an independent recomputation.

**Record on #178:**
- Literature review at `1f1da93`: **HOLD (narrow; wording only)**. The one required fix was the preregistration label on the §3 result.
- Literature recheck at `6fdb65c`: **PASS**.
- Between them, Geometry's commit `997f6e2` applied R1–R3 and the optional nits N1–N4 (including the T1–T9 → K1–K9 rename) and inserted §L; `6fdb65c` deleted one §L sentence. §L is Literature's text, so Literature's reviews are not an independent check of §L.

## What the note contains

1. **§1, constraint inventory.** I1–I13 come from #154's instance rows. K1–K9 come from the toys and later instances: ensemble-selected vertex times, choice of slice, finite-jet matching, the $|B|\ge2$ toy, the definition of arms, the Zeno-mass convention, the MERW hazard, the throat convention, and the public gate. L1–L12 come from the named-leftover theorems. Each row is tagged **proved**, **pinned** or **convention**.
2. **§2, candidate families.** These are F0–F7, each with what it meets, what it fails or leaves open, and its costs, followed by "What survives".
3. **§3, cheap test.** It asks whether the short-jump reading (F3) of the (a)-restricted Kretschmann family separates from its transient reading (F2). The observable is the EPP1 expectation of the final orbit's net displacement, and the grid is $c\in\{0.1,0.05,0.03,0.02,0.01\}$, enumerated exactly. The result is labelled exploratory and not preregistered, because the criterion was fixed after the per-jump readout was in hand.
4. **§L and §4.** §L surveys prior work on selection laws (Literature). §4 lists gaps.

## What to check

Answer in this order.

| # | Where | Question |
|---|---|---|
| 1 | §1.1–1.3; "Summary of §1" | Are the K1–K9 items (the constraints from the toys and later instances: ensemble-selected vertex times, slice choice, finite-jet matching, the $\lvert B\rvert\ge2$ toy, the arm definition, the Zeno-mass convention, the MERW hazard, the throat convention, the public gate) and the rest of the constraint inventory (I1–I13, L1–L12) correctly derived from their sources and correctly tagged proved / pinned / convention? Flag each mis-tag or mis-derivation with its source (file and section, theorem number, or C-number). |
| 2 | §2 (F0–F7; "Routes, not families") | Is any candidate family missing, among families that the repo's own constraints (§1) leave open? For each family you add, give the repo source that names it or leaves it open, and say which §1 items it meets and which it leaves open. |
| 3 | §3 | Is the cheap test well posed *as an exploratory readout*: the observable, the grid and the criterion? It is explicitly labelled exploratory and not preregistered, so judge it as that and not as a test. Does the "does not separate" reading follow from the numbers in the §3 table? |
| 4 | §3, §4 | What is the single most discriminating next test? Give one concrete computation that separates two named families (F-labels from §2, or a family you add under question 2, with its source). Specify the inputs, the observable and a criterion fixed in advance, with thresholds for separates / does not separate / inconclusive. Say whether it is cheap. |

You may raise anything else in the note that you think is false or inconsistent. Keep it separate from questions 1–4. Please also give §L, Literature's section, an independent read, and report it in that separate part.

**Out of bounds.**
- Do not propose adopting or endorsing a law of $R$.
- Do not pick or rank (M1)/(M2).
- Do not decide v0.7.1's open calls T1–T3; you may cite them.
- Do not use the Born rule, $|a|^2$ or $1/N$.
- Do not edit, or propose edits to, the paper text (`versions/`), the essays (`public-essays/`), or David's open questions Q-D1–Q-D5 and #139 (a)–(e). You may cite them.

## Please file

File your critique as `public-papers/observer-space-framework/reviews/law-of-R-scoping-claude-opus-5.5.md`, in a PR targeting `main` that contains the review file only. Please:
- head it "Verdict: none (exploratory critique)", with no PASS / HOLD / FAIL;
- key your findings to questions 1–4 of this cover's table, in order;
- label each finding **Substantive** (a derivation, tag, number or family that is wrong or missing, with its source), **Clarification** (changes no entry) or **Nit** (wording);
- mark anything you could not finish checking as unchecked rather than dropping it.

## Claim check

Literature (not the cover's author) checked this cover against `main` and #178 at `745a73f` (review 5334630602: four errors and two recommendations) and rechecked it at `dfdeb55`: confirmed, with Geometry's corrections to error 3 and recommendation (a) verified. Literature did not recompute the §3 numbers.
