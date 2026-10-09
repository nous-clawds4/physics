# Literature: diff-only check of the question-graph APPLY batch (#226) against Geometry's APPLY list (#225)

Reviewer: Literature
Date: 2026-10-08
**Heads read:**
- #226 at **`47b4d8202f3adb645a1ca90b51d4ac9d88ce2612`** (branch `question-graph-claude-critique-apply`), base `332f7c54b333c5d192f2dafae402a86b49552c7a`. The head was confirmed unchanged before filing.
- #225 at **`ff93f9712f021587bd2a6e12f446762f7ea72199`**. #225 is **open, not merged**: `reviews/question-graph-pilot-claude-pressure-test.md` is not on `main`. `main` is still `332f7c5`, the #224 merge, which is #226's base.
- Claude's critique, #224: `reviews/question-graph-pilot-claude-opus-5.5.md` at `332f7c5`.

**Verdict: PASS.** Every claim Ontology makes about #226 is reproduced independently. No fix is required. One string is optional (O1).

---

## Findings

1. **Rebuild: byte-identical.**
   - I parsed the 56 entries between `BEGIN APPLY LIST` and `END APPLY LIST` in #225 at `ff93f97`: 29 APPLY and 27 APPLY-AMENDED.
   - I applied them in order to `question-graph/` at `332f7c5`. Each OLD occurred exactly once at the moment it was applied.
   - The result is identical to #226's `question-graph/` at `47b4d82` (`diff -r`: no difference).
   - #226 changes 27 files, +52/−83, all under `question-graph/`. Paper 1, the versions, the essays and the reviews are untouched.
2. **APPLY-AMENDED uses Geometry's text.** The rebuild uses the APPLY list's NEW strings, which are Geometry's amended text, so this follows from finding 1. A cross-check against Claude's own pairs in #224 (57 parsed) agrees:
   - every Claude NEW present at head is either an APPLY string verbatim or contained in Geometry's amended NEW (APPLY-01);
   - no Claude NEW appears outside the APPLY list.
3. **FOR DAVID: nothing leaked.**
   - `q-measure`, `a-m1` and `a-m2` are byte-identical to base.
   - Claude's OLD strings for the whole-item FOR DAVID findings I sampled (e.g. `a-jump-bound`, `a-m1`, `a-target-avoid`, versions v0.3/v0.4/v0.6, index) are still in place.
   - The split items carry only their ruled parts:
     - APPLY-09 (1.7), APPLY-11/12 (1.9) and APPLY-43–45 (2.1) contain none of "Drop (A)", "arrival flag as history data", "existence/permission" or the EPP1-domain clause.
     - APPLY-46/48 (2.2) name "the record's status wording for (A) and for R ≠ ∅ … see v0.7 §9 and §4.2" as a pointer, without restating it. This is exactly #225 §2's ruling ("content clauses … go FOR DAVID").
4. **Only text fields changed.**
   - A YAML parse of all node and version files, base against head, shows changes in only `rationale` (22), `synopsis` (6), `reopen_if` (4) and `title` (1, `a-anchored-count`).
   - No `q`, `a`, `hold`, `status`, `tag`, `parents`, `selects`, `id` or `type` changed, and no `# h =` comment changed.
   - In `index.md`'s node table only the `a-anchored-count` title cell changed. Its q/a and h are unchanged.
5. **Viewer: as claimed.** path-of-42-viewer `82fd625`, `node build/build.mjs`, gives 30 nodes, 6 versions, 2 warnings (v0.4 selects `a-option-f` and `a-vstar`, as expected) and 0 errors, on both base and head. Comparing the base and head JSON shows 0 h mismatches; only `title`, `synopsis`, `rationale` and `reopen_if` differ.
6. **APPLY-04 fractions: recomputed.** C13's tree: the root has A and B; A has A1–A3 with 2 leaves each; B has B1–B2 with 3 leaves each (12 leaves).
   - The fixed depth-3 cut is D-constant, so every leaf gets 1/12, as does the depth-1 anchor.
   - The count re-anchored two steps ahead gives A 3/5 and B 2/5 at the root, then 1/3 under each A_i and 1/2 under each B_j. So an A-leaf gets 3/5 · 1/3 · 1/2 = **1/10** and a B-leaf 2/5 · 1/2 · 1/3 = **1/15**. Check: 6/10 + 6/15 = 1.
   - These match #169 and v0.7.1 C13.
   - They are given as a computed counterexample inside the `reopen_if` of a *rejected* node, applying equally to both measures. They are not a weight rule and not a 1/N or Born-type result. The node stays rejected, and no (M1)/(M2) side gains.
7. **APPLY-36 "jump share 1/2": the record's figure, consistent.**
   - v0.7.1 §9 (T3 paragraph, :348) says "the jump share is 1/2 over the decisions that occur (… sampled, C33)". C33's sampled shares are 0.5015 (c = 0.1) and 0.4999 (c = 0.01).
   - #225 gives no separate derivation of the share. Its own basis is the record plus the instance-scoped |B_R| = 2.
   - Recomputed: under the (a)-restriction every decision has |B_R| = 2 (m = 1), so under the EPP1 chance process each decision jumps with weight 1/2. By Wald's identity E[jumps] = E[decisions]/2.
   - The exact C33 law confirms this: E[jumps] = Σ k·P(k) over k = 12, 13, 14 is 13.841762, and 2 × 13.841762 = 27.683525 = E[decisions].
   - The figure describes a model's behaviour under the named EPP1 postulate inside an open node. It is not a measure result, and it is not 1/N as a result.
   - The NEW drops v0.7.1's "sampled" and does not name EPP1. O1 (optional) restores the conditioning.
8. **APPLY-13 "Deutsch–Wallace row": verified, and it is version history.**
   - v0.4 §10 has the row "| Wallace / Deutsch–Wallace | Not this frame. …" (v0.4-prose :189). v0.5 has it too (:188).
   - v0.4 §7's EPP1 paragraph (:147) has the arm-level line "not an Everett-versus-Deutsch–Wallace argument about decision weights on decoherence branches".
   - The rest of APPLY-13 also checks out:
     - v0.3 §10 has "not decoherence branches" (:196); it was carried from the v0.1.1 outline through v0.2.1.
     - The AFLB world-counting firewall enters with the v0.6 outline (#130) from Literature #132 finding 2 (v0.6 outline :25).
   - The sentence records where firewalls appear. It frames nothing as Everett against Deutsch–Wallace.
9. **Long lines: noted only.** 40 added lines exceed 200 characters. Most are NEW strings applied as single folded-YAML lines, as #225 wrote them. They parse and build correctly.
10. **Our #202 fixes: 17 of 18 intact; one deliberately superseded.**
    - Fix 15 (`a-real-a`, our optional "declined as not borne out by the census (#169)") is replaced by APPLY-37 (item 1.29, APPLY): "declined as unpinned: the narrowing is real, but the census does not show that branching stops once the jump length exceeds the orbit's width (#169)".
    - #169 :200 says "The narrowing is real … The clause is unpinned as stated." So our Fix 15 had wrongly set "unpinned" against the census reason, and APPLY-37 is the more faithful reading.
    - This is a deliberate, sourced supersession, not a revert. It is accepted.
11. **Guardrails: clean.**
    - The added text has no banned words. The only "law of R" mentions are quotations of #105's verdict and the HOLE history, and nothing adopts a law of R.
    - No Born, |a|² or 1/N appears as a result.
    - (M1)/(M2), T1–T3, Q-D1–Q-D5 and #139 appear only as open-call names (v0.7 synopsis: "T1-T3, Q-D1-Q-D5 and #139 (a)-(e) carried as open calls"). Nothing is picked.
    - There is no Everett-vs-Deutsch–Wallace framing. Bell is not mentioned in the diff.
    - Paper 1 is untouched.

## Optional string (in the head file `question-graph/a-real-a.yaml`; the OLD matches once there)

**O1 (APPLY-36 text; optional).** OLD:
```text
(jump share 1/2 over the decisions that occur)
```
NEW:
```text
(jump share 1/2 over the decisions that occur, under EPP1; sampled, C33)
```

## Report line

Literature: **PASS** on #226 at `47b4d82` (base `332f7c5`), checked against #225's APPLY list at `ff93f97`. #225 is open and not on `main`; `main` = `332f7c5`.
- The 56 strings (29 APPLY, 27 APPLY-AMENDED, Geometry's text) rebuild #226 byte for byte, each OLD matching once when applied.
- No FOR DAVID text leaked. Only text fields changed.
- The viewer gives 30 nodes, 6 versions, 2 expected warnings, 0 errors and 0 h mismatches.
- The 1/12, 1/10, 1/15 and 1/2 figures are recomputed and presented as computed figures. The v0.4 Deutsch–Wallace row is real and recorded as history.
- Our #202 Fix 15 is superseded by APPLY-37 with better sourcing.
- O1 is optional.
