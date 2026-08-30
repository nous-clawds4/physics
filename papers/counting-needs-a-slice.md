# Path-counting needs a slice

David Strayhorn

Even when walk-count $N(p,q)$ is well-defined (a DAG, finitely many walks; Theorem 21 of `papers/fusion-and-path-counting.md`), it is not a probability on $\mathrm{Obs}$ or on $V$ without a finite slice. Type-(ii) edges are not geodesic lifts, so they do not inherit proper time from $\gamma_O$. A generation, a Lyapunov, or a $\tau$-cut is extra structure, the same remainder as grain and the law of $R$.

Do not adopt a slice, a tree, $1/N$, a grain, a measure, $\Phi$, or Born. Do not write a law of $R$. Do not restore the 2007 geodesic-generated tree. Paper 1 not rewritten.

Companion: `papers/fusion-and-path-counting.md`.

**Status.** Theorem 22: none of the named candidates is a finite slice of type-(ii) targets on which $N(p,\cdot)$ is a probability. Not a closed “nothing supplies.” A slice is extra. Not adopted.

---

## 1. What path-count supplies

On a DAG with the finiteness of Theorem 21, $N(p,q)\in\mathbb{N}\cup\{0\}$ is a function of pairs. The corpus wants “the probability that $p$ will evolve into $p_i$.” That is a probability on a set of *targets*, not a list of pair-counts.

Let $V_p=\{q\in V:N(p,q)>0\}$. This may be infinite: an infinite arborescence (infinite future, finite out-degree) already has infinitely many reachable vertices, each with $N(p,q)=1$. Then $\sum_q N(p,q)=\infty$, and $N(p,\cdot)$ does not normalize. Even when $V_p$ is finite, summing over *all* depths at once mixes one-step children with their descendants; the corpus’s $1/N$ figures are drawn on a generation, not on the whole tree.

---

## 2. Theorem 22. Named non-slices

**Theorem 22.** None of the named candidates

1. proper time along $\gamma_O$ (hitchhiker $\tau$);
2. nonempty open Fermi-slice balls (Theorem 17);
3. finitely many continuous maps $f:\mathrm{Obs}\to\mathbb{R}^n$ on a nonempty connected open (Theorem 18);
4. a grain ($d$, or finite $V$ put in by hand)

is a finite (or summable) slice of type-(ii) targets on which $N(p,\cdot)$ is a probability. The law of a slice is extra relative to those.

**Proof.** (1) Hitchhiker $\tau$ is the proper-time parameter of $\sigma_O\subset P(O)$, hence labels lumps *on* $\gamma_O$ (type (i)). A type-(ii) edge leaves that curvelet; those $\tau$-slices are not the type-(ii) targets. (2) Theorem 17: $U\setminus\gamma_O$ is uncountable, so a Fermi ball is not a finite slice. (3) Theorem 18: one class or a continuum, not a nonempty finite typicality set of delayed forks. (4) A grain is extra structure, not a theorem of the jet/patch, and is not adopted. $\square$

**Not claimed.** Nothing supplies a finite slice. The empty set is a finite slice; it is trivial and is not a nonempty typicality set of delayed forks. The one-step out-neighborhood $\{O':(O,O')\in R\}$ of a *locally finite* $R$ is a finite slice. It comes from a law of $R$, which is extra (Theorem 19). Not a lock-side slice.

**Named, not adopted.** A generation $g:V\to\mathbb{N}$ with $R$ only advancing $g$ (a ranked DAG); a Lyapunov function on $\mathrm{Obs}$; a cutoff of walk-length. Each makes $\sum\{N(p,q):g(q)=n\}$ finite on locally finite graphs, and then $N(p,\cdot)$ at level $n$ normalizes. Extra structure. Not a law of $R$.

---

## 3. Report line

- **Proved.** Theorem 22: named non-slices (hitchhiker $\tau$, Fermi balls, continuous $f$, grain) fail to make $N(p,\cdot)$ a probability of type-(ii) targets.
- **Not claimed.** A closed “nothing supplies a finite slice.” Locally finite one-step out-neighborhoods are finite slices and come from a law of $R$ (extra).
- **Named, not adopted.** Generation / Lyapunov / walk-length cutoff.
- **Killed.** Grain or $|a|^2$ as a lock-side slice.
- **Open.** Whether to put in a slice; the law of $R$; whether to abandon type (ii).

---

## References

Strayhorn, D. Fusion and path-counting. `papers/fusion-and-path-counting.md`.

Strayhorn, D. The law of $R$ is extra structure. `papers/law-of-r.md`.

Strayhorn, D. Neighborhoods are not a countable $N$. `papers/neighborhood-uncountable.md`.

Strayhorn, D. Grain is not a readout of continuous invariants. `papers/grain-not-from-invariants.md`.
