# Batch 25: Set 7 kill check: conducting slit walls (Creative Lead; do not merge)

**Status.** Structure only, test-particle dynamics; classical; no Born rule; no $|a|^2$; (M1) untouched at L3. Citations are bibliographic only, per Literature, unless marked. Nothing goes into `versions/` or `papers/`. Stacked on batch 24 (#408 at 84cfe37). Ledger rows L102–L106.
- Script: `notes/creative/batch-25/walls.py` (sha256 `fed25b1902a62dfb9def781975adbc46439a40ac510027bded488fd5419cca73`).
- Output: `results.txt` (sha256 `7557bf22948171ce55bf11ed9c6abf30ce47efb372f808fede0c1a7e5c569c13`).

**Lead ruling (Physics Lead), not David's** (10:12 AM ET 2026-10-13): batch 25 runs the Set 7 kill check, with conducting slit walls, structure only.

**Carried forward from batch 24:**
- Set 2 stays at **L0–L1**.
- The zero-solution bands in the two non-orientable gluings stay **open**: possibly enumeration truncation, pending a multi-traversal search, and slit-independent.

---

## For David (plain summary)

- **The question.** Real slits are cut in a metal plate. A charged particle pulls charge around in the metal, and that charge pulls back on the particle. Opening the second slit changes the metal, so it changes that pull, even on particles going through the first slit. Could this make dark bands?
- **What we did.** We modelled a flat earthed metal plate with one or two slits and computed the pull the plate exerts on a charged particle at every point. Then we traced the particles through slit 1 to the screen, with slit 2 closed and then open. We scanned slit separation, slit width and the strength of the pull, all fixed in advance.
- **What we found.**
  - Opening slit 2 does move slit-1 particles, but only slightly: at most 0.12 screen units, and usually around 0.001–0.03.
  - The shift is smooth. Nothing folds over, and no repeating pattern appears.
  - In the one setup where the two one-slit patterns overlap, no spot with both slits open is darker than both of them. In the other eleven setups the patterns don't overlap, so that test said nothing. A rerun with a wider source, where the patterns do overlap in every setup, found no dark spots and no repeating pattern.
- **This matches experiments.** With real atoms and electrons, wall forces only shift and reshape a fringe pattern that the wave already makes. The fringes themselves need the wave.
- **Verdict.** In this model, conducting walls give a smooth deformation, not interference. The dark-band test was only possible in 1 of 12 setups, so a wider-source run was needed; it found no dark spots (see Extended-source scan). None of the lengths involved is tied to the particle's momentum.

---

## Model and regime

- **Why 2D.** The plate is translation-invariant in z, and the particle is a line charge q per unit length, with a log potential. 2D keeps the boundary-element solve exact up to discretisation, and is the cheapest geometry where an aperture changes the induced charge. A 3D plate with holes and a point charge was not done.
- **Plate.** A grounded thin conducting plate on y = 0, |x| ≤ 10, with slits of width w centred at x = ±a/2. With one slit, only x = −a/2 is open.
  - Boundary elements: N collinear panels with constant charge density, collocation at the panel centres, kernel −ln r.
  - For a particle at p, the induced density is σ(p) = −A⁻¹φ_p, and its field acts back on the particle. This is the image force; the particle's own field is excluded.
- **Dynamics.** Nonrelativistic and quasi-static: the induced charge follows the particle instantaneously. No radiation and no radiation reaction. Test-field limit (#392): no metric back-reaction.
- **Coupling.** Acceleration = κ Ẽ(p) with κ = q²/(2πε₀ m v₀²), a length. **Speed and charge enter only through κ**, so the κ scan covers both.
- **Layout.** The source is at (0, −5) and the screen at y = 10. There are 1500 launches spread over 2.5× the angular width of slit 1. Integration is RK4 with dt = 0.005, using the field tabulated on a 0.05 grid. A ball meeting metal, or coming within 0.02 of it, is absorbed.
- **Launch weighting.** Uniform in θ. This is **a histogram convention for the dark-spot test, not a probability rule**.
- **Scan:** a ∈ {2, 4}, w ∈ {0.5, 1}, κ ∈ {10⁻³, 10⁻², 10⁻¹}, all set in advance. Slit-2 launches come from mirror symmetry.

## Results [N] (results.txt)

**Convergence** (a = 2, w = 0.5, κ = 0.01, against N = 800 panels):
- The absolute hit error at N = 400 is 6.7e−2 max and 1.6e−3 median; it is dominated by edge-grazers.
- That error **cancels in the one-vs-two-slit difference**. The error in the shift at N = 400 is 2.2e−4 max and 2.5e−5 median, against a shift of 1.3e−3 max and 8.1e−4 median.
- So the shift is resolved to about 17% worst case (2.2e−4 / 1.3e−3) and 3% typical. The worst case is at edge-grazers, where uniform panels under-resolve the d^(−1/2) edge density (graded panels or Richardson would fix this). Analytic check (Geometry): with no slits, the field matches the image value −1/(2y) to 0.3% at Lb = 40. That is why it can be trusted although the absolute hits are less accurate.
- The absorbed counts are identical across N.

| a | w | κ | absorbed (1 slit / 2 slits) | max shift of slit-1 hits | folds (1 / 2) | overlap bins | bins with I_both < min(I₁, I₂) |
|---|---|---|---|---|---|---|---|
| 2 | 0.5 | 1e−3 | 978/978 | 9.4e−4 | 0/0 | 0 | 0 (vacuous) |
| 2 | 0.5 | 1e−2 | 976/975 | 2.1e−3 | 0/0 | 0 | 0 (vacuous) |
| 2 | 0.5 | 1e−1 | 965/965 | 2.9e−2 | 0/0 | 0 | 0 (vacuous) |
| 2 | 1 | 1e−3 | 950/950 | 1.5e−3 | 0/0 | 0 | 0 (vacuous) |
| 2 | 1 | 1e−2 | 950/949 | 6.1e−3 | 0/0 | 0 | 0 (vacuous) |
| 2 | 1 | 1e−1 | 938/937 | 1.2e−1 | 0/0 | 12 | **0** |
| 4 | 0.5 | 1e−3 | 1039/1039 | 2.5e−5 | 0/0 | 0 | 0 (vacuous) |
| 4 | 0.5 | 1e−2 | 1036/1036 | 2.3e−3 | 0/0 | 0 | 0 (vacuous) |
| 4 | 0.5 | 1e−1 | 1023/1024 | 1.4e−2 | 0/0 | 0 | 0 (vacuous) |
| 4 | 1 | 1e−3 | 1010/1010 | 2.3e−3 | 0/0 | 0 | 0 (vacuous) |
| 4 | 1 | 1e−2 | 1008/1008 | 3.2e−3 | 0/0 | 0 | 0 (vacuous) |
| 4 | 1 | 1e−1 | 996/996 | 4.8e−2 | 0/0 | 0 | 0 (vacuous) |

The absorbed counts are mostly launches outside the slit window, which hit metal by design. The local minima of I_both − I₁ − I₂ are 0 in every case.

## Answers

- **Does slit 2 change slit-1 trajectories?** Yes. That is contextual dynamics (Lemma A′ exit (iii), #407). The effect is small, grows with κ, and falls with slit separation.
- **Dark bands below both one-slit patterns?** None in the one case where the test applies (a = 2, w = 1, κ = 0.1; 12 overlap bins). **In the other 11 of 12 cases the test is vacuous**, because the one-slit patterns don't overlap. The deviation I_both − I₁ − I₂ has no repeated minima in any case.
- **Fold or exclusion?**
  - No folds in any case: x_hit stays monotone in θ. Geometry checked independently at 3000 launches, κ = 0.1: each transmitted set is one contiguous θ-run with dx_hit/dθ > 0, and there are no interior absorption gaps.
  - Exclusion changes by at most 1 launch in 1500, always an edge-grazer. It sits at the slit edge, not in bands.
- **Length scales.** a, w, the plate size, the source and screen distances, and κ (∝ 1/v₀², an electrostatic coupling). Nothing gives a spacing ∝ 1/p, and **no length ties to momentum as a wavelength**.
- **Prior art** (bibliographic only, per Literature):
  - Grisenti et al., PRL 83 (1999) 1755. The wall potential changes the relative intensities of diffraction orders.
  - Perreault & Cronin, PRL 95 (2005) 133201. The wall interaction adds a phase shift to an existing atom-wave pattern.
  - Barwick et al., J. Appl. Phys. 100 (2006) 074322. Abstract V-text: the image-charge potential is measured within "a quantitative path integral analysis", i.e. inside a wave analysis.
  - Also (V-meta): Brühl et al., EPL 59 (2002) 357; Gronniger et al., APL 87 (2005) 124104 and NJP 8 (2006) 224; Bach et al., NJP 15 (2013) 033018.
  - **In experiments, wall and image forces shift the phase and envelope of a pattern the wave already makes. The fringes need the wave.** A classical image force on point particles reproduces only the shift and envelope part, which is what batch 25 finds.


## Extended-source scan (`extsrc.py`)

Script: `notes/creative/batch-25/extsrc.py` (sha256 `512bbec55d4d01de7687c0b6ebf858be52900c0b66b3e8d0ca84f0b7dce39547`); output: `extsrc.txt` (sha256 `ed40f97ec01e45757c1dd3bde7258be734c47274b31c0d0eeffff507fdb5f3eb`). `walls.py` is unchanged and imported.

**Setup.**
- **Source:** a segment y = −Ds, |x| ≤ S, with S = f·S_min, S_min = (a − w)(Ds + D)/(2D), and fixed margins f ∈ {1.5, 3} (not tuned).
- **Launches:** 60 uniform source positions × 200 uniform angles covering slit 1 ± one slit width. This is a histogram convention, not a probability rule. Slit-2 launches come by mirror symmetry.
- **Unchanged:** the same a, w and κ grid as before, the grounded plate with R0 = 1, and 400 panels.
- **Screen bins:** 0.1 wide.
- **Dark-bin test:** in overlap bins (I₁ > 0 and I₂ > 0), z = (min(I₁, I₂) − I_both)/√(I_both + min) (Poisson convention). A dark bin needs z > 3.
- **Periodicity:** local minima of dev = I_both − I₁ − I₂ beyond 3σ, and the largest FFT peak of dev over the overlap region relative to its mean (reported, no threshold set in advance).
- **Spot check** at 800 panels.

**Results [N].**
- **Overlap now exists in every case:** 14–288 overlap bins (table in `extsrc.txt`).
- **Dark bins (z > 3): 0 in all 24 cases.** The largest z in every case is *negative*, between −5.0 and −2.0: I_both lies above min(I₁, I₂) by 2–5σ in every overlap bin.
- **The deviation from additivity is within noise.** max |I_both − I₁ − I₂|/σ is 0.00–1.27, so the smooth wall shift is invisible at these statistics.
- **Periodicity:** 0 dev minima beyond 3σ in every case. The FFT peak-to-mean ratios (0–5.7) are what noise gives for spectra of this length (no threshold was set in advance, and dev itself is < 1.3σ). There is no periodic structure.
- **Spot check** (N = 800; a = 2, w = 1, f = 1.5, κ = 0.1): 68 overlap bins (58 at N = 400), 0 dark bins, max z −3.99, max |dev|/σ 1.97, 0 minima. The conclusion is mesh-independent.
- **Side observation:** at κ = 0.1 with a = 4, the wide sources lose more transmitted launches with two slits (e.g. 3309 at f = 3 for w = 0.5). That is wall capture of oblique launches, a smooth exclusion. In those cases it does not create dark bins.

**Verdict.** No dark bins beyond noise, and no periodic structure, with overlapping one-slit patterns in all 24 cases. **Set 7 is confirmed at L0** within the limits below: 2D line charges, a quasi-static grounded plate (R0 = 1), κ ≤ 0.1, an absorbing rim of 0.02, and source margins of 1.5× and 3×.

## Which-route kill condition

- **Passive record** (uncharged, non-interacting, test limit): no change to the induced field, and so no change to the hits.
- **Active record** (a conductor or charge at a slit): it changes the induced charge, adding its own smooth deflection. An active record that screens slit 2's influence (for example a grounded body filling it) removes any slit-2 dependence. No bands exist for any record to kill.

## Verdict on Set 7

Smooth contextual deformation and no bands. **Set 7 drops to L0 provisionally, pending an extended-source scan with overlapping one-slit patterns, within these limits:** (**Update:** the extended-source scan below confirms L0; the dark-band test is no longer vacuous.)
- 2D line charges;
- a quasi-static, grounded plate;
- κ ≤ 0.1;
- an absorbing rim of 0.02;
- a dark-band test that is vacuous in 11 of 12 point-source cases, now covered by the extended-source scan (overlap in all 24 cases, 0 dark bins).

It could reopen only with a nonlinear regime (strong coupling folding the map), or with overlapping patterns showing below-both bins that are periodic and not tuned.

## Weak points

1. 2D line charges, not 3D point charges with holes.
2. Quasi-static: no retardation, no radiation. Retarded walls would add echoes as in batch 22, which were smooth there.
3. The one-slit patterns overlap in only 1 of 12 cases, and that is structural: with a point source and straight lines, slit k images to x_k(1 + D/Ds) ± (w/2)(1 + D/Ds), so the patterns overlap only if w > a. The single overlap comes from deflection. A wider launch spread or a different screen distance cannot help; an extended source of half-width S > (a − w)(Ds + D)/(2D) can (Geometry, #409). The dark-band test needs that scan.
4. The field grid of 0.05 and the 0.02 absorption distance make edge-grazers uncertain. The convergence check covers the shift, not those launches.
5. A grounded plate only. In 2D, "grounded" for a finite plate depends on the reference length R0 in −ln(r/R0); R0 = 1 is used. A becomes singular at R0 = Lb/2 (the log capacity). Geometry's check: the field changes by about 5% for R0 = 1, 10, 100 and by about 25% for a floating (neutral) plate. The qualitative results are unaffected; the magnitudes are convention-dependent.

Ledger: L102–L106 (L106 records the Lead ruling).
