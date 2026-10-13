# Batch 26: the low-energy approximation (LEA), stated precisely (Creative Lead; theory note; do not merge)

**Status.** Theory only, with no probability calculation. Classical; no Born rule; (M1) untouched at L3. Citations are unchecked unless they were verified earlier. Nothing goes into `versions/` or `papers/`. The LEA is defined here, not justified. Stacked on batch 25 (#409 at e6a4625). Ledger rows L108–L121.

**Program state.** Two-slit work is **paused**. Set 2 and Sets 3/5 are **on hold**, at the levels recorded in #408 and #407.

**David's direction (4:55 PM ET 2026-10-13, relayed by Physics Lead, Physics Lead chat, not signed). This is a PARAPHRASE by Physics Lead, not verbatim. Only the phrases in quotation marks are David's words, as relayed.**
- The target is generic: a particle is emitted from an arbitrarily small spacetime region (the emitter), and we want the relative probability of detection at detector d_i.
- First settle how d_i in world A is identified with d_i in world B.
- His intuition, from an old manuscript, is a "low (but not too low!) energy approximation". Spacetime looks nearly flat at human scale but stays "violently twisted, with nontrivial fundamental group, at the microscopic scale".
- Worlds A and B are each projected into one flat, simply connected spacetime. d_i in A and d_i in B count as the same if they map to the same spot, possibly with extra criteria such as matching microscopic topological structures.
- He does not want to go deep into justifying the LEA yet.

Prior art for the picture (bibliographic only, per Literature): Wheeler's foam, "Geons", Phys. Rev. 97 (1955) 511, and "On the nature of quantum geometrodynamics", Ann. Phys. 2 (1957) 604; Hawking, "Spacetime foam", NPB 144 (1978) 349. No prior coarse flat chart with a cross-world identification rule was found (Literature, #410).

---

## For David (plain summary)

- **What the projection is.** For each world, it is a "flattening map". It takes every point of a lab-sized region of that world to a point of ordinary flat spacetime. Two things are required:
  - distances agree with the flat ones up to a small relative error, at lab scales;
  - all the tiny twisted structure (little handles) gets squashed into a small blob.
- **Review round 018 (Claude review 018; applied by Lead ruling, Physics Lead).**
  - The smoothed-metric route to "flat at human scale" fails: a smoothed metric that keeps the tiny handles has strong curvature beside them (Cheeger–Gromov–Taylor). Flatness at lab scale is now stated with batch 27's distortion measure, and the old smoothed-flatness condition (C4) is replaced by it.
  - The lab region U is a ball and distances stay inside it.
  - The set of worlds now includes the lab bodies as labelled test bodies, replacing #399's tube-injection clause, which fails in foam.
  - The lab anchors are labelled, and the fit allows mirror images (O(3), not SO(3)).
  - The particle's length scale λ_E is a placeholder. We don't choose it; it is an open question for you.
  - A measure on worlds is kept separate from (M1).

  It is *not* the "unrolled" picture of the world (the universal cover). That would turn every tiny handle into infinitely many copies of each detector.
- **Fixing it.** Flat spacetime can be shifted, rotated and mirrored (boosts only approximately), so each world's map is only fixed up to such a move. We pin it to the lab: the emitter and the detectors as large objects, which every compatible world shares because they are part of what the observer knows. Pinning to the emitter alone is not enough, because a tiny error in direction there grows with distance.
- **Same detector in two worlds.** d_i in world A and d_i in world B are "the same" if their images land in the same place, to within a tolerance smaller than the gaps between detectors. Optionally, they must also have the same tiny structure, for example the same record written in it. If one world has two separate places that land on the same spot, the flattening is not legitimate there.
- **When it fails.** The approximation is ill-posed when:
  - the scales don't separate;
  - a twist is big rather than tiny (our two-slit toys were exactly this case);
  - there are time-travel regions inside the lab;
  - the emitter's surroundings differ between worlds.
- **The question, stated cleanly.** Among the worlds compatible with what the observer knows, consider those in which the particle sets off detector d_i. One question is the relative size of that set for each d_i, under some measure on worlds. That is a question about worlds, separate from (M1), which is a rule on arms in observer space; how the two relate is not settled here. *How* to measure the size of a set of worlds is left open on purpose: no probability rule is put in.

- **David's germ-order idea (5:00 PM).** Look at how many derivatives of the geometry matter at a given scale. At human scale only the flat part should matter; at the microscopic scale, ever-higher derivatives keep mattering.
  - Taken literally at one point, that runs into a snag: if the geometry twists at the tiny scale, its Taylor series at a lab point may stop converging at about that tiny distance, so it can't describe the lab. (That is a statement about convergence, not about flatness: far below the tiny scale the geometry is flat again.)
  - Using the *smoothed* geometry for "flat at human scale" does not work if smoothing keeps the tiny handles, because a tiny handle forces strong curvature right beside it. Batch 27's distortion measure says "flat at human scale" without derivatives; the raw geometry still describes "twisted at tiny scales".
  - Two limits: this picture is blind to twists that are perfectly flat (like a tiny wrapped-up direction; under the analytic lock that can only happen in a world that is flat everywhere), and the germ never fixes the global topology. Matching detectors uses only the lab window, so it fixes no global topology either.
  - **Three regimes (David, 5:03 PM).** Flat again far below the tiny scale (as any manifold is), twisted at the tiny scale, and flat at lab scales. Nothing is claimed about cosmic scales: the flat picture is needed only in a bounded window around the emitter and detectors, and everything used to match detectors lives inside that window.
  - The smoothed germ does not give a flat map when tiny handles are present. Matching detectors across worlds uses the lab-wide best fit and a comparison against one shared reference.

---

## (1) The projection: candidates and choice

**Scales.**
- ℓ: the microscopic topology scale (handle size, wrap length).
- L: the coarse-graining scale.
- R: the size of the lab region U (emitter plus detectors).
- 𝓡: the radius of curvature of the coarse geometry **on U only**, read off from the large-λ growth ε(p; λ) ≈ (λ/𝓡)² of batch 27's distortion (not from a smoothed ḡ_L, whose curvature the micro-handles keep large). No claim is made about curvature or flatness beyond U, at cosmic scales in particular (David, 5:03 PM).
- The LEA requires ℓ ≪ L ≪ R ≪ 𝓡.
- **"Not too low" energy** is recorded as a window, not justified. The particle's dynamical resolution scale λ_E satisfies ℓ ≲ λ_E ≪ L. λ_E is not yet defined: a free test particle follows a geodesic fixed by its launch event and direction at every energy, so λ_E needs a length in the classical particle model (its size, or the range of a self-field). Reading it as a de Broglie wavelength would put ħ in by hand. Until it is defined, condition 7 is a placeholder. "Low" makes the coarse, flat description apply to the apparatus. "Not too low" keeps the particle coupled to the microstructure, so the twisting can matter.

**Reference Riemannian metric.** Lorentzian distances are not a metric, so fix a unit timelike field u on U, the lab's rest frame, and set h = g + 2u♭⊗u♭. This is the standard Riemannian metric associated with a unit timelike field (signature −+++, g(u,u) = −1); it is not a Wick rotation, and it depends on the choice of u. Distances below are d_h, the length metric of (U, h): curves stay in U.

**Candidates.**
1. **Averaging (coarse-graining) map.** Average g over scale L to get ḡ_L (Isaacson 1968, Phys. Rev. 166, 1263 and 1272; Zalaletdinov 1992, GRG 24, 1015 and 1993, GRG 25, 673 [V-meta]).
   - It produces a *metric* on the same manifold, not a map of points.
   - It does not change the topology, so microscopic handles survive as topology.
   - It cannot by itself send d_i to a "spot".
   - Kept as an ingredient: it is how "nearly flat at scale L" is tested.
2. **Developing map from the universal cover.** dev: Ũ → ℝ^{1,3}.
   - It is exact only for flat (G, X)-structures, e.g. the flat cylinder, the flat Misner region, or flat exteriors of mouths.
   - The domain is the cover, so each detector has |π₁|-many lifts, infinitely many for a handle. Identification then needs a choice of lift, which is a section, and the microstructure is unrolled to macroscopic distances.
   - Rejected as the projection. Kept as the exact special case for flat hosts (§5).
3. **Coarse flat chart: chosen.** A map f: U → ℝ^{1,3} that is an **(ε, ℓ)-coarse isometry with causal compatibility**:
   - (C1) **Coarse isometry:** |‖f(p) − f(q)‖_E − d_h(p, q)| ≤ ε·d_h(p, q) + ℓ for all p, q ∈ U, where ‖·‖_E is the Euclidean norm in a fixed inertial frame of ℝ^{1,3} (that of the reference configuration, §2). A coarse map has no pushforward, so "the frame of f_*u" is not available. d_h depends on the choice of u; see §4 condition 9. (C1) implies the fibre bound in (C2) with C = 3/(1 − ε); only the density clause of (C2) is independent.
   - (C2) **Collapse:** each fibre f⁻¹(B_ℓ(x)) has d_h-diameter ≤ Cℓ, so microscopic topology is squashed into ℓ-blobs. Conversely, f(U) is ℓ-dense in a region of ℝ^{1,3} whose width is ~R in every direction (a thin slab would admit a lab crossed by a micro-wrap and lose the rigidity of §2).
   - (C3) **Causal compatibility (one-way):** for every future-directed causal curve γ in U of h-length ≥ L, f∘γ is εL-close (in C⁰, after smoothing at scale L) to a future-directed causal curve of η. This pushes causality forward only; f is non-injective and does not reflect causal relations. A closed causal curve passes only if its image has time-extent ≲ εL, so micro-CTCs are collapsed (their information survives only in (M-a)/(M-b)), and macroscopic CTCs violate (C3).
   - (C4) **Coarse flatness:** ε(p; λ) ≤ ε on the window (batch 27, regime 3). This is not a condition on a smoothed metric: a ḡ_L that keeps the micro-handles cannot be within ε of a flat metric, because a non-contractible loop of length ~ℓ in a region of Euclidean-order volume forces large curvature beside it (Cheeger–Gromov–Taylor 1982 injectivity-radius estimate; see option 4 in (b) below).

   This gives a **family** f_{ℓ,L,ε}, defined up to the ambiguity in (2). The choice is made because it is the only candidate that acts on *points* (needed for "same spot"), collapses the microscopic π₁ (the codomain is simply connected and the domain is the world itself, not its cover), and tolerates the additive microscopic error ℓ.

**Domain and codomain.**
- The domain is U ⊂ M_w, a lab-sized region of world w, not the whole spacetime.
- The codomain is a region of Minkowski space ℝ^{1,3}, which is flat and simply connected.
- So the LEA is local to the lab by construction.

## (2) Uniqueness and anchoring

- **Freedom.** If f satisfies (C1)–(C4), so does P∘f for every P in ISO(3) × time translations (7 parameters; boosts only up to O(ε), see below). In addition, any two admissible maps differ by a map within O(εR + ℓ) of some such motion. This is modelled on rigidity of approximate isometries between Euclidean spaces: Hyers–Ulam 1945 (Bull. AMS 51, 288) and Gruber 1978 (Trans. AMS 245, 263) [V-meta] treat additive error only, and the multiplicative ε·d_h term needs (1+ε)-bi-Lipschitz rigidity such as John 1961 (CPAM 14, 391) [V-meta]; see also Alestalo–Trotsenko–Väisälä, Israel J. Math. 125 (2001) 61 [V-meta]. Neither applies directly, since (U, d_h) is not a normed space, but the comparison of two admissible maps does not need that: f₂ composed with a selection of f₁⁻¹ is a (2εR + 2ℓ)-nearisometry between subsets of ℝ⁴, and by Alestalo–Trotsenko–Väisälä a bounded set has the isometric approximation property (error a constant times the nearisometry constant) iff it is thick (its narrowest projection is at least a fixed fraction of its diameter). So the bound below holds when f(U) fills a region of width ~R in every direction; for thin images only a square-root bound is available. Given h, the bounded-domain rigidity is essentially of this known type, and (C3) reduces E(4) to time-axis-preserving motions. With the fixed-frame norm of (C1), the exact freedom is ISO(3) × time translations, where ISO(3) = O(3) ⋉ ℝ³ includes spatial reflections (and time reversal too, unless (C3) is future-directed); boosts enter only at O(ε). What is not known is a coarse rigidity in terms of causal order alone: the exact results (Hawking–King–McCarthy 1976; Malament 1977; Zeeman 1964 [unchecked]) need bijections or homeomorphisms, and Zeeman's dilations show that causal order alone does not fix scale. So each world's f is fixed **modulo ISO(3) × time translations (boosts at O(ε)), up to a residual coarse error δ_f ~ εR + ℓ**.
- **Fixing across worlds** needs a cross-world gauge: a rule choosing P_w in each world.
- **Emitter anchoring** sets f_w(e) = 0 and maps an emitter frame to the standard frame. Two problems:
  - It needs the emitter's frame to be identified across worlds. Worse, E_w has h-diameter < ℓ, below the chart's additive resolution ℓ, so f_w(E_w) fixes translation to within ℓ and no frame at all. The emitter is "arbitrarily small", so its worldline gives a time direction but its spatial axes need apparatus orientation.
  - A frame error δθ at the emitter displaces images at distance R by δθ·R. Point anchoring amplifies errors with distance.
  - **Not enough on its own.**
- **Lab (observer) anchoring: chosen.** Choose P_w to minimise the misfit between f_w(lab bodies) and a fixed reference configuration in ℝ^{1,3}. The anchors are marked events a_k on the lab bodies, labelled in every world (the labels are world data, like #399's test bodies). The loss is Σ_k ‖P(f_w(a_k^w)) − a_k^ref‖²_E over P ∈ O(3) ⋉ ℝ³ × time translations; spatial reflections must be included, since (C1)–(C4) do not exclude them. The minimiser exists. For images whose errors are small against the anchors' smallest principal spread it is unique, and stable under those errors, iff the a_k^ref affinely span ℝ³ (at least 4 non-coplanar; over SO(3) alone 3 non-collinear anchors would do, but a mirrored f_w would not be aligned), and any one event fixes the time translation. Without labels, the correspondence and the fit are found together, and the result is unique only if the reference configuration has no symmetry: a mirror-symmetric lab gives two equally good fits that swap d₁ and d₂. The lab bodies are the emitter, the detector array and the walls, taken as macroscopic bodies at scale ≥ L. Least squares over several anchors removes the lever-arm amplification.
  - The reference configuration is shared across compatible worlds, because the observer's record (#399) fixes the macroscopic lab arrangement.
  - Result: P_w is fixed up to δ_P = O((εR + ℓ)·R/w), with w the anchors' second principal spread; R/w = O(1) for anchors spread across the lab. The chart errors are systematic and bounded, not independent, so there is no 1/√(number of anchors) gain in the worst case.
- **Circularity check.** Anchoring on the detectors makes their images coincide across worlds almost by construction. That is intended. The question is not *where* d_i is, but whether the particle's worldline enters it. The identification is nontrivial only for what lies *between* the anchors (paths, microstructure) and for the detectors' microscopic content (§3).

## (3) Identifying d_i across worlds

- **Base criterion.** d_i^w belongs to [d_i] iff d_H(f_w(D_i^w), D_i^ref) ≤ τ/2, where D_i^ref is detector i in the shared reference configuration (§2). Comparing to the reference makes the relation transitive; a pairwise rule d_H(f_A(D_i^A), f_B(D_i^B)) ≤ τ is not transitive under chaining and does not define classes. Here d_H is the Hausdorff distance in ℝ^{1,3}, using the Euclidean norm in the lab frame, over the detector's spacetime region D_i. The tolerance must satisfy εR + ℓ + δ_P ≲ τ ≪ Δ, with Δ the minimum separation between detectors.
- **Optional microstructure criteria** (each is a well-defined refinement, to be chosen by the program and not by the LEA):
  - (M-a) The same microscopic topology in the ℓ-neighbourhood of D_i: same handle count and homotopy classes, or same holonomy classes.
  - (M-b) The same ledger content: the same persistent entries in the detector's diary (#399) up to the emission event. Later entries include the outcome, so using them would split [d_i] by whether d_i fired; "d_i fired" becomes a record identity through the detection rule of §6, not through this refinement.
  - (M-c) The same coarse matter content at scale L.

  Refinements split classes, never merge them.
- **Two patches in one world mapping to the same spot.** Suppose f_w⁻¹(B_τ(x)) contains two components P₁, P₂ of D-type.
  - If d_h(P₁, P₂) ≤ Cℓ (microscopically separated), they are **one** coarse detector, consistent with (C2).
  - If both images lie in B_τ(x), (C1) still allows d_h(P₁, P₂) up to (2τ + ℓ)/(1 − ε). Separations between Cℓ and about 2τ are one coarse detector at resolution τ, which is harmless since τ ≪ Δ. Only d_h(P₁, P₂) ≫ τ with coincident images violates (C1), so f_w is **not admissible** there.

  This is the case of a macroscopic handle or wrap. In that region the LEA is not merely ambiguous: it is **ill-posed**. Treating P₁ and P₂ as distinct "sheets" with a multivalued identification is rejected, unless a microstructure criterion separates them. Even then it is outside the LEA proper.

## (4) Well-posedness audit (David's principle)

**Terms defined.**
- ℓ, L, R, 𝓡, ε, τ, Δ (§1, §3);
- U, u, h (§1);
- the averaging convention for ḡ_L (§1; non-unique, see the next list);
- f and (C1)–(C4) (§1);
- P_w and the reference configuration (§2);
- the base and optional identification criteria (§3);
- "detection at d_i" (§6).

**Ill-posed when any of these holds:**
1. **No scale separation** (ℓ ≪ L ≪ R ≪ 𝓡 fails). For example, curvature at lab scale, or microstructure at scale L.
2. **Macroscopic nontrivial topology in U** (a handle or wrap of size > Cℓ). Then (C1)/(C2) fail.
3. **Macroscopic chronology violation, or no time orientation, in U.** A unit timelike u exists on any time-orientable U, CTCs or not, so u is not the obstruction. The condition is closed causal curves in U whose images would have time-extent > εL (then (C3) fails), or U not time-orientable.
4. **Averaging-convention dependence above τ.** Covariant averaging is non-unique (the fitting/averaging problem: Ellis 1984; Ellis–Stoeger 1987, CQG 4, 1697; Zalaletdinov 1992; Buchert 2000, GRG 32, 105 [V-meta]). The LEA is well-posed only if admissible f exist for every reasonable convention and the identifications agree within τ.
5. **Anchors not shared.** The compatible worlds disagree on the macroscopic lab configuration, or on the emitter's neighbourhood at scale L.
6. **Detectors near ∂U, or detectors closer than τ**, so that Δ ≲ τ.
7. **The energy window fails.** λ_E ≲ ℓ, so the particle resolves the microstructure directly; or λ_E ≳ L, so it does not couple to it. In the first case the projection is irrelevant to the particle; in the second the twisting cannot matter. Neither is ill-posed for the identification, but the LEA's *purpose* fails.
8. **Anchor degeneracy:** the lab anchors do not affinely span space, or none has temporal extent (§2), so the best fit is not unique.
9. **Frame dependence:** the identification classes change by more than τ under admissible changes of u (d_h depends on u).
10. **Existence:** conditions 1–6 do not by themselves guarantee that an admissible f exists. This is an open existence question, not assumed.

## (5) Compatibility and tensions

- **Analytic lock.** No tension in the definitions: f is a description of a world, not part of its dynamics, and need not be analytic. Unique continuation still applies to each world. The lock fixes the metric germ, not the topology: analytic extensions of one germ need not be unique (Misner, Taub–NUT; #371), and compatible worlds differ only globally. So (M-a) is not decidable from data near a point; under the lock it is exactly the global datum that can distinguish worlds (see Germ and global data below).
- **Microscopic handles** (batches 14–16, the #399 diary): compatible when the handle size is < ℓ. They are then collapsed by (C2) and survive only in (M-a)/(M-b). This is the setting David describes.
- **Flat cylinder and the two-slit toys** (#401–#409): **tension.** There the wrap length (called L in #401, not the coarse-graining scale L here) was at slit or route scale, i.e. macroscopic. Under the LEA that is condition 2: the toys are *outside* the LEA. The two-slit program put the topology at the scale of the routes; David's LEA puts it at the microscopic scale. With this toy, the pause is consistent.
- **Misner, Taub–NUT and offset-mouth CTC hosts** (#385, #398, #408): condition 3 fails wherever the CTC region meets U. The LEA applies only to regions U that exclude chronology-violating sets, or where the CTC structure is microscopic and collapsed. Whether a microscopic CTC can be collapsed consistently with (C3) is **open**.
- **The flat (G, X) special case.** For exactly flat hosts the developing map exists. Composing it with a section at scale ℓ gives an admissible f when the wraps are < ℓ. That is a consistency check between candidates 2 and 3.
- **#399's 'world'**, a full spacetime with its matter and records: compatible. The LEA uses only U ⊂ M_w and the shared record (for anchoring).
  - It **helps** with #399's uncountability: the detection events partition the worlds into finitely many classes [d_i].
  - It does **not** supply a measure on worlds. That stays open, and (M1) is untouched.


## Germ and global data (analytic lock)

- **(a) Germ.** The germ of world w at a point p is the equivalence class of (M_w, g_w) on neighbourhoods of p, where two are equivalent if they agree on some neighbourhood. Under the analytic lock, g_w is real-analytic.
- **(b) What the lock gives.** Along any curve from p, the analytic continuation of the metric is unique as long as it exists. So the germ fixes the metric locally, and fixes it along each continuation path.
- **(c) What it does not give.** Analytic extensions are not unique as manifolds. Misner/Taub–NUT have inequivalent analytic extensions (#371, per Literature), and continuation along homotopically different paths need not close up into one manifold. So **the germ fixes the local metric, while π₁ and the micro-handles are global extension data that can differ between worlds with the same germ.**

Consequences for the LEA:
- Two worlds can agree near the emitter, and so share the anchor (§2), while differing in their microstructure elsewhere in U. This is exactly the case in which the optional criteria (M-a)/(M-b) matter.
- (M-a) must be evaluated on each world's global data in U, not inferred from a germ.


## Germ-order formulation (David, 5:00 PM)

**David, 5:00 PM ET 2026-10-13, relayed by Physics Lead, Physics Lead chat, not signed (verbatim):**
> One idea I have for formulating the LEA in a mathematically rigorous manner is in terms of the order k of the derivatives of the germ. We might say that flat at human scale means that k should be uniformly 0 (or below some very low number) within some interval that defines that scale; but violently twisted microscopically would be equivalent to k not being uniformly low within some other interval of k that corresponds to the microscopic scale.

**Physics Lead's reading** (a Lead reading, not David's):
- The order-k term contributes ~|a_k| ℓ^k at scale ℓ.
- Human-scale flatness means terms of order ≥ 2 are negligible at ℓ_H.
- Microscopic twisting means a_k grows ~ℓ_P^{−k}, with radius of convergence near ℓ_P. *(Qualified by the 5:03 PM Lead notes: a radius of convergence near ℓ_P does not by itself mean non-flatness below ℓ_P; see (a′).)*
- Caveat: π₁ is global, and the germ reaches it only through analytic continuation under the lock.

### (a) Definition

- **Coefficients.**
  - Fix an anchor p, the lab field u, and an h-orthonormal frame at p.
  - In Riemann normal coordinates, g_ab(x) = η_ab − ⅓R_acbd x^c x^d − ⅙∇_e R_acbd x^c x^d x^e + …
  - The order-k coefficient a_k(p) (k ≥ 2) is a universal polynomial in ∇^j R, j ≤ k − 2, including products of lower orders (normal-coordinate expansion: Manasse & Misner, J. Math. Phys. 4 (1963) 735 [V-meta, per Literature]; jets in the sense of Ehresmann [unverified]).
  - Its size is |a_k|, the h-norm of the coefficient tensor. a_0 = η and a_1 = 0, so "order 0 or 1" means flat.
- **Scale profile.** c_k(p; λ) = |a_k(p)| λ^k, which is dimensionless.
- **Effective order at scale λ.** K(p; λ) = max{k : c_k(p; λ) > ε}.
- **Curvature length of order k.** λ_k(p) = |a_k(p)|^{−1/k}. For k = 2 this is of the order of the curvature length from the Kretschmann scalar 𝒦 = R_abcd R^abcd (Kretschmann 1918), namely |𝒦|^{−1/4} (Literature correction), in Riemannian signature; in Lorentzian signature |𝒦|^{1/2} is at most a constant times |a_2|_h, so |𝒦|^{−1/4} is only an upper bound on λ_2 up to a constant (it is infinite for VSI metrics).
- **Closest prior art** (bibliographic only, per Literature): the Cartan–Karlhede algorithm (Karlhede, GRG 12 (1980) 693; Cartan 1928) classifies metrics locally by ∇^j R up to a finite order. It decides *equivalence*; c_k here measures *size at a scale*. The finite-order bound is not checked here.
- **Radius of convergence.** ρ(p) = 1/limsup |a_k|^{1/k} (Cauchy–Hadamard).

**Readings of "k uniformly low within an interval".** The text admits three:
- **(R1) Scale interval, effective order.** On I_H = [ℓ₁, ℓ₂] (human scale), K(p; λ) ≤ k₀ for all λ ∈ I_H and all p ∈ U, with k₀ = 1 (or "very low"). Microscopic twisting: K(p; λ) is large or unbounded for λ in a micro interval I_μ.
- **(R2) Tail norm.** Σ_{k > k₀} c_k(p; λ) ≤ ε on I_H, and the tail is ≥ 1 on I_μ.
- **(R3) An interval of k, as David's last clause suggests** ("some other interval of k that corresponds to the microscopic scale"). Orders map to scales via λ_k. Flat at human scale: λ_k ≥ ℓ_H for k ∈ [2, k_H]. Twisted: λ_k ≲ ℓ_μ for k in a high-order interval [k₁, k₂].

**Ambiguity flag.** R1 and R2 index the interval by *scale*; R3 indexes it by *order*. David's sentence uses both ("an interval that defines that scale"; "an interval of k"). They agree only if λ_k is monotone in k, which is not guaranteed. The program should choose. This note uses R1 for statements and R3 for intuition.


### (a′) Three regimes (David, 5:03 PM)

**David, 5:03 PM ET 2026-10-13, relayed by Physics Lead, Physics Lead chat, not signed (verbatim):**
> when we get smaller than microscopic, it needs to get flat again, because that's one of the defining features of a manifold... at the cosmic scale, we don't know whether it's flat or not, so we should be careful not to assert that it must necessarily be flat.

**Lead notes** (Physics Lead; not David's):
- The LEA has three regimes: locally flat for ℓ ≪ ℓ_P (the manifold property, since (ℓ/ℓ_P)^k → 0), twisted near ℓ_P, and flat across a bounded human-scale window [ℓ_low, ℓ_high].
- The radius of convergence near ℓ_P is not the same thing as non-flatness below ℓ_P, so the regimes should be stated in terms of the curvature scale.
- No claim about cosmic scales. The flat projection is needed only over a bounded window containing the emitter and detectors.

**Restatement in curvature-scale language.** Let ℓ_curv(p) = inf_{k ≥ 2} λ_k(p) be the curvature length of g at p (ℓ_curv ≤ ρ, and > 0 by analyticity), with ℓ_curv ~ ℓ_P in the foam picture. Below, λ denotes the running scale; ℓ stays the micro-topology constant of (C1).
1. **Locally flat, λ ≤ √ε·ℓ_curv.** c_k(p; λ) ≤ (λ/ℓ_curv)^k ≤ ε for every k ≥ 2, so g is η plus corrections of size ≤ ε on λ-balls. This is the manifold property (the tangent-space limit). It holds at every point, curved or not, and it is *not* "exactly flat on an open set", which the lock would forbid (identity theorem, (b)).
2. **Twisted, ℓ ~ ℓ_curv ~ ℓ_P.** c_k(p; ℓ) = O(1) for many k: R1/R3 for g on I_μ ∋ ℓ_P.
3. **Flat on a bounded window, λ ∈ [ℓ_low, ℓ_high] = I_H** (with L ≤ ℓ_low, since ḡ_L carries no information below L, and ℓ_high ≤ min(R, √ε·𝓡)). ε(p; λ) ≤ ε on I_H only (batch 27); R1 for a smoothed ḡ_L that keeps the micro-handles cannot hold (option 4 of (b)). Nothing is asserted for λ > ℓ_high.

**Radius of convergence vs flatness.** ρ ~ ℓ_P is compatible with regime 1. For ℓ ≪ ρ the series converges and its terms go to zero, which *is* local flatness. ρ only says where the series stops converging, not where the geometry stops being flat. The earlier wording that tied ρ ~ ℓ_P to twisting is corrected accordingly: twisting is c_k = O(1) at ℓ ~ ℓ_curv, not ρ ~ ℓ_P alone.

### (b′) Window check for the identification of d_i

Window W = U, a bounded region containing the emitter, the detectors and the anchors, of size R, at scales up to ℓ_high.

| ingredient | defined within the window? |
|---|---|
| projection f_w and (C1)–(C4) | yes: defined on U; ḡ_L needs a margin of width L around U |
| u, h | yes: the lab field on U |
| Procrustes anchors | yes: lab bodies in U |
| reference configuration | yes: a fixed configuration of lab bodies in ℝ^{1,3} (an abstract copy, not a region of the world) |
| tolerance τ, Δ, ε, ℓ, L | yes: numbers fixed by the lab |
| exponential chart of ḡ_L | only as the nearest-preimage selection: smoothing keeps the micro-handles as topology, so the injectivity radius of ḡ_L is ~ℓ, not ≥ R; exp_o is not injective on U, and the least-h-norm preimage has O(ℓ) jumps, which (C1) absorbs |
| (M-b) ledger criterion | yes: diary entries in the detector body |
| (M-c) coarse matter | yes |
| **(M-a) microtopology** | **reaches outside if stated as "same π₁".** π₁(M_w) is global. Localise it as S_B(Λ): the free homotopy classes of U that have a representative of h-length ≤ Λ inside B, an h-ball about D_i of radius ≥ Cℓ within U (with holonomy along those representatives, (c)). Free classes have no location, so "near" means "has a short representative in B". Across worlds, compare an invariant (the length spectrum of S_B(Λ) to within a micro tolerance δ_μ ≪ ℓ, since all spectra of loops of length ≤ Λ ~ ℓ agree to within τ ≫ ℓ, or the conjugacy class of the image of π₁(B) → π₁(U) up to isomorphism, with holonomies), not "the same classes": different worlds' π₁ are different groups. Loops that leave U are not used. |
| **"compatible with the record" (#399)** | the record may refer to the world outside U. For the identification only its lab part (the macroscopic lab configuration) is used; the rest enters W, not the identification. |

**Conclusion.** With (M-a) localised to loops in U, the identification of d_i needs nothing beyond the bounded window, so no cosmic-scale assumption is required. The localised (M-a) is weaker than "same π₁": π₁(B) → π₁(M_w) need be neither injective nor surjective, so worlds that agree on U can differ in global topology. Agreement in the window fixes no global topology, and none is picked.

### (b) The convergence tension

If |a_k| ~ ℓ_P^{−k} (Lead reading), then ρ ~ ℓ_P, and at λ = ℓ_H ≫ ρ the terms c_k = (ℓ_H/ℓ_P)^k grow without bound. **The series of the germ of g at a lab point diverges at human scale**, so R1–R3 cannot all be stated for the germ of g. (This is about convergence only. For λ ≪ ρ the same series converges with vanishing terms, so it is locally flat; see (a′).) Under the lock, ρ(p) is set by the distance to the nearest complex singularity of the continuation (equal to it in one variable), presumably the nearest microstructure, so with dense foam ρ ~ ℓ_P everywhere [A, heuristic].

**Options.**
1. **Asymptotic or truncated use** of the germ of g: valid only for λ ≪ ρ ~ ℓ_P. "Flat at human scale" is then inexpressible, so this fails.
2. **Two-regime profile:** small low orders and large high orders. The tail still dominates at ℓ_H, so it fails pointwise for the same reason.
3. **Exactly flat between handles:** impossible under the lock. An analytic metric that is flat on an open set is flat on the whole connected manifold (identity theorem), so curved micro-handles make the germ non-flat at every point.
4. **Smoothing: proposed, but it fails for the macro statement.** Use the germ of the coarse-grained metric ḡ_L (§1) for the macro statement, and the germ of g for the micro statement. A ḡ_L that keeps the micro-handles (§1, (b′), (d)) cannot satisfy R1 on I_H: if |Riem| ≲ ε/ℓ_low² on a ball of radius ℓ_low with Euclidean-order volume, the injectivity radius at its centre is at least a fixed fraction of ℓ_low (Cheeger–Gromov–Taylor, JDG 17 (1982) 15; local form in Chen–LeFloch, arXiv:0812.2671, Thm 2.1), so no non-contractible loop of length ~ℓ ≪ ℓ_low passes through it. Smoothing must remove the handles (another manifold) or leave curvature far above ε/ℓ_low² beside them. The macro statement is therefore made with batch 27's distortion ε(p; λ); the germ of g keeps the micro statement:
   - **flat at human scale:** ε(p; λ) ≤ ε on I_H (batch 27), not R1 for ḡ_L;
   - **violently twisted:** R1 or R3 for g on I_μ around ℓ_curv ~ ℓ_P (c_k = O(1) there); for λ ≪ ℓ_curv, g is locally flat again (regime 1, (a′)).

   Smoothing prior art (bibliographic only): Korzyński, CQG 27 (2010) 105015; Buchert, GRG 32 (2000) 105. Hamilton's Ricci flow (JDG 17 (1982)) is Riemannian and can change topology (through surgery), so it is not a ready-made ḡ_L.
   This is consistent with the lock, which constrains g, the world. ḡ_L is a derived description; it need not be analytic (whether a given smoothing yields an analytic ḡ_L is [unchecked]); R1 on I_H is therefore read through the finite-order Taylor expansion of ḡ_L with remainder (k ≤ k_H), not through a convergent series. It also matches (C4).

### (c) What the germ-order picture can and cannot detect

This is consistent with "Germ and global data" (Literature M3): the germ fixes the local metric, not the topology.

**Can detect:**
- curvature microstructure, through a_k for g;
- under the lock, the holonomy along a *given* loop, when analytic continuation of the germ (and of a frame) along it exists. The monodromy of the frame is the Levi-Civita holonomy.

**Cannot detect:**
- π₁ itself;
- which analytic extension is realised (Misner, Taub–NUT, #371);
- **flat micro-topology.** A flat wrap or flat handle has a_k = 0 for all k ≥ 2 at every point, the same germ as Minkowski space. Under the lock this can occur only in an exactly (locally) flat host: an analytic metric flat on an open set is flat on its whole connected component, so in a world with any curvature every micro-handle is curved and is seen by a_k. With the lab as test fields (test-field limit), flat hosts are allowed; beyond that limit the blindness case is excluded. So "k uniformly 0" can hold at *every* scale in a world that is "violently twisted, with nontrivial fundamental group". The germ-order criterion for twisting captures curvature twisting only; flat topology needs the global data (M-a). Outside the lock (smooth metrics) the jet does not fix the germ: smooth germs can agree to all orders and differ (flat functions such as e^{−1/x²}), so a_k-statements constrain g only through finite-order Taylor remainders. Under the lock (analytic), the ∞-jet determines the germ.

### (d) Does it fix the flat projection?

- **Exponential chart.** f_o = exp_{ḡ_L, o}^{−1}, in an h-orthonormal frame at the anchor o, with the germ truncated at k ≤ 1. This gives a flat chart on the normal neighbourhood of o for ḡ_L.
  - (C1) does not follow. "ε ~ R²/𝓡² from a_2 of ḡ_L" needs |Riem(ḡ_L)| ~ 1/𝓡², which the micro-handles rule out (option 4 of (b)). The least-h-norm preimage of exp_o⁻¹ is not O(ℓ)-close either: if a micro-handle near o has a gluing that turns by an angle θ (#399), the shortest routes to a cone of lab points run through it, and those points land O(θR) away [heuristic]. The injectivity radius of ḡ_L itself is ~ℓ, because the micro-handles survive smoothing as topology. Using g instead fails, because its injectivity radius and ρ are ~ℓ_P (g is locally flat only far below ℓ_P, not at lab scale).
  - **Residual freedom:** the frame at o, i.e. a Lorentz transformation (6 parameters, reduced to SO(3) by u; translations are fixed by o).
  - The translation is fixed by o, but o is defined only to ℓ within its anchor body.
- **Comparison with the best-fit (Procrustes) projection** (§2, F5):

  | | anchors needed | residual freedom | error growth |
  |---|---|---|---|
  | exponential chart | 1, plus a frame | that frame | frame error × R |
  | Procrustes | ≥ 4 non-coplanar, one with temporal extent | none beyond O(εR + ℓ) | none |

  The two agree to O(R²/𝓡² + εR + ℓ) once the exponential chart's frame is taken from the Procrustes fit.
- **Verdict:** with micro-handles present, the exponential chart of ḡ_L is not an admissible member (first bullet), so the germ-order picture gives no canonical chart. The frame-fixing rule stays the Procrustes fit of §2.

### (e) Does it fix the identification of d_i?

- **Truncated jets at a shared anchor.** At the anchors, the jets j^{k_H} of ḡ_L agree with flat to within ε in every compatible world. That says the worlds are all nearly flat. **It does not identify d_i.** Identification still goes through the images of D_i in the charts, compared to the shared reference (§3, F7): reference, not pairwise.
- **Is the shared anchor well-defined?** Only coarsely. The anchor is a lab body in the record, so its location in each world is defined to ℓ and its frame to the apparatus orientation. A "point o" with a micro-jet is not shared across worlds.
- **Micro-jets as a refinement criterion** (the jets of g at the anchor):
  - Pairwise comparison within a tolerance is not transitive.
  - There is no natural reference micro-jet to compare to (the flat one is the macro reference).
  - Exact equality is transitive, but under the lock equal germs mean identical local metrics, and micro-jets vary over the ℓ-ball anyway.
  - So micro-jets can serve only as a **scale-averaged** criterion, e.g. the profile λ_k(·) over the ℓ-ball (h-volume average, u fixed) compared to a reference profile. They are not a pointwise one. The criterion is u-dependent, and replacing the h-norms by Lorentzian scalar invariants is unsafe, because VSI spacetimes (e.g. pp-waves) are curved with all invariants zero [unchecked].

### (f) Well-posedness audit (new terms)

- **Defined:** a_k, c_k, K, λ_k and ρ (frame-dependent through u; fix u. h-norms are u-dependent, and Lorentzian scalar invariants are unsafe: VSI spacetimes such as pp-waves are curved with all invariants zero [unchecked]); I_H, I_μ, k₀, ε; the germ of g and of ḡ_L.
- **Ill-posed when:**
  1. it is applied to the germ of g at human scale (divergence, (b));
  2. **flat micro-topology** is present: invisible to the criterion, (c), so the twisting has to be stated via (M-a);
  3. the dependence on the averaging convention exceeds the tolerance (inherits §4 condition 4);
  4. a_k depends on the frame (u) above the tolerance (inherits §4 condition 9);
  5. a micro-criterion at "the anchor point" is used (o is defined only to ℓ, (e)), instead of a scale-averaged one;
  6. the reading is not fixed: R1/R2 versus R3, (a).

## (6) The emitter–detector question, stated

**Data.**
- Scales ℓ ≪ L ≪ R ≪ 𝓡, a tolerance τ, and an energy window ℓ ≲ λ_E ≪ L.
- A set W of worlds: #399's worlds with the emitter, the particle, the detectors and the walls added as labelled test bodies (#399 §5 (iii), as batch 20 did for its source and screen). "Compatible with the observer's prior record Rec₀" (renamed: 𝓡 is already used in §1) must be defined; at least, the lab bodies' images match the reference configuration within τ/2 and the diaries hold Rec₀. #399's tube-injection clause cannot be kept as is: in micro-foam a micro-handle's deck element moves nearby worldline points by O(ℓ), so no tube wider than about ℓ injects; replace it (for example by injection at scales ≥ L) or say why it stays. State which data may differ between worlds in W (gluings of micro-handles in U, extensions, the particle's launch data below resolution ℓ) and which Rec₀ fixes.
- Each w ∈ W contains:
  - (i) an emitter region E_w of h-diameter < ℓ, with an emission event that starts one test particle with a single classical worldline γ_w, with no superposition;
  - (ii) detector bodies D_1^w, …, D_n^w;
  - (iii) a lab region U_w ⊃ E_w ∪ ⋃ D_i^w for which none of §4's ill-posedness conditions 1–6, 8 and 9 holds.
- Each w has an admissible projection f_w, lab-anchored (§2). For this question, admissible means (C1) in batch 27's additive form (|‖f(p) − f(q)‖_E − d_h(p, q)| ≤ εR on U), the density clause of (C2), and (C3); the multiplicative (C1) is not needed for the W_i. Existence then follows from batch 27's regime 3, since ε(p₀; R) is an infimum over such maps; only (C3) is extra.

**Definitions.**
- **Detection at d_i in w:** γ_w enters D_i^w before entering any other D_j^w. Under (M-b), detection may instead be defined as the first new persistent entry being in d_i's diary; the two definitions agree only if every entry into a detector writes a persistent entry and nothing else writes one, which #390's grades do not guarantee.
- **Classes:** [d_i] is the equivalence class across W under the base criterion of §3, plus whichever (M-·) refinements are adopted. W_i = {w ∈ W : detection at a member of [d_i] in w}.
- **Admissibility of the classes:** the W_i are pairwise disjoint because detection is "first entry". Together with W_∅ (no detection), they cover W.

**Question.** For a measure μ on W, specified independently of the LEA, find the ratios μ(W_i)/μ(W_j).
- The LEA makes the *events* W_i well-defined and comparable across worlds. It says nothing about μ. A measure on worlds is not (M1), which stays the ruled per-vertex rule (L3); the ratio is posed as a question about worlds, and a μ that counts worlds falls under the ledger's standing rule on counting.
- The question is well-posed iff (a) none of §4's conditions 1–6, 8 and 9 holds for any w ∈ W, and each w has an admissible f_w (condition 10), (b) the identification classes are independent of the admissible choices within τ, and (c) μ is a measure on a σ-algebra of W containing every W_i, with 0 < μ(W_j) < ∞ for each W_j in a ratio.
- Item (c) is the open problem. No probability is computed here, and no rule is assumed.

---

## Open items

0. Which global extension data (π₁, micro-handles) are admissible for a given germ: a classification, open.
1. Coarse rigidity in terms of causal order alone (the Riemannian rigidity via h is essentially known; see §2). Exact causal rigidity (Hawking–King–McCarthy, Malament, Zeeman) needs bijections, and no coarse or non-injective analogue is known. Lorentzian-intrinsic alternatives to the h-trick (options, not adopted; bibliographic only, per Literature/Geometry): Noldus, CQG 21 (2004) 839; Bombelli–Noldus, CQG 21 (2004) 4429; Sormani–Vega, CQG 33 (2016) 085001 (null distance, needs only a time function); Kunzinger–Sämann, Ann. Glob. Anal. Geom. 54 (2018) 399; Minguzzi–Suhr, Lett. Math. Phys. 114 (2024) [V-meta]; finitary topology: Sorkin, IJTP 30 (1991) 923.
2. The choice of averaging convention, and a test of condition 4 on a host.
3. Microscopic CTCs: collapse is consistent with the one-way (C3) by construction (§1), at the price that the chart keeps no CTC information. Open: whether (M-a)/(M-b) can carry it consistently across worlds.
4. Which microstructure criterion (M-a/b/c) the program adopts. (M-b) ties the LEA to the ledger.
5. The measure μ on W, which is outside the LEA.
6. Whether more than one W_i is non-empty. With the launch fixed by the record, worlds differ only in micro-handle gluings in U, extensions and launch data below ℓ; no mechanism yet takes these to detectors Δ ≫ τ apart. A structure-only computation (no μ) on a test host is the next step.

Ledger: L108–L121 (L108 records the paraphrase of David's 4:55 PM direction; L115 records David's 5:00 PM words verbatim; L119 records his 5:03 PM words verbatim).
