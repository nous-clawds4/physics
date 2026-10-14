# Batch 28: S5, which W_i are non-empty? (structure-only; Physics Lead ruling; do not merge)

**Status.** A Lead ruling (Physics Lead) runs S5 from Claude review 018.
- Structure-only: no outcome counts, no measure, no Born input; (M1) is untouched.
- Nothing goes into `versions/` or `papers/`. Citations are bibliographic only and unread unless marked.
- Stacked on batch 27 (#411 at bf6a62d). Ledger rows L130–L135; **L131 is void**.

**Record.** The first run (`s5.py`, kept unchanged as a record, as `ekt.py` was in #408) is **void**. Its seam map sent the direction d ↦ R_θ d without flipping the component normal to the mouth, so the ray re-emerged *into* disk 2, the #408 wrong-side defect (Geometry K1, Literature G1, #413). The rerun `s5b.py` uses valid exterior-to-exterior gluings.

## For David (plain summary)

- **The question.** We fix everything the lab records about the launch. Can tiny differences between worlds, too small for the coarse flat picture to see, change *which* detector fires?
- **Answer in the toy: yes, even without a twist.** A correctly glued tiny handle acts like a diverging mirror: a change smaller than the handle in where the particle meets it changes its direction smoothly but strongly. This is a deterministic, smooth bending, not chaos: each far detector is hit by a very thin range of launch offsets, from under 10⁻⁵ to a few times 10⁻³ of the mouth radius, depending on the twist. On a fine grid, a single tiny handle near the emitter sends the particle to **every one of the 21 detectors**, and off the array, for every gluing and twist tried.
- **Review round 019 (Claude review 019; applied by Lead ruling, Physics Lead).**
  - The all-detectors result is now exact, with no grid needed: the particle's exit direction sweeps a full circle as the offset crosses the mouth, so by the intermediate-value theorem every detector is reached.
  - Topology isn't what picks the detector. A plain curved mirror would do the same, so this is sensitivity to tiny launch data, not a fingerprint of the handle.
  - The toy's sharp-seam handle lies outside the lock in *every* host, not only in flat ones. A smooth curved throat is the lock-compatible version (next batch).
  - The particle is a point, which resolves the throat to 10⁻⁶ of the handle size. That is the case batch 26 marks as outside the LEA's purpose. We keep the point particle; its size λ_E is left to you.
  - The same strong bending that fills the detectors also scrambles the path when there are many handles. That is the main obstacle, and the next batch maps it.
- **Withdrawn from the first (void) run:** "an ordinary tiny handle only shifts the particle", "it needs a twist", and "the detector index is about θR/Δ". All three came from the invalid gluing.
- **What decides it.** Among worlds that share one geometry, only the sub-tiny launch data. Across geometries, Geometry's reading is that the lock allows different handles only through the symmetries of the shared unrolled geometry: none in a generic curved world; in a flat one, any twist from 3D on (screw motions), but only for wraps without mouths. The toy's seam handle is neither: it lies outside the lock.
- **Scope.** A flat plane with one seam-glued handle, which is not analytic and so lies outside the lock; a point test particle; 2D. This shows the question is not empty in this toy. It says nothing about *how often* each detector fires.

## Setup

**Host.** A 2D flat plane with one idealised seam-glued micro-handle (#408-style, not analytic):
- the mouths are disks of radius a = 0.3ℓ at M₁, M₂ with |M₁ − M₂| = 1.6ℓ, the centres in a common ℓ-ball; the mouths themselves need a ball of radius 1.1ℓ, but the handle is micro by batch 27's π₁ criterion (generators: the seam circle, 2πa ≈ 1.9ℓ, and the shortest loop through the handle, 1.0ℓ for the mirror and 1.6ℓ for G1 at θ = 0, all ≤ 2ℓ);
- the gluings, both with an extra seam rotation θ and both followed by the normal flip w ↦ w − 2(w·e′)e′, so the ray exits mouth 2 *outward* (asserted in the script):
  - **G1** (same seam point, non-orientable handle): e′ = R_θ e, w = R_θ d.
  - **Mirror** (orientable handle): reflect e and d along d̂ = (M₂ − M₁)/|M₂ − M₁|, then rotate by R_θ. Its inverse, for passages from mouth 2 to mouth 1, is the same map R_θ·M (a reflection is its own inverse), not the R₋θ·M that s5b.py applies there. That branch never runs here: no launched ray meets mouth 2 first, and a ray leaving mouth 2 can reach only mouth 1, so every passage is 1 → 2 (Claude 019's rerun with the true inverse gives identical sets). Fix it before any run in which rays can enter mouth 2.

**The LEA.** One micro-handle changes distances by at most |M₁ − M₂| + 2a = 2.2ℓ, so lab-scale ε, regime 3 and additive (C1) are unaffected. (C3) constrains the chart, not the path: through the seam a causal curve's image jumps by at most about 2.2ℓ, which (C3) tolerates when εL ≳ 2.2ℓ (time is not modelled). The particle is a point geodesic, which resolves the throat down to the sliver widths (as small as about 10⁻⁶ℓ): that is the λ_E ≲ ℓ case of #410 §4 condition 7, where the LEA's purpose fails. λ_E is not chosen here (open for David), so the geometry is within the LEA, and the finding holds for this particle model only (Claude 019).

**Particle and detectors.**
- A geodesic test particle is launched from E at the origin along +x.
- Rec₀ fixes the direction to τ/R; the sub-ℓ offset y₀ ∈ [−ℓ/2, ℓ/2] is free.
- 21 contiguous apertures of width Δ = 50ℓ sit at x = R = 10⁴ℓ (they tile |y| ≤ 525ℓ, so their Hausdorff separation is Δ ≫ τ, as #410 §3 needs). τ = 10ℓ. Per run the host and gluing are fixed, and a world in W is a launch (y₀, φ) with y₀ ∈ [−ℓ/2, ℓ/2] and |φ| ≤ 0.4τ/R (the script's range); W_i is the set of launches whose ray first crosses aperture i.

**Output.** Only **the set of indices reached** on a finite grid (a lower bound; resolution-dependent because each j ≠ 0 is reached on thin slivers of offsets: at θ = 0 the widest per index is about 3×10⁻⁵ℓ (two passes) and the first-pass grazing ones about 2×10⁻⁶|j|ℓ; at θ = π/2 they are about 5×10⁻⁴ℓ (Claude 019). These are lengths in the offset coordinate, quoted only to explain the grid dependence, not sizes of the W_j). Up to 200 passages; no ray was trapped.

## Results

**Coarse grid** (2001 offsets × 5 directions, `s5b_coarse_out.txt`). This **reproduces Geometry's box run** (`/workspace/geom/s5fix.py`, sha256 3301fa8f…5f04f):
- G1, θ = 0: {0, 3, 4, 5, None}
- mirror, θ = 0: {−5, −4, −3, 0, None}

The rest of the coarse grid also matches Geometry's table.

**Fine grid** (10001 offsets × 11 directions, `s5b_out.txt`). For G1 and mirror, at every θ ∈ {0, 0.005, 0.02, 0.1, 0.5, π/2}, the reached set is **all of {−10, …, 10} plus None**.

Literature's check (201 × 5, normal flip) found subsets of these, for example {0, 5, None} at θ = 0. The growth with resolution is what a sub-ℓ → O(1) sensitive map looks like. For one handle the map is piecewise smooth and deterministic (for G1 at θ = 0, every j ≠ 0 is reached after 1–2 passes, at non-grazing incidence except j = ±10; Geometry box diagnostic; with the mirror gluing some slivers need up to 6 passes, near its periodic orbit, Claude 019). All detectors are reached by continuity of the exit angle over an O(1) range that contains the about 0.1 rad array. This is exact, with no grid: on the first pass the exit angle runs once through a full turn as the impact parameter crosses the mouth, and a ray leaving mouth 2 within 0.06 rad of +x cannot reach mouth 1 (it would have to drop 1ℓ within 0.6ℓ of run). So by the intermediate-value theorem every aperture, and None, is reached for every θ and both gluings (Claude 019 checked θ = 0, 0.005, 0.02, 0.1, 0.5, π/2, 2.5, −1). Here the grid's lower bound is attained. It is not chaotic randomisation, and it is not a count.

## Finding (S5)

**Status: L1, structure-only toy (valid gluing).**
- **Throat defocusing.** The seam's normal reflection on a disk of radius a ~ ℓ is a dispersing reflection. A sub-ℓ change in impact parameter gives an O(1) change in exit direction, with or without twist. So **several W_i are non-empty even at θ = 0**. On the fine grid, every detector's W_i is non-empty for a single micro-handle within ~ℓ of the path near E.
- **The condition.** More than one W_i is non-empty if worlds compatible with Rec₀ have such a handle near the path and Rec₀ leaves the sub-ℓ launch data free. No "only if" is established. What selects the detector is the sub-ℓ launch datum behind a dispersing throat, not the handle's topology: on the first pass, G1 at θ = 0 acts as a convex mirror displaced by 1.6ℓ, so a plain reflecting disk would reach the same indices. Topology enters as the source of the seam's −4π of curvature (Gauss–Bonnet; Claude 019).
- **What does not hold.** "Needs a twist" and j ≈ θR/Δ are withdrawn.
- **Prior art (bibliographic only, unread).**
  - Closest analogue: Visser, PRD 39 (1989) 3182, flat-interior polyhedral wormholes with curvature on the edges.
  - Also Visser, NPB 328 (1989) 203, and Wielgus–Horák–Vincent–Abramowicz, PRD 102 (2020) 084044, for rays traced through a thin shell.
  - Sub-scale sensitivity (chaotic scattering; relevant to dense foam, not to the single-handle toy, which is a non-chaotic dispersing map):
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
- **Continuation** fixes holonomy only along loops of the world that lift to closed loops in the development (the contractible ones; every loop in the simply connected M̃ is contractible). Along a non-contractible loop the holonomy *is* γ's linear part.
- **Which θ are available:**
  - a continuum of θ needs an axial Killing field that commutes with γ (#398), and discrete isometries give discrete θ;
  - a generic curved analytic cover admits **no handle at all**;
  - a flat cover admits a continuum of θ only from 3D on, through screw motions: in 2D every fixed-point-free isometry is a translation or a glide reflection, so no deck element rotates. Flat quotients are wraps without mouths, so this does not cover the toy's θ, which parametrises a non-analytic seam gluing (Claude 019).
- **Where a mouth can be.** A mouth within ρ of the observer is excluded by #399's tube injection. A mouth near the emitter (a test body) is allowed (note #410's remark that tube injection fails in micro-foam).
- **Within one fixed geometry M̃/Γ,** worlds differ only in sub-ℓ launch data (#410 §6 puts the particle's worldline in the world). The reachability finding needs nothing more, since it holds at θ = 0 in one geometry, so this reading is not load-bearing for it. "No handle at all" is for a generic germ; the foam the LEA assumes is not generic, because its development carries that world's Γ. There, if Isom(M̃) has no further symmetry, each throat's local geometry is fixed by the germ, and what varies between worlds is which subgroup closes the handles, that is, where each throat leads (Claude 019).
- **Scope:** test-field, with a non-analytic seam, so outside the lock (see below); 2D. The seam handle is flat off the seam, with its curvature concentrated on the seam (a thin shell, as in Visser 1989). Under the lock no seam handle occurs, in any host: an analytic metric that is flat off the seam is flat on it too (identity theorem: analytic and flat on an open set means flat everywhere; #410 G2), while one handle in an otherwise flat plane needs total curvature −4π (Gauss–Bonnet; the surface has Euler characteristic −1, orientable or not), which here sits on the seam. An exactly flat analytic world has wraps but no mouths. So the toy is outside the lock, as batch 19 and L70 say of thin shells (Claude 019). Smooth, non-collapsed handles instead carry curvature beside them (Cheeger–Gromov–Taylor).

## Unchecked steps

1. **Curvature.** Real (curved, non-collapsed) handles carry curvature and an exterior lensing field. Neither is modelled. Heuristically both add to the sensitivity: for a spherically symmetric throat with a circular light orbit the deflection diverges logarithmically at the critical impact parameter (Bozza, PRD 66 (2002) 103001, abstract; Tsukamoto 2016 for the Ellis throat), so exit directions wind through every angle within a thin window of impact parameters. Claude 019 checked this for the analytic 2D Ellis neck ds² = dr² + (r² + a²)dφ², for reflected rays (2K(a/b) − π) and transmitted ones ((2b/a)K(b/a)). That neck joins two sheets; a smooth handle is not computed.
2. **Dimension.** 2D, not 3+1D; time is ignored.
3. **Rec₀** is modelled only as "direction to τ/R, offset free below ℓ". Its full definition (#410 R4) is open. If Rec₀, or the particle model (λ_E, R5), fixes the launch below ℓ, the finding changes.
4. **One handle.** Dense foam (diffusion versus ballistic; exponential sensitivity, ~(2·spacing/a) per passage [unchecked]) is not computed. The O(1) deflection per throat encounter that fills the W_i also scrambles the path wherever encounters are frequent: a point geodesic diffuses unless straight runs between throat encounters, of order 1/(2πa²n) in 3D for n handles per unit volume [heuristic], exceed R. Regime 3 constrains distances, not the flight of geodesics (this toy is an example), so the LEA does not yet secure ballistic arrival. Claude 018 S5's "sparse or untwisted traversal keeps the path within ~√(Rℓ)" assumed the same shift-only map as the void run and is withdrawn too (Claude 019).
5. **Finite grid.** Reached sets are lower bounds. With one handle (two disks) there is no fractal repeller, only one unstable periodic orbit; fractal exit structure is expected once a ray leaving a mouth can reach more than one other mouth, that is from two handles on [not computed] (dense foam, item 4).
6. **No measure.** Nothing here says how large any W_i is.
7. **Geometry's lock reading** was checked against #398 and #399 by Claude 019: correct in outline, with the flat-cover clause corrected (R2) and the toy outside the lock (R1).

## Provenance

| file | sha256 |
|---|---|
| `s5.py` (void, kept as a record) | `f1054253ae09f063a46f0cacebba1d2a12450c28e867c9de6c53fc07a1b759a6` |
| `s5_out.txt` (void) | `f2bdbb9de3072dbc0adcfe42303bb571aa585ee74893408af99ded6d9b072d1a` |
| `s5b.py` | `a6f30f6685ddf80eaf6950665a9a141c909da9cee36cd4e0477cfc38fe541635` |
| `s5b_out.txt` (`python3 s5b.py`, 10001 × 11) | `a5278391bc16f37ef9d0d80e644cfb4c8eaef8054c5cfcb9e1adcd29a4ca1b0f` |
| off-repo on the box (Geometry): `/workspace/geom/s5fix.py` | `3301fa8ffdac7c0c8c1ae210e40ff86f7e412872e497632ae3a58d9ec4e5f04f` |
| off-repo on the box (Geometry): `/workspace/geom/s5bdiag.py` | `8e64aec947aff154ade96874d9c8bdc5f15aa9d902a9c9eed1cbf713c4bb8d42` |
| `s5b_coarse_out.txt` (`python3 s5b.py 2001 5`) | `ae3cc9a163c8b00e7bcbf51021baa4f5d888649d701318e8afd3fb071a6d6d18` |
