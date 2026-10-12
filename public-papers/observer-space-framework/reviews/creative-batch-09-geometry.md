# Geometry quick verdict: creative batch 09 (#357), do not merge

**Read at:** #357 head `75111ac` (`notes/creative/batch-09.md`, `notes/creative/batch-09/shares.py`), main `e41412b`.

**Record type:** rough review. It applies nothing and stays neutral on David's open calls. Counting worlds is a labelled working conjecture (David, 3:47 PM ET), and (M1) is unchanged at L3. All arguments are sketches. **(U)** marks a claim from memory that was not checked.

## Reproduction (fresh clone)

- **Script.** `notes/creative/batch-09/shares.py` at `75111ac`, sha256 `0b5c4132b8cc` (first 12 hex).
- **Invocation.** `python3 notes/creative/batch-09/shares.py > out.txt`, run from the repo root. Python 3, standard library only. It took about 44 s.
- **Output.** Byte-identical to the committed `notes/creative/batch-09/results.txt`. The output sha256 is `f0a11b4e9722`.
- **Independent spot-checks.**
  - **Total subgroup counts.** The subgroups of index $\le N$ were recomputed from the closed forms: $a_n(\mathbb Z^2)=\sigma(n)$, and $a_n(\mathbb Z^3)=\sum_{d\mid n}d\,\sigma(d)$ (U as citations). This gives 339 / 1342 / 5314 for $\mathbb Z^2$ (N = 20/40/80) and 737 / 5644 / 18868 for $\mathbb Z^3$ (N = 10/20/30). All six match the script.
  - **One conditional count.** At N = 20, $\mathbb Z^2$, the record $\{\pm e_1\}$ is matched by $\Gamma\supseteq\langle e_1\rangle$ with $e_2\notin\Gamma$. That means index-$d$ subgroups of $\mathbb Z$ with $2\le d\le 20$, so 19 worlds, which matches `n_worlds=19`.
  - **The table entries** in the batch text match the output.

## Verdicts

1. **Model.** The simplifications are fair and declared, but they drop three things #355 identified: arrival curves, the expansion caveat, and the gauge. It counts pointed worlds, which is correct for records.
2. **"Full-rank record fixes Γ".** This holds for $n\le3$ once it is stated precisely, but the stated reason needs repair.
3. **L31.** Correct, with one condition added: the ratio must also converge, and do so independently of the cutoff.
4. **Non-abelian and hyperbolic lattices.** These are expected to stay degenerate at an index cutoff, because "contains $g$" costs a factor of about 1/index. Not flagged for a full note.

## (1) Model versus #355

- **First arrivals only, at time $|g|$.** #355's arrival *curves* are dropped. For a static observer at rest with the beacon switched on at $t=0$, the echo via $g$ recurs at times $|g|+t_e$. Later points on each curve add no new deck elements, so first arrivals lose no information about Γ in this model. Fair.
- **Beacon switch-on at $t=0$.** This satisfies #355's condition.
- **Fixed-frame exact vectors.** The record is lossless, and stronger than #355's isotropy-angle gauge. The square and cubic crystal's point group would identify some records. Those identifications are not quotiented, which the batch notes in (iii).
- **Pointed count ($E_{\mathcal W}$).** Correct. The quote from v0.10.1 §4 is used as written; v0.10.1 was not edited.
- **Static and flat.** No expansion, so (f) of batch 08 is not tested. The degeneracy found here does not depend on that choice.

## (2) Does a full-rank record fix Γ?

- **The trivial version.** A record holding *all* nonzero $g\in\Gamma$ as vectors from $p$ simply is Γ.
- **A record of lengths only** (return times, no directions) asks whether the length spectrum, i.e. the theta series, determines the lattice. In general it does not: isospectral non-isometric flat tori exist, from Milnor 1964 in dimension 16 and Conway–Sloane in dimension 4 (U). For $n\le3$ lengths determine the lattice up to isometry (Schiemann for $n=3$, (U)). But "up to isometry" is not "as a subgroup of the fixed crystal $\mathbb Z^n$ at a fixed point": crystal rotations relate distinct pointed Γ with the same spectrum. So a lengths-only record does not fix pointed Γ, even for $n\le3$.
- **Finite-time full rank, with directions** (the batch's model). $n$ independent vectors in $R_\tau$ generate a sublattice $L_0$ that may be proper in Γ, so they do not fix Γ by themselves. The claim holds when $R_\tau$ contains vectors realising the **successive minima** of Γ. For $n\le3$ those vectors form a basis of Γ, whereas for $n\ge4$ they can fail to (e.g. $D_4$-type lattices) (standard, U). Precise statement: *for $n\le3$, once $\tau\ge\lambda_n(\Gamma)$ the exact-vector record determines Γ.* The batch's covering-radius argument reaches the same end, and its 2D example is consistent with this.
- **Side note from the output.** Certain (share-1) predictions also occur *before* full rank. In $\mathbb Z^3$ the rank-2 record $\{\pm e_1,\pm e_2\}$ gives "+4 new: 1.000" with 9/19/29 matching worlds. Closure under addition forces $\pm e_1\pm e_2$ into the record. So "certain" does not imply "one world".

## (3) L31: when is a share nontrivial?

$\text{share}=\lim_N a_N(\text{match})/a_N(\text{total})$. It is nonzero only if the two counts grow at the same order. L31 is right as stated. Two further conditions are needed:
- the ratio of leading terms must actually converge, rather than oscillate (for $\mathbb Z^n$ the divisor sums are irregular termwise but regular cumulatively, (U));
- the limit must be the same under every admissible cutoff family (#355 (d); the batch's S1 table).

Agreement at finite cutoffs is not required, and the batch's finite-cutoff spread (0.69 to 0.85) shows it does not hold.

## (4) Non-abelian and hyperbolic lattices

- **Growth.** Subgroup growth is superexponential: about $(n!)^{r-1}$ for free groups of rank $r$, and of factorial type for surface groups and many hyperbolic 3-manifold groups (Lubotzky–Segal 2003, U).
- **Index-$n$ subgroups correspond to transitive actions on $n$ points.** A *pointed* subgroup ($E_{\mathcal W}$) contains $g$ exactly when the basepoint coset is fixed by $g$. For a uniformly random action of a free group and a fixed nontrivial word $w$, the expected number of fixed points of $w(\sigma)$ tends to a constant: 1 if $w$ is not a proper power, and the number of divisors of the power otherwise (Nica 1994, U). So the probability that the basepoint is fixed is about constant$/n\to0$.
- **Surface groups.** Magee–Puder give the analogue (U).
- **Conclusion (sketch).** At an index cutoff the share of worlds containing any fixed element still tends to 0, for abelian, free and (expectedly) surface or hyperbolic lattices alike. Containing a fixed element is a codimension-like condition costing about 1/index. This is not an artefact of $\mathbb Z^n$. No lattice class tried or surveyed here gives a nontrivial share under the index cutoff. A nontrivial share would need a cutoff that does not rank worlds by index or volume, which brings back the listing-independence burden, or records that stay ambiguous.

**Citations (U):** the closed forms for $a_n(\mathbb Z^2)$ and $a_n(\mathbb Z^3)$ (confirmed numerically against the script, not checked against a source); Milnor 1964; Conway–Sloane; Schiemann; successive minima form a basis for $n\le3$; Lubotzky–Segal 2003; Nica 1994; Magee–Puder. In-repo: #352, #355, #356.
