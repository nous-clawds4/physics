# Batch 26: the low-energy approximation (LEA), stated precisely (Creative Lead; theory note; do not merge)

**Status.** Theory only, with no probability calculation. Classical; no Born rule; (M1) untouched at L3. Citations are unchecked unless they were verified earlier. Nothing goes into `versions/` or `papers/`. The LEA is defined here, not justified. Stacked on batch 25 (#409 at e6a4625). Ledger rows L108–L114.

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

  It is *not* the "unrolled" picture of the world (the universal cover). That would turn every tiny handle into infinitely many copies of each detector.
- **Fixing it.** Flat spacetime can be shifted and rotated (boosts only approximately), so each world's map is only fixed up to such a move. We pin it to the lab: the emitter and the detectors as large objects, which every compatible world shares because they are part of what the observer knows. Pinning to the emitter alone is not enough, because a tiny error in direction there grows with distance.
- **Same detector in two worlds.** d_i in world A and d_i in world B are "the same" if their images land in the same place, to within a tolerance smaller than the gaps between detectors. Optionally, they must also have the same tiny structure, for example the same record written in it. If one world has two separate places that land on the same spot, the flattening is not legitimate there.
- **When it fails.** The approximation is ill-posed when:
  - the scales don't separate;
  - a twist is big rather than tiny (our two-slit toys were exactly this case);
  - there are time-travel regions inside the lab;
  - the emitter's surroundings differ between worlds.
- **The question, stated cleanly.** Among the worlds compatible with what the observer knows, consider those in which the particle sets off detector d_i. We want the relative size of that set for each d_i. *How* to measure the size of a set of worlds is left open on purpose: no probability rule is put in.

---

## (1) The projection: candidates and choice

**Scales.**
- ℓ: the microscopic topology scale (handle size, wrap length).
- L: the coarse-graining scale.
- R: the size of the lab region U (emitter plus detectors).
- 𝓡: the radius of curvature of the coarse-grained geometry.
- The LEA requires ℓ ≪ L ≪ R ≪ 𝓡.
- **"Not too low" energy** is recorded as a window, not justified. The particle's dynamical resolution scale λ_E satisfies ℓ ≲ λ_E ≪ L. "Low" makes the coarse, flat description apply to the apparatus. "Not too low" keeps the particle coupled to the microstructure, so the twisting can matter.

**Reference Riemannian metric.** Lorentzian distances are not a metric, so fix a unit timelike field u on U, the lab's rest frame, and set h = g + 2u♭⊗u♭. This is the standard Riemannian metric associated with a unit timelike field (signature −+++, g(u,u) = −1); it is not a Wick rotation, and it depends on the choice of u. Distances below are d_h.

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
   - (C2) **Collapse:** each fibre f⁻¹(B_ℓ(x)) has d_h-diameter ≤ Cℓ, so microscopic topology is squashed into ℓ-blobs. Conversely, f(U) is ℓ-dense in a region of ℝ^{1,3}.
   - (C3) **Causal compatibility (one-way):** for every causal curve γ in U of h-length ≥ L, f∘γ is εL-close (in C⁰, after smoothing at scale L) to a causal curve of η. This pushes causality forward only; f is non-injective and does not reflect causal relations. A closed causal curve passes only if its image has time-extent ≲ εL, so micro-CTCs are collapsed (their information survives only in (M-a)/(M-b)), and macroscopic CTCs violate (C3).
   - (C4) **Coarse flatness:** on U, ḡ_L is within ε of a flat metric in C⁰.

   This gives a **family** f_{ℓ,L,ε}, defined up to the ambiguity in (2). The choice is made because it is the only candidate that acts on *points* (needed for "same spot"), collapses the microscopic π₁ (the codomain is simply connected and the domain is the world itself, not its cover), and tolerates the additive microscopic error ℓ.

**Domain and codomain.**
- The domain is U ⊂ M_w, a lab-sized region of world w, not the whole spacetime.
- The codomain is a region of Minkowski space ℝ^{1,3}, which is flat and simply connected.
- So the LEA is local to the lab by construction.

## (2) Uniqueness and anchoring

- **Freedom.** If f satisfies (C1)–(C4), so does P∘f for every P in ISO(3) × time translations (7 parameters; boosts only up to O(ε), see below). In addition, any two admissible maps differ by a map within O(εR + ℓ) of some Poincaré P. This is modelled on rigidity of approximate isometries between Euclidean spaces: Hyers–Ulam 1945 (Bull. AMS 51, 288) and Gruber 1978 (Trans. AMS 245, 263) [V-meta] treat additive error only, and the multiplicative ε·d_h term needs (1+ε)-bi-Lipschitz rigidity such as John 1961 (CPAM 14, 391) [V-meta]; see also Alestalo–Trotsenko–Väisälä 2001 [unchecked]. Neither applies directly, since (U, d_h) is not a normed space; the transfer to U is assumed, not proved. Given h, the bounded-domain rigidity is essentially of this known type, and (C3) reduces E(4) to time-axis-preserving motions. With the fixed-frame norm of (C1), the exact freedom is ISO(3) × time translations; boosts enter only at O(ε). What is not known is a coarse rigidity in terms of causal order alone: the exact results (Hawking–King–McCarthy 1976; Malament 1977; Zeeman 1964 [unchecked]) need bijections or homeomorphisms, and Zeeman's dilations show that causal order alone does not fix scale. So each world's f is fixed **modulo Poincaré, up to a residual coarse error δ_f ~ εR + ℓ**.
- **Fixing across worlds** needs a cross-world gauge: a rule choosing P_w in each world.
- **Emitter anchoring** sets f_w(e) = 0 and maps an emitter frame to the standard frame. Two problems:
  - It needs the emitter's frame to be identified across worlds. Worse, E_w has h-diameter < ℓ, below the chart's additive resolution ℓ, so f_w(E_w) fixes translation to within ℓ and no frame at all. The emitter is "arbitrarily small", so its worldline gives a time direction but its spatial axes need apparatus orientation.
  - A frame error δθ at the emitter displaces images at distance R by δθ·R. Point anchoring amplifies errors with distance.
  - **Not enough on its own.**
- **Lab (observer) anchoring: chosen.** Choose P_w to minimise the misfit between f_w(lab bodies) and a fixed reference configuration in ℝ^{1,3}. The loss is the sum of squared Euclidean distances between anchor images and reference anchor points. The minimiser exists (a Procrustes problem with compact rotations and quadratic translations) and is unique iff the spatial anchors affinely span ℝ³ (at least 4 non-coplanar) and at least one anchor has temporal extent. The lab bodies are the emitter, the detector array and the walls, taken as macroscopic bodies at scale ≥ L. Least squares over several anchors removes the lever-arm amplification.
  - The reference configuration is shared across compatible worlds, because the observer's record (#399) fixes the macroscopic lab arrangement.
  - Result: P_w is fixed up to δ_P = O(εR + ℓ). The chart errors are systematic and bounded, not independent, so there is no 1/√(number of anchors) gain in the worst case.
- **Circularity check.** Anchoring on the detectors makes their images coincide across worlds almost by construction. That is intended. The question is not *where* d_i is, but whether the particle's worldline enters it. The identification is nontrivial only for what lies *between* the anchors (paths, microstructure) and for the detectors' microscopic content (§3).

## (3) Identifying d_i across worlds

- **Base criterion.** d_i^w belongs to [d_i] iff d_H(f_w(D_i^w), D_i^ref) ≤ τ/2, where D_i^ref is detector i in the shared reference configuration (§2). Comparing to the reference makes the relation transitive; a pairwise rule d_H(f_A(D_i^A), f_B(D_i^B)) ≤ τ is not transitive under chaining and does not define classes. Here d_H is the Hausdorff distance in ℝ^{1,3}, using the Euclidean norm in the lab frame, over the detector's spacetime region D_i. The tolerance must satisfy εR + ℓ + δ_P ≲ τ ≪ Δ, with Δ the minimum separation between detectors.
- **Optional microstructure criteria** (each is a well-defined refinement, to be chosen by the program and not by the LEA):
  - (M-a) The same microscopic topology in the ℓ-neighbourhood of D_i: same handle count and homotopy classes, or same holonomy classes.
  - (M-b) The same ledger content: the same persistent entries in the detector's diary (#399). That makes "d_i fired" a record identity, not only a position identity.
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
- **Flat cylinder and the two-slit toys** (#401–#409): **tension.** There the wrap L was at slit or route scale, i.e. macroscopic. Under the LEA that is condition 2: the toys are *outside* the LEA. The two-slit program put the topology at the scale of the routes; David's LEA puts it at the microscopic scale. With this toy, the pause is consistent.
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

## (6) The emitter–detector question, stated

**Data.**
- Scales ℓ ≪ L ≪ R ≪ 𝓡, a tolerance τ, and an energy window ℓ ≲ λ_E ≪ L.
- A set W of worlds (#399), each compatible with the observer's prior record 𝓡_0.
- Each w ∈ W contains:
  - (i) an emitter region E_w of h-diameter < ℓ, with an emission event that starts one test particle with a single classical worldline γ_w, with no superposition;
  - (ii) detector bodies D_1^w, …, D_n^w;
  - (iii) a lab region U_w ⊃ E_w ∪ ⋃ D_i^w satisfying conditions 1–6 of §4.
- Each w has an admissible projection f_w, lab-anchored (§2).

**Definitions.**
- **Detection at d_i in w:** γ_w enters D_i^w before entering any other D_j^w. Equivalently, under (M-b), the first new persistent entry is in d_i's diary.
- **Classes:** [d_i] is the equivalence class across W under the base criterion of §3, plus whichever (M-·) refinements are adopted. W_i = {w ∈ W : detection at a member of [d_i] in w}.
- **Admissibility of the classes:** the W_i are pairwise disjoint because detection is "first entry". Together with W_∅ (no detection), they cover W.

**Question.** For a measure μ on W, specified independently of the LEA, find the ratios μ(W_i)/μ(W_j).
- The LEA makes the *events* W_i well-defined and comparable across worlds. It says nothing about μ.
- The question is well-posed iff (a) §4's conditions 1–6 hold for every w ∈ W, (b) the identification classes are independent of the admissible choices within τ, and (c) μ is defined.
- Item (c) is the open problem. No probability is computed here, and no rule is assumed.

---

## Open items

0. Which global extension data (π₁, micro-handles) are admissible for a given germ: a classification, open.
1. Coarse rigidity in terms of causal order alone (the Riemannian rigidity via h is essentially known; see §2). Exact causal rigidity (Hawking–King–McCarthy, Malament, Zeeman) needs bijections, and no coarse or non-injective analogue is known. Lorentzian-intrinsic alternatives to the h-trick (options, not adopted; bibliographic only, per Literature/Geometry): Noldus, CQG 21 (2004) 839; Bombelli–Noldus, CQG 21 (2004) 4429; Sormani–Vega, CQG 33 (2016) 085001 (null distance, needs only a time function); Kunzinger–Sämann 2018 and Minguzzi–Suhr 2022 [unchecked]; finitary topology: Sorkin, IJTP 30 (1991) 923.
2. The choice of averaging convention, and a test of condition 4 on a host.
3. Microscopic CTCs: collapse is consistent with the one-way (C3) by construction (§1), at the price that the chart keeps no CTC information. Open: whether (M-a)/(M-b) can carry it consistently across worlds.
4. Which microstructure criterion (M-a/b/c) the program adopts. (M-b) ties the LEA to the ledger.
5. The measure μ on W, which is outside the LEA.

Ledger: L108–L114 (L108 records the paraphrase of David's direction).
