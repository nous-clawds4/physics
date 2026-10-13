# Batch 28: S5, which W_i are non-empty? (structure-only; Physics Lead ruling; do not merge)

**Status.** A Lead ruling (Physics Lead) runs S5 from Claude review 018.
- Structure-only: no outcome counts, no measure, no Born input; (M1) is untouched.
- Nothing goes into `versions/` or `papers/`. Citations are bibliographic only and unread unless marked.
- Stacked on batch 27 (#411 at bf6a62d). Ledger rows L130–L135; **L131 is void**.

**Record.** The first run (`s5.py`, kept unchanged as a record, as `ekt.py` was in #408) is **void**. Its seam map sent the direction d ↦ R_θ d without flipping the component normal to the mouth, so the ray re-emerged *into* disk 2, the #408 wrong-side defect (Geometry K1, Literature G1, #413). The rerun `s5b.py` uses valid exterior-to-exterior gluings.

## For David (plain summary)

- **The question.** We fix everything the lab records about the launch. Can tiny differences between worlds, too small for the coarse flat picture to see, change *which* detector fires?
- **Answer in the toy: yes, even without a twist.** A correctly glued tiny handle acts like a diverging mirror: a change smaller than the handle in where the particle meets it changes its direction by a lot. On a fine grid, a single tiny handle near the emitter sends the particle to **every one of the 21 detectors**, and off the array, for every gluing and twist tried.
- **Withdrawn from the first (void) run:** "an ordinary tiny handle only shifts the particle", "it needs a twist", and "the detector index is about θR/Δ". All three came from the invalid gluing.
- **What decides it.** Within one world, only the sub-tiny launch data. Across worlds, Geometry's reading is that the lock allows different handles only through the symmetries of the shared unrolled geometry: none in a generic curved world, any twist in a flat one.
- **Scope.** Flat host, test particle, 2D. This shows the question is not empty in this toy. It says nothing about *how often* each detector fires.

## Setup

**Host.** A 2D flat plane with one idealised seam-glued micro-handle (#408-style, not analytic):
- the mouths are disks of radius a = 0.3ℓ at M₁, M₂ with |M₁ − M₂| = 1.6ℓ, both in a common ℓ-ball (micro, per batch 27);
- the gluings, both with an extra seam rotation θ and both followed by the normal flip w ↦ w − 2(w·e′)e′, so the ray exits mouth 2 *outward* (asserted in the script):
  - **G1** (same seam point, non-orientable handle): e′ = R_θ e, w = R_θ d.
  - **Mirror** (orientable handle): reflect e and d along d̂ = (M₂ − M₁)/|M₂ − M₁|, then rotate by R_θ.

**The LEA.** One micro-handle changes distances by ≲ ℓ, so lab-scale ε, regime 3 and additive (C1) are unaffected. A kinked straight path is still causal, so (C3) holds too.

**Particle and detectors.**
- A geodesic test particle is launched from E at the origin along +x.
- Rec₀ fixes the direction to τ/R; the sub-ℓ offset y₀ ∈ [−ℓ/2, ℓ/2] is free.
- 21 apertures of width Δ = 50ℓ sit at x = R = 10⁴ℓ. τ = 10ℓ.

**Output.** Only **the set of indices reached** on a finite grid (a lower bound; resolution-dependent near fractal boundaries). Up to 200 passages; no ray was trapped.

## Results

**Coarse grid** (2001 offsets × 5 directions, `s5b_coarse_out.txt`). This **reproduces Geometry's box run** (`/workspace/geom/s5fix.py`, sha256 3301fa8f…5f04f):
- G1, θ = 0: {0, 3, 4, 5, None}
- mirror, θ = 0: {−5, −4, −3, 0, None}

The rest of the coarse grid also matches Geometry's table.

**Fine grid** (10001 offsets × 11 directions, `s5b_out.txt`). For G1 and mirror, at every θ ∈ {0, 0.005, 0.02, 0.1, 0.5, π/2}, the reached set is **all of {−10, …, 10} plus None**.

Literature's check (201 × 5, normal flip) found subsets of these, for example {0, 5, None} at θ = 0. The growth with resolution is what a sub-ℓ → O(1) sensitive map looks like.

## Finding (S5)

**Status: L1, structure-only toy (valid gluing).**
- **Throat defocusing.** The seam's normal reflection on a disk of radius a ~ ℓ is a dispersing reflection. A sub-ℓ change in impact parameter gives an O(1) change in exit direction, with or without twist. So **several W_i are non-empty even at θ = 0**. On the fine grid, every detector's W_i is non-empty for a single micro-handle within ~ℓ of the path near E.
- **The condition.** More than one W_i is non-empty if worlds compatible with Rec₀ have such a handle near the path and Rec₀ leaves the sub-ℓ launch data free. No "only if" is established.
- **What does not hold.** "Needs a twist" and j ≈ θR/Δ are withdrawn.
- **Prior art (bibliographic only, unread).**
  - Closest analogue: Visser, PRD 39 (1989) 3182, flat-interior polyhedral wormholes with curvature on the edges.
  - Also Visser, NPB 328 (1989) 203, and Wielgus–Horák–Vincent–Abramowicz, PRD 102 (2020) 084044, for rays traced through a thin shell.
  - Sub-scale sensitivity (chaotic scattering):
    - Gaspard–Rice, J. Chem. Phys. 90 (1989) 2225;
    - Ott–Tél, Chaos 3 (1993) 417;
    - Bleher–Grebogi–Ott, Physica D 46 (1990) 87;
    - Dettmann–Frankel–Cornish, PRD 50 (1994) R618;
    - Cornish–Levin, CQG 20 (2003) 1649.
  - **Context only:** lensing by macroscopic mouths. These cover a mouth's exterior field, not transmission:
    - Cramer et al., PRD 51 (1995) 3117;
    - Safonova–Torres–Romero, PRD 65 (2002) 023001;
    - Nandi–Zhang–Zakharov, PRD 74 (2006) 024020;
    - Tsukamoto–Harada–Yajima, PRD 86 (2012) 104062; Tsukamoto, PRD 94 (2016) 124001;
    - Chetouani–Clément, GRG 16 (1984) 111; Abe, ApJ 725 (2010) 787.

    A curved handle's exterior field would add a deflection of this kind.

## The lock (Geometry's reading, #413)

- **The germ fixes the development M̃, not θ.** A world is M̃_ext/Γ (#399 §3), and a handle is a deck element γ ∈ Isom(M̃). θ is γ's linear part, chosen as world data along with Γ.
- **Continuation** fixes holonomy only along loops contractible in the development. Along a non-contractible loop the holonomy *is* γ's linear part.
- **Which θ are available:**
  - a continuum of θ needs a rotational Killing field (#398), and discrete isometries give discrete θ;
  - a generic curved analytic cover admits **no handle at all**;
  - a flat cover admits any θ.
- **Where a mouth can be.** A mouth within ρ of the observer is excluded by #399's tube injection. A mouth near the emitter (a test body) is allowed (note #410's remark that tube injection fails in micro-foam).
- **Within one fixed world,** variation comes only from sub-ℓ launch data.
- **Scope:** test-field and flat-host only. Under the lock, a flat seam handle exists only in an exactly flat host (#410 G2; Cheeger–Gromov–Taylor).

## Unchecked steps

1. **Curvature.** Real (curved, non-collapsed) handles carry curvature and an exterior lensing field. Neither is modelled.
2. **Dimension.** 2D, not 3+1D; time is ignored.
3. **Rec₀** is modelled only as "direction to τ/R, offset free below ℓ". Its full definition (#410 R4) is open. If Rec₀, or the particle model (λ_E, R5), fixes the launch below ℓ, the finding changes.
4. **One handle.** Dense foam (diffusion versus ballistic; exponential sensitivity, ~(2·spacing/a) per passage [unchecked]) is not computed.
5. **Finite grid.** Reached sets are lower bounds. The fractal structure of the exit map is not measured.
6. **No measure.** Nothing here says how large any W_i is.
7. **Geometry's lock reading** is not independently checked: it was not checked against #398 and #399 here.

## Provenance

| file | sha256 |
|---|---|
| `s5.py` (void, kept as a record) | `f1054253ae09f063a46f0cacebba1d2a12450c28e867c9de6c53fc07a1b759a6` |
| `s5_out.txt` (void) | `f2bdbb9de3072dbc0adcfe42303bb571aa585ee74893408af99ded6d9b072d1a` |
| `s5b.py` | `a6f30f6685ddf80eaf6950665a9a141c909da9cee36cd4e0477cfc38fe541635` |
| `s5b_out.txt` (`python3 s5b.py`, 10001 × 11) | `a5278391bc16f37ef9d0d80e644cfb4c8eaef8054c5cfcb9e1adcd29a4ca1b0f` |
| `s5b_coarse_out.txt` (`python3 s5b.py 2001 5`) | `ae3cc9a163c8b00e7bcbf51021baa4f5d888649d701318e8afd3fb071a6d6d18` |
