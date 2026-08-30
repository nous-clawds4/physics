# Countable out-degree is not a grain of $\mathrm{Obs}$

David Strayhorn

Live hole is the law of $R$, not a grain. After uniformity (`papers/uniform-law-of-r.md`): a countable typicality set of delayed forks from one $O$ is a set of *paths*, not a grain of $\mathrm{Obs}$. Countable out-degree of $R$ supplies that countability. It is still extra. Do not adopt. Do not invent a grain. Not $\Phi$. No $|a|^2$. No $L$. No $1/N$. Paper 1 not rewritten.

Companions: `papers/law-of-r.md`, `papers/uniform-law-of-r.md`, `papers/counting-needs-a-slice.md`, `papers/fusion-and-path-counting.md`, `papers/extra-structure.md`.

**Status.** Theorem 31: if every vertex reachable from $O_0$ has countable out-degree, the set of finite $R$-walks from $O_0$ is countable; if the root already has uncountable out-degree, length-1 evolutions are uncountable. This is a restriction on $R$, not a discrete cut of $\mathrm{Obs}$. Extra relative to Theorems 19–30 and to uniformity. Named, not adopted. Distinguishes extra-structure item 1 (grain of $\mathrm{Obs}$) from item 2 (law of $R$).

---

## 1. What 2008 counts from one $O$

2008 wanted a countable set of distinct evolutions from a given observer. On type (ii) those evolutions are finite walks in $(V,R)$ starting at $O_0$ (Definition 7; Definition 8 delayed forks). They are not points of $\mathrm{Obs}$.

A grain of $\mathrm{Obs}$ (countable $V$) makes every path-set countable, even for the complete graph. That is stronger than the 2008 job from one $O$ needs, and it is extra (Theorems 17–18, 28–30).

---

## 2. Theorem 31

Let $(V,R)$ be a directed graph, $O_0\in V$. Write $\mathrm{succ}(v)=\{v':(v,v')\in R\}$. Let $\mathrm{Path}(O_0)$ be the set of finite walks starting at $O_0$, including the empty walk.

**Theorem 31.**

1. If $|\mathrm{succ}(v)|\le\aleph_0$ for every $v$ reachable from $O_0$ by a finite walk, then $\mathrm{Path}(O_0)$ is countable.
2. If $|\mathrm{succ}(O_0)|$ is uncountable, the set of length-$1$ walks from $O_0$ is uncountable.
3. Countable out-degree is a restriction on $R$, not a grain of $\mathrm{Obs}$: $V$ may remain a continuum. It is extra relative to Theorems 19–30 and to uniformity of $R$ (`papers/uniform-law-of-r.md`). Not adopted.

**Proof.** (1) Let $P_k$ be the set of walks of length $k$ from $O_0$. $P_0$ is a singleton. If $P_k$ is countable and each vertex has countable successor set, then $P_{k+1}$ is a countable union of countable sets, hence countable. By induction each $P_k$ is countable, so $\mathrm{Path}(O_0)=\bigcup_{k\ge 0}P_k$ is countable.

(2) Length-$1$ walks are in bijection with $\mathrm{succ}(O_0)$.

(3) Take $V=\mathrm{Obs}$ (a continuum, Theorem 17) and any $R$ with $|\mathrm{succ}(v)|\le 2$ at every $v$. Then $\mathrm{Path}(O_0)$ is countable and $V$ is not. The restriction is on the stars of $R$. Theorems 19 and 30: the lock does not supply those stars. Uniformity of the *rule* does not make the *stars* countable (`papers/uniform-law-of-r.md`). $\square$

**Not claimed.** This writes a law of $R$. Empty $R$ has out-degree $0$ and $\mathrm{Path}(O_0)$ a singleton; constant $\mathrm{succ}(v)=\{O_{\mathrm{Mink}}\}$ is countable-out-degree. Both are maps. They are not the 2008 job.

**Not claimed.** Countable $\mathrm{Path}(O_0)$ is a typicality *measure*. Circularity remains (`papers/circularity.md`). Unique-measure stays named conditions (`papers/unique-measure-conditions.md`). No $1/N$.

**Relation to Theorem 22.** Finite out-degree makes the one-step out-neighborhood a finite slice (already named extra in Theorem 22). Countably infinite out-degree still makes $\mathrm{Path}(O_0)$ countable and makes that one-step slice infinite, so path-count still needs a further slice to normalize (Theorem 22). Theorem 31 is the countability of *evolutions*, not a slice.

---

## 3. Named leftover, not adopted

Countable (or finite) out-degree of $R$. Extra. Not a grain of $\mathrm{Obs}$. Not lock-side. Not adopted. Grain of $\mathrm{Obs}$ remains extra and is a different cut. Uniformity remains extra and does not replace this.

---

## 4. Report line

- **Proved.** Theorem 31: countable out-degree $\Rightarrow$ countable finite paths from a root; uncountable out-degree at the root $\Rightarrow$ uncountable one-step evolutions. Not a grain of $\mathrm{Obs}$.
- **Not claimed.** A law of $R$. A typicality measure. A closed “no countable path-set without a grain of $\mathrm{Obs}$.”
- **Named, not adopted.** Countable out-degree as a restriction on $R$.
- **Killed.** Reading extra-structure item 1 as if the 2008 job from one $O$ required a grain of $\mathrm{Obs}$. $|a|^2$. $\Phi$.
- **Open.** The law of $R$; whether out-degree is countable; grain of $\mathrm{Obs}$; slice.

---

## References

Strayhorn, D. The law of $R$ is extra structure. `papers/law-of-r.md`.

Strayhorn, D. Uniformity of the law of $R$ is extra. `papers/uniform-law-of-r.md`.

Strayhorn, D. Path-counting needs a slice. `papers/counting-needs-a-slice.md`.

Strayhorn, D. Fusion and path-counting. `papers/fusion-and-path-counting.md`.

Strayhorn, D. Extra structure the 2008 typicality job still needs. `papers/extra-structure.md`.
