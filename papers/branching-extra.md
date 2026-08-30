# Branching is extra

David Strayhorn

Live hole is the law of $R$, not a grain. Delayed-fork typicality from one $O$ (Definition 8) needs a vertex of out-degree at least $2$. Unique-successor $R$ restores empty typicality of forks (one walk). That branching is extra. Do not adopt. Do not invent a grain. Not $\Phi$. No $|a|^2$. No $L$. No $1/N$. Paper 1 not rewritten.

Proposition 14 is already the formal-Fréchet fact in `papers/obs-as-a-space.md`. This is Theorem 32, after Theorem 31.

Companions: `papers/law-of-r.md`, `papers/tree-as-structure.md`, `papers/type-ii-adopted.md`, `papers/uniform-law-of-r.md`, `papers/countable-outdegree.md`.

**Status.** Theorem 32: if every vertex reachable from $O_0$ has out-degree at most $1$, there is no delayed fork from $O_0$. A delayed fork requires some reachable $v$ with $|\mathrm{succ}(v)|\ge 2$. That is a restriction on $R$, not a grain of $\mathrm{Obs}$. Extra relative to Proposition 13 and Theorems 19–31. Named, not adopted.

---

## 1. What 2008 needs from one $O$

2008 wanted a countable set of *distinct* evolutions that delayed-fork. Definition 8: two paths share a prefix of positive length, then occupy distinct vertices. A single walk is not that set. Hitchhiking already gives one curvelet (Theorem 8). Type (ii) is extra edges; they still do not fork unless some star branches.

---

## 2. Theorem 32

Let $(V,R)$ be a directed graph, $O_0\in V$. Write $\mathrm{succ}(v)=\{v':(v,v')\in R\}$.

**Theorem 32.**

1. If $|\mathrm{succ}(v)|\le 1$ for every $v$ reachable from $O_0$ by a finite walk, then there is at most one walk of each length from $O_0$, and no delayed fork from $O_0$ in the sense of Definition 8.
2. A delayed fork from $O_0$ requires some $v$ reachable from $O_0$ with $|\mathrm{succ}(v)|\ge 2$. That is a restriction on $R$. Extra relative to Proposition 13 and Theorems 19–31. Not a grain of $\mathrm{Obs}$: $V$ may remain a continuum. Not adopted.

**Proof.** (1) From $O_0$, each vertex has at most one successor, so the walk is unique at each length (or it dies). Definition 8 needs $\pi_{n+1}\ne\pi'_{n+1}$ after a common prefix, hence two distinct edges out of $\pi_n$. (2) Immediate from (1). Take $V=\mathrm{Obs}$ and a unique-successor $R$ (a ray, or empty). $V$ is a continuum (Theorem 17); there is no delayed fork. The lock does not pick the vertices of out-degree $\ge 2$ (Proposition 13, Theorem 19). $\square$

**Not claimed.** This writes a law of $R$. The complete relation has huge stars. Empty $R$ and a ray both satisfy $|\mathrm{succ}|\le 1$. They are maps. They are not the 2008 job.

**Not claimed.** Branching supplies a typicality *measure*. Circularity remains. No $1/N$.

**Relation to Theorem 31.** Theorem 31: countable out-degree makes $\mathrm{Path}(O_0)$ countable, where $\mathrm{Path}(O_0)$ is the set of *finite* walks (`papers/countable-outdegree.md`, on main). Branching is existence of delayed forks. Neither is a grain of $\mathrm{Obs}$. Uniformity of the rule does not supply either (`papers/uniform-law-of-r.md`). A countably branching tree still has a continuum of *infinite* rays; 2008 counting is finite walks (Theorem 31), not those rays.

---

## 3. Named leftover, not adopted

Out-degree $\ge 2$ at some reachable vertex. Extra. Not lock-side. Not a grain. Not adopted. Unique-successor type (ii) is extra and restores empty typicality of forks from one $O$.

---

## 4. Report line

- **Proved.** Theorem 32: unique-successor $R$ $\Rightarrow$ no delayed fork from $O_0$; a delayed fork needs some reachable out-degree $\ge 2$. Not a grain of $\mathrm{Obs}$.
- **Not claimed.** A law of $R$. A typicality measure. A closed “no branching without a grain.” Countability of infinite rays.
- **Named, not adopted.** Branching as a restriction on $R$.
- **Killed.** Reading type (ii) as if existence of extra edges already supplied delayed-fork typicality. Numbering this as Proposition 14 (that number is the formal-Fréchet fact). $|a|^2$. $\Phi$.
- **Open.** The law of $R$; whether some star branches; grain of $\mathrm{Obs}$.

---

## References

Strayhorn, D. The across-worlds tree as a structure. `papers/tree-as-structure.md`.

Strayhorn, D. Type-(ii) links, adopted as working motion. `papers/type-ii-adopted.md`.

Strayhorn, D. The law of $R$ is extra structure. `papers/law-of-r.md`.

Strayhorn, D. Uniformity of the law of $R$ is extra. `papers/uniform-law-of-r.md`.

Strayhorn, D. Countable out-degree is not a grain of $\mathrm{Obs}$. `papers/countable-outdegree.md`. Theorem 31.

Strayhorn, D. Observer space as a space. `papers/obs-as-a-space.md`. Proposition 14 (analytic jets are not a Fréchet-closed subset).
