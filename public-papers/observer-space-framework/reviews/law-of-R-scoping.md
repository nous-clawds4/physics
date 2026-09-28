**SCOPING ONLY, NOT A CLAIM.**

# Law of $R$: what is already constrained, what survives, and one cheap test

Author: Geometry
Date: 2026-09-28
Question (Physics Lead, approved by CoS): what the 16 named instances, the toys and the named-leftover theorems already impose on any law of $R$; which candidate families the repo already names survive; and one cheap computation that would separate two survivors.

Scope and rules:
- This is an inventory. No law of $R$ is adopted or endorsed, and no new leftover theorem is proved.
- No paper, essay or Paper 1 edits. No (M1)/(M2) pick. No choice among T1–T3.
- No Born rule, no $|a|^2$ and no $1/N$ by hand.
- David's open questions (Q-D1–Q-D5, `mathematical-foundations/reviews/v0.1-ontology.md`; #139 (a)–(e)) are cited only as existing.
- Where a classifier matters, the corrected one is used (`c33r.py`; #169, #174).

**Answer.** The repo already fixes a good deal about any law of $R$, but almost all of it is negative or conditional:
- $R$ is extra (Prop. 13, Thm 19).
- A lock-side readout gives a singleton or a continuum unless a grain is added (Thms 17, 18, 24–30).
- Under (a), cross-continuation edges are excluded (C1).
- Any $R$ must meet (J1) or (J2) if typical histories are to look geodesic (C17).

Two families have worked instances: the Kretschmann rule as stated, and its (a)-restriction. Only the (a)-restriction meets the constraints the rule as stated fails, (a) and a late-window (J1). The other named families are either properties a law may have (measurable, closed-graph and so on) or add-ons that need a grain (least-action support, integer bins). None is motivated in the sense of the public gate (v0.7.1 §5.4).

The cheap test (§3) asks whether the "short jumps" reading of the (a)-restricted Kretschmann family is a separate survivor from its "transient" reading. It was run (about 70 s): on the grid it **does not separate** them. Shrinking the scale $c$ shrinks each jump in proportion to $c$, but the expected number of jumps grows in inverse proportion. The orbit's net displacement when the jumps end stays at about 9–11 radial units for every $c$ on the grid.

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
| T1 | Vertex times selected by the ensemble ("where some compatible world ends") form a continuum, even with inextendibility. $R$'s source set must come from a lock-side slice or an explicit discrete sub-ensemble (a grain on $E_W$) | V\*/Option F, C24, C25 | proved |
| T2 | The slice is codimension one, discrete only per curvelet. Which scalar, and critical point versus level, is a free choice (Bertrand over (slice, rule) pairs) | C21, C22, §5.1 | proved (C21); the choice is a convention |
| T3 | Finite-jet matching cannot create an edge: vacuous at $k=1$, prohibitive at $k\ge2$ | C27 | proved |
| T4 | $\lvert B\rvert\ge2$ is a digraph fact. The toy's two arms differ in lock-side invariants ($K=0$ versus $80/27$), so no germ symmetry swaps them; any equal weighting is postulated | `papers/B-ge2-minimal-toy.md`, #159 P8 | pinned (symbolic) |
| T5 | Arms are $B_R=\{[\gamma]\}\cup\mathrm{succ}_R$, with first-edge equivalence; dying is not an arm | C11, §4.2, §5.2 | convention |
| T6 | The Zeno-mass convention changes weights (undefined, $1/2$ or $1$) | C35 | pinned; the choice is open |
| T7 | A path-counting (M2) on a finite graph carries the MERW hazard | C36 | pinned (a hazard, not a constraint on $R$) |
| T8 | A rule whose jump path can meet the bifurcation sphere needs a throat convention (a case clause if "undefined") | C37 | pinned |
| T9 | Public gate: stated, uniform (no finite case list) and motivated. Motivation must select the rule within an independently named class, or state an empirical target; covariance does not count | C26, §5.4 | convention (the bar in force) |

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

"Survives" means it meets every proved constraint and every convention in force, allowing that some are left open. Motivation (T9) is met by no family, so it is not repeated in each row.

| Family | One line | Meets | Fails or leaves open | Costs (extra structure) |
|---|---|---|---|---|
| **F0. Empty $R$ (CWS)** | No type-(ii) edges; the singleton baseline | everything in §1 trivially | fails the working postulate $R\ne\emptyset$ and Paper 1's "the evolution is not unique"; no weights to ask about | abandoning type (ii) (`abandon-type-ii.md`) |
| **F1. Curvature-slice readout, as stated** (Kretschmann $\pm\varepsilon\hat n$) | At an isolated critical point of $K$ along $\gamma$, jump a proper distance $\varepsilon=c\lvert K\rvert^{-1/4}$ along $\pm\nabla K$ | stated, uniform, lock-side readout; finite stars ($\le3$); no Zeno on the instance (C7, C29) | fails (a) (outward edges, C30); fails (J1) and (J2) (C17, C34: jump share $2/3$); continuum of histories (C16); needs a throat convention (C37); slice empty on standard backgrounds (I7, I11) | the slice scalar, critical point versus level, $c$, throat convention, isotropy quotient |
| **F2. (a)-restricted curvature-slice readout** | F1 filtered by the lock-side test $O'^{u'}\in F(O)$ | (a); lock-side; finite stars; countable histories; late-window (J1) (C33) | fails (J2) at fixed $c$ (per-jump deviation over one period $\approx 90c$–$235c$ radial units, §3); fails early-window (J1) (share $1/2$); transient branching; slice blind spots as in F1 | as F1 minus the throat convention; plus the arrival flag (I4) |
| **F3. Short-jump reading of F2** (T3 row: "short jumps: near at the vertex, not (J2)") | F2 with $c\to0$, aiming at (J2) | per-jump deviation $\to0$ linearly in $c$ over a fixed window (§3) | jump count grows like $1/c$ and net displacement does not fall (§3); curvelet deviation grows with the window | as F2; a window and tolerance for (J2) |
| **F4. Grain-bearing lock-side readouts** | Stars from invariants rounded or binned (integer $y$, curvature bins, rounded Fermi distance) | finite stars by construction; lock-side apart from the grain | no instance; the grain is a free choice (L3–L6, L4) | a named grain |
| **F5. Least-action support filter** | Only diagrams that extremise an observable $y$ appear (`least-action-support.md`) | compatible with any family underneath | not a law by itself; continuous $y$ does not finite-support (L5); $L$ and $y$ unwritten | $y$, and a grain or an underlying law |
| **F6. In-patch support restriction** | Targets restricted to $S(O)$, or to $F(O)$ under (a) | lock-side, not E-smuggling (L7); (a) when restricted to $F(O)$ | continuum stars (C4, L7), so a selector is still needed | a selector (grain) |
| **F7. Regularity classes** | Measurable, closed-graph, open-graph, compact-valued, proper, with a measurable selection; uniform, local, Markov | compatible in principle with F1–F6 (none is excluded by §1) | properties, not laws: none selects a star or grains (L12). Whether F1/F2 have these properties is not checked here | each is a named extra |

Two further points:
- **Routes, not families.** The T3 row names "rule jumps out" (F0), "show jumps negligible" by (J1) (F2 over late windows) or (J2) (F3's aim), and "keep jumps" (F1). They are readings of the families above.
- **"Jump toward 10"** (C16) is a sub-rule of F1 used for the countability proof. It is not a separate candidate.

**What survives.** Among families with instances, only F2 meets every proved constraint and the conventions in force, with (J1) met only over late windows. F0 survives only by giving up $R\ne\emptyset$. F3–F7 are not excluded by anything in §1, but each either lacks an instance (F4, F6) or is not a law by itself (F5, F7). F1 is excluded as a candidate by I13 (it fails both (J1) and (J2)) and by (a) if Compatibility is kept. It stays useful as a consistency witness for the schema without (a).

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

**Result: does not separate.**

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
- The criterion was written with the per-jump readout already in hand, so this is a well-defined readout, not a preregistered test.

---

## §L Literature

Literature section to be supplied by Literature.

---

## 4. Gaps

- **The 16 instances.** Only rows 1–15 bear on $R$, and all are from one worked rule plus analytic cases. No row tests a rule other than the Kretschmann family.
- **Regularity classes (F7).** Whether F1/F2 are measurable, closed-graph or compact-valued in the Fermi-slice topology was not checked. Doing so would be new leftover work and is out of scope.
- **Grain-bearing and support families (F4–F6).** None has a worked instance, so none can enter a discriminating test yet.
- **§3 range.** The test stops at $c=0.01$. Below that the exact tree is not cheap, and sampling was not used.
- **Slice choice (T2).** A second slice scalar on the same instance (e.g. the Bel–Robinson $W$) was not tried, so the Kretschmann family's dependence on the slice choice is not measured.
- **Motivation (T9).** No family meets it. Nothing here addresses it.
- **David's open questions.** Q-D1–Q-D5 and #139 (a)–(e) exist and bear on T1–T3 and on "near". They are not answered here.

## References

Framework files:
- `versions/v0.7.1-prose.md`: §§4.2, 5.1, 5.3, 5.4, 7, 9 and App. A (C1–C38);
- `reviews/v0.6-prose-claude-opus-5.5.md` §1 (the 16 named instances) and `reviews/v0.6-claude-154-geometry.md` §4;
- `reviews/born-rule-readiness.md` (#159), `reviews/born-rule-readiness-scan.md` (#165, #174), `reviews/v0.7-prose-claude-pressure-test.md` (#169), `reviews/v0.7.1-prose-claude-pressure-test.md` (#176).

Named leftovers: the `papers/` files cited in §1.3, with `cheat-sheet.md` and `remainder.md` as the index.
