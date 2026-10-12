# Geometry quick verdict: creative batch 13 (#369) — do not merge

**Read at:** #369 head `c4049ff` (`notes/creative/batch-13.md`), main `e41412b`.

**Record type.** Rough review. It applies nothing and stays neutral on David's open calls. Scope is exploration under the rulings of 3:14, 3:53, 4:16, 4:17 and 4:28 PM ET, and structure only. All arguments are sketches. **(V #n)** means verified in PR #n; **(U)** means from memory and not checked.

**Verdicts.**
- **(A)** Facts 1–3 and the recommendation to keep "record branch" and "state branch" separate stand. Two claims need correcting. "Off-path geometry is never fixed at finite τ" is wrong under the analytic lock and right only in the smooth case. "Reaches a single branch in finite time only for $n\le3$ crystals" is too narrow: it holds for any cocompact Γ in a known cover with exact-vector records.
- **(B)** "Survival is determined within each world" stands. The Misner case rests on Geometry's computation (#367), not on a verified source, so it should be relabelled. Eternal geons do not break ensemble comparison. $E_{\mathcal W}$ and $E_M$ are defined by germs, not by Cauchy surfaces, so the anchor is the germ, not the region $U$.
- Not flagged.

## (A) Outcome = branch

- **Fact 1 (nesting) is correct.** $[W]^S_\tau\subseteq[W]^R_\tau$ because the state contains the record. So #367 (d) is a state difference and no longer a crossing. Geometry's earlier one-line answer said the same.
- **Correction 1: off-path geometry.**
  - *Under the analytic lock.* The germ fixes the geometry of the cover everywhere, off-path included, by continuation (Theorems A–B). So that geometry is fixed already at $\tau=0$. It is only unfixed past points where maximal extension is non-unique (#352 (1)). What stays open at finite $\tau$ is the **quotient Γ** and the **choice of extension**. The batch's "hosts with different Γ, or different off-path geometry" should read "different Γ or a different extension" under the lock.
  - *In the smooth case* (relaxed lock), geometry outside $J^-(\gamma(\tau))$ is never fixed by germ and records together (#346, #361 (3)). The batch's sentence is right only here.
- **Correction 2: "only $n\le3$".** This is a sketch.
  - For $n\le3$, #359 used the fact that successive minima form a basis. A covering argument works more generally.
  - Take a cover with a known isometry group and exact displacement records (arrival positions $g\tilde p$, not only isotropy angles; #355). Let $\Gamma$ be cocompact with quotient diameter $D$. Suppose $\tau$ is at least the largest displacement among some generating set, and at least about $2D$.
    - Then $\langle R_\tau\rangle=\Gamma$.
    - Any discrete $\Gamma'\supsetneq\Gamma$ would contain an element with displacement $\lesssim 2D$, which would already appear in the record.
    - So the record fixes Γ at finite $\tau$.
    - The observer can also **certify** this. It can compute $\langle R_\tau\rangle$ and that group's quotient diameter from the record, so it knows when the bound is met.
  - This covers $\mathbb Z^n$ crystals for all $n$, and cocompact hyperbolic Γ, provided the record identifies each $g$ from $g\tilde p$. In a homogeneous cover the stabiliser of $\tilde p$ blurs that, which (U) needs care.
  - It fails for non-cocompact Γ (no finite $D$), and when records keep only isotropy angles.
- **Recommendation (keep record branch and state branch).** Agreed. The L29 rule makes "outcome = branch" a definition. That is acceptable as bookkeeping but is not evidence. Under LT2 it would be a cheat only if it were offered as a finding. The substantive question, whether a germ can diverge with no record difference, stays visible only if both notions are kept.

## (B) Survival beyond Misner

- **Misner.** #367 is Geometry's explicit computation in null coordinates, not a verified source. "(#367, verified)" should read "(#367, Geometry computation; Misner 1967 and Hawking–Ellis §5.8 (U))".
- **Taub–NUT.** The two inequivalent NUT extensions and their non-isometry are established (Chruściel–Isenberg 1993 (V #332)). The geodesic dichotomy, and the existence of **imprisoned incomplete geodesics** that end in both extensions, are as I recall them from Misner–Taub 1969 and Misner 1967 ("Taub–NUT space as a counterexample to almost anything") (U). The batch's reading is consistent with this.
- **Compactly generated Cauchy horizons** (Hawking 1992, *Phys. Rev. D* 46, 603 (U); Kay–Radzikowski–Wald 1997, *Commun. Math. Phys.* 183, 533 (U)).
  - In a fixed extended spacetime, completeness is a property of the geodesic. So survival is a function of the pair (extension, observer data).
  - Extensions beyond such horizons may be non-unique, or may not exist analytically at all. In the second case some worlds simply have no continuation. That is dropout, not an arm (v0.10.1 §6.2).
  - The verdict stands: survival is determined within a world and varies between worlds.
- **Eternal geons without a Cauchy surface.**
  - Such hosts are not globally hyperbolic, so $D^+(S)$, "the shared past" and "beyond the horizon" are undefined there.
  - But ensemble comparison never needed them. $E_{\mathcal W}(O)$ and $E_M(O)$ are defined by occurrences of the germ (v0.10.1 §4; geodesic-lifts §2). Augmented with the record, the rule is "hosts sharing $\hat O$ up to $\tau$" (L29). That is well-posed with no Cauchy surface.
  - What does need $D(S)$ is the *timing* analysis: #346's first-divergence locus, and #364 (d)'s "no reply inside $D^+(S)$". In eternal-geon hosts those results do not apply, so replies are not barred before any horizon.
  - The anchor is therefore the **germ/curvelet** (plus record), which is host-independent. It should not be the region $U$, which belongs to one host and cannot be compared across hosts.

**Citations (U):** Misner 1967; Misner–Taub 1969; Hawking–Ellis §5.8; Hawking 1992; Kay–Radzikowski–Wald 1997; the stabiliser caveat for homogeneous covers. **(V #332):** Chruściel–Isenberg 1993. **In-repo:** #346, #352, #355, #359, #361, #364, #367.
