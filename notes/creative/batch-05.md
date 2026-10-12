# Creative batch 05 (Creative Lead; proposal, do not merge)

**Status.** Proposal only, exploration only, under David's 3:14 PM ET ruling (relayed, not signed). Nothing goes into `versions/` or `papers/`. Hypotheses H1–H5: `batch-03.md`. Citations are **unchecked** unless marked "verified per #342" or "verified in #332".

**Target (David's reframing, 2026-10-12 3:19 PM ET, relayed via Physics Lead, not signed; recorded in the ledger).** Free fall is deterministic inside each world. Branching in observer space comes only from which world we are in: branch A *is* world A. So the target is **not** a fork inside one host. It is a set of hosts that all agree on the observer's current state $O$ but give different later states along $\gamma_O$, and that set must be discrete or countable, not a continuum. Under analyticity this is impossible: the germ fixes $P(O)$ and the whole path (Prop 3.2), so every compatible host gives the same sequence. We want the weakest independently motivated relaxation, probably of analyticity, that allows it. Earlier rules kept: an independent reason; name the H broken; no law of $R$ by fiat; no sneaked-in measure.

**Reframing note on batches 01–04.** Several earlier "failures" ("this is just which host we're in", #332 R2, #336, #338) are now the *intended* mechanism. What still matters from those records is the count: a continuum (#334, #342 R2) still fails.

## Structural observation (Creative Lead sketch; for Geometry to check)

Where can two compatible hosts first differ along $\gamma_O$?
- If they agree on an open set $U\ni p$, well-posedness of the vacuum Einstein equations (Choquet-Bruhat–Geroch 1969, verified in #332) makes them agree on the domain of dependence of any spacelike slice inside $U$.
- They can first differ only where $\gamma_O$ leaves that domain of dependence, i.e. crosses its (null) boundary. What the observer meets there is data from outside its shared past: "news".
- So the question reduces to: **what class of incoming data is allowed?**
  - Analytic: none (the germ fixes everything).
  - Quasianalytic: none (the jet fixes the germ; #331 §4).
  - $C^\infty$ or Gevrey: any bump, which is a continuum (L8, #334).
  - A countable outcome needs a countable class of allowed data, for an independent reason.

This also matches the charter's theme "We need local state to tell us something about global state, but not everything." (Unchecked as a theorem: it assumes the hosts' agreement region contains a slice with $p$ in its interior development, and that $C^\infty$ uniqueness holds there; spacelike and timelike hypersurfaces are covered by Cauchy uniqueness and unique continuation (unchecked) respectively, so the divergence sits on null hypersurfaces.)

## Set 1: "Worlds of finite description" (L20)

**In a minute.** David wants several possible worlds that look exactly the same to the observer now but give it different futures, with only a countable number of them. In perfectly smooth (analytic) worlds that can't happen, because the present fixes everything. In merely smooth worlds it happens too much: a smooth spread of infinitely many futures. The middle ground is worlds stitched together from perfectly smooth pieces, where each piece and each seam can be written down with a finite description (like a formula with whole-number or algebraic constants). Two such worlds can agree everywhere the observer can see and then differ when news arrives from outside, across a lightlike seam. Because finite descriptions can be listed one by one, the possible futures are countable, not a continuum. The catch: it is not yet clear that "finite description" is a physical reason rather than a mathematician's one. The countable set is also dense, and so close to a continuum that it may not satisfy the spirit of the rule.

**Tweak.** "analytic host" → "piecewise-analytic $C^{1,1}$ host whose pieces and junctions are finitely definable" (for example semialgebraic or analytic-with-algebraic-data; which class is open).
**Breaks.** H1 (the germ fixes $P(O)$ only up to the first junction) and H5 (the lifts are piecewise analytic, so Cor 3.1's analytic-split argument stops at a junction). Within each piece, Prop 3.2 holds: free fall stays deterministic in each world, as the target asks.
**Why junctions are null, not chosen.** By the structural observation, across spacelike or timelike hypersurfaces the other side is fixed anyway. Only null (characteristic) junctions carry free data, as in impulsive waves (Penrose cut-and-paste, unchecked). So the divergence locus follows from the equations, not from a choice.
**Avoiding the recorded objections.**
- Continuum (#334, #342 R2): the class is countable by construction.
- Law of $R$ by fiat (#341, #344): no rule selects a future; the alternatives are whole hosts, which is the target.
- Atypical hits (#336): the observer crosses the null boundary of its shared domain of dependence whenever news arrives, so no aiming is needed. This needs checking for vacuum hosts.
- Borrowed quantisation (#339): none.
- Measure: none. A countably infinite set carries no uniform countably additive measure (Paper 1 §6), so any later weighting is a separate, named step.

**Taste.** TT1: the class must be named, and "finitely definable" needs a precise logic or field; with $C^{1,1}$ matching, the junction conditions must be consistent with vacuum Einstein (unchecked). TT2: **main risk.** The reason ("physical worlds have finite descriptions") is not yet physics, and the choice of class is a grain. TT3: small: a piecewise version of the existing word "analytic". TT4: no measure; but the set is countable *and dense*, and that should be judged against David's "between determinism and chaos".
**Check for Geometry.** (a) Is the structural observation right, i.e. is divergence only on the null boundary? (b) Do countably many finitely-definable vacuum continuations across a null junction exist, beyond the trivial one?

## Candidates checked and dropped

| # | Candidate | Breaks | Fails | Why |
|---|---|---|---|---|
| E1 | $C^\infty$ / Gevrey hosts (L5, L8 recycled) | H1, H5 | continuum | Any bump in the incoming data gives a different host (#332, #334). |
| E2 | Quasianalytic non-analytic classes (L6) | none effective | no divergence | The jet still fixes the germ (Denjoy–Carleman; #331 §4). |
| E3 | Agreement to order $k$, then $k\to\infty$ | H1 | continuum / no divergence | Each finite $k$ leaves a continuum; the limit returns analytic uniqueness. |
| E4 | Topology-only differences, with rigid countable families (e.g. hyperbolic quotients; Mostow rigidity, unchecked) | none | no divergence | Countable, but locally invisible along the path: the germ along $\gamma_O$ is the same (`papers/geodesic-lifts.md` Cor 3.1 discussion; `papers/patch-edge.md` Prop 7.2). |
| E5 | Scale hierarchy: identical at human scale, different microscopically | H1 | continuum, measure | The microstructure is a continuum; coarse-graining it needs weights (#339). |
| E6 | Global regularity selecting a discrete family (e.g. Bartnik–McKinnon-type discrete solitons, unchecked) | — | no shared $O$ | Distinct analytic solutions have distinct germs, so they do not agree on $O$; gluing them returns to E1. |
| E7 | Piecewise-analytic hosts with junctions in an *unrestricted* class | H1, H5 | continuum | Impulsive-wave profiles are free functions. Set 1 is this candidate restricted to a countable class. |
| E8 | Batch-05 draft ideas from before the redirect: smooth ODE bifurcations, caustics, Morse critical surfaces, threshold memory | — | off-target | They aim at a fork inside one host. Also, a smooth ODE with a pitchfork or saddle-node stays deterministic: solutions are unique, the bifurcation is in parameter space, and "choices" come from initial data below resolution. That is sensitivity, not non-uniqueness. |

## Lesson (L22)

Under David's reframing, the question "how does the motion branch?" becomes "what class of data may arrive from outside the observer's shared past?" Analytic and quasianalytic classes give no branching; $C^\infty$ and Gevrey give a continuum. A discrete or countable branching needs a countable data class with a physical reason, and that reason is the open problem.
