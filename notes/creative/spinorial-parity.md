# Note: is the number of spinorial geons conserved mod 2 under topology change?

*DO NOT MERGE. Paper only, exploration (for notes/creative/). Classical only: no Born input or claim, no probability rule; μ is open; (M1) untouched at L3; frame-level exactness 1(a) not adopted. Spin-½ adopted for fermions (#431 §3c); CTCs adopted (David, 2:27 AM ET 2026-10-14, relayed via Physics Lead, not signed). Recording approved by David at 3:09 PM ET 2026-10-15 (relayed via Geometry, not signed; paraphrase as relayed by Geometry, no verbatim words recorded; unverified by Literature, no original seen; approval of recording the note, not a ruling on its content; no hold level stated). Authored by Geometry: a reviewer reading (Geometry analysis), not a ruling. Follow-up to #432 §3a (T-a); stacked on #432 (creative/particle-topology-record at 27eb3eb; base b236247 merged since, see change log). Nothing in versions/ or papers/. Ledger row L182 is in §9.*

## Plain summary (for David)

No. The rule that comes from geometry, Gibbons and Hawking's, conserves one yes/no number. It is not "how many fermion-like geons, mod 2". It counts how many pieces of space have an odd number of independent mod-2 loops. Some spinorial (fermion-like) pieces count and some don't, and the same goes for non-spinorial pieces (#432 now calls these "tensorial", since "boson-like" is a quantum label). So with no kinks, a single fermion-like geon such as the Poincaré sphere can be created from a slice with no geons (an ordinary 3-sphere: ordinary empty space with its far region closed off, as batch 32 §1 does when it applies the rule), though not from the empty slice, and one can split into two. Spin bookkeeping would have to be added as a rule; the topology does not supply it.

## 1. Question

Within the Friedman–Sorkin geon picture, a prime summand of the spatial slice is fermion-like if it is spinorial, i.e. its 2π rotation is not isotopic to the identity. (In Sorkin's usage a topological geon is a nontrivial prime; S¹×S², a handle or wormhole, is usually treated separately. The table in §3(c) lists all primes.) [Claude 027: precisely, after Giulini §2, P is spinorial if the rotation of a small ball in P against a slightly larger concentric sphere, i.e. the 2π rotation at the end of P#ℝ³, is not isotopic to the identity through diffeomorphisms that fix a frame at the ball's centre. The frame matters, since without it the rotation is undone by turning the ball. In a slice with several primes the rotation is taken parallel to the sphere that splits P off (proof of Giulini's Corollary 1). "Fermion-like" names only this property: in Friedman–Sorkin's quantization, spinoriality allows half-integer-spin states but does not force them, so the spinorial count is a count of primes, not of fermions.] Is the number of spinorial primes conserved mod 2 under every allowed topology change? If it were, one fermion-like geon could split into a fermion plus a boson but never into two fermions, and spin bookkeeping would come from the geometry.

## 2. Definitions

- A **cobordism** is a compact oriented smooth 4-manifold W with ∂W = Σ₀ ⊔ Σ₁, where Σ₀ and Σ₁ are closed oriented 3-manifolds and may be empty or disconnected. e(W) is the Euler characteristic (Euler number) of W.
- A **Lorentzian cobordism without kinks** is a W carrying a time-oriented Lorentz metric for which Σ₀ and Σ₁ are spacelike, Σ₀ initial and Σ₁ final. It exists iff W admits a nowhere-zero vector field pointing inward on Σ₀ and outward on Σ₁ (take a Riemannian metric h and set g = h − 2v♭⊗v♭/h(v,v)). By Poincaré–Hopf the obstruction is e(W) − e(Σ₀) = e(W), since every closed 3-manifold Σ has Euler characteristic e(Σ) = 0. So the condition is **e(W) = 0** on each component of W (Reinhart 1963). A disconnected W can first be made connected by interior connected sums, which keep it oriented (and spin) and lower e by 2 each, so below W is taken connected (Claude 027). With kinks, the condition is replaced by kink-number bookkeeping (Gibbons–Hawking 1992b).
- A **spin-Lorentz cobordism** is a Lorentzian cobordism with W spin (w₂(W) = 0). For time-oriented g the Lorentz frame bundle reduces to SO(3) and an SL(2,ℂ) structure is a spin structure on W. Chamblin shows tetrad and spin-Lorentz cobordism are equivalent.
- The **mod-2 Kervaire semi-characteristic** is u(Σ) = dim H₀(Σ;ℤ₂) + dim H₁(Σ;ℤ₂) mod 2. It is additive under ⊔. For connected Σ, u(Σ) = 1 + d(Σ), where d(Σ) = dim H₁(Σ;ℤ₂).
- Since H₁(P₁#P₂) = H₁(P₁) ⊕ H₁(P₂), d is additive under connected sum.
- **Spinorial primes.** The only non-spinorial primes are the lens spaces L(p,q) (with S³ = L(1,0) and RP³ = L(2,1)) and S¹×S² (Giulini, Theorem 2, after Hendriks). A connected sum is non-spinorial iff all its primes are.

## 3. Results by class

### (a) Any smooth oriented cobordism: no conservation law

Ω₃^SO = 0 and Ω₃^Spin = 0 (Rokhlin; standard), so any two closed oriented 3-manifolds are cobordant, with spin structures if wanted. Nothing is conserved.

### (b) Lorentzian, no kinks, no spin condition: no constraint

**Claim.** For any Σ₀, Σ₁ there is a W with e(W) = 0.

**Proof.** Take any oriented cobordism W. Interior connected sum changes e by e(W#X) = e(W) + e(X) − 2. #CP² adds +1, #(S¹×S³) adds −2, #(S²×S²) adds +2. Use these to reach e = 0. ∎

The parity of e(W) is not fixed by the boundary here, so it constrains nothing. Geroch's theorem still applies: a compact time-oriented Lorentzian topology change has CTCs. CTCs are adopted, so this is allowed here.

### (c) Spin-Lorentz (Gibbons–Hawking): one ℤ₂ invariant, and it is not spinoriality

**Lemma (parity formula).** For any compact 4-manifold W with ∂W = M:

e(W) ≡ r + u(M) (mod 2),

where r is the rank of the ℤ₂ intersection form on the image of j: H₂(W;ℤ₂) → H₂(W,M;ℤ₂). (Gibbons–Hawking 1992a; Chamblin, Lemma, credited to Milnor and Kervaire; cf. G. Lusztig, J. Milnor and F. P. Peterson, "Semi-characteristics and cobordism", Topology 8, 357–359 (1969), doi:10.1016/0040-9383(69)90021-4, Crossref-checked by Literature.)

*Proof sketch.* Write b_i = dim H_i(W;ℤ₂) and m_i = dim H_i(M;ℤ₂). Take the exact sequence of the pair from H₄(W) = 0 to im j. Lefschetz duality gives dim H_i(W,M) = b_{4−i}. Its alternating dimension sum vanishes, which gives b₀ + b₁ + b₂ + b₃ ≡ r + m₂ + m₃. Poincaré duality on M gives m₂ + m₃ = m₁ + m₀. Since b₄ = 0, e(W) ≡ b₀ + b₁ + b₂ + b₃ ≡ r + u(M). ∎

**Spin step.** By Wu's formula, y∪y = v₂∪y for y ∈ H²(W,M;ℤ₂), with v₂ = w₂ + w₁². If W is spin, v₂ = 0, so the induced form on im j (which is nondegenerate) is alternating, and a nondegenerate alternating ℤ₂ form has even rank. Hence spin W has **e(W) ≡ u(∂W) (mod 2)**.

(Chamblin states "rank(h) even ⇔ w₂ = 0". Only the forward direction is needed here; even rank alone does not force the form to be alternating, so the converse as written is too strong.)

**Theorem (Gibbons–Hawking selection rule, kink-free; necessity from Gibbons–Hawking 1992a; sufficiency is stated in their abstract ("determines whether") and in Chamblin's Theorem 1, whose converse uses the same connected sums and cites Gibbons–Hawking for them; the argument below is Geometry's, Claude 027).** A spin-Lorentz cobordism from Σ₀ to Σ₁ exists iff

u(Σ₀) = u(Σ₁) (mod 2).

*Proof.* Necessity: Lorentzian means e(W) = 0, and the spin step then gives u(Σ₀) + u(Σ₁) ≡ 0. Sufficiency: Ω₃^Spin = 0 gives a spin cobordism W for any spin structures on the ends. Its e(W) is even by the spin step. Interior connected sum with S¹×S³ (−2) or S²×S² (+2), both spin, brings e(W) to 0. ∎

With kinks, the rule becomes u(∂W) + kink(∂W) ≡ 0 (mod 2) (Gibbons–Hawking 1992b; Chamblin Theorem 1).

**The conserved quantity.** For connected slices, u = 1 + d, so the conserved ℤ₂ is

d(Σ) = Σ over primes P of dim H₁(P;ℤ₂) (mod 2),

i.e. the number of primes with odd dim H₁(P;ℤ₂), mod 2. With several components, the number of components also counts. "Wormholes in pairs" is the special case P = S¹×S², which has d = 1.

**Per-prime table** (d = dim H₁(P;ℤ₂)):

| prime | spinorial? | H₁(P;ℤ) | d mod 2 |
|---|---|---|---|
| S³ | no | 0 | 0 |
| S¹×S² | no | ℤ | 1 |
| L(p,q), p odd | no | ℤ_p | 0 |
| L(p,q), p even (e.g. RP³) | no | ℤ_p | 1 |
| Poincaré sphere S³/I* | yes | 0 (I* perfect) | 0 |
| prism S³/D*₄ₙ, n even (e.g. the quaternionic space S³/D*₈) | yes | ℤ₂×ℤ₂ | 0 |
| prism S³/D*₄ₙ, n ≥ 3 odd (n = 1 is the lens space L(4,1); Giulini takes n ≥ 2) | yes | ℤ₄ | 1 |
| T³ | yes | ℤ³ | 1 |
| hyperbolic integral homology sphere | yes | 0 | 0 |

The abelianisations of D*₄ₙ follow Giulini's §4 presentations. Hyperbolic homology spheres are spinorial because they are K(π,1) primes other than S¹×S² (Giulini, Theorem 2).

Every combination occurs: spinorial with d even or odd, and non-spinorial with d even or odd. **The invariant is independent of spinoriality.**

### (d) Pin and time-non-orientable variants (brief)

- The parity formula holds for any compact W, using ℤ₂ Lefschetz duality.
- **Pin⁻** (w₂ + w₁² = 0; conventions of R. C. Kirby and L. R. Taylor, "Pin structures on low-dimensional manifolds", in Geometry of Low-Dimensional Manifolds 2, LMS Lecture Note Ser. 151 (CUP, 1990) [unchecked: Crossref gives 1991], pp. 177–242, doi:10.1017/CBO9780511629341.015): v₂ = 0, so the form stays alternating and the rule e(W) ≡ u(∂W) survives.
- **Pin⁺** (w₂ = 0, w₁ ≠ 0): v₂ = w₁² can be non-zero, and the rule can fail.
  - Example (Geometry's computation): RP⁴ has w(RP⁴) = (1+a)⁵, so w₂ = 0 and RP⁴ is pin⁺.
  - RP⁴ minus a ball has boundary S³ and e = 1 − 1 = 0. It carries a kink-free Lorentz metric (time-oriented or not, depending on how the line field splits), and it creates S³ from nothing although u(S³) = 1.
  - The same manifold, with a time-non-orientable metric, is Gibbons's example in Chamblin §V: de Sitter space between two slices, identified antipodally, "the standard example of the 'creation of a spacelike S³ from nothing' spacetime" (Claude 027; RP⁴ minus a ball is Claude 027's reading of Chamblin's S³ × [0,1]/ℤ₂).
- Chamblin derives the pin-Lorentz conditions case by case with Karoubi's criterion (Theorem 2 and its corollary). Our reading of his case 3 (time-orientable, not space-orientable) is unchecked. [Claude 027: the time-oriented example fits his Theorem 2. In signature (−+++) his Pin(3,1) condition is w₂ = (w₁⁻)², i.e. w₂ = 0 when time is orientable, which RP⁴ minus a ball meets; and (w₁⁺)² = a² ≠ 0 there, since RP²·RP² = 1, so r = 1 is odd and the theorem gives u + kink ≡ 1, as S³ from nothing needs. His "Property [P]" discussion is not needed, since the parity lemma gives r = 1 directly.]
- None of these variants refers to spinoriality of the slice primes either.
- Hadley's spin-½ uses time-non-orientable spacetimes, which is a different mechanism.

## 4. Test cases (spin-Lorentz, kink-free, all explicit)

Let P be the Poincaré homology sphere. It is spinorial, with d = 0 and u = 1. It bounds the E8 plumbing X: simply connected, with even form, hence spin, and e(X) = 1 + 8 = 9.

1. **One fermion-like geon from a geon-free slice: S³ → P.** (From the empty slice it is forbidden: u(∅) = 0 ≠ u(P) = 1.)
   - W = (X minus an open ball) # 4(S¹×S³). Its boundary is S³ ⊔ P, and e = 8 − 8 = 0. It is spin.
   - Selection rule: u(S³) = u(P) = 1. ✓
   - **A single spinorial prime is created with no kink.**
2. **One spinorial geon splits into two: P → P#P.**
   - W = (P×I) ♮ X, a boundary connected sum on the Σ₁ end, then # 4(S¹×S³). Here e(W) = 0 + 9 − 1 − 8 = 0, it is spin, and its ends are P and P#P.
   - u(P#P) = 1 + 0 = 1 = u(P). ✓
3. **A forbidden split of one spinorial geon into two: P → P#T³.**
   - u(P#T³) = 1 + 3 ≡ 0 ≠ u(P), so no kink-free spin-Lorentz cobordism exists.
   - It is forbidden because d(T³) is odd, not because T³ is spinorial.
4. **Pair creation (Dowker–Sorkin): S³ → P#P̄.** u = 1 + 2d(P) ≡ 1. Allowed for every P, as it must be.

## 5. Literature

- **Gibbons–Hawking (CMP 148, 1992).** Abstract and text excerpts read: "it is impossible to create a single wormhole … but it is kinematically possible to create such wormholes in pairs"; the invariant is "the mod 2 Kervaire semi-characteristic", u = dim(H₀(Σ;ℤ₂) ⊕ H₁(Σ;ℤ₂)) mod 2. Their wording describes compact Σ bounding a spin Lorentzian M. Applied to Σ₀ ⊔ Σ₁ it gives §3(c). [Geometry note: Claude 026's #432 S1 reading, u(Σ) = 0 with Σ the whole boundary, is the same rule, since u adds mod 2 over Σ₀ ⊔ Σ₁; it conserves only the total number of primes with odd dim H₁(P; ℤ₂) mod 2, not the handle count alone (for example RP³ → S¹×S² is allowed).]
- **Gibbons–Hawking (PRL 69, 1992).** Abstract read: "the Kervaire semicharacteristic of the boundary plus the kink number … must vanish modulo 2"; "the number of wormholes plus the number of kinks created during a topology change is conserved modulo 2."
- **Chamblin (1994).** Text read: Theorem 1 (spin-Lorentz: u + kink ≡ 0) and Theorem 2 (pin-Lorentz, with the w₁⁺ condition). One overstatement is noted in §3(c).
- **Dowker–Sorkin (1998).** Abstract and summary read: spin-statistics holds for non-chiral abelian geons "if they are described by a wave function which is given by a functional integral over metrics on a particular four-manifold", the U-tube pair-creation cobordism. "In a theory without topology change there is no obstruction to 'anomalous' spin-statistics pairings for geons." Their result is quantum, sum-over-histories, and specific to pair creation. It does not give a classical parity law, and nothing in it contradicts §4.
- **Dowker–Surya (1998).** Text read by Claude 027 (arXiv TeX source; the abstract says only that these transitions are investigated). The index criterion is the Borde–Sorkin conjecture: a Morse metric is causally discontinuous iff it has a point of index 1 or n−1. The U-tube that creates a pair of geons "is necessarily causally discontinuous", while the black-hole pair-creation instanton admits causally continuous Morse metrics. Their §4 answers the single-geon question for Morse metrics: by Lickorish–Wallace every 3+1 transition is the trace of index-2 surgeries, so, given Borde–Sorkin, it has a causally continuous cobordism, and for the creation of a single prime "the restriction of causal continuity will not be enough to rule this out". Morse metrics are the alternative to CTCs (batch 31 §3), not the program's class (§6, Scope).
- **Sorkin (1986)**, "Introduction to topological geons": bibliographic data checked; text not read.
- **A classical theorem that fermion-number parity is conserved under topology change:** none found. This is a negative search result, not a proof that none exists.

## 6. Verdict

**False in classes (a), (b) and (c), and in (d): the §4 examples are spin, hence also pin⁺ and pin⁻; pin⁺ in addition breaks the u rule.**

- The only kink-free spin-Lorentz selection rule is u(Σ₀) = u(Σ₁). For connected slices it conserves the number of primes with odd dim H₁(P;ℤ₂), mod 2.
- That invariant is independent of spinoriality (table in §3(c)).
- Explicit counterexamples: S³ → P creates a single spinorial geon, and P → P#P splits one into two. Reversing the time orientation of §4 case 1 gives P → S³, also kink-free and spin-Lorentz, so P can also vanish alone: #432 §3a (T-b)'s "P cannot vanish without P̄" holds only under a species postulate (Claude 027).
- Spin bookkeeping in the Friedman–Sorkin sense is therefore not supplied by the classical geometry. It would need an added rule, which is a T2 risk, for example restricting the allowed cobordisms to pair-creation types. Kinks only relax the u rule: with any kink number allowed, spin-Lorentz cobordisms exist between arbitrary slices (Chamblin, after Corollary 1). Dowker–Sorkin's mechanism is not a route here: it is a quantum sum over histories, so it cannot be an input in this classical model, and it gives a spin–statistics correlation for geons created in pairs through the U-tube, not a conservation law (Claude 027).

**The program's class.** It is (c) without kinks. Closure vertices are compact, time-oriented Lorentzian regions with spacelike ends (batch 32 §1–§2; CTCs adopted, L162), and the adopted spin-½ needs a spin structure on the world, which restricts to every vertex region (batch 31 §1b; #423). The §4 examples lie in this class, hence in every larger one. Time-non-orientable geon hosts are allowed only as exploration (David, 4:16 PM ET 2026-10-12, relayed by Physics Lead, not signed; paraphrase of the verbatim ledger row "Yes, allow CTCs and non-time-orientability in geon hosts, as exploration only."; unverified by Literature, no original seen; ledger, "Geon hosts"), and using Geroch's non-orientable branch for closures is a scope choice for David (#421 §8). Conservation of each species (P̄ counting −1) would conserve the spinorial count mod 2, since P and P̄ are spinorial together, so §4 also shows that species conservation is not kinematic. P's spinoriality does not rest on the Hatcher-conjecture cases of Giulini's proof: I* has a non-cyclic Sylow 2-subgroup (Q₈), which is the Hendriks criterion Giulini quotes (Claude 027).

**Scope.** Within §3(c) the result is exact: the rule is necessary and sufficient. It covers only existence of a topology. Whether such a W carries an analytic metric meeting the program's other conditions (exact closure, the lock, no singularity under energy conditions) is not addressed. Causal continuity is not one of them. In the adopted class Geroch's theorem puts a CTC in every topology-changing W, so no such W is even distinguishing, let alone causally continuous. And since e(W) = Σ(−1)^λ m_λ for any Morse function on W relative to Σ₀, e(W) = 0 with no points of index 1 or 3 leaves no critical points at all, i.e. W = Σ₀ × I: in this class every topology change has index-1 or index-3 points. Causal continuity in Dowker–Surya's sense is a property of Morse metrics, and even there it does not forbid creating a single geon (§5) (Claude 027).

## 7. Open items

- Do the cobordisms of §4 admit analytic Lorentz metrics consistent with the program's rules (exact closure, the lock)? An analytic, time-oriented Lorentz metric with spacelike ends is cheap on any W with e(W) = 0: approximate h and v of §2 by analytic ones, since the conditions are open (Claude 027 sketch, not checked against a source). Causal continuity is not asked (§6, Scope).
- Does any physically motivated restriction make spinoriality parity conserved? For example: only pair-creation cobordisms, or a requirement relating the frame-lift spin structure of #431 §3c to geon spinoriality. (Only Morse indices 0, 2 or 4 is not a candidate. In this class it forbids every topology change, since e(W) = 0 (§6, Scope). For Morse metrics it still allows a single P from S³: X minus a ball is S³ × I with eight 2-handles of even framing, so it is spin, and Dowker–Surya §4 note that causal continuity does not forbid single-prime creation. Claude 027.)
- Cost of a species postulate (for David's decision; not a ruling and not adopted): under #432's chain (ℤ-valued for a chiral species, ℤ₂-valued if P ≅ P̄), a geon-free slice can only produce an even number of non-trivial primes. So the odd n-tuples in David's 1:36 AM ET 2026-10-14 closure family (Creative Lead paraphrase, L153) (batch 31 §1 and §4; L153), such as a triple appearing together, would be excluded; nested splittings (1 → 3 → 1) would not (Claude 027).
- Kinks: with u + kink ≡ 0, does any natural kink rule tie in spinoriality? (Not expected: kink numbers see the boundary, not the mapping class group.)
- Pin⁺ example in §3(d): checked against Chamblin's Theorem 2 for the time-oriented metric (§3(d), Claude 027); the time-non-orientable version is Gibbons's example in Chamblin §V.
- How the adopted spin-½ (a spin structure on M, #423/#431) relates to Friedman–Sorkin spinoriality (the mapping class group of the slice). These are different structures; how they relate is unchecked.

No Born claim is made; μ is open; (M1) is untouched at L3; 1(a) is not adopted.

## 8. Citations (verified by web unless marked)

- G. W. Gibbons and S. W. Hawking, "Selection rules for topology change", Commun. Math. Phys. 148, 345–352 (1992), doi:10.1007/BF02100864 (abstract and text excerpts read).
- G. W. Gibbons and S. W. Hawking, "Kinks and topology change", Phys. Rev. Lett. 69, 1719–1721 (1992), doi:10.1103/PhysRevLett.69.1719 (abstract read).
- A. Chamblin, "Some applications of differential topology in general relativity", J. Geom. Phys. 13, 357–377 (1994), doi:10.1016/0393-0440(94)90015-9, arXiv gr-qc/9509048 (text read).
- B. L. Reinhart, "Cobordism and the Euler number", Topology 2, 173–177 (1963), doi:10.1016/0040-9383(63)90031-4 (abstract and theorem statements read; pages Crossref-checked by Literature).
- R. P. Geroch, "Topology in general relativity", J. Math. Phys. 8, 782–786 (1967), doi:10.1063/1.1705276 (bibliographic data checked).
- J. L. Friedman and R. D. Sorkin, "Spin 1/2 from gravity", Phys. Rev. Lett. 44, 1100–1103 (1980), doi:10.1103/PhysRevLett.44.1100; erratum Phys. Rev. Lett. 45, 148 (1980).
- H. F. Dowker and R. D. Sorkin, "A spin-statistics theorem for certain topological geons", Class. Quantum Grav. 15, 1153–1167 (1998), doi:10.1088/0264-9381/15/5/007 (abstract and summary read).
- F. Dowker and S. Surya, "Topology change and causal continuity", Phys. Rev. D 58, 124019 (1998), doi:10.1103/PhysRevD.58.124019, arXiv gr-qc/9711070 (abstract read).
- R. D. Sorkin, "Introduction to topological geons", in P. G. Bergmann and V. De Sabbata (eds.), Topological Properties and Global Structure of Space-Time, NATO ASI Series B 138 (Plenum, 1986), pp. 249–270, doi:10.1007/978-1-4899-3626-4_19 (bibliographic data checked; text not read).
- D. Giulini, "On the configuration space topology in general relativity", Helv. Phys. Acta 68, 86–111 (1995), arXiv gr-qc/9301020 (text read; Theorem 2, Corollary 1, §4 abelianisations).
- M. J. Hadley, "Spin-1/2 in classical general relativity", Class. Quantum Grav. 17, 4187–4194 (2000), doi:10.1088/0264-9381/17/20/303 (abstract read).
- Standard and not re-verified here: Ω₃^SO = Ω₃^Spin = 0 (Rokhlin); Wu's formula; that the E8 plumbing bounds the Poincaré sphere (e.g. R. E. Gompf and A. I. Stipsicz, 4-Manifolds and Kirby Calculus, AMS GSM 20, 1999; text not read by Literature); Hendriks (1977), cited via Giulini; see also J. L. Friedman and D. M. Witt, "Homotopy is not isotopy for homeomorphisms of 3-manifolds", Topology 25, 35–44 (1986), doi:10.1016/0040-9383(86)90003-0 (Crossref-checked by Literature).

## 9. Ledger row and change log

| L182 | No mod-2 conservation of spinorial geons (spinorial-parity.md; follow-up to #432 T-a; authored by Geometry, reviewer reading, not a ruling; recording approved by David 3:09 PM ET 2026-10-15, relayed via Geometry, not signed, paraphrase as relayed by Geometry (no verbatim words), unverified by Literature, no original seen, approval of recording, not a ruling on content, no hold level) | The count of spinorial primes is not conserved mod 2 under any allowed class of topology change: (a) smooth oriented cobordism, nothing conserved; (b) Lorentzian, no kinks (e(W) = 0), no constraint; (c) spin-Lorentz (Gibbons–Hawking) conserves only the Kervaire semi-characteristic u mod 2 (for connected slices, the number of primes with odd dim H₁(P;ℤ₂)), independent of spinoriality; (d) pin⁺ can break even that. Counterexamples: S³ → P and P → P#P (Poincaré sphere), kink-free spin-Lorentz. For #432: species or fermion-parity conservation remains a postulate (e.g. pair-only creation P#P̄, T2 risk); Dowker–Sorkin's quantum spin–statistics result is a comparison, not an input, and not a conservation law (Claude 027) | Geometry (analysis, reviewer reading); David (approval of the step) | reading | analytic metrics meeting exact closure and the lock for the §4 cobordisms (causal continuity is not a condition here: Geroch's CTCs rule it out in this class, and for Morse metrics it does not forbid single-geon creation, Dowker–Surya §4; Claude 027); any motivated restriction (pair-only; Morse indices 0, 2, 4 excluded, Claude 027) making spinoriality parity conserved; kink rules; relation of the adopted spin-½ structure (#431 §3c) to Friedman–Sorkin spinoriality; μ open; (M1) untouched |

L182 was checked against every `creative/*` branch and is free. On merge into the stack's ledger, move this row there.

**Change log**
- 2026-10-15: note recorded from Geometry's draft (content intact; only the header attribution was expanded and this ledger section added); L182 added. Forward pointer from #432 §3a (T-a) deferred while Claude job 026 is pending on #432. (Since added on #432 at 4a12f4a; Geometry's 3:28 PM bracket followed at cb44738; #432's head is now b236247, ahead of this branch's base 27eb3eb. Claude 027.)
- 2026-10-15: Literature A1–A12 applied: 3:09 PM item recorded as a paraphrase relayed by Geometry, unverified by Literature, recording approved (header and L182); CTC adoption dated (2:27 AM 2026-10-14, relayed via Physics Lead); Sorkin caveat on S¹×S²; Gibbons–Hawking necessity vs Geometry's sufficiency argument; 'from nothing' corrected (from a geon-free S³; from ∅ forbidden); citations added or completed (Lusztig–Milnor–Peterson, Dowker–Surya DOI, Reinhart pp. 173–177, Kirby–Taylor, Gompf–Stipsicz, Friedman–Witt).
- 2026-10-15: merged the moved base (creative/particle-topology-record at b236247; normal merge commit, no conflicts). Geometry note added to the Gibbons–Hawking (CMP 148) bullet of §5, verbatim: Claude 026's #432 S1 reading is the same rule (u adds mod 2 over Σ₀ ⊔ Σ₁; only the total number of primes with odd dim H₁(P; ℤ₂) is conserved mod 2; RP³ → S¹×S² allowed). Claude 027/028 items applied per Lead ruling (Physics Lead, 9:36 PM ET 2026-10-15, relayed; a Lead ruling under delegation, not David's): Claude 027 review of #434 at 92ea429 (https://github.com/nous-clawds4/physics/pull/434#pullrequestreview-5541400631), all items as-is with Claude's exact OLD→NEW text. R1: causal continuity is not a program condition or open test (Geroch CTCs rule it out in the adopted class; Morse indices 0, 2, 4 forbid every topology change there; Dowker–Surya §4: it does not forbid single-geon creation for Morse metrics); §5, §6, §7 (two items), L182 and the PR description. R2: Dowker–Sorkin is not a route to species conservation (quantum, a spin–statistics correlation, not a conservation law); kinks only relax the u rule; §6, L182, PR description. S1: new "program's class" paragraph in §6 (class (c) without kinks; species conservation not kinematic; P's spinoriality unconditional). S2: frame-fixed definition of "spinorial"; "boson-like" replaced in the plain summary. S3: e(W) = 0 per component; sufficiency credited to Gibbons–Hawking's abstract and Chamblin's Theorem 1. S4: RP⁴ example credited (Gibbons's example in Chamblin §V), checked against Chamblin's Theorem 2; open pin⁺ item closed in §7 and L182. S5: P can vanish alone (P → S³); cost of a species postulate recorded for David (not adopted). N1: "fermion" → "spinorial geon" in §4 case titles. N2: odd-n prism row n ≥ 3. N3: Dowker–Sorkin quote completed ("for geons"). N4: verdict line covers pin⁺ and pin⁻. N5: deferred-pointer note updated. N6: "ordinary 3-sphere" explained (note and PR description). No species-conservation postulate adopted; 1(a) and the write rule not adopted.
- 2026-10-15: fix round after Claude 027/028 (brief relayed 9:49 PM ET 2026-10-15). Geometry's and Literature's items are labelled Geo- and Lit- because both used the letter G. Geo-G1 (Geometry comment https://github.com/nous-clawds4/physics/pull/438#issuecomment-6206123511): line 16 now reads 'every closed 3-manifold Σ has Euler characteristic e(Σ) = 0'. Recorded reading (Geometry, reviewer reading, not a ruling): the standing rule bars only the Greek letter and its name, so 'Euler characteristic' written with e(·) is allowed; line 15's wording stays. Lit-F1–F4 (Literature comment https://github.com/nous-clawds4/physics/pull/434#issuecomment-6206181919): the 9:36 PM ruling labelled a Lead ruling under delegation, not David's (F1); David's 1:36 AM ET 2026-10-14 closure family labelled a Creative Lead paraphrase, L153 (F2); the 4:16 PM ET 2026-10-12 line labelled a paraphrase of the verbatim ledger row, unverified by Literature (F3); header pointer notes the b236247 merge (F4). Kirby–Taylor's year left as 1990, flagged '[unchecked: Crossref gives 1991]'. Nothing adopted.
