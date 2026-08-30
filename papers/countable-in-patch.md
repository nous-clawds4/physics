# Lock-side subsets of in-patch occurrence are not a countable $N$

David Strayhorn

$S(O)=\mathrm{Occ}(O)\setminus\gamma_O$ is lock-side and typically a continuum. Can a *named lock-side subset* of it be a nonempty countable typicality set of delayed forks without a grain? Spatial slice at one hitchhiker $\tau$, Cauchy surface in $P(O)$, integer curvature bins: prove or kill. Do not adopt. Do not write $\Phi$, $L$, or $|a|^2$. Do not put a $d$ by hand. Paper 1 not rewritten.

Companions: `papers/in-patch-support.md` (PR #35; $\mathrm{Occ}$ is defined here, the support constraint is not used), `papers/neighborhood-uncountable.md`, `papers/grain-not-from-invariants.md`.

**Status.** Theorem 28: the named constructions — Fermi spatial slice at one $\tau$, a Cauchy surface in $P(O)$, integer bins of finitely many continuous curvature scalars — each yield one class or a continuum of lumps in $S(O)$, or else smuggle a grain (a mesh, a selector, or a choice of surface). Not a closed “no countable subset of $S(O)$.” $\mathbb{Q}$-meshes in Fermi coordinates are countable and extra. Empty and singleton are countable and are not a nonempty typicality set of delayed forks.

---

## 0. The set

$P(O)$ is the unique simply-connected analytic continuation of the germ (Theorem B). For $q\in P(O)$ write $O_q$ for the lump at $q$ (infinite jet of the metric, plus a future unit timelike; along $\sigma_O$ one takes $\dot\sigma_O$). Set
$$
\mathrm{Occ}(O)\;=\;\{O_q:\ q\in P(O)\},\qquad
S(O)\;=\;\mathrm{Occ}(O)\setminus\gamma_O.
$$
Both are functions of the locked patch. They do not use $E(O)$. Restricting $R$ to $S(O)$ is a named support constraint, not adopted (PR #35). This note asks only whether a lock-side subset of $S(O)$ counts.

The map $q\mapsto O_q$ can collapse. On a homogeneous patch (Minkowski) it is constant, so $S(O)$ may be empty. “Typically” below means: for a generic real-analytic Lorentzian germ, local isometries are discrete, and $q\mapsto O_q$ is locally injective off $\sigma_O$.

---

## 1. Theorem 28. Named lock-side subsets do not count

**Theorem 28.** None of the following supplies a nonempty countable typicality set of delayed forks as a lock-side subset of $S(O)$, without a grain:

1. *Spatial slice at one hitchhiker $\tau$.* Let $\tau\in(0,\tau_\partial)$ and let $\Sigma_\tau$ be the Fermi spatial slice through $\sigma_O(\tau)$ in a convex neighbourhood of $p$ (points with Fermi $x^0=\tau$). Write $S_\tau=\{O_q:\ q\in\Sigma_\tau\}\setminus\gamma_O$.
2. *A Cauchy surface $\Sigma$ in $P(O)$.* Write $S_\Sigma=\{O_q:\ q\in\Sigma\}\setminus\gamma_O$, when such a $\Sigma$ exists.
3. *Integer curvature bins.* Let $f$ be a finite list of continuous curvature scalars (or any continuous $f:\mathrm{Obs}\to\mathbb{R}^n$), and let $\pi_\mathbb{Z}$ be rounding to $\mathbb{Z}^n$. The occupied bins $\pi_\mathbb{Z}(f(S(O)))$, or the fibers $(\pi_\mathbb{Z}\circ f)^{-1}(k)\cap S(O)$.

**Proof.** (1) $\Sigma_\tau$ is lock-side (Fermi coordinates in a convex neighbourhood). It is an open set in a spacelike $3$-plane. The image $S_\tau$ is the continuous image of a connected $3$-manifold (minus at most the one point $\sigma_O(\tau)$). If $q\mapsto O_q$ is constant on $\Sigma_\tau$, then $S_\tau$ is empty or a singleton: not a nonempty typicality set of *distinct* delayed forks. If it is not constant, then (analyticity) it is non-constant on a nonempty open in $\Sigma_\tau$, hence $S_\tau$ contains a continuum of lumps. Either one class or a continuum; never a countably infinite typicality set without a further cut.

(2) $P(O)$ need not be globally hyperbolic. Existence of a Cauchy surface for the whole patch is extra. A Cauchy surface for a convex neighbourhood, if one takes the Fermi slice, is (1). If a connected Cauchy surface $\Sigma$ does exist, the same alternative applies: $S_\Sigma$ is empty, a singleton, or a continuum. Choosing one Cauchy surface among many is extra.

(3) Without rounding, $f$ on a connected open of lumps is one class or a continuum (Theorem 18). Restricted to $S(O)$ along a connected slice, the same alternative holds. Rounding $\pi_\mathbb{Z}$ is a mesh, the same kind of choice as $d$-decimal (Theorem 18, §3). That mesh is a grain, extra. Each nonempty fiber of $\pi_\mathbb{Z}\circ f$ on a slice is typically a positive-dimensional level set, hence a continuum of lumps; using the fiber as one vertex packs a continuum into a class (a grain quotient). Using one representative per occupied bin is a selector, extra. The set of occupied bins may be countable; those are labels, not lumps. $\square$

**Corollary 28.1.** Discrete algebraic invariants (Petrov type, $\dim$ Killing) remain finitely many labels. On $S(O)$ each nonempty type is typically a continuum of germs. They fail to grain, as already for $\mathrm{Obs}$ (Theorem 19). Not a fourth functor in Theorem 28.

**Not claimed.** $S(O)$ has no countable subset. A $\mathbb{Q}$-mesh in Fermi coordinates (points with rational $x^i$ on $\Sigma_\tau$) is countable; the mesh is extra, the same kind of $d$ as grain-candidates. The empty set is countable. A singleton (homogeneous slice; Minkowski) is countable and is not a typicality set of delayed forks. Isolated zeros of a Morse function on $\Sigma_\tau$ can be finite; choosing the function, and assuming Morse, is extra.

**Killed.** Fermi spatial slice as a countable $N$. Cauchy surface in $P(O)$ as a countable $N$. Integer curvature bins as a lock-side grain. $|a|^2$ as a selector inside a bin. $L$ as a discrete action that would pick the bins.

---

## 2. Named leftover, not adopted

None of (1)–(3) is adopted as a typicality set. $S(O)$ as a support constraint on $R$ remains named, not adopted (PR #35). A mesh, a selector, or a grain would make a countable subset; those stay extra.

---

## 3. Report line

- **Proved.** Theorem 28: Fermi spatial slice at one $\tau$, a Cauchy surface in $P(O)$, and integer curvature bins each give one class or a continuum in $S(O)$, or else smuggle a grain. Not a countable lock-side typicality set.
- **Not claimed.** No countable subset of $S(O)$. $\mathbb{Q}$-meshes extra. Empty and singleton are not the 2008 job.
- **Named, not adopted.** The three constructions as cuts. In-patch support (PR #35).
- **Killed.** Those three as lock-side countable $N$. $|a|^2$. $L$ unwritten.
- **Open.** Grain, or any other discrete cut. The law of $R$.

---

## References

Strayhorn, D. In-patch occurrence as a support constraint. `papers/in-patch-support.md` (PR #35).

Strayhorn, D. Neighborhoods are not a countable $N$. `papers/neighborhood-uncountable.md`.

Strayhorn, D. Grain is not a readout of continuous invariants. `papers/grain-not-from-invariants.md`.

Strayhorn, D. The law of $R$ is extra structure. `papers/law-of-r.md`.

Strayhorn, D. Theorem: the simply-connected analytic patch from an infinite jet. `papers/analytic-patch-from-jet.md`.
