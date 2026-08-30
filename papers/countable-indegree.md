# Countable in-degree is extra

David Strayhorn

Live hole is the law of $R$, not a grain. Dual of Theorem 31: countable *out*-degree makes finite walks *from* a root countable. Countable *in*-degree makes finite walks *into* a vertex a set that can be counted. Uncountable in-degree already makes length-$1$ incoming walks uncountable, so $N(\cdot,q)$ is not a natural number. Extra. Do not adopt. Do not invent a grain. Not $\Phi$. No $|a|^2$. No $L$. No $1/N$. Paper 1 not rewritten.

Companions: `papers/countable-outdegree.md` (Theorem 31), `papers/fusion-and-path-counting.md` (Theorem 21), `papers/local-law-of-r.md`, `papers/uniform-law-of-r.md`.

**Status.** Theorem 33: uncountable in-degree at $q$ $\Rightarrow$ uncountably many length-$1$ walks into $q$. Countable in-degree is a restriction on $R$, not a grain of $\mathrm{Obs}$. Extra relative to Theorems 19–32, locality, and no-dead-ends (all on main). Theorem 21 already used finite in-degree as a *sufficient* example for finitely many walks $p\to q$; it is not lock-side. Named, not adopted.

---

## 1. Dual of Theorem 31

Theorem 31: $\mathrm{Path}(O_0)$ is finite walks *from* $O_0$; countable out-degree $\Rightarrow$ that set is countable. Walk-count $N(p,q)$ (Theorem 21) is walks *into* $q$ from $p$. Incoming stars are $\mathrm{pred}(q)=\{v:(v,q)\in R\}$.

---

## 2. Theorem 33

Let $(V,R)$ be a directed graph. Write $\mathrm{pred}(q)=\{v:(v,q)\in R\}$.

**Theorem 33.**

1. If $|\mathrm{pred}(q)|$ is uncountable, the set of length-$1$ walks into $q$ is uncountable, so $N(\cdot,q)$ is not a natural number.
2. If $|\mathrm{pred}(v)|\le\aleph_0$ at every $v$ that can reach $q$ by a finite walk, then the set of finite walks into $q$ is countable. No DAG is required. A pumpable cycle makes $N(p,q)$ infinite (Theorem 20), not the set uncountable.
3. Countable in-degree is a restriction on $R$, not a grain of $\mathrm{Obs}$: $V$ may remain a continuum. Extra relative to Theorems 19–32. Not adopted.

**Proof.** (1) Length-$1$ walks into $q$ are in bijection with $\mathrm{pred}(q)$. (2) Dual of Theorem 31(1). Let $W_k$ be the walks of length $k$ ending at $q$. $W_0$ is a singleton. Each walk in $W_{k+1}$ is a walk in $W_k$ with a predecessor prepended at its start; if $W_k$ is countable and each such start has countable $\mathrm{pred}$, then $W_{k+1}$ is a countable union of countable sets. Cycles are allowed: they contribute countably many finite concatenations, not a continuum. (3) Take $V=\mathrm{Obs}$ (Theorem 17) and $|\mathrm{pred}(v)|\le 2$. Continuum of lumps, countable in-stars. The lock does not pick those stars (Theorem 19). $\square$

**Relation to Theorem 21.** $N(p,q)\in\mathbb{N}\cup\{0\}$ needs *finitely many* walks $p\to q$, not merely a countable set of them. A DAG (no pumpable cycle) plus finite in-degree plus a finite ancestor set is a *sufficient* condition named in Theorem 21. That DAG / no-pumpable-cycle hypothesis lives here, not in (2). A pumpable cycle makes $N(p,q)$ infinite (Theorem 20) while the set of finite walks into $q$ stays countable under (2). Fusion adds walks (Theorem 21); it does not grain $\mathrm{Obs}$. Countable in-degree is extra either way.

**Not claimed.** This writes a law of $R$. Empty $R$ has in-degree $0$. Constant $\mathrm{pred}(v)=\{O_{\mathrm{Mink}}\}$ is countable-in-degree. Both are maps. They are not the 2008 job.

**Not claimed.** A typicality measure. Locality (`papers/local-law-of-r.md`) does not supply countable in-degree (Theorem 17). Uniformity does not. No $1/N$.

---

## 3. Named leftover, not adopted

Countable (or finite) in-degree of $R$. Extra. Dual of Theorem 31. Not a grain of $\mathrm{Obs}$. Not adopted.

---

## 4. Report line

- **Proved.** Theorem 33: uncountable in-degree $\Rightarrow$ uncountable length-$1$ incoming walks; countable in-degree $\Rightarrow$ countable finite walks into $q$ (cycles allowed). Not a grain of $\mathrm{Obs}$. DAG / no pumpable cycle is for $N(p,q)\in\mathbb{N}$ (Theorems 20–21), not for countability of the set.
- **Not claimed.** A law of $R$. A typicality measure.
- **Named, not adopted.** Countable in-degree as a restriction on $R$.
- **Killed.** Reading Theorem 21’s finite-in-degree example as lock-side. $|a|^2$. $\Phi$.
- **Open.** The law of $R$; whether in-degree is countable; grain of $\mathrm{Obs}$.

---

## References

Strayhorn, D. Countable out-degree is not a grain of $\mathrm{Obs}$. `papers/countable-outdegree.md`. Theorem 31.

Strayhorn, D. Fusion and path-counting. `papers/fusion-and-path-counting.md`. Theorem 21.

Strayhorn, D. The law of $R$ is extra structure. `papers/law-of-r.md`.

Strayhorn, D. Locality of $R$ in the Fermi-slice topology is extra. `papers/local-law-of-r.md`.
