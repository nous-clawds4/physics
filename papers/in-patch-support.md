# In-patch occurrence as a support constraint

David Strayhorn

The lumps that occur in $P(O)$ are locked data. Restricting the support of type-(ii) $R$ at $O$ to those lumps (off $\gamma_O$) does not choose an extra $W$. Name that constraint. Do not adopt it. It does not finite-support $R$. Do not write $\Phi$, $L$, or a law of which remaining pairs are edged. Do not put $1/N$ or $|a|^2$. Paper 1 not rewritten.

Companions: `papers/type-ii-clock.md`, `papers/least-action-support.md`, `papers/countable-in-patch.md` (Theorem 28).

**Status.** Theorem 27: $\mathrm{Occ}(O)$, the set of lumps realized at points of $P(O)$, is lock-side. The candidate support constraint “type-(ii) targets of $O$ lie in $\mathrm{Occ}(O)\setminus\gamma_O$” does not use $E(O)$. If curvature (or a jet coefficient) is nonconstant on $P(O)$, the analytic image is a continuum of lumps; if the patch is locally homogeneous, $\mathrm{Occ}$ may collapse and $S$ may be empty (Minkowski). Neither is a nonempty finite typicality set of delayed forks. Named, not adopted.

---

## 1. The lock-side set

$P(O)$ is the unique simply-connected analytic continuation of the germ (Theorem B). For $q\in P(O)$ write $O_q$ for the lump at $q$: the infinite jet of the metric at $q$, plus a future unit timelike. The lock-side choice of that $u$ is Fermi-transport of $u$ from $\sigma_O$ (in a convex neighbourhood: $u=\partial/\partial x^0$ in Fermi coordinates, as in Theorem 28(1)). The alternative is to take all future units at $q$; $\sim_L$ may still collapse Minkowski to one lump.

Write
$$
\mathrm{Occ}(O)\;=\;\{O_q:\ q\in P(O)\},\qquad
S(O)\;=\;\mathrm{Occ}(O)\setminus\gamma_O.
$$
These sets are functions of the locked patch, not of an extra $W$ from $E(O)$. $E_\gamma$ members share $\gamma_O$ (Theorem 4) and do not enlarge $\mathrm{Occ}(O)$ as a set of lumps.

The map $q\mapsto O_q$ can collapse. Along $\sigma_O$, the lumps are type (i). Off $\sigma_O$, $O_q$ is type (ii) *if it is a different lump and the pair is edged in $R$*. On a homogeneous patch it need not be a different lump. Whether an edge lies in $R$ is still a law of $R$ (Theorem 19).

---

## 2. Theorem 27. In-patch support is lock-side; counting is of lumps

**Theorem 27.** Let $S(O)=\mathrm{Occ}(O)\setminus\gamma_O$. Then:

1. $S(O)$ is determined by $P(O)$ (lock-side). Restricting type-(ii) targets of $O$ to $S(O)$ does not select an extra $W$ and is not $E$-smuggling.
2. Count *lumps*, not points of $P(O)$. If curvature (or some jet coefficient) is nonconstant on $P(O)$, the analytic image of $q\mapsto O_q$ is a continuum of lumps, so $S(O)$ does not grain. If the patch is locally homogeneous, $\mathrm{Occ}(O)$ may collapse and $S(O)$ may be empty. In neither case is $S(O)$ a nonempty finite typicality set of delayed forks. “Typically a continuum” means: for a generic real-analytic Lorentzian germ, local isometries are discrete, and $q\mapsto O_q$ is locally injective off $\sigma_O$.
3. Lorentzian distance $\tau(p,q)$ (Theorem 23(2b), supremum) can timestamp an edged pair $(O,O_q)$ when $q\in I^+(p)$, uniquely given that $q$. Several occurrences of the same lump still give several values.

**Proof.** (1) Immediate from Theorem B and the definition of $O_q$. Members of $E(O)$ are occurrences of the *same* lump $O$ in other $W$; they are not extra points of $S(O)$.

(2) Let $\varphi:P(O)\to\mathrm{Obs}$ send $q$ to $O_q$, with $u$ Fermi-transported from $\sigma_O$. $\mathrm{Occ}(O)=\varphi(P(O))$. This is a map into observer space, not a count of manifold points. $P(O)$ is an open $4$-manifold and the complement of a curve is uncountable *as points*; that does not imply uncountably many lumps. Theorem 17 varies germs in a Fermi-slice ball in $\mathrm{Obs}$, not basepoints in a *fixed* patch, and is not used to count $\mathrm{Occ}(O)$.

$\varphi$ is real-analytic as a map into jet space. If some curvature scalar (or some Fermi jet coefficient) is nonconstant on the connected patch $P(O)$, then $\varphi$ is nonconstant, so its image has cardinality of the continuum. For a generic germ, local isometries are discrete and $\varphi$ is locally injective off $\sigma_O$, hence $S(O)$ is a continuum.

If the patch is locally homogeneous (Minkowski), $\varphi$ is constant, $\mathrm{Occ}(O)$ is a singleton, and $S(O)=\emptyset$. Empty and singleton are not a nonempty finite typicality set of delayed forks. A continuum does not grain.

(3) Theorem 23(2b) as restated. $\square$

**Not claimed.** $R$ must be supported on $S(O)$. That is a constraint one could adopt; it is extra as a *choice to restrict*, even though the *set* $S(O)$ is lock-side. Most type-(ii) pairs in an unrestricted $R$ need not meet $S(O)$. $S(O)$ is always uncountable (false for Minkowski). Theorem 17 supplies the continuum *inside this patch*.

**Killed.** Using $E(O)$ to enlarge the in-patch support (that is $E$-smuggling). Treating $S(O)$ as a finite $N$. $|a|^2$ as a selector inside $S(O)$. Counting points of $P(O)\setminus\sigma_O$ as if they were lumps.

---

## 3. Named leftover, not adopted

In-patch support: $R$ type-(ii) at $O$ lands in $S(O)$. Lock-side *set*, extra *as a restriction of $R$*. Does not replace a grain, a slice, or a law of which pairs in $S(O)$ are edged. Named subsets of $S(O)$ do not count without a grain (Theorem 28).

---

## 4. Report line

- **Proved.** Theorem 27: $\mathrm{Occ}(O)\setminus\gamma_O$ is lock-side. Nonconstant curvature (or jet coefficient) $\Rightarrow$ continuum of lumps; local homogeneity $\Rightarrow$ $\mathrm{Occ}$ may collapse and $S$ may be empty. Restricting type-(ii) targets to $S(O)$ is not $E$-smuggling and does not grain.
- **Named, not adopted.** In-patch support as a constraint on $R$.
- **Killed.** $E$-smuggling as an enlargement of in-patch support. $S(O)$ as a finite typicality set. Points-of-the-patch as lumps.
- **Open.** Whether to adopt the restriction; the law of which pairs in $S(O)$ are edged.

---

## References

Strayhorn, D. Type-(ii) does not inherit hitchhiker $\tau$. `papers/type-ii-clock.md`.

Strayhorn, D. Lock-side subsets of in-patch occurrence are not a countable $N$. `papers/countable-in-patch.md`.

Strayhorn, D. Neighborhoods are not a countable $N$. `papers/neighborhood-uncountable.md`.

Strayhorn, D. Theorem: the simply-connected analytic patch from an infinite jet. `papers/analytic-patch-from-jet.md`.
