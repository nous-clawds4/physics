# Path-counting needs a slice

David Strayhorn

Even when walk-count $N(p,q)$ is well-defined (a DAG, finitely many walks; Theorem 21 of `papers/fusion-and-path-counting.md`), it is not a probability on $\mathrm{Obs}$ or on $V$ without a finite slice. Type-(ii) edges are not geodesic lifts, so they do not inherit proper time from $\gamma_O$. A generation, a Lyapunov, or a $\tau$-cut is extra structure, the same remainder as grain and the law of $R$.

Do not adopt a slice, a tree, $1/N$, a grain, a measure, $\Phi$, or Born. Do not write a law of $R$. Do not restore the 2007 geodesic-generated tree. Paper 1 not rewritten.

Companion: `papers/fusion-and-path-counting.md`.

**Status.** Theorem 22: $N(p,\cdot)$ does not determine a probability measure on $V$ from the locked object. A slice is extra. Not adopted.

---

## 1. What path-count supplies

On a DAG with the finiteness of Theorem 21, $N(p,q)\in\mathbb{N}\cup\{0\}$ is a function of pairs. The corpus wants “the probability that $p$ will evolve into $p_i$.” That is a probability on a set of *targets*, not a list of pair-counts.

Let $V_p=\{q\in V:N(p,q)>0\}$. This may be infinite: an infinite arborescence (infinite future, finite out-degree) already has infinitely many reachable vertices, each with $N(p,q)=1$. Then $\sum_q N(p,q)=\infty$, and $N(p,\cdot)$ does not normalize. Even when $V_p$ is finite, summing over *all* depths at once mixes one-step children with their descendants; the corpus’s $1/N$ figures are drawn on a generation, not on the whole tree.

---

## 2. Theorem 22. No locked slice

**Theorem 22.** Nothing already locked — the jet/patch object, hitchhiking, $E(O)$, $\sim_L$, the Fermi-slice topology, the named functors of Theorem 19, or a DAG walk-count $N$ — supplies a finite (or summable) slice of $V$ on which $N(p,\cdot)$ is a probability. In particular type-(ii) edges, not being geodesic lifts, do not carry the proper time of $\gamma_O$.

**Proof.** Proper time is defined along $\sigma_O$ in $P(O)$, hence along $\gamma_O$ (type (i)). A type-(ii) edge $(O,O')$ leaves that curvelet by definition. No locked map $\tau:R\to\mathbb{R}$ or generation $g:V\to\mathbb{N}$ has been named. Fermi-slice neighborhoods are uncountable (Theorem 17), so “targets in a small ball” is not a finite slice. Continuous invariants do not grain (Theorem 18). A finite $V$ is a grain, not adopted. $\square$

**Named, not adopted.** A generation $g:V\to\mathbb{N}$ with $R$ only advancing $g$ (a ranked DAG); a Lyapunov function on $\mathrm{Obs}$; a cutoff of walk-length. Each makes $\sum\{N(p,q):g(q)=n\}$ finite on locally finite graphs, and then $N(p,\cdot)$ at level $n$ normalizes. Extra structure. Not a law of $R$.

---

## 3. Report line

- **Proved.** Theorem 22: path-count is not a probability without a slice; type-(ii) has no locked clock.
- **Named, not adopted.** Generation / Lyapunov / walk-length cutoff.
- **Killed.** Grain or $|a|^2$ as a lock-side slice.
- **Open.** Whether to put in a slice; the law of $R$; whether to abandon type (ii).

---

## References

Strayhorn, D. Fusion and path-counting. `papers/fusion-and-path-counting.md`.

Strayhorn, D. The law of $R$ is extra structure. `papers/law-of-r.md`.

Strayhorn, D. Neighborhoods are not a countable $N$. `papers/neighborhood-uncountable.md`.
