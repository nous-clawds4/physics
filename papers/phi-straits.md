# The straitjacket on $\Phi$

David Strayhorn

Constraints on any later equation of motion, recorded as theorems of what is already locked. $\Phi$ itself is not written. No $\Phi$ is proposed to save 2008. Born is not derived. Gauge stays open. $E$ is not folded into $\sim$. No replacement typicality count, no complexity bound by hand, no measure placed on $\mathrm{Obs}$.

Companions: `papers/analytic-split.md`, `papers/geodesic-lifts.md`, `papers/ensemble-labels.md`, `papers/patch-edge.md`, `papers/typicality-under-the-lock.md`.

**Status.** Under geodesic hitchhiking, typicality over branches from one $O$ is an empty set (Theorem 8). Any $\Phi$ whose solutions are real-analytic curves $I\to\mathrm{Obs}$ cannot have a thick-trunk delayed fork (Theorem 9). Restoring “agree then diverge” requires a *new* hypothesis on motion, not a theorem of the locked object. That hypothesis is named below and is not adopted.

---

## 0. What this note is not

It is not an equation of motion. It is not a choice of $\Phi$ among those that survive the straitjacket. It is not a measure on $\mathrm{Obs}$. It is not a closing of gauge.

The motion stand-in remains geodesic hitchhiking. The object remains $O=(j_\infty,u)\equiv P(O)$.

---

## 1. Theorem 8. Typicality of branches from one $O$ is empty

**Theorem 8.** Assume geodesic hitchhiking (the locked stand-in, not $\Phi$). Then:

1. Realized paths in $\mathrm{Obs}$ are parameterized by the initial germ: one curvelet $\gamma_O$ per $O$ (Prop. 3.2).
2. Members of $E_\gamma(O)$ share $\gamma_O$ on $\mathrm{int}\,P(O)$ (Thm 4). They are labels, not extra curves.
3. There is no $\sim$-split of next germs among those members at $\partial P$ (Thm 7).

Therefore the set of $\sim$-distinct hitchhiking evolutions issuing from a single $O$ has cardinality one. Typicality over *branches from one $O$* is typicality over the empty set of alternatives.

**Proof.** (1)–(3) are Prop. 3.2, Thm 4, Thm 7. A typicality theorem that counts distinct $\sim$-classes from one $O$ therefore has nothing to count. $\square$

This is the typicality-under-the-lock note, now with the boundary included. Unique-measure remains conditional on a *new* hypothesis that supplies a countable set of distinct evolutions. This note does not supply one.

---

## 2. Theorem 9. Analytic-curve $\Phi$ cannot delayed-fork

**Theorem 9.** Let $\Phi$ be any later law of motion on $\mathrm{Obs}$ whose solution curves are real-analytic maps $I\to\mathrm{Obs}$. Then $\Phi$ cannot have a thick-trunk delayed fork: two distinct solutions that agree on a positive-length initial interval and then disagree. In particular, geodesic hitchhiking in a real-analytic $W$ is one such $\Phi$ (Thm 3), and concatenating disagreeing analytic pieces at $\tau_\partial$ is not a solution of it (Thm 3 + Thm 7).

**Proof.** Theorem 2 is a statement about analytic curves in $\mathrm{Obs}$, independent of how they arise. If every solution of $\Phi$ is such a curve, Theorem 2 applies to the solution set. Geodesic lifts of analytic $W$ are analytic (Thm 3), hence fall under this. If two such lifts share $[0,\tau_\partial)$ and both extend through $\tau_\partial$, they coincide through the extension (Thm 7(2)). A concatenation of two *different* analytic germs at $\tau_\partial$ would fail to be analytic on any interval containing $\tau_\partial$, so it is not a geodesic lift of an analytic $W$. $\square$

Analytic $W$ plus geodesics is therefore an existence proof that *some* law on $\mathrm{Obs}$ lives inside the straitjacket — and, for that law, the straitjacket is the whole motion story from one $O$.

---

## 3. The remaining motion revision (not adopted)

**Named, not adopted.** A law $\Phi$ on $\mathrm{Obs}$ whose solutions are merely *piecewise* analytic (or not analytic at all), in such a way that two solutions may agree on a positive-length initial interval and then diverge, would restore “agree then diverge” as a statement about motion. That is a *new hypothesis on $\Phi$*, not a theorem of the locked object, and not a consequence of geodesic hitchhiking in analytic $W$.

Do not adopt it here. If typicality of *branches from one $O$* is still the goal, this is the remaining motion revision that would have to be argued for. It is a change of motion, not a change of the elementary object.

A $C^\infty$ but non-analytic $\Phi$ is the same kind of move: it leaves Theorem 2’s hypothesis, so it is not forced and is not written.

---

## 4. Honest remainder

Do not close gauge. Do not put a measure on $\mathrm{Obs}$.

What is left, honestly:

- Typicality of *branches from one $O$* needs a non-analytic (or piecewise-analytic) $\Phi$. The locked object plus geodesic hitchhiking does not supply those branches.
- Typicality of *many $O$* needs a measure on a space of germs. Gauge is still open, so that space is not identified. A measure written now would be a measure on an unidentified space.

Those are two different jobs. Neither is done by writing $\Phi$ to save 2008, and neither is done by folding $E$ into $\sim$.

---

## 5. Open

- Gauge.
- $\Phi$ itself.
- Whether the remaining motion revision is wanted. Not adopted.
- Countability of distinct evolutions, still not supplied.
- Classification of $\tau_\partial<\infty$ vs $=\infty$ (Thm 6), independent of this note.

---

## 6. Report line

- **Proved.** Theorem 8: under hitchhiking, one $\gamma_O$ per $O$; $E_\gamma$ shares it; no $\sim$-split at $\partial P$; typicality of branches from one $O$ is empty. Theorem 9: any $\Phi$ with analytic solution curves inherits Theorem 2; analytic $W$+geodesics is one such; concatenating disagreeing pieces at $\tau_\partial$ is not.
- **Killed.** Saving 2008 by writing a $\Phi$ inside the analytic-curve class that delayed-forks. That class cannot. Also killed: treating the remaining motion revision as already locked.
- **Named, not adopted.** Piecewise-analytic (or non-analytic) $\Phi$ as the remaining motion revision, if typicality of branches is still the goal.
- **Open.** Gauge; a measure on an unidentified space of many $O$; $\Phi$ itself.
- **Not done.** $\Phi$; Born; a replacement count; a complexity bound; a measure on $\mathrm{Obs}$.

---

## References

Strayhorn, D. Analyticity and the split. `papers/analytic-split.md`.

Strayhorn, D. Geodesic lifts are analytic curves in observer space. `papers/geodesic-lifts.md`.

Strayhorn, D. The ensemble $E(O)$ as a labeled object. `papers/ensemble-labels.md`.

Strayhorn, D. The edge of $P(O)$. `papers/patch-edge.md`.

Strayhorn, D. Typicality under the lock. `papers/typicality-under-the-lock.md`.
