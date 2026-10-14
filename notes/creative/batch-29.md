# Batch 29: many handles along the path. Ballistic or diffusive, and are several W_i still non-empty? (structure-only; Lead ruling; do not merge)

**Status.** A Lead ruling (Physics Lead) runs Claude review 019's next step.
- **Structure-only:** detector reachability only. No counts of worlds, no measure, no Born input; (M1) is untouched.
- **Scope:** 2D, point test particle; λ_E is left to David. Nothing goes into `versions/` or `papers/`. Citations are unchecked unless marked.
- **Branch:** stacked on batch 28 (#413 at 959fa13, merged here in 2bd2328). Ledger rows L136–L140.

## For David (plain summary)

- **The question.** In batch 28 one tiny handle could send the particle to any detector. But the same strong bending, repeated at many handles, might scramble the path so badly that it never arrives in a straight-ish way. We placed handles all along the path at spacing s and asked two things: when does the flight stay roughly straight, and are several detectors still reachable then?
- **Answer (toy).** There is a clear crossover at s ≈ √(4·a·R), about 110ℓ here (ℓ the micro scale: about 50 handle spans of 2.2ℓ, or about 370 mouth radii). That is where the typical straight run between handle encounters, about s²/(4a), reaches the lab size R.
  - **Sparser than that:** arriving paths meet 0–6 handles. The flight is ballistic, a few straight legs, and, with the handle we placed in front of the emitter, every one of the 21 detectors is reached by a path that meets only that handle (Claude 020; our coarse grid finds fewer, a lower bound).
  - **Much denser** (s ≤ 20): paths that arrive have met hundreds to thousands of handles, and most launches on our grid are turned back out of the foam; a few are still inside it at our step limit. We call this "diffusive" by analogy with a gas of scatterers; we didn't measure spreading.
  - **So both conditions hold together in a window of spacings, about 110ℓ to 335ℓ here:** sparse enough for straight flight, dense enough that the thin tube of launches the lab cannot tell apart still meets a mouth. Our runs place a handle in that tube by hand; without it, foam sparser than about 335ℓ leaves the tube empty unless a mouth happens to sit in it, and then only one detector can fire. In dense foam the computer cannot follow a path through hundreds of encounters (double precision lasts about five), so whether several detectors stay reachable there is open. In the sparse window every launch arrives or leaves the foam within our step limit (an earlier flag said otherwise; it came from a slip in the code). And under the lock, a lab with handles in it is only approximately flat, never exactly. That matches your "dense but not TOO dense" proposal (still held open) in a concrete, two-sided way: "dense" means a mouth inside the tube of launches the lab cannot tell apart, and "not too dense" means a free run between throat encounters longer than the lab.
- **Review round 020 (Claude review 020; applied by Lead ruling, Physics Lead).**
  - The window has two edges, roughly 110ℓ to 335ℓ. Below it, the flight wanders. Above it, the thin tube of launches the lab can't tell apart usually contains no handle at all, and then only one detector can fire. Our runs had put a handle in that tube by hand.
  - A code slip (the "didn't arrive" marker was also detector −1's number) is fixed and rerun. Detector −1 now shows up where it should, and every launch in the sparse window arrives or leaves.
  - In dense foam the computer can't follow a path through hundreds of handles, so whether detectors stay reachable there is open.
- **Is it chaotic?** One handle: no, the map is smooth. Clusters of four or more handles close together (2×2 and 3×3; two handles were not run): the signs of chaotic scattering appear. As we refine the launch grid, the number of outcome boundaries keeps growing like a power of the resolution, and the longest run of passes grows too, by roughly a fixed amount per tenfold refinement.
- **A smooth throat, inside the analytic lock, does the same.** For a smooth analytic neck (Ellis-like), the particle that skims the throat winds round it many times. On our grid every one of the 21 detectors is reached by rays that stay on the emitter's side. This is a neck joining two sheets, not a handle; a smooth handle is still not computed.

## Setup

**Foam (`foam.py`).**
- The plane is tiled by cells of side s for x > 5 − s/2. Each cell holds one seam handle: mouth disks of radius a = 0.3ℓ, 1.6ℓ apart, at a fixed pseudo-random offset inside the cell (no overlaps).
- Cell (0,0) holds batch 28's handle at M₁ = (5, 0), placed by hand in every run, so every launch tube contains a mouth whatever s is (Claude 020 R1).
- Gluings, at θ = 0: G1 (non-orientable) or mirror (orientable). Both use the normal flip, and the outward exit is asserted. At θ = 0 both inverses are exact (Claude 019 S1).
- Launch from (0, y₀), with y₀ ∈ [−ℓ/2, ℓ/2] (sub-ℓ) and |φ| ≤ 0.4τ/R.
- Detectors: 21 contiguous apertures of width Δ = 50ℓ at x = R = 10⁴ℓ.
- Outcomes:
  - a detector index;
  - None: crosses x = R outside the array, or leaves (x < −s or |y| > 3R);
  - "no arrival within cap": the step cap is 40R/s + 200 loop steps (cell crossings and seam passages), recorded with a code that is not an aperture index (Claude 020 R2).
- Grid: 1001 × 3 (a lower bound, coarse because the dense cases are slow).
- Encounter numbers are reported only for paths that reach a detector, as a diagnostic in the launch-offset coordinate, not a size of any W_i.
- Free run between throat encounters: ℓ_free = 1/(nσ) = s²/(4a), with σ = 2a (the 2D cross-section is the disc's full width) and n = 2/s² (two mouths per cell). This is the 2D Lorentz-gas mean free path (Santaló's mean-free-path formula; Bunimovich–Sinai 1981; Bunimovich–Sinai–Chernov 1991; Boltzmann–Grad limit: Gallavotti 1969, Spohn 1978, Boldrighini–Bunimovich–Sinai 1983 [V-meta]) [checked by Geometry]. For periodic layouts the free-path law is not exponential (Marklof–Strömbergsson 2010 [V-meta]); this foam is pseudo-random per cell. At ℓ_free = R a path still meets about 1 handle on average over straight lines (the kinematic average of Santaló's formula, a property of the layout, not a weight on worlds).

**Cluster (`scatter3.py`).**
- K × K handles at spacing s₀ (G1 or mirror, θ = 0) in an empty plane, with incoming parallel rays and an outcome of exit sector out of 8.
- Diagnostic: the number of outcome changes C(n) on n offsets across the cluster, n = 10³…10⁶, and the largest number of passes.
- A piecewise-smooth map saturates C(n). A fractal boundary gives C(n) ~ n^D with 0 < D < 1.

**Smooth throat (`ellis.py`).**
- The 2D Ellis neck ds² = dr² + (r² + a²)dφ², which is analytic (the equatorial slice of the Ellis drainhole: Ellis, J. Math. Phys. 14 (1973) 104 [V-meta]; Bronnikov 1973 [unverified]; geodesics: Chetouani–Clément 1984, Müller 2008 [V-meta]). Geodesics are integrated with scipy DOP853 at rtol 1e-11.
- The numerical sweep matches the closed form 2K(a/b) to 6 digits (b = a(1 + 10⁻¹…10⁻⁶)).
- Reflected rays are continued straight from the neck to the 21-aperture line at distance R. 4500 impact parameters are clustered at b = a.

## Results

**Foam, reached sets** (lower bounds; G1 / mirror; rerun after the cap-code fix, Claude 020 R2: aperture −1 joins G1 at s = 110 and 200 and mirror at s = 200, and no launch is capped at s ≥ 50 for either gluing; no other set changed on this platform. Platform: Linux x86_64, Python 3.13.5, numpy 2.2.4; pins hold on this platform only, Claude 020 R3):

| s (ℓ) | ℓ_free ≈ s²/4a | G1 reached | mirror reached | encounters on arriving paths (G1; mirror) | regime |
|---|---|---|---|---|---|
| 5 | 21 | 0 | 0 | none arrive; none arrive | diffusive, no arrival within cap |
| 10 | 83 | 1 | 0 | 2590; none arrive | diffusive |
| 20 | 333 | 4 | 2 | 172–652; 136–178 | diffusive |
| 50 | 2.1×10³ | 12 | 8 | 6–53; 3–26 | crossover |
| 110 | 1.0×10⁴ (≈ R) | 14 | 11 | 1–6; 1–6 | ballistic (a few legs) |
| 200 | 3.3×10⁴ | 17 | 11 | 0–3; 0–4 | ballistic |
| 500 | 2.1×10⁵ | 5 | 4 | 0–3; 0–2 | ballistic, single-handle-like |
| 2000 | 3.3×10⁶ | 4 | 4 | 0–2; 0–2 | single-handle |

For s = 2000 (and for the mirror also at s = 500; G1 at s = 500 adds index 2) the coarse sets match batch 28's coarse single-handle sets: {0, 3, 4, 5} for G1 and {−5, −4, −3, 0} for mirror. Launches aimed at the one-pass intervals of batch 28's handle (101 per aperture, φ = 0) reach all 21 apertures after a single encounter at s = 110, 200, 500 and 2000, for both gluings; at s = 50 only 3 (G1) and 5 (mirror) do, the rest meeting a second mouth (Claude 020). The cone is never fully clear (the 0.1 rad wedge from the handle to the array holds about 10⁷/s² mouths), but a mouth r away shadows only 2a/r rad, less than one aperture once r ≳ 2aR/Δ = 120ℓ.

**Cluster, C(n)** (n = 10³, 10⁴, 10⁵, 10⁶):

| gluing | K = 1 (s₀ = 4) | K = 2 (s₀ = 4) | K = 3 (s₀ = 4) | K = 3 (s₀ = 2.5) |
|---|---|---|---|---|
| G1 | 27, 28, 28, 28 (saturates; max 2 passes) | 64, 168, 500, 1550 (max passes 3 → 7) | 86, 329, 1497, 6822 (5 → 10) | 114, 498, 2708, 15218 (10 → 17) |
| mirror | 31, 46, 65, 78 (slow growth; 4 → 6) | 59, 183, 523, 1694 (4 → 8) | 90, 343, 1376, 6112 (4 → 10) | 113, 468, 2157, 11094 (6 → 13) |

- For K ≥ 2 (4 or more handles), C(n) grows by a factor of about 2.6–5.6 per decade (local log-slopes about 0.4–0.75, rising at first and then levelling off: G1 K = 3, s₀ = 2.5 gives 0.64, 0.74, 0.75 and then 0.745 from n = 10⁶ to 10⁷; G1 K = 2 gives 0.42, 0.47, 0.49 and then 0.488; Claude 020), and the longest pass sequence grows with resolution. C(n) estimates the box dimension D = 1 − α of the boundary set (α the uncertainty exponent). D ≈ 0.4–0.75 is a range of local slopes, not a converged dimension; smooth boundaries and grazing roundoff bias it. These are the signatures of a fractal repeller (chaotic scattering; cf. Gaspard–Rice 1989, Ott–Tél 1993, bibliographic only).
- For one handle, G1 saturates, which is piecewise smooth (batch 28, Geometry N1–N4). The mirror's slow growth is consistent with its single unstable periodic orbit (Claude 019 N6).

**Smooth throat.**
- Reflected rays reach all 21 detectors and None, and transmitted rays exist (to sheet 2).
- The sweep near b = a grows like ln(1/(b − a)) (11.29 at 10⁻⁴, 15.89 at 10⁻⁶), so every direction recurs in each thin window of b. The result is exact by continuity and the IVT, as in Claude 019 S3. From the closed form, each aperture's b-interval is about 10⁻⁶ℓ wide on the first winding (b − a ≈ 1.9×10⁻⁴ℓ) and about 2×10⁻⁹ℓ on the second. Without any winding, the far field (deflection ≈ (π/4)(a/b)² for b ≫ a) sends reflected rays with b from 1.18ℓ to 2.03ℓ, a sub-ℓ window, into apertures 4–10 (ellis.py's sign convention) on intervals 0.06–0.24ℓ wide (Claude 020).

## Findings

1. **Ballistic window (L1, toy).** The foam is ballistic, with arriving paths of a few legs, when ℓ_free ≈ s²/(4a) ≳ R, i.e. s ≳ √(4aR) ≈ 110ℓ here. For s ≲ 20ℓ paths wander ("diffusive" by Lorentz-gas analogy only; no displacement statistics). In the ballistic window every W_i stays non-empty when a mouth lies in Rec₀'s launch tube (all 21 by single-encounter launches at s = 110–2000; Results), but here that mouth is the handle placed by hand in cell (0,0). The tube (area A ≈ R(ℓ + 0.4τ + 2a) ≈ 5.6×10⁴ℓ²) holds about 2A/s² of the foam's own mouths, fewer than one for s ≳ √(2A) ≈ 335ℓ; with none, every launch flies straight and one W_i is non-empty (two if the tube's 9ℓ-wide end straddles an aperture edge), as in foam.py's layout without the override at s = 500 and 2000 (Claude 020). So **"several W_i non-empty" and "ballistic flight" hold together for √(4aR) ≲ s ≲ √(2A), about 110–335ℓ,** in this toy; the factor of about 3 between the edges, √((ℓ + 0.4τ + 2a)/(2a)), is set by the launch freedom Rec₀ leaves compared with the mouth size. In dense foam the flight is not ballistic. Whether several W_i stay non-empty there is not settled by this computation: the s = 20 hits come after hundreds of encounters, but launches 10⁻¹⁵ℓ apart already hit different mouths by the fifth or sixth encounter, so those paths are roundoff-driven (whether true paths shadow them is unchecked; Claude 020 R3).
   - This is a concrete, geometric, two-sided reading of David's 5:26 PM "dense but not TOO dense": dense enough that Rec₀'s launch tube meets a mouth, not so dense that the flight wanders (Claude 020 R1). It differs from batch 27's Creative Lead reading (micro-error ~ℓ/λ below ε with an unbiased stable norm), which is about distances, not flight. It also bounds regime 2's open "L-dense": the window needs L at least of order √(4aR) ≈ 110ℓ here (in 3D, heuristically, ballistic flight needs s ≳ (2πa²R)^{1/3}), which batch 26's ordering ℓ ≪ L ≪ R allows. That proposal is still held open, not adopted.
   - Note that "not too dense" here is a condition on *geodesic flight* (ℓ_free ≳ R), which regime 3 alone does not secure (Claude 019 S4).
2. **Chaos needs at least two handles that can see each other; nearby clusters show it clearly (L1).** One handle gives a piecewise-smooth map. Clusters of four or more handles (2×2, 3×3) within a few ℓ of each other show growing boundary counts and pass numbers (a two-handle cluster, four mouths, is the analogue of the three-disk condition, Gaspard–Rice 1989, Eckhardt 1987 [V-meta], and is plausible but not run), consistent with a fractal (chaotic-scattering) exit structure. In the ballistic window, encounters along a path are typically 0–6 isolated handles, so no cluster is involved; still, only a single-encounter path has the single-handle kind of sensitivity, and each further encounter multiplies it by about 2L/a (L the leg length; about 10⁴ or more for s ≥ 110), which is why the coarse sets there depend on roundoff (Claude 020 R3). Widely spaced handles should still form a repeller, with a smaller dimension (three-disk analogy; not computed).
3. **A smooth analytic throat gives the same reachability (L1).** The Ellis neck's logarithmic winding reaches every detector from the emitter's sheet. That moves the *mechanism* inside the lock (analytic geometry), though not yet as a handle, and, like the seam result, within one fixed geometry. Its total curvature is ∫K dA = −4π, the same Gauss–Bonnet budget any one-sheet handle needs. Under the lock, a world with handles is curved near each of them, so lab flatness is only the approximate regime 3, never exact on an open set (identity theorem). The neck's far field acts out to a few ℓ (deflection beyond the array's half-angle for b < 1.18ℓ; more than one aperture per ℓ of offset for b ≲ 3ℓ), so for smooth throats both edges of the window move to larger s [not computed; Claude 020].

## Unchecked steps

1. **No smooth analytic handle is computed.** The Ellis neck is a two-sheet neck; turning it into a one-sheet handle needs a second neck or a seam, i.e. more curvature, with the total fixed at −4π per handle by Gauss–Bonnet. The foam uses non-analytic seams (outside the lock; Claude 019 R1, applied in batch 28).
2. **2D only, point particle.** This is the λ_E ≲ ℓ case of #410 §4 condition 7. λ_E is left to David, and a particle with a length must re-derive all of this.
3. **Coarse grids (1001 × 3) for the foam.** The sets are lower bounds. For s ≤ 200 they also depend on roundoff: each encounter multiplies an offset error by about 2L/a (L the leg length), so double precision follows a path for only about five encounters; moving every launch by 10⁻¹⁵ℓ, or the layout hash by one ulp, changes the sets, and a rerun on macOS differs from the pins at s = 10–110, so the pins hold only on the platform that made them, which should be named (Claude 020 R3). Single-encounter witnesses are immune and give all 21 for s ≥ 110 (Results).
   - The step cap biases the dense cases: "no arrival within cap" is not the same as "never arrives". The cap allows about 40 straight crossings, but a wandering crossing needs about 4aR²/s³ cell steps (1.5×10⁴, 1.2×10⁵ and 9.6×10⁵ at s = 20, 10 and 5, against caps of 2.0×10⁴, 4.0×10⁴ and 8.0×10⁴), so at s ≤ 10 the launches still inside at the cap might yet arrive; most grid launches, though, are turned back out of the foam long before it, and the few detectors reached at s ≤ 20 say how few grid launches cross the slab, not which W_i are empty (Claude 020). The cap flags at s = 110 (G1) and s = 200 (both) were hits on aperture −1, which foam.py also used as its cap code; with a separate code no launch is capped at s ≥ 50 (Claude 020 R2). "Diffusive" is a label by Lorentz-gas analogy (many encounters before arrival); no displacement statistics were computed, and Bunimovich–Sinai-type diffusion theorems are for billiard collisions, not seam passages.
   - ℓ_free = s²/(4a) is the random-layout value (approximate for this per-cell layout), and the cell-based foam has a pseudo-random but fixed layout (one world geometry per s).
4. **The fractal dimension is rough.** It comes from three decades of n, plus a fourth for two cases (Claude 020). An independent implementation and a translated copy of the cluster reproduce C(n) in five of the eight cases (exactly for K ≤ 2; to within 10 of 15,218 for G1 K = 3, s₀ = 2.5), and no ray reaches the 4000-pass cap, so the growth is not a cap or roundoff artifact. There is no Lyapunov exponent or escape-rate computation.
5. **The Ellis continuation** treats the ray as straight from the neck. The residual curvature on sheet 1 beyond r = 60ℓ = 200a (script rout = 60 with a = 0.3) and the emitter–neck geometry are simplified. The residual angle there is ~(a/r)² ≈ 2.5×10⁻⁵ rad, far below the aperture angle Δ/R = 5×10⁻³ (Geometry).
6. **No measure.** Nothing says how large any W_i is; encounter numbers and C(n) are offset-coordinate diagnostics only.
7. **Rec₀ is crude:** offset free below ℓ, direction to τ/R. Its full definition is open (#410 R4). It sets the window's upper edge: with the direction fixed ten times better (0.4ℓ/R) the factor between the edges falls from about 3 to about 1.8, and with the offset fixed below the sliver widths the window closes. **Next step (Claude 020):** remove the hand-placed handle, launch from many emitter placements, keep only witnesses that roundoff cannot move (single encounters, or launches aimed at each one-pass interval), and map the two-sided window against s and against Rec₀'s angular freedom; then close two analytic necks into a one-sheet handle and redo the window with its far field.

## Provenance

| file | sha256 |
|---|---|
| `foam.py` (cap code −999, Claude 020 R2; docstring N9) | `bbb851cfb4499f2f96b7247ca69bcf06db8ae8df4555a744f21c9080003a4f15` |
| `foam_g1.txt` (`python3 foam.py g1 1001`) | `2ff830004e1600077d14b555c4a07fe0939e3daf488f6533bc659e352f997581` |
| `foam_mirror.txt` (`python3 foam.py mirror 1001`) | `6c723fb51e321713c2187c52d10be817b561dbdaa6a277f74c709a0c21b2a87e` |
| `scatter3.py` (docstring only changed, N9; not rerun, output unchanged) | `4b86adbea27ac6784a2d69db7e27528f5c79e35cc357de60459048775638d3f5` |
| `scatter3_out.txt` | `82b1baadf85efbf790756e532f1550355d766d338cda789459b98bc26b517b35` |
| `ellis.py` | `40eaeb5e06d33843c4f1ee672fa290e6382da804aac6e61fbf9d53c8a90778a4` |
| `ellis_out.txt` | `bf1f6d1155a7c404fa9759640f7bff2245a669e08166e3321ba7800ef19368e7` |
