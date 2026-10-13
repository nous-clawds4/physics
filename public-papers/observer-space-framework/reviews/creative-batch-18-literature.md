# Literature pass: creative batch 18 (world-differing ledger states; L65–L69), PR #393

Reviewer: Literature agent. PR head recorded: `6acc5a0`, stacked on #390. Files: `notes/creative/batch-18.md`, `charter.md`, `ledger.md`. Do not merge. Marks: **V-text** = wording read by us (abstract or text); **V-meta** = bibliographic data verified, content from the standard account.

## Verdict

**Passes with must-fixes M1–M3.**
- Sets 1–3 are sound as [A]/sketch.
- The flat-quotient read-out is exactly the "ghost image" signature of cosmic topology. That is uncited prior art; see the note below.
- The one error is the topology-change carry-over from #380. It is stated as "needs time loops or a singularity" and "excluded classically (Geroch …)", which misstates both Geroch and Tipler.

## 1. David's words

- **10:43 PM quote and widget answer:** identical across `batch-18.md`, `charter.md` and `ledger.md`. Each is labelled "relayed by Physics Lead, Physics Lead chat, not signed; verbatim".
  - **Flag:** we have no original for either, so the verbatim text is unverified by us.
- **"the 'which handle structure are we in' idea you had at 3:43 PM"** (For David, catch 1): this is a further attribution to David that we cannot check against any original. Flag; no string.
- **10:37 PM:** Physics Lead has confirmed it verbatim. It is not restated in batch 18.

## 2. Flat 3-manifolds: classification

- **Hantzsche & Wendt, "Dreidimensionale euklidische Raumformen", Math. Ann. 110 (1935) 593–611 (V-meta; sometimes cited as 1934–35).** Their classification gives the 10 closed flat 3-manifolds: 6 orientable (G1–G6) and 4 non-orientable (B1–B4). G6 is the Hantzsche–Wendt manifold.
- **Wolf, *Spaces of Constant Curvature*, McGraw-Hill (1967) (V-meta):** the standard monograph.
- **Conway & Rossetti, "Describing the platycosms", arXiv:math/0311476 (V-text, introduction):** "That there are just 10 closed flat 3-manifolds — we propose to call them platycosms — has been known since around 1933." They give fundamental groups, covers and injectivity radii.
- **Relevance to the batch:**
  - Set 2 uses only 3-tori, $\mathbb R^{1,3}/\Lambda$. The general Γ of Set 1 also includes the other nine (rotation and screw parts; the four non-orientable ones are not space-orientable). The batch should say that Set 2 is the torus case of a 10-type classification. Note.
  - **Weak point 2 is confirmed and sharpened.** Fixing the topological type gives at most 10 compact flat options. But each type has continuous geometric moduli (the lattice parameters), so a choice of topology does not make the ledger states countable.
  - **No topology pick is made**, and none should be: David deferred topology.
- **Set 2 item 2:** isometry of flat tori is $\Lambda'=A\Lambda$ with $A\in O(3)$. Requiring the observer's frame data to be preserved (#324) restricts $A$ to the isotropy group, so the statement is consistent. Note: reflections are included only if the frame data allow them.

## 3. Cosmic topology: prior art for the read-out (Set 3)

- **Lachièze-Rey & Luminet, "Cosmic topology", Phys. Rep. 254 (1995) 135, doi:10.1016/0370-1573(94)00085-H (V-meta).** The standard review. In a multiply connected flat universe, a source has "ghost" images at displacements $g\in\Gamma$.
- **Cornish, Spergel & Starkman, "Circles in the sky", CQG 15 (1998) 2657 (V-meta).** Matched CMB circles as the topology signature.
- **Consequence:** Set 3's "a ray returns after $|g|$ with deck label $g$" is the observer-centred version of ghost images. Its novelty is only in the framing (a reply as the record of world revelation), not in the physics. The batch's "This is #370's result" (weak point 1) should be extended to this literature. Note; recommended citation.

## 4. Other checks

- **Set 1 (analytic continuation fixes the universal cover; worlds differ only by Γ and extension):** consistent with #370 (A). Chruściel–Isenberg 1993 (V-meta per #365) is cited correctly.
- **Far-handle flux excluded:** correct [A]. An analytic $F$ that vanishes on an open set vanishes everywhere. This is consistent with Misner–Wheeler (#386): the flux needs $F\neq0$ near the mouth.
- **Flat U(1) holonomy is classically unreadable** (Aharonov–Bohm is quantum): correct. Excluding it under 5:00 PM is consistent.
- **Misner/Taub–NUT parked, read by survival:** consistent with the same-extension correction (#383/#388). No "all end" claim.
- **Carry-overs:**
  - Simpson–Visser, the per-passage vs per-period trace and Dent et al. are not restated, so there is no error.
  - #391's interval definition of persistence: Set 4 uses "readable on every interval", which is consistent.
  - **Tipler/Borde/Geroch:** misstated (M1–M3). Per #380:
    - Geroch (compact region, time-orientable) shows that topology change brings CTCs, so it permits change with time loops or non-time-orientability.
    - Tipler and Borde forbid it outright with Einstein's equation and ordinary matter, "even at the price of singularities".

    So "would need time loops or a singularity" is wrong, and Geroch does not "exclude" it.

## Must-fixes (each OLD occurs once at 6acc5a0)

M1. `notes/creative/batch-18.md`
- OLD: `Topology can't change classically (that would need time loops or a singularity), so the ledger state is permanent: every entry is kept forever.`
- NEW: `With ordinary matter, Einstein's equations forbid topology change outright, even at the price of singularities (Tipler, Borde), and without time loops or time-flips it cannot happen at all (Geroch); so the ledger state is permanent: every entry is kept forever.`

M2. `notes/creative/batch-18.md`
- OLD: `topology change is excluded classically (Geroch 1967; Tipler 1977; Borde 1994; per #380).`
- NEW: `topology change in a compact region requires CTCs or non-time-orientability (Geroch 1967) and is forbidden outright for Einstein's equation with reasonable sources (Tipler 1977; Borde 1994, causally compact regions); per #380. In a CTC-free, time-orientable host such as $W_\Lambda$ it does not occur.`

M3. `notes/creative/ledger.md`
- OLD: `no classical topology change`
- NEW: `no topology change for reasonable sources in a CTC-free, time-orientable host; Tipler, Borde, Geroch per #380`

## Guardrails
- No forbidden Greek letter in the batch or in this file.
- **No count or measure from world-differing states.** Record classes are sets that refine and nest. Weak point 1 keeps the 0/1 "shares" of #359 parked. No 1/N, no Born rule, no weights.
- No M1/M2 pick; (M1) stays at L3.
- **No topology pick.** Lattices are an existence example only. The batch does not choose a topology, and the classification note above adds none.
- No T-option pick and no CTC pick. Set 3 is explicitly CTC-free; CTCs stay exploration only.
- No Everett framing.
- Paper 1 untouched; nothing goes into `versions/` or `papers/`.
- David's words are labelled relayed by Physics Lead, not signed. They are unverified by us (flagged above).
- No geon ruling.

## Rows
- **L65:** live.
- **L66:** live. Note that the tori are one of 10 flat types (Hantzsche–Wendt), with continuous moduli.
- **L67:** live. Cite cosmic topology (Lachièze-Rey–Luminet; Cornish–Spergel–Starkman).
- **L68:** live, after M2/M3.
- **L69:** open. Weak point 2 is confirmed: the classification does not make the states countable.
