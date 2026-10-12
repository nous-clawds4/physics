# Geometry fidelity pass: consolidation note #372 (do not merge)

**Read at:** #372 head `07d8912` (`notes/creative/measurement-model-v0.md`), main `e41412b`.

**Scope.** This pass checks each claim in the note that is attributed to Geometry's reviews (#346, #352, #355, #359, #361, #364, #367, #370, and the one-line nesting answer) or that relies on them. Claims sourced only to other PRs (#362, #365, #368, #371) are checked only where they conflict with a Geometry result. The pass adds no new physics, applies nothing, and stays neutral.

**Counts.** 22 rows: OK 11; missing caveat 7; overstated 2; wrong 2.

**Most serious.**
- **l.51:** "the non-Hausdorff union is complete, and only a measure-zero set gets through neither". This conflicts with #367: in Misner, geodesics through the fixed point are incomplete in both extensions, so also in the union. It also uses a measure where #367 said "meagre".
- **l.42:** "none if π1 = Z/2". #364 said no *non-trivial* Type O class. A return in the trivial class, through G with no wrapping, can still be Type O.
- **l.15 / l.46:** #364 (d) is stated without its precondition, a slice S before the geon. That makes it contradict l.17 and l.69, where eternal geons have no S, and #370 says the timing result does not apply.

| Location | Claim (short) | Status | Suggested replacement string |
|---|---|---|---|
| l.14 | Type O replies count; Type F are correlations (#364) | OK | — |
| l.15 | Replies only after the observer passes a horizon; survival fixed by its own motion | missing caveat | "Where the geon forms after a period with a Cauchy surface, replies can only arrive after the observer has passed that horizon (#364 (d), sketch). Beyond it, whether the observer continues is fixed by its own motion within each world (Misner: Geometry's own computation, #367; Taub–NUT unverified). Stopping is not a branch (#367, #370, #371)." |
| l.16 | Narrows to exactly one world in finite time | missing caveat | "…for worlds with a closed repeating structure (cocompact Γ in a known cover) and exact displacement records, it narrows to exactly one in a finite time (#370, sketch; homogeneous covers need care)." |
| l.17 | Comparison works for eternal geons | OK | — |
| l.34 | Well-posedness conditions (#355) | OK | — |
| l.41 | Homotopy-invariant via w1; Type O = double-cover repair | OK | — |
| l.42 | "Type O returns exist iff w1 has nontrivial kernel; none if π1 = Z/2" | wrong | "Non-trivial Type O homotopy classes exist (topologically) iff ker w1 ≠ {1}; there is no non-trivial Type O class if π1 = Z/2. Whether Hadley geons realise any of them by a causal curve through the CTC region is unchecked (#364 (b))." |
| l.46 | No reply inside D⁺(S); observer's path depends on the extension | missing caveat | "If the host has a slice S before the geon, no reply can reach an observer still inside D⁺(S) (#364 (d), sketch; Hawking–Ellis §6.5 unverified). Measurements then happen beyond the observer's Cauchy horizon, where the observer's own path can depend on the extension. Without such an S (eternal geons) this timing result does not apply (#370)." |
| l.50 | Misner: Geometry's computation, not a verified source | OK | — |
| l.51 | Non-Hausdorff union complete; only a measure-zero set gets through neither | wrong | "Taub–NUT: the extensions are non-isometric (verified, #332). The dichotomy and the imprisoned geodesics are unverified (Misner–Taub 1969). In Misner (#367, Geometry's computation), geodesics through the boost's fixed point are incomplete in both extensions and in their non-Hausdorff union, and they form a meagre set (topological; no measure adopted). #371's claim about the union is not checked against this." |
| l.54 | Survival determined within each world | missing caveat | "Survival is determined within each world and varies between worlds (L38, L42; Misner by Geometry's computation, #367; Taub–NUT and Hadley hosts unverified)." |
| l.57 | Nesting, not crossing | OK | — |
| l.58 | Outcome is a class of branches, refining | OK | — |
| l.59 | Record = branch by definition is convention, not evidence | OK | — |
| l.63 | Γ fixed, and certifiably so, for any cocompact Γ | missing caveat | "…Γ is fixed, and certifiably so, once τ exceeds a generating set's displacements and about twice the quotient diameter, provided the record identifies each deck element from its arrival (#370, sketch; this supersedes #359's 'n ≤ 3')." |
| l.65 | Under the lock, the germ fixes the cover at τ = 0; Γ and the extension stay open | missing caveat | "…What stays open is Γ and the extension (#370). In the smooth case (relaxed lock), geometry outside J⁻(γ(τ)) is never fixed by germ and record (#346, #370)." |
| l.68–69 | Germ-based comparison; only #346 and #364 (d) need D(S) | OK | — |
| l.99 | Degenerate 0/1 counting shares | OK | — |
| l.102 | "Continuous families arise only for symmetric data" | overstated | "Continuous families arise for data invariant under a continuous symmetry, and possibly from continuous internal degrees of freedom such as spin or inelasticity (unverified) (#367). Generic isolation assumes transversality of the actual EKT map (unverified)." |
| l.105 | Linear-field uniqueness by Friedman & Morris | missing caveat | "Friedman et al. 1990 is verified from the abstract only (#364 (c)): linear fields behave benignly in the wormhole examples, and interacting systems can have multiple solutions. Linear uniqueness (Friedman & Morris) was unverified in #364; its status in #365 is as recorded there. Non-benign spacetimes may misbehave even for linear fields." |
| l.109 | #346 and #364 (d) "must be restated without D(S)" | overstated | "Eternal geons: #346's first-divergence argument and #364 (d)'s timing do not apply (no D(S)); replies are not barred before any horizon. Ensemble comparison by germ + record is unaffected (#370)." |
| l.111 | Non-Hausdorff union is a low-priority note only | OK | — (optional: add "the Misner union forks no single geodesic; under the lock the branches share germs along the path (#367)") |

**Not checked:** #362, #365, #368 and #371 as sources in their own right; §3's verbatim rulings, which do not rely on Geometry.
