# The ensemble $E(O)$ as a labeled object

David Strayhorn

What $E(O)$ is, how it is labeled, what is constant along a geodesic lift, and what countability would take. Locked object unchanged. $\Phi$ is not written. Born is not derived. $E(O)$ is not folded into $\sim$. Gauge is still open. $\mathrm{Obs}$ is not declared non-analytic.

Companions: `papers/cheat-sheet.md`, `papers/analytic-patch-from-jet.md`, `papers/analytic-split.md`, `papers/geodesic-lifts.md`.

**Status.**

- **Theorem.** $E(O)$ is the set of pointed analytic occurrences of the germ $O$ (Definition 1), a set once $W$ is second-countable. Two ensembles are not one: the hitchhiking ensemble along the unique curvelet $\gamma_O$ is locally constant in the interior of $P(O)$; the fiber $E(\,\cdot\,)$ over a moving point of $\mathrm{Obs}$ can jump off that curvelet (Theorem 4). Topology labels are discrete, so a membership change is a jump.
- **Theorem (inherited).** Unique curvelet from one $O$, not a star; delayed local fork of analytic geodesic lifts killed; $E$ locally invisible along the curvelet (`papers/geodesic-lifts.md`, Theorem 3, Cor. 3.1, Prop. 3.2).
- **Killed.** A complete census of 4-manifold topologies as a way to list $E(O)$. Folding $E(O)$ into $\sim$. Using $|a|^2$ as $M$. Compact Lorentzian $S^4$. Conflating Freedman with Donaldson with analytic Lorentzian $W$. Treating “every $W$ containing this germ” as a continuous motion of topologies along $\gamma_O$.
- **Open.** Countability of $E(O)$. A classifying complete label. Whether exotic $\mathbb{R}^4$’s enter $E(O)$. $\Phi$. Unique measure, which stays conditional on countability.

---

## 0. Locked starting point

Elementary observer $O=(j_\infty,u)$, equivalently the unique simply-connected real-analytic patch $P(O)$. Extra topologies are the ensemble, not a second observer. Realized paths are geodesic lifts: one $\gamma$, many $W$ in $E(O)$. That geodesic law is the motion stand-in, not $\Phi$.

Along that geodesic, in the interior of $P(O)$, the hitchhiker’s members persist. Abstract $E(O)$ as “every $W$ containing this germ” is a different assignment at each point of $\mathrm{Obs}$ and can jump off the curvelet. Those two must be distinguished.

---

## 1. Definition. $E(O)$ is a set of pointed occurrences

Assume throughout that a spacetime $W$ is a connected, Hausdorff, second-countable, real-analytic Lorentzian 4-manifold, time-orientable. Second-countability makes isomorphism classes a set, not a proper class.

**Definition 1 (occurrence).** An *occurrence* of $O$ in $W$ is a real-analytic isometric embedding
$\iota\colon U\to W$,
where $U\subset P(O)$ is a neighbourhood of the basepoint $p$ of $P(O)$, such that $\iota_*u$ is future unit timelike in $W$. Write $\iota(O)$ for this pointed germ in $W$.

**Definition 2 (the ensemble).** $E(O)$ is the set of equivalence classes of pairs $(W,\iota)$, where $\iota$ is an occurrence of $O$ in $W$. Two pairs are equivalent if there is a pointed real-analytic isometry $W\to W'$ carrying $\iota$ to $\iota'$ on a neighbourhood of $p$.

If a single $W$ admits $M$ inequivalent occurrences of $O$, that $W$ contributes $M$ classes to $E(O)$. That integer is the *multiplicity* $M(W,O)$. It is not $|a|^2$. It does not enter $\sim$.

This is the labeled object. A label of a class $[W,\iota]$ is any invariant of that class. Candidate labels, none complete:

| Label | What it records | What it is not |
|---|---|---|
| $\iota$ | Which occurrence, as a pointed embedding of the germ | A second elementary observer |
| $M(W,O)$ | How many times the germ sits in that $W$ | Born weight |
| $\pi_1(W)$ | Topology attached away from the simply-connected patch, up to isomorphism of groups | A classifying invariant; an algorithm (Markov) |
| Intersection form | Unimodular form on $H_2$, when $W$ is closed oriented | Available for EKT-style noncompact $W$; a smooth classification |

$\sim$ compares curves in $\mathrm{Obs}$. $E(O)$ is not a quotient of $\mathrm{Obs}$ and is not folded into $\sim$.

---

## 2. Analytic rigidity, then topology away from $P(O)$

On a connected simply-connected real-analytic patch, the germ determines the metric (Theorems A–B of `papers/analytic-patch-from-jet.md`). Ensemble members are therefore *not* a moduli space of metrics on $P(O)$. They are ways of continuing or covering beyond $P(O)$: monodromy, quotients of the maximal simply-connected continuation when isometries exist, and pointed embeddings of $P(O)$ into larger analytic $W$.

Topologically, if $P(O)$ is a 4-ball and $W$ is obtained by attaching the rest of the manifold along $\partial P\simeq S^3$, van Kampen gives $\pi_1(W)$ from the attached piece. That is the right picture for *underlying manifolds*: topology lives away from the simply-connected patch.

It is not a free construction of analytic $g$. An analytic metric on a glueing must match the germ on an overlap. Arbitrary topological attachment need not extend $j_\infty$ as a real-analytic Lorentzian metric. The operations that *do* stay inside the locked analytic category are continuation along paths (with monodromy when $\pi_1\neq 0$) and pointed analytic isometries. The “attach anything” slogan is a topological hunch, not an analytic existence theorem. It is not used as one.

---

## 3. Theorem 4. Two ensembles, not one

Let $\gamma_O=\pi_{P(O)}(\sigma_O)$ be the unique geodesic curvelet of $O$ (`papers/geodesic-lifts.md`, Prop. 3.2). For $\tau$ in the interior lifetime of $\sigma_O$ in $P(O)$, write $O_\tau=\gamma_O(\tau)$.

**Definition 3 (hitchhiking ensemble along the curvelet).**
$E_\gamma(O)\;:=\;\bigl\{[W,\iota]\in E(O):\ \pi_W(\sigma)\ \text{coincides with }\gamma_O\text{ on a neighbourhood of }0\text{ in }\tau\bigr\}$.
These are the members that actually hitchhike with the realized path.

**Definition 4 (fiber over a point of $\mathrm{Obs}$).**
$E_{\mathrm{pt}}(O')\;:=\;E(O')$
as in Definition 2, for each $O'\in\mathrm{Obs}$. This is an assignment of a set of pointed $W$ to each germ, whether or not that germ lies on $\gamma_O$.

**Theorem 4.**

1. *(Persistence along the curvelet.)* If $[W,\iota]\in E_\gamma(O)$, then for every $\tau$ in the interior of the lifetime of $\sigma_O$ in $P(O)$, the same $W$ contains $O_\tau$ (the jet of $g_W$ at $\sigma_O(\tau)$). Thus $E_\gamma(O)$ injects into $E_{\mathrm{pt}}(O_\tau)$, and the hitchhiking members persist. Topology labels of those members do not move: they are discrete invariants of $W$, constant along $\gamma_O$ while $\sigma_O$ remains in $P(O)$.

2. *(Jump, not continuous motion.)* There is no continuous motion of topology labels along $\gamma_O$. A change of membership in $E_\gamma$ is a jump: some $[W,\iota]$ appears or disappears. It cannot be a path in a moduli space of $\pi_1$ or of diffeomorphism types, because those labels are discrete.

3. *(The fiber can jump off the curvelet.)* $E_{\mathrm{pt}}(O')$ for $O'$ not on $\gamma_O$ is a different set. A spacetime that contains the germ $O$ need not contain a neighbouring germ off the curvelet. So the assignment $O'\mapsto E_{\mathrm{pt}}(O')$ can jump as $O'$ moves in $\mathrm{Obs}$, even while $E_\gamma(O)$ is constant along $\gamma_O$. These are not the same object.

**Proof of (1).** $P(O)$ is a neighbourhood of the whole short geodesic $\sigma_O$ (Prop. 3.2). An occurrence $\iota$ embeds a neighbourhood of $p$ isometrically into $W$; analytic continuation along $\sigma_O$ inside $P(O)$ is unique, so $\iota$ extends along that segment and $W$ contains every $O_\tau$. Labels of $W$ do not depend on $\tau$. $\square$

**Proof of (2).** $\pi_1(W)$, diffeomorphism type, and $M(W,O)$ take values in discrete spaces (groups up to isomorphism, integers, combinatorial types). A continuous family of such labels that actually changes must jump. $\square$

**Proof of (3).** Take a germ $O'$ at a point of $P(O)$ off the geodesic, or a germ not realized by $P(O)$ at all. Containment of $O$ does not imply containment of $O'$. Distinct fibers. $\square$

Local invisibility (`papers/geodesic-lifts.md`, Cor. 3.1) is (1) in observer-space language: along $\gamma_O$, the hitchhiker does not see which member of $E_\gamma(O)$ they are in. Persistence of members is compatible with invisibility of labels.

---

## 4. What a census cannot be

**Theorem 5 (no complete census).** There is no algorithm that, given finite presentations of two closed 4-manifolds, decides whether they are homeomorphic (Markov 1958). Every finitely presented group is $\pi_1$ of some closed smooth 4-manifold (standard, dimension $\ge 4$). Therefore $\pi_1$ as a label does not yield a computable classification of $E(O)$, and there is no complete census of 4-manifold topologies to list ensemble members by.

This is a no-go for *listing by topology*. It is not a proof that $E(O)$ is infinite, and it is not a proof that $E(O)$ is uncountable.

**Compact Lorentzian constraint.** A compact manifold admits a Lorentzian metric if and only if it admits a nowhere-vanishing vector field, hence if and only if $\chi=0$ in the closed case (Poincaré–Hopf). So $S^4$ ($\chi=2$) is out, as is $\mathbb{CP}^2$ ($\chi=3$). Closed ensemble members, if any, live in the $\chi=0$ class ($T^4$, $S^1\times S^3$, $S^1\times S^1\times S^2$, \ldots). EKT-style wormhole spacetimes are noncompact; noncompact manifolds always admit Lorentzian metrics.

**Freedman is not Donaldson is not analytic Lorentzian.** Freedman classified simply-connected *closed topological* 4-manifolds by intersection form plus Kirby–Siebenmann invariant. Donaldson constrains which forms are realized *smoothly*. Neither is a classification of pointed real-analytic Lorentzian $W$ containing a germ. Intersection form is not even defined as a complete invariant for the noncompact EKT-style case. Do not quote Freedman’s list as a census of $E(O)$.

**Exotic $\mathbb{R}^4$.** There are uncountably many diffeomorphism types of smooth manifolds homeomorphic to $\mathbb{R}^4$ (Taubes 1987). That kills casual countability of *smooth types of noncompact 4-manifolds*. It does **not** place those types in $E(O)$. Membership in $E(O)$ requires a real-analytic Lorentzian metric and an occurrence of the germ. Whether any exotic $\mathbb{R}^4$ admits that is open. They are recorded as a reason not to assume countability in the noncompact smooth category, not as ensemble members.

---

## 5. Countability is open

**Proposition 5.1.** Countability of $E(O)$ is not a theorem of the locked object.

Reasons, none of which is a proof of uncountability of $E(O)$ either:

- Compact combinatorial types (finite triangulations, finite handlebodies) form a countable set, but are not classified, and compact Lorentzian is already $\chi=0$.
- Noncompact smooth types are not known to be countable (exotic $\mathbb{R}^4$).
- Analytic isometric classes of metrics can a priori be as large as the continuum (Taylor data of transition functions), even after rigidity on $P(O)$.
- A full census is impossible (Theorem 5).

**What would count as countability.** An explicit bound that cuts $E(O)$ down to a countable set of labels, with each label realized by finitely many (or countably many) classes, *without* using $|a|^2$ and *without* folding into $\sim$. The only realistic path in sight is a bound on presentation complexity (generators and relators of $\pi_1$, number of handles, a compact core of bounded complexity), or some other named finiteness. That bound is not locked. Until it is proved, Paper 1’s unique-measure claim remains conditional on countability of distinct *evolutions*. Countability of $E(O)$ is not that count: ensemble members are not extra elementary observers, and along $\gamma_O$ they are not even extra curves in $\mathrm{Obs}$.

Typicality cannot be a count of delayed $\mathrm{Obs}$-branches (`papers/geodesic-lifts.md`). It also cannot be an uncountable census of topologies. If a later typicality statement uses $E(O)$, it needs the bound of the previous paragraph first.

---

## 6. What this does not do

It does not write $\Phi$. It does not reconstruct a unique $W$ from $O$. It does not fold $E(O)$ into $\sim$. It does not derive the Born rule. It does not declare $\mathrm{Obs}$ non-analytic. Gauge is still open. The unique curvelet from one $O$ is untouched.

---

## 7. Report line

- **Object.** $E(O)=$ pointed analytic occurrences of the germ, modulo pointed analytic isometry; $M$ counts occurrences in one $W$.
- **Proved.** Theorem 4: hitchhiking ensemble persists and is locally constant along $\gamma_O$ in $\mathrm{int}\,P(O)$; membership changes by jumps; the fiber $E_{\mathrm{pt}}(\,\cdot\,)$ can jump off the curvelet. Theorem 5: no complete topological census (Markov). Compact Lorentzian $\Rightarrow\chi=0$; $S^4$ out.
- **Killed.** Census-as-list; $E(O)$ as extra observers; $|a|^2$ as $M$; Freedman/Donaldson as a census of analytic Lorentzian $W$; continuous motion of topologies along $\gamma_O$.
- **Open.** Countability of $E(O)$; a complete label; exotic $\mathbb{R}^4$ in $E(O)$; the presentation-complexity bound that would make unique measure more than conditional.

---

## References

Donaldson, S. K. An application of gauge theory to four-dimensional topology. *Journal of Differential Geometry* 18 (1983) 279--315.

Freedman, M. H. The topology of four-dimensional manifolds. *Journal of Differential Geometry* 17 (1982) 357--453.

Markov, A. A. Insolubility of the problem of homeomorphy. *Proc. Internat. Congress Math.* 1958, 300--306. (Homeomorphism problem for $n\ge 4$.)

Taubes, C. H. Gauge theory on asymptotically periodic 4-manifolds. *Journal of Differential Geometry* 25 (1987) 363--430. (Uncountably many exotic $\mathbb{R}^4$’s.)

Strayhorn, D. Geodesic lifts are analytic curves in observer space. `papers/geodesic-lifts.md`.

Strayhorn, D. Cheat sheet: names and symbols. `papers/cheat-sheet.md`.
