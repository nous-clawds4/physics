# Batch 27: which variable should define the LEA regimes? (Creative Lead proposal, pending review; do not merge)

**Status.** Theory only. Classical; no Born rule; (M1) untouched at L3. Citations are unchecked unless they were verified earlier. Nothing goes into `versions/` or `papers/`. Stacked on batch 26 (#410 at 2e348dc). Ledger rows L122–L126. **The recommendation below is a Creative Lead proposal pending review, not a ruling by David.**

**David, 5:17 PM ET 2026-10-13, direct in Creative Lead chat, not signed (verbatim):**
> Intuitively, it makes sense to think in terms of regimes. Whether k is the most sensible variable to use in defining these regimes is a question about which I am much less certain. I am inclined to rely upon you more than me for the details of what exactly we should do with k, or whether k is even the right variable for our purposes.

---

## For David (plain summary)

- **The three regimes stay:** flat far below the tiny scale, twisted near the tiny scale, and flat at lab scales.
- **Proposed variable: scale itself, not derivative order.** At each place and each size λ, ask how badly the best flat map of a ball of that size distorts distances. Call that number the *distortion at scale λ*. Zero means perfectly flat at that size; order one means badly twisted.
- **Why this one.**
  - It is the same quantity our flat-projection condition (C1) uses. At the lab scale it gives that condition in a weaker, additive form, which is enough for matching detectors. The full multiplicative form needs a multi-scale step that is still open.
  - It doesn't need derivatives or smoothness.
  - It sees flat tiny wraps, which the derivative count k misses, provided we also require that the flat map fill a ball.
  - It doesn't need the smoothed metric, on one assumption: the tiny twists average out to an *isotropic* (Euclidean) distance at lab scale. If they average to a lopsided distance, the lab scale doesn't look flat in this measure.
- **What happens to k.** It becomes a diagnostic. At very small sizes, the order-k terms put an upper bound on the distortion. So k bounds the distortion at small sizes and helps explain flatness or twisting there, but it doesn't define the regimes.
- This is our proposal and needs review. You left the choice to us; it is not your ruling.

---

## Candidates

**(i) Derivative order k.** The per-order size is c_k(p; λ) = |a_k(p)| λ^k, with readings R1–R3 (#410).
- It needs a frame and u.
- It needs the germ: only the finite-order Taylor remainder when the metric is smooth, and the convergent series only within ρ.
- It is blind to flat micro-topology (a_k = 0). Per Geometry (#410 F1), under the lock that blindness arises only in wholly flat hosts, but the test-field limit allows such hosts.
- It cannot speak at λ ≫ ρ, and so not at lab scale, without smoothing.
- It plugs into (C1) only indirectly, through a sum over k.

**(ii) Scale λ with a deviation functional.** Define the **flat distortion at scale λ**:

  ε(p; λ) = (1/λ) · inf_f sup_{x,y ∈ B_λ(p)} | ‖f(x) − f(y)‖_E − d_h(x, y) |,

  with the infimum taken over maps f: B_λ(p) → ℝ⁴ (h-balls, Euclidean norm).
- Here d_h is M's distance restricted to the ball, which need not be a topological ball. Since f need not be onto a ball, this is not the GH distance to a Euclidean λ-ball. It equals (2/λ)·inf over subsets Z ⊂ ℝ⁴ of d_GH(B_λ(p), Z), by the distortion/correspondence relation (Burago–Burago–Ivanov 2001 [V-meta]).
- **Density (filling) clause, part of the definition:** f(B_λ(p)) is ελ-dense in a Euclidean λ-ball, as for (C2). Without it, ε is blind to dimension drop: a wrap of size s ≪ λ gives a near-3-dimensional image with ε ~ s/λ. With it, ε ≍ GH(B_λ, Euclidean λ-ball)/λ [unchecked].
- Closest prior art: Reifenberg flatness, i.e. δ-close to a plane at every point and scale (Reifenberg 1960 [V-meta]); Cheeger–Naber's "(k, ε)-symmetric at scale r" (Invent. Math. 191 (2013) 321 [V-meta]), the nearest analogue to our regimes; Cheeger–Colding 1996/1997; Gromov 1981 [V-meta; bibliographic].
- Variant: the relative metric deviation of ḡ_L on λ-balls. It needs smoothing and does not see topology, so it is not preferred.

**(iii) A field of scales.** The curvature length ℓ_curv(p) (for example |K|^{−1/4}, or inf_k λ_k), the injectivity radius inj(p), and the local systole sys(p), meaning the length of the shortest loop through p's neighbourhood that is non-contractible in that neighbourhood (a local notion; contractibility in M_w is global, and matching sys does not fix π₁(M_w)).
- Each of these is invariant given h, and the systole sees flat topology.
- In foam, inj ~ sys ~ ℓ everywhere, so none of them can express "flat at lab scale". They give *where* things happen, not a regime criterion.
- They plug into (C1) only through a further rule.

**(iv) Other options considered.**
- **Spectral / heat-kernel deviation.** Compare the heat trace on a λ-ball with its flat value at diffusion time λ² (Weyl-law deviation). Prior art: Bérard–Besson–Gallot, GAFA 4 (1994) 373 [V-meta]. A heat trace on a ball needs boundary conditions, which this candidate would have to specify.
  - It is invariant, sees topology and is defined for smooth metrics.
  - But it is Riemannian only, through h, and it is further from (C1). It is a backup.
- **A Lorentz-native (ii).** Replace d_h with the null distance of a time function (Sormani–Vega 2016; this trades u-dependence for time-function dependence) or with an intrinsic Lorentzian distance or GH notion: Noldus 2004; Bombelli–Noldus 2004; Kunzinger–Sämann, Ann. Glob. Anal. Geom. 54 (2018) 399; Minguzzi–Suhr, Lett. Math. Phys. 114 (2024) [V-meta]; Müller 2022 [unchecked].
  - This removes the dependence on u.
  - It is less developed. It is recorded as the upgrade path for (ii).

## Side-by-side

| criterion | (i) order k | (ii) distortion ε(p; λ) | (iii) ℓ_curv, inj, sys | (iv) heat kernel |
|---|---|---|---|---|
| well-posed under David's principle | yes, once a reading R1/R2/R3 is chosen | yes (an inf of a sup; finite on bounded balls) | yes | yes |
| coordinate / frame invariance | coordinate-free given a frame; needs u | invariant given h (u only); Lorentz-native variant available | invariant given h | invariant given h |
| sees flat micro-topology | **no** | **yes**, at λ ~ sys | systole yes; ℓ_curv no | yes |
| works for smooth, non-analytic metrics | finite-order remainder only | **yes** (only distances needed) | yes | yes |
| compatible with the lock | yes | yes (needs nothing from it) | yes | yes |
| plugs into (C1) and the d_i identification | indirectly | **directly for additive (C1)** (ε(p₀; R) ≤ ε gives error εR); multiplicative (C1) needs a Reifenberg-type step | through a further rule | indirectly |
| regime 3 without smoothing | no (diverges) | **yes, if the homogenised norm is Euclidean to within ε** | no | probably (unchecked) |
| simplicity | moderate (three readings) | **one function of (p, λ)** | three fields | moderate |

## Recommendation: (ii), the flat-distortion profile ε(p; λ)

**Why (ii).**
- It is the (C1) quantity itself.
- It is defined from distances alone, so it needs no analyticity and no derivatives.
- It responds to curvature *and* topology: a flat wrap of length s gives ε(p; λ) = O(1) at λ ~ s. For λ ≫ s the error is ~s/λ, but only through a near-3-dimensional image, so the density clause is needed to register the dimension drop.
- Each micro-handle changes distances by ≲ ℓ. In dense foam the changes accumulate: a path of length λ can use ~λ/ℓ handles. At large λ, rescaled periodic fine-scale metrics GH-converge to a normed space that is generally not Euclidean (D. Burago, "Periodic metrics", Adv. Soviet Math. 9 (1992) 205 [V-meta]). The relative micro-error is ~ℓ/λ only if that homogenised (stable) norm is Euclidean to within ε (an isotropic rescaling is absorbed by f). Otherwise ε(p; λ) stays O(1) at all lab scales and regime 3 fails. **This isotropy (isotropic-foam) condition is an assumption of the LEA in this variable.** So the lab-scale regime is visible **in the raw metric**, without ḡ_L. Smoothing becomes optional, a tool for computing ε, not part of the definition. That removes batch 26's non-unique averaging problem (§4 condition 4) from the *definition* of the LEA (given the isotropy condition).
- **Definition (was a caveat):** a handle is *micro* iff its mouths lie in a common h-ball of radius ℓ. This, together with the isotropy condition of the previous item, is what the claim needs. Long-range micro-wormholes, which are macroscopic shortcuts, would show up as large ε at all scales, and they *should*: the LEA then correctly fails.

**How k fits in (derived diagnostic).**
- For a smooth h and λ < min(inj, ρ, sys/2) (so λ ≲ ℓ when micro-handles are present), Riemann normal coordinates of **h** give the upper bound ε(p; λ) ≲ C₂|Riem_h(p)|λ² + C₃|∇Riem_h(p)|λ³ + …, from d² = |x − y|² − ⅓R(x, y, y, x) + … [heuristic; constants unchecked]. These are the coefficients of h. They involve ∇u and equal g's a_k only for parallel u.
- So, heuristically, **the order-k profile controls ε(p; λ) at small λ**: an asymptotic upper bound with leading order ~|Riem_h|λ² (a matching lower bound is expected from comparison geometry [unchecked]). ε need not be smooth or analytic in λ, so this is a bound, not a Taylor series. k explains *why* the distortion is small in regime 1 and becomes O(1) near ℓ_curv in regime 2.
- k says nothing in regime 3, where the expansion is outside its range, and nothing about flat topology (sys is invisible to it).
- Under the lock it remains useful for one thing: detecting curvature microstructure from local data.

## Regimes and the LEA restated in ε(p; λ)

Fix tolerances ε ≪ 1 (flat) and ε_tw = O(1) (twisted), a micro-interval I_μ ∋ ℓ_P, and a window I_H = [ℓ_low, ℓ_high].

1. **Locally flat (the manifold property).** For each p, ε(p; λ) → 0 as λ → 0. Let λ_flat(p) = sup{λ : ε(p; λ′) ≤ ε for all λ′ ≤ λ}. This is automatic for any smooth h; no assertion is made for exact flatness.
2. **Twisted near ℓ_P.** sup_{λ ∈ I_μ} ε(p; λ) ≥ ε_tw for p in a set that is L-dense in U. This is the foam statement, and it covers both curvature and topological twisting.
3. **Flat on the window.** ε_U(p; λ) ≤ ε for all p ∈ U and all λ ∈ I_H, with ℓ_P ≪ ℓ_low and ℓ_high ≥ diam_h(U). Here ε_U uses B_λ(p) ∩ U with d_h restricted to it, since otherwise the balls leave U and the well-posedness clause below fails. Nothing is asserted for λ > ℓ_high (no cosmic claim, #410 5:03 PM).

**The LEA on U** is the conjunction of 1–3. Then:
- **(C1): the additive form follows, the multiplicative form is open.** Taking λ = ℓ_high ≥ diam U, a near-optimal f for U satisfies |‖f(x) − f(y)‖ − d_h(x, y)| ≤ εR + ℓ_low for all x, y: an additive error, not (C1)'s multiplicative ε·d_h + ℓ, and pairs closer than ℓ_low are uncontrolled. That is enough for the d_i identification, since τ ≳ εR + ℓ already. The multiplicative (C1) needs ε small at every scale in I_H and a single map compatible with all of them. Uniform small flatness at all scales gives only bi-Hölder charts; bi-Lipschitz needs a summability condition on ε over dyadic scales (Reifenberg 1960; Toro, Duke Math. J. 77 (1995) [V-meta]; Cheeger–Colding; David–Toro [unchecked]). Open. The batch-26 projection is the best flat chart at the lab scale, in this additive sense.
- **(C2)** follows from (C1) (#410 F1). **(C3)** and the ℓ-density clause remain separate conditions.
- **The d_i identification is unchanged:** lab anchoring, comparison to the reference, (M-a) localised as S_B(Λ), and (M-b). The systole profile now gives (M-a) a natural Λ: take Λ at the scale where ε(·; λ) is O(1).

**Well-posedness.** ε(p; λ) is defined for every p and λ for which B_λ(p) ⊂ U. The infimum need not be attained, which is harmless. It depends on u through h: under a boost γ the change is O(1)·(γ − 1) + O(λ|∇u|), and zero for parallel u. So restrict u to bounded γ with λ|∇u| ≪ ε. The Lorentz-native variant is the upgrade path. Computing it is hard in general, but well-definedness is what is required here. Ill-posed when B_λ(p) leaves U (λ too large near ∂U), or when the regime constants (ε, ε_tw, I_μ, I_H) are not fixed.

## Weak points

1. The relation ε ↔ GH distance and the small-λ expansion constants are standard-looking but unchecked.
2. Riemannian through h (u-dependent). The Lorentz-native distortion (null distance, Lorentzian GH) is not developed.
3. Computability: the inf over maps is not constructive. Bounds via (iii) (ℓ_curv, sys) or via ḡ_L may be needed in practice.
4. Regime 2's "L-dense" and ε_tw are conventions, to be fixed.

Ledger: L122–L126 (L122 records David's 5:17 PM words).
