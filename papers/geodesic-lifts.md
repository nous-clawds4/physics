# Geodesic lifts are analytic curves in observer space

David Strayhorn

Locked starting point: $W$ is real-analytic; observers follow geodesics. This note proves that the mapping $\pi_W$ sends those geodesics to real-analytic curves in $\mathrm{Obs}$, and records what that kills. It does not declare $\mathrm{Obs}$ non-analytic. It does not change the locked object. It does not write $\Phi$. It does not derive the Born rule.

Companion: `papers/cheat-sheet.md`, `papers/analytic-split.md`, `papers/analytic-patch-from-jet.md`.

**Status.** Proved: a geodesic in a real-analytic $W$ lifts to a real-analytic curve in $\mathrm{Obs}$ (Theorem 3). Corollary of Theorem 2: two such lifts that agree on a positive-length prefix are the same curve wherever both remain analytic. Delayed local “knows which path” is killed. Multiplicity of $E(O)$ is locally invisible. From a single $O$, geodesic lifts do not form a star: the simply-connected patch determines a unique curvelet. What remains is one $\gamma$ with many $W$ in $E(O)$, and the general possibility (not realized by geodesic evolution of one $O$) of analytic curves that meet only at $\tau=0$. No branching analytic evolution with thick trunks. Typicality cannot be a count of delayed $\mathrm{Obs}$-branches.

---

## 0. What this is about

Analyticity of a *curve* $\gamma:I\to\mathrm{Obs}$ is a statement about a map of one real variable. It is not a statement that $\mathrm{Obs}$ is a real-analytic manifold. $\mathrm{Obs}$ may still be a Fréchet space of infinite jets (inverse limit of $J^k$), or some other locally convex space. A map into a Fréchet space can be real-analytic as a curve without that space having been given an analytic-manifold atlas.

`papers/analytic-split.md` already used Fermi coordinates as the meaning of “analytic curve in $\mathrm{Obs}$,” and stated that $\pi_W(\sigma)$ is such a curve. This note proves that claim, then applies Theorem 2.

---

## 1. Theorem 3. Geodesic lifts are real-analytic curves

Let $W$ be a real-analytic Lorentzian 4-manifold, $g$ its metric. Let $\sigma:I\to W$ be a geodesic, parameterized by proper time, with $g(\dot\sigma,\dot\sigma)=-1$. Let

$$
\gamma(\tau)
\;=\;
\pi_W(\sigma)(\tau)
\;=\;
\bigl(j_\infty\bigl(g,\sigma(\tau)\bigr),\;\dot\sigma(\tau)\bigr)
\in\mathrm{Obs}.
$$

**Theorem 3.** $\gamma:I\to\mathrm{Obs}$ is a real-analytic curve, in this sense: there exist Fermi coordinates along $\sigma$ in which every jet coefficient of $g$ at $\sigma(\tau)$, and every component of $\dot\sigma(\tau)$, is a real-analytic function of $\tau$ on $I$. Equivalently, each projection of $\gamma$ to a finite-order jet space $J^k$ is a real-analytic map $I\to J^k$, so $\gamma$ is real-analytic as a map into the inverse limit (a Fréchet space of jets). This does not require $\mathrm{Obs}$ to be a real-analytic manifold.

**Proof.**

*Step 1 (analytic ODE).* Where $g$ is real-analytic and nondegenerate, $g^{-1}$ is real-analytic, hence so are the Christoffel symbols $\Gamma^\lambda{}_{\mu\nu}$. The geodesic equation

$$
\ddot\sigma^\lambda+\Gamma^\lambda{}_{\mu\nu}(\sigma)\,\dot\sigma^\mu\dot\sigma^\nu=0
$$

is an autonomous real-analytic ODE on $TW$. A real-analytic vector field has a real-analytic flow: given real-analytic initial data $\bigl(\sigma(0),\dot\sigma(0)\bigr)$, there is a unique real-analytic solution on some interval, unique among $C^2$ solutions (standard analytic existence and uniqueness for ODEs; e.g. Dieudonné, *Foundations of Modern Analysis*, Ch. X). So $\sigma$ and $\dot\sigma$ are real-analytic $W$-valued and $TW$-valued maps of $\tau$.

*Step 2 (Fermi coordinates).* Along a timelike geodesic there exist Fermi coordinates $(x^0,x^1,x^2,x^3)$ with $x^0=\tau$ on $\sigma$ and $\sigma$ given by $x^i=0$ (Manasse and Misner 1963; Fermi 1922). If $g$ and $\sigma$ are real-analytic, the Fermi frame obtained by Fermi–Walker transport of an analytic orthonormal frame at $\sigma(0)$ is real-analytic in $\tau$, and the coordinate change is real-analytic on a tubular neighbourhood of $\sigma$. In those coordinates $g_{\mu\nu}(\tau,x)$ is real-analytic in $(\tau,x)$ on that tube.

*Step 3 (jet coefficients).* The infinite jet of $g$ at $\sigma(\tau)$ is, in Fermi coordinates, the collection

$$
\bigl(\partial_{x^{i_1}}\cdots\partial_{x^{i_m}} g_{\mu\nu}(\tau,0)\bigr)_{m\ge 0}.
$$

Each finite derivative of a real-analytic function of $(\tau,x)$, restricted to $x=0$, is real-analytic in $\tau$. The $0$-jet of $g$ at $\sigma(\tau)$ is Lorentzian, and $\dot\sigma(\tau)$ is future unit timelike, both analytic in $\tau$ by Step 1. Therefore every component of $\bigl(j_\infty(g,\sigma(\tau)),\dot\sigma(\tau)\bigr)$ is real-analytic in $\tau$.

*Step 4 (Fréchet, not a manifold claim).* The inverse limit $\varprojlim J^k$ carries a Fréchet topology. A map into the inverse limit is real-analytic if and only if each map into $J^k$ is. That is exactly Step 3. No analytic atlas on $\mathrm{Obs}$ is used. $\square$

Cauchy–Kovalevskaya is not used. The Einstein equation is not used. The data are an analytic metric and a geodesic of that metric.

---

## 2. Corollary. No delayed local “knows which path”

**Corollary 3.1** (Theorem 2 applied to geodesic lifts). Let $\sigma,\sigma'$ be geodesics in real-analytic spacetimes $W,W'$, with lifts $\gamma=\pi_W(\sigma)$ and $\gamma'=\pi_{W'}(\sigma')$. If $\gamma$ and $\gamma'$ agree on a subinterval of positive length, then they agree on every connected interval on which both remain defined (hence analytic). In particular they cannot agree on $[0,\tau_*]$ with $\tau_*>0$ and disagree at some later $\tau$ while both lifts are still analytic.

**Proof.** Theorem 3 puts both lifts in the hypothesis of Theorem 2 of `papers/analytic-split.md`. $\square$

**Delayed local “knows” is killed.** An observer who has followed a geodesic lift cannot, by looking at the elementary object $\bigl(j_\infty(\tau),u(\tau)\bigr)$ at a later time, discover which of two analytic lifts they were on, if those lifts agreed on a positive-length prefix. There are not two such lifts. First disagreement of $P$, if it ever happens between *analytic* geodesic lifts, cannot be postponed through a shared trunk of duration $\tau_*>0$.

**Multiplicity of $E(O)$ is locally invisible.** Distinct $(W,\iota)\in E(O)$ share the same germ $O$ at $\tau=0$. That is agreement at a point, which is not yet a prefix. But the germ determines more than a point: it determines the simply-connected patch $P(O)$ (`papers/analytic-patch-from-jet.md`, Theorems A–B). On $P(O)$, the geodesic with initial $u$ is unique (Step 1). The lift of that geodesic is a unique analytic curvelet $\gamma_O$, defined on a positive interval (the lifetime in $P$). Every $(W,\iota)\in E(O)$ whose geodesic starts at that occurrence therefore satisfies

$$
\pi_W(\sigma)\big|_{[0,\varepsilon)}
\;=\;
\gamma_O
$$

for some $\varepsilon>0$. Locally, $E(O)$ is many spacetimes and one curve in $\mathrm{Obs}$. Topology of $W$ does not show up in the germ along that curvelet. That is local invisibility of ensemble multiplicity.

---

## 3. From one $O$: not a star of geodesic lifts

Agreement at the single instant $\tau=0$ is not a positive-length prefix. Theorem 2 therefore *permits*, as a statement about analytic maps $I\to\mathrm{Obs}$, a star of distinct analytic curves through a common point $O$: they meet at $\tau=0$ and nowhere else in a neighbourhood. Isolated intersection is allowed; a thick trunk is not.

Geodesic lifts from a *fixed* elementary observer $O=(j_\infty,u)$ do not populate that star.

**Proposition 3.2.** Let $O=(j_\infty,u)$ with simply-connected patch $P(O)$. There is a unique geodesic $\sigma_O$ in $P(O)$ with that initial $(p,u)$, and a unique analytic curvelet $\gamma_O=\pi_{P(O)}(\sigma_O)$ in $\mathrm{Obs}$. Every geodesic lift of $O$ in every $W\in E(O)$ coincides with $\gamma_O$ on a common positive interval. In particular, geodesic evolution of one $O$ does not produce distinct analytic curves through $O$ that agree only at $\tau=0$.

**Proof.** Uniqueness of $\sigma_O$ is analytic ODE uniqueness on $P(O)$. Uniqueness of the germ of $g$ on $P(O)$ is Theorem A. The lift is Theorem 3. Local coincidence of all ensemble lifts is Corollary 3.1 plus the shared curvelet. $\square$

So:

- A *star* of analytic curves through $O$, agreeing only at $\tau=0$, is compatible with Theorem 2 and is *not* produced by geodesic hitchhiking from that $O$. Producing it would be a different evolution law. That law is not written here.
- *One $\gamma$, many $W$ in $E(O)$* is what geodesic hitchhiking from one $O$ does produce.
- *No branching analytic evolution with thick trunks* is forced: an analytic $\Phi$, if it were later taken to have analytic solution curves in $\mathrm{Obs}$, cannot branch after a shared prefix of length $\tau_*>0$. $\Phi$ is not written.

---

## 4. What we can say about $\mathrm{Obs}$ (and what we are not forced to say)

We are **not** forced to say that $\mathrm{Obs}$ as a space is non-analytic. Nothing in Theorems 2–3, and nothing in the locked object, requires $\mathrm{Obs}$ to lack an analytic structure, nor requires it to have one. The Fréchet space of jets is compatible with analytic *curves* whether or not one later equips $\mathrm{Obs}$ with an analytic-manifold atlas. Declaring $\mathrm{Obs}$ non-analytic in order to save delayed forks would be a new hypothesis, and it is not used.

What we **can** say:

1. *Realized paths are analytic maps $\mathbb{R}\to\mathrm{Obs}$.* Every geodesic in every real-analytic $W$ lifts to such a map (Theorem 3). “Realized” means: of the form $\pi_W(\sigma)$ for some geodesic $\sigma$ in some real-analytic $W$.

2. *Distinct realized paths meet in a discrete set or coincide.* If two realized paths agree on a set with an accumulation point, they coincide on the connected interval where both are defined (Corollary 3.1). Isolated meetings are allowed. Positive-length overlap forces identity.

3. *Typicality cannot be a count of delayed $\mathrm{Obs}$-branches.* There are no delayed branches in $\mathrm{Obs}$ among analytic geodesic lifts: no pair of distinct realized paths shares a trunk of duration $\tau_*>0$ and then splits. A count of “which way the hitchhiker went after $\tau_*$,” read off elementary objects, is not a count of distinct $\sim$-classes produced by geodesic lifts. Ensemble multiplicity $M$ is not that count either: it is locally invisible, and it is not folded into $\sim$. $|a|^2$ is not that count. Countability of distinct evolutions remains conditional, and this note does not supply it.

---

## 5. What this does not do

It does not write $\Phi$. It does not reconstruct a unique $W$ from $O$. It does not fold $E(O)$ into $\sim$. It does not derive the Born rule. It does not change the locked object: elementary observer $(j_\infty,u)$, equivalently $P(j_\infty,u)$; $W$ of any global topology; ensemble $E(O)$ counted with multiplicity of occurrences.

EKT 1991 remains an existence proof of *global* classical non-uniqueness, and a picture for “doesn’t know / knows.” It is not local branching of an analytic geodesic lift, and it is not $\Phi$.

---

## 6. Report line

- **Proved:** Theorem 3 (geodesic in real-analytic $W$ $\Rightarrow$ analytic curve in $\mathrm{Obs}$, Fermi coordinates / inverse-limit of $J^k$).
- **Proved:** Corollary 3.1 (thick prefix $\Rightarrow$ same curve; delayed local “knows” killed; $E(O)$ locally invisible).
- **Proved:** Proposition 3.2 (from one $O$, unique geodesic curvelet in $P(O)$; not a star of lifts).
- **Remains:** one $\gamma$ with many $W\in E(O)$; Theorem 2 still allows isolated meetings of analytic curves; geodesic evolution of one $O$ does not use that allowance as a star of lifts.
- **Not forced:** $\mathrm{Obs}$ non-analytic.
- **Killed:** branching analytic evolution with thick trunks; typicality as a count of delayed $\mathrm{Obs}$-branches.
- **Not done:** $\Phi$; Born; unique cosmos.

---

## References

Dieudonné, J. *Foundations of Modern Analysis.* Academic Press, 1960. (Analytic ODEs: existence, uniqueness, analyticity of the flow.)

Fermi, E. Sopra i fenomeni che avvengono in vicinanza di una linea oraria. *Atti della Reale Accademia Nazionale dei Lincei* 31 (1922) 21--23, 51--52, 101--103.

Manasse, F. K. and Misner, C. W. Fermi normal coordinates and some basic concepts in differential geometry. *Journal of Mathematical Physics* 4 (1963) 735--745.

Krantz, S. G. and Parks, H. R. *A Primer of Real Analytic Functions.* 2nd ed. Birkhäuser, 2002.

Strayhorn, D. Analyticity and the split. `papers/analytic-split.md`.

Strayhorn, D. Theorem: the simply-connected analytic patch from an infinite jet. `papers/analytic-patch-from-jet.md`.

Strayhorn, D. Cheat sheet: names and symbols. `papers/cheat-sheet.md`.
