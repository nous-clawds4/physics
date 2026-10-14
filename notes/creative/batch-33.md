# Batch 33 — S8: can the spin structure be fixed for independent reasons? (paper only, DO NOT MERGE)

Paper only: no scripts (runs paused). Classical; no Born input, no |a|², no superposition by hand; no topology pick; (M1) untouched at L3; nothing in versions/ or papers/. CTCs adopted (David, 2:27 AM ET 2026-10-14, relayed via Physics Lead, not signed; unverified by Literature, no original seen; hold level unspecified; L162). Citations unchecked unless marked. Labels: **[CL]** = Creative Lead proposal or reading; **[C022]** = Claude 022; **[Geo]** = Geometry; **[PL]** = Physics Lead ruling.

## Plain summary for David

Batch 32 ended in a dilemma (Claude 022, Geometry; outcome per Physics Lead ruling, L167). Any exact condition on the closure loop's turn holds either for every route or only on isolated points or lines, never in bands, unless it is set by *discrete* data that the routes thread. The best such data is a single sign: in the spin-½ reading, a relative 2π turn gives −1. That sign depends on the **spin structure**, a choice of how spinors wrap around each loop. On a multiply connected world there are several choices: they form a torsor over H¹(M; ℤ₂).

So S8 asks: **can that choice be fixed for reasons that have nothing to do with getting interference?** If yes, the −1 is fixed by geometry (it passes T2). If we would have to pick it to make fringes come out, it fails (LT2).

We survey candidate "fixers": the cap or handle topology; requiring spinors to look trivial far away on ℝ³; requiring the spin structure to extend over the creation/capping region (which Gibbons–Hawking's pair rule already uses); time-orientation and Pin constraints; and conditions on how the routes thread the handles. For each we say whether it fixes the sign on the loops that matter, or leaves it free. **Outcome so far (Geometry/Literature reading, pending a Lead ruling):** none of the candidates fixes the sign on a loop that matters.
- **F6 fails:** the 2-handle's framing is fixed by the slice topology (only framing 0 gives S¹×S²), and the loop it fixes, the meridian, bounds the handle's core, so its sign was never free.
- **F3 is redundant:** requiring the spin structure to extend over a larger region fixes it only on loops that vanish there (in H₁(N; ℤ₂)), where the frame's turn alone already decides the sign.
- **F5's source is empty:** the loop with a free sign comes from the 1-handle, and 1-handles carry no framing.
- **Cancelling cap:** there is no choice to make, but the sign is then set by the frame's continuous turn, so it falls back into batch 32's second horn (isolated points, not bands).
- **π₁ = ℤ cap:** a two-way choice remains, as world data like Γ. Picking −1 by hand to get fringes would be LT2.
- **Which handle creates which summand** is itself a topology pick, for you.
Nothing is computed.

## 1. David's words

- David, 11:47 AM ET 2026-10-14, direct in Creative Lead chat, not signed (unverified by Literature, no original seen); verbatim: "Yes, that sounds like a good next step. Let's wait for Claude's review and then do that as the next step, unless the review points us in a different direction."
- **[PL]** Physics Lead ruled that Claude 022's review did not redirect, so S8 proceeds.

## 2. The question and why it is the escape [CL]

- **Dilemma** (#421 §8, L167): Hol(γ) depends real-analytically on continuous route data, and a fixed-point condition is an algebraic subset, so a condition holds everywhere or on a nowhere-dense set. Only locally constant data threaded by the routes escapes: (i) the class [γ] ∈ H₁(M; ℤ), and (ii) for a spinor, the sign ⟨s, [γ]⟩ ∈ ℤ₂ set by the spin structure s. (Strictly, spin structures form a torsor, not a group, so only differences of spin structures pair with [γ]; the sign itself is defined for a *framed* loop, relative to a reference, and depends on the frame's turn along γ as well as on s. That framing is the carried frame's turn, so it must not be chosen either.)
- **The spin-½ cancellation** (#419 R1, A1): with a spin-½ particle (L161, not adopted, an input until derived), two routes whose loop γ carries a relative 2π turn give a relative sign −1 *if* s assigns the non-trivial sign to [γ].
- **The question:** is s fixed by independent structure, at least on [γ]? The spin structures on M form a torsor over H¹(M; ℤ₂). Two choices differ on [γ] iff their difference class evaluates non-trivially on [γ] mod 2. So, for a fixed framing of γ, the sign on γ is free exactly when some class in H¹(M; ℤ₂) that is allowed by the fixer pairs non-trivially with [γ].
- **T2 test:** the fixer must be stated before fringes and motivated without them. A fixer chosen because it gives −1 on γ fails (LT2).

## 3. Candidate fixers (each a Creative Lead proposal)

| # | Fixer | Fixes the sign on [γ]? | Tuned to target? |
|---|---|---|---|
| F1 | **Cap/handle topology itself.** With the cancelling cap the closure is simply connected (S³ × I, #421 S1): H¹ = 0, so s is unique, but [γ] = 0 and the sign is trivially +1. With the π₁ = ℤ cap, H¹(M; ℤ₂) = ℤ₂ and two spin structures exist. | Cancelling cap: no choice (H₁(M) = 0); the spinor sign on γ is then fixed by the frame's turn alone (−1 for a relative 2π turn, as on a contractible loop), which is T2-clean but set by continuous data, so it stays in #421's second horn. π₁ = ℤ cap: **free** (two choices). | Choosing the cap to get room is a topology pick; not allowed here. Flag for David. |
| F2 | **Asymptotic triviality on ℝ³.** Require s to be the unique spin structure of ℝ³ outside a compact set. | Fixes s on loops that reach infinity; a loop through a handle is compactly supported, so its sign is **left free**. | Independent (natural boundary condition), but doesn't reach [γ]. |
| F3 | **Extension over the cobordism.** Require s on Σ₁ to extend over K₀₁ and K₁₂ (the spin-Lorentz cobordism Gibbons–Hawking use). A loop through the handle that bounds a disc in K₀₁ (the cancelling 2-handle) must get the bounding (+1) sign. | Fixes the sign on loops killed by the cobordism. For the π₁ = ℤ cap, the surviving loop is **not** killed, so its sign stays free. Since s is already a spin structure on M ⊇ K₀₁ ∪ K₁₂, extension adds nothing beyond requiring s on M: in general an extension over N ⊇ M fixes the sign only on loops that vanish in H₁(N; ℤ₂). | Independent: it is already part of the pair rule. Partial. Extension over *some* spin 4-manifold constrains nothing (Ω₃^Spin = 0: every spin 3-manifold bounds); F3 bites only through the given Lorentzian K₀₁, K₁₂ (Gibbons–Hawking). |
| F4 | **Time orientation / Pin.** An SL(2,ℂ) spin structure needs a time orientation (#421 R1); a non-orientable (G1) piece needs a Pin± structure, with its own obstruction (w₂ or w₂ + w₁²). | Restricts which worlds admit any structure; does not pick among the remaining choices. | Independent, but selects worlds, not the sign. |
| F5 | **Route-threading condition.** Require each member's carried frame to come back to itself round its own handle (an "untwisted" carrier), or require the spin structure to be the one induced by the members' framings. | Could fix ⟨s, [γ]⟩ through the framing of the handle the routes enclose. | **Risk of LT2:** if the framing is chosen to give −1, it is tuned. It needs an independent source. The 2-handle's framing is not one: the loop whose sign is free comes from the 1-handle, and 4D 1-handles carry no framing. |
| F6 | **Even framing from the creation 2-handle** (#421 S1: framing 0 gives the pair). Surgery on an unknot gives S¹×S² only for framing 0 (framing n gives L(n,1)), so the framing is fixed by the slice topology, not chosen. A spin structure extends over a 2-handle iff it restricts to the framed attaching circle as the bounding structure (Gompf–Stipsicz §5.7), so of S¹×S²'s two spin structures exactly one extends over D²×S², the one bounding on the meridian μ, while both extend over S¹×D³ (1-handle). | **No.** It fixes s on μ_B, but μ_B bounds the 2-handle's core in M, so [μ_B] = 0 and its sign was never free. The only free loop is the 1-handle summand's core, and neither F6 nor the reverse cap touches it. For the π₁ = ℤ cap, F3 + F6 leave two choices. | Independent, but does not reach [γ]. |

**Outcome (Geometry/Literature reading, pending a Lead ruling):** none of F1–F6 fixes the sign on a class [γ] ≠ 0 in H₁(M; ℤ₂). Extension-type fixers (F3, F6) fix s only on loops that vanish in M, where the spinor sign is set by the frame's turn alone (continuous data, #421's second horn). On the π₁ = ℤ cap's surviving class the ℤ₂ stays world data, like Γ: fixing it needs a non-topological principle, and choosing it to give −1 is LT2. F5 is at risk of LT2. Which handle creates which summand is itself cobordism data (a topology pick, for David).

## 4. What must be specified first [CL]

1. The cap: cancelling (π₁ trivial) or π₁ = ℤ (#421 S1). This is a topology choice, for David.
2. M's H¹(M; ℤ₂) and the class [γ], with γ's closing arcs and tube curves fixed (#421 §3).
3. Whether s must extend over K₀₁ ∪ K₁₂ (F3) and the 2-handle framings (F6).
4. The spin-½ candidate's status (L161, not adopted): without it there is no sign to fix.
5. Time orientation (assumed, #421) or a Pin setting.

## 5. Ill-posed questions to avoid

- "Which spin structure does the world have?" before the fixers are stated: it is world data, like Γ.
- "The sign of one route": only ⟨s, [γ]⟩ on a closed loop is defined.
- "Which spin structure gives the sign?" on a loop that vanishes in H₁(M; ℤ₂): there is no choice, and the spinor sign is fixed by the frame's turn (−1 for an odd number of 2π turns, as on a contractible loop), not "+1".
- "Is the sign −1?" as a goal: that is LT2.

## 6. Open scope questions (raised by Claude 022 and Geometry; held for David via Physics Lead, L167; not David's words)

- What, if anything, couples the frame at v_a.
- What curvature or topology lies between the routes (handles there change H₁ and H¹).
- Whether to look at Geroch's non-orientable alternative (Pin structures, Hadley 2000's setting).

## 7. Prior art (bibliographic data checked by Literature, #423, unless marked; texts unread)

Milnor, "Spin structures on manifolds", Enseign. Math. (2) 9, 198–203 (1963) (not on Crossref; standard, unverified); Geroch, J. Math. Phys. 9, 1739 (1968) and 11, 343 (1970) (noncompact 4D spacetime is spin iff it has a global orthonormal tetrad field: existence, not uniqueness; abstract read); Gibbons–Hawking, CMP 148, 345 (1992) (abstract read by Claude 021/022); Kirby–Taylor, "Pin structures on low-dimensional manifolds", in Geometry of Low-Dimensional Manifolds 2, LMS Lecture Note Ser. 151 (CUP 1990) 177–242; Lawson–Michelsohn, Spin Geometry (Princeton 1989); Chamblin, Commun. Math. Phys. 164, 65 (1994) (obstructions to non-Cliffordian pin structures; pin-Lorentz cobordism; abstract read); Hadley, CQG 17, 4187 (2000) (abstract read by Claude 021); Friedman–Sorkin, PRL 44, 1100 (1980) (metadata); Isham, Proc. R. Soc. A 362, 383 (1978) (twisted scalar fields) and Proc. R. Soc. A 364, 591 (1978) (spinor fields in four-dimensional space-time); Petry, J. Math. Phys. 20, 231 (1979) (exotic spinors); Avis–Isham, Nucl. Phys. B 156, 441 (1979) and Commun. Math. Phys. 72, 103 (1980) (inequivalent and generalized spin structures; quantum). Spin cobordism Ω₃^Spin = 0, Ω₄^Spin = ℤ (standard, not re-read).

## 8. Next step [CL]

Done on paper by Geometry (#423 H1–H6): F3 + F6 do not fix the sign on the surviving class (outcome above, pending a Lead ruling). Remaining: whether any non-topological principle fixes the π₁ = ℤ cap's ℤ₂, without choosing it to give −1 (LT2); and David's topology pick of which handle creates which summand. No runs.
