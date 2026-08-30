# A finite ancestor set is extra

David Strayhorn

Live hole is the law of $R$, not a grain. Theorem 21 names a finite ancestor set as part of a *sufficient* condition for $N(p,q)\in\mathbb{N}$. Countable out-degree makes the *set* of finite walks countable (Theorem 31), including on an infinite ancestor set. Finite ancestors are a further extra, for a finite *count*. Do not adopt. Do not invent a grain. Not $\Phi$. No $|a|^2$. No $L$. No $1/N$. Paper 1 not rewritten.

Companions: `papers/fusion-and-path-counting.md` (Theorem 21), `papers/countable-outdegree.md` (Theorem 31), `papers/counting-needs-a-slice.md` (Theorem 22).

**Status.** Named leftover. Write $\mathrm{Anc}(q)$ for vertices that reach $q$ by a finite walk, including $q$. Countable in-degree (dual of Theorem 31) makes $\mathrm{Anc}(q)$ countable. Finite $\mathrm{Anc}(q)$ is stronger and still extra. Distinct from a slice (Theorem 22) and from unique-tree. Not lock-side (Proposition 13, Theorem 19). Not a grain of $\mathrm{Obs}$: $V\setminus\mathrm{Anc}(q)$ may remain a continuum. Not adopted.

---

## 1. What Theorem 21 actually used

Theorem 21: on a DAG, $N(p,q)$ is well-defined if only finitely many walks $p\to q$ exist, e.g. only finitely many vertices both reachable from $p$ and able to reach $q$, with finite in-degree. That “e.g.” is a finite ancestor set in the interval from $p$ to $q$, plus finite in-degree, plus a DAG.

An infinite arborescence (infinite future, finite out-degree) already has infinitely many reachable vertices and $\sum_q N(p,q)=\infty$ (Theorem 22). Finite $\mathrm{Anc}(q)$ looking *backward* is the dual cut: finitely many possible origins for walks into $q$.

---

## 2. Countable vs finite

Theorem 31: countable out-degree $\Rightarrow$ countable finite walks *from* a root; the reachable set is countable; it need not be finite. Dual backward: countable in-degree $\Rightarrow$ countable $\mathrm{Anc}(q)$ and countable finite walks into $q$, cycles allowed. Finite $\mathrm{Anc}(q)$ is not implied.

König: locally finite plus infinite reachable $\Rightarrow$ an infinite ray (`papers/dead-ends-and-rays.md`). So local finiteness plus no dead ends, with $\mathrm{Anc}(q)$ infinite, still leaves infinitely many finite walks (prefixes of the ray, at least). Finite $N(p,q)$ needs a further cut: finite ancestors, or a slice, or a DAG plus finite depth, or simple paths. All extra.

**Not claimed.** No finite $N$ exists. Empty $R$ has $\mathrm{Anc}(q)=\{q\}$ and $N=1$ at $q$. A finite DAG is a map. They are not the 2008 job.

---

## 3. Named leftover, not adopted

Finite ancestor set. Finite depth / generation (already named, Theorem 22). Simple paths (already named, Theorem 20). All extra for finite $N$. None adopted. Not a grain of $\mathrm{Obs}$.

---

## 4. Report line

- **Named, not adopted.** Finite $\mathrm{Anc}(q)$ as a restriction on $R$. Extra for $N\in\mathbb{N}$, not for a countable walk-set (Theorem 31).
- **Killed.** Reading Theorem 21’s finite-ancestor example as lock-side. Reading Theorem 31 as a finite ancestor set. $|a|^2$. $\Phi$.
- **Open.** The law of $R$; whether $\mathrm{Anc}(q)$ is finite; grain of $\mathrm{Obs}$.

---

## References

Strayhorn, D. Fusion and path-counting. `papers/fusion-and-path-counting.md`. Theorem 21.

Strayhorn, D. Countable out-degree is not a grain of $\mathrm{Obs}$. `papers/countable-outdegree.md`. Theorem 31.

Strayhorn, D. Path-counting needs a slice. `papers/counting-needs-a-slice.md`. Theorem 22.

Strayhorn, D. No dead ends is extra; König rays may be a continuum. `papers/dead-ends-and-rays.md`.
