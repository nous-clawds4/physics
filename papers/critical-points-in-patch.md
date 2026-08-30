# Critical points and the conjugate locus do not lock a countable $N$

David Strayhorn

Theorem 28 killed named *subsets* of $S(O)$ (spatial slice, Cauchy surface, integer bins). Leftover discrete-looking loci in $P(O)$: Morse critical points of a curvature scalar, the conjugate locus of $p$, the cut locus of $p$. Prove or kill as a lock-side countable typicality set of delayed forks. Do not adopt. No $\Phi$, no $|a|^2$, no $L$. Paper 1 not rewritten.

Companions: `papers/countable-in-patch.md`, `papers/in-patch-support.md` (PR #35).

**Status.** Theorem 29: Morse of a curvature scalar is extra (a mesh-like condition). Degenerate critical sets are continua. The conjugate locus and the cut locus of $p$ in $P(O)$ are typically caustics (continua of points; typically continua of lumps after $q\mapsto O_q$). Isolated conjugates along $\sigma_O$ are type (i). Not a closed “no countable subset.”

---

## 1. Theorem 29. Named loci in $P(O)$ do not count

Let $\varphi:P(O)\to\mathrm{Obs}$ send $q$ to $O_q$ with $u$ Fermi-transported from $\sigma_O$ (Theorem 27). $S(O)=\varphi(P(O))\setminus\gamma_O$.

**Theorem 29.** None of the following supplies a nonempty countable typicality set of delayed forks as a lock-side subset of $S(O)$, without a grain:

1. *Critical points of a curvature scalar.* Let $f$ be Ricci scalar, Kretschmann, or any finite list of continuous curvature scalars pulled back to $P(O)$. The set $\mathrm{Crit}(f)=\{q:\ df_q=0\}$, or $\varphi(\mathrm{Crit}(f))\setminus\gamma_O$.
2. *Conjugate locus of $p$.* Points of $P(O)$ conjugate to $p$ along a geodesic from $p$, and their lumps off $\gamma_O$.
3. *Cut locus of $p$.* Points at which the geodesic from $p$ ceases to minimize Lorentzian distance (Theorem 23(2b)), and their lumps off $\gamma_O$.

**Proof.** (1) If $f$ is constant on $P(O)$, $\mathrm{Crit}(f)$ is empty or the whole patch: local homogeneity, $S$ may be empty (Theorem 27(2)). If the zero set of $df$ has a positive-dimensional component, that component is a continuum of *points*; after $\varphi$, one class or a continuum of lumps (Theorem 28). Isolated critical points require a Morse (or Morse–Bott with $0$-dimensional critical manifolds) condition on $f$. That condition is extra, the same kind of choice as a mesh $\delta$ (Theorem 18). On noncompact $P(O)$, even a Morse $f$ may have infinitely many critical points; countability then still rides on Morse, not on the jet/patch.

(2) In a convex neighbourhood of $p$ there are no conjugates of $p$. If $P(O)$ is only that neighbourhood, the conjugate locus is empty. Globally, the conjugate locus is the caustic of $\exp_p$: typically of dimension $2$ or $3$, a continuum of points. After $\varphi$, one class or a continuum of lumps, unless a further cut. Isolated conjugate times along $\sigma_O$ are type (i), not delayed forks.

(3) The cut locus of $p$ is closed, and in a convex neighbourhood is empty. Where it exists it is typically a spine or hypersurface (continuum of points). “First cut point in each spatial direction” is a $2$-parameter family, still a continuum. $\square$

**Not claimed.** No Morse function on $P(O)$ exists. A $\mathbb{Q}$-mesh of directions on the exponential $2$-sphere is countable and extra (Theorem 28). Empty conjugate locus in a convex neighbourhood is not a typicality set of delayed forks.

**Killed.** Morse critical points as a lock-side countable $N$. Conjugate locus or cut locus of $p$ as that $N$. $|a|^2$ as a selector on the caustic. $L$ unwritten.

---

## 2. Named leftover, not adopted

None of (1)–(3) is adopted. Grain, Morse, and a mesh of directions stay extra.

---

## 3. Report line

- **Proved.** Theorem 29: Morse of a curvature scalar is extra; degenerate critical sets, the conjugate locus, and the cut locus of $p$ are typically continua of lumps after $q\mapsto O_q$. Isolated conjugates along $\sigma_O$ are type (i).
- **Not claimed.** No countable subset of $S(O)$. $\mathbb{Q}$-meshes extra.
- **Named, not adopted.** Morse, conjugate locus, cut locus as cuts.
- **Killed.** Those three as lock-side countable $N$.
- **Open.** Grain, or any other discrete cut. The law of $R$.

---

## References

Strayhorn, D. Lock-side subsets of in-patch occurrence are not a countable $N$. `papers/countable-in-patch.md`.

Strayhorn, D. In-patch occurrence as a support constraint. `papers/in-patch-support.md` (PR #35).

Strayhorn, D. Type-(ii) does not inherit hitchhiker $\tau$. `papers/type-ii-clock.md`.

Hawking, S. W. and Ellis, G. F. R. *The Large Scale Structure of Space-Time.* Cambridge, 1973. (Conjugate points, cut locus.)
