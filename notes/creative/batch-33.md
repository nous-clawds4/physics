# Batch 33 — S8: can the spin structure be fixed for independent reasons? (paper only, DO NOT MERGE)

Paper only: no scripts (runs paused). Classical; no Born input, no |a|², no superposition by hand; no topology pick; (M1) untouched at L3; nothing in versions/ or papers/. CTCs adopted (David, 2:27 AM ET 2026-10-14, relayed via Physics Lead, not signed; unverified by Literature, no original seen; hold level unspecified; L162). Citations unchecked unless marked. Labels: **[CL]** = Creative Lead proposal or reading; **[C022]** = Claude 022; **[Geo]** = Geometry; **[PL]** = Physics Lead ruling.

## Plain summary for David

Batch 32 ended in a dilemma (Claude 022, Geometry; outcome per Physics Lead ruling, L167). Any exact condition on the closure loop's turn holds either for every route or only on isolated points or lines, never in bands, unless it is set by *discrete* data that the routes thread. The best such data is a single sign: in the spin-½ reading, a relative 2π turn gives −1. That sign depends on the **spin structure**, a choice of how spinors wrap around each loop. On a multiply connected world there are several choices: they form a torsor over H¹(M; ℤ₂).

So S8 asks: **can that choice be fixed for reasons that have nothing to do with getting interference?** If yes, the −1 is fixed by geometry (it passes T2). If we would have to pick it to make fringes come out, it fails (LT2).

We survey candidate "fixers": the cap or handle topology; requiring spinors to look trivial far away on ℝ³; requiring the spin structure to extend over the creation/capping region (which Gibbons–Hawking's pair rule already uses); time-orientation and Pin constraints; and conditions on how the routes thread the handles. For each we say whether it fixes the sign on the loops that matter, or leaves it free. Early reading: most candidates fix the sign on loops that stay inside one region, but leave it free on exactly the loops the two routes form around a handle. The cap that leaves π₁ = ℤ is the case to check first. Nothing is computed.

## 1. David's words

- David, 11:47 AM ET 2026-10-14, direct in Creative Lead chat, not signed (unverified by Literature, no original seen); verbatim: "Yes, that sounds like a good next step. Let's wait for Claude's review and then do that as the next step, unless the review points us in a different direction."
- **[PL]** Physics Lead ruled that Claude 022's review did not redirect, so S8 proceeds.

## 2. The question and why it is the escape [CL]

- **Dilemma** (#421 §8, L167): Hol(γ) depends real-analytically on continuous route data, and a fixed-point condition is an algebraic subset, so a condition holds everywhere or on a nowhere-dense set. Only locally constant data threaded by the routes escapes: (i) the class [γ] ∈ H₁(M; ℤ), and (ii) for a spinor, the sign ⟨s, [γ]⟩ ∈ ℤ₂ set by the spin structure s.
- **The spin-½ cancellation** (#419 R1, A1): with a spin-½ particle (L161, not adopted, an input until derived), two routes whose loop γ carries a relative 2π turn give a relative sign −1 *if* s assigns the non-trivial sign to [γ].
- **The question:** is s fixed by independent structure, at least on [γ]? The spin structures on M form a torsor over H¹(M; ℤ₂). Two choices differ on [γ] iff their difference class evaluates non-trivially on [γ] mod 2. So the sign on γ is free exactly when some class in H¹(M; ℤ₂) that is allowed by the fixer pairs non-trivially with [γ].
- **T2 test:** the fixer must be stated before fringes and motivated without them. A fixer chosen because it gives −1 on γ fails (LT2).

## 3. Candidate fixers (each a Creative Lead proposal)

| # | Fixer | Fixes the sign on [γ]? | Tuned to target? |
|---|---|---|---|
| F1 | **Cap/handle topology itself.** With the cancelling cap the closure is simply connected (S³ × I, #421 S1): H¹ = 0, so s is unique, but [γ] = 0 and the sign is trivially +1. With the π₁ = ℤ cap, H¹(M; ℤ₂) = ℤ₂ and two spin structures exist. | Cancelling cap: fixed but trivial. π₁ = ℤ cap: **free** (two choices). | Choosing the cap to get room is a topology pick; not allowed here. Flag for David. |
| F2 | **Asymptotic triviality on ℝ³.** Require s to be the unique spin structure of ℝ³ outside a compact set. | Fixes s on loops that reach infinity; a loop through a handle is compactly supported, so its sign is **left free**. | Independent (natural boundary condition), but doesn't reach [γ]. |
| F3 | **Extension over the cobordism.** Require s on Σ₁ to extend over K₀₁ and K₁₂ (the spin-Lorentz cobordism Gibbons–Hawking use). A loop through the handle that bounds a disc in K₀₁ (the cancelling 2-handle) must get the bounding (+1) sign. | Fixes the sign on loops killed by the cobordism. For the π₁ = ℤ cap, the surviving loop is **not** killed, so its sign stays free. | Independent: it is already part of the pair rule. Partial. |
| F4 | **Time orientation / Pin.** An SL(2,ℂ) spin structure needs a time orientation (#421 R1); a non-orientable (G1) piece needs a Pin± structure, with its own obstruction (w₂ or w₂ + w₁²). | Restricts which worlds admit any structure; does not pick among the remaining choices. | Independent, but selects worlds, not the sign. |
| F5 | **Route-threading condition.** Require each member's carried frame to come back to itself round its own handle (an "untwisted" carrier), or require the spin structure to be the one induced by the members' framings. | Could fix ⟨s, [γ]⟩ through the framing of the handle the routes enclose. | **Risk of LT2:** if the framing is chosen to give −1, it is tuned. It needs an independent source (e.g. the 2-handle's framing, which spin already fixes even). |
| F6 | **Even framing from the creation 2-handle** (#421 S1: framing 0 gives the pair). The framing parity is fixed by the existence of a spin structure, and could determine the induced s on the core loop. | Possibly fixes the sign on the handle's core loop. **To check.** | Independent: it comes from the pair rule. The most promising. |

**Early reading [CL]:** F2–F4 fix or restrict s only away from [γ]. F1 is either trivial or leaves the sign free. F6 (with F3) is the one candidate that might fix the sign on the core loop for independent reasons. F5 is at risk of LT2.

## 4. What must be specified first [CL]

1. The cap: cancelling (π₁ trivial) or π₁ = ℤ (#421 S1). This is a topology choice, for David.
2. M's H¹(M; ℤ₂) and the class [γ], with γ's closing arcs and tube curves fixed (#421 §3).
3. Whether s must extend over K₀₁ ∪ K₁₂ (F3) and the 2-handle framings (F6).
4. The spin-½ candidate's status (L161, not adopted): without it there is no sign to fix.
5. Time orientation (assumed, #421) or a Pin setting.

## 5. Ill-posed questions to avoid

- "Which spin structure does the world have?" before the fixers are stated: it is world data, like Γ.
- "The sign of one route": only ⟨s, [γ]⟩ on a closed loop is defined.
- "Does the spinor flip sign?" on a contractible loop: the answer is always +1.
- "Is the sign −1?" as a goal: that is LT2.

## 6. Open scope questions (from David via Physics Lead, L167)

- What, if anything, couples the frame at v_a.
- What curvature or topology lies between the routes (handles there change H₁ and H¹).
- Whether to look at Geroch's non-orientable alternative (Pin structures, Hadley 2000's setting).

## 7. Prior art (bibliographic, unchecked unless marked)

Milnor, "Spin structures on manifolds", Enseign. Math. 9 (1963) 198; Gibbons–Hawking, CMP 148, 345 (1992) (abstract read by Claude 021/022); Kirby–Taylor, "Pin structures on low-dimensional manifolds" (1990); Lawson–Michelsohn, Spin Geometry (1989); Hadley, CQG 17, 4187 (2000) (abstract read by Claude 021); Friedman–Sorkin, PRL 44, 1100 (1980) (metadata); Petry 1979 / Isham 1978 on twisted spinor fields and inequivalent spin structures (unchecked).

## 8. Next step [CL]

On paper: for the π₁ = ℤ cap and the cancelling cap, compute H¹(M; ℤ₂), [γ], and whether F3 + F6 fix ⟨s, [γ]⟩. Bring it to Geometry. No runs.
