# The law of $R$ is extra structure

David Strayhorn

What can constrain which type-(ii) edges exist, without a grain, $1/N$, a measure, $\Phi$, or $|a|^2$. Do not write a law for $R$. Do not put a $d$ or $|a|^2$ in by hand. Do not smuggle $E(O)$ into $\mathrm{Obs}$. Do not restore the 2007 geodesic-generated tree. Do not restore 2005 $3$-manifold observers. Paper 1 not rewritten.

Companions: `papers/type-ii-adopted.md`, `papers/tree-as-structure.md`, `papers/remainder.md`, `papers/original-two-layer.md`.

**Status.** Proposition 13 already: locked data at $O$ do not determine type-(ii) edges. Theorem 19: none of the *named* lock-side functors (listed data at $O$, open neighborhoods, continuous $f:\mathrm{Obs}\to\mathbb{R}^n$) supply countable type-(ii) successors of lumps. The law of $R$ is extra relative to those. Not a blanket “no map.” Corpus candidates (2005 random walk, Strayhorn3 transition matrix, ActionPrinciple least-action pattern) are named, not adopted. Grain, $E$-smuggling, or Born stay killed as lock-side constraints. Definition 9 stays.

---

## 0. What is already locked / working

Type-(ii) links are working across-worlds motion on $\mathrm{Obs}=\mathcal{P}/{\sim_L}$, abandonable. Hitchhiking remains in-world only. Theorem 11 still kills the 2007 geodesic-generated tree as a theorem of layer (i). Delayed forks are graph-paths (Definition 8); Theorem 2 is silent (Proposition 12). $\sim_L$ is pointed germ equivalence; unpointed $\mathrm{Diff}(M)$ is excluded. Grain, $1/N$, measure, and $\Phi$ are not adopted.

---

## 1. Proposition 13 already, and named functors

**Proposition 13** (`papers/type-ii-adopted.md`): the lump, the patch $P(O)$, the curvelet $\gamma_O$, and the ensemble $E(O)$ determine at most type-(i) successive pairs. They do not determine a type-(ii) edge $(O,O')$ with $O'$ not on $\gamma_O$. Not renumbered.

**Theorem 19.** None of the named lock-side functors

1. the listed data at $O$: $j_\infty$, $u$, $P(O)$, $\gamma_O$, $E(O)$ (Proposition 13);
2. nonempty open neighborhoods in the Fermi-slice topology (Theorem 17);
3. finitely many continuous maps $f:\mathrm{Obs}\to\mathbb{R}^n$ on a nonempty connected open (Theorem 18)

supplies a countable set of type-(ii) successors of lumps. The law of $R$ is extra relative to those functors.

**Proof.** (1) is Proposition 13. (2) Theorem 17: every nonempty open $U\ni O$ has $U\setminus\gamma_O$ uncountable, so “successors $=$ a neighborhood” is a continuum, not a countable set. (3) Theorem 18: finitely many continuous functions on a connected open yield one class or a continuum, so “successors $=$ nearby lumps with the same (or nearby) continuous invariants” does not grain. $\square$

A neighborhood-*constraint* (targets must lie in $U$, plus a further discrete cut) is still extra: the cut is the grain, or something else not locked. It is not a law of $R$ from the topology.

**Not claimed.** There is no map of this data to successor-sets. The empty assignment $\mathrm{succ}(O)=\emptyset$ and the constant assignment $\mathrm{succ}(O)=\{O_{\mathrm{Mink}}\}$ are maps of the data. They are trivial. They do not give a countable typicality set of delayed forks, and they are not a law of $R$. They kill a blanket impossibility.

**Third disjunct dropped.** The previous wording forbade a “canonical nonempty proper subset of a neighborhood.” That is false. Ricci-flat germs in a Fermi ball are selected by the jet (the Einstein condition is a condition on $j_\infty$) and form a nonempty proper subset: nearby non-Einstein germs exist. Weyl $=0$ and Petrov walls similarly. Those subsets remain uncountable (they do not grain). They are why the disjunct fails, not a successor-law.

**Discrete algebraic invariants.** Petrov type and $\dim$ of the Killing algebra are locked functors Theorem 18 does not cover (they are not continuous $\mathbb{R}^n$-valued functions). There are finitely many Petrov types; each type-class in a Fermi ball is still a continuum of lumps. Finite type, continuum fibre: they fail to grain. Not a counterexample to the intended remainder (countable type-(ii) successors still not supplied). Not folded into Theorem 19 as a fourth named functor.

---

## 2. Corpus, as written (not a new law)

**Strayhorn3.** After truncating jet coefficients to $d$ decimals:

> Given any point $p$ in state space, we can draw a collection of directed links, each of which starts at $p$ and ends at some other point in state space. \ldots Starting at any given point $p$, the set of all paths that start at $p$ will construct a branching tree-like diagram. \ldots We will call this the transition matrix. \ldots the time dependent evolution is determined entirely by the local structure of the tree diagram within an infinitesimal ball around the point $p$ in state space. \ldots the relative probability of evolution to point $p_i$ is proportional to the number of distinct paths linking $p$ to $p_i$.

Merging is allowed as well as branching (fn. 4). The $d\to\infty$ slogan that “each path becomes a geodesic” is not the in-$W$ parallel-transport sentence (`papers/original-two-layer.md` §4).

**2005 RHF.** The observer is a bounded $3$-manifold $O$. Evolution is a random walk along a unique tree diagram in $O$-state space. Probability measure $1$ at the root; at a branch point with $N$ discrete branches, each distal branch gets the proximal measure times $1/N$. As $N\to\infty$, a “current” through state space. The $3$-manifold object is not restored.

**2007 OutcomeCounting.** The Everettian tree is generated by running geodesics in each world in $M_O$ and superposing the lifts. Theorem 11: not a theorem of hitchhiking. Not remaining motion.

**ActionPrinciple.** Observation 1: patterns in a state-transition diagram can extremize an observable $y$. Exact $S$ deferred; $L$ never written. Least action is a tree pattern, not $\Phi$.

---

## 3. Named candidates, not adopted

| Candidate | What it would be on lumps | Extra? | Adopted? |
|---|---|---|---|
| Strayhorn3 transition matrix | Directed links among (truncated) lumps; $R$ plus a grain $d$ | Yes: $d$, and the links themselves | no |
| 2005 random walk | Walk on a discrete tree in observer-state space, $1/N$ at branches | Yes: $3$-manifold object, $1/N$, discrete $N$ | no |
| Least-action pattern | A constraint on *which diagrams* appear, via extremizing $y$ | Yes: the pattern class; $L$ still unwritten | no |
| Neighborhood-law | Type-(ii) targets fill an open set | Does not pick a countable $R$ (Theorem 17) | no |
| Invariant-law | Targets selected by continuous $f:\mathrm{Obs}\to\mathbb{R}^n$ | Does not grain (Theorem 18) | no |

**Killed as constraints from the lock.**

- Any rule that first puts in a $d$ or a mesh $\delta$ (grain by hand).
- Any rule that takes targets from $E(O)$ (occurrences of the *same* lump are not extra vertices; that smuggles $E$ into $\mathrm{Obs}$).
- Any rule that uses $|a|^2$ or Born weights to pick or weight edges ($M$ is occurrence count, not Born).
- The 2007 geodesic-generated tree (Theorem 11).

The least-action pattern and the transition matrix, stripped of $1/N$ and of $d$, reduce to: *there is an $R$*. That is the working hypothesis already. They do not further determine which pairs lie in $R$.

---

## 4. Theorem 19, as remainder

**Theorem 19 (restated).** Relative to the named lock-side functors of §1, the type-(ii) relation $R$ is extra structure, of the same kind as grain. Not a claim that no map of the data exists.

Type-(ii) *existence* is working, abandonable. The *law* is not written. $1/N$ is not put in to fill the gap.

---

## 5. Report line

- **Already Prop. 13.** Locked data at $O$ do not determine extra edges. Not renumbered.
- **Proved.** Theorem 19: named lock-side functors (data at $O$, open neighborhoods, continuous $f:\mathrm{Obs}\to\mathbb{R}^n$) do not supply countable type-(ii) successors of lumps. Law of $R$ extra relative to those.
- **Dropped.** Blanket “no map”; the third disjunct (canonical nonempty proper subset of a neighborhood). Ricci-flat / Weyl $=0$ / Petrov walls are why.
- **Recorded.** Discrete algebraic invariants (Petrov type, $\dim$ Killing) fail to grain; not a counterexample; not a fourth functor in Theorem 19. Corpus transition matrix / random walk / least-action pattern, not adopted. Definition 9 stays.
- **Killed.** Grain, $E$-smuggling, or Born as a lock-side constraint on $R$. 2007 geodesic-generated tree.
- **Open.** The law of $R$; whether to abandon type (ii).

---

## References

Strayhorn, D. Type-(ii) links, adopted as working motion. `papers/type-ii-adopted.md`.

Strayhorn, D. Neighborhoods are not a countable $N$. `papers/neighborhood-uncountable.md`.

Strayhorn, D. Grain is not a readout of continuous invariants. `papers/grain-not-from-invariants.md`.

Strayhorn, D. Original two-layer dynamics vs the lock. `papers/original-two-layer.md`.

Strayhorn, D. `old-manuscripts/Strayhorn3.pdf`.

Strayhorn, D. Outcome counting. `old-manuscripts/2007-10-20-OutcomeCounting.pdf`.

Strayhorn, D. Relative histories formulation I. `old-manuscripts/2005-01-05-RHF-I.pdf`.

Strayhorn, D. An action principle from the many-worlds interpretation. `old-manuscripts/ActionPrinciple.pdf`.
