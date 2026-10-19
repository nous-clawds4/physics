# The weight gap (#427's honest gap): a clean negative and a well-posedness repair (Geometry draft, workstream (C))

**Do not merge. Paper only.** Geometry draft, 2026-10-19, tasked by Physics Lead at 1:13 PM ET (Lead tasking under David's delegation, relayed; not David's words). Stacked on #444 (creative/detector-funnel-record at 8e8000e). Pins: #427 head 5bd192e, #444 head 8e8000e. #427 and #444 are not edited. Nothing is adopted.

## Plain summary (for David)

As #427 states it, the question of what weight exact-closure worlds get is ill-posed, because it needs a reference measure on route data and nothing fixes one. Each candidate tested (counting, 1/|Aut|, frame-lift signs, MERW, Euler characteristic e(W), entropy-max) fails T2 on at least one input: a cutoff, a coupling constant, a fixed ambient graph, or the unspecified (M1) values. The question becomes well-posed if the set of worlds is countable and the setup is finite; exact closure is then a combinatorial constraint, not a measure-zero event. The cutoff, the (M1) values and μ stay free, and countability is a hypothesis.

## Geometry's draft (verbatim from https://github.com/nous-clawds4/physics/pull/444#issuecomment-6272908761)

> Attribution: Geometry draft, 2026-10-19, tasked by Physics Lead at 1:13 PM ET (Lead tasking under David's delegation, relayed; not David's words). Text below is Geometry's, unedited apart from heading levels and one edit Geometry itself requested (see change log).

**Geometry, workstream (C): the weight gap (#427's honest gap).** Draft note text for Creative Lead to open as a stacked do-not-merge PR. Paper only; nothing is adopted. Classical only, no Born claim, μ open, (M1) untouched, 1(a) and the write rule not adopted, CTCs adopted, spin-½ adopted for fermions, species conservation not adopted, R-geon/R-frame open, (F)/(W) open. No ħ, measure or phase rule is put in. Pins: #427 head 5bd192e, #444 head 8e8000e.

### Result in one paragraph
**Clean negative, plus a well-posedness repair.** As #427 states it, "the weight of exact-closure worlds" is ill-posed: it asks for a ratio between a codimension ≥ 1 set and its complement, and that ratio depends on a reference measure on route data, which nothing fixes. No candidate tested here (counting, automorphism-symmetric, frame-lift signs, MERW, Euler characteristic e(W), entropy-max) gives a weight with nothing put in by hand. Each fails T2 on at least one input: an exhaustion order, a coupling constant, a fixed ambient graph, or the unspecified (M1) per-vertex weights. The question becomes well-posed once worlds form a countable set (countability of worlds is assumed here; whether the lock supplies it is open). Closure is then an exact combinatorial constraint, not a measure-zero event, and the "zero weight from smoothness" argument no longer applies. What remains free is a single input: how to compare infinite counts (a finite setup or an exhaustion), together with the (M1) weights themselves. That is a sharper gap than #427's, not a closed one.

### 1. The object (Step 1)
- **Object:** a weight w on worlds, restricted to the set C(S) of exact-closure worlds for a setup S.
- **Domain:** C(S) ⊂ W(S), the worlds compatible with S. Under the 5:14 PM definition (adopted 5:17 PM, #427 §3a), every virtual pair is exact, so C(S) is the set of worlds containing at least one virtual pair.
- **Codomain:** [0, ∞) for a weight, or ℝ if signs are allowed (§2.3). A probability needs normalization, and none is available yet (§2.1).
- **Fixed by the framework:** the lock (real-analytic jet observers); exact closure (a law, #427); CTCs adopted; spin-½ for fermions; species conservation not adopted, so C(S) includes worlds where species change; the frame lift ±1 on every loop (#434).
- **Chosen but not specified:** (M1) per-vertex weights at L3 (David's choice, strong opinion weakly held; the values are not given).
- **Free:** μ; any reference measure on route data; any exhaustion or order on W(S); 1(a) and the write rule (not adopted); R-geon vs R-frame; (F) vs (W).
- **Reading:** Step 1 uses neither (F) nor (W). Under (F) the detector restricts C(S) (#444 funnel). Under (W) the detector constrains nothing (Reading A) and C(S) is larger. The problem has the same form in both readings.

### 2. Candidates (Step 2), judged against T1–T4
**2.1 Counting / uniform on a countable C(S).** If W(S) is countable (assumed here; whether the lock supplies it is open), counting is canonical up to an overall scale (T2 passes on its inputs). It fails if C(S) is infinite: then the closure-versus-pair-free ratio is ∞/∞. Choosing a cutoff (by size, by order or by vertex count) is an input put in by hand. **Verdict:** canonical only for a finite S. Applies to both (F) and (W).

**2.2 Automorphism-symmetric (1/|Aut|, groupoid counting).** This is fixed by the combinatorial structure of a world, so no tuning is involved. It is a refinement of 2.1 and inherits the same normalization failure. It also shifts weight toward asymmetric worlds, with no independent reason that this matters for T3/T4. **Verdict:** same as 2.1. Applies to both readings.

**2.3 Frame lift ±1 as a signed weight.** The sign is fixed by topology (#434: the frame lift; G3: the Dirac box's −1). Signs alone only give magnitudes once a magnitude is supplied, and that magnitude would come from 2.1 or 2.2. A signed sum of counts is a cancellation statement, not a weight: it can be negative, and it is not a measure. Adding a square to recover positivity is squaring by hand. **Verdict:** not a weight; it is input to one. Under R-geon with the core's class this also depends on #434 §7's open shadow-map item. Applies to both readings.

**2.4 MERW (maximal-entropy random walk).** This is the one place where a square is forced. The stationary weight on a fixed graph G is ψ_i², the product of the left and right Perron eigenvectors, so no square is chosen. Its costs:
- (a) It needs a fixed ambient graph G, but worlds are not walks on a given G (the stage is all there is).
- (b) With (M1) weights the transfer matrix contains those weights, so the result is only as fixed as they are, and they are unspecified.
- (c) It weights paths in the long-length limit, not closure worlds.

**Verdict:** fails T2 on G and on (M1). Worth recording as an example of a square the geometry forces in a different setting. No Born link is claimed. It is closest to (F), where the detector fixes part of G.

**2.5 Euler characteristic e(W).** For closed odd-dimensional slices, e = 0, so it is useless on 3-slices. On a 4-dimensional world W, e(W) is an integer and is fixed by topology. A weight exp(λ e(W)) needs λ, which is a tuning constant and fails T2. Using e(W) directly gives a signed integer and runs into the problems of 2.3. **Verdict:** fails T2. Applies to both readings.

**2.6 Entropy-max.** This needs a reference measure and constraints. With counting as the reference and no constraints it reduces to 2.1. Any constraint (fixing ⟨N_pairs⟩, for example) is tuning toward the target. **Verdict:** nothing new.

### 3. Well-posedness (David's principle)
- **Ill-posed form (#427):** "a measure smooth in route data gives C(S) zero weight; what fixes a nonzero weight?" This presupposes a continuum of route data and a smooth reference measure, and neither is fixed.
- **Well-posed form:** assume W(S) countable (a hypothesis; whether the lock supplies it is open) and S finite, or fix one exhaustion for an independent reason. Then (M1) weight × counting on C(S) is determined up to the unspecified per-vertex values, and C(S) has positive weight whenever it is non-empty. Whether C(S) is non-empty for a given S is still "not established" (#427).
- **Inputs that remain free:** the exhaustion (or the finiteness of S), the (M1) values, and μ beyond (M1). These are David's calls. No recommendation is made here.

### 4. Honest costs / flags
- The repair moves the gap; it does not close it. "Rare means negligible" now becomes "which cutoff", and that has no answer yet.
- Countability from the lock is used as stated in the program. If the jets were taken to all orders with real coefficients, the countability claim needs checking (flag).
- MERW's forced square is an observation, not a proposal. It is not tied to |amp|² and no Born claim is made.
- 2.3 depends on #434 §7 under R-geon. Under R-frame the sign is the frame type and the same verdict holds.
- #427 and #444 are not edited. Nothing in versions/ or papers/.

## Guardrails

Classical only. No Born claim, no probability rule. μ open; (M1) untouched at L3. 1(a) and the write rule not adopted. CTCs adopted (David, 2:27 AM ET 2026-10-14, relayed via Physics Lead, not signed). Spin-½ adopted for fermions only (#431 §3c). Species conservation not adopted. R-geon/R-frame and (F)/(W) open. No ħ, no measure, no phase rule put in. Countability of worlds is a hypothesis. Nothing adopted. Nothing in versions/ or papers/.

## Ledger row and change log

| Row | Item | Content | Source | Status | Notes |
|---|---|---|---|---|---|
| L189 | The weight gap (weight-gap.md; Geometry draft, 2026-10-19, tasked by Physics Lead at 1:13 PM ET (Lead tasking under David's delegation, relayed; not David's words)) | Clean negative: #427's weight question is ill-posed without a reference measure on route data, which nothing fixes; counting, 1/\|Aut\|, frame-lift signs, MERW, Euler characteristic e(W) and entropy-max each fail T2 on at least one input. Repair: well-posed if worlds are countable and the setup finite; exact closure is then a combinatorial constraint | Geometry (draft) | candidate analysis, not adopted | Cutoff/exhaustion, (M1) values and μ stay free (David's calls); countability a hypothesis; #427 and #444 not edited; μ open; (M1) untouched |

### Change log

- 2026-10-19: note created by Creative Lead from Geometry's workstream (C) draft (comment 6272908761 on #444); ledger row L189. Geometry's own edit to its draft applied in the result paragraph: the parenthetical saying the lock gives countability replaced with "(countability of worlds is assumed here; whether the lock supplies it is open)", because jets with real coefficients are uncountable.
- 2026-10-19: Geometry's wording applied to its draft in §2.1 and §3 (countability of W(S) stated as a hypothesis; whether the lock supplies it is open). Geometry passes #447 with these. Literature's pass is still pending; no Literature fixes applied.
