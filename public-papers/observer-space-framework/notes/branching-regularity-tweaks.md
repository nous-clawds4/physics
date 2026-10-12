# Branching from a one-word regularity tweak: three candidates (proposal note, do not merge)

**Status.** Proposal only. Nothing here is adopted, and nothing recommends adoption. No `versions/` draft (v0.9.1, v0.10, v0.10.1) is touched. Topology T0–T4, the throat convention, the law of $R$, (M1) and (A) are not revisited. Written for David's request of 2026-10-12 ("mostly deterministic" motion: deterministic along stretches, with discrete branch points, without CTCs, obtained by changing the meaning of one word of the framework).

**Read at:** main `2b215ec`: `notes/born-litmus-test.md` (LT1–LT4, quoted below), `papers/piecewise-geodesic-Ck-graph.md` (Option F, 2026-09-07, and its v0.6 banner), `papers/geodesic-lifts.md` (Prop 3.2, Thm 3), `notes/inextendible-ensemble.md` (#320), gauge-quotient note (#324).

## 0. The baseline and why it does not branch

The observer state $O$ is the infinite jet at $p$ of a real-analytic Lorentzian metric, plus a future unit timelike $u$; equivalently the germ, and the simply connected analytic patch $P(O)$. The curvelet $\gamma_O$ is the unique geodesic lift (geodesic-lifts Prop 3.2, Thm 3). Analytic continuation along a single path has no monodromy, so free fall on $V$ is deterministic. Type-(ii) jumps supply alternatives only by postulate.

The template is the EKT billiard ball (Echeverria, Klinkhammer, Thorne, *Phys. Rev. D* 44, 1077 (1991)). There local dynamics is deterministic and the multiplicity comes from a global consistency condition that has more than one solution. The question is whether a weakened regularity word can reproduce that pattern without closed timelike curves.

## 1. The test (verbatim, `notes/born-litmus-test.md`, L3)

- **LT1 Identity:** the squared quantity is the same object that does amplitude work elsewhere in the theory (it superposes, evolves linearly, interferes); if it appears only in the counting step, the square is a coincidence of form.
- **LT2 Prior inputs:** the law of R, the slice and the measure are fixed for independent reasons, ideally within a class named in advance, not tuned until |psi|^2 appears.
- **LT3 Robustness:** the result survives refining the grain, changing the cut, and irrelevant further splitting.
- **LT4 Novel prediction:** it gives correct weights in a second, unrelated setup, or interference that was not put in.

None of the candidates makes a Born-type claim, so under "Pre-emptive use" each LT records only whether there is anything to check yet and what a later claim would have to show. The test cannot be passed here; it can only be failed by an injection, and none is found below. Two extra filters come from David's well-posedness principle (every term defined) and his taste criteria (small, independently motivated, smuggles no count or measure).

## 2. Candidate A: "analytic" becomes "analytic off a thin branch set"

**Definition change.** A host is a pair $(M,\Sigma)$, where $\Sigma\subset M$ is a closed embedded codimension-2 submanifold, $g$ is real-analytic on $M\setminus\Sigma$, and near $\Sigma$ the metric is locally a finite branched cover of an analytic metric, with cone angle $2\pi n$ ($n\ge 2$), or a conical defect $2\pi(1-\delta)$ (the cosmic-string metric; Vilenkin, *Phys. Rev. D* 23, 852 (1981)). States stay germs at points $p\notin\Sigma$.

**What branches.** Continuation of the germ along loops in $M\setminus\Sigma$ now has monodromy, valued in a permutation group of the sheets for branched covers, or in rotations/holonomy for a conical defect. A curvelet that meets $\Sigma$ has no unique continuation: geodesics hitting a cone vertex or a branch locus are not determined by the ODE, and the outgoing directions form a set. That set is discrete (the $n$ sheets) for a branched cover; for a conical defect it is a **continuum** (every outgoing direction in the normal plane is a candidate), unless a rule picks one.

**Discreteness and LT2.** The sheet number $n$ is a topological integer, fixed by the host, and not tuned. That is the attractive part. But whether $\Sigma$ exists and where it sits is a choice of host, exactly like $\pi_1$ was a choice of $M$ in the ant discussion; the geometry does not force $\Sigma$. Hitting a codimension-2 set is non-generic: a generic timelike geodesic misses it, so branching would be measure-zero along curvelets unless something attracts orbits to $\Sigma$. Branching off near-misses is not available without a new rule.

**Ill-posed terms.** "Branch locus of a Lorentzian metric" must be specified: timelike, spacelike or null $\Sigma$ (the cosmic string is timelike, and its world-sheet is the spacetime branch locus); what Einstein equations mean on $\Sigma$ (distributional curvature, a delta source, so the analytic vacuum record gets a source term); and what the germ "at" $\Sigma$ is (undefined; points of $\Sigma$ are not states). "Which sheet" after the hit is undefined without a law of $R$, which reintroduces the open question it was meant to replace.

**Cost and measure.** Adds a singular source and a hit-rule. It smuggles no measure by itself; equal weight over $n$ sheets would be an added count (LT2 would then have to be argued). LT1: nothing amplitude-like yet; monodromy representations do superpose linearly on functions over the cover, which is the only hook a later LT1 claim could use. LT3: $n$ is topological, so refinement-robust, a good sign if a claim is ever made. LT4: nothing to check.

## 3. Candidate B: "smooth" becomes "analytic pieces with $C^k$ junctions" (Option F)

**Definition change.** As adopted in-house 2026-09-07 (working, abandonable): analytic-geodesic pieces, finite-order $C^k$ matching at vertices, plus graph incidence (Option E).

**What branches.** Non-unique continuation at a vertex: any analytic piece whose $k$-jet agrees with the incoming one is admissible.

**The record already answers this.** The v0.6 banner of `papers/piecewise-geodesic-Ck-graph.md` (Claude #128 row 3): "Finite $k$ is not the HOLE escape. Truncated-jet matching is vacuous at $k=1$ between distinct lumps, prohibitive at $k\ge2$ for curvature-changing jumps, and cannot create a branching edge." The working reading reverted to the Option E residue, i.e. type-(ii) jumps plus graph incidence. So the branching in B comes from graph incidence, which is the postulate David now finds physically senseless, not from the regularity tweak.

**Discreteness and LT2.** Discreteness is put in by the graph, so it is not fixed for independent geometric reasons; vertices are chosen. $C^k$ matching gives a continuum of continuations (any analytic tail with that $k$-jet), so without the graph the alternatives are uncountable. **Ill-posed:** "vertex" has no geometric definition; "$C^k$ at a join between distinct lumps" is the menu left to Ontology. **Measure:** none smuggled; a count over out-stars would be an added count. LT1, LT4: nothing to check. LT3: the deferred $k\to\infty$ and edge-length limits are exactly the robustness questions, and at $k=\infty$ the CWS singleton returns (one continuation).

## 4. Candidate C: "analytic" becomes "Gevrey of order $s>1$"

**Definition change.** Replace real-analytic ($s=1$: $|\partial^\alpha g|\le C R^{|\alpha|}\alpha!$) by Gevrey $G^s$ ($|\partial^\alpha g|\le CR^{|\alpha|}(\alpha!)^s$, $s>1$). By the Denjoy–Carleman theorem (Hörmander, *The Analysis of Linear Partial Differential Operators I*, §1.3) a class is quasianalytic (a function with zero jet at one point vanishes identically) iff $\sum M_{k-1}/M_k=\infty$; analytic classes and other quasianalytic classes keep "jet determines germ", so they give nothing new. $G^s$ with $s>1$ is non-quasianalytic: it contains compactly supported bump functions, so two metrics can agree on an open set and differ elsewhere.

**What changes in the framework.** The jet at $p$ no longer determines the germ, let alone the patch. "Observer = infinite jet" and "observer = germ" stop being equivalent, and the record must pick one. $P(O)$ as "the unique analytic patch" is undefined.

**What branches, and well-posedness.** The geodesic equation is an ODE with Lipschitz coefficients, so given the metric the curvelet is still unique; branching is not in the motion law. Branching is in the host: the vacuum Einstein equations in harmonic gauge are a hyperbolic system that is well-posed for smooth data with finite propagation speed, and Gevrey regularity is a natural class for hyperbolic Cauchy problems (Colombini, De Giorgi, Spagnolo, *Ann. Sc. Norm. Sup. Pisa* (4) 6, 511–559 (1979); Colombini, Jannelli, Spagnolo, *ibid.* (4) 10, 291–312 (1983)). Hence a Gevrey Cauchy datum can be altered by a Gevrey bump outside any given region, and the two developments agree on that region's domain of dependence and differ beyond its Cauchy horizon. That is a genuine "agree on a stretch, then diverge" structure, and the divergence is caused by data, which is EKT-like in spirit (global, not local). (I have not verified a specific theorem stating Gevrey well-posedness of the Einstein equations themselves; the claim above rests on the smooth well-posedness of harmonic-gauge Einstein and should be checked by Literature before anything leans on it.)

**Discreteness and LT2.** This is the weak point: the alternatives form an infinite-dimensional continuum (any bump, anywhere, any size), and the divergence surface is any Cauchy horizon, so there are no preferred branch points. This is the "anything goes" extreme, not the middle. Discreteness would need an extra rule (e.g. branching only where a bump is forced by a constraint), and that rule would carry the LT2 burden. The order $s$ is itself a free parameter with no independent reason to pick a value.

**Ill-posed terms.** "The germ of $O$" (if the state is the jet), "the patch $P(O)$", and "the ensemble $E(O)$" all need redefinition; inextendibility (#320) must be stated within $G^s$. The gauge quotient (#324) must use $G^s$ diffeomorphism germs, whose jets also fail to determine them. **Measure:** none smuggled, but there is no natural measure on the bump space either. LT1/LT3/LT4: nothing to check.

## 5. Comparison

| | A: branch set | B: $C^k$ junctions | C: Gevrey $s>1$ |
|---|---|---|---|
| Word changed | analytic → analytic off codim-2 $\Sigma$ | smooth → piecewise analytic, $C^k$ joins | analytic → $G^s$ |
| Motion law still deterministic off branch points | yes | yes | yes (branching is in host data) |
| Branching discrete by geometry | yes for branched covers ($n$ sheets); no for conical defects | no; discreteness from the graph | no; continuum |
| Branch points fixed independently (LT2) | sheet number yes; locus is a host choice; non-generic hits | no (vertices chosen) | no |
| New undefined terms | $\Sigma$'s causal type, field equations on $\Sigma$, sheet rule | vertex, join law | jet vs germ, $P(O)$, $E(O)$ |
| Measure smuggled | no | no | no |
| Already ruled on | no | yes, v0.6 banner: cannot create a branching edge | no |

**Neutral reading.** A is the only one where the discreteness comes from a topological integer and not from fiat; its open costs are the singular source, the non-genericity of hits and the sheet-selection rule. B's branching is the Option E graph and not the tweak, per the record. C gives exactly the "agree then diverge" shape but sits at the continuum extreme unless a discreteness rule is added. None is recommended for adoption; which, if any, to pursue is David's call.
