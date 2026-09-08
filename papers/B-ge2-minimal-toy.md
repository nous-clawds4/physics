# Minimal toy: $|B_R|=2$ as a digraph fact (retired as $V^*$ demo)

David Strayhorn

**Status (v0.5 honesty — Claude #117 / Geometry #118).** This note is **retired as a demonstration that $V^*$ extend-vs-not + Option F yield discrete $|B|\ge 2$ under the public §2 ensemble.** Keep at most as a **digraph fact**: some abstract $(V,R)$ has $|B_R|=2$ under composition reading (C) (continue class + one type-(ii) out). Hand-built in **three** places: (i) ensemble $\{W_{\mathrm{M}},W_{\mathrm{cut}}\}$ chosen so $T_{\mathrm{die}}=\{1\}$ (under public §2, Minkowski deaths fill a continuum); (ii) vertex / $W_{\mathrm{cut}}$ (restricted Minkowski — Thm 6 “Not an example” / killed as finite-lifetime patch after maximality; flat curvelet ⇒ $\gamma(1)$ same Obs lump as root under “same germ = same vertex”); (iii) type-(ii) out named by hand (Prop. 13). Public v0.5 join reading = **Option E residue**, not Option F. No Born. No $1/N$. Leftover mill not restarted. Prefer a non-flat germ if a schematic is rebuilt later.

**Historical body below** is retained for provenance; do not cite it as clearing the public controlled-example gate or as a $V^*$ discreteness theorem.

---

# (archived body)

## 0. $V^*$ caveats (stamped)

From Geometry ADOPT-with-caveats on extend-vs-not:

1. Scope = along a named hitchhiking curvelet $\gamma_{O^u}$ only.
2. Vertices are extend-vs-not / Thm 7(3) loci, **not** Obs forks by themselves.
3. Discrete $V^*$ along $\gamma$ needs discrete $T_{\mathrm{die}}$ (here finite).
4. Prop. 13 still governs type-(ii) outs.

This toy obeys those caveats. It does **not** claim $|B|\ge 2$ from extend-vs-not alone.

---

## 1. Named worlds and hitchhiking data

**Root.** Let $O^u$ be the infinite jet of Minkowski metric at the origin $p=0$, with $u=\partial_t$ (future unit). Prop. 3.2: unique curvelet $\gamma=\gamma_{O^u}$ along the geodesic $\sigma(\tau)=(t=\tau,\mathbf{0})$.

**Finite hitchhiking family $E_\gamma=\{W_{\mathrm{M}},W_{\mathrm{cut}}\}$** (two pointed occurrences of the same germ; schematic labels):

| Label | World (schematic) | Lifetime $\tau_W$ of $\sigma$ |
| --- | --- | --- |
| $W_{\mathrm{M}}$ | Full Minkowski spacetime, anchor at $0$ | $\tau_W=+\infty$ (Thm 6 infinite case) |
| $W_{\mathrm{cut}}$ | Minkowski cut off so $\sigma$ is future-inextendible at $\tau=1$ (e.g. only the open slab $t<1$, or $t\ge 1$ deleted), same germ at $0$ | $\tau_W=1$ |

Both realize $O^u$ at $\tau=0$ and share $\gamma$ on $[0,1)$ (Thm 4 / Prop. 3.2). $W_{\mathrm{cut}}$ is deliberately **incomplete** as a manifold-with-edge story; it is not the maximal simply-connected patch $P(O)$ (Thm 6: restricted Minkowski maximality goes to full Minkowski). As a member of $E_\gamma$ it is enough for a finite-lifetime label. Abandonable schematic — not a claim that incomplete cuts are preferred ontology.

**Death set.** $T_{\mathrm{die}}=\{1\}$, discrete. Finite $E_\gamma$ $\Rightarrow$ discrete candidate vertex times.

---

## 2. $V^*$ nonempty at $\tau_*=1$

At $\tau_*=1$:

$$
E_{\mathrm{ext}}(1)=\{W_{\mathrm{M}}\}\neq\emptyset,\qquad
E_{\mathrm{die}}(1)=\{W_{\mathrm{cut}}\}\neq\emptyset.
$$

**Vertex.** $O^{u*}=\gamma(1)$: Minkowski germ at $(t=1,\mathbf{0})$ with $u=\partial_t$. Mark $O^{u*}\in V^*$ under extend-vs-not.

**Not an Obs fork.** Thm 7(3): $W_{\mathrm{cut}}$ dying and $W_{\mathrm{M}}$ extending yields a **single** analytic continuation of the elementary object (the extender), not two $\sim$-branches. Die = dropout.

---

## 3. Explicit $E^*$ at $O^{u*}$ (out-degree $2$)

**Option F.** Join at $O^{u*}$: truncated jet $+\,u$ through fixed finite $k\ge 1$; graph incidence; arms = graph out-star.

**Two outgoing edges** (named):

| Edge | Kind | Target / piece | Role |
| --- | --- | --- | --- |
| $e_{\mathrm{ext}}$ | Thm 7 analytic geodesic continuation | Continue $\sigma$ in $W_{\mathrm{M}}$ for $\tau>1$; next germs along $\gamma\big|_{[1,1+\delta)}$ | The **one** hitchhiking out. Any other analytic geodesic extender from $E_{\mathrm{ext}}$ is identified with this arm (Thm 7(2)). |
| $e_{\mathrm{ii}}$ | **Type-(ii)** | Edge $(O^{u*},O_{\mathrm{FLRW}}^{u'})$ where $O_{\mathrm{FLRW}}^{u'}$ is the comoving germ of spatially flat dust FLRW with future crunch (Thm 6 finite twin: scale factor $(1-t)^{2/3}$, germ at $t=0$, $u=\partial_t$) | Second arm. **Not** successive germs along the Minkowski geodesic lift of $O^{u*}$. Different curvature invariants; not Thm-7-identified with $e_{\mathrm{ext}}$. |

**Graph.** $V^*\supseteq\{O^{u*},O_{\mathrm{FLRW}}^{u'}\}$ (and whatever prefix vertices one wants unused here). $E^*\ni e_{\mathrm{ext}},e_{\mathrm{ii}}$ at $O^{u*}$.

**Option F matching.** On $e_{\mathrm{ext}}$, the piece is the analytic geodesic lift in $W_{\mathrm{M}}$ (type i on the open edge). On $e_{\mathrm{ii}}$, the piece begins at $O_{\mathrm{FLRW}}^{u'}$ as a geodesic lift in that FLRW world after a type-(ii) jump; join datum at $O^{u*}$ is only finite-$k$ truncated jet $+\,u$ agreement under the adopted identification rule for F, **not** infinite-order CWS matching (which would be impossible across distinct germs anyway).

**Equivalence / $B$.** Arms = distinct out-edges of the out-star at $O^{u*}$.

$$
B(O^{u*})=\bigl\{[e_{\mathrm{ext}}],[e_{\mathrm{ii}}]\bigr\},\qquad |B(O^{u*})|=2.
$$

Discrete, finite. Hard gate for EPP1 is met **in form** for this toy only. No weights assigned.

---

## 4. Prop. 13 honesty

Locked data at $O^{u*}$ (lump, local patch, curvelet germ, ensemble fiber) determine at most the type-(i) successive pairs along $\gamma$ — here $e_{\mathrm{ext}}$. They do **not** determine $e_{\mathrm{ii}}$.

The type-(ii) out is **extra structure**, written by hand for the toy. Not forced by the germ. Not a neighborhood-law. Not a grain of all of $\mathrm{Obs}$. No $1/N$ on either edge.

Abandon $e_{\mathrm{ii}}$ and $|B|$ collapses to $1$ (plus optional terminal sink, not used). Abandon type (ii) entirely and layer (i) is unchanged.

---

## 5. Checklist (Vstar §3.3)

| Item | Toy |
| --- | --- |
| Finite $E_\gamma$ with finite lifetime and extender | $\{W_{\mathrm{M}},W_{\mathrm{cut}}\}$; $\tau_*=1$ |
| $V^*$ nonempty under extend-vs-not | $O^{u*}=\gamma(1)$ |
| Explicit $E^*$ out-degree $\ge 2$ under Option F | $\{e_{\mathrm{ext}},e_{\mathrm{ii}}\}$ |
| At most one Thm 7 out; other named type-(ii) | $e_{\mathrm{ext}}$ vs $e_{\mathrm{ii}}$ |
| Prop. 13 honesty | §4 |
| No $1/N$; no Born; Paper 1; leftover mill; public v0.3 | Firewall below |

---

## 6. What this does *not* show

- Not that $|B|\ge 2$ is forced along Minkowski hitchhiking.
- Not that incomplete cuts $W_{\mathrm{cut}}$ are preferred ensemble members.
- Not a Born derivation; not EPP1 weights; not a law of $R$.
- Not a continuum of arms (flat $C^\infty$ perturbations are not outs).
- Not a restart of leftover $R$-property inventory.
- Not a public v0.3 rewrite (cross-link only: type-(ii) launching pad + honesty that controlled examples were missing — this is an in-house existence sketch for discreteness **in form**).

---

## 7. Report line

- **Exhibited.** $|B(O^{u*})|=2$ under $V^*$ extend-vs-not (caveats stamped) + Option F out-star + $E^*$ lean, with outs $=\{e_{\mathrm{ext}},e_{\mathrm{ii}}\}$ (Thm 7 continuation + named type-(ii) to FLRW comoving germ).
- **Prop. 13.** Type-(ii) out extra, not forced by the germ.
- **Abandonable.** Drop $e_{\mathrm{ii}}$ $\Rightarrow$ $|B|=1$. No $1/N$. No Born. Paper 1 untouched.

---

## References

Strayhorn, D. $V^*$ by extend-vs-not. `papers/Vstar-extend-vs-not.md`. §3.3 checklist; ADOPT caveats.

Strayhorn, D. Patch edge. `papers/patch-edge.md`. Thms 6–7.

Strayhorn, D. Geodesic lifts. `papers/geodesic-lifts.md`. Prop. 3.2.

Strayhorn, D. Type-(ii) adopted. `papers/type-ii-adopted.md`. Prop. 13.

Strayhorn, D. Piecewise geodesic $C^k$ graph / Ontology F. `papers/piecewise-geodesic-Ck-graph.md`, `papers/piecewise-geodesic-Ck-graph-ontology.md`.