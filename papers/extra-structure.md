# Extra structure the 2008 typicality job still needs

David Strayhorn

Not a new theorem. Inventory of *extra* structure, after the lock-side support well (Theorem 30). Grain, law of $R$, slice, tree-or-DAG, measure. Assumptions, not theorems. Do not adopt any of them here. No $\Phi$, no $|a|^2$, no $L$. Paper 1 not rewritten.

Companion to `papers/remainder.md`. Theorems 19–33 on main. Uniformity: `papers/uniform-law-of-r.md`. Countable out-degree: `papers/countable-outdegree.md`. Locality: `papers/local-law-of-r.md`. No dead ends: `papers/dead-ends-and-rays.md`. Acyclicity: `papers/acyclicity-of-r.md`. Finite ancestors: `papers/finite-ancestors.md`. Markov law of $R$: `papers/markov-law-of-r.md`. Measurability: `papers/measurable-r.md`. Closed-graph: `papers/closed-graph-r.md`. Compact-valued stars: `papers/compact-stars.md`. Properness leftover (1): `papers/proper-r.md` (on main via #58). Open-graph: `papers/open-graph-r.md` (on main via #59). Measurable selection: `papers/measurable-selection.md`. Irreflexivity: `papers/irreflexive-r.md`. Selection theorems: `papers/selection-theorems-extra.md`. Transitivity: `papers/transitive-r.md`. Asymmetry: `papers/asymmetric-r.md`. Totality: `papers/total-r.md` (on main via #68). Antisymmetry: `papers/antisymmetric-r.md` (on main via #70). Well-foundedness: `papers/well-founded-r.md` (on main via #71).

**Status.** 2008 wanted a unique measure from typicality of a countable set of distinct evolutions. Hitchhiking does not supply those evolutions from one $O$ (Theorem 8). Named lock-side functors do not (Theorem 19). Named support constraints do not finite-support $R$ without a grain (Theorems 25–30). What remains is extra structure. Unique-measure stays conditional. This is an inventory, not a sit.

---

## Extra structure, listed

To do the 2008 job *on this object*, one would still have to assume at least:

1. **Grain of $\mathrm{Obs}$** (or some other discrete cut of lumps). Extra. Not a readout of continuous invariants (Theorem 18). Not neighborhoods (Theorem 17). Not integer bins, Morse, conjugate/cut, or $I^+$ (Theorems 28–30). $d$-decimal is combinatorial and not put in by hand. Not required for countable *paths* from one $O$: countable out-degree of $R$ already makes $\mathrm{Path}(O_0)$ countable (Theorem 31).

2. **A law of $R$.** Which type-(ii) pairs are edged. Extra relative to named lock-side functors (Theorem 19). The leftover named support constraints do not supply it without a grain (Theorem 30). Uniformity extra (`papers/uniform-law-of-r.md`). Countable out-degree extra (Theorem 31) and is not a grain of $\mathrm{Obs}$; $\mathrm{Path}$ is finite walks. Branching extra (Theorem 32). Locality extra (`papers/local-law-of-r.md`). No dead ends extra (`papers/dead-ends-and-rays.md`). Countable in-degree extra (Theorem 33). Acyclicity extra for finite $N$, distinct from unique-tree, not for a countable walk-set (`papers/acyclicity-of-r.md`). Finite $\mathrm{Anc}(q)$ extra for $N\in\mathbb{N}$ (Theorem 21 example; `papers/finite-ancestors.md`). Markov (one-step) is Definition 9; history-dependent is extra-on-extra (`papers/markov-law-of-r.md`). Measurability extra, toward a measure, not a grain (`papers/measurable-r.md`). Closed-graph extra, distinct from locality and Borel (`papers/closed-graph-r.md`). Compact-valued stars extra, distinct from closed-graph (`papers/compact-stars.md`). Leftover (1) extra (`papers/proper-r.md`, on main via #58). Open-graph extra, dual of closed-graph (`papers/open-graph-r.md`, on main via #59). Measurable selection extra-on-extra, a function not the graph (`papers/measurable-selection.md`). Irreflexivity extra (`papers/irreflexive-r.md`). Selection-theorem hypotheses extra-on-extra, not a law of $R$ (`papers/selection-theorems-extra.md`). Transitivity extra (`papers/transitive-r.md`). Asymmetry extra; irreflexive+transitive already implies asymmetric (`papers/asymmetric-r.md`). Totality extra; tournament extra-on-extra; does not force uncountable out-degree (`papers/total-r.md`, on main via #68). Antisymmetry extra, distinct from asymmetry; on already-irreflexive $R$ equivalent to it (`papers/antisymmetric-r.md`, on main via #70). Well-foundedness extra, distinct from acyclicity and from finite $\mathrm{Anc}(q)$ (`papers/well-founded-r.md`, on main via #71). Empty and $\{O_{\mathrm{Mink}}\}$ are laws; they are not the 2008 job.

3. **A slice / clock**, if path-count is to be a probability of type-(ii) targets. Named non-slices fail (Theorem 22). Hitchhiker $\tau$ is type (i) only (Theorem 23(1)). Fermi-slice distance is a continuous scale (Theorem 24). A locally finite one-step out-neighborhood is a finite slice *from* a law of $R$ (extra). Rounding a continuous scale is a grain.

4. **Tree or DAG**, if walk-count is the typicality rule. Unique-tree extra. On a DAG, $N(p,q)$ is well-defined (Theorem 21). On a pumpable cycle it is infinite (Theorem 20). Acyclicity (a DAG) extra for finite $N$, distinct from unique-tree (`papers/acyclicity-of-r.md`). Finite $\mathrm{Anc}(q)$ extra for $N\in\mathbb{N}$ (Theorem 21 example; `papers/finite-ancestors.md`). $1/N$ flow is a different extra rule, not path-count except on special graphs.

5. **A measure on $\mathrm{Obs}$**, if typicality of many $O$ is wanted instead of (or after) delayed forks from one $O$. Fermi-slice topology exists (Theorem 16) and does not count (Theorem 17). Measurability of $R$ is extra toward a measure, not a measure (`papers/measurable-r.md`). A measure is not written. Circularity of “count first, then typicality, then the measure that was used to count” is not resolved.

Type-(ii) links themselves are extra working motion, abandonable (`papers/type-ii-adopted.md`). They are presupposed by (1)–(4) as stated. Without them the job is not delayed-fork typicality from one $O$; see `papers/abandon-type-ii.md`.

Those five are extra. None is a theorem of the jet/patch. Unique-measure stays conditional on them.

---

## Named leftover, not adopted

Grain of $\mathrm{Obs}$ extra. Law of $R$ extra. Uniformity extra. Countable out-degree extra, not a grain of $\mathrm{Obs}$ (Theorem 31). Branching extra (Theorem 32). Locality extra. No dead ends extra. Countable in-degree extra (Theorem 33). Acyclicity extra for finite $N$, distinct from unique-tree. Finite $\mathrm{Anc}(q)$ extra for $N\in\mathbb{N}$. Markov (one-step) is Definition 9; history-dependent extra-on-extra. Measurability extra, toward a measure, not a grain. Closed-graph extra, distinct from locality and Borel. Compact-valued stars extra, distinct from closed-graph. Leftover (1) extra. Open-graph extra, dual of closed-graph. Measurable selection extra-on-extra. Irreflexivity extra. Selection-theorem hypotheses extra-on-extra. Transitivity extra. Asymmetry extra. Totality extra. Tournament extra-on-extra. Antisymmetry extra, distinct from asymmetry. Well-foundedness extra. Slice extra. Unique-tree extra; DAG vs cycle open. Measure extra. Type-(ii) working, abandonable. Not $\Phi$. Not $L$. Not $|a|^2$. Not $1/N$ as a lock-side rule.

---

## Report line

- **Inventory.** Grain, law of $R$, slice, tree-or-DAG, measure: extra structure for the 2008 typicality job on this object. Not theorems of the lock.
- **Not a sit.** The lock-side support well is dry (Theorem 30). These five remain.
- **Open.** Whether to put any of them in; whether to abandon type (ii).

---

## References

Strayhorn, D. Remainder inventory. `papers/remainder.md`.

Strayhorn, D. The law of $R$ is extra structure. `papers/law-of-r.md`.

Strayhorn, D. Named leftover support constraints do not finite-support $R$ without a grain. `papers/support-without-grain.md`.

Strayhorn, D. Type-(ii) links, adopted as working motion. `papers/type-ii-adopted.md`.

Strayhorn, D. What abandoning type-(ii) leaves. `papers/abandon-type-ii.md`.

Strayhorn, D. Uniformity of the law of $R$ is extra. `papers/uniform-law-of-r.md`.

Strayhorn, D. Countable out-degree is not a grain of $\mathrm{Obs}$. `papers/countable-outdegree.md`.

Strayhorn, D. Branching is extra. `papers/branching-extra.md`. Theorem 32.

Strayhorn, D. Locality of $R$ in the Fermi-slice topology is extra. `papers/local-law-of-r.md`.

Strayhorn, D. No dead ends is extra; König rays may be a continuum. `papers/dead-ends-and-rays.md`.

Strayhorn, D. Countable in-degree is extra. `papers/countable-indegree.md`. Theorem 33.

Strayhorn, D. Acyclicity of $R$ is extra. `papers/acyclicity-of-r.md`.

Strayhorn, D. A finite ancestor set is extra. `papers/finite-ancestors.md`.

Strayhorn, D. A Markov (one-step) law of $R$ is already Definition 9. `papers/markov-law-of-r.md`.

Strayhorn, D. Measurability of $R$ in the Fermi-slice product is extra. `papers/measurable-r.md`.

Strayhorn, D. Closed-graph $R$ in the Fermi-slice topology is extra. `papers/closed-graph-r.md`.

Strayhorn, D. Compact-valued stars in the Fermi-slice topology are extra. `papers/compact-stars.md`. Theorem 16: `papers/obs-as-a-space.md`. Theorem 17: `papers/neighborhood-uncountable.md`.

Strayhorn, D. Properness leftover (1). `papers/proper-r.md`. On main via #58.

Strayhorn, D. Open-graph $R$ is extra. `papers/open-graph-r.md`. On main via #59.

Strayhorn, D. Totality of $R$ is extra. `papers/total-r.md`. On main via #68.

Strayhorn, D. Antisymmetry of $R$ is extra. `papers/antisymmetric-r.md`. On main via #70.

Strayhorn, D. Well-foundedness of $R$ is extra. `papers/well-founded-r.md`. On main via #71.
