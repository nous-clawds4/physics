# Batch 23: step back: where could a classical cross term come from? (Creative Lead; brainstorm; do not merge)

**Status.** Brainstorm only, no computation. Classical only; no Born rule; no $|a|^2$; no superposition by hand; (M1) untouched at L3; CTCs as exploration only; loosening the analytic lock as exploration only. Citations are unchecked unless they were verified earlier. Nothing goes into `versions/` or `papers/`. Stacked on batch 22 (#406 at 5b14b3d). Ledger rows L90–L97.

**David, 9:36 AM ET 2026-10-13, relayed by Physics Lead, Physics Lead chat, not signed (widget answer):**
> Step back: have Creative Lead propose new idea sets for where interference could come from.

---

## For David (plain summary)

- **What is dead.** Three things can't make dark spots: weights on single routes, weights on whole worlds, and the particle's own weak echoes. The reason is simple. If every world counts with a non-negative weight, and opening a slit only *adds* worlds, then the two-slit pattern is a blend of the one-slit patterns. A blend is never darker than both of its ingredients.
- **The way out.** For a spot to go darker when the second slit opens, something in the assumptions must fail: opening it removes worlds that used to land there, changes where launches land (the slit changes the fields or walls), lets one launch have several histories, or changes what counts as a hit. Classically, the natural way for that to happen is a **consistency condition**: a world with both routes open must satisfy a condition, around the loop the two routes make, that a one-route world never faces.
- **Six idea sets (one rejected), each tweaking one concept.**
  1. A condition around the two-route loop.
  2. Self-consistency of the whole history.
  3. The screen hit has to be a lasting record.
  4. What a hit records beyond its position.
  5. Counting the observer's histories.
  6. Loosening the analytic lock.
  7. Conducting slit walls: slit-dependent dynamics.
- **After review.** Set 1 (the loop condition) is dead on the flat cylinder unless a source turns up. The loop is the handle's own cycle, which is there whichever slit is open, and Misner's 8πN is a period of time, not of path difference; supplying a period by hand would be tuning. Set 6 goes with it. **Most promising now:** Set 2, where one launch can have several self-consistent histories (exploration only, needing a CTC host and a self-interacting particle), and Set 7, conducting slit walls.
- **Rejected as ill-posed or as sneaking in the answer:** "the particle takes both routes" and "negative weights".

---

## What's dead, and the one door left

**Lemma A' (exclusion is necessary) [A, from #405 Lemma A].** Assume three things:
- (i) every world has exactly one route;
- (ii) weights are non-negative;
- (iii) the two-route world set is the union of the one-route world sets, with unchanged weights up to one normalisation.

Then the normalised pattern satisfies $\min(\hat I_0,\hat I_{-1})\le\hat I_{\rm both}\le\max$ (#405, M1 form). So a dark spot needs one of these to fail. Dropping (ii) is rejected (Set R). Dropping (i) by "the particle takes both routes" is not a classical world (Set R), but (i) also fails legitimately when the dynamics has several solutions per launch (EKT multiplicity, Set 2; non-Hausdorff extensions, Set 6). The remaining exits are: (iii) fails: **opening a route must exclude, or re-weight in an x-dependent way, worlds that existed with one route open.**
- Re-weighting chosen to fit is the LT2 failure of #405.
- So the independently motivated candidates are: **exclusion mechanisms** (opening a route removes worlds); **contextual dynamics** (the open slit changes boundary conditions or fields, e.g. conducting walls (#406), so the launch-to-hit map changes); **multiplicity** (several self-consistent histories per launch, which breaks (i)); and **a change of the read-out map**. All four are exhaustive negations of (i)–(iii) plus the fixed record map: a condition a world must satisfy that depends on the *set* of open routes.

The **dead list** is: route-local weights (#401, additivity), whole-world configuration-independent weights (#405 A), and weak self-field echoes (#406: smooth lens, Lemma A for kick-only slits).

**Kill rule for every set.** The set must exclude worlds, and the exclusion must be independently motivated: it must exist before anyone looks at fringes. A which-route record must lift it.

---

## Set 1: a loop condition on the two-route cycle (holonomy or regularity exclusion)

**Plain summary.** With both slits open, the two candidate routes bound a closed curve. If they differ by a wrap, that curve is the handle's own cycle and exists with either slit open; if they pass two slits on one wrap, it encircles the barrier. Suppose the world must be regular around every such loop. Then worlds whose path difference violates the condition are not allowed, and they leave dark spots that repeat.

- **Concept tweaked.** "Compatible world": add the requirement that the world's fields be regular (single-valued) around every cycle that the particle's possible routes enclose.
- **Independent motivation.** Regularity conditions that quantise a classical parameter already exist without quantum input:
  - Misner's condition in Taub–NUT: time is periodic with period 8πN, to remove the wire singularity (Misner, J. Math. Phys. 4 (1963) 924; bibliographic only, per Literature). This is a condition on a spacetime cycle, present whether or not a slit is open.
  - Dirac-string-free monopole gluing [unchecked; the Dirac condition itself uses ħ, so it must be avoided].

  The tweak is to ask whether the cycle *created by opening a slit* inherits such a condition.
- **Mechanism.**
  - Let $\Delta(x)$ be the difference in length or proper time between the two geodesics to $x$ in the cover. Caution: this is not a holonomy. Holonomy of a fixed connection depends only on the loop's homotopy class, so it cannot vary with $x$. And in a one-route world the second geodesic is a curve, not a history, so any condition on $\Delta(x)$ is a condition on a counterfactual and must be justified as such.
  - A regularity condition of the form "a holonomy accumulated around the cycle is in a discrete set" is satisfied only for $\Delta(x)$ in a lattice.
  - It excludes, or allows, worlds periodically in $x$.
  - It is an **exclusion**, not a weight: there are no amplitudes, nothing is squared, and nothing is added.
  - No known rule turns a regularity scale such as Misner's 8πN (a period of the Taub–NUT time coordinate, fixed by the host) into a period in $\Delta(x)$. On the flat cylinder N = 0 and there is no scale at all. Supplying one by hand would be T2 tuning (a de Broglie length in disguise).
- **What a which-route record does.** A record body on one route carries its own field or flux (#399 persistence) through the cycle. That shifts the cycle's holonomy by a world-dependent amount and smears the condition, so the dips go away. A passive record that carries no field would *not* lift it. That would be a prediction distinguishing this set from quantum mechanics.
- **First killing check.** Is there any classical, ħ-free regularity condition whose cycle is the two-route loop *formed by an aperture configuration* (test matter), rather than by the spacetime itself?
  - If regularity only constrains spacetime cycles, then the cycle exists whether or not the slit is open (fixed wrap, #405). Opening the slit then changes nothing, and the set is dead.
  - Literature should check the Misner and NUT regularity sources first.
- **Ill-posedness flag.** "Holonomy around a cycle formed by test-matter apertures" is defined only if the field is required to be regular on the region the apertures bound. That must be stated, not assumed.
- **Answer to the first killing check (Literature, #407).** No ħ-free condition on an aperture-bounded cycle is known.
  - Misner/NUT conditions are spacetime-cycle conditions.
  - The water-wave AB analogue (Berry, Chambers, Large & Upstill, Eur. J. Phys. 1 (1980) 154) needs a wave.
  - EBK/Maslov (Keller, Ann. Phys. 4 (1958) 180) needs ħ.

  Bibliographic only, per Literature. On the flat cylinder there is no x-dependent holonomy, and the loop is the handle's own cycle, present with either slit open (Geometry, #407).
- The record prediction (a flux-carrying record smears the dips, a passive one doesn't) is well-posed only in the test-field limit (#392).
- **Status: dead on the flat cylinder, pending a source. Was rank 1; now L0.**

## Set 2: global self-consistency (EKT-type), with open routes constraining launches

**Plain summary.** With a time-shifted handle, a particle can meet its own past. Only self-consistent histories are allowed. Opening a second route can make some launches inconsistent, and those launches then simply don't happen.

- **Concept tweaked.** "World" means a globally self-consistent solution, as in the Echeverria–Klinkhammer–Thorne billiard ball (PRD 44 (1991) 1077; verified, Crossref; readings per #365).
- **Independent motivation.** This is the standard classical treatment of CTC spacetimes. Consistency is not chosen for fringes. Exploration only (CTC).
- **Mechanism.** EKT found infinitely many consistent solutions for a wide class of "dangerous" initial trajectories, and exactly one for a ball starting at rest far from the wormhole (V-text abstract, per #365); in the standard account they found no initial trajectory without a solution [abstract-level; zero-solution launches are not reported]. Uniqueness results are for linear fields (Friedman–Morris), not EKT. So the documented lever is multiplicity, which breaks Lemma A' (i) and needs a counting rule (#399), not exclusion. Interaction (self-collision) is required for any non-uniqueness (Friedman et al. 1990, PRD 42, 1915, abstract only). If the slit configuration enters as boundary data for the consistency equations, then opening a route changes which launches have solutions. That is exclusion, and also multiplicity (non-uniqueness).
- **What a which-route record does.** The record is part of the world and enters the consistency conditions. It can restore solutions that had been excluded.
- **First killing check.**
  - Use a time-shifted wormhole host (offset mouths, #385 L56; note per #398 that a fixed time-shift gluing has CTCs at every time, so this is a new host, not the cylinder toy), with a self-interacting particle: is the set of consistent launches through slit A different with slit B open versus closed?
  - EKT-type self-collision requires the routes to interact. With a single particle and slits far from the mouths, the condition may be identical. Then the set is dead.
- **Confidence: L1, rank 1 (up).** Its lever is multiple histories per launch, which breaks (i). It needs the offset-mouth CTC host and a self-interacting particle (exploration only), and it reopens the counting problem (#399).

## Set 3: the screen hit must be a lasting ledger entry

**Plain summary.** A hit only counts if the screen keeps a readable record of it. With both routes open, a record at some places might be unreadable or unstable, and those places would be dark.

- **Concept tweaked.** "Hit": a persistent entry in the append-only diary (#399), readable by a handle round trip, rather than a coordinate crossing.
- **Independent motivation.** This is already our definition of measurement (#399 persistence); we are applying it to the screen.
- **Mechanism.** Persistence needs the entry's readout loop to be unambiguous. With both routes open, entries at some $x$ might fail the readout criterion, e.g. if their round-trip classes coincide with an open route's cycle. Then they would be excluded, giving exclusion through the record definition.
- **What a which-route record does.** A separate route record makes the readout unambiguous and restores the hit.
- **First killing check.** Write the persistence criterion for a screen entry with one route open and with two. If the criterion does not depend on the open routes (likely, because the entry's readout is local to the screen), the set is dead.
- **Ill-posedness flag.** "Unreadable because ambiguous" must be defined by #399's graded-effectiveness criterion. Without that, reject.
- **Confidence: L1, rank 3.** Even if it works it gives dips where the routes overlap, not periodic ones. (It is the read-out-map exit of Lemma A'.)

## Set 4: a hit records more than x

**Plain summary.** A hit also fixes when and how the particle arrived. Worlds that land at the same place but disagree on those details are different outcomes.

- **Concept tweaked.** The observer state at the hit is (x, arrival time, arrival momentum, …), not x alone.
- **Independent motivation.** The memory-augmented state (#388) already includes everything received.
- **Mechanism.**
  - Finer records split record classes.
  - Counting distinct observer states rather than launches would make counting non-additive: two routes to the same full state would count once.
  - This is **subadditive but never below either route**. It is a max-type merge, so it cannot give dips.
- **What a which-route record does.** It splits the merged states again. The prediction is a difference between a record and no record, but never a dark fringe.
- **First killing check.** Already done in the abstract: distinct-state counting gives $\hat I_{\rm both}\ge\min$. **Dead for dips**, although it is a genuine record-dependent non-additivity, worth recording.
- **Confidence: L0 for dips, rank 6.**

## Set 5: counting over observer histories, not launches

**Plain summary.** Count the different life stories the observer could have, rather than the ways the particle could be launched. Opening a slit changes how many stories there are, and so how much each one counts.

- **Concept tweaked.** The counting measure is uniform over observer histories (record-class sequences, #399 labelled counting).
- **Independent motivation.** "Fork = discovery": what is distinguished is the observer's experience.
- **Mechanism.**
  - The weight per world is $1/|\text{class}|$, which depends on the configuration through the class sizes.
  - That is a reweighting. Without exclusion it again gives the number of classes reaching $x$, which is non-negative and monotone under adding routes.
  - Dips only if opening a route *merges* classes across different $x$, which is not possible because $x$ is in the record.
- **What a which-route record does.** It splits the classes, so the counts change but there are still no dips.
- **First killing check.** Use the S1 two-launch case, with classes counted per $x$, both slits versus one. Expected: no dips. Dead unless combined with exclusion (Sets 1–2).
- **Confidence: L0–L1, rank 5.**

## Set 6: loosen the analytic lock (exploration only)

**Plain summary.** If the world isn't forced to be smooth in the strongest sense, there is extra freedom at the handle. Opening a route could then change which extensions exist.

- **Concept tweaked.** Analyticity becomes smoothness: continuation past the handle or Cauchy horizon is non-unique (extension data, non-Hausdorff branching; #388).
- **Independent motivation.** Smooth GR is the standard setting, and the analytic lock is our own choice.
- **Mechanism.**
  - The world set includes extensions.
  - If the extensions compatible with a hit must glue consistently along *both* open routes, then a two-route world needs matching extension data on the cycle. That is an exclusion condition like Set 1, now with free data.
  - The data is a continuum, so the uncountability (#399) comes back.
- **What a which-route record does.** It fixes the extension data on one route and lifts the matching condition.
- **First killing check.** Can any matching condition on extension data be discrete without being chosen? If it is a continuum, there are no dips (only measure-zero exclusion). It does reduce to Set 1: the matching cycle is a spacetime cycle that exists with either slit open, and the second route is counterfactual. So Set 6 lives or dies with Set 1's first killing check, and as a counting proposal it is ill-posed (no measure on extension data).
- **Ill-posedness flag.** There is no measure on extensions. Any count is ill-posed until one is defined, so it is rejected as a counting proposal and kept only as a source of conditions.
- **Status: reduces to Set 1, so dead pending a source; ill-posed as counting. L0.**

## Set 7: contextual dynamics (conducting slit walls)

**Plain summary.** Real slits are made of matter. If the walls are conducting, opening the second slit changes the walls, and so changes the field that the charged particle feels, everywhere along its path.

- **Concept tweaked.** The slit is no longer a kick-only test aperture. The barrier is a conductor whose image charges depend on which slits are open.
- **Independent motivation.** This is ordinary electrostatics of real barriers. The #406 weak point and the Geometry review flag it.
- **Mechanism.** The launch-to-hit map depends on the configuration (the contextual-dynamics exit of Lemma A'). Batch 22 suggests that at first order this is a smooth deformation, so no repeated dips are expected at that order. Nonlinear focusing could fold the map, giving caustics but not periodic bands.
- **What a which-route record does.** A conducting record body adds its own images. A passive, uncharged one does nothing.
- **First killing check.** Compute the first-order image force with a conducting plane carrying one or two slits (for example a thin-slot Green's function), and compare the hit maps.
- **Confidence: L0–L1, rank 2 (up).**

## Set R (rejected)

- **"The particle takes both routes":** not a classical world (one trajectory per world, #401). It is superposition by hand. **Rejected.**
- **Signed (negative) world weights:** well-posed, but it sneaks in the answer (LT2), because cancellation is the target. Prior art (not endorsed): quasi-probabilities with negative values (Wigner, Phys. Rev. 40 (1932) 749; Feynman, "Negative probability", 1987). **Rejected.**

---

## Recommended order of checks

1. **Set 2, multiplicity:** EKT on the offset-mouth host (#385 L56) with a self-interacting particle (exploration only). Does the slit configuration change the multiplicity or the consistent histories per launch, and what counting rule (#399) applies?
2. **Set 7, conducting slit walls:** a first-order hit map with a conducting barrier carrying one or two slits.
3. **Set 3, screen persistence criterion:** is it local, or does it depend on the open routes?
4. **Set 5, class counting in the S1 case:** a quick formal check, expected dead.
5. **Sets 1 and 6:** dead pending a source. Reopen only if Literature finds an ħ-free condition on an aperture-bounded cycle.
6. **Set 4:** no further check; dead for dips.

## Weak points

1. Lemma A' is stated for the toy's one-route worlds and normalised patterns. Worlds with several routes, such as self-colliding CTC worlds, are outside (i). Set 2 lives there and must be counted carefully.
2. Set 1 has the highest LT2 risk: any condition chosen *because* it is periodic in Δ is tuning. Only an existing regularity rule is admissible.
3. No set gives the quantum fringe spacing (λ = h/p). Nothing here predicts it, and matching it would need a new scale.
4. CTC-dependent sets (2, possibly 1 via Misner) are exploration only.

Ledger: L90–L97 (L97 records David's 9:36 AM words).
