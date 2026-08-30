# Fusion and path-counting

David Strayhorn

Strayhorn3 fn. 4 allows merging as well as branching. 2008 / OutcomeCounting / Strayhorn3 count distinct paths for relative probability. On lumps (Definition 7; Definition 9 in PR #24, not adopted): what fusion does to “relative probability $\propto$ number of distinct paths”; when the count is well-defined; that a unique tree is extra.

Do not adopt a tree, $1/N$, a grain, a measure, $\Phi$, or Born. Do not restore the 2007 geodesic-generated tree (Theorem 11). Do not write a law of $R$ (Theorem 19). Do not smuggle $E(O)$ into $\mathrm{Obs}$. Paper 1 not rewritten.

Companions: `papers/tree-as-structure.md`, `papers/law-of-r.md` (PR #24), `papers/transition-matrix-on-lumps.md` (PR #24), `papers/original-two-layer.md`.

**Status.** Walk-count is well-defined on a DAG and fusion just adds walks (Theorem 21). Walk-count is infinite as soon as a cycle can be pumped (Theorem 20); Strayhorn3’s both-ways clause forces that as walk-count. Unique-tree is extra. $1/N$ flow is a different extra rule, and disagrees with path-count except in special graphs. None of this is adopted.

---

## 0. What is already locked / working

Type-(ii) is working across-worlds motion, abandonable. Hitchhiking remains in-world only. $R$ is a directed graph on $\mathrm{Obs}$ (Definition 7). Theorem 19 (PR #24): the law of $R$ is extra relative to the named lock-side functors. Grain, $1/N$, measure, $\Phi$, Born are not adopted.

Write a *walk* of length $k$ from $p$ to $q$ as a sequence $p=v_0,\ldots,v_k=q$ with $(v_i,v_{i+1})\in R$. A *simple path* repeats no vertex. The corpus says “a series of links joined head to tail,” i.e. a walk, and calls it a path.

---

## 1. Corpus, as written

**Strayhorn3.** Directed links from each $p$; the set of all such series from $p$ is a “branching tree-like diagram,” called the transition matrix. Fn. 4: merging is allowed as well as branching. Relative probability of evolution from $p$ to $p_i$ is proportional to the number of distinct paths linking $p$ to $p_i$. Also: no dead ends; and, because QM amplitudes are never strictly zero, a path $p_1\to p_2$ and a path $p_2\to p_1$, hence a closed walk at each $p$.

**OutcomeCounting.** Fig. 1: if a tree branches into $N$ directions, each branch has probability $1/N$; the rule is transitive (the caption’s $O_1\to O_2$ product). Postulate: outcome counting. Explicitly *not* assumed: that branch fusion is or is not allowed. The 2007 tree itself is geodesic-generated; Theorem 11 still kills that as a theorem of layer (i).

**2005 RHF.** Random walk on a unique tree diagram; at a discrete $N$-way branch, distal measure is proximal times $1/N$. The $3$-manifold object is not restored.

---

## 2. Theorem 20. Walk-count dies on a cycle

**Theorem 20.** Let $(V,R)$ be a directed graph and $p,q\in V$. If some walk from $p$ to $q$ visits a vertex that lies on a directed cycle, then there are infinitely many walks from $p$ to $q$. In particular, “relative probability $\propto$ number of distinct walks” is not a finite number.

**Proof.** Let $w$ be a walk $p\to q$ that visits $c$, and let $c=c_0\to\cdots\to c_m=c$ be a directed cycle, $m\ge 1$. For each $n\in\mathbb{N}$ concatenate $n$ copies of the cycle into $w$ at $c$. These walks are pairwise distinct. $\square$

**Corollary 20.1.** If $R$ is strongly connected and $|V|\ge 2$, then every pair has infinitely many walks. Strayhorn3’s both-ways clause (“always at least one path from $p_1$ to $p_2$” and the reverse, and a closed walk at each $p$), read as walks on $|V|\ge 2$, makes walk-count infinite. Their own path-counting rule is then not a finite relative probability.

**Simple paths are extra.** Restricting to simple paths makes the count finite on a *finite* $V$. Finite $V$ is a grain (not adopted). On a DAG, walks are already simple in the vertex-repetition sense if one forbids remaining at a vertex; the restriction is then redundant. Choosing “simple paths” to kill Theorem 20 is an extra rule, not a theorem of Definition 7.

---

## 3. Theorem 21. On a DAG, fusion just adds walks

**Theorem 21.** Let $(V,R)$ be a directed acyclic graph, $p,q\in V$, and suppose only finitely many walks from $p$ to $q$ exist (e.g. only finitely many vertices are both reachable from $p$ and can reach $q$, with finite in-degree). Let $N(p,q)$ be the number of walks from $p$ to $q$. Then $N(p,q)\in\mathbb{N}\cup\{0\}$ is well-defined. Write $N(p,p)=1$ for the empty walk. For $q\ne p$,
$$
N(p,q)\;=\;\sum_{(v,q)\in R} N(p,v).
$$
Fusion does not break the count: if two in-edges meet at $q$, both families of walks are counted.

**Proof.** Acyclicity: no walk can be pumped, so each walk is a finite vertex-sequence without a cycle, and the set of walks $p\to q$ is finite by the finiteness hypothesis. The recurrence is the last-edge partition of that finite set. $\square$

So: on a DAG, “$\propto$ number of distinct paths” is a well-defined function of pairs. Fusion *is* what makes $N(p,q)$ able to exceed $1$. That is not a typicality theorem and not a probability (no slice; see the next remainder).

---

## 4. Unique-tree is extra; $1/N$ is a different extra

**Proposition (unique-tree extra).** That $R$ be an arborescence rooted at a given $O$ (at most one walk from $O$ to each vertex) is extra structure, not a theorem of Definition 7, of hitchhiking, or of Theorem 19. The corpus allows fusion (Strayhorn3 fn. 4). OutcomeCounting does not assume fusion is forbidden. Not adopted.

On an arborescence rooted at $p$, Theorem 21 gives $N(p,q)\in\{0,1\}$. Then “$\propto N(p,q)$” is $1$ at every reachable $q$, which is not a probability on $V$ without a further slice, and is not $1/N$ flow.

**$1/N$ flow, named not adopted.** Push a mass $1$ at $p$; at a vertex with $N$ outgoing edges, split equally. On OutcomeCounting’s Fig. 1 this is the transitive $1/N$ product. On an uneven tree it disagrees with path-count: each leaf still has $N(p,\mathrm{leaf})=1$, while $1/N$ flow gives different leaves different masses. On a DAG with fusion they disagree again: path-count sums over incoming walks; $1/N$ flow splits outgoing mass and does not in general add incoming masses as integer walk-counts.

Neither rule is locked. Neither is Born. Putting $|a|^2$ on edges to force agreement is killed as a lock-side constraint.

---

## 5. Killed / not adopted

- Unique-tree, not adopted.
- Walk-count as relative probability, not adopted (ill-defined on cycles, Theorem 20; well-defined on DAGs, Theorem 21, still not a probability).
- $1/N$ flow, not adopted.
- Grain to make $V$ finite so that simple-path count is finite, killed as a lock-side constraint.
- $|a|^2$ as edge weights, killed.
- 2007 geodesic-generated tree, still killed (Theorem 11).
- A law of $R$, not written (Theorem 19).

---

## 6. Report line

- **Proved.** Theorem 20: walk-count is infinite if a cycle can be pumped. Corollary 20.1: Strayhorn3 both-ways, as walks, is ill-defined.
- **Proved.** Theorem 21: on a DAG with finitely many walks $p\to q$, $N(p,q)$ is well-defined and fusion adds walks.
- **Named, not adopted.** Unique-tree is extra. $1/N$ flow $\ne$ path-count except on special graphs.
- **Killed.** Grain or $|a|^2$ as a lock-side fix of the count.
- **Open.** Acyclicity of $R$; a slice that would make $N(p,\cdot)$ a probability; the law of $R$.

---

## References

Strayhorn, D. The across-worlds tree as a structure. `papers/tree-as-structure.md`.

Strayhorn, D. The law of $R$ is extra structure. `papers/law-of-r.md`.

Strayhorn, D. The transition matrix as a structure on lumps. `papers/transition-matrix-on-lumps.md`.

Strayhorn, D. `old-manuscripts/Strayhorn3.pdf`.

Strayhorn, D. Outcome counting. `old-manuscripts/2007-10-20-OutcomeCounting.pdf`.

Strayhorn, D. Relative histories formulation I. `old-manuscripts/2005-01-05-RHF-I.pdf`.
