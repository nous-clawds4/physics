# Batch 31 — Virtual geon closures, winding phase and negative interference (brainstorm, DO NOT MERGE)

Ideas only; runs are paused (David, 11:51 PM ET 2026-10-13), so there are no scripts. **CTCs are allowed in this line** (David, 1:36 AM ET 2026-10-14; charter addendum). Everything else stays: classical, no Born input, no |a|², no superposition by hand; (M1) untouched at L3; nothing in versions/ or papers/. Citations are unchecked unless marked otherwise. **Every proposal here is a Creative Lead proposal** unless labelled otherwise. Terms: *shadow spacetime* and *topological geon* as in batch 30 §1a (classical use, handles allowed).

## Plain summary for David

Your picture: a topological geon whose shadow traces a loop, like a virtual pair that appears and later recombines. If something winds around the handle in the not-shadow space, its total winding must come in whole multiples of 2π, and two geons can annihilate only if their phases line up exactly (for opposite directions, perhaps 180° apart). Annihilated geons never reach the detector, and that would be a classical foot in the door for negative interference.

What we propose:
- **A name for the not-shadow space:** *object spacetime* (the thing that casts the shadow), or *host spacetime*. This is your choice.
- **There is no "change" in one world.** Seen from above, one 4-manifold is fixed. A "virtual pair" is a fixed 4D handle structure (like a cobordism) whose shadow is a closed loop, or a path from the source to the detector.
- **There are more closures than pairs:** triples, n-tuples, nested splittings (1→3→1 inside a pair), and in general a graph of geon worldlines, which looks like a Feynman diagram. Each one shadows to one path in "all possible paths".
- **Where the phase would come from:** a twist or holonomy carried around the 4D structure. The step from a whole-number winding to an angle must be fixed by the geometry, not chosen by us.
- **What "annihilate" would mean:** the geons' topological charges or holonomies combine to the identity, so the 4D structure closes off. "180° out of phase" may be a picture of this condition rather than the condition itself. That is open.
- **Negative interference without negative numbers:** a closure that annihilates never reaches the detector, so the geometry excludes those worlds. No weight is negative. This is the "exclusion" exit from Lemma A.
- **The goal is Feynman's path integral.** We must *derive* the rule that adds phases. The known rule (Schulman 1968; Laidlaw–DeWitt 1971) is quantum, so importing it is not allowed.

Nothing is computed, and the dark-fringe test is set aside for now, as you asked.

## 1. David's words (verbatim as reported by Creative Lead, direct in Creative Lead chat, not signed)

- David, 1:23 AM ET 2026-10-14: "let’s imagine a topological geon, the shadow of which traces out a loop in shadow space. We can think of it as a virtual particle pair that pops into existence, then pops out of existence at some later point in time when they come back together. If something — the action — is winding around the handle (in World space of course, not in shadow space; I think we need a name now for “not shadow” space … ), then the total number of loops will need to be an integer multiple of 2 pi. Which means the only way for the two “virtual particles” to annihilate each other is for their phases to coincide exactly. Since they’re going in opposite directions, “coincide exactly” could mean: 180 degrees out of phase. If tue virtual particles annihilate each other, it means they weren’t absorbed by the detector. And now we have our foot inside the door for phases to cancel each other out, producing negative interference."
- David, 1:36 AM ET 2026-10-14 (full message): "Yes, let’s make this the next brainstorm batch. Let’s not worry about CTCs; in fact, I suspect that Hadley is right, and we’re going to need CTCs sooner or later. In the topic of “topology change”, there’s no actual change if you take a single 4-manifold (a single World) and take the bird’s eye view of it. Let’s not worry yet about the dark fringe test. Let’s focus first on negative interference; I suspect the 2-slit will fall out as a consequence. One thing to add: the virtual particle pair could be a triple rather than a pair; or it could be any number of topological geons that pop into existence together, then annihilate each other all at once. Or an even more complicated arrangement of virtual particles: a pair appears, one of the pair splits into 3 which coalesce back into one, then the original pair coalesce. In shadow space, each of these virtual particle trajectories is a path (one element in the set of “all possible paths”) from the source to the detector; and in case that phrase didn’t already ring a bell, I’m hoping eventually to invoke Feynman’s path integral technique for our derivation of the Born rule."

## 2. Name for the not-shadow space (Creative Lead proposal; for David to choose)

- **Object spacetime** (preferred): the multiply connected 4-manifold that casts the shadow, i.e. the domain of the LEA chart f: U → shadow spacetime.
- **Host spacetime** (alternative): matches the existing "host" usage (#408, batches 28–29), but there "host" means the background a toy lives in, so it may blur.
- Avoid "world space": a *world* is an element of W (a whole 4-manifold plus lab bodies), not a space inside one.

## 3. Bird's-eye reading (Creative Lead proposal)

- In one world there is one fixed 4-manifold, so nothing "changes" (David 1:36 AM). Topology change is a statement about spatial slices: the topology of Σ_t differs between slices.
- A "virtual pair" is a 4D handle structure. Between two slices, the spatial topology gains a handle and then loses it. The region between them is cobordism-like.
- **Shadow:** the projection of the pair's worldlines to the shadow spacetime is a closed loop (vacuum-like closure) or, when tied to the source and detector, a path from source to detector.
- **Costs** (not obstacles here, given the guardrail change): Geroch 1967 says Lorentzian topology change on a compact region needs CTCs or loses time-orientability. The alternative is degenerate metrics (Horowitz 1991) or Morse-type points (Dowker et al.). CTCs are now allowed, so the Geroch route is open. The analytic lock's status for such manifolds is not checked.

## 4. The family of closures (Creative Lead proposal)

- **Pair:** two geons appear and later recombine. The shadow is one loop, or two arcs.
- **n-tuple:** n geons appear and annihilate all together.
- **Nested:** a pair appears, one member splits 1→3→1, and then the pair recombines.
- **General:** a finite graph of geon worldlines in object spacetime. Vertices are creation, splitting, joining or annihilation events, and the edges are geon worldlines. This is Feynman-diagram-like 4D topology. Each closure shadows to one path (or path set) in the sum over paths.
- **Bookkeeping:** a closure is labelled by its 4D topology plus its gluing data (Γ and the extension), so it is world data (#399 §3). Different closures are different worlds, or different structures within one world. Which one holds is open (see §9).

## 5. The phase (Creative Lead proposal)

- **Geometric source:** the twist or holonomy carried along the 4D structure. That is the linear part of the deck element along each geon worldline, together with the enclosed curvature (#418 B1–B3: fixed by the germ, Γ and the route, and loop-dependent).
- **From integer winding to phase:** David's "integer multiple of 2π" needs a map ℤ → U(1), n ↦ e^{inα}. For T2 cleanliness, α must be fixed by the geometry, for example the holonomy angle of a one-parameter subgroup selected by the structure's own symmetry. It must not be chosen by hand. A natural candidate is the rotation angle θ of an orientable (mirror) gluing, which is circle-valued. A non-orientable G1 piece contributes ℤ₂ = ±1, which is the "180°" case.
- **T1:** circle values are necessary, not sufficient (#418). They label routes. They do not add.
- **T2:** clean only if α comes from Γ and the germ.

## 6. The annihilation condition (Creative Lead proposal)

Candidate topological statements:
- **(A1) Charge triviality:** the product of the geons' holonomies, or their topological charges, around the closure is the identity in the relevant group (for instance, the mapping-class or deck charges cancel).
- **(A2) Bounding:** the closed 4D handle structure bounds, i.e. it caps off in object spacetime, so no handle survives to the detector slice.
- **(A3) Phase matching:** relative holonomy π between the two members (David's "180° out of phase" for opposite orientations).

Reading: (A3) is probably a *picture* of (A1) for a pair. Reversing orientation inverts the holonomy, so "coincide" for opposite directions means the product is trivial. A relative angle of π is one way to describe that for a ℤ₂ piece. Whether (A1) and (A2) are equivalent for our gluings is not checked.

## 7. Negative interference as route-dependent exclusion (Creative Lead proposal)

- **Lemma A′ exclusion exit** (the batch 23 list: exclusion, contextual dynamics, multiplicity, read-out change). Closures that annihilate (A1/A2) do not reach the detector, so the worlds in which they would have fired d_i are removed from W_i by the geometry.
- No weight is negative, and Lemma A's positivity still holds. "Darkness" would come from which closures exist, not from cancelling numbers.
- **To check:** the exclusion must depend on the *route* (the relative holonomy of two shadow paths to the same d_i), not just on d_i. Otherwise it is just a filter and gives no pattern.
- **Set aside as instructed:** the dark-fringe test and two-slit spacing.

## 8. Path-integral goal (Creative Lead proposal)

What would need to be derived, not imported, to reach Feynman's rule:
1. The set of closures that shadow to source→detector paths: the "all possible paths" of David's 1:36 AM message.
2. A geometry-fixed phase per closure (§5).
3. **The phase-addition rule:** why contributions combine as Σ e^{iφ} and not some other way. The known rule (Schulman 1968; Laidlaw–DeWitt 1971: weight each homotopy class by a unitary character of π₁ and sum) is the quantum path integral. Importing it imports QM, so it must come out of §6–§7.
4. Only after that, the step to frequencies. The Born rule itself is out of scope, and so are μ and |a|².

## 9. Ill-posed questions to avoid

- "When does the geon pop into existence?" in one world without a foliation. Topology change is slice-relative; the 4-manifold itself does not change.
- "The phase of one geon": only closure (loop) holonomies are gauge-invariant.
- "Do the two geons annihilate?" before (A1)/(A2) is fixed.
- "Which closure happened?" when nothing records it (#401 R2).
- "The amplitude of a closure": we have phases as labels, not amplitudes.
- "The probability of d_i": μ stays open.

## 10. Prior art (bibliographic only, unread, unchecked unless noted)

Hadley, Found. Phys. Lett. 10 (1997) 43, quant-ph/9706018 (4-geons with CTCs; definition verified by Literature, #418); Geroch, J. Math. Phys. 8, 782 (1967) (topology change); Horowitz, Class. Quantum Grav. 8, 587 (1991) (degenerate metrics); Dowker and collaborators on topology change and cobordism (e.g. Dowker–Garcia 1998; Borde–Dowker–Garcia–Sorkin–Surya 1999); Friedman–Sorkin, Phys. Rev. Lett. 44, 1100 (1980) (metadata only); Wheeler, Ann. Phys. 2, 604 (1957) (spacetime foam); Feynman, Rev. Mod. Phys. 20, 367 (1948); Schulman, Phys. Rev. 176, 1558 (1968); Laidlaw–DeWitt, Phys. Rev. D 3, 1375 (1971).

## 11. Next steps (proposal; no runs while paused)

1. David picks object spacetime or host spacetime.
2. On paper: the 2D/3D toy of a pair closure built from the G1 and mirror gluings; compute its relative holonomy (ℤ₂ vs R_θ).
3. Decide whether (A1) ⇔ (A2) for those gluings.
4. Find out whether exclusion can be route-dependent.
