# Batch 29: many handles along the path. Ballistic or diffusive, and are several W_i still non-empty? (structure-only; Lead ruling; do not merge)

**Status.** A Lead ruling (Physics Lead) runs Claude review 019's next step.
- **Structure-only:** detector reachability only. No counts of worlds, no measure, no Born input; (M1) is untouched.
- **Scope:** 2D, point test particle; λ_E is left to David. Nothing goes into `versions/` or `papers/`. Citations are unchecked unless marked.
- **Branch:** stacked on batch 28 (#413 at 87b5bd7). Ledger rows L136–L140.

## For David (plain summary)

- **The question.** In batch 28 one tiny handle could send the particle to any detector. But the same strong bending, repeated at many handles, might scramble the path so badly that it never arrives in a straight-ish way. We placed handles all along the path at spacing s and asked two things: when does the flight stay roughly straight, and are several detectors still reachable then?
- **Answer (toy).** There is a clear crossover at s ≈ √(4·a·R), about 110ℓ here (ℓ the micro scale: about 50 handle spans of 2.2ℓ, or about 370 mouth radii). That is where the typical straight run between handle encounters, about s²/(4a), reaches the lab size R.
  - **Sparser than that:** arriving paths meet 0–6 handles. The flight is ballistic, a few straight legs, and many detectors are reached: 10–16 of 21 on our coarse grid, a lower bound.
  - **Much denser** (s ≤ 20): paths that arrive have met hundreds to thousands of handles, and most don't arrive within our step limit. We call this "diffusive" by analogy with a gas of scatterers; we didn't measure spreading.
  - **So both conditions hold together for sparse foam.** They don't simply fail together in dense foam: at s = 20 a few detectors are still reached, after hundreds of encounters. Even in the sparse window some launches don't arrive within our step limit, so "ballistic" describes the paths that do arrive. And under the lock, a lab with handles in it is only approximately flat, never exactly. That matches your "dense but not TOO dense" proposal (still held open) in a concrete way: "not too dense" means a free run between throat encounters longer than the lab.
- **Is it chaotic?** One handle: no, the map is smooth. Clusters of four or more handles close together (2×2 and 3×3; two handles were not run): the signs of chaotic scattering appear. As we refine the launch grid, the number of outcome boundaries keeps growing like a power of the resolution, and so does the longest run of passes.
- **A smooth throat, inside the analytic lock, does the same.** For a smooth analytic neck (Ellis-like), the particle that skims the throat winds round it many times. On our grid every one of the 21 detectors is reached by rays that stay on the emitter's side. This is a neck joining two sheets, not a handle; a smooth handle is still not computed.

## Setup

**Foam (`foam.py`).**
- The plane is tiled by cells of side s for x > 5 − s/2. Each cell holds one seam handle: mouth disks of radius a = 0.3ℓ, 1.6ℓ apart, at a fixed pseudo-random offset inside the cell (no overlaps).
- Cell (0,0) holds batch 28's handle at M₁ = (5, 0).
- Gluings, at θ = 0: G1 (non-orientable) or mirror (orientable). Both use the normal flip, and the outward exit is asserted. At θ = 0 both inverses are exact (Claude 019 S1).
- Launch from (0, y₀), with y₀ ∈ [−ℓ/2, ℓ/2] (sub-ℓ) and |φ| ≤ 0.4τ/R.
- Detectors: 21 contiguous apertures of width Δ = 50ℓ at x = R = 10⁴ℓ.
- Outcomes:
  - a detector index;
  - None: crosses x = R outside the array, or leaves (x < −s or |y| > 3R);
  - "no arrival within cap": the step cap is 40R/s + 200 cell steps.
- Grid: 1001 × 3 (a lower bound, coarse because the dense cases are slow).
- Encounter numbers are reported for arriving paths only, as a diagnostic in the launch-offset coordinate, not a size of any W_i.
- Free run between throat encounters: ℓ_free = 1/(nσ) = s²/(4a), with σ = 2a (the 2D cross-section is the disc's full width) and n = 2/s² (two mouths per cell). This is the 2D Lorentz-gas mean free path (Santaló's mean-free-path formula; Bunimovich–Sinai 1981; Bunimovich–Sinai–Chernov 1991; Boltzmann–Grad limit: Gallavotti 1969, Spohn 1978, Boldrighini–Bunimovich–Sinai 1983 [V-meta]) [checked by Geometry]. For periodic layouts the free-path law is not exponential (Marklof–Strömbergsson 2010 [V-meta]); this foam is pseudo-random per cell. At ℓ_free = R a path still meets about 1 handle on average.

**Cluster (`scatter3.py`).**
- K × K handles at spacing s₀ (G1 or mirror, θ = 0) in an empty plane, with incoming parallel rays and an outcome of exit sector out of 8.
- Diagnostic: the number of outcome changes C(n) on n offsets across the cluster, n = 10³…10⁶, and the largest number of passes.
- A piecewise-smooth map saturates C(n). A fractal boundary gives C(n) ~ n^D with 0 < D < 1.

**Smooth throat (`ellis.py`).**
- The 2D Ellis neck ds² = dr² + (r² + a²)dφ², which is analytic (the equatorial slice of the Ellis drainhole: Ellis, J. Math. Phys. 14 (1973) 104 [V-meta]; Bronnikov 1973 [unverified]; geodesics: Chetouani–Clément 1984, Müller 2008 [V-meta]). Geodesics are integrated with scipy DOP853 at rtol 1e-11.
- The numerical sweep matches the closed form 2K(a/b) to 6 digits (b = a(1 + 10⁻¹…10⁻⁶)).
- Reflected rays are continued straight from the neck to the 21-aperture line at distance R. 4500 impact parameters are clustered at b = a.

## Results

**Foam, reached sets** (lower bounds; G1 / mirror):

| s (ℓ) | ℓ_free ≈ s²/4a | G1 reached | mirror reached | encounters on arriving paths (G1; mirror) | regime |
|---|---|---|---|---|---|
| 5 | 21 | 0 | 0 | none arrive; none arrive | diffusive, no arrival within cap |
| 10 | 83 | 1 | 0 | 2590; none arrive | diffusive |
| 20 | 333 | 4 | 2 | 172–652; 136–178 | diffusive |
| 50 | 2.1×10³ | 12 | 8 | 6–53; 3–26 | crossover |
| 110 | 1.0×10⁴ (≈ R) | 13 | 11 | 1–6; 1–6 | ballistic (a few legs) |
| 200 | 3.3×10⁴ | 16 | 10 | 0–3; 0–4 | ballistic |
| 500 | 2.1×10⁵ | 5 | 4 | 0–3; 0–2 | ballistic, single-handle-like |
| 2000 | 3.3×10⁶ | 4 | 4 | 0–2; 0–2 | single-handle |

For s = 2000 (and for the mirror also at s = 500; G1 at s = 500 adds index 2) the coarse sets match batch 28's coarse single-handle sets: {0, 3, 4, 5} for G1 and {−5, −4, −3, 0} for mirror. By batch 28's exact IVT argument, all 21 are reachable whenever the first-pass exit cone toward the array is not blocked by another mouth [not proven here for the foam].

**Cluster, C(n)** (n = 10³, 10⁴, 10⁵, 10⁶):

| gluing | K = 1 (s₀ = 4) | K = 2 (s₀ = 4) | K = 3 (s₀ = 4) | K = 3 (s₀ = 2.5) |
|---|---|---|---|---|
| G1 | 27, 28, 28, 28 (saturates; max 2 passes) | 64, 168, 500, 1550 (max passes 3 → 7) | 86, 329, 1497, 6822 (5 → 10) | 114, 498, 2708, 15218 (10 → 17) |
| mirror | 31, 46, 65, 78 (slow growth; 4 → 6) | 59, 183, 523, 1694 (4 → 8) | 90, 343, 1376, 6112 (4 → 10) | 113, 468, 2157, 11094 (6 → 13) |

- For K ≥ 2 (4 or more handles), C(n) grows by a factor of about 2.6–5.6 per decade (local log-slopes about 0.4–0.75, still rising across the three decades: G1 K = 3, s₀ = 2.5 gives 0.64, 0.74, 0.75; G1 K = 2 gives 0.42, 0.47, 0.49), and the longest pass sequence grows with resolution. C(n) estimates the box dimension D = 1 − α of the boundary set (α the uncertainty exponent). D ≈ 0.4–0.75 is a range of local slopes, not a converged dimension; smooth boundaries and grazing roundoff bias it. These are the signatures of a fractal repeller (chaotic scattering; cf. Gaspard–Rice 1989, Ott–Tél 1993, bibliographic only).
- For one handle, G1 saturates, which is piecewise smooth (batch 28, Geometry N1–N4). The mirror's slow growth is consistent with its single unstable periodic orbit (Claude 019 N6).

**Smooth throat.**
- Reflected rays reach all 21 detectors and None, and transmitted rays exist (to sheet 2).
- The sweep near b = a grows like ln(1/(b − a)) (11.29 at 10⁻⁴, 15.89 at 10⁻⁶), so every direction recurs in each thin window of b. The result is exact by continuity and the IVT, as in Claude 019 S3.

## Findings

1. **Ballistic window (L1, toy).** The foam is ballistic, with arriving paths of a few legs, when ℓ_free ≈ s²/(4a) ≳ R, i.e. s ≳ √(4aR) ≈ 110ℓ here. It is diffusive for s ≲ 20ℓ. In the ballistic window several W_i stay non-empty (10–16 of 21 on a coarse grid; all 21 by IVT if the exit cone is clear [unproven]). So **"several W_i non-empty" and "ballistic flight" hold together for sparse foam** in this toy. In dense foam the flight is not ballistic, but several W_i can still be non-empty (s = 20: 4 indices for G1 and 2 for mirror, after hundreds of encounters), so they do not fail together.
   - This is a concrete, geometric reading of David's 5:26 PM "dense but not TOO dense". That proposal is still held open, not adopted.
   - Note that "not too dense" here is a condition on *geodesic flight* (ℓ_free ≳ R), which regime 3 alone does not secure (Claude 019 S4).
2. **Chaos needs several nearby handles (L1).** One handle gives a piecewise-smooth map. Clusters of four or more handles (2×2, 3×3) within a few ℓ of each other show growing boundary counts and pass numbers (a two-handle cluster, four mouths, is the analogue of the three-disk condition, Gaspard–Rice 1989, Eckhardt 1987 [V-meta], and is plausible but not run), consistent with a fractal (chaotic-scattering) exit structure. In the ballistic window, encounters along a path are typically 0–6 isolated handles, so sensitivity there is the single-handle kind, unless handles cluster.
3. **A smooth analytic throat gives the same reachability (L1).** The Ellis neck's logarithmic winding reaches every detector from the emitter's sheet. That moves the *mechanism* inside the lock (analytic geometry), though not yet as a handle. Its total curvature is ∫K dA = −4π, the same Gauss–Bonnet budget any one-sheet handle needs. Under the lock, a world with handles is curved near each of them, so lab flatness is only the approximate regime 3, never exact on an open set (identity theorem).

## Unchecked steps

1. **No smooth analytic handle is computed.** The Ellis neck is a two-sheet neck; turning it into a one-sheet handle needs a second neck or a seam, i.e. more curvature, with the total fixed at −4π per handle by Gauss–Bonnet. The foam uses non-analytic seams (outside the lock, batch 28 R1).
2. **2D only, point particle.** This is the λ_E ≲ ℓ case of #410 §4 condition 7. λ_E is left to David, and a particle with a length must re-derive all of this.
3. **Coarse grids (1001 × 3) for the foam.** The sets are lower bounds, and IVT completeness in the foam is not proven.
   - The step cap biases the dense cases: "no arrival within cap" is not the same as "never arrives". Some launches also hit the cap inside the ballistic window (s = 110 for G1; s = 200 for both gluings), so "ballistic" describes arriving paths only. "Diffusive" is a label by Lorentz-gas analogy (many encounters before arrival); no displacement statistics were computed, and Bunimovich–Sinai-type diffusion theorems are for billiard collisions, not seam passages.
   - ℓ_free ≈ s²/(4a) is heuristic, and the cell-based foam has a pseudo-random but fixed layout (one world geometry per s).
4. **The fractal dimension is rough.** It comes from three decades of n. There is no Lyapunov exponent or escape-rate computation.
5. **The Ellis continuation** treats the ray as straight from the neck. The residual curvature on sheet 1 beyond r = 60ℓ = 200a (script rout = 60 with a = 0.3) and the emitter–neck geometry are simplified. The residual angle there is ~(a/r)² ≈ 2.5×10⁻⁵ rad, far below the aperture angle Δ/R = 5×10⁻³ (Geometry).
6. **No measure.** Nothing says how large any W_i is; encounter numbers and C(n) are offset-coordinate diagnostics only.
7. **Rec₀ is crude:** offset free below ℓ, direction to τ/R. Its full definition is open (#410 R4).

## Provenance

| file | sha256 |
|---|---|
| `foam.py` | `6802133ccd16e648a26c0321ab2a7411c9163296d03e1848c1ea8f47edb0f49f` |
| `foam_g1.txt` (`python3 foam.py g1 1001`) | `89c2b93e002362baf724119f5fcabb2d95ae4d024d21e546334b4fd20b0da42c` |
| `foam_mirror.txt` (`python3 foam.py mirror 1001`) | `ca96102af029e690c128e4e506496df2c3b3694e7f88a4453ebe1254f3071e49` |
| `scatter3.py` | `9486da16b008e8c78dbf83a448c0ee7db73851eaa4e86c1fed9300b87674c4f8` |
| `scatter3_out.txt` | `82b1baadf85efbf790756e532f1550355d766d338cda789459b98bc26b517b35` |
| `ellis.py` | `40eaeb5e06d33843c4f1ee672fa290e6382da804aac6e61fbf9d53c8a90778a4` |
| `ellis_out.txt` | `bf1f6d1155a7c404fa9759640f7bff2245a669e08166e3321ba7800ef19368e7` |
