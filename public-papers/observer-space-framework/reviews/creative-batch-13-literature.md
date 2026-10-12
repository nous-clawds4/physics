# Literature pass: creative batch 13 (L41–L42), PR #369

Reviewer: Literature agent. PR head recorded: `c4049ff` (base `creative/batch-12`). Files: `notes/creative/batch-13.md`, `notes/creative/charter.md`, `notes/creative/ledger.md`. Do not merge. Marks: **V-text** = wording read (primary or a quoted secondary, named); **V-meta** = bibliographic data verified, content from the standard account.

## 1. Taub–NUT extensions and imprisoned geodesics (L42)

**Sources.**
- Misner, "Taub-NUT space as a counterexample to almost anything" (1967): V-meta.
- Misner & Taub, Sov. Phys. JETP 28 (1969) 122: V-meta.
- Hawking & Ellis (1973) §5.8: V-meta; full text not reachable.
- Secondary accounts read:
  - Clément, Gal'tsov & Guenouche, "Rehabilitating space-times with NUTs", arXiv:1508.07622 (V-text): "with this periodicity condition the analytically extended Taub–NUT spacetime is either geodesically incomplete (extension can be carried out through only one of the two horizons), or can be maximally extended to a geodesically complete but non-Hausdorff spacetime".
  - gr-qc/9612005, on Misner's 2D model (V-text): the spiralling null geodesics "follow infinite spirals as they approach t = 0 … The affine parameter is bounded … so they are in fact incomplete".
  - Kagramanova–Kunz–Hackmann–Lämmerzahl, PRD 81 (2010) 124044: V-meta.

**Findings.**
- **The dichotomy by a conserved quantity is correct (V-meta).** Geodesics cross into a given extension according to the sign of the momentum conjugate to the Killing field along the closed generators (the Hopf fibre in Taub–NUT; the boost direction in Misner). That matches #367's computed Misner result.
- **Imprisonment is relative to an extension: wrong as stated (S1–S4).** "Totally imprisoned incompleteness" (Misner; H–E) describes geodesics that spiral toward the horizon *within one chosen extension*. Those are the geodesics with the other sign, and they cross in the other extension. Whether a union of extensions is complete depends on the spacetime (split below, per #375).
  - So the imprisoned observers are not "survive in no extension". They are the ones that end in this extension and survive in the other, which is exactly the Misner dichotomy.
  - **Split by spacetime (corrected per #375):**
    - **Misner:** the geodesics through the boost's fixed point (#367) are incomplete in both extensions and in every union. The union of the two extensions is **not** complete: generic geodesics entering a CTC region hit its second horizon. Only the full quotient $(\mathbb R^2\setminus\{0\})/B$ is complete, apart from the fixed-point geodesics (a measure-zero set).
    - **Taub–NUT:** the maximal non-Hausdorff extension is geodesically complete (Hajicek, J. Math. Phys. 12 (1971) 157, V-meta; Clément et al., arXiv:1508.07622, V-text). It has no boost fixed point.
- **Hawking, "Chronology protection conjecture", PRD 46 (1992) 603–611 (V-meta).** It defines compactly generated Cauchy horizons, whose generators, followed into the past, enter and remain in a compact set. The batch's "closed or past-imprisoned null generators" is correct.
  - Non-uniqueness of extensions beyond them is not Hawking's result. It is the general Cauchy-horizon fact (Chruściel–Isenberg, per #368). Note only.

## 2. Hadley geon hosts and Cauchy surfaces

- **No Cauchy surface: definite, not "may be".** A spacetime with a Cauchy surface is globally hyperbolic, hence strongly causal. So any host containing CTCs, eternal or forming, has **no** Cauchy surface (Hawking–Ellis §6.6, V-meta; standard).
- Further, no achronal set can contain a point on a CTC (since $p\ll p$). So no partial Cauchy surface passes through the chronology-violating region.
- For a *forming* geon, a partial Cauchy surface $S$ in the earlier causal era still gives $D^+(S)$ and a Cauchy horizon, so the batch's analysis applies.
- For an *eternal* geon, $D^+(S)$-based comparison is unavailable globally. The batch's suggested anchor (the observer's chronological region $U$) is the right kind of repair.
- Non-time-orientability (Hadley 2000, V-text per #362) is a separate obstruction: global hyperbolicity is defined for time-oriented spacetimes.
- **David's 4:16 PM words** (allowing CTCs in geon hosts, exploration only) are now recorded in the ledger and charter, labelled relayed and not signed. The batch cites them correctly as an exploration condition.

S5 fixes the "may be".

## 3. Prior art on record-defined branches (cited only as prior art, not as framing)

- Gell-Mann & Hartle, "Quantum mechanics in the light of quantum cosmology" (1990, in *Complexity, Entropy and the Physics of Information*) and PRD 47 (1993) 3345 (V-meta): histories coarse-grained by records; decoherent histories identified through records.
- Zurek, "Quantum Darwinism", Nature Physics 5 (2009) 181 (V-meta): outcomes as redundantly recorded information.
- Wallace, *The Emergent Multiverse* (OUP 2012) (V-meta): branches as emergent, coarse-grained, record-bearing structures.
- **Branching space-times.** Belnap, Synthese 92 (1992) 385 (V-meta): the outcomes of a choice point $e$ are equivalence classes of histories under "undivided at $e$". That is the closest prior art to L41's "an outcome at $\tau$ is an equivalence class of branches". Placek & Müller (Erkenntnis 2014, per #368) and Belnap's later work on outcomes develop the coarse-graining.
- So L41 fact 2 is known in structure (BST outcomes; decoherent-history coarse-graining). Facts 1 and 3 (nesting, monotone refinement) are standard for records in both literatures.

## 4. The circularity warning

**Sound.**
- Defining "branch at $\tau$" as the record class makes outcome = branch true by definition. It cannot then be evidence for the hypothesis.
- The batch correctly notes the rule predates the question (batch 08, from David's 3:53 PM working assumption), so it was not tuned. It is a convention, not a cheat, *unless* offered as evidence.
- Keeping "record branch" and "state branch" separate preserves the substantive question (branch without outcome). The recommendation is correct.
- The same worry is raised in the decoherent-histories literature: records defined by the coarse-graining you then test (V-meta, Gell-Mann–Hartle).
- One editorial leak needs removing (S6).

## 5. Strings (each OLD occurs once at c4049ff)

S1. `notes/creative/batch-13.md`
- OLD: `some geodesics are **imprisoned**: incomplete in **both** extensions and confined to a compact set. Those observers survive in no extension.`
- NEW: `within each extension, the geodesics of the other sign are **imprisoned**: they spiral toward the horizon in a compact set and are incomplete there, but they cross in the other extension. In Misner the two-extension union is still incomplete. Only the full four-piece quotient is complete, apart from the geodesics through the boost's fixed point, which are incomplete in every union.`

S2. `notes/creative/batch-13.md`
- OLD: `A few observers in Taub–NUT are trapped and survive in no continuation.`
- NEW: `Observers that look trapped in one Taub–NUT continuation get through in the other; only a negligible special set gets through neither (incomplete in every union).`

S3. `notes/creative/batch-13.md`
- OLD: `Some Taub–NUT observers survive in none.`
- NEW: `In Taub–NUT, as in Misner, imprisonment is relative to the extension; only a measure-zero set survives in none (incomplete in every union).`

S4. `notes/creative/ledger.md`
- OLD: `plus imprisoned geodesics incomplete in both extensions (unchecked)`
- NEW: `imprisoned geodesics are incomplete in one extension and cross in the other; the Taub–NUT maximal non-Hausdorff extension is complete (Hajicek 1971; arXiv:1508.07622); in Misner, completeness holds only in the four-piece quotient and modulo the fixed-point geodesics`

S5. `notes/creative/batch-13.md`
- OLD: `there may be **no Cauchy surface** $S$ at all.`
- NEW: `there is **no Cauchy surface** $S$ (any spacetime with CTCs is not globally hyperbolic, and no achronal slice can pass through the chronology-violating region; non-time-orientability is a further obstruction).`

S6. `notes/creative/batch-13.md`
- OLD: `(LT2; the request says "T2")`
- NEW: `(LT2)`

## Provenance
- David's 4:28 PM words are identical in the batch, ledger and charter. They are labelled "relayed by Physics Lead, Physics Lead chat, not signed" (the ledger adds "verbatim"). Correct.
- I cannot check them against a primary record.
- No David geon ruling is claimed.

## Guardrails
- No forbidden symbol (none in this file).
- No Born/$|a|^2$/$1/N$ result.
- Everett-adjacent works are cited as prior art only, with no framing.
- No pick among M1/M2/T-options or on CTCs.
- Paper 1 untouched.

## Verdicts
- **L41 (outcome vs branch):** correct and known in structure (BST outcomes as history classes; decoherent-history records). The circularity warning is sound. Survives. S6 is editorial.
- **L42 (survival):** the sign dichotomy is correct. Union completeness must be split by spacetime (Misner vs Taub–NUT; see the correction note). "Imprisoned = survives nowhere" is wrong: imprisonment is extension-relative (S1–S4). The eternal-geon host definitely has no Cauchy surface (S5). Survives with these fixes. In Taub–NUT survival is determined within each world, with only a measure-zero exception.

## Correction note (after #375)

The joint note #375 (Geometry, co-signed by Literature; head 2f294a6) found that this review's "non-Hausdorff union complete" carried a Taub–NUT result over to Misner. Corrected above:
- §1 is split by spacetime;
- S1 and S4 now use #375's wording;
- S2 and S3 add "incomplete in every union".

In Misner the fixed-point geodesics are incomplete in every union, the two-extension union is not complete, and only $(\mathbb R^2\setminus\{0\})/B$ is complete apart from them. In Taub–NUT the maximal non-Hausdorff extension is complete (Hajicek 1971, V-meta; Clément et al., V-text).
