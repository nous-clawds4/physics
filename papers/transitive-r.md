# Transitivity of $R$ is extra

David Strayhorn

Live hole is the law of $R$, not a grain. Irreflexivity (`papers/irreflexive-r.md`, on main via #64) is extra: no self-loops. Acyclicity (`papers/acyclicity-of-r.md`, on main) is extra for finite $N$. Transitivity is a different extra: $(O,O^\prime)\in R$ and $(O^\prime,O^{\prime\prime})\in R$ imply $(O,O^{\prime\prime})\in R$. A DAG need not be transitive (missing shortcuts). A transitive relation can have cycles (an equivalence on a pair). Distinct from irreflexivity, from acyclicity, from unique-tree. Do not adopt. Do not invent a grain. Not $\Phi$. No $|a|^2$. No $L$. No $1/N$. Paper 1 not rewritten.

Companions: `papers/irreflexive-r.md`, `papers/acyclicity-of-r.md`, `papers/fusion-and-path-counting.md` (Theorems 20--21), `papers/countable-outdegree.md` (Theorem 31), `papers/extra-structure.md`.

**Status.** Named leftover. Walk-count $N(p,q)$ counts walks, not the presence of a shortcut edge. Transitivity would collapse walks of length $\ge 2$ into length-$1$ edges; that is a different typicality rule, not path-count on Def 9. Empty $R$ is transitive. A single edge is transitive. They are maps and not the 2008 job. Not lock-side (Proposition 13, Theorem 19). Not a grain of $\mathrm{Obs}$. Not adopted.

---

## 1. Three extras, not one

**Irreflexivity.** No $(O,O)$. On main via #64. Not reopened.

**Acyclicity.** A DAG. Extra for finite $N$. Already named. Not reopened.

**Transitivity.** Shortcuts exist. Extra. A transitive DAG is a strict partial order only after irreflexivity too; that bundle is extra-on-extra, not adopted here.

Theorem 20: a pumpable cycle makes $N$ infinite. Transitivity does not kill that (a complete relation on two points is transitive, reflexive, and has $N=\infty$). Theorem 31 still needs countable out-degree for a countable walk-set; transitivity can *raise* out-degree (shortcuts).

---

## 2. Not lock-side and not a grain

Locked data at $O$ do not determine type-(ii) edges (Proposition 13, Theorem 19). Hitchhiker $\tau$ is a linear order along $\gamma_O$ (type (i)); that does not timestamp type (ii) (Theorem 23(1)) and does not force $R$ to be transitive.

Transitivity does not grain $\mathrm{Obs}$. $V$ may remain a continuum. It does not make $\mathrm{Path}(O_0)$ countable. It does not finite-support $R$.

**Not claimed.** No transitive $R$ exists. Empty $R$ is transitive. A singleton edge is transitive. They are maps and not the 2008 job.

---

## 3. Named leftover, not adopted

Transitivity of $R$. Extra. Distinct from irreflexivity and from acyclicity. Not a grain. Not lock-side. Not adopted. Paper 1 not rewritten.

---

## 4. Report line

- **Named, not adopted.** Transitivity of $R$. Live hole is still the law of $R$.
- **Killed.** Reading hitchhiker $\tau$ as type-(ii) transitivity. Reading acyclicity as transitivity. Reading walk-count as already transitive. Inventing a grain so transitive classes are countable. $|a|^2$. $\Phi$.
- **Open.** The law of $R$; whether $R$ is transitive; grain of $\mathrm{Obs}$.

---

## References

Strayhorn, D. Irreflexivity of $R$ is extra. `papers/irreflexive-r.md`. On main via #64.

Strayhorn, D. Acyclicity of $R$ is extra. `papers/acyclicity-of-r.md`.

Strayhorn, D. Fusion and path-counting. `papers/fusion-and-path-counting.md`. Theorems 20--21.

Strayhorn, D. Countable out-degree is not a grain of $\mathrm{Obs}$. `papers/countable-outdegree.md`. Theorem 31.

Strayhorn, D. Extra structure the 2008 typicality job still needs. `papers/extra-structure.md`. Proposition 13, Theorem 19.
