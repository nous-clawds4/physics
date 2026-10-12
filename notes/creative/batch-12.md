# Creative batch 12: germ divergence beyond the Cauchy horizon as the branching (Creative Lead; proposal, do not merge)

**Status.** Exploration only, under David's 3:14 PM ruling, his 3:53 PM working assumptions, his 4:16 PM approval of relaxing #352 for geon hosts, and his 4:17 PM central hypothesis. Structure only: no probabilities. Nothing goes into `versions/` or `papers/`. Citations are **unchecked** unless verified in #362, #364 or #365. Everything is a sketch.

**Framing (Physics Lead, positive).** A germ that diverges beyond the observer's Cauchy horizon *is* the branching sought since L26: branches with different states, tied to different worlds.

## For David (one minute)

The good news first: when the observer's signal comes back from the particle's time-loop, it can only do so past a "horizon" beyond which the past no longer fixes the future. Past that horizon, different possible worlds give the observer genuinely different states, which is the kind of branching we have wanted all along. We checked three things. **First, does the observer survive in every branch?** In the textbook examples (Misner and Taub–NUT spaces), no. Each possible continuation lets some observers through and ends the others, so in some branches the observer simply stops. Surviving in every branch needs the worlds to differ away from the observer's own path, and that brings back the "infinitely many smoothly varying options" problem. **Second, is the measurement result the same thing as the branch?** Not automatically. The result can be coarser than the branch (several branches show the same reply), or finer (the same world with different replies, if the replies differ only in what the signal did and not in the geometry). They match only when each reply picks out exactly one world. **Third, are the branches countable?** For the billiard-ball-type solutions, probably yes, generically: each "number of trips through the loop" gives a few isolated solutions. But a perfectly symmetric particle smears each solution into a continuous family, and symmetry is exactly what the handle story needed earlier.

---

## (1) When does the observer survive?

**Setting.** Observer $\gamma$ in a globally hyperbolic region $D^+(S)$ whose Cauchy horizon $H^+(S)$ is compact, e.g. the geon's chronology horizon. By #364 (d), replies arrive only beyond $H^+(S)$, so the question is whether $\gamma$ continues across $H^+(S)$ in each maximal extension.

**Misner space (2D sketch; Misner 1967; Hawking–Ellis §5.8; unchecked).**
- Misner space is the quotient of the region $t^2-x^2>0$ of $\mathbb R^{1,1}$ by a boost. It has two inequivalent analytic extensions across the compact null horizon.
- **In each extension, one family of incomplete geodesics is completed and the other is not**: those winding one way around the horizon cross in extension I, those winding the other way cross in extension II. The union of both is non-Hausdorff.
- Geodesics through the boost's fixed point (the "comoving" ones) are incomplete in both.
- **Consequence.** A generic observer crosses in **exactly one** of the two extensions and **ends** in the other. No observer survives in both.

**Taub–NUT (sketch; Chruściel–Isenberg 1993, V-text per #332; unchecked as stated for observers).** Taub–NUT has the same structure: the inequivalent extensions complete different families of geodesics.

**Conditions for survival in every extension (sketch).**
- (i) **The extensions agree along $\gamma$'s continuation.** They differ only off the observer's path. In the analytic case this is impossible across the horizon, because the germ at the crossing fixes the extension locally (Theorem A), so differing extensions give differing germs or no crossing. In the $C^\infty$ case it is possible: the extensions differ by data placed away from $\gamma$. But then they are a **continuum** (bumps; #334, batch 05).
- (ii) **$\gamma$ stays off the horizon generators** and crosses the horizon transversally in every extension. For compact horizons of Misner/Taub type, (ii) fails as shown: crossing is extension-dependent.

**Answer (1).** In the analytic examples the observer survives in **some** extensions and ends in others. That is the nested-prefix pattern again, alongside a genuine split among the extensions in which it survives. Survival in all extensions needs non-analytic extensions that differ off-path, which gives a continuum. So the positive reading holds **among surviving branches**, and dropout (ending) is a separate outcome. That is consistent with v0.10.1 §6.2, "dying is not an arm".

## (2) Does germ divergence coincide with the returned record?

**Analytic hosts (sketch).**
- Beyond $H^+(S)$, the germ at $\gamma(s)$ fixes the local extension (Theorem A).
- The reply at $s$ is determined by the host. If the reply's causal past lies inside that patch, the germ also determines the reply.
- So the **record partition is a coarsening of the germ partition**: same germ means same reply, but different germs can give the same reply.

**Ways they come apart.**
- (a) **Branch without outcome.** The germs diverge, but no Type O reply distinguishes them: only Type F returns, or none (#364 (b): no Type O for $\pi_1=\mathbb Z/2$).
- (b) **Outcome without branch.** On a fixed geometry, EKT-type solutions differ only in the signal's or ball's history (batch 11 reading (a)). The record differs, the germ does not, so the outcome is in-host and not branch A = world A.
- (c) **Coarser outcome.** Several extensions return the same reply.

**Answer (2).** Outcome and branch coincide exactly when (i) the world includes the content, or the solutions back-react on the geometry (batch 11 readings (b) and (c)), **and** (ii) the reply map from branches to records is injective. Neither condition is automatic.

## (3) Are EKT's infinitely many solutions countable or a continuum?

- **Literature (#365, V-text abstract).** EKT find infinitely many self-consistent trajectories for the same initial data across a wide class of "dangerous" trajectories. A ball at rest far from the wormhole has exactly one.
- **Structure (sketch).** For fixed initial data, a self-consistent solution is a fixed point $F(x)=x$ of the round-trip map on the finite-dimensional data of the ball's trajectory where it enters the wormhole.
  - Solutions fall into classes by the **number of wormhole traversals** (or collisions) $n$, a discrete label (as I recall the EKT and Lossev–Novikov solutions; unchecked).
  - Within a class, for generic smooth $F$, fixed points are **isolated** (transversality, standard), so finitely many in each compact region.
  - So generically: **countably many** solutions in total (sketch).
- **Continuum trap: symmetry.**
  - If the wormhole or geon is symmetric, e.g. rotationally symmetric mouths, then rotating a solution about the symmetry axis gives another solution, so each isolated solution becomes a **continuous family**, unless the initial data break the symmetry.
  - Hosts with exact symmetry are exactly what L27 needed for nontrivial $\pi_1$.
  - **Tension:** the symmetry that makes handles possible under analyticity tends to make the solution set a continuum.
- **Also:**
  - Finite-size, spinning or inelastic balls add continuous internal parameters. Whether these are fixed by consistency is unchecked.
  - Test fields probably give a single solution (Friedman & Morris, V-text/V-meta per #365) and add no multiplicity.

**Answer (3).** Countable generically, by discrete traversal classes with isolated solutions in each. A continuum appears under symmetry or with continuous internal degrees of freedom. The continuum trap is live for the symmetric hosts the π₁ story favoured.

---

## Ledger rows

- **L38** (survival)
- **L39** (outcome vs branch)
- **L40** (EKT countability)

## Weak points

1. The Misner and Taub–NUT geodesic dichotomy is from memory (Hawking–Ellis), and its application to timelike observers is unchecked.
2. "The germ determines the reply" assumes the reply's causal past lies in the analytic patch.
3. EKT's discrete traversal classes and isolated solutions are a sketch from memory. Generic transversality may fail in the actual EKT map.
4. The symmetry-versus-countability tension is unresolved.
5. Survival in every extension needs a $C^\infty$ off-path difference, which is a continuum.
6. Dropout (ending) must not be counted as an arm (v0.10.1 §6.2).
7. The non-Hausdorff union of extensions resembles branching spacetimes (Belnap; McCabe; #332 N1). That is an Everett framing hazard; it is flagged, not used.
