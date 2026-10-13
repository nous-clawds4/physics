# Batch 28: S5, which W_i are non-empty? (structure-only; Physics Lead ruling; do not merge)

**Status.** A Lead ruling (Physics Lead) runs S5 from Claude review 018. This is structure-only:
- no outcome counts, no measure, no Born input; (M1) is untouched;
- nothing goes into `versions/` or `papers/`;
- citations are unchecked unless they were verified earlier.

Stacked on batch 27 (#411 at bf6a62d). Ledger rows L130–L132.

## For David (plain summary)

- **The question.** We fix everything the lab records about the launch. Can tiny differences between worlds, too small for the coarse flat picture to see, change *which* detector fires?
- **Answer in the toy: yes, but only through a handle with a twist.**
  - An ordinary tiny handle just shifts the particle sideways by a tiny amount, so every world sends it to the same detector.
  - A tiny handle whose gluing turns the direction by an angle θ larger than about (detector spacing)/(distance) can send the particle to a different detector. It depends on whether the particle happens to pass through the handle, which a sub-tiny difference in the launch decides.
- **So some detector-sets other than the "straight-line" one are non-empty.** This holds when worlds compatible with the record may differ in twisted tiny handles near the emitter, or in sub-tiny launch data beside such a handle. The question is not empty.
- **The catch.** Large twists mostly send the particle off the detector array altogether. Whether the lock even allows worlds that share the lab's local geometry but differ in such handles is not checked.

## Setup

**Host.** A 2D flat plane with one idealised seam-glued micro-handle, of the kind #408 used (idealised, not analytic):
- mouths are disks of radius a = 0.3ℓ, centred at M₁ and M₂ with |M₁ − M₂| = 1.6ℓ, so both lie in a common ℓ-ball (micro, per batch 27);
- the gluing maps mouth 1 to mouth 2 by translation composed with a rotation by θ (θ = 0: untwisted).

**The LEA.** One micro-handle changes distances by ≲ ℓ, so ε(p; λ) at lab scale is unaffected, and regime 3 and the additive (C1) hold. A kinked straight path is still causal, so (C3) is unaffected. The world therefore lies within the LEA for every θ.

**Particle and detectors.**
- A geodesic test particle is launched from E at the origin, in direction +x.
- Rec₀ fixes the direction to resolution τ/R. The sub-ℓ offset y₀ ∈ [−ℓ/2, ℓ/2] is not fixed.
- The detectors are apertures of width Δ = 50ℓ at x = R = 10⁴ℓ, centred at jΔ, |j| ≤ 10. τ = 10ℓ, with ℓ ≪ τ ≪ Δ.

**The script.** `batch-28/s5.py` maps each (θ, y₀, launch direction) to a detector index (None: misses the array). It reports only **which indices occur**, with no frequencies.

## Result (`batch-28/s5_out.txt`)

| twist θ | detector indices reached |
|---|---|
| 0 | {0} |
| 0.005 | {0, 1} |
| 0.02 | {0, 4} |
| 0.1, 0.5, π/2 | {0, None} |

**Reading.**
1. **Untwisted micro-handles give no non-triviality.** The exit displacement is ≲ 2ℓ ≪ Δ, so only W₀ is non-empty, in line with Claude 018 S5's heuristic.
2. **A twist θ ≳ Δ/R makes a second W_j non-empty.** Here j ≈ θR/Δ (θ = 0.02 gives j = 4). Which index occurs is set by whether the sub-ℓ launch datum enters the mouth. That is a micro difference below the LEA tolerance, and it changes the macroscopic detector.
3. **θ ≫ N·Δ/R sends the particle off the array**, so only "no detector" joins W₀.

## Finding (S5)

**Status: L1, structure-only toy.**
- Within the LEA, the W_i are generically **not** all empty except one. More than one is non-empty iff worlds compatible with Rec₀ may contain, within ~ℓ of the particle's path, a micro-handle whose gluing turns directions by θ ≳ Δ/R, with θ not fixed by Rec₀.
- The mechanism is classical: micro-gluing holonomy, sampled by sub-ℓ launch data.
- **What is still missing.** Without twisted gluings (θ = 0, or holonomy trivial on directions), the S5 obstacle stands: no classical mechanism takes micro-data to detectors Δ apart.

## Unchecked steps

1. **The lock.** Under the analytic lock, the universal cover's metric near E is fixed by the germ. Worlds can differ only by Γ and extensions (#399 §3). Whether different Γ can give a handle near E with a different twist, or none, while sharing the observer's germ is **not checked**. Batch 26 notes that continuation fixes holonomy along a given loop, so θ along a loop already in the germ's domain may be fixed. If so, the variation must come from sub-ℓ launch data alone, in one fixed twisted world.
2. **Idealised seam gluing** in 2D, not analytic. It has a single handle, and no curvature beside it (Claude 018 R1 says real handles in a non-collapsed region carry curvature, which adds a deflection not modelled here).
3. **2D, not 3+1D.** Time and recrossings are ignored beyond up to 50 passages.
4. **Rec₀** is modelled only as "direction to τ/R, offset free below ℓ". Its full definition (#410 R4) is open.
5. **No dense foam.** The diffusion-versus-ballistic question for many twisted handles (Claude 018 S5) is not computed.
6. No measure: nothing here says how *large* any W_j is.

## Provenance

- `s5.py`, sha256 `f1054253ae09f063a46f0cacebba1d2a12450c28e867c9de6c53fc07a1b759a6`
- `s5_out.txt`, sha256 `f2bdbb9de3072dbc0adcfe42303bb571aa585ee74893408af99ded6d9b072d1a`
