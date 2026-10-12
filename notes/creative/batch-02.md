# Creative batch 02 (Creative Lead; proposal, do not merge)

**Verdicts (Geometry #338, Literature #339).** All three sets **parked**; see ledger L11–L13 and lesson L15. #339 R1 and R2 applied.

**Status.** Proposal only; nothing adopted; no `versions/` draft touched. Charter: `notes/creative/charter.md`. Ledger: `notes/creative/ledger.md` (L11–L14 added). Taste tests TT1–TT4 (infinite-harness `docs/lessons/creative-tweaks.md`). Which set, if any, to pursue is David's call.

**Starting point (#336, Geometry).** Within one host, curvelets that hit a codim-2 seam form a meagre, codimension-1 set of data, whatever the seam's causal type. Cones don't focus rays onto the seam. Countably many seams don't help, dense seams break the definition, and walls have no sheets. So Sheets as it stands is a property of the ensemble of hosts, not branching of motion. The smallest fix, #336 (f), is a finite observer tube of radius $r_0$. It costs three things: (C1) an undefined scale; (C2) a change of state from a germ at a point to a tube; (C3) a sheet rule that is a law of $R$ in disguise. Batch 02 attacks C1 first, as Physics Lead asked, and offers one other mechanism plus one recycled idea.

**Charter hooks.** "flat at the smallest scale, nonflat (and nontrivial topology) microscopically, flat at human scale…"; "using “low energy approximation” as justification"; "if we let k approach infinity, we no longer need to justify it"; "all possible worlds includes all possible fundamental groups".

---

## Set 1: "The tube is the coarse-graining scale" (L11, centre of batch)

**In a minute.** #336 showed that a point-sized traveller essentially never touches a seam, but a traveller with some size does. The problem is "what size?", because any number we pick is arbitrary. David's notes suggest an answer: the universe may be tangled (full of tiny handles and seams) at a microscopic scale ℓ and smooth at the human scale. Then the traveller's size isn't a new constant. It is the scale at which the traveller can no longer see the tangle, which is the usual low-energy approximation. Every honest observer is much bigger than ℓ, so as the ratio r₀/ℓ grows the exact size stops mattering, the same way David's "let k go to infinity" removes the need to justify k. The catch: we still have to say what the traveller's state is once it's a tube, and which sheet it ends up on.

**Tweak.** One word: "observer state" means the coarse-grained state at the scale where the host's microscopic topology averages out, not the germ at a point. $r_0$ is then set by the host (the seam/handle spacing ℓ), and the claim to test is whether branching statistics have a limit as $r_0/\ell\to\infty$.
**Taste.** TT1: "coarse-graining scale of a host" must be defined (for example, the smallest radius above which the tube's region is simply connected and nearly flat). Undefined so far. TT2: the scale comes from the host, not from the Born target. This is the point of the set, and it answers C1 if the limit exists. TT3: low-energy/effective-description reasoning is standard physics. TT4: C3 remains, so the sheet rule must not be equal weight by fiat.
**Next check (Geometry).** With seams at spacing ℓ (#336 (d), countable case), does a tube with $r_0\gg\ell$ meet seams at a rate that is a function of $r_0/\ell$ alone, and is any quantity finite as $r_0/\ell\to\infty$? If every quantity diverges or depends on $r_0$, the set dies.
**Open costs.** C2 (state change) is now the tweak itself, and it collides with the germ-based observer space of v0.10.1. Possible tension with the charter's warning against non-physical existence examples: none is used here.

## Set 2: "Handles inside the tube" (L12; recycles L7)

**In a minute.** Instead of seams we use the tiny handles (wormhole-like loops) that David's notes already allow in "all possible worlds". A traveller of size r₀ that encloses handles has a state that must fit together consistently around each handle, much as a wave must fit around a ring. Only a few ways of fitting exist, so the options come out discrete and the number is set by the topology. Local motion stays deterministic. The multiplicity comes from a global consistency condition (the parked billiard-ball idea, L7) applied inside the traveller rather than to spacetime loops. There is no time machine and no seam to aim at. Handles are everywhere at scale ℓ, so the condition applies to every typical traveller. The catch: "fitting together around a loop" is close to borrowed quantum mechanics, which we must not import.

**Tweak.** "consistency" (L7) is applied around non-contractible loops of $\pi_1$ inside the observer tube (microscopic topology), not around loops in $V$ (Set 3 of batch 01, parked by #334).
**Taste.** TT1: the consistency condition is undefined; it must be written in geometric terms (holonomy of the tube's frame around the loop?) before anything else. TT2: discreteness from $\pi_1$ is fixed by the host, which is good. TT3: microscopic topology is in the charter's tentative definitions. TT4: **high hazard.** Sectors labelled by representations of $\pi_1$ are Schulman 1968 / Laidlaw–DeWitt 1971 (#332 R4), so this must not borrow amplitudes. Also check that a single history is not again forced (the #334 objection to Set 3): in free fall, does the tube's consistency condition have more than one solution?
**Depends on** Set 1's tube (C2).

## Set 3: "Where the observer's patch runs out" (L13; another mechanism)

**In a minute.** The observer "knows" a simply connected patch of its world around itself. In a world with handles the patch itself never overlaps itself: $P(O)$ is the maximal simply connected continuation, like the unrolled map of a donut. What overlaps is its image in the host, which is ensemble structure ($E(O)$), and `papers/patch-edge.md` already finds "The hitchhiker story is dead at the boundary too". This set proposes that the branch point is where the patch runs out, and not a place in spacetime the traveller has to hit. Every traveller in a tangled world reaches such a point, so hitting is not rare. The choices there are the ways of continuing the patch, which are discrete and counted by the topology. The catch: this may be one more fact about which world we are in (ensemble) rather than a fork in the motion. That is exactly what #336 found for Sheets, so it needs Geometry's check first.

**Tweak.** "branch point" means where the map from the analytic patch $P(O)$ carried along the curvelet into the host stops being injective (an injectivity-type scale), not where the curvelet meets a seam. ($P(O)$ itself stays simply connected; patch-edge Prop. 7.2: "quotients do not lengthen past the cover".)
**Taste.** TT1: "patch stops being simply connected" needs a definition along a path. TT2: set by the host's topology. TT3: natural. TT4: none yet. **Likely failure:** continuation along one path is unique (#331 §0; #336 setting), so this may be host/ensemble structure only. Ranked last on that risk.

---

**Ranking (Creative Lead, for review).** Set 1 > Set 2 > Set 3. Set 1 is the direct answer to #336's C1; Set 2 needs Set 1. Set 3 is the only mechanism that skips the tube, but it carries the #336-type risk.

**Not proposed.** Walls (#336 (e), killed), dense seams (#336 (d), killed), focusing (#336 (c), killed), Planck-length $r_0$ by fiat (an LT2 burden, #336 (f)).
