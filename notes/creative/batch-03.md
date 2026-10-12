# Creative batch 03 (Creative Lead; DRAFT, local only, do not merge)

**Verdicts (Geometry #341, Literature #342).** All three sets **parked**. Each would reopen the lock of `papers/geodesic-lifts.md` ("Locked starting point: $W$ is real-analytic; observers follow geodesics."); reopening it is David's call. See ledger L16–L18.

**Status.** Proposal, reviewed. Nothing adopted; no `versions/` draft touched. Charter: `notes/creative/charter.md`. Built under ledger lesson L15: a set must name which hypothesis of Prop 3.2 it breaks, and give an independent physical reason for breaking it. Otherwise it only feeds the ensemble. Outside citations are marked individually: those Literature verified in #342 (ALD, Hartman–Wintner 1951, Landau–Lifshitz §75, the runaway pathology, Myrheim 1978, Brightwell–Gregory 1991, Stephani et al. 2003, Hall 2004) are marked "verified per #342"; the rest stay **unchecked**. ALD, Mino–Sasaki–Tanaka and Quinn–Wald are cited in #342's R1 wording.

## Prop 3.2 and its hypotheses (`papers/geodesic-lifts.md` §3)

> **Proposition 3.2.** Let $O=(j_\infty,u)$ with simply-connected patch $P(O)$. There is a unique geodesic $\sigma_O$ in $P(O)$ with that initial $(p,u)$, and a unique analytic curvelet $\gamma_O=\pi_{P(O)}(\sigma_O)$ in $\mathrm{Obs}$. Every geodesic lift of $O$ in every $W\in E(O)$ coincides with $\gamma_O$ on a common positive interval. In particular, geodesic evolution of one $O$ does not produce distinct analytic curves through $O$ that agree only at $\tau=0$.

The proof rests on four hypotheses:
- **H1 (state fixes the patch):** the jet determines the germ and $P(O)$ (Theorem A; analyticity).
- **H2 (motion law):** the motion is geodesic, a second-order law whose initial data $(p,u)$ are exactly what the state supplies.
- **H3 (ODE uniqueness):** the Christoffel symbols are analytic (Lipschitz suffices) and nondegenerate.
- **H4 (continuum):** $W$ is a manifold and $\tau$ is continuous.
- **H5 (analytic lifts; #341):** the lifts are analytic curves in Obs (Theorem 3), so Theorem 2 of `papers/analytic-split.md` applies, which Cor 3.1 needs. A law that produces non-analytic curves escapes Cor 3.1, not Prop 3.2.

The paper itself names the loophole (§3): a **star** of analytic curves meeting only at $\tau=0$ is allowed by Theorem 2 but "would be a different evolution law". A thick shared trunk followed by divergence is impossible for analytic curves (Cor. 3.1). So any branching of motion must happen **at points**, via a law that breaks H2 or H3 there, or via a non-analytic curve in Obs (the denial of H5, #341).

## Candidate check

| Candidate | Breaks | Independent physical reason? | Verdict |
|---|---|---|---|
| Memory (state includes a recorded past) | none: the geodesic is still fixed by $(p,u)$; memory adds data, it does not remove any | n/a | **Feeds nothing.** Not a set. |
| Memory "in between" via a third-order law (self-force) | **H2**: the law needs the acceleration, which the memoryless state does not supply | **Yes, for charge:** a charged body feels a self-force whose equation is third order (Abraham–Lorentz–Dirac; Dirac, *Proc. R. Soc. A* 167, 148 (1938)). For mass, the gravitational self-force in reduced order is a tail (past-history) term, not an acceleration term (Mino–Sasaki–Tanaka, *PRD* 55, 3457 (1997); Quinn–Wald, *PRD* 56, 3381 (1997)) | **Beats it, but gives a continuum.** Set 3. |
| Lattice instead of manifold | **H3/H4**: geodesics on a graph are generically non-unique (several shortest paths) | Partly: discreteness at the smallest scale is a charter idea; the lattice choice is arbitrary | **Beats it, discretely.** Set 1. |
| $C^k$, $k\ge2$ | none: $C^{1,1}$ already gives Lipschitz Γ, so uniqueness holds | n/a | **Feeds the ensemble** (host non-uniqueness, #332). |
| $C^{1,\alpha}$ (below Lipschitz Γ) | **H3**: geodesics can fail to be unique (Hartman–Wintner 1951, verified per #342) | **No:** the class is chosen to break uniqueness, it runs against the charter's "k→∞" justification, and it collides with Paper 1's "smooth is not enough" lock | **Beats it, but not independently.** Parked, not a set. |
| Gevrey / non-quasianalytic | H1 only (jet no longer fixes germ); the motion is still unique given the host | n/a | **Feeds the ensemble** (#332, #335). |
| Equal-probability postulate | none: it weights alternatives, it does not create them | n/a | **Feeds the ensemble** (or the arms). Not a set. |
| Follow a physically preferred direction field instead of free fall | **H2**: motion is an integral curve of a line field fixed by the jet; at degeneracy points the field is not Lipschitz or not unique | **Yes, if the field is physical**: e.g. comoving with matter (the timelike Ricci eigenvector is the fluid 4-velocity) | **Beats it at degeneracies, but with a continuum.** Set 2. Hitting risk as in #336. |
| Higher-dimensional observer / embedding (ant) | none, unless the ambient space is singled out (L1) | no | Parked (L1). |

**Why $C^{1,\alpha}$ is not a set.** It fails the taste tests: the class is chosen precisely to break uniqueness, which is an arbitrary non-physical assumption; it cuts against the charter's k→∞ route; and it hits Paper 1's "smooth is not enough" lock.

## Set 1: "Lattice geodesics tie" (breaks H3/H4) — parked

**Verdict.** Parked (#341): the ties are two-point (endpoint) problems, not initial-value ones, so the endpoint is a law of $R$ in disguise; the count diverges as ℓ→0; a network drops jets, germs and $P(O)$ (H1). #342: tie counts as weights would be a count by fiat. Reopens the geodesic-lifts lock (David's call).

**In a minute.** On a smooth surface there is exactly one straightest path from a given position and direction, which is why free fall never forks (Prop 3.2). On a grid, like city blocks, there are often several equally short routes between two corners: going east-then-north ties with north-then-east. If space is a network at the smallest scale (one of David's ideas), a traveller's straightest path can genuinely tie, and the number of tied options is a whole number set by the network. That number is not picked by us. At human scales the ties average out and ordinary smooth free fall comes back. The catch: the number of ties depends heavily on which network we choose, and it grows quickly with path length.

**Tweak.** "manifold" → a causal network at scale ℓ; "free fall" → extremal path on the network.
**Prop 3.2 check.** Breaks H3/H4: path extremality on a graph has no uniqueness theorem, and ties are generic on regular lattices. The branching is in the motion and is discrete.
**Taste.** TT1: needs a Lorentzian network notion of "extremal path" (causal sets have longest chains: Myrheim 1978, Brightwell–Gregory 1991, verified per #342; that they are typically non-unique is unchecked). TT2: the network type is a choice, so this is an LT2 burden unless the network is itself random or derived. TT3: discreteness at small scales is common in quantum-gravity programmes. TT4: counting tied paths is a count; it must not be used as a weight by fiat. Continuum limit: must recover the CWS singleton as ℓ→0 (the charter's k→∞ pattern).

## Set 2: "Ride the matter, fork at the degeneracies" (breaks H2) — parked

**Verdict.** Parked (#341, #342 R2): degeneracies give a continuum, not discrete forks; the frame is undefined in vacuum; degeneracy sets are codim-2 and rarely hit (#336 again); reading $u$ off the jet removes the state's free $u$. Reopens the geodesic-lifts lock (David's call).

**In a minute.** A real observer is made of matter and moves with it, not along an idealised free-fall line through empty space. Suppose the rule is "move with the local rest frame that the geometry itself picks out", for example the frame in which the matter is at rest. Usually that frame is unique, so the motion is predictable. At special points the preferred frame stops being unique, and then a whole continuum of frames is equally good (a degenerate eigenvalue has an eigenspace, not a few eigenvectors), so the rule allows a continuum of ways onward unless something else picks one. That is a fork in the traveller's path, not a choice of universe. The open question is what defines that frame in empty space. A second catch: as with seams in #336, we must show a typical traveller actually reaches such points.

**Tweak.** "motion" → integral curve of a geometrically preferred timelike line field (e.g. the timelike eigendirection of the Ricci tensor; in vacuum something Weyl-built would be needed), not the geodesic with given $u$.
**Prop 3.2 check.** Breaks H2: $u$ is no longer free data but read off the jet, and uniqueness fails where the eigenvalue becomes degenerate (Segre-type change; Stephani et al. 2003, Hall 2004, verified per #342; the freedom there is a continuum, #342 R2). Within the state's own jet, so the branching is in motion.
**Taste.** TT1: **THE open question for this set is what defines the frame in empty space** (Ricci vanishes in vacuum, so something Weyl-built would be needed). TT2: comoving with matter is physically motivated, not tuned. TT3: natural ("observers are made of stuff"). TT4: none yet. **Main risk:** degeneracy loci may be lower-dimensional and atypically hit, the #336 problem again. Also check that analytic degeneracies don't still give a unique analytic continuation.

## Set 3: "Self-force needs memory" (breaks H2; continuum) — parked

**Verdict.** Parked (#341, #342 R1): third order holds only for charge; for mass the Quinn–Wald deviation is a past-path tail term; reduction of order restores uniqueness; the continuum is "anything goes". Reopens the geodesic-lifts lock (David's call).

**In a minute.** Free fall assumes the traveller is a weightless point. A real charged body is pushed by its own field, the self-force. In the simplest equation for this (the electromagnetic one), knowing where you are and how fast you're moving is not enough: you also need your acceleration. For a body's mass, the self-force instead depends on its whole past path (a "tail"), not on its acceleration. If the observer's state is "memoryless" (David's question), the next step is then not fixed. If the state carries some memory, it is. This is a physical reason for "something in between". The catch: the extra freedom is a continuum ("anything goes"), and physicists usually remove it with a reduction-of-order rule that restores uniqueness.

**Tweak.** "motion law" → geodesic plus self-force (third-order), with the state kept at $(j_\infty,u)$.
**Prop 3.2 check.** Breaks H2 for an independent physical reason (self-force is standard physics). But the alternatives are a 3-parameter continuum of initial accelerations, and the standard physical fix (Landau–Lifshitz §75 reduction of order, verified per #342) reinstates uniqueness. Probably beats Prop 3.2 only by keeping runaway-type solutions, which most physicists reject.
**Taste.** TT1: well-posed as an ODE. TT2: independent. TT3: the runaway issue is a known pathology (verified per #342). TT4: none. Ranked last: no discreteness, and the fix kills it.

---

**Ranking (draft).** Set 2 > Set 1 > Set 3. Set 2 has a physical reason and branching in motion, but its degeneracies give a continuum, not discreteness; its risk is hitting. Set 1 is discrete but the network is a choice. Set 3 is independent but a continuum.
