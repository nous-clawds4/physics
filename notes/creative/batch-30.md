# Batch 30 — What is a particle, and what action does it carry? (brainstorm, DO NOT MERGE)

Ideas only. Runs are paused (David, 11:51 PM ET 2026-10-13), so this batch has no scripts. Classical only: no Born input, no |a|², no superposition put in by hand. (M1) is untouched at L3. Nothing goes in versions/ or papers/. Citations are unchecked unless marked otherwise. **Every proposal here is a Creative Lead proposal** unless it is labelled differently.

## Plain summary for David

You asked two things: whether we can define a quantity that plays the role of the "action" in the Born rule, and what a particle is, since the action belongs to the particle's path. That makes sense, and we think the order is right: first define the particle, then read off the action it naturally carries.

We list five candidates for a particle. For each we give its natural size (λ_E, which stays your choice), what it does to throat defocusing, and the action it carries. Then we put two questions to each one. T1: could that action add up and cancel across routes? T2: is it fixed by geometry alone, before any outcome is counted?

- **Point test body.** The action is proper time. This is clean and already used in our runs, but it has no size, so λ_E is undefined. A single real number per world cannot cancel anything (Lemma A).
- **Extended lump (a geon).** It has a real size and could pick up phase-like quantities, but it is hard to model.
- **A carried handle or defect.** Its action is topological: a twist or holonomy around handles, or a winding number. This is the most interesting candidate for T1, because these quantities live on a circle and so can cancel.
- **A pattern in the ledger.** It gives identity and repeatability for free, but its action is not geometric yet.
- **A world-tube identified across worlds by record class.** This defines the particle the way we defined the detectors d_i. It fits the LEA best, but it is a definition of identity, not an action.

**Most promising (Creative Lead proposal):** the handle/defect candidate (c), with action = proper time + a holonomy/twist phase, and identity across worlds via the record-class world-tube (e). This is the one combination where a circle-valued, geometry-fixed quantity could escape Lemma A's no-cancellation result. Nothing here is computed.

## 1. David's words (verbatim, direct in Creative Lead chat, not signed)

- David, 12:25 AM ET 2026-10-14: "One puzzle piece that comes to my mind is whether it will be possible for us to define a quantity that plays the role of the “action” in the Born rule."
- David, 12:40 AM ET 2026-10-14: "Let’s think about what a particle is; it needs to be done, and it might shed some light on our understanding of action. The action is intimately connected to the path of the particle through spacetime, so it may be difficult to think of one without the other. Does that make sense?"

Creative Lead reading: yes. In the path-integral picture the action is a functional of the path, S[γ], so a particle definition (what γ is, and what S[γ] the particle carries) comes first. The Born rule's "action" enters only through e^{iS/ħ}. Here we look only for a classical, geometry-fixed S that *could* later play that role. We do not put e^{iS/ħ} in.

## 2. Tests

- **T1 (superpose/interfere):** does S take values in a group where contributions can cancel (a circle U(1), or a ℤ_n), rather than only in ℝ≥0? Lemma A (batch 21): one route per world with non-negative fixed weights gives no dark spot. Its exits are (i) more than one route per world contributing, (ii) signed or phase-valued per-route quantities, or (iii) weights that are not fixed per world. A particle's action is useful only if it opens one of these exits *classically*.
- **T2 (fixed independently):** is S fixed by the germ, Γ and the launch alone, with no outcome count or fit to frequencies?
- **Repeatability:** does a second detection agree with the first (the same d_i on a repeated measurement)?
- **Which-path:** does the particle write a which-route record (#401 R2: routes are branches only if recorded)? If it does, a route-phase should not be able to interfere.
- **Identity across worlds:** how do we say it is "the same particle" in W_A and W_B (like d_i: additive (C1), O(3) fit, labelled anchors)?

## 3. Candidates

### (a) Point test body
- **Definition:** a timelike geodesic fixed by its launch event and direction (#410 §6; free fall is universal).
- **λ_E:** none intrinsic. This is the λ_E ≲ ℓ case of all our runs. Choice left to David.
- **Defocusing:** applies fully. Sub-ℓ launch data reach several W_i (batches 28–29).
- **Action:** proper time τ[γ] (S = −m∫dτ), which geodesics extremise. Also available: the deck-element class of the route loop, and the holonomy of the flat connection around a handle (a rotation θ).
- **T1:** τ is real and positive, so on its own it cannot cancel. With one route per world it falls in Lemma A. The holonomy θ is circle-valued, but a point body has no internal frame for it to act on. It needs a carried vector (spin/frame), which is a step towards (c).
- **T2:** yes. τ and θ are fixed by germ, Γ and launch.
- **Lemma A exits:** none on its own. Several routes to one hit in one world (the #401 multiplicity) give exit (i), but routes are not branches unless recorded.
- **Repeatability / which-path:** it is repeatable (deterministic). It writes no record, so which-path is free.

### (b) Extended lump (geon / matter lump in the ledger, #388)
- **Definition:** a localised self-bound lump of field or geometry with a world-tube of width λ_E.
- **λ_E:** the lump's size (or the range of its self-field). It is the first candidate with a real λ_E (R5 of Claude 018).
- **Defocusing:** if λ_E ≫ ℓ, a throat sees only part of the lump. Tidal splitting or smoothing may kill the O(1) deflection. If λ_E ≲ ℓ it reduces to (a). The open question is whether a lump straddling a throat splits, which would give two partial routes in one world.
- **Action:** the matter or field action on the tube, ∫L√−g; the enclosed curvature (deficit) of the tube; the field holonomy for a charged lump.
- **T1:** a lump straddling two routes could carry a *relative* holonomy between its two parts. That is a candidate for exit (i)/(ii) inside one world. Unchecked.
- **T2:** yes in principle, but stability is unknown (Wheeler geons are unstable classically [unchecked]).
- **Repeatability:** fair, if the lump is stable. **Which-path:** a split lump records its own route, which may block interference. This is a tension to test.

### (c) Topological defect or handle carried along
- **Definition:** the particle *is* a handle, kink or defect: charge without charge (flux through a handle), or a topological kink.
- **λ_E:** the handle's mouth size a (or its span ~2a + throat length). It is purely geometric.
- **Defocusing:** a carried handle meeting a foam handle is handle–handle scattering. That is not computed, and the IVT argument may not apply.
- **Action:** topological, e.g. the winding number of the carried handle around foam handles; the holonomy/twist (deck-element linear part) accumulated along the route; flux through the handle (AB-like phase from enclosed flux, classically the line integral of the connection).
- **T1:** **the best candidate.** Holonomies and windings take values in U(1)/SO(2) or ℤ, so two routes to the same hit can carry different circle-valued values. The difference is gauge-invariant (a loop holonomy). That opens exit (ii) classically, *if* two routes contribute in one world, or if worlds pair up.
- **T2:** yes. Holonomy is fixed by Γ and the germ (#399 §3), and no count enters.
- **Lemma A exits:** (ii). It needs a rule for how phase-valued route data combine, and that rule is exactly the open Born-side step. We do not supply it.
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

## 6. Prior art (bibliographic only, unread, unchecked)

Wheeler 1955 (geons); Misner–Wheeler 1957 ("charge without charge"); Finkelstein–Misner 1959 (topological kinks); Feynman 1948 / Feynman–Hibbs 1965 (path integral); Aharonov–Bohm 1959; Berry 1984 (geometric phase); Sorkin (topological geons and spin, unchecked); Friedman–Sorkin 1980 (spin ½ from gravity, unchecked).

## 7. Next steps (proposal; no runs while paused)

1. Ask David to choose λ_E and the particle candidate (suggest (c) with (e) for identity).
2. In the batch-28 toy, write down (on paper) the route holonomy θ_route for the G1 vs mirror gluings, and check whether two routes to one hit exist in one world.
3. State Lemma A's exit (ii) precisely for circle-valued route data, with no combination rule yet.
