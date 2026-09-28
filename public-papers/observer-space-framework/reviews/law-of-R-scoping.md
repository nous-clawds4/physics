**SCOPING ONLY, NOT A CLAIM.**

# Law of $R$: what is already constrained, what survives, and one cheap test

Author: Geometry (§L: Literature)
Date: 2026-09-28
Question (Physics Lead, approved by CoS): what the 16 named instances, the toys and the named-leftover theorems already impose on any law of $R$; which candidate families the repo already names survive; and one cheap computation that would separate two survivors.

Scope and rules:
- This is an inventory. No law of $R$ is adopted or endorsed, and no new leftover theorem is proved.
- No paper, essay or Paper 1 edits. No (M1)/(M2) pick. No choice among v0.7.1's open calls T1–T3.
- No Born rule, no $|a|^2$ and no $1/N$ by hand.
- David's open questions (Q-D1–Q-D5, `public-essays/mathematical-foundations/reviews/v0.1-ontology.md`; #139 (a)–(e)) are cited only as existing.
- Where a classifier matters, the corrected one is used (`c33r.py`; #169, #174).

**Answer.** The repo already fixes a good deal about any law of $R$, but almost all of it is negative or conditional:
- $R$ is extra (Prop. 13, Thm 19).
- A lock-side readout gives a singleton or a continuum unless a grain is added (Thms 17, 18, 24–30).
- Under (a), cross-continuation edges are excluded (C1).
- Any $R$ must meet (J1) or (J2) if typical histories are to look geodesic (C17).

Two families have worked instances: the Kretschmann rule as stated, and its (a)-restriction. Only the (a)-restriction meets the constraints the rule as stated fails, (a) and a late-window (J1). The other named families are either properties a law may have (measurable, closed-graph and so on) or add-ons that need a grain (least-action support, integer bins). None is motivated in the sense of the public gate (v0.7.1 §5.4).

The cheap test (§3) asks whether the "short jumps" reading of the (a)-restricted Kretschmann family is a separate survivor from its "transient" reading. It was run (about 70 s) as an exploratory readout, not preregistered (the criterion was fixed after the per-jump readout was in hand): on the grid it **does not separate** them. Shrinking the scale $c$ shrinks each jump in proportion to $c$, but the expected number of jumps grows in inverse proportion. The orbit's net displacement when the jumps end stays at about 9–11 radial units for every $c$ on the grid.

---

## 1. Constraints already in the repo

Status labels:
- **proved**: a theorem or proof in the repo;
- **pinned**: checked numerically on a named instance;
- **convention**: a definitional choice or named clause, revisable.

"Extra" means the repo has shown that the item is not supplied by the lock, so any law must bring it.

### 1.1 From the 16 named instances

"The 16 named instances" are the rows of Claude Opus 5.5's #154 §1 (`reviews/v0.6-prose-claude-opus-5.5.md`), all recomputed or re-read in `reviews/v0.6-claude-154-geometry.md` §4. Row numbers below are those; C-numbers are v0.7.1's Appendix A.

| # | Constraint on any law of $R$ | Source | Status |
|---|---|---|---|
| I1 | Under (a), no edge crosses analytic-continuation classes; e.g. Schwarzschild $M=1\to M=2$ is excluded (lump invariants $K$, $\lvert\nabla K\rvert^2$ recover $(M,r)$) | row 1, C1 | proved (analytic rigidity), pinned |
| I2 | An (a)-edge must leave along $u''\ne u$ (leaving along $u$ is type (i), so $R=\emptyset$); curvature-changing edges within a class are allowed | row 2, C2–C3 | proved (definition), pinned |
| I3 | The Kretschmann outward edges fail (a) and the inward edges pass; under (a) the worked rule keeps $\lvert B_R\rvert=2$ but its branching is transient and completed histories are countable | rows 3–4, C30, C31, C33 | pinned (exact; corrected classifier) |
| I4 | With arrival rule (A), the arm set depends on how a germ was reached, so an $R$ used with EPP1 gives a process Markov on $(O^u,a)$, not on $O^u$ | row 5, C6 | pinned; (A) is a convention (working postulate) |
| I5 | No-Zeno is not implied by the slice: it holds on bound Schwarzschild but fails on an oscillating FLRW, so a law of $R$ needs a named no-Zeno clause or a per-instance check | rows 6–7, C7, C8 | pinned; the clause is a convention |
| I6 | Stars and arm counts are physical only modulo germ isotropy (3 versus 2 on the flat lump) | row 8, C9 | convention, pinned |
| I7 | On locally symmetric lumps (Minkowski, dS, ESU, Cahen–Wallach), every lock-side scalar is constant along curvelets. A slice-sourced $R$ therefore has no source there, and type (ii) is visible only in oriented observer space | row 9, C10, C19, C32 | proved (Killing, transvections), pinned |
| I8 | The degree pattern of $R$'s tree decides whether (M1) and (M2) agree: they agree on a cut iff $D$ is constant on it, and proper-time cuts can disagree even on generation-regular trees | row 10, C12–C14 | proved (iff), pinned (exact) |
| I9 | Depth counts converge to per-vertex weights iff siblings are asymptotically balanced | row 11, C15 | proved/pinned |
| I10 | Without (a), a rule with two jump options on an invariant window has a continuum of completed histories | row 12, C16 | proved |
| I11 | The example $K$-slice is empty on flat ΛCDM, and the choice of scalar matters. A slice-sourced $R$ can have no source on standard backgrounds | row 13, C18, C23 | proved (sympy) |
| I12 | For a freely falling near-flat lab, $K$-vertices are exactly its radial turning points, so a $K$-sourced $R$ branches only at the lab's own turning points | row 14, C38 | proved (formula) |
| I13 | No jump dominance: under EPP1 the pure-geodesic history has weight $(1+m)^{-n}$, so any $R$ must meet (J1) sparse vertices or (J2) observationally null jumps. The rule as stated fails both | row 15, C17, C34 | arithmetic proved; the aim ("typical histories look geodesic") is a stated target; pinned (sampled) |
| — | Row 16 (SHPMP 2008 pedigree) is a text check. It constrains the measure's pedigree, not $R$ | row 16 | none on $R$ |

### 1.2 From the toys and the later instances

| # | Constraint | Source | Status |
|---|---|---|---|
| K1 | Vertex times selected by the ensemble ("where some compatible world ends") form a continuum, even with inextendibility. $R$'s source set must come from a lock-side slice or an explicit discrete sub-ensemble (a grain on $E_W$) | V\*/Option F, C24, C25 | proved |
| K2 | The slice is codimension one, discrete only per curvelet. Which scalar, and critical point versus level, is a free choice (Bertrand over (slice, rule) pairs) | C21, C22, §5.1 | proved (C21); the choice is a convention |
| K3 | Finite-jet matching cannot create an edge: vacuous at $k=1$, prohibitive at $k\ge2$ | C27 | proved |
| K4 | $\lvert B\rvert\ge2$ is a digraph fact. The toy's two arms differ in lock-side invariants ($K=0$ versus $80/27$), so no germ symmetry swaps them; any equal weighting is postulated | `papers/B-ge2-minimal-toy.md`, #159 P8 | pinned (symbolic) |
| K5 | Arms are $B_R=\{[\gamma]\}\cup\mathrm{succ}_R$, with first-edge equivalence; dying is not an arm | C11, §4.2, §5.2 | convention |
| K6 | The Zeno-mass convention changes weights (undefined, $1/2$ or $1$) | C35 | pinned; the choice is open |
| K7 | A path-counting (M2) on a finite graph carries the MERW hazard | C36 | pinned (a hazard, not a constraint on $R$) |
| K8 | A rule whose jump path can meet the bifurcation sphere needs a throat convention (a case clause if "undefined") | C37 | pinned |
| K9 | Public gate: stated, uniform (no finite case list) and motivated. Motivation must select the rule, up to named constants, within an independently named class of uniform rules, or state an empirical target; covariance does not count | C26, §5.4 | convention (the bar in force) |

### 1.3 From the named-leftover theorems (`papers/`)

| # | Constraint | Source | Status |
|---|---|---|---|
| L1 | Locked data at $O$ determine no type-(ii) edge; a law of $R$ is extra | Prop. 13 (`type-ii-adopted.md`) | proved |
| L2 | The named lock-side functors (data at $O$, open neighbourhoods, continuous $f:\mathrm{Obs}\to\mathbb R^n$) supply no nonempty countable typicality set of delayed forks. This is not a blanket "no map" | Thm 19 (`law-of-r.md`) | proved (scoped) |
| L3 | Singleton or continuum. Neighbourhoods minus $\gamma_O$ are uncountable; finitely many continuous invariants on a connected open give one class or a continuum. A countable star needs a grain | Thms 17, 18 (`neighborhood-uncountable.md`, `grain-not-from-invariants.md`) | proved |
| L4 | None of the following finite-supports $R$ without a grain: named non-slices; Fermi distance (a continuous scale); lock-side subsets of $S(O)$; Morse, conjugate and cut loci; $I^+$, vacuum and energy conditions | Thms 22, 24, 28, 29, 30 | proved (named scope; "not a closed nothing supplies") |
| L5 | Least action on the support: a continuous $y$ does not finite-support $R$; an integer $y\in[0,Y]$ is a grain | Thm 25 (`least-action-support.md`) | proved |
| L6 | Combinatorial $y$ (edge count, Euler characteristic, out-degree) does not finite-support $R$ without a grain, or a law plus a slice | Thm 26 (`combinatorial-y.md`) | proved |
| L7 | Restricting targets to $S(O)=\mathrm{Occ}(O)\setminus\gamma_O$ is lock-side and not E-smuggling. It gives a continuum on non-constant curvature and may be empty on homogeneous lumps | Thm 27 (`in-patch-support.md`) | proved; named, not adopted |
| L8 | Countable (uncountable) out-degree gives countable (uncountable) finite walks, and dually for in-degree. A countably branching tree still has a continuum of rays | Thms 31, 33 | proved |
| L9 | A delayed fork needs some reachable out-degree $\ge2$ | Thm 32 (`branching-extra.md`) | proved |
| L10 | A walk count is infinite if a cycle can be pumped; on a DAG with finitely many walks it is well defined | Thms 20, 21 (`fusion-and-path-counting.md`) | proved |
| L11 | Hitchhiker $\tau$ does not timestamp type (ii), so edges carry no proper time (hence strict alternation, §4.2) | Thm 23 (`type-ii-clock.md`) | proved; alternation is a convention |
| L12 | The following are all extras, named, not adopted, and "not a grain" or "does not grain": uniformity (#46); locality; Markov versus history dependence; measurability (#54); closed graph (#55); compact-valued stars (#57); properness leftover (1) (#58); open graph (#59); measurable selection (#63, "extra-on-extra"); selection theorems; irreflexivity, transitivity, asymmetry, totality, antisymmetry, (converse) well-foundedness, acyclicity, finite ancestors; no dead ends | `uniform-law-of-r.md` … `converse-well-founded-r.md`; `remainder.md` | named (each proved "extra" or "does not grain" where stated) |

**Summary of §1.** The proved constraints are all of one shape:
- whatever a law of $R$ is, it is extra (L1, L2);
- a readout of the germ gives stars that are singletons or continua unless a grain is named (L3–L6);
- counting needs finiteness that $R$ must supply (L8–L10).

The pinned constraints come from one worked rule on one orbit at two values of $c$. Under (a), transient branching is an instance fact, not a theorem. The conventions are the ones v0.7.1 lists as open (§9).

---

## 2. Candidate families the repo names, and what survives

"Survives" means it meets every proved constraint and every convention in force, allowing that some are left open. Motivation (K9) is met by no family, so it is not repeated in each row.

| Family | One line | Meets | Fails or leaves open | Costs (extra structure) |
|---|---|---|---|---|
| **F0. Empty $R$ (CWS)** | No type-(ii) edges; the singleton baseline | everything in §1 trivially | fails the working postulate $R\ne\emptyset$ and Paper 1's "the evolution is not unique"; no weights to ask about | abandoning type (ii) (`abandon-type-ii.md`) |
| **F1. Curvature-slice readout, as stated** (Kretschmann $\pm\varepsilon\hat n$) | At an isolated critical point of $K$ along $\gamma$, jump a proper distance $\varepsilon=c\lvert K\rvert^{-1/4}$ along $\pm\nabla K$ | stated, uniform, lock-side readout; finite stars ($\le3$); no Zeno on the instance (C7, C29) | fails (a) (outward edges, C30); fails (J1) and (J2) (C17, C34: jump share $2/3$); continuum of histories (C16); needs a throat convention (C37); slice empty on standard backgrounds (I7, I11) | the slice scalar, critical point versus level, $c$, throat convention, isotropy quotient |
| **F2. (a)-restricted curvature-slice readout** | F1 filtered by the lock-side test $O'^{u'}\in F(O)$ | (a); lock-side; finite stars; countable histories; late-window (J1) (C33) | fails (J2) at fixed $c$ (per-jump deviation over one period $\approx 90c$–$235c$ radial units, §3); fails early-window (J1) (share $1/2$); transient branching; slice blind spots as in F1 | as F1 minus the throat convention; plus the arrival flag (I4) |
| **F3. Short-jump reading of F2** (v0.7.1 §9 T3 row: "short jumps: near at the vertex, not (J2)") | F2 with $c\to0$, aiming at (J2) | per-jump deviation $\to0$ linearly in $c$ over a fixed window (§3) | jump count grows like $1/c$ and net displacement does not fall (§3); curvelet deviation grows with the window | as F2; a window and tolerance for (J2) |
| **F4. Grain-bearing lock-side readouts** | Stars from invariants rounded or binned (integer $y$, curvature bins, rounded Fermi distance) | finite stars by construction; lock-side apart from the grain | no instance; the grain is a free choice (L3–L6, L4) | a named grain |
| **F5. Least-action support filter** | Only diagrams that extremise an observable $y$ appear (`least-action-support.md`) | compatible with any family underneath | not a law by itself; continuous $y$ does not finite-support (L5); $L$ and $y$ unwritten | $y$, and a grain or an underlying law |
| **F6. In-patch support restriction** | Targets restricted to $S(O)$, or to $F(O)$ under (a) | lock-side, not E-smuggling (L7); (a) when restricted to $F(O)$ | continuum stars (C4, L7), so a selector is still needed | a selector (grain) |
| **F7. Regularity classes** | Measurable, closed-graph, open-graph, compact-valued, proper, with a measurable selection; uniform, local, Markov | compatible in principle with F1–F6 (none is excluded by §1) | properties, not laws: none selects a star or grains (L12). Whether F1/F2 have these properties is not checked here | each is a named extra |

Two further points:
- **Routes, not families.** v0.7.1's T3 row names "rule jumps out" (F0), "show jumps negligible" by (J1) (F2 over late windows) or (J2) (F3's aim), and "keep jumps" (F1). They are readings of the families above.
- **"Jump toward 10"** (C16) is a sub-rule of F1 used for the countability proof. It is not a separate candidate.

**What survives.** Surviving is not adoption or ranking; no family is endorsed. Among families with instances, only F2 meets every proved constraint and the conventions in force, with (J1) met only over late windows. F0 survives only by giving up $R\ne\emptyset$. F3–F7 are not excluded by anything in §1, but each either lacks an instance (F4, F6) or is not a law by itself (F5, F7). F1 is excluded as a candidate by I13 (it fails both (J1) and (J2)) and by (a) if Compatibility is kept. It stays useful as a consistency witness for the schema without (a).

### Pins

Python 3.13.5, numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0 (venv `/workspace/g128/venv`). Units $G=c=1$, $M=1$; source orbit $[10,20]$ with $E=0.969087$ and $L=4.170288$. Scripts stay on the shared machine; the repo holds no scripts. All pins are exact or deterministic, except #159 P1 (sampled, seed 7).

| script | SHA-256 | what it pins here |
|---|---|---|
| `/workspace/lawR/jtest.py` | `f9e9573fe708a72df22c53eee6a93e008b5f20a71b5f4be7aab7d4671d7b0631` | per-jump deviation versus $c$ (F2, F3); (a)-model jump law and census at $c=0.1,0.05,0.03,0.02,0.01$ |
| `/workspace/lawR/disp.py` | `7693c2629642351e2e287d9943b7d4bd82d575fd96e3db07b884413ef98addc6` | §3 test: net displacement of the final orbit |
| `/workspace/g175/census175.py` | `934e770644265039415e3a0061c29b4ef588a8ea33ebeb1443a22b24bd9a48d9` | C33 at $c=0.01$: 29,119 orbits, 14,478 stuck, exact law (#176) |
| `/workspace/g154/sim.py` | `df306f17…e035` | jump share 0.6672 (#159 P1) |
| `/workspace/born/pins/flrw_k.py` | `3ee6f263…dffa` | $K=80/27$ versus 0 (#159 P8) |

Imports:
- `/workspace/g168/c33r.py` `f9e9c31b61e9c3889245af8b70cec65bb4a105c50ccbd96c75fd488e431dcd45` (corrected classifier);
- `/workspace/g168/c33x.py` `4c02a785ed38c8c0b9fd9dd9b63d43b4bbc4074e9e9ffbebd4698fd1d5738d40`;
- `/workspace/g154/kr.py` `0432cc20f56afbc3ad862b16de8f825bf9e1d4a490cde07ad8e5740f9d872dee`.

Outputs are `/workspace/lawR/jtest_out.txt` and `disp_out.txt`. Other figures cited in §1 are cited by C-number and are pinned where v0.7.1 pins them.

---

## 3. One cheap test: does the short-jump reading separate from the transient reading?

- **Families separated.**
  - *F2 at fixed $c$*, the transient (J1) route: finitely many jumps per history, each of order the orbit's size.
  - *F3*, the short-jump (J2) route: the same rule read with $c\to0$, so that each jump is near the continuation.
  - v0.7.1's T3 row records "short jumps: near at the vertex, not (J2)" without numbers. The test asks whether shrinking $c$ produces a regime distinct from F2, in which the jumps are negligible in aggregate.
- **Inputs.**
  - The Kretschmann rule of v0.7.1 §5.4 (unadopted), restricted to (a)-admissible edges, with `kr.py` and the corrected classifier `c33r.py`.
  - Root: the $r=10$ periastron of $[10,20]$, $a=\mathrm{seg}$.
  - EPP1 weights as in `c33x.py`: with edges at both turning points, the first jump is at the current point with weight $2/3$ and at the other with $1/3$.
- **Grid.** $c\in\{0.1,0.05,0.03,0.02,0.01\}$, exact enumeration. $c<0.01$ is not cheap, since the reachable-orbit tree roughly doubles per jump.
- **Observable.** Under (a) decisions end almost surely, so every history ends on a stuck orbit $[r_{p,f},r_{a,f}]$. Let $\Delta=\lvert r_{p,f}-10\rvert+\lvert r_{a,f}-20\rvert$, and report $E_{\rm EPP1}[\Delta]$. This is the history-level form of (J2): how far the observer's orbit has moved once jumping stops.
- **Criterion** (fixed in the script header before `disp.py` was first run; the per-jump readout below had already been computed):
  - **SEPARATES** if $E[\Delta](0.01)/E[\Delta](0.1)\le0.2$: aggregate displacement falls at least in proportion to $c$, the short-jump signature;
  - **DOES NOT SEPARATE** if the ratio is $\ge0.5$: displacement stays of the order of the orbit's size, so shrinking $c$ trades jump size for jump count;
  - otherwise **INCONCLUSIVE**.

**Result (exploratory readout, not preregistered): does not separate.**

| $c$ | jump counts (support) | $E[\text{jumps}]$ | $c\,E[\text{jumps}]$ | final orbits | $E[\Delta]$ | $E[r_{p,f}]$, $E[r_{a,f}]$ |
|---|---|---|---|---|---|---|
| 0.1 | {1} | 1 | 0.100 | 2 | 10.863 | 11.764, 14.481 |
| 0.05 | {2} | 2 | 0.100 | 4 | 8.386 | 12.414, 15.247 |
| 0.03 | {4} | 4 | 0.120 | 16 | 8.583 | 13.144, 14.727 |
| 0.02 | {6, 7} | 6.4486 | 0.129 | 92 | 9.053 | 13.656, 14.645 |
| 0.01 | {12, 13, 14} | 13.8418 | 0.138 | 14,478 | 9.559 | 13.935, 14.376 |

The ratio $E[\Delta](0.01)/E[\Delta](0.1)=0.880$.

**Per-jump readout** (`jtest.py`; first decision at $[10,20]$, curvelet topology named as the sup-norm of $r(\tau)$ over the window):
- The deviation from the continuation over one radial period ($T_r=425.13$) scales linearly in $c$ as $c\to0$: $D_1/c\to234.2$ for the inward jump at periastron and $99.9$ for the outward jump at apastron, at $c=10^{-4}$.
- Over ten periods, $D_{10}\approx8.6\,D_1$ at small $c$, so the deviation grows with the window.
- At $c\ge0.01$ it saturates at about 10.

**What this shows, neutrally.**
- Within the only instanced surviving family, shrinking $c$ makes each jump near in proportion to $c$, on any fixed window.
- But the expected number of jumps grows roughly as $0.1$–$0.14/c$ on the grid, and the orbit still ends about 10 radial units from where it started. The final orbits narrow as $c$ falls (mean proper width 2.92 at $c=0.1$, 0.48 at $c=0.01$; 10.78 at the start) and sit near $r\approx14$.
- So on this grid F3 is not a separate survivor: (J2) per jump is bought at the cost of (J1).

**What it does not show.**
- Anything about $c<0.01$, other orbits, other slice scalars or other families.
- Anything about motivation, weights, Born or (M1)/(M2).
- The criterion was written with the per-jump readout already in hand, so this is a well-defined readout, not a preregistered test; it is exploratory.

---

## §L Literature

Author: Literature. **SCOPING ONLY, NOT A CLAIM.**

Prior work that selects which evolution is realised, read against §1's constraints and §2's families (labels as in this note). Each item gives (i) what it bears on here; (ii) where it clearly does not apply; (iii) citations. Nothing is proposed, adopted or ranked, and nothing bears on (M1) versus (M2). One (ii) holds throughout: apart from classical sequential growth, Müller, and Hall, Deckert and Wiseman, every item takes its weights from a wave function or quantum measure, and the framework has no amplitudes or interference (#159 §1.2), so at most the structure transfers.

**§L.1 Spontaneous collapse.**
(i) Ghirardi–Rimini–Weber (GRW) adds localisation "hits" at a fixed rate per particle. CSL makes the process continuous and couples it to mass density. Diósi and Penrose tie the rate to the gravitational self-energy of the difference between superposed mass distributions. All are stated, uniform stochastic jump laws whose constants are fixed by experiment. That is K9's empirical-target branch, applied to constants rather than to the law's form. GRW meets its own analogue of (J1) (I13): isolated microsystems almost never jump. There, jump rate and jump width are separate constants, whereas in F2 and F3 the single constant $c$ moves both jump size and jump count (exploratory, §3); a contrast, not a proposal. Bell's flashes (contrasted with matter density by Allori et al.) make the hits the beables. Tumulka's relativistic flash model violates Bell's inequality without a preferred foliation (v0.7.1, "Which Bell premise" row).
(ii) Diósi–Penrose needs superposed geometries; arms here are distinct germs. Not candidates.
(iii) Ghirardi, Rimini and Weber (1986); Pearle (1989); Ghirardi, Pearle and Rimini (1990); Diósi (1989); Penrose (1996); Bell (1987); Tumulka (2006); Allori et al. (2008).

**§L.2 Consistent and decoherent histories.**
(i) Griffiths, Omnès, and Gell-Mann and Hartle give probabilities within a consistent set but do not choose the set. Dowker and Kent find consistent sets many and mostly not quasiclassical, and conclude that "some selection principle" is needed for unconditional predictions. Kent shows that set freedom yields contrary retrodictions, each with probability one. Kent and McElwaine find Schmidt-based selection algorithms problematic. This is the histories version of L3 and F4: a measure does not fix the grain of individuation, which must be named, as the slice choice (this note's K2) and first-edge equivalence (K5) already are. Gell-Mann and Hartle (2012) posit one real fine-grained history in preferred variables: the chance reading with the variables named in advance.
(ii) Consistency is a condition on interference. With none, every tree is trivially consistent, and set selection returns only as the choice of slice, grain and cut.
(iii) Griffiths (1984); Omnès (1988); Gell-Mann and Hartle (1993; 2012); Dowker and Kent (1996); Kent (1997); Kent and McElwaine (1997).

**§L.3 Bohmian guidance and Bell-type jumps.**
(i) The initial configuration fixes the realised history. Dürr, Goldstein and Zanghì's typicality rests on equivariance: the dynamics carries the typicality measure to itself. The analogue here would be a consistency condition between a law of $R$ and the weights at successive slices, constraining the pair, not choosing (M1) or (M2). Bell's beables for quantum field theory, and the Bell-type field theories of Dürr, Goldstein, Tumulka and Zanghì, put stochastic jumps between deterministic segments, the nearest structural cousin of F1/F2. Their rates are not free: equivariance plus a minimality choice fixes them. That is selection by a principle within a named class, the kind K9 asks for.
(ii) v0.7.1 (§4.3, §10) already names both neighbours.
(iii) Dürr, Goldstein and Zanghì (1992); Bell (1986); Dürr, Goldstein, Tumulka and Zanghì (2004; 2005).

**§L.4 Causal-set sequential growth.**
(i) Classical sequential growth adds one element at a time. Internal temporality, discrete general covariance and Bell causality, with the Markov sum rule, narrow the transition probabilities to a generic family labelled by couplings $t_n\ge0$, $t_0=1$; Varadarajan and Rideout give the non-generic solutions. **The axioms narrow the law to a family; they do not force one.** v0.7.1 §5.4's motivation test allows exactly this: a rule selected "up to named constants" within an independently named class. K9's summary omits that clause. Brightwell et al. show that the physical questions are the label-invariant stem-set ones, which bears on I6 (arms modulo isotropy) and on F7's measurability. Rideout and Sorkin note that a classical stochastic dynamics reproducing quantum effects would have to drop Bell causality; so if F7's "local" were read as Bell causality, a law of $R$ would stay in the class Bell's theorem constrains. With Sorkin's quantum measure, the measure need not extend to the covariant σ-algebra. Dowker, Johnston and Surya give a quantum sequential growth model where it does not; Surya and Zalel give a criterion, and a large family where it does. This bears on v0.7.1 §9's "completed histories versus a cut" and on L8's continuum of rays.
(ii) A causal set grows its own spacetime and has no observer; here the vertices are germs joined by $R$. Not adopted (v0.7.1 §10).
(iii) Rideout and Sorkin (2000); Varadarajan and Rideout (2006); Brightwell et al. (2003); Sorkin (1994); Dowker, Johnston and Surya (2010); Surya and Zalel (2020).

**§L.5 Final conditions.**
(i) In the Aharonov–Bergmann–Lebowitz rule, extended to the two-state-vector formalism, a suitable final state can fix each measurement's result (Aharonov et al. 2014). Gell-Mann and Hartle put a final density matrix into the decoherence functional. Kent conditions beables on a hypothetical final-time measurement of mass-energy density. A late boundary condition fixes the realised history; no §2 family is of this kind. Such a law would take the history-dependent side of L12's "Markov versus history dependence" and fail F7's "Markov". It would strain memorylessness (Problem note 6, as v0.7.1 §9 cites it). It would not be Obs-local in v0.7.1 §9's sense unless the final condition were folded into $R$.
(ii) Kent (1997) derives contrary probability-one predictions in the time-neutral version.
(iii) Aharonov, Bergmann and Lebowitz (1964); Aharonov, Cohen, Gruss and Landsberger (2014); Gell-Mann and Hartle (1994); Kent (2014; 2015).

**§L.6 Anhomomorphic logic.**
(i) Sorkin takes reality to be one co-event, constrained by preclusion: events of quantum measure zero do not happen. Predictive content comes from what is forbidden, not from weights: the shape of the support filters F5 and F6, and of the forbid-only constraints I1 and this note's K3 (finite-jet matching).
(ii) Without interference, co-events reduce to single histories, so the family adds nothing without amplitudes.
(iii) Sorkin (2007a; 2007b).

**§L.7 Observer-first and outcome-counting work, 2008–2026.**
One observer-first proposal names a selection law. Müller postulates that the chance of the next observer state $y$, given the current state $x$, is an algorithmic prior $P(y|x)$, and keeps only the predictions shared by every choice of prior. In form this is an Obs-local, Markov chance rule (F7's regularity terms). Keeping what every member of a family predicts is a second precedent beside Rideout–Sorkin (not proposed for F2's $c$). It does not apply directly: its observer states are finite binary strings, not germs, and algorithmic probability is not computable. Weidner (preprint) adds a "small-signal truncation" to the Schrödinger equation and counts surviving branches; it acts on amplitudes, and Paper 1 §9 firewalls it. Hall, Deckert and Wiseman give a deterministic law for finitely many worlds, each counted once; nothing is selected and nothing branches. We found no work on observer space in the framework's sense (analytic germs with a time direction) that names a selection law. #159 §1.1's branch counting supplies weights, not such a law. Page–Wootters and Barbour's time capsules select no branch; omitted.

### §L References

- Aharonov, Y., Bergmann, P. G., and Lebowitz, J. L. (1964). Time symmetry in the quantum process of measurement. *Phys. Rev.* 134, B1410–B1416. doi:10.1103/PhysRev.134.B1410.
- Aharonov, Y., Cohen, E., Gruss, E., and Landsberger, T. (2014). Measurement and collapse within the two-state vector formalism. *Quantum Stud.: Math. Found.* 1, 133–146. doi:10.1007/s40509-014-0011-9; arXiv:1406.6382.
- Allori, V., Goldstein, S., Tumulka, R., and Zanghì, N. (2008). On the common structure of Bohmian mechanics and the Ghirardi–Rimini–Weber theory. *Brit. J. Phil. Sci.* 59(3), 353–389. doi:10.1093/bjps/axn012.
- Bell, J. S. (1986). Beables for quantum field theory. *Phys. Rep.* 137, 49–54. doi:10.1016/0370-1573(86)90070-0. Reprinted in *Speakable and Unspeakable in Quantum Mechanics*, 2nd ed., Cambridge University Press (2004), 173–180, doi:10.1017/CBO9780511815676.021.
- Bell, J. S. (1987). Are there quantum jumps? In C. W. Kilmister (ed.), *Schrödinger: Centenary Celebration of a Polymath*, Cambridge University Press. Reprinted in *Speakable and Unspeakable in Quantum Mechanics*, 2nd ed. (2004), 201–212, doi:10.1017/CBO9780511815676.024.
- Brightwell, G., Dowker, H. F., García, R. S., Henson, J., and Sorkin, R. D. (2003). "Observables" in causal set cosmology. *Phys. Rev. D* 67, 084031. doi:10.1103/PhysRevD.67.084031; arXiv:gr-qc/0210061.
- Diósi, L. (1989). Models for universal reduction of macroscopic quantum fluctuations. *Phys. Rev. A* 40, 1165–1174. doi:10.1103/PhysRevA.40.1165.
- Dowker, F., Johnston, S., and Surya, S. (2010). On extending the quantum measure. *J. Phys. A* 43, 505305. doi:10.1088/1751-8113/43/50/505305; arXiv:1007.2725.
- Dowker, F., and Kent, A. (1996). On the consistent histories approach to quantum mechanics. *J. Stat. Phys.* 82, 1575–1646. doi:10.1007/BF02183396; arXiv:gr-qc/9412067.
- Dürr, D., Goldstein, S., Tumulka, R., and Zanghì, N. (2004). Bohmian mechanics and quantum field theory. *Phys. Rev. Lett.* 93, 090402. doi:10.1103/PhysRevLett.93.090402.
- Dürr, D., Goldstein, S., Tumulka, R., and Zanghì, N. (2005). Bell-type quantum field theories. *J. Phys. A* 38, R1–R43. doi:10.1088/0305-4470/38/4/R01; arXiv:quant-ph/0407116.
- Dürr, D., Goldstein, S., and Zanghì, N. (1992). Quantum equilibrium and the origin of absolute uncertainty. *J. Stat. Phys.* 67, 843–907. doi:10.1007/BF01049004.
- Gell-Mann, M., and Hartle, J. B. (1993). Classical equations for quantum systems. *Phys. Rev. D* 47, 3345–3382. doi:10.1103/PhysRevD.47.3345.
- Gell-Mann, M., and Hartle, J. B. (1994). Time symmetry and asymmetry in quantum mechanics and quantum cosmology. In J. J. Halliwell, J. Pérez-Mercader and W. H. Zurek (eds.), *Physical Origins of Time Asymmetry*, Cambridge University Press. arXiv:gr-qc/9304023. Reprinted in World Scientific Series in 20th Century Physics (2010), 331–359, doi:10.1142/9789812836854_0023.
- Gell-Mann, M., and Hartle, J. B. (2012). Decoherent histories quantum mechanics with one real fine-grained history. *Phys. Rev. A* 85, 062120. doi:10.1103/PhysRevA.85.062120; arXiv:1106.0767.
- Ghirardi, G. C., Pearle, P., and Rimini, A. (1990). Markov processes in Hilbert space and continuous spontaneous localization of systems of identical particles. *Phys. Rev. A* 42, 78–89. doi:10.1103/PhysRevA.42.78.
- Ghirardi, G. C., Rimini, A., and Weber, T. (1986). Unified dynamics for microscopic and macroscopic systems. *Phys. Rev. D* 34, 470–491. doi:10.1103/PhysRevD.34.470.
- Griffiths, R. B. (1984). Consistent histories and the interpretation of quantum mechanics. *J. Stat. Phys.* 36, 219–272. doi:10.1007/BF01015734.
- Hall, M. J. W., Deckert, D.-A., and Wiseman, H. M. (2014). Quantum phenomena modeled by interactions between many classical worlds. *Phys. Rev. X* 4, 041013. doi:10.1103/PhysRevX.4.041013; arXiv:1402.6144.
- Kent, A. (1997). Consistent sets yield contrary inferences in quantum theory. *Phys. Rev. Lett.* 78, 2874–2877. doi:10.1103/PhysRevLett.78.2874; arXiv:gr-qc/9604012.
- Kent, A. (2014). Solution to the Lorentzian quantum reality problem. *Phys. Rev. A* 90, 012107. doi:10.1103/PhysRevA.90.012107; arXiv:1311.0249.
- Kent, A. (2015). Lorentzian quantum reality: postulates and toy models. *Phil. Trans. R. Soc. A* 373, 20140241. doi:10.1098/rsta.2014.0241; arXiv:1411.2957.
- Kent, A., and McElwaine, J. (1997). Quantum prediction algorithms. *Phys. Rev. A* 55, 1703–1720. doi:10.1103/PhysRevA.55.1703; arXiv:gr-qc/9610028.
- Müller, M. P. (2020). Law without law: from observer states to physics via algorithmic information theory. *Quantum* 4, 301. doi:10.22331/q-2020-07-20-301; arXiv:1712.01826.
- Omnès, R. (1988). Logical reformulation of quantum mechanics. I. Foundations. *J. Stat. Phys.* 53, 893–932. doi:10.1007/BF01014230.
- Pearle, P. (1989). Combining stochastic dynamical state-vector reduction with spontaneous localization. *Phys. Rev. A* 39, 2277–2289. doi:10.1103/PhysRevA.39.2277.
- Penrose, R. (1996). On gravity's role in quantum state reduction. *Gen. Relativ. Gravit.* 28, 581–600. doi:10.1007/BF02105068.
- Rideout, D. P., and Sorkin, R. D. (2000). Classical sequential growth dynamics for causal sets. *Phys. Rev. D* 61, 024002. doi:10.1103/PhysRevD.61.024002; arXiv:gr-qc/9904062.
- Sorkin, R. D. (1994). Quantum mechanics as quantum measure theory. *Mod. Phys. Lett. A* 9, 3119–3127. doi:10.1142/S021773239400294X.
- Sorkin, R. D. (2007a). Quantum dynamics without the wave function. *J. Phys. A* 40, 3207–3221. doi:10.1088/1751-8113/40/12/S20; arXiv:quant-ph/0610204.
- Sorkin, R. D. (2007b). An exercise in "anhomomorphic logic". *J. Phys.: Conf. Ser.* 67, 012018. doi:10.1088/1742-6596/67/1/012018; arXiv:quant-ph/0703276.
- Surya, S., and Zalel, S. (2020). A criterion for covariance in complex sequential growth models. *Class. Quantum Grav.* 37, 195030. doi:10.1088/1361-6382/ab987f; arXiv:2003.11311.
- Tumulka, R. (2006). A relativistic version of the Ghirardi–Rimini–Weber model. *J. Stat. Phys.* 125, 821–840. doi:10.1007/s10955-006-9227-3; arXiv:quant-ph/0406094.
- Varadarajan, M., and Rideout, D. (2006). General solution for classical sequential growth dynamics of causal sets. *Phys. Rev. D* 73, 104021. doi:10.1103/PhysRevD.73.104021.
- Weidner, M. (2025). Unified quantum dynamics: the emergence of the Born rule. Preprint, arXiv:2504.06495.
- Framework: this note §§1–3; `versions/v0.7.1-prose.md` §§4.3, 5.4, 7, 9, 10; `reviews/born-rule-readiness.md` (#159) §1; `papers/observer-space-ontology.md` §9.

---

## 4. Gaps

- **The 16 instances.** Only rows 1–15 bear on $R$, and all are from one worked rule plus analytic cases. No row tests a rule other than the Kretschmann family.
- **Regularity classes (F7).** Whether F1/F2 are measurable, closed-graph or compact-valued in the Fermi-slice topology was not checked. Doing so would be new leftover work and is out of scope.
- **Grain-bearing and support families (F4–F6).** None has a worked instance, so none can enter a discriminating test yet.
- **§3 range.** The test stops at $c=0.01$. Below that the exact tree is not cheap, and sampling was not used.
- **Slice choice (K2).** A second slice scalar on the same instance (e.g. the Bel–Robinson $W$) was not tried, so the Kretschmann family's dependence on the slice choice is not measured.
- **Motivation (K9).** No family meets it. Nothing here addresses it.
- **David's open questions.** Q-D1–Q-D5 and #139 (a)–(e) exist and bear on v0.7.1's T1–T3 and on "near". They are not answered here.

## References

Framework files:
- `versions/v0.7.1-prose.md`: §§4.2, 5.1, 5.3, 5.4, 7, 9 and App. A (C1–C38);
- `reviews/v0.6-prose-claude-opus-5.5.md` §1 (the 16 named instances) and `reviews/v0.6-claude-154-geometry.md` §4;
- `reviews/born-rule-readiness.md` (#159), `reviews/born-rule-readiness-scan.md` (#165, #174), `reviews/v0.7-prose-claude-pressure-test.md` (#169), `reviews/v0.7.1-prose-claude-pressure-test.md` (#176).

Named leftovers: the `papers/` files cited in §1.3, with `cheat-sheet.md` and `remainder.md` as the index.
