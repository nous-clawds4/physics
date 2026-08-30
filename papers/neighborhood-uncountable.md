# Neighborhoods are not a countable $N$

David Strayhorn

Fermi-slice neighborhoods (Theorem 16) make a neighborhood-law for type-(ii) $R$ *stateable*. They do not make the set of type-(ii) successors countable. Do not adopt a neighborhood-law. Do not write $R$. Do not put $1/N$. Do not lock a grain.

Companions: `papers/obs-as-a-space.md`, `papers/type-ii-adopted.md`, `papers/typicality-under-the-lock.md`.

**Status.** Theorem 17: an open ball about $O$ in the Fermi-slice topology, minus the curvelet $\gamma_O$, is uncountable. Any neighborhood-law whose allowed targets include an open set of lumps therefore supplies a continuum of type-(ii) candidates, not a finite $N$. Countability of evolutions still needs a grain, or some other discrete cut. Neighborhoods unblock stateability of a law, not the 2008 typicality job.

---

## 1. Theorem 17. Open balls are continua

Let $\mathrm{Obs}$ carry the Fermi-slice topology (Theorem 16). Let $O\in\mathrm{Obs}$, and let $\gamma_O$ be its geodesic curvelet (Prop. 3.2), image a subset of $\mathrm{Obs}$.

**Theorem 17.** Every nonempty open set $U\subset\mathrm{Obs}$ containing $O$ contains uncountably many lumps not on $\gamma_O$. In particular $U\setminus\gamma_O([0,\tau_\partial))$ is uncountable.

**Proof.** Fermi presentations: $g(0)=\eta$, geodesic in direction $u$ along $x^0$, spatial frame defined up to $O(3)$. A basic open set in the inverse-limit topology specifies, for some finite $k$ and $\varepsilon>0$, that the $k$-jet lie in an $\varepsilon$-ball. In particular it contains all germs whose $2$-jet is sufficiently close to that of $O$ and whose higher jets may be chosen analytic.

The vector space of algebraic curvature tensors on $\mathbb{R}^{1,3}$ (Riemann symmetries) is positive-dimensional. The $O(3)$ action on $u^\perp$ has compact orbits, so the space of $2$-jets of Fermi presentations, modulo $O(3)$, still contains a continuum: already a one-parameter family of $O(3)$-inequivalent curvature tensors exists (e.g. vary one independent sectional curvature in a small interval).

Each such $2$-jet is realized by an analytic metric germ: in Fermi coordinates take
$$
g_{\mu\nu}(x)=\eta_{\mu\nu}+h_{\mu\nu\rho\sigma}x^\rho x^\sigma
$$
with $h$ small, encoding that curvature tensor, and vanishing of the linear term (Christoffel at $0$ already zero in Fermi form). For $\lvert h\rvert$ small, $g$ is Lorentzian and real-analytic on a ball. Distinct $O(3)$-invariants of $h$ give distinct $\sim_L$-classes (Theorem 10). These classes all lie in $U$ for $h$ small enough.

The image $\gamma_O([0,\tau_\partial))$ is the continuous image of an interval, hence separable and a countable union of compact metrizable curves. It cannot contain a nonempty open set of a space that has a continuum of distinct $2$-jets in every ball (an open set in the Fermi-slice topology meets infinitely many $J^2$-classes). Removing it leaves a continuum. $\square$

The locked object is any real-analytic Lorentzian germ, not an Einstein germ. Restricting to vacuum would be a new cut; even then one should not assume without proof that nearby vacuum germs are discrete. The theorem is for the locked object.

---

## 2. Neighborhood-laws do not supply finite $N$

A *neighborhood-law* would be a rule that includes, among type-(ii) targets of $O$, all lumps in some nonempty open $U\ni O$ (or an open subset of $U\setminus\gamma_O$). By Theorem 17 that set of targets is uncountable.

Typicality over branches from one $O$, and any $1/N$ at a vertex, need a countable (resp. finite) set of successors. A neighborhood-law does not provide one. Putting $1/N$ on a continuum is not a rule we have, and it is not written.

This does not forbid a neighborhood-law as a *constraint* (targets must lie in $U$, plus a further discrete cut). The further cut is a grain, or something else not yet adopted. Neighborhoods alone are not that cut.

---

## 3. What neighborhoods did unblock

Proposition 13: locked data at $O$ do not determine type-(ii) edges; a neighborhood-law was not even stateable while $\mathrm{Obs}$ was only a set. Theorem 16: Fermi-slice neighborhoods exist. Theorem 17: they do not count.

Stateability of a law $\ne$ the 2008 typicality job. Unique-measure stays conditional on a hypothesis that supplies a countable set of distinct evolutions. Grain remains open. $d$-decimal is still not put in by hand. Engulfing-in-$P(O)$ is still not type (ii).

Do not adopt a neighborhood-law here. Do not write $R$.

---

## 4. Report line

- **Proved.** Theorem 17: Fermi-slice open balls minus $\gamma_O$ are uncountable. Neighborhood-laws that include an open set of targets supply a continuum, not a finite $N$.
- **Not adopted.** A neighborhood-law. $R$. $1/N$. A grain.
- **Open.** Grain, or any other discrete cut that could make successors countable. The 2008 typicality job still needs that cut.

---

## References

Strayhorn, D. $\mathrm{Obs}$ as a space? `papers/obs-as-a-space.md`.

Strayhorn, D. Type-(ii) links, adopted as working motion. `papers/type-ii-adopted.md`.

Strayhorn, D. Typicality under the lock. `papers/typicality-under-the-lock.md`.
