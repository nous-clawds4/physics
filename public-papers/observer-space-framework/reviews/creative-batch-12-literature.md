# Literature pass: creative batch 12 (L38–L40), PR #366

Reviewer: Literature agent. PR head recorded: `dbcfc18` (base `creative/batch-11`). Files: `notes/creative/batch-12.md`, `notes/creative/ledger.md`. Do not merge. Marks: **V-text** = wording read; **V-meta** = bibliographic data verified (Crossref or publisher), content from the standard account; **computed** = checked directly.

## 1. Misner / Taub–NUT and observers (L38)

**Sources.**
- Misner, "Taub-NUT space as a counterexample to almost anything" (1967, in *Relativity Theory and Astrophysics I*, Lectures in Applied Math. 8, AMS): V-meta.
- Hawking & Ellis (1973) §5.8: V-meta. Full text not reachable. The two-extension and one-family-completed account is the standard one.

**Timelike observers: computed in the Minkowski cover.**
- Misner space is the quotient of the future wedge $t>|x|$ by a boost.
- A timelike geodesic in the wedge that does not pass through the origin leaves the wedge through exactly one of the two null lines $t=x$, $t=-x$. Its image therefore crosses the horizon in exactly one of the two extensions and is incomplete in the other.
- Geodesics through the origin (the boost's fixed point, "comoving") hit the corner and are incomplete in both.
- So the batch's dichotomy applies to timelike observers as well as null geodesics. **Correct.**

**Imprecision (S1).** "The region $t^2-x^2>0$" has two components (future and past wedges). Misner space uses one.

**Isometry caveat (no string).**
- Chruściel–Isenberg's abstract (per #332, V-meta) notes that "many of the familiar extensions are isometric". Misner's two extensions are isometric, by the reflection $x\to-x$.
- They are "inequivalent" only *as extensions of the given region*, i.e. as **pointed** worlds relative to the observer.
- L38's split is real in $E_{\mathcal W}$, but it is not a split in $E_M$.
- For Taub–NUT, Chruściel–Isenberg also construct genuinely non-isometric extensions.

**Mark error (S2).** The batch cites Chruściel–Isenberg as "V-text per #332". #332 marked it V-meta (abstract only; the full text was unreachable).

## 2. EKT, Lossev–Novikov and countability (L40)

**Sources.**
- Echeverria–Klinkhammer–Thorne, PRD 44 (1991) 1077: V-text abstract, per #365.
- Lossev & Novikov, "The Jinn of the time machine: nontrivial self-consistent solutions", CQG 9 (1992) 2309–2321, doi:10.1088/0264-9381/9/10/014: V-meta.

**Discrete classes and isolated solutions.**
- Classification by number of traversals or collisions matches the standard account of EKT (V-meta). EKT's infinite multiplicity comes from solutions differing in their self-collision and traversal structure, and EKT note that "two of the infinity of solutions are slight perturbations" (V-text abstract).
- Isolation within a class is generic transversality. That is a sketch, and it is correctly marked as one.
- Lossev–Novikov's "jinn" are self-existent loop objects not fixed by the initial data. That is a second, separate source of multiplicity, which the batch does not mention. Note only.

**Symmetry: overclaim (S3).**
- A symmetry of the mouths maps a solution with initial data $d$ to a solution with *rotated* data $Rd$.
- For **fixed** data it yields a continuous family only if $d$ is itself invariant, e.g. on the symmetry axis, while the solution is not.
- Generic dangerous data break the symmetry. So "each isolated solution becomes a continuous family" is wrong as a default, and the claimed L27 tension is weaker than stated: it applies to symmetric data or to jinn-type content.

**Friedman–Morris.** Commun. Math. Phys. 186 (1997) 495–529, "Existence and Uniqueness Theorems for Massless Fields on a Class of Spacetimes with Closed Timelike Curves", doi:10.1007/s002200050118: V-meta. The batch's use is consistent with it.

## 3. Prior art: branching through extensions and non-Hausdorff branching

**Non-unique Cauchy-horizon extensions as branching.**
- Misner 1967 and Hawking–Ellis already note that the union of the two Misner extensions is non-Hausdorff.
- Chruściel–Isenberg give genuinely non-isometric extensions.
- #332 R2 found no branching of *motion* there. That is consistent with L38's "survives in some, ends in others".

**Non-Hausdorff branching:**
- Hajicek, Commun. Math. Phys. 21 (1971) 75, "Causality in non-Hausdorff space-times": non-Hausdorff spacetimes either fail strong causality or admit bifurcating geodesics (V-meta via Placek–Belnap's account).
- McCabe, "The topology of branching universes", Found. Phys. Lett. 18 (2005) 665 (V-text abstract): branching need not be non-Hausdorff.
- Earman, "Pruning some branches from branching spacetimes" (2008, in *The Ontology of Spacetime II*, Elsevier; doi:10.1016/S1871-1774(08)00010-7) (V-text excerpt): bifurcating geodesics raise the question of "how would such a particle know which branch … to follow?"
- Placek & Belnap / Müller ("Branching space-times, general relativity, the Hausdorff property, and modal consistency", PhilSci 8577; Erkenntnis 2014, doi:10.1007/s10670-013-9455-2) (V-text abstract): each BST history is Hausdorff, and only the multi-history model is not.
- Belnap, "Branching space-time", Synthese 92 (1992) 385 (V-meta).

**Bearing.**
- L38 avoids bifurcating geodesics because the observer *ends* in one extension rather than bifurcating. That is the Hajicek/Earman escape.
- Its "worlds = separate Hausdorff extensions" reading is the BST ensemble picture, not individual branching. The batch's weak point 7 (flagged, not used) is accurate.
- Belnap's branching space-times is a logical, indeterminist framework; using it does not import Everett.

## 4. Strings (`notes/creative/batch-12.md`; each OLD occurs once at dbcfc18)

S1
- OLD: `quotient of the region $t^2-x^2>0$ of $\mathbb R^{1,1}$ by a boost`
- NEW: `quotient of the future wedge $t>|x|$ of $\mathbb R^{1,1}$ by a boost (the region $t^2-x^2>0$ has two components; Misner space uses one)`

S2
- OLD: `V-text per #332`
- NEW: `V-meta (abstract only) per #332; the abstract notes "many of the familiar extensions are isometric", so Misner's two extensions differ as pointed worlds ($E_{\mathcal W}$), not as manifolds ($E_M$)`

S3
- OLD: `so each isolated solution becomes a **continuous family**, unless the initial data break the symmetry.`
- NEW: `but this maps a solution for data $d$ to one for rotated data $Rd$; for fixed data a **continuous family** arises only if $d$ is itself symmetric (e.g. on the axis) while the solution is not. Generic dangerous data break the symmetry, so isolated solutions stay isolated.`

## 5. Flag for David (not resolved)

- The batch (Status) and the ledger record "David's 4:16 PM approval of relaxing #352 for geon hosts" (relayed by Physics Lead, not signed). **No verbatim words are recorded anywhere** in `notes/` (searched).
- Per this review's brief, the CTC choice (#352's no-CTC condition vs L33) stays open for David.
- So the record and the brief conflict. Either the 4:16 PM words should be added verbatim and labelled relayed, or the status should say "pending David". This review takes no side.

## Guardrails
- No forbidden symbol (none in this file).
- No Born/$|a|^2$/$1/N$ result.
- No interpretation-camp framing; BST is cited as logic, not Everett.
- No pick among M1/M2/T-options or on CTCs.
- Paper 1 untouched.
- No David geon ruling is claimed.

## Verdicts
- **L38 (survival):** correct, and it applies to timelike observers (computed). The split is pointed-world only for Misner (isometric extensions). Known (Misner, H–E, Chruściel–Isenberg). Survives. S1 and S2 apply.
- **L39 (outcome vs branch):** an internal sketch; no literature conflict. Survives.
- **L40 (EKT countability):** "generically countable" is plausible and matches the standard account. The symmetry-continuum claim is overstated (S3). Jinn-type multiplicity (Lossev–Novikov) is not covered.
- **Prior art:** branching through extensions and non-Hausdorff branching are well studied (Hajicek, McCabe, Earman, Placek–Belnap, Belnap). L38's ending-rather-than-bifurcating avoids Hajicek's dichotomy.
