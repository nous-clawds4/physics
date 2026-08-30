# Converse well-foundedness of $R$ is extra

David Strayhorn

Live hole is the law of $R$, not a grain. Well-foundedness (`papers/well-founded-r.md`, leftover, not this PR): no infinite *descending* chain. No dead ends (`papers/dead-ends-and-rays.md`): every lump has a successor; König rays may still be a continuum. Converse well-foundedness is a different extra: no infinite *ascending* chain. There is no sequence $(O_n)_{n\in\mathbb{N}}$ with $(O_n,O_{n+1})\in R$ for all $n$. Well-foundedness does not imply it (the naturals with $n\,R\,n{+}1$ are well-founded and have an infinite ascending chain). No dead ends does not imply it (seriality *supplies* successors; it does not cut rays). Do not adopt. Do not invent a grain. Not $\Phi$. No $|a|^2$. No $L$. No $1/N$. Paper 1 not rewritten.

Companions: `papers/well-founded-r.md`, `papers/dead-ends-and-rays.md`, `papers/acyclicity-of-r.md`, `papers/finite-ancestors.md`, `papers/type-ii-clock.md` (Theorem 23(1)), `papers/extra-structure.md`.

**Status.** Named leftover. Hitchhiker $\tau$ along $\gamma_O$ is a forward chain (type (i)). That does not timestamp type (ii) (Theorem 23(1)) and does not force $R$ to be converse well-founded. Empty $R$ is converse well-founded. A finite DAG is. They are maps and not the 2008 job. Not lock-side (Proposition 13, Theorem 19). Not a grain of $\mathrm{Obs}$. Not adopted.

---

## 1. Distinct from well-foundedness and from König

**Well-foundedness.** No infinite descending chain. Leftover, not this PR. Dual cut. Not reopened.

**Acyclicity.** No finite directed cycle. Extra for finite $N$. The naturals with $n\,R\,n{+}1$ are acyclic and not converse well-founded. Not reopened.

**No dead ends / König.** Extra for infinite *forward* rays if the graph is locally finite and infinite (`papers/dead-ends-and-rays.md`). Seriality does not forbid those rays. Converse well-foundedness forbids the chain itself, locally finite or not. Distinct. Not reopened.

**Finite $\mathrm{Anc}(q)$.** Backward and finite. Dual of a finite *descendant* set, which would be a further extra, not this one. Not reopened.

**Converse well-foundedness.** No infinite ascending chain. Extra. Implies acyclicity (a cycle loops into an infinite ascending walk). Does not imply well-foundedness. Does not finite-support $R$. Does not make $\mathrm{Path}(O_0)$ countable (Theorem 31 is countable out-degree). A converse well-founded $R$ may still have a continuum of finite walks from a root if out-degree is uncountable.

2008 counts finite walks, not infinite rays. Cutting infinite ascending chains is still extra structure on $R$, not a grain of $\mathrm{Obs}$.

---

## 2. Not lock-side and not a grain

Locked data at $O$ do not determine type-(ii) edges (Proposition 13, Theorem 19). In-world geodesics do not reverse $\tau$. That does not timestamp type (ii) (Theorem 23(1)).

Converse well-foundedness does not grain $\mathrm{Obs}$. $V$ may remain a continuum.

**Not claimed.** No converse well-founded $R$ exists. Empty $R$ is converse well-founded. A finite DAG is. They are maps and not the 2008 job.

---

## 3. Named leftover, not adopted

Converse well-foundedness of $R$. Extra. Distinct from well-foundedness and from no dead ends / König. Not a grain. Not lock-side. Not adopted. Paper 1 not rewritten.

---

## 4. Report line

- **Named, not adopted.** Converse well-foundedness of $R$. Live hole is still the law of $R$.
- **Killed.** Reading hitchhiker $\tau$ as type-(ii) converse well-foundedness. Reading well-foundedness as the same extra. Reading no-dead-ends or König as converse well-foundedness. Inventing a grain so converse well-founded classes are countable. $|a|^2$. $\Phi$.
- **Open.** The law of $R$; whether $R$ is converse well-founded; grain of $\mathrm{Obs}$.

---

## References

Strayhorn, D. Well-foundedness of $R$ is extra. `papers/well-founded-r.md`. Leftover, not this PR.

Strayhorn, D. No dead ends is extra; König rays may be a continuum. `papers/dead-ends-and-rays.md`.

Strayhorn, D. Acyclicity of $R$ is extra. `papers/acyclicity-of-r.md`.

Strayhorn, D. A finite ancestor set is extra. `papers/finite-ancestors.md`.

Strayhorn, D. Type-(ii) clock. `papers/type-ii-clock.md`. Theorem 23(1).

Strayhorn, D. Extra structure the 2008 typicality job still needs. `papers/extra-structure.md`. Proposition 13, Theorem 19.
