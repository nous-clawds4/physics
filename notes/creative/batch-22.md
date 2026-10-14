# Batch 22: the returning echoes, computed (Creative Lead; do not merge)

**Status.** Exploration only. Classical only; test-field limit; no Born rule; no $|a|^2$; no superposition by hand; (M1) untouched at L3; CTCs as exploration only. Citations are bibliographic and unchecked unless marked. Nothing goes into `versions/` or `papers/`. Stacked on batch 21 (#405 at 7263adf). Ledger rows L85–L89. Script: `notes/creative/batch-22/echoes.py` (sha256 `08057d2c27731dcf5491b5bfc57025be51b80a636f459995ec9b2a0aeeb0d790`); output: `results.txt` (sha256 `9b0027ca2d6e0c3b94dbea63a0e080665405bcf72d622ca68d9041222388fc09`); step-size check `dtcheck.py` (sha256 `686985f02a227a6697da077df9d149452c417c1aa16254220defe9bf8d85e3c8`), output `dtcheck.txt` (sha256 `470b37226c3075f5cea549f81e8c920297a0d599c808a2f0f5d1b25e4d8815a0`). Rerun after Geometry's pre-launch fix (#406 review M1): images now carry zero acceleration before launch.

**David, 9:10 AM ET 2026-10-13, relayed by Physics Lead, Physics Lead chat, not signed:**
> Let's have creative lead model the returning echoes.

---

## For David (plain summary)

- **What we did.** We gave the particle a small charge and let it be launched, which makes it radiate. The radiation goes round the wrap and comes back. We computed the push those returning echoes give the particle, and where it lands as a result.
- **Result.** The echoes do push the particle. But the push changes smoothly with launch angle, a gentle overall squeeze like a weak focusing lens. There are no bands: no repeating light-and-dark stripes.
- **No natural wavelength.** The effect simply grows as the wrap gets smaller (roughly as L^−1.3) and barely depends on speed. Nothing sets a stripe spacing.
- **Two slits.** The echoes a particle feels come only from its own path, and a neutral slit it didn't go through doesn't change them. So opening the second slit still just adds the two one-slit patterns (batch 21 Lemma A). There are no dark spots.
- **Records.** A passive route record changes nothing. A field-coupled one adds another smooth push, and there are no bands for it to remove.
- **Verdict.** In this model, the echoes give smooth distortion, not interference. (An earlier version overstated the size about 50× because of a script bug, now fixed.) This is unlike the droplets, whose wave is kept going by the bath and so lasts.

---

## Model (and why)

- **Space and launch.** Flat cylinder: 3+1 dimensions, space $\mathbb R^2\times S^1$ ($x\sim x+L$), motion in $z=0$, $c=1$. (In 2+1 the field has tails inside the light cone; not done.) The charge is at rest at the origin for $t<0$. It is then launched at angle θ, with constant acceleration to speed $v$ over time $\tau$. The screen is at $y=D$.
- **Slit crossing.** An optional slit kick is a transverse $\delta v_s$ over $\tau$ at $y=y_s$. A neutral, ideal aperture exerts no force; the kick stands in for a real slit interaction and is shown at one value only.
- **Image fields.** Images sit at $r+mL\hat x$, $m\ne0$, with the full retarded Liénard–Wiechert fields (velocity and acceleration parts). The retarded time is solved by bisection; before launch, the images' rest (Coulomb) fields apply, with zero acceleration; the image sum is checked by doubling M.
- **Local self-force.** Landau–Lifshitz reduced order, chosen because it is free of runaways and pre-acceleration and agrees with Lorentz–Dirac to $O(\epsilon)$ (reduction of order: Spohn, EPL 50 (2000) 287; Gralla, Harte & Wald, PRD 80 (2009) 024031; bibliographic only, per Literature). It is nonzero only during the prescribed accelerations, where the launcher absorbs it, and zero in free flight.
- **Order.** First order in $\epsilon=q^2/(4\pi\varepsilon_0 mc^2)$, a length. The image force is evaluated on the unperturbed path, and the deflection at the screen is integrated: $\Delta x_{\rm hit}=\epsilon\,f(\theta;v,L,\tau,D)$.
- **Density change.** $\delta=-\partial_\theta\Delta x_{\rm hit}/(D\sec^2\theta)$, so density ≈ baseline × $(1+\delta)$, with baseline ∝ launch weighting × $(D\sec^2\theta)^{-1}$ (batch 21).
- **Parameters.** None was fitted. $D=10$ and $\tau=0.2$ are fixed. Scanned: $L\in\{1.25,2.5,5\}$; $v\in\{0.3,0.5\}$; with and without a slit kick ($y_s=5,\ \delta v_s=0.05$); θ from −10° to 20° in 121 steps. A τ scan was not run. The charge enters only through ε (linear).
- **Validity.** Weak coupling, $|\delta|\ll1$, i.e. $\epsilon\ll1$ in these units (the caustic estimate is ε of order 1, from the rerun). The particle is a test body in a test field (no metric back-reaction, #399 §4). The flat, eternal wrap is fixed.

## Results [N] (results.txt)

Rerun with the pre-launch fix. δ/ε is the first-order relative density change; positive means denser (converging).

| case | $\Delta x_{\rm hit}/\epsilon$ range | mean δ/ε | δ/ε range (incl. step-size noise) |
|---|---|---|---|
| L=2.5, v=0.5 | −4.44 … 2.27 | 1.24 | −0.17 … 2.72 |
| L=2.5, v=0.3 | −4.99 … 2.44 | 1.38 | 0.23 … 2.33 |
| L=1.25, v=0.5 | −10.4 … 5.33 | 2.91 | 0.77 … 5.34 |
| L=5, v=0.5 | −1.81 … 0.91 | 0.50 | 0.04 … 0.90 |
| L=2.5, v=0.5, slit kick | −4.26 … 2.42 | 1.23 | −0.08 … 2.62 |

**M-doubling** (L=2.5, v=0.5, $\Delta x_{\rm hit}/\epsilon$): θ=−10°: 2.270 / 2.367 / 2.393 for M = 12 / 24 / 48. θ=−1°: 0.278 / 0.288 / 0.290. θ=8°: −1.849 / −1.925 / −1.946. θ=20°: −4.428 / −4.649 / −4.709. M=12 is within about 5% of M=48 (the static-chain tail), converging. These agree with Geometry's check values (2.24/2.36, 0.23/0.24, −1.81/−1.90, −4.39/−4.67 at M = 12/48) to within a few per cent; the small differences are step-size noise.

**Step-size noise.** The jitter in δ on a scale of about 1° (the 56–76 sign changes the script counts, and its "period" output) is numerical. Halving dt in `dtcheck.txt` changes the pattern, while the mean (≈1.3) holds. Δx is smooth; the jitter comes from differencing at dt = 0.01. The script's "eps at which delta first reaches −1" line uses the wrong sign for a converging lens. The caustic is at εδ ≈ 1, i.e. ε ≈ 1/δ ≈ 0.4–2 for L = 2.5, of order 1.

- **What it looks like.** $\Delta x_{\rm hit}$ is close to linear in θ: a uniform inward squeeze, i.e. a weak converging lens, plus a small smooth curvature. The mean density change is a squeeze, about 50× weaker than first reported (bug fixed); under normalisation it only rescales the pattern.
- **Residual.** Beyond that, Δx shows only a gentle curvature. The fine jitter in δ is step-size noise (see above). No periodic structure survives the dt check.
- **Physics.** The dominant piece is causal. Until the launch's light front returns from image $m$, at $t\approx|m|L/(1-v\cos\cdot)$, the particle feels the images' fields from *before* launch, i.e. at rest at the launch point. That field is repulsive from the launch point and does not cancel pairwise once the particle has moved. The radiation (acceleration) part adds pulses at each return time. Integrated over flight, they average to a smooth kick. This image (echo) force is the flat-quotient analogue of the tail term of curved-spacetime self-force, the particle's own field returning to it (DeWitt & Brehme 1960; Mino, Sasaki & Tanaka 1997; Quinn & Wald 1997; review: Poisson, Pound & Vega, Living Rev. Relativ. 14 (2011) 7; bibliographic only, per Literature).

## Answers

**(1) Bands? Below baseline?**
- No bands at first order. The density change is smooth in θ, a lens-like squeeze plus a gentle trend (fine jitter is step-size noise).
- Normalised, it lies above the baseline in some places and below it in others by $O(\epsilon)$ smooth amounts. There are no repeated dips.
- **Two-slit:** for neutral, kick-only apertures (a modelling choice: no field boundary conditions), a world's self-force depends only on its own path; conducting walls would make the image field depend on which slits are open and would need Lemma A re-proved, so $p^{\rm both}(w)$ and its hit are as with one slit open. Batch 21 Lemma A then gives the normalised two-slit pattern as a convex blend of the one-slit patterns. **No point falls below both.**
- Only at ε of order 1 (far outside validity) would the squeeze fold into a caustic, and that would be a single focus, not bands.

**(2) Scaling, wavelength?**
- $|\delta|$ falls roughly as $L^{-1.3}$ (values from the rerun): mean δ/ε ≈ 2.91, 1.24, 0.50 for L = 1.25, 2.5, 5 (fitted exponent −1.27).
- It depends only weakly on $v$ (within about 10% for v = 0.3 vs 0.5): mean δ/ε ≈ 1.38 vs 1.24. It is linear in ε by construction.
- No oscillation period appeared, so **no natural length acts as a wavelength**. The available lengths are $L$, $\epsilon$, $v\tau$ and the echo spacing $\sim L/(1-v)$. The last sets the pulse timing, but integration over flight washes it out.

**(3) Records.**
- **Passive** (uncharged counter): it changes nothing.
- **Active** (a conductor or charge near one route): it adds its own images and a smooth, route-specific deflection. It is configuration-dependent, but smooth.
- There are no bands, so recording has nothing to kill. In this model, which-route records and patterns are decoupled.

**(4) Droplets** (bibliographic only: Couder & Fort PRL 97 (2006) 154101; Andersen et al. PRE 92 (2015) 013006; Pucci et al. JFM 835 (2018) 1136; path memory: Fort et al. PNAS 107 (2010) 17515; Eddi et al. JFM 674 (2011) 433).
- In the droplets, the bath pumps energy in, so the wave left along the path lasts for many bounces (the long memory time near the Faraday threshold). That wave is what guides the droplet.
- Here, each echo is a one-off pulse that falls off as $1/R$ and ends up spread over the whole flight. Nothing keeps it going, so it gives a smooth push rather than a guiding wave.
- The two replications did not get single-particle interference even with a lasting wave. So the gap between our echoes and a pattern is larger than the gap the droplets themselves failed to close.

## Weak points

1. First order only; a nonperturbative run (self-consistent path) was not done.
2. The launch profile is a single shape (constant acceleration over τ = 0.2). τ was not scanned (open; it should be scanned, not chosen).
3. A neutral ideal slit, with a single kick value as a stand-in. Conducting slit walls would add configuration-dependent images. They would be smooth at first order (not computed).
4. Flat cylinder only. A curved handle, or a conical or Misner gluing (Linet 1986, see batch 21), is not done.
5. **Pre-launch history** was the bug Geometry found (fixed). Other limits: the M tail beyond 48 is about 5% (static chain); the image force is also integrated during the launch window (O(τ)); 3+1 only (2+1 has tails inside the light cone); and Lemma A holds only for kick-only slits (conducting walls: open).
6. The θ grid is 0.25°, so structure finer than about 1° would be missed. The coarse sampling in `results.txt` shows smoothness only down to that scale.

Ledger: L85–L89 (L89 records David's 9:10 AM words).
