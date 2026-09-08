# $V^*$ by extend-vs-not (pressure-test)

David Strayhorn

Working pressure-test under adopted Option F (`papers/piecewise-geodesic-Ck-graph.md`, `papers/piecewise-geodesic-Ck-graph-ontology.md`, PR #104). Not a public v0.3 rewrite. Not Paper 1. No Born. No $1/N$. Leftover $R$-property mill not restarted.

**Status.** Formalizes a proposed selection rule for discrete vertices $V^*$ along a hitchhiking curvelet, and an optional lean for outgoing edges $E^*$. Geometry verdicts below: **adopt $V^*$ with caveats**; **adopt the $E^*$ lean as honesty**; **kill $E^*$ lean as a route to $|B|\ge 2$ by itself**.

Companions: `papers/patch-edge.md` (Thms 6–7), `papers/geodesic-lifts.md` (Prop. 3.2, Cor. 3.1), `papers/ensemble-labels.md` (Thm 4, Defs 1–3), `papers/type-ii-adopted.md` (Prop. 13), `papers/piecewise-geodesic-Ck-graph.md` (§3.3 continuum risk on “edge of at least one”).

---

## 0. Proposed rules (as received)

**$V^*$ (working proposal).** Along the hitchhiking curvelet $\gamma_{O^u}$, mark a vertex at parameter $\tau_*$ iff the hitchhiking family $E_\gamma$ splits nontrivially into

- nonempty $E_{\mathrm{ext}}(\tau_*)$: members whose analytic geodesic **extends** through $\tau_*$;
- nonempty $E_{\mathrm{die}}(\tau_*)$: members that **do not**.

Not the raw pool “edge of at least one patch in the multiverse.” Scope: along the curvelet under consideration. Same oriented germ $O^{u*}$ at $\tau_*$ = same vertex.

**$E^*$ (optional lean).** At such a $\tau_*$, candidate outs = inequivalent **extending** continuations after an Option F join (distinct next edges / post-join pieces). “Die” is ensemble **dropout**, not a second Obs arm, unless a terminal sink vertex is added explicitly. Multiple analytic extenders forced by Theorem 7 to the **same** next germ = **one** arm. So $|B|\ge 2$ needs disagreement among extenders (or a true second type-(ii) piece), not mere extend-vs-not.

---

## 1. Formalization

### 1.1 Hitchhiking data (locked)

Fix oriented $O^u$. Prop. 3.2: unique analytic curvelet $\gamma=\gamma_{O^u}$ on a positive interval. Definition 3 / Theorem 4 (`ensemble-labels.md`): hitchhiking ensemble $E_\gamma$ is the set of pointed occurrences that realize that curvelet; it is locally constant on $\mathrm{int}\,P(O)$ along $\gamma$. Multiplicity of $E$ is locally invisible as a fork of $\mathrm{Obs}$ (Cor. 3.1).

For each $[W,\iota]\in E_\gamma$, write $\tau_W\in(0,\infty]$ for the proper-time lifetime of the geodesic of $O^u$ in that $W$ (may be $+\infty$; Theorem 6: both finite and infinite occur).

### 1.2 Extend / die at $\tau$

For $\tau>0$ in the domain of $\gamma$ (including candidate boundary times),

$$
E_{\mathrm{ext}}(\tau)=\bigl\{[W,\iota]\in E_\gamma:\tau_W>\tau\bigr\},\qquad
E_{\mathrm{die}}(\tau)=\bigl\{[W,\iota]\in E_\gamma:\tau_W\le\tau\bigr\}.
$$

(Equivalently: extends through $\tau$ vs does not. Boundary convention $\tau_W=\tau$ in die is harmless for the split if adjusted consistently.)

**Definition ($V^*$ along $\gamma$, extend-vs-not).** A time $\tau_*$ is a **candidate vertex time** iff $E_{\mathrm{ext}}(\tau_*)\neq\emptyset$ and $E_{\mathrm{die}}(\tau_*)\neq\emptyset$. The vertex is the oriented germ $O^{u*}=\gamma(\tau_*)$ (same germ = same vertex).

**Remark.** Along a single curvelet the set of candidate times is determined by the set of distinct finite lifetimes

$$
T_{\mathrm{die}}=\{\tau_W:[W,\iota]\in E_\gamma,\ \tau_W<\infty\}.
$$

If $T_{\mathrm{die}}$ is discrete (e.g. finite $E_\gamma$), candidate $\tau_*$ are discrete along $\gamma$. If $T_{\mathrm{die}}$ is a continuum, candidate times are a continuum.

### 1.3 Relation to Theorem 7

Theorem 7 at a boundary time $\tau_\partial$:

1. Neither extends $\Rightarrow$ no next germ.
2. Both extend analytically $\Rightarrow$ **same** continuation of the elementary object (identity theorem / Thm 2 on the lifts).
3. One extends, one does not $\Rightarrow$ **single** continuation of the elementary object (the extender); prefixes are earlier nodes of the **same** history — **not** two disagreeing $\sim$-branches.

So a nontrivial extend-vs-not split is exactly the setting of Thm 7(3) (and of staggered deaths along $\gamma$). It **licenses a vertex** (something happens to the ensemble at $\tau_*$). It does **not** license two Obs arms from extend-vs-not alone.

### 1.4 Option F at such a vertex

Adopted join law F: at $O^{u*}$, truncated jet $+\,u$ through finite $k$, plus discrete graph incidence; arms = graph out-stars. Extend-vs-not supplies **when** to place a vertex on $\gamma$. It does not by itself choose outgoing type-(ii) edges off $\gamma$.

---

## 2. Pressure-test: $V^*$

### 2.1 What works

- **Strictly better than “edge of at least one.”** Candidates are times along a **named curvelet** where $E_\gamma$ actually splits, not an unbound multiverse edge pool (§3.3 of the hybrid note).
- **Aligns with Thm 6–7 / Thm 4.** Uses hitchhiking ensemble persistence on $\mathrm{int}\,P$, then dropout/extension at lifetimes; Thm 7(3) is the geometric meaning of the split.
- **Compatible with CWS HOLE honesty.** Does not pretend CWS infinite-order matching forks $\mathrm{Obs}$. Vertices can sit where the ensemble thins without claiming two curvelets.
- **Compatible with Option F.** Gives a discrete *schedule* of join/dropout loci **if** $T_{\mathrm{die}}$ is discrete; Option F then governs how pieces attach at those loci.
- **Same germ = same vertex.** Prevents duplicating one $O^{u*}$ as many labels.

### 2.2 What fails / stays empty

- **Not an Obs fork.** Thm 7(3): extend-vs-not $\neq$ two next germs. $V^*$ marks **ensemble events on one history**, not delayed $\sim$-branches.
- **Discreteness not free.** $|V^*\cap\gamma|$ inherits the cardinality structure of $T_{\mathrm{die}}$. Continuum many distinct lifetimes $\Rightarrow$ continuum many candidate $\tau_*$ along one curvelet. Countability/finiteness of $E_\gamma$ (or of $T_{\mathrm{die}}$) remains extra / open (cf. Claude HOLD on $|E|$; in-house Prop. 5.1-style openness).
- **Prop. 13 honesty.** Adopting “mark extend-vs-not times” is still a **chosen selection rule** reading $E_\gamma$. Locked germ data alone do not force a discrete vertex set. Better motivated than an arbitrary grain, still not a theorem that $V^*$ is finite.
- **Does not close law of $E^*$.** Vertices without outs are only dropout ticks unless edges are added.

### 2.3 Continuum risks (specific)

| Risk | Note |
| --- | --- |
| Continuum $T_{\mathrm{die}}$ | Continuum of incomplete lifetimes in $E_\gamma$ $\Rightarrow$ continuum candidate $\tau_*$. |
| Fiber jumps off curvelet (Thm 4) | $V^*$ rule as stated is **along $\gamma$**. Do not silently union edges of patches for germs off $\gamma$ or raw $E_{\mathrm{pt}}$ fibers — that reopens “at least one” overgeneration. |
| Sibling anchors | Occurrences modulo pointed isometry (Def. 2) already quotient siblings; do not double-count as two deaths at once unless lifetimes differ. |
| $\tau_*=0^+$ accumulation | Infinitely many deaths accumulating at $0$ would densify vertices at the root; forbid by finiteness of $T_{\mathrm{die}}$ near $0$, or accept and lose discrete local $B$. |

### 2.4 Verdict on $V^*$

**ADOPT with caveats** (working, abandonable).

Caveats to stamp beside the rule:

1. Scope = along a named hitchhiking curvelet $\gamma_{O^u}$ only.
2. Vertices are extend-vs-not / Thm 7(3) loci, **not** Obs forks.
3. Discrete $V^*$ along $\gamma$ requires discrete/finite $T_{\mathrm{die}}$ (extra honesty).
4. Still not a neighborhood-law; Prop. 13 remains for edges.

**Revise if:** one wants vertices off $\gamma$ or “edge of at least one” restored — Geometry would then **kill** that widening.

**Kill if:** marketed as supplying $|B|\ge 2$ or as forced finite grain of $\mathrm{Obs}$.

---

## 3. Pressure-test: $E^*$ lean

### 3.1 What works

- **Die $\neq$ arm.** Correct reading of Thm 7(3) and of ensemble dropout (Thm 4 jumps). Adding a terminal sink would be an **explicit** extra vertex type — fine if named, not smuggled.
- **Multiple analytic extenders = one next germ = one arm.** Theorem 7(2). Prevents fake $|B|=|E_{\mathrm{ext}}|$ counting.
- **Forces honesty for $|B|\ge 2$.** Needs disagreement among outs (inequivalent post-join pieces) or a true type-(ii) edge off the unique geodesic continuation — not extend-vs-not alone.
- **Fits Option F.** Graph out-star equivalence; finite-$k$ join; not CWS path-jet equivalence.

### 3.2 What fails

- **Cannot yield discrete $|B|\ge 2$ from hitchhiking extenders alone.** Under analytic geodesic continuation, Thm 7 collapses extenders to one Obs continuation. The lean correctly predicts $|B|=1$ (or $1+$ optional sink) at a pure extend-vs-not vertex.
- **Does not write the law of which type-(ii) outs exist.** Prop. 13 unchanged.
- **No $1/N$.**

### 3.3 Can it yield discrete $|B|\ge 2$ “in form”?

**In form, yes only after extra outs.** Schema:

- Vertex $O^{u*}$ from $V^*$ rule (extend-vs-not).
- Option F join datum at $O^{u*}$.
- At least **two** inequivalent outgoing edges in $E^*$ whose post-join pieces are **not** identified by Thm 7 — hence at least one out must be a **true type-(ii) / non-shared-geodesic-continuation** piece (or a non-analytic-geodesic piece, which is a different package).

**Minimal toy (checklist, not constructed here).**

1. Finite $E_\gamma$ with at least one finite lifetime $\tau_*$ and at least one extender (so $V^*$ nonempty).
2. Explicit $E^*$ at $O^{u*}=\gamma(\tau_*)$ with out-degree $\ge 2$ under Option F equivalence.
3. At most one of those outs is “the” Thm 7 analytic geodesic continuation; the other(s) named as type-(ii) (or otherwise not Thm-7-identified).
4. No $1/N$; no claim of Born; Paper 1 untouched.

Until (2)–(3) are written, $|B|\ge 2$ remains unexhibited — same public v0.3 honesty.

### 3.4 Verdict on $E^*$ lean

**ADOPT as honesty** (working): die = dropout; Thm 7 identify extenders; $|B|\ge 2$ needs real disagreement or type-(ii).

**KILL as a self-contained branching mechanism:** it does not produce a second Obs arm from extend-vs-not.

**REVISE only** if one explicitly adds a named terminal-sink arm and counts it in $B$ — then say so; Geometry would still not call that a delayed $\sim$-fork of analytic lifts.

---

## 4. Interaction with Option F and CWS HOLE

| Item | Interaction |
| --- | --- |
| CWS singleton HOLE | Unbroken for CWS paths. This $V^*$/$E^*$ package does not restore CWS as branching. |
| Option F | $V^*$ proposes *where* vertices sit on $\gamma$; F says *how* joins match; $E^*$ lean says *die isn’t an out*. |
| Thm 2 / 9 | Still on open analytic-geodesic edges. |
| Prop. 13 | Law of type-(ii) outs still extra. |
| Public v0.3 | Cross-link only; no rewrite required for this note. |

---

## 5. Report line

- **$V^*$ extend-vs-not: ADOPT with caveats.** Better than “edge of at least one”; formal along $\gamma$ via $E_{\mathrm{ext}}/E_{\mathrm{die}}$; Thm 7(3) loci; not Obs forks; discreteness inherits $T_{\mathrm{die}}$; Prop. 13 honesty retained.
- **$E^*$ lean: ADOPT as honesty; KILL as $|B|\ge 2$ engine.** Die = dropout; analytic extenders = one arm (Thm 7); discrete $|B|\ge 2$ needs explicit inequivalent outs (type-(ii) or equivalent), minimal toy checklist in §3.3.
- **Not done.** Constructed toy; law of $E^*$; $1/N$; Born; Paper 1; leftover mill; public rewrite.

---

## References

Strayhorn, D. Patch edge. `papers/patch-edge.md`. Thms 6–7.

Strayhorn, D. Geodesic lifts. `papers/geodesic-lifts.md`. Prop. 3.2, Cor. 3.1.

Strayhorn, D. Ensemble labels. `papers/ensemble-labels.md`. Thm 4, Defs 1–3.

Strayhorn, D. Type-(ii) adopted. `papers/type-ii-adopted.md`. Prop. 13.

Strayhorn, D. Piecewise geodesic $C^k$ graph. `papers/piecewise-geodesic-Ck-graph.md`.

Ontology. Option F adoption. `papers/piecewise-geodesic-Ck-graph-ontology.md`.
