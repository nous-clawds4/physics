# Batch 34 — S9: pairing rule, exact vs tolerance, and the leftover count (paper only + one short check, DO NOT MERGE)

Paper only, plus one short committed check script (point 3). Classical; no Born input; no |a|², no superposition by hand; (M1) untouched at L3; nothing in versions/ or papers/. CTCs adopted (David, 2:27 AM ET 2026-10-14, relayed via Physics Lead, not signed; unverified by Literature, no original seen; hold level unspecified; L162). Citations unchecked unless marked. Labels: **[CL]** = Creative Lead proposal or reading; **[Geo]** = Geometry; **[C022]** = Claude 022.

## Plain summary for David

You described a circle of dots, one per path. Dots that "line up" pair off as virtual particles and vanish; leftover dots must be absorbed by the detector. Evenly spread dots mostly pair, while a clump leaves many unpaired, and that would make the pattern. We checked three things.

1. **What "line up" means.** For two paths to cancel, their dots must sit *opposite* each other on the circle, half a turn apart. Equal dots reinforce. For a clock hand, "opposite" breaks the alignment you asked for (#419). With spin-½, a relative full turn shows up as a sign flip, so aligned paths can still cancel. That sign depends on the spin structure, and on a loop that goes round a surviving handle it is a two-way choice (#423). So the clean version of your rule is: **two paths cancel when the spinor sign round the loop they form is −1, under the spin-½ reading. That sign is the product of the spin-structure value on the loop's class (a two-way choice only if the loop goes round a surviving handle an odd number of times) and the sign from its relative full turns; only the product is defined, so the same loop cancels in one spin structure and reinforces in the other.**
2. **Exact or approximate.** If the dots move continuously, exactly opposite pairs are rare (measure zero; Geometry's #421 dilemma). A tolerance would be a number we put in by hand. Discrete phases (signs set by which handles a loop goes round) avoid this. Among the options we listed, they are the only one that can be fixed without tuning (other discrete data, such as non-abelian handle classes, finite holonomy groups, or an isometry exchanging routes, would also qualify), and that again points to handles between the routes.
3. **How many are left over.** With "remove opposite pairs" as the rule, the leftover count is at least the **length** of the arrow sum |Σ e^{iφ}| (for exactly opposite pairs; approximately, with a tolerance), so near dark fringes it cannot fall below that length. This is a negative result for this pairing rule as posed, not a refutation of every rule. The triangle inequality gives a floor: at least that many dots are left. In our toy (greedy matching within a tolerance, N = 400) the log-log slopes are 0.5–0.9. **That does not match quantum-mechanical frequencies**, and we do not adjust the rule to make it match. This is the biggest obstacle found so far for the pairing picture as stated.

**Bearing on the topology choice** (recommendation, for you to rule on): only the cap that leaves one handle (π₁ = ℤ), with the closed route loop crossing the 1-handle summand A's S² an odd number of times (in 3D space a loop has no "sides"), gives the discrete sign that point 1 needs and point 2 allows. The cancelling cap leaves no sign. We recommend the π₁ = ℤ cap, keeping the remaining ℤ₂ spin choice as world data (both spin structures kept as separate worlds, each with its own fixed sign, neither picked; comparing them would need the measure μ, which stays open). It is your call. But point 3 means this alone does not give quantum-mechanical frequencies.

## 1. David's words (verbatim as reported by Creative Lead, direct in Creative Lead chat, not signed; unverified by Literature, no original seen)

- David, 1:58 PM ET 2026-10-14: "Before we make the topology choice, let me see if I understand where things stand. In my mind, two independent paths from the emitter to the detector have the option of cancelling if (and only if) their phases line up perfectly. What that means is that the virtual particles annihilate each other and are never seen by the detector. The only other option, besides wiring up to another virtual particle, would be to be absorbed by one of the particles in the detector, perhaps through a mechanism similar to the wiring together of two virtual particles. The idea is that if we look at “all possible” paths from source to the i_th detector d_i, then for some values of i, then “most” virtual particles pair together, which means there are (relatively) few remaining ones to interact with the detector. We can envision a circle, with dots along the rim, each one indicating the phase of one path. If the dots are evenly distributed, then most of the particles get paired in this manner. But for other values of i, the dots are not evenly distributed; there is a clump of dots at some position on the circle, and they cannot pair up with any other virtual particles, and self-consistent means the only other option is that they wire up with a particle in the detector. In this manner, we get an interference pattern. This is a qualitative picture, and we have not yet addressed why the phases might be evenly distributed for some values of i but not for others; but this is what I currently envision."
- David, 2:01 PM ET 2026-10-14: "Yes, let's deal with points 1-3. I am very much hoping the MTW spin-1/2 okays the role we want it to play. And I wonder: do points 1-3 help us make the topology choice? I may need to rely upon you to help me make the topology choice."

(Points 1–3 are Creative Lead's framing from chat.)

## 2. Point (1): the pairing rule [CL]

- **Equal phase:** arrows e^{iφ} coincide and reinforce. Equal phase cannot be the cancelling rule.
- **Relative π (clock hand):** cancels under arrow addition, but breaks David's 1:54 AM alignment condition, since the loop then winds an odd multiple of π (#419 R1, Geometry pass).
- **Relative 2π with the spin-½ sign −1:** aligned *and* cancelling (#419 R1/A1). It needs (i) a spin-½ particle (L161, not adopted; MTW §41.9, unchecked) and (ii) a spin structure s.
  - On a loop γ that vanishes in H₁(M; ℤ₂), the sign is fixed by the frame's turn alone: −1 for an odd number of 2π turns (#423 H6). That turn is continuous data, so this falls into #421's second horn.
  - On a class [γ] ≠ 0, the sign also depends on s, a ℤ₂ choice that no topological fixer settles (#423, L169: reading pending a Lead ruling).
- **Reading:** David's "line up perfectly" is best read as "relative 2π turn with the spin-½ sign −1". The discrete part of that sign lives only on loops round a surviving handle.
- **Note on David's "if (and only if)":** a sign −1 makes a pair cancel. "Only if" also excludes all other pairings, so the rule is exclusive. Whether unpaired dots can also partially cancel (three at 120°) is not covered by pairwise annihilation; triples (David 1:36 AM) would be a separate rule.

## 3. Point (2): exact versus tolerance [CL]

| Option | Fixed independently (T2)? | Notes |
|---|---|---|
| **Exact** match of continuous phases | Yes, but empty | Measure zero: holds only on isolated points or lines (#421 X3, assuming real-analytic dependence) |
| **Tolerance δ** | **No**: δ is a scale put in by hand (LT2), unless some geometric length sets it (e.g. ℓ/λ_E; λ_E is still undefined, for David) | The leftover count depends on δ (§4) |
| **Discrete phases** (signs from H₁ class and spin structure) | **Yes**, if the class is set by which handles the routes thread and s is world data | Locally constant, so it gives bands. Needs handles between the routes or the π₁ = ℤ cap |
| **Deterministic matching rule** (e.g. pair each path with its "mirror" route) | Only if the rule comes from the geometry (e.g. an isometry exchanging routes) | Otherwise it is chosen, so LT2 |

**Reading:** among the options listed, only discrete phases pass T2 without a free scale. Other locally constant data (the class of γ in π₁ for non-abelian deck groups, finite holonomy ℤ_n, or a geometric route-exchanging isometry) would also pass, as would a δ set by a geometric length once λ_E is defined.

## 4. Point (3): the leftover count [CL]

- **Bound (paper).** Let N dots have resultant R = |Σ e^{iφ_k}|. Remove pairs that are exactly opposite (with a tolerance δ each removed pair leaves a residual of up to 2 sin(δ/2), so the bound is then approximate; it held in the toy, min(leftover − R) ≥ 0.2): each removed pair contributes 0 to the sum, so the remaining dots alone have resultant R. They are unit vectors, so their count is at least R. **Leftover ≥ R**, with equality when the leftovers all point the same way (a clump). With a tolerance δ each removed pair contributes up to 2 sin(δ/2), so the bound becomes leftover ≥ R − P·2 sin(δ/2) for P removed pairs. The floor is the decisive point: no rule of this kind can give a count that falls below R (up to the tolerance term) near dark fringes, so minima cannot be darker than linear in R, and the rule does not match quantum-mechanical frequencies.
- **Toy cases.** N = 2 opposite: leftover 0 = R. N = 3 at 120°: R = 0, but no pair is opposite, so leftover is 3 under pairwise rules. N dots clumped at one phase: leftover N = R.
- **Numeric check** (`batch-34/pairing.py`; greedy antipodal matching within tolerance δ; von Mises phases, N = 400, 20 reps × 8 concentrations):

| δ | log-log slope of leftover vs R | median leftover/R |
|---|---|---|
| 0.05 | 0.49 | 1.68 |
| 0.2 | 0.77 | 1.31 |
| 0.5 | 0.93 | 1.16 |

  For small δ there is a noise floor of unmatched dots; as δ grows, leftover → R (slope → 1). Toy conditions: greedy antipodal matching in random order, von Mises phases, N = 400, 20 reps × 8 concentrations, fit over R > 5; reproduced by Literature (#424). The bound does not cap the leftover from above (three dots at 120°: R = 0, leftover 3). The "slope" is one log-log fit pooled across concentrations at fixed N = 400 (R > 5 only; leftover ≤ N), so it describes this family, not a scaling law; the bound above is the general statement.
- **Plain statement:** under pairwise annihilation of exactly opposite dots the leftover at d_i is at least |Σ e^{iφ}| (proved above), and in the toy it grows at most about linearly with it. This is a statement about this rule as posed, not about every pairing rule. **This does not match quantum-mechanical frequencies.** We do not adjust the rule to match them: a rule designed to reproduce them would be aiming at the answer (LT2). Any other rule must be motivated independently and fixed before frequencies are compared.
- **Pinned:** `pairing.py` sha256 0386d7bbf32feb88501becb6e4319aedff9508d8e202332dcc756f6a5cb2cc04; `pairing_out.txt` sha256 318c92c943b8abbec75f3abb41b13cc367b5fd98a040702ab910933c38e8ed0c. Run: `cd notes/creative/batch-34 && python3 pairing.py` (Linux x86_64, Python 3.13.5, numpy 2.2.4, seeded RNG 34); output byte-identical to `pairing_out.txt` (reproduced by Geometry and Literature, #424).

## 5. Bearing on the topology choice (for David)

David asked (2:01 PM) whether points 1–3 help with the topology choice, and said he may need to rely on Creative Lead here. What each answer to (1) requires:

| Reading of "line up" | Cap | Handle-to-summand assignment |
|---|---|---|
| Relative π, clock hand | Either | None needed, but it breaks alignment |
| Spin-½, sign from the frame's turn only (loop vanishes in H₁) | Cancelling cap (S³ × I) | None. Continuous data, so measure zero (point 2) |
| Spin-½, discrete sign on [γ] ≠ 0 | **π₁ = ℤ cap** | The surviving class must be the **1-handle summand's core (A)**, with the closed route loop γ = route 1 · route 2⁻¹ (closing arcs as in #421 §3) meeting A's S² (its belt sphere) an odd number of times algebraically, i.e. [γ] = odd·[core_A] in H₁(M; ℤ₂). (In 3+1 a loop does not separate a slice, so "either side" has no meaning; the intersection with the S² is the condition.) The 2-handle summand's meridian bounds and carries no free sign (#423 H4) |

**Creative Lead recommendation (for David to rule on; not a choice):** the π₁ = ℤ cap, with the closed route loop meeting A's S² (belt sphere) an odd number of times algebraically ([γ] = odd·[core_A] in H₁(M; ℤ₂)). Keep the remaining ℤ₂ spin-structure choice as world data, both values kept as separate worlds and neither picked (both spin structures, each a separate world with its own fixed sign), so that picking −1 by hand (LT2) is avoided. Each world has its own fixed sign, opposite on [γ]; comparing or combining the two would need the measure μ, which stays open (#419 R5). This is the only option that gives the discrete, untuned phase that points 1–2 require. Caveat (point 3): even then, pairwise annihilation gives a leftover linear in the resultant, not its square, so this choice does not by itself reach quantum-mechanical frequencies.

## 6. Ill-posed questions to avoid

- "How many dots are at d_i?" before the set of "all possible paths" and its counting are defined (μ open).
- "Do these two paths pair?" without a rule fixed before fringes.
- "The phase of one path": only loop data (pairs) are defined.

## 7. Prior art (bibliographic data checked by Literature in #418/#419/#424; texts unread)

Feynman–Hibbs 1965 (arrows/clock hands); MTW, Gravitation (1973) §41.9 (ToC checked; text unchecked); Schulman 1968 and Laidlaw–DeWitt 1971 (the quantum rule, not imported); random walks on the circle and greedy matching (standard).
