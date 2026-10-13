# Literature pass: creative batch 16 (L54–L59), PR #385

Reviewer: Literature agent. PR head recorded: `ffd602d` (base `creative/batch-15`). Files: `notes/creative/batch-16.md`, `batch-16/threading.py`, `results.txt`, `ledger.md`. Do not merge. Marks: **V-text** = wording read (abstract or text); **V-meta** = bibliographic data verified, content from the standard account. **No errors requiring OLD/NEW strings were found**; the notes below are citation upgrades.

## 1. Visser thin-shell wormholes (Set 1 host)

- **Visser, "Traversable wormholes: some simple examples", PRD 39 (1989) 3182, arXiv:0809.0907 (V-text abstract).**
  - These are non-spherically symmetric examples in which "it is possible for a traveler to traverse such a wormhole without passing through a region of exotic matter".
  - "the weak-energy condition is violated".
- **Visser, "Traversable wormholes from surgically modified Schwarzschild spacetimes", NPB 328 (1989) 203, arXiv:0809.0927 (V-text abstract).**
  - Two Schwarzschild exteriors are grafted together with "a non-zero stress-energy on the boundary layer".
  - A partial dynamical stability analysis "places constraints on the equation of state of the exotic matter".
- **One-universe versions.** Neither abstract states the one-universe (intra-universe) construction. I verified no text for it, so the batch's [M] tag on "Visser-type … on $\mathbb R^3$" should stay.
- **Topology check [A].** The batch's gluing "with a reflection" is the choice that keeps the handle orientable. Gluing the two spheres by a pure translation gives a non-orientable handle instead, which is Sorkin's setting (§5). The batch has this right, and the spatial $\pi_1=\mathbb Z$ is correct. Note: say explicitly that the reflection is what fixes orientability.

## 2. MTY 1988 and Frolov–Novikov 1990 (Set 2)

- **Morris, Thorne & Yurtsever, PRL 61 (1988) 1446 (V-text abstract):** a maintained wormhole "can be converted into a time machine with which causality might be violatable". The threshold "time shift > outside light-travel time" is the standard account in the paper body (V-meta here).
- **Frolov & Novikov, PRD 42 (1990) 1057 (V-text abstract):** "the interaction of a wormhole with the surrounding matter and with the external gravitational field almost inevitably transforms it into a time machine."
- **Consequence (note):** the batch's "static symmetric host is CTC-free" is correct as stated [A]. But per Frolov–Novikov, generic external fields produce the offset. So "CTC-free" is non-generic once the host is embedded with other masses (e.g. the "bound to some other mass" parking of Set 1).
- No pick on CTCs; the choice stays David's.

## 3. Misner–Wheeler 1957 (Set 3 flux)

**Misner & Wheeler, "Classical physics as geometry", Ann. Phys. 2 (1957) 525 (V-text abstract and p. 534).**
- Charge is "source-free electromagnetic fields that … are trapped in the worm holes of a space with a multiply-connected topology".
- p. 534: the field equations and multiple connectivity "force one to the conclusion that the wormhole flux remains invariant. This constant of the motion represents the charge. The charge or wormhole flux is unquantized."

How this bears on the batch:
- **Conservation:** this matches the batch's "topologically conserved" (H₂ class).
- **Change when a charge passes through:** M–W treat source-free fields only. The batch's $\Delta\Phi_A=q$ per passage is its own [A] from $d\star F=J$. It is correct: Gauss's law on the mouth sphere $S_A$ counts the charge that crossed it.
- **"Unquantized":** this is V-text support for the batch's L58 position that discreteness is not derived classically.
- **Citation fix (note):** Wheeler's companion paper is Ann. Phys. 2 (1957) 604 (V-meta). The L57 tags "Wheeler 1957, Misner–Wheeler 1957 (unchecked)" can be upgraded to V-text for M–W.

## 4. Wormhole flux as memory; identical carriers ⇒ discreteness

- **Flux as a memory:** I verified no prior art treating wormhole flux as a written record.
  - Khusnutdinov–Bakhmatov, arXiv:0802.1358, "Electrostatic interaction of a pointlike charge with a wormhole", turned up in search. I did not verify its content, so I cite nothing from it.
- **"Identical carriers make the flux discrete" without quantum input:** I found no verified prior art. It follows trivially from additivity: $\Phi=\Phi_0+nq_0$. M–W's "unquantized" (V-text) confirms that geometry alone does not give it. The batch's flag (an assumption about matter, near a law of R by fiat) stands.

## 5. Non-orientable and non-time-orientable handles and charge (weak point 7)

- **Sorkin, "On the relation between charge and topology", J. Phys. A 10 (1977) 717 (V-text abstract):** "The generalization of Stokes' theorem to non-orientable manifolds shows that a suitable topology can appear to carry net electromagnetic charge"; read this way, "one explains the non-existence of magnetic monopoles".
- **Diemer & Hadley, "Charge and the topology of spacetime", CQG 16 (1999) 3567, gr-qc/9905069 (V-text abstract):** "electrically charged wormholes in which the outer 2-sphere is not spanned by a compact, co-orientable hypersurface … can therefore display net electric charge from the source-free Maxwell equations", extending Sorkin "to spacetimes which do not admit a time orientation".
- **"Friedman":** I verified no specific Friedman paper on charge and orientability, so I cite none.
- **Assessment:** the batch's weak point 7 says that "a non-time-orientable handle flips charge sign along the loop", which would make the flux record orientation-dependent. The literature says something stronger:
  - on a non-co-orientable handle, the outer sphere can carry **net** charge with no sources;
  - so the flux is no longer a closed-handle invariant tied to net passages.

  In Hadley-type geons, the flux record would therefore mix the host's intrinsic topological charge with written passages. The weak point is right to flag the concern, but should cite Sorkin 1977 and Diemer–Hadley 1999. Note, no string: the batch marks it unchecked.

## 6. Geodesic instability of the threading orbit (L55)

- **Independent check [A].** Model each traversal as a convex-mirror map with power $2/a$, and the gap as a free flight of length $L$. One period (two traversals) has monodromy trace $(2+2L/a)^2-2=4(1+L/a)^2-2$. This gives 14, 62 and 322 for $L/a=1,3,8$, matching the batch's [N].
  - It is the classic two-disc dispersing-billiard result.
  - The mirror equivalence for a flat, reflection-glued thin shell is my [A]; I verified no literature statement of it.
- **"as for any NEC-violating throat":** this is an overreach in wording. NEC violation gives defocusing of null congruences at the throat (the flaring-out condition, Morris–Thorne). Stability of a specific closed timelike orbit is a separate statement, and batch 15's Simpson–Visser T class shows that threading orbits *can* be stable with mouth gravity. The batch itself admits this in weak point 6. Note, no string.
- **Prior art:** I verified no paper on the stability of closed geodesics threading a one-universe handle.

## 7. Batch-internal checks

- **L57:** dissipation-proofness via $d\star F=J$ is correct. Radiation fields are sourceless, so the flux through $S_A$ changes only by charge crossing.
- **L59:** GW memory as a continuum record is consistent with #380.
- **Ledger L56:** "(MTY 1988; Frolov–Novikov 1990, unchecked)" can become V-text abstracts. That's a note, not an error.

## Strings

None. No OLD/NEW string is warranted at ffd602d. The upgrades in §§1–3 and 5 are optional citation edits for the Creative Lead.

## Guardrails
- No forbidden Greek letter in this file.
- No Born/$|a|^2$/$1/N$ result. The batch disclaims the Born rule, probability and measure. Dirac quantisation is excluded under 5:00 PM, which is consistent.
- No Everett framing.
- No pick among M1/M2/T-options or on CTCs; Set 2 is "noted", exploration only (4:16 PM).
- Paper 1 untouched.
- The rulings are labelled relayed by Physics Lead, not signed.
- No geon ruling is claimed. "Not a Hadley geon" is stated.

## Verdicts
- **L54 (one-universe winding):** correct as topology. Live; the host is Visser-type [M for one-universe].
- **L55 (threading orbit dead):** the numerics are confirmed analytically. The "any NEC-violating throat" wording overreaches (note).
- **L56 (MTY tie-back):** consistent with the MTY and Frolov–Novikov abstracts (V-text). By Frolov–Novikov, the offset is generic once there are external fields.
- **L57 (flux record):** correct. Conservation is V-text from Misner–Wheeler, and the passage rule $\Delta\Phi=q$ is [A].
- **L58 (discreteness conditional):** correct. M–W's "unquantized" (V-text) supports it, and I found no prior art deriving discreteness classically.
- **L59 (GW memory):** consistent.
- **Weak point 7:** understated. Sorkin and Diemer–Hadley show that a non-(co-)orientable handle can carry net source-free charge, so in Hadley geons the flux record is not a pure passage count.
