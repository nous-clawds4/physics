# Literature prior-art and taste pass: Creative batch 01 (#333)

**Reviewer:** Literature. **Date:** 2026-10-12. **Record type:** review record; applies nothing; do not merge.

**Heads.** #333 head `fd3a904` (open; `creative/batch-01.md`, `creative/ledger.md`); main `e41412b`. No earlier review of #333 exists.

**Marks.**
- **V-text:** text or abstract checked, here or in #332 / #330.
- **V-meta:** bibliographic data and topic only.

## Verdict: PASS with one fix (R1) and two notes

### Per-set verdicts

| Set | (a) Already known? | (b) Already killed by the record? | (c) Sneaks the answer in? |
|---|---|---|---|
| 1 Sheets | **Partly.** Branched covers and conical defects are standard: cosmic strings (Vilenkin 1981, V-meta), and Geroch–Traschen 1987 shows strings are not distributional sources (V-text, #332). The use as a branching rule for observer motion has no owner found. | **No.** It is #331 A, live, with #332 R3/R4/N1 costs, and it is carried correctly. | **No**, provided "equal weight per sheet" is not added (T4). Watch the amplitude hook (#332 R4: Schulman 1968 V-meta; Laidlaw–DeWitt 1971 V-text) and the framing (#332 N1: Belnap 1992 V-meta, McCabe 2005 V-text). |
| 2 Jet, not germ | **Yes, the math.** In smooth or Gevrey classes the jet does not fix the germ (Borel's lemma; Denjoy–Carleman, Hörmander *ALPDO I* §1.3, V-meta). Agree-then-diverge is Choquet-Bruhat–Geroch 1969 (V-meta) and Chruściel–Isenberg 1993 (V-text). The jet-as-state branching rule has no owner found. | **Collides with a lock.** Paper 1: "Smooth is not enough. In the smooth category any jet is realized by some smooth metric, so the jet does not pick a unique lump." It also says "The infinite jet, analyticity, and the unique simply-connected patch are locked." A non-quasianalytic host reopens that lock, which is David's call, not a tweak inside v0.10.1. v0.10.1 §8.1's CWS singleton uses (E1)/(E2), and those coincide only for analytic paths, so the batch's "unchecked" is right. | **No count yet.** But it is a continuum (T4 high risk, as the batch says). |
| 3 Loops in $V$ | **Template known.** Echeverria–Klinkhammer–Thorne, *PRD* 44, 1077 (1991) (V-meta). Friedman et al., "Cauchy problem in spacetimes with closed timelike curves", *PRD* 42, 1915 (1990) (V-meta). Novikov's self-consistency principle. Consistency loops in state space rather than spacetime: no owner found. | **No.** Self-targets are on record (v0.10.1 §11; C10 points there), and the law of $R$ is open. #315 is untouched, since no topology is needed to state a loop condition. | **Not yet**, because it is undefined. **Watch:** EKT's own follow-ups weight the multiple consistent histories by a sum over histories. Importing that weighting would be borrowed quantum structure (cf. #332 R4). Counting solutions without weighting stays clean. |

### Citations and pointers checked (all accurate except R1)

- #331 §0/§2/§4 and #332 R1–R4/N1 are characterised correctly. That includes the #332 corrections (Gevrey is not doing the work; host versus motion).
- These v0.10.1 pointers are correct:
  - §8.1 CWS singleton, (E1)/(E2);
  - §8.2 Option E residue, and finite-$k$ "cannot create a branching edge" (C27);
  - §11 self-targets.
- infinite-harness `docs/lessons/creative-tweaks.md` exists. It is relayed and not signed, and its four taste tests and its Nash/Clarke ant example match the ledger. The batch paraphrases David and does not quote him.
- Ledger L4 and L6 kill reasons match the record. L5's credit line matches #332.

### R1 (claim overstated)

L10 is complex monodromy where real-path continuation stays unique. #331 §0 and #332 R2 speak only about continuation along a real path. So they do not contradict L10, and the ledger itself says "Probably fails".

OLD:
~~~
L10 complex monodromy (contradicted by #331 §0 / #332 R2)
~~~
NEW:
~~~
L10 complex monodromy (probably fails: #331 §0 / #332 R2 cover real-path continuation only; unchecked)
~~~

### Notes (no string)

- **N1, label collision.** Taste tests "T1–T4" collide with #301's topology options (T0)–(T4) and with David's T1–T4, which the litmus note writes as LT1–LT4 for this reason. Consider "TT1–TT4".
- **N2, sources.** Entries marked **CL** in the ledger have no literature check by their own statement. This pass covers L8 (Set 2) and L9 (Set 3) only at the prior-art level above.

### Guardrails

Both files are clean:
- No forbidden Greek letter or its TeX macro.
- No Born, $|a|^2$ or $1/N$ result.
- No Everett or many-worlds framing; Everett-style branching is only flagged, citing #332 N1.
- No topology, (M1) or (A) pick.
- `versions/` and Paper 1 are untouched.
