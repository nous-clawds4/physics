# Piecewise geodesic $C^k$ graph (hybrid motion package)

David Strayhorn

Working, abandonable. In-house note. Not a public v0.3 rewrite. Not Paper 1. No Born. No $1/N$ by hand. Leftover $R$-property mill not restarted.

**Status.** A hybrid motion package pressed against the CWS singleton HOLE (`reviews/v0.2.1-prose-claude-fable-5.1.md`; Geometry confirm `reviews/v0.2.1-motion-recommendation-geometry.md`) and against Theorem 7 / Prop. 7.3 (`papers/patch-edge.md`). Pieces stay analytic-geodesic; joins are only finite smoothness; the skeleton is a discrete graph (grain approach). Deferred: $k\to\infty$, edge lengths $\to 0$, max $k$, min edge length. For now: some fixed finite $k$, discrete graph. The open question “what is $C^k$ at a join?” is framed as a **menu for Ontology**, not locked here.

Companions: `papers/geodesic-lifts.md`, `papers/patch-edge.md`, `papers/phi-straits.md`, `papers/type-ii-adopted.md`, `papers/neighborhood-uncountable.md` (Thm 17), public `v0.3-prose.md` (type-(ii) $R$ background).

---

**Adopted (working, abandonable) — David 2026-09-07.** Option **F** is the working in-house join law: analytic-geodesic pieces; at vertices, Option **C** at fixed finite $k\ge 1$ plus Option **E** (graph incidence); arms = graph out-star. Reject D as primary; A parked until gauge-as-space; B only inside C. Continuum limits deferred. Public v0.3 type-(ii) $R$ not replaced until a controlled discrete $|B|\ge 2$ example. No $1/N$. Paper 1 untouched. Leftover $R$-property mill not restarted. See `papers/piecewise-geodesic-Ck-graph-ontology.md`.

---

## 1. Why this escapes the CWS singleton HOLE

**CWS HOLE (confirmed).** Under CWS 1–4, every piece is a geodesic lift and joins match to **infinite order** in $\tau$. Then $|B_{\mathrm{CWS}}(O^u)|=1$: unique curvelet; switches invisible in $\mathrm{Obs}$ (Prop. 3.2, Cor. 3.1, Thm 7, Thms 8–9).

**What this package drops.** Infinite-order / $C^\infty$ matching at joins. The history as a whole is **not** a single real-analytic map $I\to\mathrm{Obs}$. Theorem 2 / Theorem 9 (analytic-curve $\Phi$ cannot thick-trunk delayed-fork) therefore **do not apply to the whole path**. They still apply **on each open edge**.

**What this package keeps.** Analytic geodesic lifts on pieces (type-(i) honesty inside edges). Discrete $V^*$ so that branching is a graph out-star, not a continuum of $C^\infty$ flat perturbations (Claude escape (a) continuum risk under weak equivalence).

**Not claimed.** That $|B|\ge 2$ is forced. Only that the CWS mechanism that forced $|B|=1$ is broken, so $|B|\ge 2$ is *structurally possible* once vertices and edges are chosen.

---

## 2. At a join, what is $C^k$? — menu for Ontology

Do **not** lock one option here. The phrase “$C^k$ across a vertex” is ambiguous until a carrier is named. Geometry lists options Ontology (and David) can choose among. Combinations are possible; costs differ.

Write $\tau_*$ for the join parameter and $O^{u*}$ for the vertex germ.

### Option A — Obs-path in $\tau$ (needs $\mathrm{Obs}$ as a space)

The map $\gamma:I\to\mathrm{Obs}$ is $C^k$ at $\tau_*$ in some fixed topology / charts / Fréchet structure on $\mathrm{Obs}$.

- **Needs:** gauge-as-space closed enough to make $C^k(\mathrm{Obs})$ meaningful (open in public v0.3).
- **Cost:** imports the space problem into the join law.
- **Escape from HOLE:** yes, if $k<\infty$ and equivalence of arms uses jets of $\gamma$ only through order $k$ (or graph out-stars), not infinite-order path-jets.

### Option B — Orientation $u(\tau)$ only

Transport $u$ along each piece (Fermi / parallel transport in its $W$). At $\tau_*$, require the incoming and outgoing $u$ to agree through order $k$ in a common identification of tangent spaces at the shared germ (germ isometry / isotropy — public v0.3 already flags isotropy).

- **Needs:** a transport-and-identify rule for $u$ across worlds (already open for type-(ii) switches).
- **Cost:** does not by itself constrain how the *metric* germs approach the join along the two pieces beyond $O^{u*}$ at the vertex.
- **HOLE:** matching $u$ to infinite order with geodesic pieces and shared germ re-enters uniqueness; finite $k$ leaves room for distinct outgoing pieces only if something else differs (different $W$, different higher jets of $\gamma$, or graph choice of next vertex).

### Option C — Metric jets along the path through order $k$

Along each piece, the infinite jet of $g$ varies analytically in $\tau$. At $\tau_*$, require agreement of the **truncated** jet $j^k g$ (and $u$ through order $k$) between incoming and outgoing pieces.

- **Needs:** a meaning of $j^k g(\tau)$ along a geodesic lift (available in Fermi coordinates on each piece); a comparison map at the shared germ.
- **Cost:** for $k=\infty$ this is CWS matching and the HOLE returns. Finite $k$ is a deliberate truncation.
- **Note:** Borel / finite jets do not determine a unique analytic lump (Paper 1 / public analyticity lock). Truncation is therefore a *join rule*, not a replacement for the elementary object (still infinite jet at each $\tau$ on open edges).

### Option D — Spacetime curve in a chart / Fermi frame (single-$W$ reading)

If both pieces live in one $W$, require the spacetime curve $\sigma(\tau)$ to be $C^k$ (or $C^{k+1}$ with $\dot\sigma$ $C^k$) at $\tau_*$ in $W$.

- **Needs:** a single ambient $W$ across the join, or an isometric identification of neighborhoods.
- **Cost / clash:** if the glue of *metrics* across a hypersurface is only $C^k$, Prop. 7.3: that $W$ **leaves the locked analytic spacetime category**. So either (i) $W$ stays analytic and the “join” is only a non-geodesic $C^k$ reparameterization/kink *inside* one analytic $W$ (then analytic geodesic uniqueness still pushes toward one geodesic unless the curve is allowed to be non-geodesic at the join — i.e. Direction Switching territory), or (ii) one accepts non-analytic $W$ as a different object (not this package’s default).
- **Geometry advice:** do **not** take Option D as the primary reading of this package if the intent is to keep analytic worlds on pieces and fork by **switching** $W$ or by **graph edges**. Prefer A/B/C/E.

### Option E — Graph-native (no continuum matching beyond the vertex)

The only join datum is: both edges are incident to the same discrete vertex $O^{u*}\in V^*$. No $C^k$ matching of paths in a continuum ambient space is required beyond “same vertex.” Smoothness language is then metaphorical, or applies only *within* each edge.

- **Needs:** the discrete skeleton (already in the package).
- **Cost:** “$C^k$ joins” becomes almost vacuous unless supplemented by A–C on how pieces attach to the vertex’s infinite jet / $u$.
- **HOLE:** escaped by discreteness of out-stars, not by finite smoothness. Closest to public type-(ii) $R$ with geodesic-labelled edges.

### Option F — Hybrid default candidate (for Ontology to accept or reject)

On each open edge: analytic geodesic lift in some analytic $W$ (type i). At vertex $O^{u*}$: require **Option C at finite $k$** (truncated jet + $u$ through order $k$) **and** incidence in the discrete graph (**E**). Equivalence of arms = distinct outgoing edges in $E^*$ (graph out-star), not infinite-order Obs-path jets.

- **Escapes HOLE:** yes (no infinite-order matching; arms are graph edges).
- **Still open:** law of $V^*$ and $E^*$; choice of $k$; continuum risk in *generating* $V^*$ (next section).

---

## 3. Pressure-test

### 3.1 What works

- **Breaks CWS singleton mechanism.** Whole-path analyticity / infinite-order matching is dropped at vertices.
- **Keeps type-(i) honesty on edges.** Prop. 3.2, Thm 3, Cor. 3.1 still govern each open piece.
- **Discrete $|B|$ possible in form.** If $V^*,E^*$ are given as a locally finite graph, out-degree at $O^{u*}$ is a discrete $|B|$ candidate (hard gate shape).
- **Compatible with public type-(ii) spirit.** Graph-paths; abandonable; Prop. 13 still applies to *which* edges exist.
- **Thm 7 scoped correctly.** Thm 7 kills $\sim$-splits among *analytic geodesic* extensions of $E_\gamma$ members at $\partial P$. It does not forbid a *different package* whose joins are non-analytic in $\tau$ or whose next edge is a type-(ii) choice off the unique curvelet. Prop. 7.3 forbids analytic *metric* gluing that invents a new germ; it does not force CWS matching on Obs-paths that switch $W$ with only finite-order agreement.

### 3.2 What fails or stays empty

- **No law of the graph.** Locked data at $O$ still do not determine $V^*$ or $E^*$ (Prop. 13 pattern). Discrete $|B|\ge 2$ is not exhibited.
- **No $1/N$.** Weights not implied.
- **Option D as primary fails** against locked analytic $W$ (Prop. 7.3) unless one changes the spacetime object or allows non-geodesic pieces (Direction Switching continuum risk).
- **Reintroducing $C^\infty$ joins** returns the HOLE.
- **Using infinite-order equivalence on arms** while only requiring $C^k$ joins is incoherent: pick equivalence compatible with finite $k$ (graph out-star or $j^{\le k}$).

### 3.3 Continuum risks of “edge of at least one”

Vertex rule: $p^*$ lies on the edge of **at least one** patch in the ensemble.

| Risk | Why |
| --- | --- |
| **Continuum of candidate $p^*$** | For a fixed germ, $\partial P$ along a geodesic is often a single $\tau_\partial$ (Thm 6 examples), but “edge of at least one patch in the ensemble” ranges over many $W\in E(O)$ and many occurrence anchors. Without a selection rule, the raw pool of candidates can be a continuum (sibling anchors; continuum of ensemble labels; Fermi-slice continua nearby — Thm 17). |
| **“At least one” is weak** | Almost any incompleteness or chart-edge in some exotic $W$ could nominate a vertex. That is not yet a grain of $\mathrm{Obs}$; it is an invitation to overgenerate $V^*$. |
| **Grain still extra** | Declaring $V^*$ discrete is a **grain approach** (chosen subset), not a theorem that $\mathrm{Obs}$ is discrete. Same honesty as public v0.3: grain not locked. |
| **Edge lengths $\to 0$ (deferred)** | If edges can shrink without a positive lower bound, discrete graphs can densify toward continuum path space and reintroduce continuum $|B|$ under weak equivalences. Deferred on purpose. |
| **$k\to\infty$ (deferred)** | Recovering CWS-like matching in the limit may recover the singleton HOLE along convergent sequences of joins. Deferred; do not treat the limit as harmless. |

**Pressure-test conclusion.** The package is a coherent *escape hatch* from the CWS HOLE if joins are finite-$k$ and arms are graph out-stars. It does **not** by itself supply countable discrete branching. The phrase “edge of at least one” needs a later selection rule or it continuum-risks $V^*$.

---

## 4. Relation table

| Object | Relation to this package |
| --- | --- |
| CWS 1–4 | Rejected as branching law; retained as null baseline ($\|B\|=1$). |
| Public type-(ii) $R$ (v0.3) | Background launching pad; this note specializes edges to geodesic-labelled pieces + $C^k$ joins + discrete $V^*$. |
| Thm 2 / Thm 9 | Apply on open edges; not to whole piecewise path if joins are not analytic. |
| Thm 7 | No analytic $\sim$-split of next germs among $E_\gamma$ at $\partial P$; does not forbid non-CWS joins. |
| Prop. 7.3 | Analytic metric glue across $S$ cannot invent a new germ; $C^k$ *spacetime* glue leaves locked $W$. Prefer Obs/graph join readings (A/C/E/F) over changing $W$'s category. |
| Prop. 13 | Still: locked data do not determine which type-(ii) / graph edges exist. |
| Leftover $R$-property mill | Not restarted (no acyclicity / finite Desc / … inventory here). |

---

## 5. Other open questions the package needs

1. **Which option in §2 is the join law?** (Ontology / David.) Geometry’s non-binding lean: **F** (C at finite $k$ + graph incidence E), not D.
2. **Law of $V^*$:** which $O^{u*}$ count as vertices among “edge of at least one”? Selection rule, or named finite/countable set — without pretending it is forced by the germ alone.
3. **Law of $E^*$:** which piecewise-geodesic segments are allowed edges? (Same Prop. 13 cost.)
4. **Choice of fixed $k$:** minimal $k$ for the intended physics; whether $k$ is universal or edge-dependent.
5. **Discrete $|B|\ge 2$ controlled example:** exhibit one finite graph with out-degree $\ge 2$ under explicit rules — or say none yet (public v0.3 honesty).
6. **Equivalence for $B$:** graph out-star vs $j^{\le k}$ path agreement — pick one compatible with finite $k$.
7. **Cross-world identification at a vertex:** how $u$ and truncated jets are compared when incoming and outgoing pieces live in different $W$.
8. **Deferred limits:** $k\to\infty$, edge length $\to 0$, max $k$, min length — when reopened, re-pressure-test the HOLE and continuum risks.
9. **Abandon / replace public $R$:** whether this package stays a refinement note or becomes the next public launching pad.
10. **Weights:** still not $1/N$ by hand; EPP1 still needs discrete $B$ first.

---

## 6. Report line

- **Named (working, abandonable).** Piecewise analytic-geodesic pieces + $C^k$ joins + discrete graph skeleton (grain approach). Deferred continuum limits.
- **Escapes CWS singleton HOLE** by dropping infinite-order matching on the whole path; Thm 2/9 scoped to open edges.
- **$C^k$ menu (§2).** Options A–F for Ontology; do not lock here. Lean F, not D.
- **Pressure-test.** Works as escape hatch; fails to supply law of $V^*$/$E^*$ or discrete $|B|\ge 2$; “edge of at least one” continuum-risks candidate vertices.
- **Not done.** Law of graph; $1/N$; Born; Paper 1; leftover mill; public rewrite.

---

## References

Strayhorn, D. Geodesic lifts. `papers/geodesic-lifts.md`. Prop. 3.2, Thm 3, Cor. 3.1.

Strayhorn, D. Patch edge. `papers/patch-edge.md`. Thm 7, Prop. 7.3.

Strayhorn, D. Straitjacket on $\Phi$. `papers/phi-straits.md`. Thms 8–9.

Strayhorn, D. Type-(ii) links adopted. `papers/type-ii-adopted.md`. Prop. 13.

Strayhorn, D. Neighborhoods uncountable. `papers/neighborhood-uncountable.md`. Thm 17.

Geometry. CWS HOLE confirm + type-(ii) recommendation. `public-papers/observer-space-framework/reviews/v0.2.1-motion-recommendation-geometry.md`.

Claude Fable 5.1. HOLD on v0.2.1. `public-papers/observer-space-framework/reviews/v0.2.1-prose-claude-fable-5.1.md`.
