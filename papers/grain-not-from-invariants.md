# Grain is not a readout of continuous invariants

David Strayhorn

Finitely many continuous functions on $\mathrm{Obs}$ (curvature scalars, injectivity radius, and the like) do not yield a countable grain. Do not lock a grain. Do not put a $d$ by hand. Do not put $1/N$.

Companions: `papers/neighborhood-uncountable.md`, `papers/obs-as-a-space.md`, `papers/grain-candidates.md`.

**Status.** Theorem 18: for a continuous $f:\mathrm{Obs}\to\mathbb{R}^n$, the set of value-classes meeting a nonempty open $U$ is either a singleton or uncountable. Level sets are uncountable in the latter case as soon as a fiber over a continuum of values is taken, and in any case the set of classes is uncountable. Rounding the values to a mesh $\delta$ is a new discrete scale, the same kind of choice as $d$-decimal truncation. The locked object does not supply that scale. Grain, if adopted later, is extra structure, not a theorem of the jet/patch.

---

## 1. What a grain-from-invariants would be

Let $f:\mathrm{Obs}\to\mathbb{R}^n$ be continuous in the Fermi-slice topology (Theorem 16). Examples: Ricci scalar, Kretschmann scalar, any finite list of curvature scalars built polynomially from the $2$-jet; any continuous function of a finite jet. Injectivity radius of $P(O)$ at the basepoint, when it is continuous (it is at least upper semi-continuous as a function of the germ in reasonable topologies).

Write $O\sim_f O'$ iff $f(O)=f(O')$. The quotient $\mathrm{Obs}/{\sim_f}$ is the set of *value-classes*. Using those classes as grain vertices is the candidate: two lumps count as the same grain-point when the named invariants agree.

---

## 2. Theorem 18. Continuous invariants do not grain

**Theorem 18.** Let $f:\mathrm{Obs}\to\mathbb{R}^n$ be continuous, and let $U\subset\mathrm{Obs}$ be nonempty and open. Then either $f(U)$ is a singleton, or $f(U)$ is uncountable. Equivalently: the number of $\sim_f$-classes meeting $U$ is either $1$ or uncountable.

**Proof.** $U$ is open in the Fermi-slice topology, hence connected in a neighborhood of any point after shrinking to a basic ball (basic open sets in the inverse-limit topology are connected, as convex balls in each $J^k$). Continuous images of connected sets are connected. A connected subset of $\mathbb{R}^n$ is either a singleton or uncountable (it contains a nontrivial interval along some line if it has two points: more precisely, a connected subset of $\mathbb{R}^n$ with at least two points has cardinality of the continuum). $\square$

**Corollary 18.1.** If $f$ is locally constant on $U$, then $\sim_f$ does not separate the continuum of lumps in $U$ given by Theorem 17. If $f$ is not locally constant, then $\sim_f$ produces uncountably many classes in $U$, not a countable vertex-set. Either way, $\sim_f$ is not a countable grain on $U$.

Level sets: if $f(U)$ is a continuum, a typical fiber $f^{-1}(c)\cap U$ is itself uncountable (Theorem 17 supplies a continuum of $2$-jets in $U$; a continuous $f$ depending on finitely many jet coefficients has positive-dimensional fibers on that continuum unless it is a local coordinate). Using fibers as vertices would pack uncountably many lumps into each vertex *and* leave uncountably many vertices. Using values as vertices leaves uncountably many vertices. Neither is a countable grain.

---

## 3. Rounding is a $d$

Replace $f$ by $\pi_\delta\circ f$, where $\pi_\delta$ is a partition of $\mathbb{R}^n$ into bins of mesh $\delta>0$ (decimal truncation of each coordinate is the case $\delta=10^{-d}$). Locally, if $f(U)$ is bounded, only finitely many bins meet $f(U)$. Globally one gets a countable vertex-set.

That $\delta$ (or $d$) is extra structure. It is the same kind of choice as Strayhorn3’s $d$-decimal truncation of jet coefficients (`papers/grain-candidates.md`). The locked object — an infinite analytic jet and its patch — does not name a $\delta$. Borel already closed finite jets as the *object*. Putting a mesh on continuous invariants does not sneak a grain out of the object; it puts a grain in by hand.

Do not put a $d$ in by hand. Do not put $1/N$ on the resulting bins.

Semi-continuous variants (injectivity radius as a lower or upper semi-continuous function of the germ) do not change the alternative: without a mesh, the set of values on an open $U$ is typically a continuum; with a mesh, the mesh is the grain.

---

## 4. Grain is extra structure

The jet/patch object determines the germ, the curvature scalars, the patch, and (when defined) the injectivity radius. It does not determine a countable partition of $\mathrm{Obs}$. Theorem 17: open sets are continua. Theorem 18: continuous invariants preserve that alternative (one class, or a continuum of classes). A discrete cut is a further hypothesis.

Grain, if adopted later, is extra structure, not a theorem of the jet/patch. It is not adopted here.

---

## 5. Report line

- **Proved.** Theorem 18: finitely many continuous functions on $\mathrm{Obs}$ yield, on every nonempty open $U$, either one value-class or uncountably many. Rounding is a mesh $\delta$, the same kind of choice as $d$. The locked object does not supply that scale.
- **Killed.** Reading a countable grain off curvature scalars, injectivity radius, or any finite continuous invariant list.
- **Not adopted.** A grain. A $d$. $1/N$.
- **Open.** Grain, as extra structure.

---

## References

Strayhorn, D. Neighborhoods are not a countable $N$. `papers/neighborhood-uncountable.md`.

Strayhorn, D. $\mathrm{Obs}$ as a space? `papers/obs-as-a-space.md`.

Strayhorn, D. Grain candidates. `papers/grain-candidates.md`.
