# Batch 32 — S7: the smallest Gibbons–Hawking closure in 3+1 (paper only, DO NOT MERGE)

Paper only: no scripts (runs paused, David 11:51 PM ET 2026-10-13). Classical; no Born input, no |a|², no superposition by hand; (M1) untouched at L3; nothing in versions/ or papers/. CTCs adopted (David, 2:27 AM ET 2026-10-14, in Physics Lead chat, relayed via Physics Lead, not signed; unverified by Literature, no original seen; hold level unspecified; L162). Citations unchecked unless marked. The task is Claude 021's S7 (a reviewer proposal, run under a Lead ruling). Labels: **[CL]** = Creative Lead proposal or reading; **[Geo]** = Geometry's reading; **[C021]** = Claude 021's reading.

## Plain summary for David

Batch 31's weak point (Claude 021): nothing in the geometry yet makes two geons annihilate *only when their phases line up*. Topology lets any pair be capped off, and the known rules (metric, causality, spin structure, energy conditions) never look at the phase. This batch sets up the smallest concrete case where that could change:
- **The closure:** in 3D space, two wormhole handles (each an S¹×S² summand) appear together and later close off together. With a spin structure, and a compact topology-changing region with a Lorentzian metric and spacelike boundary, wormholes can only be made or removed in pairs (Gibbons–Hawking 1992: a single wormhole is impossible, pairs are kinematically possible; with "kinks" in the boundary the count can change), so a pair is the smallest allowed case. 2D space can't host this at all.
- **Where the CTCs sit:** by an argument (not a theorem), Geroch's CTCs can be confined to the moments where the topology changes. We put them at the capping vertex, where the pair closes off.
- **The question (reframed per Geometry):** EKT showed that with CTCs, a classical billiard ball must be self-consistent. A little frame (a clock hand) carried round a CTC must likewise come back matching itself. The geometry already fixes how far the hand turns round any loop, so self-consistency cannot *force* that turn. What it can do is restrict the frame's own data, or rule out whole worlds in which no self-matching frame exists. The question is whether the worlds it rules out are exactly the ones where the pair's phases fail to line up, and whether that depends on the routes. Two cautions: a passive frame does not push back on anything, so unlike EKT's balls it gives no extra solutions unless it couples to something; and the constraint reaches the closure loop only if that loop is itself a CTC, or is joined to one by a region whose geometry we know. If yes, "they annihilate only if their phases line up" (batch 31's plain-summary wording, a Creative Lead paraphrase, not David's verbatim words) would come out of structure we already have, with no ħ and no rule for adding arrows. If no, the exclusion route is parked, like batch 23's Set 1.

Nothing is computed. Below are the setup, what has to be specified, and what would count as yes or no.

## 1. Setup [CL]

- **Object spacetime M:** a 3+1 Lorentzian manifold. Slices: Σ₀ (before) ≅ Σ₂ (after) ≅ some fixed 3-manifold (ℝ³ near the lab); Σ₁ (between) ≅ Σ₀ # (S¹×S²) # (S¹×S²).
- **Closure:** a compact cobordism K₀₁ from Σ₀ to Σ₁ (creation vertex v_c), a product region Σ₁ × [t₁, t₂] (members carried, batch 30 B5), and K₁₂ from Σ₁ to Σ₂ (capping vertex v_a).
- **Why pairs:** in a compact region with a Lorentzian metric, spacelike boundary and a spin structure, single wormhole creation is impossible but pairs are possible; the selection rule is a mod-2 invariant of the closed boundary 3-manifold (the Kervaire semi-characteristic), so for our asymptotically ℝ³ slices it applies to a compact sub-region or the one-point compactification (unchecked); wormholes plus kinks are conserved mod 2 (Gibbons–Hawking, CMP 148, 345 (1992); PRL 69, 1719 (1992); abstracts read by Claude 021). These results are stated for compact slices; with Σ₀ ≅ ℝ³ near the lab a version for compactly supported change (or the one-point compactification) is needed [unchecked].
- **Why 3+1:** in 2+1 a compact non-degenerate Lorentzian cobordism needs equal Euler characteristics at its two ends (Sorkin, PRD 33, 978 (1986); abstract read by Claude 021), and a handle changes a surface's by −2, so no handle can appear between connected slices. In 3+1 the condition is on the cobordism's own Euler characteristic, χ(K) = 0 for spacelike ends (Reinhart, Topology 2, 173 (1963); text unchecked); Gibbons–Hawking's spin condition comes on top of this.
- **Shadow:** each vertex region is micro (inside an ℓ-ball) or outside U; between vertices the members separate macroscopically, one through each slit (batch 31 §7, R4), so the shadow is a loop or a source→detector path.

## 2. Where the CTCs sit (argument, not theorem) [Geo, per #419 A4]

- Geroch 1967: a time-oriented compact Lorentzian cobordism with spacelike boundary between non-diffeomorphic slices contains a CTC *somewhere*.
- Applied to thin slabs around each vertex, and since a product region with a timelike field transverse to the slices needs no CTCs, this **suggests** that the CTCs can be confined to the vertex slabs. That is an argument, not the theorem. The slabs are still spatially global; spatial localisation needs a causally compact version (Borde, gr-qc/9406053, abstract read only).
- **Placement for S7 [CL]:** take the CTCs at v_a (and v_c). Call the chronology-violating set C_a ⊂ K₁₂.
- **Costs:** with the field equations and the WEC, Tipler 1977 says this cannot occur on Geroch's compact spacetime, and within a finite region it must be singular; Borde (dimensions ≥ 3, causally compact) says it cannot satisfy Einstein's equation with a reasonable source even at the price of singularities. So the matter model, or the absence of one (test-field geometry only), must be stated. The analytic lock's status for K₁₂ is unchecked.

## 3. The carried frame and the loop holonomy [CL]

- Each member carries a frame e (a clock hand): a unit vector, or a spinor in the spin-½ candidate (L161; MTW, Gravitation, §41.9, p. 1157, ToC checked; figure number unchecked), parallel-transported along its worldline. Spin-½ needs a spin structure as world data (A1: the choices form a torsor over H¹(M; ℤ₂)).
- **Closure loop γ:** creation at v_c → member 1's route → v_a → member 2's route reversed → v_c. Its holonomy Hol(γ) is gauge-invariant (batch 31 N5).
- What matters is the hand's turn round γ: mod 2π for a vector, mod 4π for spin-½. A "turn" is defined only if Hol(γ) is conjugate into a rotation subgroup SO(2) of SO⁺(1,3); a Levi-Civita holonomy round a loop in a curved Lorentzian M generically includes a boost, and then has no angle.

## 4. The question: does EKT-type self-consistency constrain Hol(γ)? [C021 S7, set up by CL]

- **EKT** (Echeverria–Klinkhammer–Thorne, Phys. Rev. D 44, 1077 (1991); abstract read by Literature, #421): a classical billiard ball entering a CTC region must have self-consistent motion; all "dangerous" initial trajectories in a wide class have infinitely many consistent solutions ("far too many solutions"), and in the standard account none was found to have zero (abstract-level; batch 23 Set 2).
- **Analogue:** a frame carried into C_a that meets its own future (via a CTC) must match itself: the transported frame e must equal its earlier self at the meeting point. That is a **fixed-point condition**: e must be fixed by Hol(c) for the CTC c through C_a (a vector needs eigenvalue 1 on a unit spacelike vector; a spinor needs eigenvalue 1 of the SL(2,ℂ) lift, which a lifted 2π rotation, −1, never has). Hol(c) is already fixed by the metric (#418 B3), so the condition constrains the frame's data, or excludes worlds whose Hol(c) has no admissible fixed point; it does not force Hol. For a passive parallel-transported frame there is no back-reaction, unlike EKT's colliding balls, so no multiplicity arises unless the frame couples to something. It also needs a member's worldline to traverse c; members end at v_a, so say how one enters C_a. It is not yet a condition on γ.
- **The link to γ:** homotopy is not enough. Under the lock M is curved, so freely homotopic loops generally have different holonomies (they differ by the curvature swept by the homotopy), and a shared deck element fixes only the linear (deck) part. The fixed-point condition restricts Hol(γ) only if the CTC is γ itself (up to reparametrisation), or if the holonomy of the region connecting them is known. (Two loops in a 4-manifold generically do not link, so "linking" is not available either.) Find out whether γ can itself be a CTC, or be connected to one with computable holonomy, for the S¹×S² pair.
- **Possible outcomes:**
  - (Y) Worlds whose Hol(γ) lies outside a subset (e.g. trivial mod 2π, or mod 4π, where an angle is defined) admit no self-consistent frame and so cannot cap off, and the subset depends on the members' routes. (Hol(γ) is world data, so this is exclusion of worlds, not dynamics forcing Hol.) Then "annihilate only if the phases line up" is derived. **Check against LT2:** the condition must be fixed before looking at fringes (batch 23 kill rule).
  - (N1) Self-consistency always has a solution, whatever Hol(γ) is (EKT found no zero-solution trajectory for balls, per the standard account; not an EKT quote). Then there is no constraint, and §7 is parked with Set 1.
  - (N2) The constraint exists but does not depend on the route (only on the vertex geometry). Then it is a filter, not a pattern, and is again parked.
- **Which-path:** a record on one member's route must lift the constraint (batch 23 kill rule). A passive record changes no geometry, so state what a record does here.
- **What is detected:** which object reaches d_i, and where each member's charge ends (#419 R4).

## 5. What must be specified before the question is well-posed [CL]

1. K₁₂ explicitly: a handle decomposition capping two S¹×S² summands, with a Lorentzian metric (or line field) and time orientation, so that Geroch applies.
2. C_a: the CTC set inside K₁₂, and its homotopy classes.
3. The spin structure (or vector frame) on M and its restriction to γ.
4. The matter model (test frame only, or one obeying an energy condition).
5. The routes: one member through each slit, and the slit geometry.

## 6. Ill-posed questions to avoid

- "When does the pair annihilate?" without a time function (with CTCs there is none globally).
- "The phase of one member": only Hol(γ) is gauge-invariant.
- "Does the frame match itself?" before C_a and its loops are specified.
- "The probability of capping": μ stays open, and no weights are used.

## 7. Prior art (bibliographic; abstracts read by Claude 021 and re-checked by Literature, #421, where noted; else unchecked)

Geroch, J. Math. Phys. 8, 782 (1967) (abstract read); Tipler, Ann. Phys. 108, 1 (1977) (abstract read); Borde, gr-qc/9406053 (abstract read); Gibbons–Hawking, Commun. Math. Phys. 148, 345 (1992) and Phys. Rev. Lett. 69, 1719 (1992) (abstracts read); Sorkin, Phys. Rev. D 33, 978 (1986) (abstract read); Reinhart, Topology 2, 173 (1963) (unchecked); Echeverria–Klinkhammer–Thorne, Phys. Rev. D 44, 1077 (1991) (abstract read, #421); Friedman–Morris–Novikov–Echeverria–Klinkhammer–Thorne–Yurtsever, "Cauchy problem in spacetimes with closed timelike curves", Phys. Rev. D 42, 1915 (1990) (Crossref metadata; text unchecked); Hadley, Class. Quantum Grav. 17, 4187 (2000) (abstract read); Dowker, gr-qc/0206020 (review). In-repo: batch 23 Sets 1–2, batch 24 (#408), batch 31 (#419).

## 8. Next step [CL]

On paper: construct K₁₂ (step 5.1) for the simplest pair cap, and find whether its CTCs can be homotopic to γ. Bring that to Geometry before any script (runs stay paused).
