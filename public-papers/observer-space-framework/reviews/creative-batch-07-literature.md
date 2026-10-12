# Literature pass: creative batch 07 ("branches as geometries"), PR #351

Reviewer: Literature agent. PR head re-checked: `43b5d51` (base `creative/batch-06`). Files: `notes/creative/batch-07.md`, `notes/creative/ledger.md`. Do not merge.

Source marks: **V-text** = wording read in the source; **V-meta** = bibliographic data verified, content from the standard account.

## 1. (M1) explanation (highest priority)

**Mapping: correct.** Checked against `versions/v0.10.1-prose.md` (origin/main, V-text), `notes/m1-m2-decision-brief.md` (#266, V-text) and the EPP1 pedigree (MMWI 2006 applied rule; SHPMP 2008 Def. 3, as cited in v0.10.1 §App. B, V-text in v0.10.1):
- (M1) = per-vertex EPP1, "equal weight on each arm in force", $1/|A|$ per arm, ruled by David at L3 (#266: 11:45 PM ET 2026-10-10, relayed via Ontology's chat, not signed; L3 hold "strong opinion, weakly held, open to reversal if the analysis turns against it").
- EPP2 = "weight by ensemble size", kept as a foil. (M2) = Paper 1's count of distinct evolutions at a named cut, not adopted.
- (M1) is **not** "weight ∝ number of worlds". The ledger's plain-language note and batch-07's L23 bullet say exactly this. The agreement condition (the rules agree on a cut iff $\prod\deg$ is constant on it) matches v0.10.1. Note: "number of worlds" literally is EPP2 (hosts); (M2) counts distinct evolutions. They coincide only under David's "branch A = geometry A" reading. The ledger's "EPP2 or (M2)" is acceptable.
- Quote labelling: David's 3:43 PM words are marked "relayed via Physics Lead, not signed; verbatim". OK.

**Neutrality: two lines resolve the question for David. Wrong as stated.** David's acceptance was conditional: "Are we saying the weight is proportional to the number of worlds? If so, that is acceptable." The record answers "no" to the premise, so the acceptance does not yet attach to (M1). The two lines below turn a conditional into a ruling and lift L23. This is an apparent conflict, and David should resolve it. These lines do not reopen (M1).

S1. `notes/creative/batch-07.md`
- OLD: `David accepts weighting by counting worlds, so L23 is no longer a blocker in itself.`
- NEW: `David said weighting by counting worlds would be acceptable *if* that is what (M1) means; (M1) as recorded is per-vertex EPP1, not counting worlds, so whether L23 still blocks is flagged for David and not resolved here.`

S2. `notes/creative/ledger.md`
- OLD: `L23 is no longer a blocker in itself: weighting by counting worlds is acceptable to David.`
- NEW: `Open, flagged for David. His 3:43 PM acceptance of weighting by counting worlds was conditional on (M1) meaning that; (M1) as recorded is per-vertex EPP1, which is not counting worlds. Whether he accepts (M1) as recorded, or a world-counting rule (EPP2 or (M2)), is his call; until then L23's status is unchanged.`

## 2. Literature

| Claim / source | Status |
|---|---|
| Lachièze-Rey & Luminet, "Cosmic topology", Phys. Rep. 254 (1995) 135 | V-meta. Standard review of multiply-connected FLRW and ghost images. |
| Cornish, Spergel & Starkman, "Circles in the sky", CQG 15 (1998) 2657, gr-qc/9602039 | V-text (abstract). Matched circles come from the last-scattering sphere seen by "copies of the observer". |
| Planck 2013 XXVI (A&A 571, A26, 2014); Planck 2015 XVIII (A&A 594, A18, 2016) | V-text (2015 intro and abstract). The topology scale must exceed about $\chi_{\rm rec}$. Cubic torus: $R_i>0.92\chi_{\rm rec}$ (2013 likelihood); matched circles $R_i>0.94$ (2013); $R_i>0.97\chi_{\rm rec}$ (2015, T+P). |
| Topological lensing / cosmic crystallography (Lehoucq, Lachièze-Rey & Luminet, A&A 313 (1996) 339) | V-meta. |
| Ellis, "Topology and cosmology", GRG 2 (1971) 7; Ellis & Schreiber, "small universe", Phys. Lett. A 115 (1986) 97 | V-meta. Ghost images of our own galaxy in a small universe. |
| Mostow, Publ. Math. IHÉS 34 (1968) 53 | V-meta. Rigidity holds for **finite-volume** (lattice) hyperbolic manifolds, $n\ge3$. See R1. |
| Countably many finite-volume hyperbolic 3-manifolds; Thurston–Jørgensen: volumes are well-ordered, order type $\omega^\omega$, finite-to-one (Thurston notes 1978–79, ch. 6) | V-meta. Correct for lattices. |
| Quotients $\tilde M/\Gamma$, $\Gamma$ discrete, free and proper in Isom (Clifford–Klein; Wolf, *Spaces of Constant Curvature*) | V-meta. Correct. |

**R1 (wrong claim): countability needs finite volume, not just rigidity of Isom.** Infinite-covolume discrete subgroups of $\mathrm{Isom}(\mathbb H^3)=\mathrm{PSL}(2,\mathbb C)$, such as Schottky and quasi-Fuchsian groups, act freely and properly. They come in continuous families (quasiconformal deformations), and Mostow does not apply to them. "Hyperbolic sections ⇒ countable" holds only when $\Gamma$ is restricted to lattices (compact or finite-volume spatial sections).

S3. `notes/creative/batch-07.md`
- OLD: `is countable when $\mathrm{Isom}(\tilde M)$ is rigid, as for hyperbolic spatial sections (Mostow rigidity, unchecked).`
- NEW: `is countable for hyperbolic spatial sections only when $\Gamma$ is restricted to lattices (finite-volume quotients: Mostow 1968 rigidity plus countably many finitely presented groups); infinite-covolume groups (Schottky, quasi-Fuchsian) come in continuous families.`

S4. `notes/creative/ledger.md`
- OLD: `countable if rigid (Mostow), continuum if flat`
- NEW: `countable for finite-volume hyperbolic quotients (Mostow), continuum if flat or infinite-volume`

Note (no string): batch-07 line 53, "For rigid (hyperbolic) quotients the compatible set is countable", inherits R1. It is fine if "rigid" is read as "lattice".

**Trap sketch: correct.** If $\tilde M$ is $\Gamma$-periodic, every image in $\tilde M/\Gamma$ is the image of a real periodic copy, so geometry on the past cone cannot tell the two apart. Cosmic-topology tests (CSS circles, crystallography) work only because the perturbations in the simply-connected comparison model are *not* periodic. Under analyticity, the germ forces the cover's periodicity, so that lever is gone for geometry. That is consistent with the batch.

## 3. L27 and L28 verdicts

**L27 (symmetry bound).** Known: a Clifford–Klein space form constrained by the germ through $\tilde M$. Not killed (after S3/S4). Nothing smuggled. Note: "non-timelike" should mean that no element maps a point into its own chronological future. That is the usual no-CTC condition, so it is fine as a gloss.

**L28 (self-signal).** Known in spirit: ghost images of the observer or our galaxy in a small universe (Ellis 1971; Ellis–Schreiber 1986), and CSS's "copies of the observer". The test-field argument is valid: in $\tilde M$, one emitting worldline gives no returns, while in the quotient the lifted field is the $\Gamma$-sum. Not killed. Flags for David, not resolved:
- **Jet/patch lock.** A memory of received signals adds data beyond the jet/patch pair that Paper 1 locks as the observer state. Also, Paper 1 branches only "when the simply-connected analytic patches disagree", and L28's splits are by topology label with identical patches. The batch says this is a different object from $B_R$; it is a collision with the locked identity criterion, not a refinement.
- **Relative ensemble.** The narrowing by returns acts on $E(O)$ (cf. geodesic-lifts: multiplicity of $E(O)$ is locally invisible). This is consistent only if the record is admitted as state.
- **Measure / quantum smuggle.** No quantum structure is borrowed (a classical test field). No weight is written. The measure over the classes goes to David (see §1). An emitting body as matter in $g$ is already flagged as weak point 2.

## Guardrails
No forbidden symbol; no Born/$|a|^2$/$1/N$ result; no interpretation-camp framing; no pick among M1/M2/T-options (flagged only); Paper 1 untouched; David's words quoted exactly and marked relayed.

## Verdicts
- (M1) explanation: mapping **correct and neutral**; two lines **overstate** David's conditional acceptance (S1, S2: flag for David).
- Literature: citations **verified**; one wrong claim (R1: S3, S4).
- L27: **known, survives, nothing smuggled**.
- L28: **known in spirit, survives**; it collides with the jet/patch lock and Paper 1's identity criterion, and the measure goes to David.
