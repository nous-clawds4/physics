# LEA consolidated: #410, #411, #413, #415 (do not merge)

**Status.**
- **Consolidation only:** no new runs, nothing in `versions/` or `papers/`.
- **Physics:** classical, no Born input; (M1) is untouched at L3.
- **Citations:** each keeps the verification status it had in its source PR (V-meta, V-text, unread or unverified).
- **Heads covered:** #410 236b01c, #411 bf6a62d, #413 959fa13, #415 b1b417e. **#415 content is at b1b417e, with its Claude 020 re-passes pending.** #412 and #414 are not covered (not this lane).

**David's instruction (verbatim):** "Pause the runs and have Creative Lead consolidate #410–#415 into one note first." (David, 11:51 PM ET 2026-10-13, widget answer relayed by Physics Lead, not signed; unverified by Literature, no original seen.)

## For David (plain summary)

- **What the LEA is now.** Each world is mapped onto one flat spacetime over a bounded lab region, the way you described. What decides "flat at lab scale, twisted at tiny scales" is a single number for each place and size: how badly the best flat map of a ball of that size distorts distances. The derivative order k no longer defines the regimes; it only bounds that number at very small sizes. The earlier "smoothed metric" route failed, because tiny handles force strong curvature beside them.
- **Matching detectors across worlds.** Each world's flat map is pinned to the lab by labelled marker events on the lab bodies, fitted to one shared reference; the fit allows mirror images. Two worlds' detectors count as the same if their images land in the same spot to within a tolerance. A weaker, additive version of our flatness condition is enough for this.
- **Which worlds count.** A world now includes the emitter, the particle, the detectors and the walls, as labelled test bodies. What the observer already knows (Rec₀) still has to be defined.
- **The question** is stated rigorously: for each detector, the set of compatible worlds in which the particle first enters that detector. How to *weigh* those sets (μ) is left open, and kept separate from (M1).
- **Can tiny differences change which detector fires?** In our toys, yes.
  - A single correctly glued tiny handle near the emitter acts like a diverging mirror. Changes in the launch smaller than the handle send the particle to every detector. This is exact (by continuity), not chaos.
  - The first run of this was void (a gluing error) and was redone.
  - The sharp-seam handle is outside the analytic lock. A smooth analytic throat (an Ellis neck) gives the same result.
- **Many handles.** It works in a window of handle spacings, about 110ℓ to 335ℓ in our 2D toy:
  - sparse enough that the particle flies roughly straight;
  - dense enough that the narrow bundle of launches the lab can't tell apart still meets a handle.

  That is a concrete two-sided reading of your "dense but not TOO dense", which is still held open, not adopted.
- **The window's upper edge is soft:** at 335ℓ there is still roughly a one-in-three chance the launch bundle meets no handle.
- **Is this a model of superposition? Not yet** (Creative Lead reading, §10). Each world has one definite outcome, and the bending is deterministic sensitivity, not measurement. What we have is a candidate mechanism for *variety* of outcomes; interference and frequencies are still open.
- **Open, and partly for you.**
  - What the lab record Rec₀ fixes.
  - The particle's own length scale λ_E. We don't choose it; with a point particle, the throat is resolved down to tiny slivers.
  - Dense foam, which the computer can't follow.
  - A smooth one-handle geometry.
  - The measure μ.

  A next-step proposal (S6) is recorded below, not adopted.

## Attribution labels used

- **David, verbatim as relayed, with source (none signed; all unverified by Literature, since no originals were seen):**
  - 4:55 PM (a paraphrase by Physics Lead, apart from its quoted phrases);
  - 5:00 PM and 5:03 PM;
  - 5:17 PM (direct in Creative Lead chat);
  - 5:26 PM (relayed by Geometry; unverified by Literature);
  - 11:51 PM (above).

  The exact wording is in the source notes and the ledger (L108, L115, L119, L122, L127).
- **Lead rulings (Physics Lead):**
  - applying Claude 018 (#410, #411), 019 (#413) and 020 (#415);
  - running S5 (#413) and the multi-handle step (#415).
- **Geometry's readings:** the candidate LEA hypothesis (L128, as corrected by G1), and the lock reading (L135, as corrected by Claude 019 R1–R2).
- **Literature's readings:** citation statuses and scope caveats.
- **Creative Lead proposals (pending review):** the choice of ε(p; λ) as the regime variable (#411).

## PRs, heads and pinned files

| PR | branch | final head | content | scripts and outputs (sha256) |
|---|---|---|---|---|
| #410 | creative/batch-26 | 236b01c | LEA definition, projection, anchoring, identification, W, question | none (theory) |
| #411 | creative/batch-27 | bf6a62d | regime variable ε(p; λ) | none (theory) |
| #413 | creative/batch-28 | 959fa13 | S5: single-handle reachability | `s5.py` (void) f1054253…a1b759a6; `s5_out.txt` (void) f2bdbb9d…9b072d1a; `s5b.py` a6f30f66…fe541635; `s5b_out.txt` a5278391…a4ca1b0f; `s5b_coarse_out.txt` ae3cc9a1…a6d6d18; off-repo (Geometry, box): `s5fix.py` 3301fa8f…5f04f, `s5bdiag.py` 8e64aec9…bb8d42, `ivt413.py` 44f62932…3b79b64 |
| #415 | creative/batch-29 | b1b417e (re-pass pending) | many handles; cluster chaos; Ellis neck | `foam.py` bbb851cf…a4f15; `foam_g1.txt` 2ff83000…f997581; `foam_mirror.txt` 6c723fb5…c21b2a87e; `scatter3.py` 4b86adbe…38d3f5 (docstring-only change; output pin from the earlier run); `scatter3_out.txt` 82b1baad…6b517b35; `ellis.py` 40eaeb5e…90778a4; `ellis_out.txt` bf1f6d11…9368e7 |

The full hashes are in each batch's provenance table. The foam pins hold on Linux x86_64, Python 3.13.5, numpy 2.2.4 only (Claude 020 R3).

## 1. The LEA and the regime variable (#410, #411)

- **Projection.**
  - Fix a unit timelike u on the lab region U (the lab frame) and set h = g + 2u♭⊗u♭. u is restricted to bounded boost and slow variation, λ|∇u| ≪ ε (Geometry F8).
  - **U = B_R(p₀)** is an h-ball containing the emitter, the detectors and the anchors. Distances are the length metric of (U, h), so curves stay in U (Claude 018 R3).
  - The projection f: U → ℝ^{1,3} must be **admissible**:
    - (C1) in additive form: |‖f(p) − f(q)‖ − d_h| ≤ εR;
    - (C2): an ℓ-dense image of width ~R in every direction, so that it is thick (Claude 018 S2; Alestalo–Trotsenko–Väisälä, used as "if thick");
    - (C3): one-way, future-directed causal compatibility (N6).
  - **The old (C4) is removed.** A smoothed ḡ_L that keeps the micro-handles cannot be within ε of flat (Cheeger–Gromov–Taylor injectivity estimate, which needs its volume premise; Lorentzian, observer-based form in Chen–LeFloch CMP 278 (2008) 679; LeFloch 2008 review; "Thm 2.1" is unverified).
  - The multiplicative (C1) needs a Reifenberg-type multi-scale step (Reifenberg 1960; Toro 1995). It is open, and it is not needed for d_i.
- **Regime variable (Creative Lead proposal, pending review; David delegated it at 5:17 PM).** The flat distortion is

  ε(p; λ) = (1/λ)·inf_f sup_{x,y ∈ B_λ(p)} |‖f x − f y‖ − d_h(x, y)|,

  with a density (filling) clause: f(B_λ) is ελ-dense in a Euclidean λ-ball.
  - It satisfies (2/5)·d_GH/λ ≤ ε ≤ 2·d_GH/λ, or 2/3 in place of 2/5 if the image lies inside the ball. These bounds are derived, not sourced; the correspondence lemma is from Burago–Burago–Ivanov 2001.
  - Closest prior art: Reifenberg flatness and Cheeger–Naber's (k, ε)-symmetry.
- **The three regimes (Lead notes, 5:03 PM).**
  1. ε(p; λ) → 0 as λ → 0. This is the manifold property.
  2. ε reaches ε_tw = O(1) near ℓ_P, on an L-dense set.
  3. ε ≤ ε for every whole ball B_λ(p) ⊂ U with λ ∈ [ℓ_low, R] and ℓ_low ≳ ℓ/ε.
  - There is no claim beyond R, and none at cosmic scales.
- **Why ε and not k.** Once micro-handles are present, no curvature statement about a metric on U can express regime 3; ε can (Claude 018 S3).
  - **k as a bound:** for λ < min(inj, ρ, sys_r/2), ε ≲ C|Riem_h|λ² + …. This is an asymptotic upper bound in h-curvature, not a Taylor series.
  - **Flat micro-wraps** collapse volume and escape Cheeger–Gromov–Taylor. The density clause excludes them.
- **Regime 3 in the raw metric** needs the foam's stable norm N to equal c·‖·‖_{h_{u′}} to within ε, for a constant c and a constant u′ (Geometry G1; "isotropic", u′ = u, is the sufficient special case).
  - Periodic foam (Burago 1992): the error is C/λ, which needs C/λ ≤ ε.
  - Non-periodic foam: the deviation is only sublinear [unchecked] (Literature P4).
  - A handle is *micro* if π₁(U) is normally generated by loops of length ≤ 2ℓ (N8). "Mouths in a common ℓ-ball" is the rough picture, not an equivalent: batch 28's mouths need a 1.1ℓ ball yet are micro by the π₁ criterion.
- **Under the lock,** a lab containing handles is only approximately flat: never exactly flat on an open set (identity theorem; Geometry Q4).

## 2. Cross-world identification of d_i (#410)

- **Anchoring.**
  - The anchors are marked events on the lab bodies, labelled in every world; the labels are world data.
  - The fit runs over **O(3) ⋉ ℝ³ × time translations**, so reflections are included. Time reversal is excluded because (C3) is future-directed.
  - The fit is unique if the reference anchors affinely span ℝ³ (at least 4 non-coplanar). The mirror branch can be told apart only if the third principal spread w₃ ≫ εR + ℓ. The reflection sign is recorded as world data (Geometry H1–H2; Claude 018 R6).
  - Without labels, a symmetric lab gives two fits that swap d₁ and d₂.
  - The anchoring error is δ_P = O((εR + ℓ)·R/w), where w is the second principal spread.
- **Identification.**
  - d_i in two worlds is the same if each world's image agrees with the shared reference within τ/2 (so the two agree within τ, transitively), with τ ≫ C·εR. Additive (C1) suffices (Claude 018 R2).
  - Optional criteria:
    - (M-a) compares local loop data S_B(Λ) to a micro tolerance δ_μ ≪ ℓ, localised to the window; the local systole sys_r does not fix global π₁;
    - (M-b) uses diary entries **up to emission** only.
  - Everything is defined inside the bounded window.

## 3. The set W (#410, Claude 018 R4)

- W is #399's worlds with the emitter, the particle, the detectors and the walls added as labelled test bodies.
- "Compatible with Rec₀" (renamed from 𝓡₀) must be defined. At least, the lab bodies' images match the reference within τ/2 and the diaries hold Rec₀.
- #399's tube-injection clause fails in micro-foam and is replaced, for example by injection at scales ≥ L.
- **What may differ between worlds:** micro-handle gluings in U, extensions, and launch data below ℓ.

## 4. The emitter–detector question (#410)

- W_i is the set of w ∈ W in which the particle's classical worldline first enters a member of [d_i].
- **The question:** μ(W_i)/μ(W_j) for an independently specified measure μ.
- **Well-posed if:**
  - none of §4's ill-posedness conditions 1–6, 8 or 9 holds;
  - each w has an admissible f_w (condition 10);
  - the classes are stable within τ;
  - μ is a measure on a σ-algebra containing the W_i, with 0 < μ(W_j) < ∞.
- **μ is left open.** A measure on worlds is not (M1), which stays the ruled per-vertex rule at L3 (Claude 018 S1).
- **λ_E (condition 7) is a placeholder,** left to David (Claude 018 R5). A free test particle's geodesic is energy-independent, and reading λ_E as a de Broglie wavelength would put ħ in by hand.

## 5. Single-handle reachability (#413, at 959fa13)

- **Void run.** `s5.py` rotated the direction without flipping its normal component, so the ray exited *into* disk 2 (the #408 wrong-side defect; Geometry K1, Literature G1). It is kept as a record. Its claims are withdrawn: "an ordinary handle only shifts the particle", "needs a twist" and j ≈ θR/Δ.
- **Valid rerun (`s5b.py`).** Exterior gluings G1 (non-orientable) and mirror (orientable), with the normal flip and the outward exit asserted. On 10001 × 11, both gluings at every θ reach all 21 detectors and None.
- **Exact, by the IVT (Claude 019 S2; Geometry P1–P2).**
  - The one-pass offsets form two intervals. For G1 at θ = 0 the exit angles range over [−1.223, −0.0002] and [0.0002, 4.653] rad, and together these cover the array.
  - The other directions need two passes.
- **Not chaos.** The map from offset to exit angle is piecewise smooth and deterministic.
  - Sliver widths per detector: about 3×10⁻⁵ℓ at θ = 0 (two passes), first-pass grazing slivers about 2×10⁻⁶|j|ℓ, and about 5×10⁻⁴ℓ at θ = π/2.
  - These are offset-coordinate lengths, not sizes of W_j.
- **Sensitivity, not a π₁ signature.** A plain convex mirror would do the same (Claude 019 S6).
- **Lock scope.**
  - The seam toy is outside the lock in **every** host. By the identity theorem, flat off the seam means flat on it; by Gauss–Bonnet, one handle needs −4π of curvature, which here sits on the seam (Claude 019 R1). This corrects Geometry's K5.
  - Geometry's lock reading (L135) is correct in outline (Claude 019):
    - the germ fixes M̃, not θ;
    - θ is the linear part of a deck element, chosen with Γ;
    - a continuum of θ needs an axial Killing field commuting with γ;
    - a flat 2D cover has no rotating deck element; in 3D, screw motions allow one, but only for wraps without mouths;
    - within one geometry M̃/Γ, worlds differ only in sub-ℓ launch data.
- **Point particle.** It is the λ_E ≲ ℓ case of condition 7 (Claude 019 R3). The geometry is within the LEA; the particle model is not.
- **Prior art (bibliographic):**
  - closest analogue: Visser 1989 (PRD 39 3182; NPB 328 203);
  - Wielgus et al. 2020;
  - chaotic scattering, relevant to clusters: Gaspard–Rice, Ott–Tél, Bleher–Grebogi–Ott, Dettmann–Frankel–Cornish, Cornish–Levin;
  - lensing, as context only.
  - Dowker is not cited.

## 6. The two-sided multi-handle window (#415, at b1b417e, re-pass pending)

- **Setup.** A 2D seam foam: cells of side s, one handle per cell at a fixed pseudo-random offset. Batch 28's handle is **placed by hand** in cell (0,0), in the launch tube.
- **Lower edge.**
  - The flight is ballistic once ℓ_free = 1/(nσ) = s²/(4a) ≳ R, i.e. s ≳ √(4aR) ≈ 110ℓ, about 50 handle spans. This is the 2D Lorentz-gas mean free path (Santaló; Bunimovich–Sinai; Boltzmann–Grad: Gallavotti, Spohn, Boldrighini–Bunimovich–Sinai; periodic layouts: Marklof–Strömbergsson).
  - For s ≲ 20ℓ paths wander ("diffusive" is an analogy only).
- **Upper edge (Claude 020 R1).**
  - Several W_i are non-empty only if a mouth lies in Rec₀'s launch tube, whose area is A ≈ R(ℓ + 0.4τ + 2a) ≈ 5.6×10⁴ℓ².
  - The foam's own layout supplies one on average only for s ≲ √(2A) ≈ 335ℓ (a soft edge: the chance of an empty tube is about exp(−2A/s²), ≈ 0.37 at 335ℓ).
  - With a mouth in the tube, single-encounter launches reach all 21 detectors for s = 110–2000. These witnesses are robust to roundoff.
- **Window:** about 110–335ℓ. Both edges scale like √R. The factor of about 3 between them is set by Rec₀'s launch freedom compared with the mouth size.
- **Coarse reached sets** after the cap-code fix (Claude 020 R2; aperture −1 had collided with the cap code):

  | | s = 110 | s = 200 | s = 500 | s = 2000 |
  |---|---|---|---|---|
  | G1 | 14 | 17 | 5 | 4 |
  | mirror | 11 | 11 | 4 | 4 |

  No launch is capped at s ≥ 50.
- **Dense foam:** reachability is **open**. Double precision follows a path for about five encounters, and the s = 20 hits came after hundreds (Claude 020 R3).
- **Chaos.**
  - One handle is piecewise smooth. For G1, C(n) saturates; the mirror gluing grows logarithmically near its periodic orbit.
  - Clusters of four or more handles (2×2, 3×3) show C(n) ~ n^D, with local slopes about 0.4–0.75 that stay level from n = 10⁶ to 10⁷ (0.488 for G1 K = 2, s₀ = 4.0; 0.745 for G1 K = 3, s₀ = 2.5; Claude 020 S1, not in the pinned scatter3_out.txt, which stops at 10⁶; levelling checked for two cases only). One decade is weak evidence of convergence; D is not a converged dimension.
  - Two handles that can see each other should suffice, but this was not run.
  - In the ballistic window, each further encounter multiplies the sensitivity by about 2L/a.

## 7. The smooth Ellis neck (#415)

- The 2D neck ds² = dr² + (r² + a²)dφ² is analytic (Ellis 1973; Bronnikov 1973 unverified; geodesics: Chetouani–Clément 1984, Müller 2008).
- Integrated geodesics match the closed form 2K(a/b) − π. Reflected rays wind logarithmically near b = a and reach all 21 detectors plus None, exactly by the IVT.
  - Aperture windows are about 10⁻⁶ℓ wide on the first winding.
  - The far field alone reaches apertures 4–10 from a sub-ℓ window at b ≈ 1.2–2ℓ, on intervals 0.06–0.24ℓ wide (Claude 020 S4).
- **Scope.**
  - The residual sheet-1 curvature beyond r = 60ℓ = 200a was treated as straight (residual angle ~2.5×10⁻⁵ rad, below the aperture angle).
  - It is a two-sheet neck, not a one-sheet handle; it has the same −4π Gauss–Bonnet budget. A one-sheet handle needs a second neck or a seam, i.e. more curvature.
  - It is analytic, so the mechanism sits inside the lock, within one fixed geometry.
  - For smooth throats, both edges of the window move to larger s (not computed).

## 8. David's held-open proposal

**David, 5:26 PM, relayed by Geometry, not signed (unverified by Literature):** "assume the foam is dense but not TOO dense". It is **held open, not adopted.**
- **Geometry's reading (candidate LEA hypothesis):** the stable norm ≈ c·‖·‖_{h_{u′}} to within ε. It is geometric, T2-clean, and involves no outcome count.
- **Two-sided reading (#415, Claude 020 S5):**
  - "dense" means a mouth inside Rec₀'s launch tube;
  - "not too dense" means a free run between throat encounters longer than the lab;
  - here that gives about 110–335ℓ, in 2D. In 3D, ballistic flight needs s ≳ (2πa²R)^{1/3}, heuristically.
- This differs from the distance-based reading of batch 27. It also bounds regime 2's open "L-dense": L must be at least of order √(4aR).

## 9. Open problems

1. **Rec₀.** Not defined. It sets the window's upper edge.
2. **λ_E (for David).** The point particle resolves throats down to 10⁻⁶ℓ slivers; a particle with a length must re-derive everything.
3. **Dense foam.** Beyond double precision; whether true paths shadow the computed pseudo-orbits is unchecked.
4. **A smooth one-sheet analytic handle.** Not computed.
5. **The measure μ.** Open by design. It is separate from (M1).
6. **Other open items:**
   - the multiplicative (C1) (Reifenberg-type);
   - a Lorentz-native ε;
   - non-periodic foam;
   - 3D.
7. **S6, Claude 020's next step (proposal only, not adopted; no runs while paused):**
   > The window's two edges pull in opposite directions. What keeps them apart is how much launch freedom Rec₀ leaves compared with the mouth size, and Rec₀ is still undefined. If Rec₀ fixed the direction ten times better, the factor between the edges would fall from about 3 to about 1.8. If it fixed the offset below the sliver widths, the window would close. The mechanism also needs a particle that resolves the throat (λ_E ≲ ℓ). So whether a window exists depends on two inputs left open by design, Rec₀ and λ_E. The foam it needs is sparse on the micro scale: isolated handles at least √(4aR) apart (about 110ℓ here), not a space-filling foam. The next step is cheap and decisive:
   > 1. Remove the hand-placed handle and launch from many emitter placements.
   > 2. Keep only witnesses that roundoff cannot move: single encounters, or launches aimed at each one-pass interval.
   > 3. Map the two-sided window against s and against Rec₀'s angular freedom.
   > 4. Then close two analytic necks into a one-sheet handle, and redo the window with its far field.

## 10. Creative Lead reading: is this a model of superposition?

Prompted by David's question (11:59 PM ET 2026-10-13, direct in Creative Lead chat, not signed; unverified by Literature, no original seen): "would it be fair to say that we have a model for superposition, with World A and World B being identical except for a particle that is in different topological states im each World, with our model for backscattering triggering a measurement of the superposed state?"

**Creative Lead reading (not a ruling):**
- **Not yet.** The model is a classical ensemble of record-compatible worlds. They differ in micro-geometry and in sub-ℓ launch data, not in a particle's topological state.
- **Each world has one definite outcome.**
- **Throat defocusing is deterministic sensitivity,** not measurement.
- **Superposition would need more.** It would need a T1-type quantity that superposes and interferes, and Lemma A forbids cancellation with one route per world and non-negative weights.
- **The narrower fair claim:** a candidate mechanism for outcome variety under the LEA, with interference and frequencies left open.

Ledger: L141–L143.
