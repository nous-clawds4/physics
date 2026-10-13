# Batch 27: which variable should define the LEA regimes? (Creative Lead proposal, pending review; do not merge)

**Status.** Theory only. Classical; no Born rule; (M1) untouched at L3. Citations are unchecked unless they were verified earlier. Nothing goes into `versions/` or `papers/`. Stacked on batch 26 (#410 at 2e348dc). Ledger rows L122–L126. **The recommendation below is a Creative Lead proposal pending review, not a ruling by David.**

**David, 5:17 PM ET 2026-10-13, direct in Creative Lead chat, not signed (verbatim):**
> Intuitively, it makes sense to think in terms of regimes. Whether k is the most sensible variable to use in defining these regimes is a question about which I am much less certain. I am inclined to rely upon you more than me for the details of what exactly we should do with k, or whether k is even the right variable for our purposes.

---

## For David (plain summary)

- **The three regimes stay:** flat far below the tiny scale, twisted near the tiny scale, and flat at lab scales.
- **Proposed variable: scale itself, not derivative order.** At each place and each size λ, ask how badly the best flat map of a ball of that size distorts distances. Call that number the *distortion at scale λ*. Zero means perfectly flat at that size; order one means badly twisted.
- **Why this one.**
  - It is the exact quantity our flat-projection condition already uses (batch 26), so there is no translation step.
  - It doesn't need derivatives or smoothness.
  - It sees flat tiny wraps, which the derivative count k misses.
  - It doesn't need the smoothed metric: at lab scales the tiny twists average out by themselves.
- **What happens to k.** It becomes a diagnostic. At very small sizes, the distortion can be expanded in powers of λ, and the coefficients of that expansion are the order-k terms. So k explains *why* the geometry is flat or twisted at small sizes, but it doesn't define the regimes.
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
- This is twice the Gromov–Hausdorff distance between B_λ(p) and a Euclidean λ-ball, divided by λ, up to a constant [standard GH facts; unchecked].
- Variant: the relative metric deviation of ḡ_L on λ-balls. It needs smoothing and does not see topology, so it is not preferred.

**(iii) A field of scales.** The curvature length ℓ_curv(p) (for example |K|^{−1/4}, or inf_k λ_k), the injectivity radius inj(p), and the systole sys(p), meaning the length of the shortest non-contractible loop through p's neighbourhood.
- Each of these is invariant given h, and the systole sees flat topology.
- In foam, inj ~ sys ~ ℓ everywhere, so none of them can express "flat at lab scale". They give *where* things happen, not a regime criterion.
- They plug into (C1) only through a further rule.

**(iv) Other options considered.**
- **Spectral / heat-kernel deviation.** Compare the heat trace on a λ-ball with its flat value at diffusion time λ² (Weyl-law deviation).
  - It is invariant, sees topology and is defined for smooth metrics.
  - But it is Riemannian only, through h, and it is further from (C1). It is a backup.
- **A Lorentz-native (ii).** Replace d_h with the null distance of a time function (Sormani–Vega 2016) or with Lorentzian GH distance (Noldus 2004) [bibliographic, per #410].
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
| plugs into (C1) and the d_i identification | indirectly | **directly**: (C1) at scale R is ε(p₀; R) ≤ ε | through a further rule | indirectly |
| regime 3 without smoothing | no (diverges) | **yes**: micro-error ~ℓ/λ | no | probably (unchecked) |
| simplicity | moderate (three readings) | **one function of (p, λ)** | three fields | moderate |

## Recommendation: (ii), the flat-distortion profile ε(p; λ)

**Why (ii).**
- It is the (C1) quantity itself.
- It is defined from distances alone, so it needs no analyticity and no derivatives.
- It responds to curvature *and* topology: a flat wrap of length s gives ε(p; λ) = O(1) at λ ~ s, and a relative error ~s/λ → 0 for λ ≫ s.
- Microstructure of size ~ℓ contributes an additive error ≲ ℓ, which is relative ℓ/λ. So the lab-scale regime is visible **in the raw metric**, without ḡ_L. Smoothing becomes optional, a tool for computing ε, not part of the definition. That removes batch 26's non-unique averaging problem (§4 condition 4) from the *definition* of the LEA.
- **Caveat:** this holds if the microscopic handles connect only points within ~ℓ of each other. Long-range micro-wormholes, which are macroscopic shortcuts, would show up as large ε at all scales, and they *should*: the LEA then correctly fails.

**How k fits in (derived diagnostic).**
- For a smooth h and λ below ρ (or below the remainder bound), Riemann normal coordinates give ε(p; λ) = C₂|a₂(p)|λ² + C₃|a₃(p)|λ³ + … [heuristic: the metric deviation ~|a_k|λ^k gives distance distortion of the same order; constants unchecked].
- So **the order-k profile is the small-λ Taylor expansion of ε(p; λ)**. k explains *why* the distortion is small in regime 1 and becomes O(1) near ℓ_curv in regime 2.
- k says nothing in regime 3, where the expansion is outside its range, and nothing about flat topology (sys is invisible to it).
- Under the lock it remains useful for one thing: detecting curvature microstructure from local data.

## Regimes and the LEA restated in ε(p; λ)

Fix tolerances ε ≪ 1 (flat) and ε_tw = O(1) (twisted), a micro-interval I_μ ∋ ℓ_P, and a window I_H = [ℓ_low, ℓ_high].

1. **Locally flat (the manifold property).** For each p, ε(p; λ) → 0 as λ → 0. Let λ_flat(p) = sup{λ : ε(p; λ′) ≤ ε for all λ′ ≤ λ}. This is automatic for any smooth h; no assertion is made for exact flatness.
2. **Twisted near ℓ_P.** sup_{λ ∈ I_μ} ε(p; λ) ≥ ε_tw for p in a set that is L-dense in U. This is the foam statement, and it covers both curvature and topological twisting.
3. **Flat on the window.** ε(p; λ) ≤ ε for all p ∈ U and all λ ∈ I_H, with ℓ_P ≪ ℓ_low and ℓ_high ≥ diam_h(U). Nothing is asserted for λ > ℓ_high (no cosmic claim, #410 5:03 PM).

**The LEA on U** is the conjunction of 1–3. Then:
- **(C1) follows directly.** Taking λ = ℓ_high ≥ diam U, a near-optimal f for B_{ℓ_high}(p₀) ⊇ U satisfies (C1) with relative error ε and additive ℓ (absorbed, since ε(p; λ) includes ℓ/λ). The batch-26 projection *is* the best flat chart at the lab scale.
- **(C2)** follows from (C1) (#410 F1). **(C3)** and the ℓ-density clause remain separate conditions.
- **The d_i identification is unchanged:** lab anchoring, comparison to the reference, (M-a) localised as S_B(Λ), and (M-b). The systole profile now gives (M-a) a natural Λ: take Λ at the scale where ε(·; λ) is O(1).

**Well-posedness.** ε(p; λ) is defined for every p and λ for which B_λ(p) ⊂ U. The infimum need not be attained, which is harmless. It depends on u through h; the Lorentz-native variant is the upgrade path. Computing it is hard in general, but well-definedness is what is required here. Ill-posed when B_λ(p) leaves U (λ too large near ∂U), or when the regime constants (ε, ε_tw, I_μ, I_H) are not fixed.

## Weak points

1. The relation ε ↔ GH distance and the small-λ expansion constants are standard-looking but unchecked.
2. Riemannian through h (u-dependent). The Lorentz-native distortion (null distance, Lorentzian GH) is not developed.
3. Computability: the inf over maps is not constructive. Bounds via (iii) (ℓ_curv, sys) or via ḡ_L may be needed in practice.
4. Regime 2's "L-dense" and ε_tw are conventions, to be fixed.

Ledger: L122–L126 (L122 records David's 5:17 PM words).
