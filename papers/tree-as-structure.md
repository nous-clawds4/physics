# The across-worlds tree as a structure

David Strayhorn

Make the remaining motion hypothesis precise as mathematics, on $\mathrm{Obs}=\mathcal{P}/{\sim_L}$ (Theorem 10). Do not adopt it. Do not write $\Phi$. Do not put $1/N$ on the edges. Do not derive Born. Do not reopen the jet/patch. Do not restore 2005 $3$-manifold observers.

Companions: `papers/obs-as-a-set.md`, `papers/original-two-layer.md`, `papers/analytic-split.md`, `papers/phi-straits.md`.

**Status.** An across-worlds tree is a directed graph (equivalently a transition relation) on lumps: vertices in $\mathrm{Obs}$, edges allowed one-step evolutions, paths candidate histories. Delayed forks are two paths with a common prefix then distinct vertices. Theorem 2 does not apply, because those paths are not required to be analytic curves $I\to\mathrm{Obs}$. The in-world geodesic lift $\gamma_O$ remains one per $O$; extra tree edges are whatever is *not* that lift. Grain (a discrete set of vertices) is open; Strayhorn3’s $d$-decimal truncation is a candidate, not locked. Named, not adopted.

---

## 0. What this note is not

It is not $\Phi$. It is not a probability rule. It is not a Lagrangian. It does not fold $E$ into $\sim$. It does not change the elementary object.

---

## 1. Vertices are lumps

Theorem 10: $\mathrm{Obs}=\mathcal{P}/{\sim_L}$ is a set of lumps. Typicality of many $O$, and any across-worlds tree, range over this set. $E(O)$ is occurrences of a given lump, not extra vertices.

A vertex is a point of $\mathrm{Obs}$, or of a subset (a grain; §5). Not a $3$-manifold, not a raw coordinate jet, not a pair $(W,\iota)$.

---

## 2. Definition (named, not adopted)

**Definition 7 (transition structure).** A *transition structure* on observer space is a pair $(V,R)$ where $V\subseteq\mathrm{Obs}$ and $R\subseteq V\times V$. Equivalently, a directed graph with vertex-set $V$ and an edge $O\to O'$ whenever $(O,O')\in R$.

- An *edge* is an allowed one-step evolution. No number is attached to it.
- A *path* is a finite or infinite sequence $O_0,O_1,O_2,\ldots$ in $V$ with $(O_n,O_{n+1})\in R$ for each $n$. Paths are candidate histories.
- The structure is a *tree rooted at $O$* when, for every vertex reachable from $O$, there is a unique path from $O$ to that vertex. The 2007 slogan “unique Everettian tree rooted at the jet” is this special case, if it exists. The general object is the relation $R$; uniqueness of a rooted tree is an extra property, not assumed.

This is the across-worlds layer as a structure. It is not adopted as motion. It is not $\Phi$.

---

## 3. Delayed forks, and why Theorem 2 is silent

**Definition 8 (delayed fork in a graph).** Two paths $\pi,\pi'$ *delayed-fork* if there is an index $n\ge 1$ such that $\pi_k=\pi'_k$ for all $k\le n$ and $\pi_{n+1}\ne\pi'_{n+1}$. They share a common prefix of positive length, then occupy distinct vertices.

OutcomeCounting footnote 3 is this picture, drawn in $g_{ij}(\tau)$. Definition 8 is that picture as a graph.

**Proposition 12.** Theorem 2 does not forbid delayed forks in a transition structure. Theorem 2 assumes two *real-analytic* maps $I\to\mathrm{Obs}$ that agree on a nonempty open subinterval. A graph-path is a sequence of vertices. It is not, without a further hypothesis, an analytic curve. The hypothesis of Theorem 2 is not met, so the conclusion is not forced.

Concatenating two disagreeing analytic germs at a vertex is still not an analytic curve (Theorem 3 + Theorem 7). That remains killed *for geodesic lifts of analytic $W$*. Extra tree edges are not required to be such lifts, so they are outside that kill.

---

## 4. Two kinds of edge

**(i) In-world geodesic lift.** From one $O$, Prop. 3.2 supplies a unique curvelet $\gamma_O$. Along $\gamma_O$, successive germs $O_\tau=\gamma_O(\tau)$ for $\tau$ in the lifetime. If a transition structure includes, as edges, only successive germs of geodesic lifts in analytic $W$, then from $O$ one obtains at most the vertices along $\gamma_O$ (and, at $\partial P$, no $\sim$-split: Theorem 7). Typicality of branches from one $O$ stays empty (Theorem 8). That layer is already locked as the stand-in, not as $\Phi$.

**(ii) Extra tree edges.** An edge $(O,O')\in R$ that does *not* arise as a successive pair along any geodesic lift of $O$ in a real-analytic $W$. These are the across-worlds content. Delayed forks, if they exist, use these. They are not supplied by hitchhiking. Naming them does not write $\Phi$ and does not adopt $1/N$.

A transition structure that contains only type-(i) edges is not an across-worlds tree. It is the geodesic stand-in redrawn as a graph, and Theorems 2–8 still apply to the underlying curves.

---

## 5. Grain is open

$\mathrm{Obs}$ is a set (Theorem 10). A relation $R\subseteq\mathrm{Obs}\times\mathrm{Obs}$ is therefore a set. That does not make $(V,R)$ a *combinatorial* tree with discrete branching.

If $V=\mathrm{Obs}$ and $R$ is, say, a continuum family of edges out of a vertex, the structure is a directed graph on a (likely uncountable) set. Countability of paths from one $O$, discrete $N$-way branches, and any later $1/N$, all fail to even be stated until the vertex-set is discrete enough that outgoing edges are a set one can count.

**Open, not locked.** A *grain* is a choice of $V\subseteq\mathrm{Obs}$ (or a quotient of $\mathrm{Obs}$) on which $R$ is a discrete directed graph: at most countably many edges out of each vertex, or finite. Strayhorn3’s truncation to $d$ decimal places of jet coefficients is a candidate grain. It is not adopted. Grain (jet order, what counts as physically different) remains open. Do not put a $d$ in by hand.

Without a grain, Definition 7 still makes sense as a relation on lumps. The 2007 picture of a unique rooted tree with finite branches is then an extra demand, not a theorem of $\mathrm{Obs}=\mathcal{P}/{\sim_L}$.

---

## 6. No probability on the edges

Edges are allowed transitions, not weights. $1/N$ is not written. $|a|^2$ is not written. $M$ is still occurrence count in $E(O)$, not a weight on $R$. Outcome counting on paths, if ever, waits on a grain *and* an adoption this note does not make.

---

## 7. Open

- Whether any transition structure other than type (i) is wanted. Not adopted.
- Grain: whether $V$ must be discrete, and if so which $V$. $d$-decimal not locked.
- Whether $R$ is a tree, a DAG, or a general relation (fusion of branches is a further hypothesis; 2007 allowed it as unstated).
- $\Phi$; $L$; Born; a measure on $\mathrm{Obs}$.

---

## 8. Report line

- **Named, not adopted.** Definition 7: a transition structure is a directed graph / relation $R$ on (a subset of) $\mathrm{Obs}=\mathcal{P}/{\sim_L}$. Vertices are lumps. Edges are one-step evolutions, unweighted. Paths are candidate histories.
- **Recorded.** Delayed forks = common prefix, then distinct vertices (Definition 8). Proposition 12: Theorem 2 is silent, because graph-paths need not be analytic curves. Type (i) edges = the unique $\gamma_O$. Type (ii) = extra, not geodesic lifts; that is the across-worlds content.
- **Killed.** Putting $1/N$ or $|a|^2$ on the edges. Treating the tree as $\Phi$. Restoring 2005 $3$-manifold vertices. Locking $d$-decimal grain. Reading type-(i)-only graphs as an across-worlds tree.
- **Open.** Grain; whether to adopt any $R$ beyond geodesic lifts; $\Phi$.

---

## References

Strayhorn, D. $\mathrm{Obs}$ as a set. `papers/obs-as-a-set.md`.

Strayhorn, D. Original two-layer dynamics vs the lock. `papers/original-two-layer.md`.

Strayhorn, D. Analyticity and the split. `papers/analytic-split.md`.

Strayhorn, D. The straitjacket on $\Phi$. `papers/phi-straits.md`.

Strayhorn, D. `old-manuscripts/Strayhorn3.pdf`.
