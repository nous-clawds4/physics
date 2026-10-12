# Creative batch 07: branches as geometries (Creative Lead; proposal, do not merge)

**Status.** Exploration only, under David's 3:14 PM ET ruling. Nothing goes into `versions/` or `papers/`. All outside citations are **unchecked**. In-repo pointers: `papers/geodesic-lifts.md` (Prop 3.2, Cor 3.1 and "Multiplicity of $E(O)$ is locally invisible"), `papers/patch-edge.md` (Prop 7.2), `papers/analytic-patch-from-jet.md` (Theorems A–B), v0.10.1 (§4, §9, §11), #320, #324, #336, ledger L15–L26.

**Target (David, 3:43 PM ET, relayed via Physics Lead, not signed; recorded verbatim in the ledger).** "branch A means geometry (fundamental group) A, B means B … Somehow, the local state teaches the observer something about the global state."

**The measure under (M1).** David said weighting by counting worlds would be acceptable *if* that is what (M1) means; (M1) as recorded is per-vertex EPP1, not counting worlds, so whether L23 still blocks is flagged for David and not resolved here. Batch 07 stays within (M1) as recorded and writes no other weights; see the ledger's (M1) explanation for how (M1) relates to counting worlds.

---

## Repairs and verdicts (Geometry #352, Literature #353)

**Trap premises, repaired (#352).**
- "The universal analytic extension" is ill-posed: maximal analytic extensions need not be unique (Taub–NUT). So each host is a quotient of *its own* universal cover; the text below should be read that way.
- The no-CTC condition is precise: no deck element maps a point into its own chronological future.
- Lensing *does* differ between quotients. It fails to split the compatible set only because the images are not in the local state.
- Literature (#353) confirms the trap sketch: periodic copies are real in a $\Gamma$-periodic cover.

**L27 (#352).**
- "Generic" is meant only topologically.
- The list is countable only for cocompact hyperbolic spatial sections with dim ≥ 3 ($\mathbb R\times\mathbb H^3/\Gamma$; Mostow/Prasad).
- Infinite-volume hyperbolic, 2+1 Teichmüller, flat, and AdS$_3$/BTZ quotients are continua. The dS case is unchecked.
- Known (#353): Clifford–Klein space forms; Wolf, *Spaces of Constant Curvature*.

**L28 (#352).**
- With a record in the state, the split is genuine, not a nested prefix. But it is *learning which world*, not branching of the motion.
- The partition is countable, not necessarily finite.
- In the flat case, return times vary continuously. Accelerated expansion may give no return at all.
- Costs: the non-local state breaks the germ definition; #324's gauge quotient must act on records; emission needs a body.
- Known in spirit (#353): Ellis's "small universe"; the observer copies of Cornish–Spergel–Starkman.

**Drops (#352).** "The whole causal past", taken with its self-overlap identifications, is Set 2 in disguise.

**Citation marks (#353).**
- V-text: Cornish–Spergel–Starkman 1998; Planck 2015 XVIII.
- V-meta: Lachièze-Rey–Luminet; Planck 2013 XXVI; Ellis 1971; Ellis–Schreiber; Lehoucq et al. 1996; Mostow 1968; Thurston–Jørgensen.
- All others remain unchecked.

**Status.** L27 and L28: **awaiting final verdict** (pending David). L28's lock and split-rule questions are David's call (see Items for David).

## Items for David

1. **Memory beyond the lock.** L28's record of received self-signals goes beyond the jet/patch lock: the state is no longer the germ (#352).
2. **Split rule.** Splitting while the patches are identical conflicts with Paper 1's split rule, under which a split needs differing patches.
3. **Record as state.** The narrowing works only if the record counts as part of the observer's state.
4. **(M1) vs counting.** (M1) as recorded is per-vertex EPP1, equal shares per arm, not weight proportional to the number of worlds; that is EPP2 / (M2). L23 is pending David's answer. Counting is allowed in creative sets only as a labelled conjecture (ledger standing rule).

## The trap to beat (why the obvious version fails)

Under analyticity, the germ $O$ fixes the simply connected patch $P(O)$, and with it the universal analytic extension $\tilde M$ (Theorems A–B). Every compatible host with that cover is a quotient $\tilde M/\Gamma$, with $\Gamma$ a discrete group of isometries of $\tilde M$ acting freely and properly (and, to avoid CTCs, with no timelike translations). Along the observer's path, every such quotient gives the **same germ sequence**: the projection is a local isometry, so "Multiplicity of $E(O)$ is locally invisible" (geodesic-lifts §2), and patch-edge Prop 7.2 holds. That is the identical-state trap (L26). Worse, **light does not help either**.
- Any light ray in $\tilde M/\Gamma$ lifts to a ray in $\tilde M$ ending at the observer's lift.
- So everything the observer sees *of the geometry* (the curvature lumps, their "multiple images") is identical in $\tilde M/\Gamma$ and in $\tilde M$.
- In $\tilde M$ the "images" are real periodic copies. An analytic germ that admits a quotient forces $\tilde M$ itself to be $\Gamma$-periodic, a crystal universe.
- So topological lensing *of the geometry* cannot split the compatible set (Creative Lead sketch, unchecked).

Both sets below get past the trap by naming what does differ: something that is **not** part of the host geometry and so is not periodic.

---

## Set 1: "The germ fixes the cover; its symmetries bound $\pi_1$" (L27)

**In a minute.** From its local state the observer can, in principle, work out the shape of the "unrolled" universe: the version with no handles, like a flat strip of wallpaper before it is rolled into a tube. What it cannot work out is how that unrolled universe is rolled up. It can work out *which ways it could be* rolled up, though, because rolling up is only possible along the universe's own symmetries. If the unrolled universe has no symmetries, there is only one possibility: no handles at all. If it has a repeating pattern, the possible handle structures are exactly the ways of matching repeats, which is a definite but limited list. This is the "local state teaches something about global state, but not everything" mechanism, and it is static. Set 2 adds what makes the list shrink over time.

**Mechanism (named).** *Symmetry bound.* The germ $\to$ $\tilde M$ (Theorems A–B) $\to$ $\mathrm{Isom}(\tilde M)$. The admissible fundamental groups are then the discrete subgroups $\Gamma\le\mathrm{Isom}(\tilde M)$ acting freely, properly, and with no timelike elements. So $\pi_1$ is constrained (it must embed in $\mathrm{Isom}(\tilde M)$) but not fixed.
**Checks.**
- Prop 3.2, H1–H5: nothing is broken. Free fall is deterministic in each host, which fits David's 3:19 ideal.
- Nested prefix: not applicable. It is a statement about the compatible set at one instant, not about splitting.
- #320: quotients of an inextendible $\tilde M$ should be inextendible (unchecked).
- #336: no hitting is needed.
**Count.** The list of $\Gamma$ is countable for hyperbolic spatial sections only when $\Gamma$ is restricted to lattices (finite-volume quotients: Mostow 1968 rigidity plus countably many finitely presented groups); infinite-covolume groups (Schottky, quasi-Fuchsian) come in continuous families. It is a continuum for flat sections (lattice shape moduli). Generic germs (trivial isometry group) give a single host. That is "teaches everything": the charter's "all possible fundamental groups" is realised only on symmetric covers.
**Weak points.**
1. Nontrivial $\pi_1$ needs an exactly periodic cover, so the multiplicity lives only on non-generic, symmetric hosts.
2. On its own, Set 1 does not split along the path.
3. The flat case is a continuum.

## Set 2: "The ant meets its own trail": self-signals split the set by $\pi_1$ (L28)

**In a minute.** David's ant can learn that it lives on a cylinder by walking around and finding its own footprints. Our observer can do the same with light. Light it sends out, or light it gives off, travels around the universe's handles and can come back to it. In a world with a handle the observer eventually sees itself; in a world without one it never does. Copies of the geometry don't help, because in the unrolled universe those copies really exist. But the observer itself is not part of the geometry, so there is no copy of *it*. Each time a possible handle is long enough for its light to have made the trip, the list of possible worlds splits into "I've seen myself that way" and "I haven't". So the branching comes from information arriving, not from the motion forking. Branch A really is geometry A: different fundamental groups, with free fall predictable in each.

**Mechanism (named).** *Self-signal return.* Treat the observer's emitted or scattered light as a test field on the host, not part of $g$. For each admissible $\Gamma$ (Set 1), the observer's past light cone in $\tilde M/\Gamma$ contains its own earlier worldline exactly when some $\gamma\in\Gamma$ carries the lift of that earlier worldline into the lift of the past cone. The first such proper time $\tau_\Gamma$ is fixed by the geometry, by the length of the shortest null loop through the deck translate (a systole-type quantity, unchecked). At each $\tau_\Gamma$ the compatible set splits into hosts where a self-image arrives (those whose $\Gamma$ contains that element) and hosts where it doesn't. The splits come at discrete proper times, and each is a finite partition.
**What the observer state must include.** The germ alone is identical across all quotients, so a **record of received self-signals** must be part of the state. This is memory, the charter's "memoryless or not?". It breaks the memoryless reading of Problem note 6, and it adds to the observer-state definition (a cost on the jet/patch lock). It does not touch H1–H5 for the motion.
**Checks.**
- **Prop 3.2 / Cor 3.1 / H1–H5:** intact for the motion. The split is in what is known, not in the path.
- **Nested prefix (Geometry's caveat, L22):** escaped. The hosts do not end early. They differ in a recorded observation at $\tau_\Gamma$, so the state sequences (germ plus record) genuinely differ after $\tau_\Gamma$.
- **Identical-state trap (L26):** escaped only because the record is added. Without it the trap holds.
- **#336 (special aim):** not needed. Light goes out in all directions, so in a host with a compact spatial direction the return is generic, provided expansion doesn't outrun it (unchecked).
- **#320:** as Set 1.
- **L23 / measure:** no weight is written. Under (M1), each split is a vertex with as many arms as observation classes, and (M1) gives each arm an equal share regardless of how many hosts are behind it. That is **not** "weight ∝ number of worlds". Under counting worlds, the shares would follow the number of admissible $\Gamma$ in each class, which is infinite or a continuum in most cases. The ledger's (M1) note flags this as David's call.
- **Borrowed QM:** none. **Everett framing:** none; the hosts are alternatives, not co-existing branches.
**Count.** For finite-volume (lattice) hyperbolic quotients the compatible set is countable and each split partitions it; infinite-volume groups come in continuous families (#353). For flat ones it is a continuum: each return also measures the loop's length and direction, which is a continuous datum.
**Weak points.**
1. The state must carry memory (a record), which runs against Problem note 6 and needs David's call.
2. A "self-signal" needs the observer to emit or scatter a test field, i.e. a body; the framework's observer is a germ.
3. Splits are informational, so this is ensemble narrowing (the charter's "evolution of the ensemble"), not motion branching. That is David's 3:19/3:43 framing, but it is a different object from the branch sets $B_R$ of v0.10.1 §8.2.
4. On flat or symmetric covers the outcomes are continuous data (loop length and direction), so the partition is a continuum unless the cover is rigid.
5. The trap sketch ("geometry lensing cannot split") is unchecked and needs Geometry.

---

**Dropped directions** (per #352, "whole causal past" with self-overlap identifications is Set 2 in disguise).
- Topological lensing *of the geometry* (multiple images of curvature lumps): killed by the trap above, because images are periodic copies in $\tilde M$.
- "The observer's state includes its whole causal past of geometry": same as the germ under analyticity, so it adds nothing.
- Non-analytic quotients: a continuum (E1, batch 05).
