# Batch 22: the returning echoes, computed (Creative Lead; do not merge)

**Status.** Exploration only. Classical only; test-field limit; no Born rule; no $|a|^2$; no superposition by hand; (M1) untouched at L3; CTCs as exploration only. Citations are bibliographic and unchecked unless marked. Nothing goes into `versions/` or `papers/`. Stacked on batch 21 (#405 at 7263adf). Ledger rows L85–L89. Script: `notes/creative/batch-22/echoes.py` (sha256 `355c4f6e03eb593985cf8b0f1828708b3e30b6afe2975a26b3978450820972bc`); output: `results.txt` (sha256 `6666830420492fb4939195963761518d96bb68e66ad191716ca81e6962b6b0e6`).

**David, 9:10 AM ET 2026-10-13, relayed by Physics Lead, Physics Lead chat, not signed:**
> Let's have creative lead model the returning echoes.

---

## For David (plain summary)

- **What we did.** We gave the particle a small charge and let it be launched, which makes it radiate. The radiation goes round the wrap and comes back. We computed the push those returning echoes give the particle, and where it lands as a result.
- **Result.** The echoes do push the particle. But the push changes smoothly with launch angle, a gentle overall spreading like a weak lens. There are no bands: no repeating light-and-dark stripes.
- **No natural wavelength.** The effect simply grows as the wrap gets smaller or the particle gets slower. Nothing sets a stripe spacing.
- **Two slits.** The echoes a particle feels come only from its own path, and a neutral slit it didn't go through doesn't change them. So opening the second slit still just adds the two one-slit patterns (batch 21 Lemma A). There are no dark spots.
- **Records.** A passive route record changes nothing. A field-coupled one adds another smooth push, and there are no bands for it to remove.
- **Verdict.** In this model, the echoes give smooth distortion, not interference. This is unlike the droplets, whose wave is kept going by the bath and so lasts.

---

## Model (and why)

- **Space and launch.** Flat cylinder $\mathbb R^3$ with $x\sim x+L$, $c=1$. The charge is at rest at the origin for $t<0$. It is then launched at angle θ, with constant acceleration to speed $v$ over time $\tau$. The screen is at $y=D$.
- **Slit crossing.** An optional slit kick is a transverse $\delta v_s$ over $\tau$ at $y=y_s$. A neutral, ideal aperture exerts no force; the kick stands in for a real slit interaction and is shown at one value only.
- **Image fields.** Images sit at $r+mL\hat x$, $m\ne0$, with the full retarded Liénard–Wiechert fields (velocity and acceleration parts). The retarded time is solved by bisection; before launch, the images' rest fields apply.
- **Local self-force.** Landau–Lifshitz reduced order, chosen because it is free of runaways and pre-acceleration and agrees with Lorentz–Dirac to $O(\epsilon)$. It is nonzero only during the prescribed accelerations, where the launcher absorbs it, and zero in free flight.
- **Order.** First order in $\epsilon=q^2/(4\pi\varepsilon_0 mc^2)$, a length. The image force is evaluated on the unperturbed path, and the deflection at the screen is integrated: $\Delta x_{\rm hit}=\epsilon\,f(\theta;v,L,\tau,D)$.
- **Density change.** $\delta=-\partial_\theta\Delta x_{\rm hit}/(D\sec^2\theta)$, so density ≈ baseline × $(1+\delta)$, with baseline ∝ launch weighting × $(D\sec^2\theta)^{-1}$ (batch 21).
- **Parameters.** None was fitted. $D=10$ and $\tau=0.2$ are fixed. Scanned: $L\in\{1.25,2.5,5\}$; $v\in\{0.3,0.5\}$; with and without a slit kick ($y_s=5,\ \delta v_s=0.05$); θ from −10° to 20° in 121 steps. A τ scan was not run. The charge enters only through ε (linear).
- **Validity.** Weak coupling, $|\epsilon\,\delta/\epsilon|\ll1$, i.e. $\epsilon\lesssim10^{-3}$ in these units (the caustic estimate is ε ≈ 0.008–0.03). The particle is a test body in a test field (no metric back-reaction, #399 §4). The flat, eternal wrap is fixed.

## Results [N] (results.txt)

| case | $\Delta x_{\rm hit}/\epsilon$ range | $\delta/\epsilon$ range | sign changes of $\delta-\bar\delta$ |
|---|---|---|---|
| L=2.5, v=0.5 | −108 … 229 | −67.8 … −60.4 | 3 |
| L=2.5, v=0.3 | −193 … 407 | −117 … −109 | 4 |
| L=1.25, v=0.5 | −210 … 446 | −131 … −118 | 3 |
| L=5, v=0.5 | −56 … 119 | −35.6 … −31.3 | 3 |
| L=2.5, v=0.5, slit kick | −164 … 166 | −67.4 … −58.6 | 3 |

- **What it looks like.** $\Delta x_{\rm hit}$ is close to linear in θ: a uniform outward stretch, i.e. a weak diverging lens, plus a small smooth curvature. The mean density change is a stretch; under normalisation it only rescales the pattern.
- **Residual.** The variation left after that is about 10–15% of the mean and monotone-ish, with 3–4 sign changes over 30°. It is a smooth trend, not periodic. (The "period" numbers in `results.txt` are the script's crude estimate from those 3–4 crossings and mean nothing.)
- **Physics.** The dominant piece is causal. Until the launch's light front returns from image $m$, at $t\approx|m|L/(1-v\cos\cdot)$, the particle feels the images' fields from *before* launch, i.e. at rest at the launch point. That field is repulsive from the launch point and does not cancel pairwise once the particle has moved. The radiation (acceleration) part adds pulses at each return time. Integrated over flight, they average to a smooth kick.

## Answers

**(1) Bands? Below baseline?**
- No bands at first order. The density change is smooth in θ, a lens-like stretch plus a gentle trend.
- Normalised, it lies above the baseline in some places and below it in others by $O(\epsilon)$ smooth amounts. There are no repeated dips.
- **Two-slit:** for neutral apertures, a world's self-force depends only on its own path, so $p^{\rm both}(w)$ and its hit are as with one slit open. Batch 21 Lemma A then gives the normalised two-slit pattern as a convex blend of the one-slit patterns. **No point falls below both.**
- Only at $\epsilon\gtrsim0.01$ (outside validity) would the stretch fold into a caustic, and that would be a single fold edge, not bands.

**(2) Scaling, wavelength?**
- $|\delta|$ scales close to $1/L$: about 118, 61 and 31 per ε for L = 1.25, 2.5 and 5.
- It scales roughly as $1/v$: 109 vs 61 for v = 0.3 vs 0.5. It is linear in ε by construction.
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
5. The θ grid is 0.25°, so structure finer than about 1° would be missed. The coarse sampling in `results.txt` shows smoothness only down to that scale.

Ledger: L85–L89 (L89 records David's 9:10 AM words).
