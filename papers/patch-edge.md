# The edge of $P(O)$

David Strayhorn

Theorems 2–4 kill delayed forks of analytic geodesic lifts in the interior of $P(O)$. This note asks what happens if the geodesic meets the boundary of the maximal simply-connected analytic patch. Locked object unchanged. $\Phi$ is not written. Born is not derived. $E$ is not folded into $\sim$. No replacement typicality count.

Companions: `papers/analytic-patch-from-jet.md`, `papers/geodesic-lifts.md`, `papers/ensemble-labels.md`, `papers/analytic-split.md`.

**Status.** The hitchhiker story is dead at the boundary too, as a $\sim$-split of next germs among $E_\gamma$ members. If two members both extend the geodesic analytically through $\tau_\partial$, they share the same continuation of the elementary object (Theorem 7). If neither extends, there is no next germ. Quotients of $P$ cannot lengthen the geodesic past the cover. Analytic gluing across a hypersurface cannot produce a different germ (identity theorem). Lifetime in $P(O)$ may be finite or infinite; that dichotomy is not a theorem for every germ (Theorem 6).

---

## 0. What the interior did not kill

$E_\gamma$ members share the unique curvelet $\gamma_O$ on $\mathrm{int}\,P(O)$ (Prop. 3.2, Thm 4). The remaining hitchhiker picture was: at $\partial P$, pointed embeddings into distinct $W$ might continue to *different* next germs in $\mathrm{Obs}$. That would restore “agree on a finite interval, then diverge” as a statement about *leaving the patch*, not about forking one analytic curve in the interior.

Investigate. If it fails, report a theorem or a precise obstruction, not a vibe.

$P(O)$ is the maximal simply-connected real-analytic continuation of the germ (Thm B). It is an open 4-manifold (a Riemann domain), not in general a manifold with smooth boundary. “$\partial P$” means the edge of that domain: the geodesic $\sigma_O$ has no extension in $P(O)$. Write

$$
\tau_\partial
\;=\;
\sup\{\tau\ge 0:\ \sigma_O\text{ is defined in }P(O)\text{ on }[0,\tau]\}.
$$

The open lifetime in $P$ is $[0,\tau_\partial)$.

---

## 1. Theorem 6. Lifetime in $P(O)$ can be finite or infinite

**Theorem 6.** There exist germs $O$ with $\tau_\partial=\infty$, and germs with $\tau_\partial<\infty$. There is no theorem, from the locked object alone, that every hitchhiker meets $\partial P$ in finite proper time, nor that none do.

**Proof, both behaviours.**

*Infinite.* Let $O$ be the germ of Minkowski space at the origin, $u=\partial_t$. The maximal simply-connected continuation is Minkowski space itself (or an isometric copy). Geodesics are complete: $\tau_\partial=\infty$.

*Finite.* Hitchhiking is future-directed, so the example must be future-incomplete after maximality.

Kruskal–Schwarzschild, real-analytic for $r>0$, simply connected ($\mathbb{R}^2\times S^2$). Let $O$ be the germ at a regular point on a future-inextendible infalling radial timelike geodesic, $u$ along that geodesic. Maximality of $P(O)$ includes the coordinate horizon (Kruskal is the analytic extension through $r=2M$). It does not include $r=0$: curvature scalars blow up there, so they have no continuous, hence no real-analytic, limit. The geodesic meets $r=0$ in finite proper time. Thus $\tau_\partial<\infty$.

The cosmological twin, with the singularity in the *future*: spatially flat dust FLRW with a crunch,
$$
ds^2=-dt^2+(1-t)^{4/3}(dx^2+dy^2+dz^2),\qquad t<1.
$$
The scale factor $(1-t)^{2/3}$ is real-analytic on $(-\infty,1)$. Curvature scalars blow up as $t\to 1^-$. The germ at $(t,x)=(0,0)$ with $u=\partial_t$ has $P(O)$ this spacetime (up to unique pointed isometry). The comoving geodesic has $t=\tau$, so $\tau_\partial=1<\infty$. (Past-bang FLRW with $u$ future is future-complete; it is not this example.)

*Not an example.* A proper open subset of Minkowski (a “restricted Minkowski chart,” or Minkowski cut off by a fictitious edge). Theorem B continues that germ to all of Minkowski, and $\tau_\partial=\infty$. Restricted Minkowski after maximality contradicts maximality.

Analyticity of $g$ on an open set does not imply geodesic completeness: the geodesic ODE can run off $P(O)$ in finite proper time. FLRW and Kruskal are instances, not a classification. $\square$

So: meeting $\partial P$ is possible, not mandatory. If $\tau_\partial=\infty$, there is no boundary story; the interior theorems are the whole hitchhiking story for that $O$.

---

## 2. Theorem 7. No $\sim$-split of next germs among $E_\gamma$ members

Assume $\tau_\partial<\infty$.

**Theorem 7.** Let $[W,\iota],[W',\iota']\in E_\gamma(O)$. Write $\gamma=\pi_W(\sigma)$ and $\gamma'=\pi_{W'}(\sigma')$ for the geodesic lifts of $O$ in those spacetimes.

1. *(Shared prefix.)* $\gamma$ and $\gamma'$ coincide with $\gamma_O$ on $[0,\tau_\partial)$.
2. *(Both extend.)* If both geodesics extend as real-analytic geodesics through $\tau_\partial$ — i.e. are defined on $[0,\tau_\partial+\delta)$ in $W$ and in $W'$ for some $\delta>0$ — then $\gamma=\gamma'$ on $[0,\tau_\partial+\delta)$. In particular they determine the *same* next germs in $\mathrm{Obs}$. Distinct $E_\gamma$ members do not disagree.
3. *(One extends.)* If one extends and the other does not, there is a single continuation of the elementary object, not two disagreeing ones. The extender is a proper extension of the curvelet, not a second $\sim$-branch. Prefixes are earlier nodes of the same history.
4. *(Neither extends.)* There is no next germ in $\mathrm{Obs}$ from these lifts. Incompleteness, not a split.

**Proof of (1).** $E_\gamma$ is defined so the lifts coincide with $\gamma_O$ near $0$. Theorem 3 makes each lift analytic on its lifetime in that $W$. Theorem 2 spreads agreement from a positive-length prefix through the connected interval $[0,\tau_\partial)$. Prop. 3.2 identifies that common restriction with $\gamma_O$. $\square$

**Proof of (2).** If both extend, Theorem 3 supplies analyticity of $\gamma$ and of $\gamma'$ on an interval $I=[0,\tau_\partial+\delta)$ that *contains* $\tau_\partial$. They already agree on $[0,\tau_\partial)$, a subset of $I$ with accumulation point $\tau_\partial\in I$. Theorem 2 gives $\gamma=\gamma'$ on $I$. $\square$

**Proof of (3)–(4).** Immediate from (2) and the meaning of $\tau_\partial$. $\square$

**Corollary 7.1.** “Agree on $[0,\tau_\partial)$, then diverge as distinct next jets in $\mathrm{Obs}$” does not occur among analytic geodesic lifts of $E_\gamma$ members. The attempted restoration of a delayed split as a statement about leaving the patch fails.

This is compatible with Theorem 2, not an exception to it. A split of next germs would require two analytic lifts defined through $\tau_\partial$ that disagree after. Theorem 2 forbids that once they share $[0,\tau_\partial)$. Concatenating two different analytic pieces at $\tau_\partial$ would be a non-analytic curve in $\mathrm{Obs}$, which analytic $W$ do not produce (Theorem 3).

---

## 3. Why extra topology does not sneak a second germ through the glue

**Proposition 7.2 (quotients do not lengthen past the cover).** Let $P=P(O)$ and let $W$ be a quotient of a domain in $P$ by a discrete group of analytic isometries. Geodesics in $W$ lift to geodesics in $P$. Therefore $W$ cannot continue $\sigma_O$ to a proper time larger than $\tau_\partial$. Extra topology of this kind shortens or closes geodesics; it does not push the hitchhiker past $\partial P$ into a new germ.

**Proposition 7.3 (analytic hypersurface gluing).** Suppose $W$ is real-analytic and contains an isometric copy of $P$, and $\sigma$ reaches an analytic hypersurface $S\subset W$ at $\tau_\partial$, with $P$ on one side. Two real-analytic Lorentzian metrics that agree on an open set on one side of $S$ and agree to infinite order on $S$ agree on a neighbourhood of $S$ (identity theorem in a chart that crosses $S$). Therefore one cannot attach a *different* analytic metric across $S$ and remain in the locked category. Unique continuation, not a choice of next jet.

If the glue is not analytic — $W$ only $C^k$ across $S$ — then $W$ is not a locked spacetime. That route is a change of object.

**Proposition 7.4 (maximality).** $P(O)$ already includes every simply-connected analytic continuation of the germ (Thm B). A larger simply-connected analytic piece along $\sigma_O$ would contradict maximality. The only candidates for “more $W$” at the edge are non-simply-connected extensions or incomplete endings. Non-simply-connected extensions that remain analytic along the geodesic are already covered by Theorem 7(2): they share next germs. They are ensemble labels, not extra curves in $\mathrm{Obs}$.

---

## 4. What “$\partial P$” can be, without a split

When $\tau_\partial<\infty$, the edge is one of:

- a *natural boundary* of analytic continuation (the jet coefficients of $g$ along $\sigma_O$ fail to have an analytic limit);
- geodesic incompleteness with curvature or Christoffel blow-up;
- the geodesic leaving every compact subset of $P$ without a limit point in $P$.

In all three, either no next germ exists, or the next germ is unique among analytic geodesic extensions. None of these is a $\sim$-branching of $E_\gamma$ members.

EKT 1991 remains global classical non-uniqueness in a fixed $W$ with wormholes/CTCs, not local ODE branching at a regular point of $\partial P$, and not $\Phi$.

---

## 5. Open

- For which germs is $\tau_\partial<\infty$? No classification.
- The geometric structure of $\partial P$: natural boundary vs incomplete end vs Cauchy-type horizon, in the analytic category.
- Geodesic completeness of $P(O)$ as a Lorentzian manifold.
- Gauge, still open.
- Countability of distinct evolutions, still not supplied. This note does not invent a typicality set at $\partial P$.

---

## 6. Report line

- **Proved.** Theorem 6: $\tau_\partial$ may be finite or infinite; both occur. Theorem 7: no $\sim$-split of next germs among $E_\gamma$ members at $\partial P$. If both extend analytically, they share the continuation; if not, there is at most one continuation, or none. Props. 7.2–7.4: quotients do not lengthen past the cover; analytic gluing does not produce a second germ; maximality already ate simply-connected extra.
- **Killed.** Restoring “agree on a finite interval, then diverge” as disagreeing jets at the patch edge, for analytic geodesic lifts in analytic $W$. The hitchhiker story is dead at the boundary too. Restricted Minkowski as a finite-lifetime example (contradicts maximality).
- **Open.** Which germs meet $\partial P$ in finite time; the nature of that edge.
- **Not done.** $\Phi$; Born; a replacement count; a complexity bound.

---

## References

Hawking, S. W. and Ellis, G. F. R. *The Large Scale Structure of Space-Time.* Cambridge, 1973. (FLRW and Schwarzschild incompleteness.)

Krantz, S. G. and Parks, H. R. *A Primer of Real Analytic Functions.* 2nd ed. Birkhäuser, 2002.

Strayhorn, D. Theorem: the simply-connected analytic patch from an infinite jet. `papers/analytic-patch-from-jet.md`.

Strayhorn, D. Geodesic lifts are analytic curves in observer space. `papers/geodesic-lifts.md`.

Strayhorn, D. The ensemble $E(O)$ as a labeled object. `papers/ensemble-labels.md`.

Strayhorn, D. Analyticity and the split. `papers/analytic-split.md`.
