# In-patch occurrence as a support constraint

David Strayhorn

The lumps that occur in $P(O)$ are locked data. Restricting the support of type-(ii) $R$ at $O$ to those lumps (off $\gamma_O$) does not choose an extra $W$. Name that constraint. Do not adopt it. It does not finite-support $R$. Do not write $\Phi$, $L$, or a law of which remaining pairs are edged. Do not put $1/N$ or $|a|^2$. Paper 1 not rewritten.

Companions: `papers/type-ii-clock.md`, `papers/least-action-support.md`.

**Status.** Theorem 27: $\mathrm{Occ}(O)$, the set of lumps realized at points of $P(O)$, is lock-side. The candidate support constraint “type-(ii) targets of $O$ lie in $\mathrm{Occ}(O)\setminus\gamma_O$” does not use $E(O)$. $\mathrm{Occ}(O)\setminus\gamma_O$ is typically a continuum, so the constraint does not grain. Named, not adopted.

---

## 1. The lock-side set

$P(O)$ is the unique simply-connected analytic continuation of the germ (Theorem B). Every $q\in P(O)$ determines a lump $O_q$ (the germ of the metric at $q$, plus a future unit timelike if one is chosen; along $\sigma_O$ one takes $\dot\sigma_O$). Write
$$
\mathrm{Occ}(O)\;=\;\{O_q:\ q\in P(O)\}.
$$
This set is a function of the locked patch, not of an extra $W$ from $E(O)$. $E_\gamma$ members share $\gamma_O$ (Theorem 4) and do not enlarge $\mathrm{Occ}(O)$ as a set of lumps.

Along $\sigma_O$, the lumps are type (i). Off $\sigma_O$, $O_q$ is a different lump. An edge $(O,O_q)$ is type (ii) *if it lies in $R$*. Whether it lies in $R$ is still a law of $R$ (Theorem 19).

---

## 2. Theorem 27. In-patch support is lock-side and uncountable

**Theorem 27.** Let
$$
S(O)\;=\;\mathrm{Occ}(O)\setminus\gamma_O.
$$
Then:

1. $S(O)$ is determined by $P(O)$ (lock-side). Restricting type-(ii) targets of $O$ to $S(O)$ does not select an extra $W$ and is not $E$-smuggling.
2. $S(O)$ is typically uncountable. In particular it is not a nonempty finite typicality set of delayed forks. The restriction does not grain.
3. Lorentzian distance $\tau(p,q)$ (Theorem 23(2b), supremum) can timestamp an edged pair $(O,O_q)$ when $q\in I^+(p)$, uniquely given that $q$. Several occurrences of the same lump still give several values.

**Proof.** (1) Immediate from Theorem B and the definition of $O_q$. Members of $E(O)$ are occurrences of the *same* lump $O$ in other $W$; they are not extra points of $S(O)$. (2) $P(O)$ is an open $4$-manifold. The complement of a curve is uncountable; distinct points in a Fermi neighbourhood of $p$, off $\sigma_O$, give a continuum of germs (Theorem 17 in the Fermi-slice topology on those lumps). (3) Theorem 23(2b) as restated. $\square$

**Not claimed.** $R$ must be supported on $S(O)$. That is a constraint one could adopt; it is extra as a *choice to restrict*, even though the *set* $S(O)$ is lock-side. Most type-(ii) pairs in an unrestricted $R$ need not meet $S(O)$.

**Killed.** Using $E(O)$ to enlarge the in-patch support (that is $E$-smuggling). Treating $S(O)$ as a finite $N$. $|a|^2$ as a selector inside $S(O)$.

---

## 3. Named leftover, not adopted

In-patch support: $R$ type-(ii) at $O$ lands in $S(O)$. Lock-side *set*, extra *as a restriction of $R$*. Does not replace a grain, a slice, or a law of which pairs in $S(O)$ are edged.

---

## 4. Report line

- **Proved.** Theorem 27: $\mathrm{Occ}(O)\setminus\gamma_O$ is lock-side and typically a continuum. Restricting type-(ii) targets to it is not $E$-smuggling and does not grain.
- **Named, not adopted.** In-patch support as a constraint on $R$.
- **Killed.** $E$-smuggling as an enlargement of in-patch support. $S(O)$ as a finite typicality set.
- **Open.** Whether to adopt the restriction; the law of which pairs in $S(O)$ are edged.

---

## References

Strayhorn, D. Type-(ii) does not inherit hitchhiker $\tau$. `papers/type-ii-clock.md`.

Strayhorn, D. Neighborhoods are not a countable $N$. `papers/neighborhood-uncountable.md`.

Strayhorn, D. Theorem: the simply-connected analytic patch from an infinite jet. `papers/analytic-patch-from-jet.md`.
