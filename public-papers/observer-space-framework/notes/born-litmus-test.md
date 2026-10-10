# Open question: the Born-rule litmus test

**Status:** open question, recorded at David Strayhorn's direction, as relayed by Chief of Staff on 2026-10-10; the relay itself is not recorded in this repository. The question and the working answer below are David's as relayed, held as "strong opinion, weakly held" (**hold L3**); Chief of Staff drafted a first version. It is **not a claim of v0.9** or of any version. Nothing in `versions/` or the essays is edited. It looks forward: it is not part of the v0.3–v0.7.1 retro-map in `question-graph/`.

**Labels.** David's tests are numbered T1–T4. This note writes them **LT1–LT4** (litmus tests), because T1–T3 already name the *Mathematical Foundations* v0.3 tensions in v0.9 §11. The wording is David's, unchanged.

## The question

> How best do we tell whether the Born rule genuinely emerges from the framework, rather than being written in by hand? (the litmus test)

David calls this an important question to answer.

## Working answer (L3, David, 2026-10-10)

Genuine emergence needs YES on all four:

- **LT1 (David's T1) Identity:** the squared quantity is the same object that does amplitude work elsewhere in the theory (it superposes, evolves linearly, interferes); if it appears only in the counting step, the square is a coincidence of form.
- **LT2 (David's T2) Prior inputs:** the law of R, the slice and the measure are fixed for independent reasons, ideally within a class named in advance, not tuned until |psi|^2 appears (the motivation clause; this is the contrast with Paper 1's trivial scheme).
- **LT3 (David's T3) Robustness:** the result survives refining the grain, changing the cut, and irrelevant further splitting.
- **LT4 (David's T4) Novel prediction:** it gives correct weights in a second, unrelated setup, or interference that was not put in.

**Scope and outcomes (David, 2026-10-10, about 11:39 ET, given directly to the Physics Lead in chat and relayed here; the exchange is not recorded in this repository; part of the L3 answer; this revises the earlier same-day reading, in which the test applied only once a Born-type result was claimed).** The test asks one question: was the Born rule put in by hand? **Failure** means circular reasoning that injects the Born rule directly, in whole or in part. The test can therefore fail before the full Born rule is claimed. It cannot be passed on a technicality, such as "we did not actually derive the Born rule, because our rule differs from it in some esoteric way". **Success** means no circularity has been detected. It does not prove emergence.

**Pre-emptive use (David, 2026-10-10, about 11:20 ET, given directly to the Physics Lead in chat and relayed here; the exchange is not recorded in this repository; part of the L3 answer).** The test can also be run when there are only hints of a Born rule, such as the squared eigenvector of maximal-entropy random walks (MERW) (`notes/merw-litmus-scoping.md`). If a reviewer raises circularity, even prematurely, the record then has an answer ready. Run this way, the test can detect a partial injection (a failure). It cannot pass a claim that has not been made. For each LT, it records whether there is yet anything to check and what a later claim would have to show.

## Substitution test (David, 2026-10-10, about 11:39 ET, given directly to the Physics Lead in chat and relayed here; the exchange is not recorded in this repository; part of the L3 answer; proposed, not yet analysed formally)

Suppose the manuscript were rewritten with a different rule in place of the Born rule. Imagine, for example, that experimental theorists told the authors of the decision-theoretic (Deutsch–Wallace) derivation that experiment supports a different rule, and that the authors believed them. What else in the manuscript would need to change? Could the new rule simply be slid in place of the old one, with a footnote saying "this equation has been justified by experiment, so that's the one we are deriving now"?

If it could be slid in with nothing else changing, the rule was put in by hand, and the test fails. If a derivation is genuine, swapping the rule should break something upstream: an input, a lemma or a symmetry.

**David's conjecture (unanalysed):** the decision-theoretic derivation would fail this test, and this framework would pass it. Neither half is checked here. How the substitution test relates to LT1–LT4 (for example, whether it sharpens LT2) is open.

## Where it connects

- `reviews/born-rule-readiness.md`, which maps the gaps before a Born-type question can be posed (v0.9 refresh, 2026-10-10).
- `notes/merw-litmus-scoping.md`, which scopes what a Born-type claim through the MERW squared-eigenvector density would have to show under LT1–LT4.
- Open calls that the tests touch: the law of R and the §8.4 motivation clause (LT2); (M1)/(M2), completed versus cut, and the grain (LT3). None is decided here.
