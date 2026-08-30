# Type-(ii) does not inherit hitchhiker $\tau$

David Strayhorn

Can a type-(ii) edge inherit any locked clock without choosing a $W$ from $E(O)$? Hitchhiker $\tau$ is in-world only. Kill $E$-smuggling. Name leftover candidates. Do not adopt a slice, a tree, $1/N$, a grain, a measure, $\Phi$, or Born. Do not write a law of $R$. Do not restore the 2007 geodesic-generated tree. Paper 1 not rewritten.

Companions: `papers/counting-needs-a-slice.md` (PR #26), `papers/fusion-and-path-counting.md`, `papers/ensemble-labels.md`.

**Status.** Theorem 23: hitchhiker $\tau$ does not label type-(ii) targets. Proper-time-in-some-$W$ is $E$-smuggling, not a lock-side clock. Not a closed “no real function of $(O,O')$.” Leftover candidates (generation, Lyapunov, walk-length) are extra, not adopted.

---

## 0. The locked clock, and where it lives

Layer (i): geodesic hitchhiking. Proper time $\tau$ is the parameter of $\sigma_O$ in $P(O)$, equivalently of $\gamma_O$ in $\mathrm{Obs}$. It is defined *along that curvelet*. $E_\gamma$ members share $\gamma_O$ (Theorem 4), so they share that $\tau$. Lifetime $\tau_\partial$ is the same clock, possibly finite (Theorems 6–7).

A type-(ii) edge $(O,O')$ is, by definition, not a geodesic lift: $O'$ does not lie on $\gamma_O$. The hitchhiker parameter does not label $O'$. Theorem 22 (restated): named non-slices fail; not a closed “nothing supplies a slice.” This note asks whether any *other* locked time-parameter still attaches to the edge without picking a $W$.

---

## 1. Theorem 23. Hitchhiker $\tau$ does not timestamp type (ii)

**Theorem 23.** Let $(O,O')$ be type (ii).

1. Hitchhiker $\tau$ along $\gamma_O$ does not label $O'$.
2. A proper-time difference along a causal curve from an occurrence of $O$ to an occurrence of $O'$ is not a function of the two lumps: it requires a choice of $W$ and of occurrences. That is $E$-smuggling, not a lock-side clock.

**Proof.** (1) Hitchhiker $\tau$ is the proper-time parameter of $\sigma_O\subset P(O)$. Every point of that geodesic determines a lump on $\gamma_O$. Type (ii) puts $O'$ off $\gamma_O$, so no $\tau$ along $\sigma_O$ is the event of $O'$. $P(O')$ has its own hitchhiker clock along $\gamma_{O'}$; the two curvelets need not meet, and there is no locked identification of their parameters.

(2) A spacetime proper time from $O$ to $O'$ needs a real-analytic Lorentzian $W$ and a causal curve $\sigma$ from an occurrence of $O$ to an occurrence of $O'$. That is a choice of $W$ together with two pointed embeddings, i.e. ensemble data for two lumps, not the lumps. Distinct $W$ can give distinct lengths ($\pi_W$ is many-to-one; Theorem 3 supplies analyticity of each lift separately, not a common $\tau$). Members of $E(O)$ are occurrences of *the same* lump $O$; they do not timestamp a different lump $O'$. Using $E(O)$ (or $E_\gamma(O)$) as the clock folds occurrence-labels into a number attached to a type-(ii) pair in $\mathrm{Obs}$. $\square$

**Corollary 23.1.** “Proper-time-in-some-$W$” is not a lock-side candidate. It is either type (i) (the $W$ is $P(O)$, the curve is $\sigma_O$) or $E$-smuggling.

**Not claimed.** There is no real function of $(O,O')$. The constant $0$ is a function. Walk-length along $R$ is a function of a law of $R$, which is extra (Theorem 19). Locally finite one-step out-neighborhoods are finite slices from that law (Theorem 22, restated).

Fermi-slice neighborhoods are uncountable (Theorem 17) and carry no locked time function. Continuous $f:\mathrm{Obs}\to\mathbb{R}$ do not grain (Theorem 18) and are not proper time.

---

## 2. Named leftover, not adopted

| Candidate | What it would be | Lock-side? | Adopted? |
|---|---|---|---|
| Hitchhiker $\tau$ along $\gamma_O$ | Proper time of $\sigma_O$ | Yes, type (i) only | already the in-world stand-in |
| Proper-time-in-some-$W$ | Length of a causal curve in a chosen $W$ through both germs | No: $E$-smuggling (Theorem 23) | no |
| Generation $g:V\to\mathbb{N}$ | Rank on a DAG so $R$ advances $g$ | Extra: needs $R$, typically locally finite | no |
| Lyapunov on $\mathrm{Obs}$ | A function that increases along $R$ | Extra: a function not locked; continuous ones do not grain | no |
| Walk-length | Number of type-(ii) edges in a walk | Extra: combinatorial, needs $R$; infinite on cycles (Theorem 20) | no |

Grain to make $V$ finite so generations are finite slices: killed as a lock-side constraint. $|a|^2$ as a clock or as edge weights: killed.

---

## 3. Report line

- **Proved.** Theorem 23: hitchhiker $\tau$ does not timestamp type (ii). Proper-time-in-some-$W$ is $E$-smuggling.
- **Not claimed.** No real function of $(O,O')$.
- **Named, not adopted.** Generation, Lyapunov, walk-length.
- **Killed.** $E$-smuggling as a lock-side clock. Grain or Born as a lock-side slice.
- **Open.** Whether to put in a slice at all; the law of $R$.

---

## References

Strayhorn, D. Path-counting needs a slice. `papers/counting-needs-a-slice.md`.

Strayhorn, D. Fusion and path-counting. `papers/fusion-and-path-counting.md`.

Strayhorn, D. The ensemble $E(O)$ as a labeled object. `papers/ensemble-labels.md`.

Strayhorn, D. Geodesic lifts are analytic curves in observer space. `papers/geodesic-lifts.md`.
