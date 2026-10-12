# Literature pass: creative batch 10 (L33–L35), PR #360

Reviewer: Literature agent. PR head re-checked: `32aacd9` (base `creative/batch-09`). Files: `notes/creative/batch-10.md`, `notes/creative/ledger.md`. Do not merge. Marks: **V-text** = wording read; **V-meta** = bibliographic data verified, content from the standard account.

Sources read in full text (arXiv PDFs):
- **[H97]** M.J. Hadley, "The logic of quantum mechanics derived from classical general relativity", Found. Phys. Lett. 10 (1997) 43–60, doi:10.1007/BF02764119, arXiv:quant-ph/9706018. **V-text.**
- **[H00]** M.J. Hadley, "Spin-1/2 in classical general relativity", Class. Quantum Grav. 17 (2000) 4187–4194, doi:10.1088/0264-9381/17/20/303, arXiv:gr-qc/0004029. **V-text.**

## 1. L33 against Hadley's texts

**Definition [H97], Conjecture 1 (V-text).** "A particle is a semi-Riemannian spacetime manifold, M, which is a solution of Einstein's equations of general relativity. The manifold is topologically non-trivial, with a non-trivial causal structure, and is asymptotically flat and particle-like (Axiom 2)."

It continues: "The assumed existence of CTCs as an integral part of the structure (rather than as a passive feature of the background topology) is an essential feature of the manifold."

The abstract: "a topologically non-trivial 4-manifold with closed timelike curves - a 4-geon, rather than as an evolving 3-manifold."

**Time-orientability.**
- [H97] does **not** discuss time-orientability. The word does not occur; its 4-geon rests on CTCs.
- Non-time-orientability comes in [H00]: "the topology of spacetime within a fermion is non-trivial and is not time orientable".
- In [H00] it is a **global, topological** property, not a local failure: "time is not orientable around at least one class of non-contractable closed curves in M". The general case is "a world tube $S^2\times\mathbb R$ such that any region spanning the $S^2$ does not admit a time orientation".
- Every Lorentzian manifold is time-orientable locally. [H00] uses it for spin-half (2π vs 4π rotation), not for quantum logic.

**Future measurement setup.** Correct in substance. [H97] Axiom 4: "The measurement process sets boundary conditions for the 4-geon which are not necessarily redundant, in the sense that they contribute to the definition of the 4-manifold." And: "This axiom is inevitable if the particle contains CTCs, because the state preparation and the measurement conditions can no longer be distinguished by causal arguments." That leads to the orthomodular, non-distributive lattice (V-text).

**Localised in time: wrong.** Axiom 2 makes the particle localised in *space* ("In any volume of 3-space an experiment to determine the presence of the particle will yield a true or a false value only"). [H00]'s model is a world tube $S^2\times\mathbb R$, which persists in time. The "4" in 4-geon refers to non-trivial *spacetime* (causal) structure, not to temporal localisation.

**Character of the return.** The "orientation flip / reversed handedness" on returning light is not in [H97] or [H00]. It is the batch's own conjecture, already marked unchecked, so no string. But it should not be attributed to Hadley.

### Strings (`notes/creative/batch-10.md`; each OLD occurs once at 32aacd9)

S1
- OLD: `localised in space **and** time`
- NEW: `localised in space (particle-like: Hadley 1997, Axiom 2) and persisting in time as a world tube (Hadley 2000: $S^2\times\mathbb R$)`

S2
- OLD: `it involves a failure of time-orientability in a small region.`
- NEW: `Hadley 1997 defines the 4-geon by non-trivial topology and causal structure with CTCs as "an essential feature" (Conjecture 1), and does not discuss time-orientability; Hadley 2000 adds that the fermion region is not time orientable, a global property ("time is not orientable around at least one class of non-contractable closed curves"), not a local failure (V-text, #this review).`

S3
- OLD: `whether Hadley's construction needs closed timelike curves near the geon is unchecked.`
- NEW: `Hadley's construction needs closed timelike curves: "The assumed existence of CTCs as an integral part of the structure ... is an essential feature of the manifold" (Hadley 1997, V-text), and his Axiom 4 (measurement sets boundary conditions) rests on them.`

Note (no string): the "If it does, it conflicts with the deck-element no-CTC condition (#352)" that follows S3 now reads as settled: it does. Strictly, #352's condition constrains deck elements of quotients. A 4-geon's CTCs conflict with it if the geon's topology is realised as a quotient; otherwise they conflict with any chronology assumption of the host class. The ledger L33 note "time-orientation/CTC questions open" is stale after this review, but it is not wrong.

## 2. Do 4-geons require CTCs?

**Yes, by Hadley's own definition** (Conjecture 1 and abstract, quoted above, V-text). README.md line 18, "4-geons in spacetimes that admit closed timeline curves", is consistent with this. "timeline" is a typo for "timelike" (noted only; not ours to edit).
- Strictly, Hadley's CTCs are "an integral part of the structure" of the particle, not just admitted by the ambient spacetime.
- Hadley 2000's spin-half argument uses non-time-orientability, not CTCs.

## 3. L34 and L35

**L34 (position as which-mouth gluing).**
- Prior art: Misner & Wheeler, "Classical physics as geometry", Ann. Phys. 2 (1957) 525 (charge without charge; wormhole mouths as charges), V-meta. Morris & Thorne, Am. J. Phys. 56 (1988) 395, V-meta. Visser, *Lorentzian Wormholes* (AIP 1995), V-meta.
- The identical-mouths remark matches topological-geon statistics (Friedman & Sorkin, PRL 44 (1980) 1100, V-meta per #339).
- Known in spirit, survives. Under the lock, the structural claim (only the gluing is uncertain for features inside $P(O)$) is correct as scoped to $P(O)$.
- Mild overclaim, no string: "the only uncertain position is topological" also omits beyond-edge continuations (patch-edge Prop 7.2).

**L35 (radar in a smooth host).**
- Prior art: Bondi k-calculus (Bondi, *Relativity and Common Sense*, 1964), V-meta. Dolby & Gull, "On radar time and the twin 'paradox'", Am. J. Phys. 69 (2001) 1257, V-meta. Perlick, "On the radar method in general-relativistic spacetimes" (2008, in *Lasers, Clocks and Drag-Free Control*), V-meta.
- Known, survives. No overclaim: the curved-space construction and the #346 null-boundary claim are both marked unchecked.

## Provenance notes

- David's 4:06 PM words are labelled "relayed …, not signed; verbatim". I cannot check the wording against a primary record.
- The batch's "Paper 1 contains a geon remark (#339) whose provenance Literature is checking" is accurate. Result: `papers/observer-space-ontology.md` l. 203 is an agent-written scope disclaimer (593b5ccd), not a David ruling. #339 was corrected in 1c0c1b0.

## Guardrails
- The forbidden symbol appears nowhere outside exact quotes; there are none in this file.
- No Born/$|a|^2$/$1/N$ result; the batch is structure only.
- No interpretation-camp framing.
- No pick among M1/M2/T-options.
- Paper 1 untouched.
- The batch makes no claim of a David geon ruling.

## Verdicts
- **L33:** Hadley's description is partly wrong (S1–S3):
  - CTCs are essential in 1997;
  - non-time-orientability is the 2000 paper and global;
  - not localised in time.
  - The future-measurement boundary-condition point is correct.
  - Survives as a lead set, now carrying a definite CTC cost.
- **L34:** known in spirit (Misner–Wheeler, wormhole literature); survives.
- **L35:** known (radar time: Bondi, Dolby–Gull, Perlick); survives.
