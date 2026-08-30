# Least action as a constraint on the support of $R$

David Strayhorn

ActionPrinciple Observation 1: patterns in a state-transition diagram can extremize an observable $y$. Exact $S$ was deferred; $L$ was never written. On lumps, that is a constraint on the *support* of $R$ (which diagrams appear), not a law of weights and not $\Phi$. Name it. Do not adopt it. Do not write $L$. Do not write $\Phi$. Do not put $1/N$. Do not lock a grain. Paper 1 not rewritten.

Companions: `papers/original-two-layer.md`, `papers/law-of-r.md`, `papers/fermi-distance.md`.

**Status.** Named, not adopted. Theorem 25: a continuous observable on a connected open does not cut the support of $R$ down to a nonempty finite typicality set of delayed forks. Isolated extrema and integer $y\in[0,Y]$ are extra. $L$ is not written.

---

## 1. Corpus, as written

ActionPrinciple: the tree diagram is a directed graph of observer-states. Outcome counting reads probabilities off the diagram. Observation 1:

> There exist patterns in the organization of the state transition diagram that result in the minimalization (more generally, extremalization) of an observable.

Exact $S$ is not given. How or why the pattern arises is deferred to an underlying theory of observer states, “not provided by this paper.” The example $y$ is an integer in $[0,Y]$.

On lumps: vertices are $\sim_L$-classes, not $3$-manifolds and not Hilbert rays. The diagram is $R$ (Definition 7; Definition 9 named, not adopted). The *support* of $R$ is the set of edges that exist. Weights, $1/N$, and path-count are not the support.

---

## 2. What the constraint would be, not adopted

**Named (not adopted).** Least-action-on-support: only those $R$ (or those finite diagrams in $R$) appear that extremize some observable $y$. No formula for $y$. No $L$. Not $\Phi$. Not a law of which pair $(O,O')$ lies in $R$ beyond “the diagram is an extremal.” Extra structure, the same remainder as the law of $R$ (Theorem 19) with a further filter on diagrams.

This is a constraint on *which graphs are allowed*, not on Born weights. Putting $|a|^2$ in as $y$ is killed as a lock-side constraint.

---

## 3. Theorem 25. Continuous $y$ does not finite-support $R$

**Theorem 25.** Let $U\subset\mathrm{Obs}$ be a nonempty connected open in the Fermi-slice topology, and let $y:U\to\mathbb{R}$ be continuous. The level sets and extremal sets of $y$ do not supply a nonempty finite typicality set of delayed forks as the support of $R$ on $U$. Rounding $y$, or taking $y$ integer in $[0,Y]$, is a grain.

**Proof.** Theorem 18: finitely many continuous functions on a connected open yield one class or a continuum. In particular $\mathrm{argmax}\,y$, $\mathrm{argmin}\,y$, and $\{y=c\}$ are one point or a continuum if nonempty in $U$. A continuum of lumps is not a finite support for type-(ii) edges. An isolated extremum is a degeneracy not supplied by the jet/patch or by Theorem 16. The ActionPrinciple example $y\in\{0,\ldots,Y\}$ is already a discrete observable: extra, the same kind of choice as $d$. $\square$

**Not claimed.** No function $y$ of diagrams exists. A $y$ that sees a locally finite $R$ and counts outgoing edges is a function of a law of $R$, which is extra. The empty support is finite and trivial.

Fermi-slice distance as $y$ is Theorem 24: a continuous scale, not a finite support.

---

## 4. Report line

- **Named, not adopted.** Least-action-on-support: a filter on which diagrams appear, without $L$ and without $\Phi$.
- **Proved.** Theorem 25: continuous $y$ on a connected open does not finite-support $R$. Integer $y\in[0,Y]$ is a grain.
- **Killed.** $|a|^2$ as $y$. Grain as the lock-side way to get isolated extrema.
- **Open.** The law of $R$; whether to adopt a support filter at all.

---

## References

Strayhorn, D. An action principle from the many-worlds interpretation. `old-manuscripts/ActionPrinciple.pdf`.

Strayhorn, D. Original two-layer dynamics vs the lock. `papers/original-two-layer.md`.

Strayhorn, D. The law of $R$ is extra structure. `papers/law-of-r.md`.

Strayhorn, D. Fermi-slice distance is a continuous scale. `papers/fermi-distance.md`.

Strayhorn, D. Grain is not a readout of continuous invariants. `papers/grain-not-from-invariants.md`.
