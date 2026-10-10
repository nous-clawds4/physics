# Literature check: Born-rule litmus-test note (#248)

**Verdict: HOLD (narrow).** One string is required: the relay attribution in the Status line. One more is recommended (the open-call list) and one is optional. Everything else checks. **Heads read:** #248 head `01e6a35` (`notes/born-litmus-test.md`, 333 words by `str.split`; `reviews/born-rule-readiness.md`); base and main `f920ca3` (#246 merged), `versions/v0.9-prose.md` at `f920ca3`. I re-checked the head before filing.

## Findings

- **F1 (framing): PASS.**
  - The Status line says "open question" and "not a claim of v0.9 or of any version". The working answer is labelled L3, the same hold level the question-graph uses for "weakly held". It is never called an adopted criterion.
  - There is no (M1)/(M2), T1–T3, Q-D, #139 or (Z-*) pick, and no law of R is implied.
  - |psi|^2 appears only inside LT2's "not tuned until |psi|^2 appears". There is no Born, |a|^2 or 1/N result and no derivation claim.
- **F2 (relabel): PASS.**
  - The change from T1–T4 to LT1–LT4 is disclosed in the note's **Labels** line and in the pointer.
  - Each LT line carries "(David's Tn)". No stray T1–T4 refers to the litmus tests. The only other T-labels are v0.9 §11's T1–T3, named as distinct.
  - `git grep -E '\bLT[0-9]'` across the repo at `01e6a35` finds no other LT label (the only other hit is a binary PDF).
- **F3 (cross-references): PASS except F4 and F5.**
  - v0.9 §11 says "T1–T3 are the tensions named in *Mathematical Foundations* v0.3", which matches the note.
  - The "motivation clause" is §8.4. "Paper 1's trivial scheme" is §10 (the circularity wall).
  - `question-graph/index.md` is titled as a v0.3 to v0.7.1 retro-map, which matches the note.
  - #246 is merged as `f920ca3`. The note's description of `born-rule-readiness.md` uses the merged heading, "Gaps before a Born-type question can be posed".
  - The pointer sits inside the merged v0.9 refresh section, between its heading and its **Read at** line. It is dated, so it is acceptable, and the refresh's "nothing above this section is edited" still holds. The relative path `../notes/born-litmus-test.md` resolves.
  - The note does not cite `notes/zeno-mass-scoping.md`, so there was nothing to check there.
- **F4 (required): the attribution is not marked as relayed.** The Status line says "recorded at David Strayhorn's direction" and "Chief of Staff drafted it first". The PR body says "via CoS", but the note does not. "Drafted it first" also sits uneasily with "The wording is David's, unchanged". There is no record of the CoS relay in the repo: a `git grep` for litmus, Chief of Staff and "hold L3" finds only this note and unrelated workflow and README text. So the verbatim wording cannot be checked against a source here. String 1 marks the relay, says neutrally that it is not recorded, and keeps the drafting fact.
- **F5 (recommended): the open-call mapping.** "(J1)/(J2) and the cut (LT3)" pairs the jump-dominance constraint (§9, §11) with LT3's robustness under a change of cut. In v0.9, cut dependence sits in (M1)/(M2) and completed-versus-cut (§9, §11; C13, C14), not in (J1)/(J2). String 2 maps it there and adds the §8.4 motivation clause to LT2. This is note text, not David's test wording.
- **F6 (optional):** `notes/merw-litmus-scoping.md` is cited as "in preparation". No such file or branch exists on origin. String 3 says so.
- **F7 (guardrails): PASS.**
  - The note has none of the banned words: egalitarian, chi, 4-geon, spin-foam, cartoon or the GRW acronym. "How best" appears only inside David's quoted question.
  - There is no Everett-vs-Deutsch–Wallace framing and no Bell claim.
  - Paper 1 and `versions/` are untouched. The diff touches only these two files.
- **F8 (the readiness diff): PASS.** `born-rule-readiness.md` changes by exactly one pointer line and one blank line (`@@ -132,0 +133,2 @@`). Nothing else changes.

## OLD/NEW (file `public-papers/observer-space-framework/notes/born-litmus-test.md` at `01e6a35`; each OLD occurs once)

1. (required) OLD: `recorded at David Strayhorn's direction on 2026-10-10. The working answer below is David's, held as "strong opinion, weakly held" (**hold L3**); Chief of Staff drafted it first.`
   NEW: `recorded at David Strayhorn's direction, as relayed by Chief of Staff on 2026-10-10; the relay itself is not recorded in this repository. The question and the working answer below are David's as relayed, held as "strong opinion, weakly held" (**hold L3**); Chief of Staff drafted a first version.`
2. (recommended) OLD: `- Open calls that the tests touch: the law of R (LT2), (M1)/(M2) and the grain (LT3), and (J1)/(J2) and the cut (LT3). None is decided here.`
   NEW: `- Open calls that the tests touch: the law of R and the §8.4 motivation clause (LT2); (M1)/(M2), completed versus cut, and the grain (LT3). None is decided here.`
3. (optional) OLD: ``- `notes/merw-litmus-scoping.md` (in preparation), which``
   NEW: ``- `notes/merw-litmus-scoping.md` (in preparation; not yet in the repository), which``

I applied all three mechanically. Each matches once, and the note goes from 333 to 361 words.
