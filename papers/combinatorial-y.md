# Combinatorial $y$ does not finite-support $R$ without a grain

David Strayhorn

Can a discrete/combinatorial observable (edge count, Euler characteristic, out-degree) cut the support of $R$ down to a nonempty finite typicality set of delayed forks, without being a grain and without writing $L$? Prove or kill. Do not adopt. Do not write $\Phi$. Do not put $|a|^2$. Paper 1 not rewritten.

Companion: `papers/least-action-support.md` (PR #31).

**Status.** Theorem 26: combinatorial $y$ of a *diagram* presupposes a finite (or locally finite, finitely sliced) graph. That finiteness is a grain, or a law of $R$ plus a slice, both extra. Euler of a compact Lorentzian $W$ is $\chi=0$ (Poincaré–Hopf / compact Lorentzian, `papers/ensemble-labels.md`) and does not select type-(ii) edges. Killed as a lock-side finite-support. Named as an extra filter once $R$ is already discrete, not adopted.

---

## 1. What combinatorial $y$ would be

ActionPrinciple Observation 1 used a pattern in a *finite* state-transition diagram. Theorem 25 killed continuous $y$ on lumps. The leftover is $y$ that sees the diagram as a graph: number of edges, number of vertices, out-degree, number of spanning trees, Euler characteristic of a finite subgraph, and the like.

These are functions of a graph $(V_0,R_0)$ with $V_0$ finite, or at least locally finite with a finite slice. They are not functions of a germ $(j_\infty,u)$ alone.

---

## 2. Theorem 26. Combinatorial $y$ presupposes finiteness

**Theorem 26.** None of the following, from the locked object, supplies a nonempty finite typicality set of delayed forks as the support of $R$:

1. edge count, vertex count, out-degree, or Euler characteristic of “the diagram $R$”;
2. Euler characteristic of $P(O)$, or of a compact Lorentzian $W$ containing the germ.

A combinatorial $y$ that is well-defined on finite graphs becomes available only after a grain (finite $V$) or after a locally finite law of $R$ plus a finite slice. Both are extra (Theorems 19, 22). Rounding a continuous scale to integers is a grain (Theorems 18, 24, 25).

**Proof.** (1) Fermi-slice open balls minus $\gamma_O$ are uncountable (Theorem 17). Without extra structure, $R$ may attach an uncountable star at $O$; then $\#E$, $\#V$, out-degree, and $\chi$ of the diagram are infinite or undefined, so $\mathrm{argmax}\,y$ is not a finite support. If $R$ is already locally finite, out-degree is a finite integer at each vertex, but comparing those integers across candidates still needs a finite comparison class (a slice). That slice is extra. (2) Compact Lorentzian $4$-manifolds have $\chi=0$ (Poincaré–Hopf). That value does not distinguish type-(ii) edges. $P(O)$ is typically noncompact; a compactification is extra. $\square$

**Not claimed.** No combinatorial $y$ of finite graphs exists. Once $V$ is discrete or $R$ is locally finite and sliced, edge count and Euler of the diagram are ordinary graph invariants. Extra filter on an already discrete $R$, not a way to *get* discreteness from the lock.

**Killed.** Combinatorial $y$ as a lock-side substitute for a grain. $|a|^2$ as $y$. Writing $L$ to manufacture a discrete action.

---

## 3. Report line

- **Proved.** Theorem 26: combinatorial $y$ (edge count, Euler, out-degree) does not finite-support $R$ without a grain or a law of $R$ plus a slice. $\chi=0$ on compact Lorentzian $W$ does not select type-(ii) edges.
- **Named, not adopted.** Combinatorial $y$ as a filter once $R$ is already discrete.
- **Killed.** Combinatorial $y$ as lock-side finite-support. $|a|^2$. $L$ still unwritten.
- **Open.** The law of $R$; whether to put in a grain.

---

## References

Strayhorn, D. Least action as a constraint on the support of $R$. `papers/least-action-support.md`.

Strayhorn, D. Grain is not a readout of continuous invariants. `papers/grain-not-from-invariants.md`.

Strayhorn, D. The ensemble $E(O)$ as a labeled object. `papers/ensemble-labels.md` (compact Lorentzian / Poincaré–Hopf paragraph, not Theorem 5).
