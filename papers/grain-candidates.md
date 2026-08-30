# Grain candidates (neither adopted)

David Strayhorn

Two candidates for a grain of $\mathrm{Obs}=\mathcal{P}/{\sim_L}$, so that a transition structure (Definition 7) can have discrete vertices and countable outgoing edges. Neither is locked. Do not put $1/N$. Do not write $\Phi$. Do not restore 2005 $3$-manifold observers. Do not reopen the jet/patch object.

Companions: `papers/tree-as-structure.md`, `papers/obs-as-a-set.md`, `papers/original-two-layer.md`.

**Status.** Candidate (1): Strayhorn3 $d$-decimal truncation of jet coefficients. Candidate (2): light-cone engulfing / mountain-over-horizon, restated with $P(O)$ and $\gamma_O$. (2) *can* be stated on the locked object without restoring 2005 observers; so stated, it coarsens the unique curvelet (type (i)), and does not by itself supply type-(ii) delayed forks. Grain remains open.

---

## 0. What a grain is for

`papers/tree-as-structure.md` §5: a relation $R\subseteq\mathrm{Obs}\times\mathrm{Obs}$ is a set, but a combinatorial tree with discrete $N$-way branches needs a vertex-set discrete enough to count outgoing edges. A *grain* is a choice of $V\subseteq\mathrm{Obs}$, or a quotient of $\mathrm{Obs}$, on which that counting could even be stated. It is not a change of the elementary object. Finite $k$-jets and $C^\infty$ remain closed as *objects* (Borel).

No $d$ is put in by hand. No $1/N$ is written on whatever vertices result.

---

## 1. Candidate (1): $d$-decimal truncation

Strayhorn3: approximate observer-state space by the first $d$ decimal places of each jet component, then draw directed links among those truncated states.

On the lock: let $T_d$ send a presentation (a real-analytic jet at $0$, plus $u$) to its coefficients truncated to $d$ decimals. $T_d$ descends, or fails to descend, through $\sim_L$ depending on whether pointed coordinate change commutes with truncation (it need not, exactly). So the honest grain is either

- vertices = $T_d(\mathcal{P})$, a discrete (countable) set of truncated presentations, or
- vertices = $\sim_L$-classes after some $d$-dependent thickening, which is not uniquely specified.

**Not locked.** $d$ is a free integer. Finite truncation is not the elementary observer. Borel already killed finite jets as the object; using $T_d$ as a *map out of* $\mathrm{Obs}$ is a different move, and still a choice. The $d\to\infty$ slogan is not a derivation of geodesic hitchhiking (`papers/original-two-layer.md` §4).

What it would do if adopted: a discrete $V$ on which Definition 7 can be a combinatorial graph. It does not choose the edges. Type (i) vs type (ii) remains a further hypothesis.

---

## 2. Candidate (2): engulfing / mountain-over-horizon

Corpus, as written:

- OutcomeCounting Fig. 3 / §6: $O$ cannot record a value $k$ on an extended system $X$ until $X$ lies in the past light cone of $O$. $X$ enters that cone over an interval $[\tau_a,\tau_b]$, not all at once. At each step, either the boundary of $X$ has been *engulfed* (final $k$) or it has not (running total). That was drawn as a bifurcating tree.
- ActionPrinciple: Alice and the mountain over the horizon; more of an extended region becomes visible bit by bit; $k/y/x$ as records. Least action was a pattern on that diagram, not $\Phi$.
- 2005 RHF: observer as a bounded $3$-manifold; dynamics as a random walk / tree current. Light-cone growth was tied to that object.

**Can (2) be stated using $P(O)$ and $\gamma_O$ without restoring 2005 observers?** Yes, as a filtration along the hitchhiker.

Let $\sigma_O$ be the geodesic in $P(O)$ with $\gamma_O=\pi_{P(O)}(\sigma_O)$, lifetime $[0,\tau_\partial)$. Write
$$
J(\tau)\;:=\;I^-(\sigma_O(\tau))\cap P(O)
$$
for the causal past in the patch. Then $\tau<\tau'$ implies $J(\tau)\subseteq J(\tau')$. For a closed set $X\subset P(O)$ (an “extended region in the patch”), define the engulfing time
$$
\tau_X\;:=\;\inf\{\tau\in[0,\tau_\partial):X\subset J(\tau)\}\in[0,\tau_\partial]\cup\{\infty\}.
$$
If $X$ is not pointlike, $X$ meets $\partial J(\tau)$ over an interval, not at a single $\tau$. A *running record* along $\gamma_O$ is any function of $(J(\tau),X)$ that is locally constant except when $J(\tau)$ crosses a distinguished locus in $X$ (the mountain’s next slice; the next CTC; the boundary of $X$).

That uses only $P(O)$, $\sigma_O$, and $\gamma_O$. The observer remains the lump $O=(j_\infty,u)$. It is not a bounded $3$-manifold. 2005 observers are not restored.

**So stated, (2) coarsens type (i).** Vertices change when an engulfing event happens along $\gamma_O$. The underlying curve is still the unique curvelet. Theorem 2 still applies to that curve. Theorem 7 still applies at $\partial P$. No delayed fork is created: what enters $J(\tau)$ in $P(O)$ is determined by the unique analytic metric on the patch.

**What (2) cannot do, from $P(O)$ alone.** OutcomeCounting Fig. 3B draws engulfed vs not-yet as *branches from one $O$*. That requires either type-(ii) extra edges, or a non-unique continuation of $X$ outside $P(O)$. Features that live only in some $W$ for $[W,\iota]\in E(O)$ are ensemble labels, not points of $\mathrm{Obs}$ (Theorem 10 vs Definition 2). Along $\mathrm{int}\,P(O)$ those labels are locally invisible (Theorem 4). Using them as grain vertices smuggles $E$ into $\mathrm{Obs}$. That is not a grain on lumps, and $E$ is not folded into $\sim$.

EKT-style CTCs in a fixed $W$ remain global non-uniqueness of a different kind, not a grain, and not $\Phi$.

---

## 3. Neither candidate locks grain

| Candidate | Vertices | Discrete? | Type (ii) forks from one $O$? | Adopted? |
|---|---|---|---|---|
| (1) $d$-decimal | truncated presentations, or an unspecified $d$-thickening of $\sim_L$ | countable, after a choice of $d$ | not supplied; edges still free | no |
| (2) engulfing in $P(O)$ | coarsening of $\gamma_O$ by causal-past events | events along one curve; not a census of $\mathrm{Obs}$ | no | no |
| (2) with $X$ taken from $E(O)$ | mixes occurrences into vertices | — | would smuggle $E$ into $\mathrm{Obs}$ | no |

Grain (what counts as physically different, at which jet order or causal scale) remains Geometry’s open job. Do not put a $d$ in by hand. Do not put $|a|^2$ in as $M$. Do not put $1/N$ on candidate vertices.

---

## 4. Open

- Which grain, if any.
- Whether a grain is needed only for combinatorial $R$, or also for typicality of many $O$.
- $\Phi$; $L$; Born; a measure on $\mathrm{Obs}$.

---

## 5. Report line

- **Named, not adopted.** Two grain candidates: (1) $d$-decimal truncation (Strayhorn3); (2) light-cone engulfing / mountain-over-horizon, restated with $P(O)$ and $\gamma_O$.
- **Proved / distinguished.** (2) *can* be stated on the locked object without 2005 $3$-manifold observers. So stated, it is a coarsening of the unique curvelet, not a source of type-(ii) delayed forks. Taking $X$ from $E(O)$ is not a grain on $\mathrm{Obs}$.
- **Killed.** Locking a grain in this note. Restoring 2005 observers as the object. Putting $1/N$ on either candidate. Treating engulfing-in-$P(O)$ as the 2007 across-worlds tree.
- **Open.** Grain itself.

---

## References

Strayhorn, D. `old-manuscripts/Strayhorn3.pdf`.

Strayhorn, D. Outcome counting in the many worlds interpretation. `old-manuscripts/2007-10-20-OutcomeCounting.pdf`.

Strayhorn, D. An action principle from the many-worlds interpretation. `old-manuscripts/ActionPrinciple.pdf`.

Strayhorn, D. The across-worlds tree as a structure. `papers/tree-as-structure.md`.

Strayhorn, D. $\mathrm{Obs}$ as a set. `papers/obs-as-a-set.md`.
