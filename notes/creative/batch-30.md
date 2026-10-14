# Batch 30 — What is a particle, and what action does it carry? (brainstorm, DO NOT MERGE)

Ideas only. Runs are paused (David, 11:51 PM ET 2026-10-13), so this batch has no scripts. Classical only: no Born input, no |a|², no superposition put in by hand. (M1) is untouched at L3. Nothing goes in versions/ or papers/. Citations are unchecked unless marked otherwise. **Every proposal here is a Creative Lead proposal** unless it is labelled differently.

## Plain summary for David

You asked two things: whether we can define a quantity that plays the role of the "action" in the Born rule, and what a particle is, since the action belongs to the particle's path. That makes sense, and we think the order is right: first define the particle, then read off the action it naturally carries.

We list five candidates for a particle. For each we give its natural size (λ_E, which stays your choice), what it does to throat defocusing, and the action it carries. Then we put two questions to each one. T1: could that action add up and cancel across routes? T2: is it fixed by geometry alone, before any outcome is counted?

- **Point test body.** The action is proper time. This is clean and already used in our runs, but it has no size, so λ_E is undefined. A single real number per world cannot cancel anything (Lemma A).
- **Extended lump (a geon).** It has a real size and could pick up phase-like quantities, but it is hard to model.
- **A carried handle or defect (a *topological geon*, in our classical sense: a localized defect that looks like a point once the world is projected onto the *shadow spacetime*, the simply connected coarse spacetime of the LEA chart).** Its action is topological: a twist or holonomy around handles, or a winding number. This is the most interesting candidate for T1, because these quantities are circle- or integer-valued, and circle values are what cancellation needs. But circle values are necessary, not sufficient: cancellation also needs a rule for adding phases, and the only known rule (Schulman 1968; Laidlaw–DeWitt 1971) is the quantum path integral. In our 2D G1 toy the holonomy is a ℤ₂ reflection, not a circle.
- **A pattern in the ledger.** It gives identity and repeatability for free, but its action is not geometric yet.
- **A world-tube identified across worlds by record class.** This defines the particle the way we defined the detectors d_i. It fits the LEA best, but it is a definition of identity, not an action.

**Most promising (Creative Lead proposal):** the topological-geon candidate (c), which matches your 12:59 AM framing of a localized defect that is a point in the shadow spacetime, with action = proper time + a holonomy/twist phase, and identity across worlds via the record-class world-tube (e). This is the one combination where a circle-valued, geometry-fixed quantity could open Lemma A's exit (ii). Circle values are necessary for that but not sufficient: the phase-addition rule is the open Born-side step, and the known rule is quantum. The holonomy is fixed by germ, Γ and route, and depends on the actual loop (enclosed curvature), not only its class. Batch 31 replaces this phase route with the exclusion exit (#419 C5). Nothing here is computed.

## 1. David's words (verbatim as reported by Creative Lead, direct in Creative Lead chat, not signed; unverified by Literature, no original seen)

- David, 12:25 AM ET 2026-10-14: "One puzzle piece that comes to my mind is whether it will be possible for us to define a quantity that plays the role of the “action” in the Born rule."
- David, 12:40 AM ET 2026-10-14: "Let’s think about what a particle is; it needs to be done, and it might shed some light on our understanding of action. The action is intimately connected to the path of the particle through spacetime, so it may be difficult to think of one without the other. Does that make sense?"

Creative Lead reading: yes. In the path-integral picture the action is a functional of the path, S[γ], so a particle definition (what γ is, and what S[γ] the particle carries) comes first. Strictly, the action enters the path-integral amplitude through e^{iS/ħ} (Feynman 1948); the Born rule then maps amplitudes to probabilities and contains no action itself. We read "the action in the Born rule" as this amplitude-level S. Here we look only for a classical, geometry-fixed S that *could* later play that role. We do not put e^{iS/ħ} in.

## 1a. Terminology (David's choices)

**Shadow spacetime.** David, 1:04 AM ET 2026-10-14, direct in Creative Lead chat, not signed; unverified by Literature, no original seen; verbatim: "Let’s try shadow spacetime and see if it sticks."
- Meaning: the simply connected coarse spacetime that a multiply connected world projects onto, i.e. the target of the LEA chart f: U → ℝ^{1,3} (#410/#411, additive (C1)).
- It replaces "reference spacetime", which would clash with the "shared reference" (the labelled-anchor reference configuration) used to identify the d_i.

**Framing of the particle.** David, 12:59 AM ET 2026-10-14, direct in Creative Lead chat, not signed; unverified by Literature, no original seen; verbatim: "I like the idea of a defect in spacetime, which is sufficiently localized that it can be approximated as a point after projecting the multiply connected world onto the simply connected reference spacetime." (His "reference spacetime" here is what we now call the shadow spacetime.) This favours candidate (c), read through (a) after projection: a localized defect that is a point in the shadow spacetime.

**The particle's name: topological geon (with a caveat).**
- *Rejected:* Hadley's "4-geon". David, 1:08 AM ET 2026-10-14, direct in Creative Lead chat, not signed; unverified by Literature, no original seen; verbatim: "If hadley strictly requires CTCs as part of the definition, let’s not abuse his terminology." Literature verified that CTCs are part of Hadley's definition (Found. Phys. Lett. 10 (1997) 43, quant-ph/9706018: "a topologically non-trivial 4-manifold with closed timelike curves - a 4-geon"). Our defects need no CTCs, so the term is not used.
- *Adopted:* "topological geon". David's widget answer, 1:20 AM ET 2026-10-14, direct in Creative Lead chat, not signed; unverified by Literature, no original seen; verbatim: "Topological geon, with a caveat".
- *Caveat:* in Sorkin–Surya (gr-qc/9605050; hep-th/9704081) and Dowker–Sorkin (gr-qc/9609064), a topological geon is a quantized, irreducible prime summand of a spatial 3-manifold, and handles (S¹×S² summands) are explicitly excluded. Our use is classical, allows handle summands (our G1 and mirror gluings), and refers to a localized spacetime defect, not a spatial prime summand.
- Giulini (math-ph/0606066) is cited for a classical use of the term. Friedman–Sorkin 1980 and Sorkin 1986 are metadata-only (texts unread).

## 2. Tests

- **T1 (superpose/interfere):** does S take values in a group where contributions can cancel (a circle U(1), or a ℤ_n), rather than only in ℝ≥0? Lemma A (batch 21): one route per world with non-negative fixed weights gives no dark spot. Its exits are (i) more than one route per world contributing, (ii) signed or phase-valued per-route quantities, or (iii) weights that are not fixed per world. A particle's action is useful only if it opens one of these exits *classically*. (This (i)–(iii) is this batch's own, batch-21-style numbering. It is not batch 23's: Lemma A′ (batch 23 L29–L36) has *assumptions* (i) one route per world, (ii) non-negative weights, (iii) union with unchanged weights, and *named* exits exclusion, contextual dynamics, multiplicity, read-out change. Exit (ii) here amounts to dropping batch 23's assumption (ii), which batch 23 rejects (Set R); batch 31 replaces this route with exclusion. Geometry, #419 C5.)
- **T2 (fixed independently):** is S fixed by the germ, Γ and the launch alone, with no outcome count or fit to frequencies?
- **Repeatability:** does a second detection agree with the first (the same d_i on a repeated measurement)?
- **Which-path:** does the particle write a which-route record (#401 R2: routes are branches only if recorded)? If it does, a route-phase should not be able to interfere.
- **Identity across worlds:** how do we say it is "the same particle" in W_A and W_B (like d_i: additive (C1), O(3) fit, labelled anchors)?

## 3. Candidates

### (a) Point test body
- **Definition:** a timelike geodesic fixed by its launch event and direction (#410 §6; free fall is universal).
- **λ_E:** none intrinsic. This is the λ_E ≲ ℓ case of all our runs. Choice left to David.
- **Defocusing:** applies fully. Sub-ℓ launch data reach several W_i (batches 28–29).
- **Action:** proper time τ[γ] (S = −m∫dτ), which geodesics extremise. Also available: the deck-element class of the route loop, and the Levi-Civita holonomy around a handle. Under the lock the metric near a handle is curved (Gauss–Bonnet), so this holonomy is the deck element's linear part times the enclosed curvature and depends on the loop, not only on its class. In 2D a flat cover has no rotating deck element (#413 R2), and the G1 gluing gives a reflection (ℤ₂), not a rotation θ. In a flat seam toy the deck element's linear part is a rotation R_θ for the orientable mirror gluing and an orientation-reversing element of O(2) for the non-orientable G1 gluing.
- **T1:** τ is real and positive, so on its own it cannot cancel. With one route per world it falls in Lemma A. The holonomy θ is circle-valued, but a point body has no internal frame for it to act on. It needs a carried vector (spin/frame), which is a step towards (c).
- **T2:** yes. τ and θ are fixed by germ, Γ and launch.
- **Lemma A exits:** none on its own. Several routes to one hit in one world (the #401 multiplicity) give exit (i), but routes are not branches unless recorded.
- **Repeatability / which-path:** it is repeatable (deterministic). It writes no record, so which-path is free.

### (b) Extended lump (geon / matter lump in the ledger, #388)
- **Definition:** a localised self-bound lump of field or geometry with a world-tube of width λ_E.
- **λ_E:** the lump's size (or the range of its self-field). It is the first candidate with a real λ_E (R5 of Claude 018).
- **Defocusing:** if λ_E ≫ ℓ, a throat sees only part of the lump. Tidal splitting or smoothing may kill the O(1) deflection. If λ_E ≲ ℓ it reduces to (a). The open question is whether a lump straddling a throat splits, which would give two partial routes in one world.
- **Action:** the matter or field action on the tube, ∫L√−g; the enclosed curvature (deficit) of the tube; the field holonomy for a charged lump.
- **T1:** a lump straddling two routes could carry a *relative* holonomy between its two parts. That is a candidate for exit (i)/(ii) inside one world. Under the lock the lump is part of the analytic metric, so the relative holonomy is the holonomy of the loop formed by the two partial routes: fixed by the world, and dependent on the enclosed curvature. Unchecked.
- **T2:** yes in principle, but stability is unknown (Wheeler geons are unstable classically [unchecked]).
- **Repeatability:** fair, if the lump is stable. **Which-path:** a split lump records its own route, which may block interference. This is a tension to test.

### (c) Topological defect or handle carried along
- **Definition:** the particle *is* a handle, kink or defect: charge without charge (flux through a handle), or a topological kink.
- **λ_E:** the handle's mouth size a (or its span ~2a + throat length). It is purely geometric.
- **Defocusing:** a carried handle meeting a foam handle is handle–handle scattering. That is not computed, and the IVT argument may not apply.
- **Action:** topological, e.g. the winding number of the carried handle around foam handles; the holonomy/twist (deck-element linear part) accumulated along the route; flux through the handle (AB-like: classically only the loop integral ∮A = enclosed flux is defined, and it exerts no force on a charge outside the flux; it becomes a phase e∮A/ħ only with quantum input, Aharonov–Bohm 1959).
- **T1:** **the best candidate, necessary but not sufficient.** Levi-Civita holonomy lies in SO(1,3) (SO(2) or O(2) in the 2D toys; for the non-orientable G1 gluing the holonomy has a ℤ₂ orientation part, which is ±1-valued rather than circle-valued). It is circle-valued only if it lies in a one-parameter subgroup (rotation about a fixed axis), and a winding is ℤ-valued, so it needs a chosen map ℤ → U(1). Then two routes to the same hit can carry different circle values. The difference is the holonomy of the closed loop the two routes form, which is gauge-invariant but depends on the routes through the enclosed curvature. Circle values alone give no superposition or linear evolution: cancellation needs an addition rule for unit phases, which is the open Born-side step (below). That opens exit (ii) classically, *if* two routes contribute in one world, or if worlds pair up.
- **T2:** yes. Given the germ, Γ and the route, the holonomy is fixed (#399 §3; #413 lock reading L135: the germ fixes M̃, the deck part is the linear part of γ ∈ Γ ⊂ Isom(M̃)), and no count enters. Within one world nothing is left free; it varies only across worlds (different Γ) or across routes. For flux, T2 must also include the field's initial data.
- **Lemma A exits:** (ii). It needs a rule for how phase-valued route data combine, and that rule is exactly the open Born-side step. We do not supply it. The known rule (sum over homotopy classes weighted by a unitary character of π₁; Schulman 1968, Laidlaw–DeWitt 1971) is the quantum path integral, so adopting it would import QM.
- **Repeatability:** the topological charge is conserved, so repeatable. **Which-path:** the winding *is* a route record if it is read later, which loses the interference. A clean test.

### (d) A persistent pattern/record in the append-only ledger
- **Definition:** a particle is a stable, repeatable entry pattern in the append-only diary (#388 R1 fix), i.e. "what gets recorded consistently".
- **λ_E:** the record's resolution (τ, Δ), not a size.
- **Defocusing:** silent. It is defined downstream of the detector.
- **Action:** none geometric. Possibly the count of writes or the record length. That is not an action.
- **T1:** no. T2: risky, since it is defined by the outcomes, so it is close to circular.
- **Use:** it gives repeatability by definition. It is a good *test*, not a definition.

### (e) A world-tube identified across worlds by record class
- **Definition:** the particle is the class of world-tubes, one per world in W, that the LEA chart maps within τ of each other up to the record time. Identity works like d_i (additive (C1), O(3) fit, labelled anchors).
- **λ_E:** the tube width, set by τ and the LEA ε. It is not intrinsic.
- **Defocusing:** this is exactly where the class splits. Past the throat the tubes separate into the W_i.
- **Action:** inherited from whatever lives in each tube ((a)–(c)). A *cross-world* quantity could be the difference of route holonomies between two worlds of one record class.
- **T1:** only as a cross-world comparison, which needs a rule for combining worlds. That is close to a measure, so μ stays open. T2: yes, it is purely LEA-defined.
- **Use:** it answers identity, not action. It pairs naturally with (a) or (c).

## 4. Side-by-side

| | λ_E | defocusing | action | T1 | T2 | Lemma A exit |
|---|---|---|---|---|---|---|
| (a) point | none (≲ ℓ) | full | τ; θ needs a frame | no | yes | none alone |
| (b) lump | size | may smooth/split | ∫L, curvature, field holonomy | maybe (split lump) | yes, stability? | (i)/(ii)? |
| (c) defect | mouth a | handle–handle, open | winding, twist, flux | **yes, circle-valued** | yes | (ii) |
| (d) record | τ, Δ | n/a | none | no | circular risk | none |
| (e) world-tube | τ, ε | splits here | inherited / cross-world | only cross-world | yes | needs μ |

## 5. Ill-posed questions to avoid (well-posedness principle)

- "Which route did the particle take?" when no route is recorded (#401 R2).
- "The particle's phase" as an absolute number. Only loop holonomies (route *differences*) are gauge-invariant.
- "The particle's size" for (a), and λ_E as a de Broglie wavelength (puts ħ in; Claude 018 R5).
- "Is it the same particle in W_A and W_B?" before an identification rule (e) is fixed.
- "The probability of d_i" before a measure on W; frequencies stay open.
- "The action of a world": the action belongs to a path in a world, not to the world.
- "A carried handle" before its meaning is fixed (proposed: a handle whose world-tube moves at fixed spatial topology, i.e. a time-dependent analytic metric), and "the same handle in W_A and W_B" before rule (e) is fixed.
- "The holonomy of a homotopy class" in a curved metric: holonomy is defined per loop, and only per class when the connection is flat. "A loop class near the detector" needs bounded-length representatives (S_B(Λ), #410).

## 6. Prior art (bibliographic data checked by Literature against Crossref, #418; texts unread)

Wheeler, Phys. Rev. 97, 511 (1955) (geons); Misner–Wheeler, Ann. Phys. 2, 525 (1957) ("charge without charge"); Finkelstein–Misner, Ann. Phys. 6, 230 (1959) (topological conservation laws, kinks); Feynman, Rev. Mod. Phys. 20, 367 (1948) / Feynman–Hibbs 1965 (path integral); Aharonov–Bohm, Phys. Rev. 115, 485 (1959); Berry, Proc. R. Soc. A 392, 45 (1984) (quantal geometric phase); Hannay, J. Phys. A 18, 221 (1985) (classical angle holonomy); Friedman–Sorkin, Phys. Rev. Lett. 44, 1100 (1980) (spin ½ from gravity); Sorkin, "Introduction to topological geons", in Topological Properties and Global Structure of Space-Time (Plenum 1986) 249; Finkelstein–Rubinstein, J. Math. Phys. 9, 1762 (1968); Skyrme, Proc. R. Soc. A 260, 127 (1961); Schulman, Phys. Rev. 176, 1558 (1968); Laidlaw–DeWitt, Phys. Rev. D 3, 1375 (1971); Dirac, Proc. R. Soc. A 133, 60 (1931); Wu–Yang, Phys. Rev. D 12, 3845 (1975); Wilczek, Phys. Rev. Lett. 49, 957 (1982). Closest: Friedman–Sorkin / Sorkin for (c); Schulman / Laidlaw–DeWitt for the combination rule (quantum).

## 7. Next steps (proposal; no runs while paused)

1. Ask David to choose λ_E and the particle candidate (suggest (c) with (e) for identity).
2. In the batch-28 toy, write down (on paper) the route holonomy θ_route for the G1 vs mirror gluings, and check whether two routes to one hit exist in one world.
3. State this batch's exit (ii) precisely for circle-valued route data, with no combination rule yet; note that it drops batch 23's assumption (ii), rejected there (Set R), and that batch 31 pursues the exclusion exit instead (#419 C5).
