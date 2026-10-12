# Geometry quick verdict: creative batch 07 (#351), do not merge

**Read at:** #351 head `43b5d51` (`notes/creative/batch-07.md`), main `e41412b`.

**Record type:** rough review. It applies nothing and is neutral on David's open calls (exploration under the 3:14 PM ET ruling, target of 3:43 PM ET). (M1) is not revisited. The arguments are sketches, not proofs. **(V)** means verified in the repository; **(U)** means from memory and not checked.

**Verdicts.**
1. **Trap sketch:** right in conclusion, two premises need repair. "The universal analytic extension" is not well defined. "No timelike elements" is too weak to rule out closed timelike curves.
2. **L27:** the bound "$\pi_1$ embeds in Isom" is right. "Generic" is only well posed topologically. Countability holds only for closed (cocompact) quotients of hyperbolic spatial sections, dimension $\ge3$; everything else listed is a continuum.
3. **L28:** with a record in the state the split is genuine, not a nested prefix. But it is observational narrowing of $E(O)$, not branching of motion. Partitions are countable, not necessarily finite, and the costs are real.
4. **Drops:** none wrongly dropped. One needs a qualifier.

**Not flagged** for a full note.

## (1) The trap

- **"The universal analytic extension $\tilde M$" is ill-posed as stated.**
  - Theorems A–B give $P(O)$, a simply connected *patch*, not a maximal extension.
  - Maximal analytic extensions can be non-unique: Taub–NUT, Chruściel–Isenberg 1993 (V, #332). Gluing the inequivalent extensions gives a non-Hausdorff object. This is the nested-prefix caveat of #346 §1 again.
  - The repair: every compatible host $M$ is the quotient of its *own* universal cover $\tilde M$ by $\pi_1(M)$. $\tilde M$ is simply connected, analytic and contains a copy of $P(O)$, but it is *one of possibly several* such covers.
  - The compatible set is then the union, over the admissible $\tilde M$, of the quotients $\tilde M/\Gamma$. Whether covers and quotients of inextendible hosts are inextendible (#320) is (U); the batch also marks it unchecked.
- **Conditions on $\Gamma$.** $\Gamma$ must act freely and properly discontinuously and preserve time orientation. "No timelike elements" is not enough to avoid closed timelike curves: the condition is that no $\gamma\ne1$ maps some $x$ into $I^+(x)$ (or $J^+$, to exclude closed causal curves).
- **Identical states along the path: confirmed.** The projection is a local isometry and continuation along one path is unique (`papers/geodesic-lifts.md` Prop 3.2, Cor 3.1 and "Multiplicity of $E(O)$ is locally invisible"; `papers/patch-edge.md` Prop 7.2).
- **Lensing: confirmed, with one correction to the reasoning.**
  - The observer's past cone in $\tilde M/\Gamma$ is the projection of its past cone in $\tilde M$. In $\tilde M$, multiple images already come from conjugate points and caustics. In the quotient, the extra images come from deck elements, and those *differ between quotients*.
  - So the images do differ across hosts. They fail to split the compatible set only because images are not part of the observer state, which is local. A record would make them count, which is exactly Set 2.
  - "Images are periodic copies in $\tilde M$" is true but tautological: $\Gamma\subset\mathrm{Isom}(\tilde M)$.

## (2) L27: symmetry bound

- **The bound is right.** $\pi_1(M)\cong\Gamma\le\mathrm{Isom}(\tilde M)$, acting as in (1).
- **"Generic" is ill-posed as written.** No topology on germs or on $V$ is adopted (T0–T4 deferred). In a fixed smooth or analytic topology on metrics over a fixed manifold, a trivial isometry group is open and dense. For Riemannian metrics on compact manifolds this is the standard slice-theorem result (Ebin 1970 (U)). That is a topological statement. Reading it as "almost every" would smuggle in a measure (#336 (a)).
- **Countable versus continuum:**
  - *Closed hyperbolic spatial sections, dimension $\ge3$.* For example $\mathbb R\times H^3/\Gamma$, static, or open FLRW with $\Gamma$ cocompact. Here $\mathrm{Isom}(\tilde M)\supseteq\mathrm{Isom}(H^3)$, and the quotients are **countable**: there are countably many such groups, and Mostow rigidity (Mostow 1968 (U); finite-volume case Prasad 1973 (U)) gives no continuous moduli for a fixed topology.
  - *Infinite-volume hyperbolic quotients* (Schottky, quasi-Fuchsian $\Gamma$): a **continuum** of deformations (U). So countability requires restricting to closed or finite-volume quotients, which is a choice.
  - *2+1 or $H^2$ sections:* Teichmüller space, a continuum (U).
  - *Flat* (tori, Misner-type boosts in Minkowski): a continuum.
  - *AdS$_3$ quotients (BTZ):* continuous mass and spin, a continuum (U).
  - *de Sitter quotients:* not checked.
  - So the rigid, countable case applies only to spacetimes whose $\tilde M$ has hyperbolic spatial sections of dimension $\ge3$ and whose admissible $\Gamma$ are cocompact on those sections.
- **The cover may not be unique.** Per (1), the list is a union over admissible $\tilde M$. Inequivalent extensions add hosts that differ in more than $\Gamma$.

## (3) L28: the ant meets its own trail

- **Genuine, not a nested prefix: confirmed in the record-augmented state.** Two compatible quotients give different records at a return time, so the states (germ plus record) differ afterwards and no host ends early.
  - Within one host the record is determined, so nothing branches in motion. This is **which-world revealed by observation** (Bayesian narrowing of $E(O)$), as the batch's weak point 3 says.
  - The object is a refinement of a partition of the ensemble over time, not the branch sets $B_R$ of v0.10.1 §8.2 (not edited here).
- **Return times.**
  - For a fixed host, proper discontinuity should make the set of return times locally finite, giving discrete splits. That is plausible but (U) as a general statement.
  - Across hosts in the flat case, return times and directions vary continuously (continuum).
  - At each time the observation class is the set of deck elements that have arrived. Over countably many $\Gamma$ that gives **countably many** classes, not necessarily finitely many. The batch's "finite partition" is too strong.
  - Return is not guaranteed. It needs the conformal time elapsed to exceed the relevant loop length. With accelerated expansion (horizons), a self-signal may never return (U). The batch also flags this.
- **Costs.**
  1. The record makes the state non-local. That changes the definition (state = germ plus $u$), and the gauge quotient (#324) must be extended to act on records.
  2. Emitting or scattering needs a body. The framework's observer is a germ with no mass or charge, so the test field needs a source the record does not supply.
  3. The (M1) arm count against "count worlds" is David's call, as the batch notes. Nothing here weighs in on it.

## (4) Dropped items

- **Lensing of the geometry:** correctly dropped. Per (1), it is killed by the locality of the state, not by periodicity.
- **"State includes the whole causal past of the geometry":** correctly dropped *as geometry*. If the causal past is taken with its identifications (the past cone self-intersects in the quotient), it is Set 2 in disguise and not nothing.
- **Non-analytic quotients:** correctly dropped as a continuum. Note that analytic flat quotients are a continuum too.

**Citations.** (V): Chruściel–Isenberg 1993 (#332). (U): Ebin 1970; Mostow 1968; Prasad 1973; Teichmüller, quasi-Fuchsian and BTZ moduli; local finiteness of return times; the horizon caveat. In-repo: geodesic-lifts, patch-edge, #320, #324, #336, #346.
