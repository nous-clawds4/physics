# $\mathrm{Obs}$ as a space?

David Strayhorn

Proposition 13: a neighborhood-law for type-(ii) $R$ needs $\mathrm{Obs}$ as a space. This note asks whether a topology (or uniformity) on presentations descends through $\sim_L$ to $\mathrm{Obs}=\mathcal{P}/{\sim_L}$. Do not close gauge by fiat. Do not identify $\mathrm{Obs}$ with Gielen–Wise. Do not write $R$. Do not put $1/N$. Do not lock a grain. Do not declare $\mathrm{Obs}$ an analytic manifold.

Companions: `papers/obs-as-a-set.md`, `papers/geodesic-lifts.md`, `papers/type-ii-adopted.md`.

**Status.** Partial. The inverse-limit topology already used for analytic *curves* (Theorem 3) does not, as a formal-Fréchet topology on all presentations, automatically give a Hausdorff quotient by $\sim_L$. A Fermi-coordinate slice, residual compact $O(3)$, does descend: neighborhoods of lumps exist. A neighborhood-law for $R$ is then *stateable* and is not written. Gauge as a named home (Gielen–Wise, a jet bundle of a fixed $W$) stays open.

---

## 0. What is being asked

Theorem 10: $\mathrm{Obs}$ is a set of lumps. Theorem 3: a map $I\to\mathrm{Obs}$ is an analytic curve when each projection to $J^k$ is analytic, i.e. as a map into the inverse limit of finite jet spaces (a Fréchet space of jets). That is a statement about *curves*, not an atlas on $\mathrm{Obs}$.

A neighborhood-law for $R$ would say: type-(ii) edges only (or at least) to lumps in a neighborhood of $O$. That sentence needs open sets on $\mathrm{Obs}$.

---

## 1. Candidate topology on presentations

Let $\mathcal{P}$ be the set of coordinate presentations at $0\in\mathbb{R}^4$ (Theorem 10). Write $J^k$ for $k$-jets of symmetric $2$-tensors at $0$, plus the $0$-jet of $u$. The inverse limit
$$
J^\infty\;=\;\varprojlim_k J^k
$$
is a Fréchet space. $\mathcal{P}$ sits in $J^\infty$ as those jets that are real-analytic and Lorentzian with future unit $u$.

**Proposition 14 (analytic jets are not a Fréchet-closed subset).** Polynomial (hence analytic) jets are dense in $J^\infty$. The subset of convergent Lorentzian jets is therefore not closed in the inverse-limit topology, and is not itself a Fréchet space in the subspace topology. Borel’s lemma is the $C^\infty$ companion: every formal series is some $C^\infty$ jet; the analytic ones are a thin subset.

So the topology Theorem 3 used for *curves* is the inverse-limit topology along a path of jets. Using the same Fréchet structure as a topology *on $\mathcal{P}$* is already a mismatch: $\mathcal{P}$ is an inductive-limit-type subset (union over radii of convergence), not a closed Fréchet subspace.

The honest analytic topology on germs is the inductive limit, over $r>0$, of Banach spaces of holomorphic extensions to a complex ball of radius $r$. That is a locally convex topology on $\mathcal{P}$, not Fréchet. Theorem 3 is compatible with either: analyticity of each $J^k$-projection still makes sense.

---

## 2. Does $\sim_L$ descend from the formal Fréchet topology?

$\sim_L$ is orbit equivalence under pointed analytic diffeomorphism-germs of $(\mathbb{R}^4,0)$ sending $u$ to $u'$ (Definition 6). Write $G$ for that group.

**Proposition 15 (formal quotient is not known to be Hausdorff).** The relation $\sim_L\subset\mathcal{P}\times\mathcal{P}$ need not be closed in the subspace topology from $J^\infty\times J^\infty$. $G$ is a group of *analytic* germs. A sequence of pairs identified by $\varphi_n\in G$ may converge in the inverse-limit topology to a pair identified only by a $C^\infty$ (non-analytic) diffeomorphism-germ, or by nothing analytic. In that case the quotient $J^\infty$-topology on $\mathcal{P}/{\sim_L}$ fails to be Hausdorff, or else the limit point leaves $\mathcal{P}$. This is the same rigidity that closed $C^\infty$ as an object (Borel): the formal topology sees too many jets.

Truncation $T_d$ already failed to commute with coordinate change (`papers/grain-candidates.md`). That is a *grain* map not descending. It is consistent with, not a proof of, Proposition 15. It is not a topology on $\mathrm{Obs}$.

**Do not take the formal-Fréchet quotient as $\mathrm{Obs}$ as a space.** Gauge is not closed that way.

---

## 3. A slice that does descend

Fermi coordinates along $u$ (Theorem 3, Manasse–Misner) put each germ in a normal form: $g(0)=\eta$, the geodesic in direction $u$ is the $x^0$-axis, spatial frame Fermi–Walker transported. Residual freedom after that is rotations of the spatial triad: compact $O(3)$.

Riemann normal coordinates give another slice, same residual $O(3)$ if $u$ is fixed.

**Theorem 16.** Let $\mathcal{P}_F\subset\mathcal{P}$ be presentations already in Fermi coordinates for their $u$. The restriction of $\sim_L$ to $\mathcal{P}_F$ is the $O(3)$-action on the spatial frame. $O(3)$ is compact and acts continuously on $\mathcal{P}_F$ in the inverse-limit topology (and in the analytic inductive-limit topology). The quotient $\mathcal{P}_F/O(3)$ is therefore Hausdorff whenever $\mathcal{P}_F$ is. Every $\sim_L$-class meets $\mathcal{P}_F$ (exponential / Fermi chart of an analytic metric germ exists in a neighbourhood of $0$). Hence $\mathrm{Obs}$ is in bijection with $\mathcal{P}_F/O(3)$, and the quotient topology on that slice is a well-defined Hausdorff topology on the set of lumps.

**Proof.** Existence of Fermi coordinates for an analytic timelike geodesic germ is Theorem 3, Step 2, at $\tau=0$. Uniqueness up to $O(3)$: the Fermi frame is an orthonormal spatial triad in $u^\perp$, and any two such triads differ by $O(3)$. Compact group, continuous linear action on each $J^k$ (rotating tensor indices), hence continuous on the inverse limit. Compact Hausdorff group acting continuously on a Hausdorff space: the orbit space is Hausdorff. The bijection with $\mathrm{Obs}$ is Theorem 10 plus the slice meeting every class. $\square$

Call this the *Fermi-slice topology* on $\mathrm{Obs}$. Neighborhoods of lumps exist. It is not an analytic-manifold atlas. It is not Gielen–Wise’s $7$-manifold of $4$-velocities on a fixed $W$ (that object needs a $W$ first; lumps do not).

The exponential/Fermi construction is continuous in the analytic topology on germs: nearby analytic metrics give nearby Fermi presentations (the Fermi–Walker ODE and the exponential map depend analytically on $g$). So the slice topology is the descent of the *analytic* topology on presentations, not of the formal Fréchet topology on all of $J^\infty$.

---

## 4. What this does and does not license

**Stateable, not written.** One may now say “a neighborhood of $O$ in $\mathrm{Obs}$” using the Fermi-slice topology. A neighborhood-law for type-(ii) $R$ is therefore a possible sentence. It is not adopted. $R$ is not written. $1/N$ is not written.

**Not a closing of gauge.** Gauge as a *named home* — Gielen–Wise, a frame bundle, a jet bundle of a completed $W$ — stays open. A topology on the set of lumps is not an identification of $\mathrm{Obs}$ with one of those spaces.

**Not a grain.** Open balls in the Fermi-slice topology are not a discrete vertex-set. $d$-decimal still does not descend. Grain stays open.

**Not $\Phi$.** Existence of open sets does not choose edges.

---

## 5. Report line

- **Partial.** Formal-Fréchet topology on all presentations does not give a known Hausdorff quotient by $\sim_L$ (Proposition 15; analytic jets not closed, Proposition 14). Fermi-slice $/O(3)$ does descend (Theorem 16): neighborhoods of lumps exist.
- **Stateable, not adopted.** A neighborhood-law for $R$. Not written.
- **Killed.** Closing gauge by taking $\mathrm{Obs}$ to be Gielen–Wise, or the formal-Fréchet quotient of all jets. Treating $T_d$ as a topology.
- **Open.** Gauge as a named space; the law for $R$; grain; $1/N$.

---

## References

Manasse, F. K. and Misner, C. W. Fermi normal coordinates and some basic concepts in differential geometry. *Journal of Mathematical Physics* 4 (1963) 735–745.

Strayhorn, D. Geodesic lifts are analytic curves in observer space. `papers/geodesic-lifts.md`.

Strayhorn, D. $\mathrm{Obs}$ as a set. `papers/obs-as-a-set.md`.

Strayhorn, D. Type-(ii) links, adopted as working motion. `papers/type-ii-adopted.md`.
