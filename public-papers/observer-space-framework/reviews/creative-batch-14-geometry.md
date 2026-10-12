# Geometry quick verdict: creative batch 14 (#379) — do not merge

**Read at:** #379 head `0ceaf85` (`notes/creative/batch-14.md`, ledger rows L43–L47). Prior context: #336 (tube cost), #364 (Type O/F, Cauchy-horizon constraint), #367/#375 (Misner/Taub–NUT), #372 R2 (under the lock the germ does not fork; the record does).

**Record type:** rough review. It applies nothing and stays neutral on David's open calls. Exploration only, under the 3:14 PM, 3:53 PM, 4:16 PM and 4:17 PM rulings (relayed, not signed). Structure only: no probability, no measure, no counting. All arguments are sketches unless marked **(proof)**. Citations: **(U)** standard, from memory, unchecked.

## Verdicts

| Q | Item | Verdict |
|---|---|---|
| 1 | winding count (L46) | **fix**: only around a *handle* is it topological; only relative (differences or classes rel endpoints) is it gauge-free; not constant between kicks |
| 2 | holonomy dichotomy (L46) | **fix**: "stable xor writable" too strong; flat holonomy is stable under flat deformations and writable by a curvature transient, exactly like winding |
| 3 | worldline vs ledger-geometry split | **fix (wording)**: sound for topology; holonomy belongs with the writable data; the winding is a joint invariant (worldline class in the fixed π₁) |
| 4 | reply-must-reach-the-ledger (weak point 7) | **OK with additions**: fits Type O; writes need a Type O class rel the ledger tube, and the write event lies beyond H⁺(S) |
| — | L43, L44/L45, L47 | **OK** (L47 with one clarifying sentence, below) |

## (1) Is the winding count well defined?

**Body around body: not topological in 3+1 (proof).** The relative direction of two point bodies in 3-space lies in S², and π₁(S²) = 0. So any closed relative motion is contractible, and "how many times body A wound around body B" has no homotopy-invariant integer value. (In spacetime terms: two timelike curves in a 4-manifold do not link; linking needs codimension 2.) Only a planar projection gives an integer, and that projection is a frame choice: gauge, not geometry. **Around a ledger handle it is topological:** a loop through a handle is a non-contractible class in π₁ of the fixed host region.

**Open worldline: no absolute integer (proof sketch).** A worldline segment c from event p to event q has no homotopy class as a loop. With a cut (a hypersurface Σ dual to the handle class), the signed crossing number c·Σ is an integer, but it depends on Σ: moving Σ across p or q changes it by ±1. A real-valued "angle/2π" version depends on a framing or connection. So the absolute value is not defined.

**What is gauge-free.**
- (i) Two segments c, c′ with the same endpoints: the loop c·c′⁻¹ has a class in π₁(M, p), and its image under the handle's homomorphism to ℤ (via H₁) is cut-independent. That is the difference of windings, as the batch says.
- (ii) Equivalently, the class of c rel endpoints, relative to a fixed reference segment. The reference must be declared (e.g. the unkicked history in the same host), or the record is gauge.
- (iii) If π₁ is non-abelian, the datum is a conjugacy class (or an element rel a basepoint path), and "an integer" needs a declared homomorphism π₁ → ℤ. Basepoint change acts by conjugation, which leaves a ℤ-valued homomorphism unchanged.

**Stability claim is wrong as written.** A body orbiting a handle keeps crossing Σ, so the count changes every orbit even with no kicks. The stable integer is the *deviation* from the reference history: the winding of c·c_ref⁻¹, taken between matched ledger events. It is constant between kicks only if the reference and actual orbits have the same period. Otherwise it drifts, and only the class at matched return events is a record.

## (2) Holonomy dichotomy

**Correct part (proof).** For a flat connection, the holonomy along a loop depends only on its homotopy class, so it is a representation ρ: π₁ → G up to conjugation. Along a continuous path of flat connections, ρ moves continuously on Hom(π₁, G)/G. If ρ is isolated (rigid, or G discrete), it cannot move by flat evolution.

**Too strong part.** Evolution need not stay flat. Matter or flux crossing a surface that spans the loop is a curvature transient. During the transient the holonomy is path-dependent. Once the region is flat again, ρ may sit in a different point or component (U(1) Aharonov–Bohm-type flux carried through the handle; for Levi-Civita, mass-energy moving through the loop) (U). That is "stable under small, flat perturbations; writable by a discrete event", the same structure as winding. Caveat: the Levi-Civita connection near a geon is not flat in vacuum (Weyl curvature), so flat holonomy needs an extra gauge field or a flat region. Parking is fine, but for lack of a mechanism, not because of the dichotomy.

## (3) Worldline-invariant vs ledger-geometry-invariant split

Sound for **topology**: deck labels and π₁ are fixed under 2C and are only labels. Not sound as stated for holonomy, by (2). The winding is not a pure worldline invariant either: it is the class of a ledger worldline in π₁ of the *fixed* topology, so the topology supplies the discreteness and matter supplies the change.

## (4) Reply-must-reach-the-ledger and Type O

**Fits (sketch).** The ledger is co-moving inside the observer's time-oriented tube U. Closing a return curve with a segment of the ledger worldline instead of γ changes the loop by a path inside U, and that adds no flip. So the Type O/F value of a class is the same whether it is read at γ or at the ledger (#364 (a), homotopy invariance). A Type O return arrives future-pointing, from the past: a genuine collision. In a Type F return, the carrier at the ledger is past-pointing relative to U (two emissions), so it would have negative energy for U-observers. That is excluded for a write under the weak energy condition. **So writes use Type O classes only,** which is #361's double-cover repair again.

**Two added constraints.**
- (a) By #364 (d), J⁻(q) ∩ J⁺(S) ⊂ D⁺(S). So the write event on the ledger lies beyond H⁺(S), and the ledger tube must itself cross the Cauchy horizon. The ledger state after a write is not fixed by data on S. That is where EKT non-uniqueness lives, so it fits, but the ledger's survival is extension-dependent too (#367/#375 exceptional sets).
- (b) A geon with π₁ ≅ ℤ/2 has no non-trivial Type O class (#364 (b)), so it cannot write.

**L47 clarification.** #372 R2 is about the observer's worldline germ. The observer-plus-ledger tube germ *after* a write differs across worlds by construction. State R2 for the worldline germ, not the tube germ.

## Replacement strings for `notes/creative/batch-14.md` (and L46)

**R1** (Set 3 table, winding row, first cell)
OLD: `**Winding count** of one ledger body around another (or around a ledger handle)`
NEW: `**Winding count** of a ledger body around a ledger handle (relative to a declared reference history; body-around-body winding is not topological in 3+1)`

**R2** (winding write, first bullet)
OLD: `Its integer winding relative to a fixed cut is a homotopy invariant of its worldline segment.`
NEW: `Its record is the class of its worldline segment rel endpoints, relative to a declared reference segment, mapped to ℤ by the handle's homomorphism. Only this difference is cut-, basepoint- and framing-independent; an open segment has no absolute integer winding.`

**R3** (winding write, stability bullet)
OLD: `Stability holds because, between kicks, the winding changes only if the body crosses the cut, which free motion does at definite times.`
NEW: `Stability holds for the deviation from the reference history, read at matched return events: between kicks, it is constant when the actual and reference orbits share a period. The raw crossing count itself advances every orbit.`

**R4** (holonomy row, last two cells)
OLD: `stability and writability conflict; **parked**`
NEW: `stable under flat deformations, writable by a curvature transient (flux or matter through the loop), like winding; **parked for lack of a mechanism** (Levi-Civita near a geon is not flat)`

**R5** (split paragraph)
OLD: `Invariants of the ledger *geometry itself* (deck labels, flat holonomy) are either fixed or continuous-only. Writes live in the matter on the fixed topology, not in the topology.`
NEW: `Topological invariants of the ledger (deck labels, π₁) are fixed. Flat holonomy is stable but writable only by a curvature transient. Writes live in data made discrete by the fixed topology and changed by matter: the classes of ledger worldlines in π₁, and possibly holonomy.`

**R6** (weak point 7, append)
OLD: `That adds a geometric condition to the round-trip definition.`
NEW: `That adds a geometric condition to the round-trip definition: the return class must be Type O (Type F arrives past-pointing at the ledger, with negative energy relative to the tube), the write event lies beyond H⁺(S) (#364 (d)), so the ledger tube must cross the Cauchy horizon, and a geon with π₁ ≅ ℤ/2 cannot write.`

**R7** (traps, nested-prefix bullet, append)
OLD: `**Passes**, as long as the ledger is not used to make the observer's geodesic fork.`
NEW: `**Passes**, as long as the ledger is not used to make the observer's geodesic fork. #372 R2 concerns the observer's worldline germ; the observer-plus-ledger tube germ after a write does differ across worlds, by construction.`

**R8** (ledger L46, middle)
OLD: `flat holonomy parked (stable xor writable)`
NEW: `flat holonomy parked (no write mechanism; stable under flat deformations, writable by curvature transients)`

**R9** (weak point 4)
OLD: `The cut** for winding counts needs a canonical choice, or else the record must be stated as differences only.`
NEW: `The cut** for winding counts has no canonical choice; the record is stated as differences from a declared reference history (fixed).`
