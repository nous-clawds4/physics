# Circularity as a named remaining lock

David Strayhorn

The sentence that stays: count first, then typicality, then the measure that was used to count. What would resolve it *without* putting $|a|^2$ in as $M$. Name candidates. Do not adopt. Not $\Phi$. No $L$. Paper 1 not rewritten.

Companions: `papers/unique-measure-conditions.md` (PR #43), `papers/extra-structure.md`, `papers/typicality-under-the-lock.md`.

**Status.** Unique-measure-from-typicality is circular unless the count that feeds typicality is not already a measure on $\mathrm{Obs}$. That circularity is a named remaining lock, not a theorem that unique-measure is impossible. Candidates below are extra. $|a|^2$ as $M$ is killed.

---

## 1. The sentence

2008 wanted a unique measure from typicality of a countable set of distinct evolutions. “Typical” is a claim about a measure (or a counting measure). “Count the evolutions, take $1/N$” uses that count as the measure. If the typicality set was itself picked by a measure, the measure is an input, not an output.

Under the lock the typicality set from one $O$ is empty without extra structure (Theorem 8). The circularity is what remains *after* one puts in the extras of `papers/unique-measure-conditions.md`: even with a grain and a law of $R$, one still owes an account of why the count is not presupposing the measure being derived.

---

## 2. Named candidates (none adopted)

1. **Combinatorial count first.** A grain supplies a nonempty finite (or countable) set of evolutions; $N$ is graph-theoretic (walk-count on a DAG, or a unique tree). Typicality is equal weight $1/N$ by counting vertices or paths, not by a measure on $\mathrm{Obs}$. Circularity avoided because no measure on $\mathrm{Obs}$ is used to count. Extra: grain, law of $R$, tree-or-DAG, and the rule $1/N$ (which is not path-count except on special graphs). This is the 2008 illustration’s shape. Not lock-side (Theorems 19–22, 26). Not adopted.

2. **Measure first.** Put a measure $\mu$ on $\mathrm{Obs}$ (or on a grain), then read typicality as $\mu$-almost every. Unique-measure is then an input. The 2008 *derivation* of unique-measure from typicality is dropped. Extra. Fermi-slice does not supply $\mu$ (Theorems 16–17). Not adopted.

3. **Self-consistent $\mu$.** A measure that reproduces itself as the counting measure of its own typical set. Extra as a fixed-point problem. $|a|^2$ as that $\mu$ (as $M$) is killed. No other fixed point is written. Not adopted.

4. **Abandon unique-measure-from-typicality.** Keep hitchhiking (and type (ii) or not) without claiming a derived unique measure. Named leftover of `papers/abandon-type-ii.md` plus dropping the 2008 output. Not taken here.

**Not a candidate.** $|a|^2$ as $M$. Union-of-ensembles as Hilbert space. $\Phi$ as the measure.

---

## 3. What stays

Until one of (1)–(4) is adopted, the circularity sentence stays. Combinatorial count first is the only named candidate that still looks like 2008 without putting a measure (or $|a|^2$) in as input. It is extra in every slot (grain, $R$, tree, $1/N$).

**Not claimed.** Circularity is a contradiction in the lock. The lock does not force (1)–(4). Empty typicality gives a unique trivial measure and is not the 2008 job.

---

## 4. Report line

- **Named remaining lock.** Circularity of count-then-typicality-then-the-measure-used-to-count.
- **Named, not adopted.** Combinatorial count first; measure first; self-consistent $\mu$; abandon unique-measure-from-typicality.
- **Killed.** $|a|^2$ as $M$ as a resolver. $\Phi$ as that resolver.
- **Open.** Whether to put in (1), or to drop the 2008 derivation.

---

## References

Strayhorn, D. Unique-measure as named conditions. `papers/unique-measure-conditions.md` (PR #43).

Strayhorn, D. Extra structure the 2008 typicality job still needs. `papers/extra-structure.md`.

Strayhorn, D. Typicality under the lock. `papers/typicality-under-the-lock.md`.

Strayhorn, D. Fusion and path-counting. `papers/fusion-and-path-counting.md`.
