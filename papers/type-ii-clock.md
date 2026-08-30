# Type-(ii) does not inherit hitchhiker $\tau$

David Strayhorn

Can a type-(ii) edge inherit any locked clock without choosing a $W$ from $E(O)$? Hitchhiker $\tau$ is in-world only. Kill $E$-smuggling. Name leftover candidates. Do not adopt a slice, a tree, $1/N$, a grain, a measure, $\Phi$, or Born. Do not write a law of $R$. Do not restore the 2007 geodesic-generated tree. Paper 1 not rewritten.

Companions: `papers/counting-needs-a-slice.md`, `papers/fusion-and-path-counting.md`, `papers/ensemble-labels.md`.

**Status.** Theorem 23(1): hitchhiker $\tau$ does not label type-(ii) targets (packaging of Theorem 22(1)). (2a): an extra $W$ from $E(O)$ is $E$-smuggling. (2b): $W=P(O)$ is locked; infimal proper time $p\to q$ in the patch, for $q$ off $\sigma_O$, is lock-side, not unique in $(O,O')$, and not a general type-(ii) clock. Not a closed “no real function of $(O,O')$.” Leftover candidates (generation, Lyapunov, walk-length) are extra, not adopted.

---

## 0. The locked clock, and where it lives

Layer (i): geodesic hitchhiking. Proper time $\tau$ is the parameter of $\sigma_O$ in $P(O)$, equivalently of $\gamma_O$ in $\mathrm{Obs}$. It is defined *along that curvelet*. $E_\gamma$ members share $\gamma_O$ (Theorem 4), so they share that $\tau$. Lifetime $\tau_\partial$ is the same clock, possibly finite (Theorems 6–7).

A type-(ii) edge $(O,O')$ is, by definition, not a geodesic lift: $O'$ does not lie on $\gamma_O$. The hitchhiker parameter does not label $O'$. Theorem 22: hitchhiker $\tau$ is a named non-slice. This note asks whether any *other* locked time-parameter still attaches to the edge without picking an extra $W$.

---

## 1. Theorem 23

**Theorem 23.** Let $(O,O')$ be type (ii). Write $p$ for the basepoint of $P(O)$.

1. Hitchhiker $\tau$ along $\gamma_O$ does not label $O'$. (Packaging of Theorem 22(1).)
2. Split:
   - *(2a) Extra $W$.* A proper-time difference along a causal curve in a spacetime $W$ taken from $E(O)$ (or from a joint ensemble of $O$ and $O'$) selects an extra topology. That is $E$-smuggling, not a lock-side clock.
   - *(2b) $W=P(O)$.* The patch is locked data, not an extra topology. If $O'$ occurs at some $q\in P(O)$ with $q\notin\sigma_O$, and if $(O,O')$ is edged, that germ is type (ii). The infimum of proper times of causal curves $p\to q$ in $P(O)$ is then lock-side. It is not a unique function of the lumps $(O,O')$: $O'$ may occur at more than one $q$, and a causal curve $p\to q$ is a further choice unless the infimum over curves to a *fixed* $q$ is taken, which still leaves the choice of $q$. Most type-(ii) pairs have no occurrence of $O'$ in $P(O)$, so this is not a general type-(ii) clock.

**Proof of (1).** Hitchhiker $\tau$ is the proper-time parameter of $\sigma_O\subset P(O)$. Every point of that geodesic determines a lump on $\gamma_O$. Type (ii) puts $O'$ off $\gamma_O$, so no $\tau$ along $\sigma_O$ is the event of $O'$. $P(O')$ has its own hitchhiker clock along $\gamma_{O'}$; the two curvelets need not meet, and there is no locked identification of their parameters. $\square$

**Proof of (2a).** Members of $E(O)$ are pointed occurrences of the *same* lump $O$ in possibly other $W$. Using such a $W$ (or a $W$ chosen to realize both $O$ and $O'$) to timestamp a type-(ii) pair in $\mathrm{Obs}$ folds ensemble labels into a number attached to lumps. Distinct extra $W$ can give distinct lengths ($\pi_W$ is many-to-one). $\square$

**Proof of (2b).** $P(O)$ is the unique simply-connected analytic continuation of the germ (Theorem B). It is not an ensemble extra. A point $q\in P(O)\setminus\sigma_O$ determines a lump $O_q$ off $\gamma_O$. An edge $(O,O_q)$ is type (ii) if it lies in $R$. Causal curves from $p$ to $q$ in $P(O)$, when they exist, have proper times; their infimum is read off the locked metric on $P(O)$. If $O'$ occurs at $q_1$ and $q_2$, those infima need not agree, so the construction does not yield a unique $\Delta\tau(O,O')$. If $O'$ does not occur in $P(O)$, the construction is undefined for that pair. The set of lumps that occur in $P(O)$ is the hitchhiking-plus-spatial content of one patch, not all of $\mathrm{Obs}$. $\square$

**Corollary 23.1.** Proper-time-in-some-extra-$W$ is $E$-smuggling (2a). In-patch infimal proper time $p\to q$ for $q\in P(O)\setminus\sigma_O$ is lock-side and is *not* type-(i) hitchhiking (the curve need not be $\sigma_O$). It is not a unique function of $(O,O')$ and is not a clock for type-(ii) pairs that do not occur in $P(O)$.

**Not claimed.** There is no real function of $(O,O')$. The constant $0$ is a function. Walk-length along $R$ is a function of a law of $R$, which is extra (Theorem 19). Locally finite one-step out-neighborhoods are finite slices from that law (Theorem 22).

Fermi-slice neighborhoods are uncountable (Theorem 17) and carry no locked time function. Continuous $f:\mathrm{Obs}\to\mathbb{R}$ do not grain (Theorem 18) and are not proper time.

---

## 2. Named leftover, not adopted

| Candidate | What it would be | Lock-side? | Adopted? |
|---|---|---|---|
| Hitchhiker $\tau$ along $\gamma_O$ | Proper time of $\sigma_O$ | Yes, type (i) only | already the in-world stand-in |
| Extra $W$ from $E(O)$ | Length of a causal curve in a chosen ensemble $W$ | No: $E$-smuggling (2a) | no |
| In-patch infimal proper time $p\to q$ | Inf of proper times of causal curves in $P(O)$ to a $q$ off $\sigma_O$ | Yes, when $O'$ occurs in $P(O)$; not unique in $(O,O')$; not general | no |
| Generation $g:V\to\mathbb{N}$ | Rank on a DAG so $R$ advances $g$ | Extra: needs $R$, typically locally finite | no |
| Lyapunov on $\mathrm{Obs}$ | A function that increases along $R$ | Extra: a function not locked; continuous ones do not grain | no |
| Walk-length | Number of type-(ii) edges in a walk | Extra: combinatorial, needs $R$; infinite on cycles (Theorem 20) | no |

Grain to make $V$ finite so generations are finite slices: killed as a lock-side constraint. $|a|^2$ as a clock or as edge weights: killed.

---

## 3. Report line

- **Proved.** Theorem 23(1): hitchhiker $\tau$ does not timestamp type (ii). (2a): extra $W$ from $E(O)$ is $E$-smuggling. (2b): in-patch infimal proper time is lock-side, not unique in $(O,O')$, not a general type-(ii) clock.
- **Not claimed.** No real function of $(O,O')$.
- **Named, not adopted.** Generation, Lyapunov, walk-length. In-patch infimal proper time not adopted as a general clock.
- **Killed.** $E$-smuggling as a lock-side clock. Grain or Born as a lock-side slice. Corollary 23.1’s previous overclaim (every proper-time-in-$W$ is type (i) or $E$-smuggling).
- **Open.** Whether to put in a slice at all; the law of $R$.

---

## References

Strayhorn, D. Path-counting needs a slice. `papers/counting-needs-a-slice.md`.

Strayhorn, D. Fusion and path-counting. `papers/fusion-and-path-counting.md`.

Strayhorn, D. The ensemble $E(O)$ as a labeled object. `papers/ensemble-labels.md`.

Strayhorn, D. Geodesic lifts are analytic curves in observer space. `papers/geodesic-lifts.md`.

Strayhorn, D. Theorem: the simply-connected analytic patch from an infinite jet. `papers/analytic-patch-from-jet.md`.
