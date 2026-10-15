# Note: the smallest detector (one #388 handle, one virtual loop)

*DO NOT MERGE. Paper only, exploration (notes/creative/). Based on creative/detection-indirect-pairing at d16ff07 (#428). Classical; no Born input or claim; no squaring by hand. μ is open; (M1) untouched at L3. Spin-½ is a candidate, not adopted (L161). Closure of the loop through the detector is a premise (#428 R1, from David's 11:48 PM statement), not a ruling. Ledger row L180 is in §6 (this stack has no `notes/creative/ledger.md`).*

## Plain summary (for David)

We took the smallest detector we could: one fixed ledger handle (#388) and one virtual loop, with the two routes wired into the loop. The question was whether anything in the geometry makes that wiring write a record. In this model, nothing does. The handle can give a turn that belongs to the detector and not to the incoming routes, which is clean. But a fixed turn closes the loop only for special incoming setups. It cannot give both a fixed −1 and a record. The graph closes up and leaves no new topology behind, so any record has to be a matter event next to the handle, and the geometry doesn't fix whether one happens. Geometry names the missing piece, a "write rule", without adopting it. There is also a question for you: does the exact-closure rule govern only the detector's own virtual loop, or also the loops through the routes? The handle doesn't settle that.

## 1. Attribution

- **David's approval, 10:20 AM ET 2026-10-15** (direct in Creative Lead chat, not signed; verbatim as reported by Creative Lead; unverified by Literature, no original seen): "Yes, let's start that."
- **The step** is Claude 025's suggested next step on #428 ("Strongest obstacle and next step"), queued by Physics Lead.
- **The analysis** (§2–§4) is Geometry's, 10:21 AM ET 2026-10-15: a reviewer reading, not a ruling. Recorded by Creative Lead.

## 2. Verdict (Geometry)

In this minimal model, nothing in the geometry ties the wiring to a #388 write. The handle gives detector-fixed data (T2-clean), but it cannot supply both a detector-fixed −1 and a record. A write needs a new rule (named in §4, not adopted).

## 3. Setup and analysis (Geometry, reviewer reading)

**Setup.** A theta graph with vertices a and b, and edges E0 (route 1 reversed, then route 2), A1 and A2. The cycles are C1 = E0·A1, C2 = E0·A2 and L = A1·A2⁻¹. Hol(L) = Hol(C2)⁻¹·Hol(C1) up to conjugation, so exactness on any two cycles forces it on the third; for central ±𝟙 this is exact. Per #428 R5, the separation of a and b matters only through the enclosed curvature or topology.

**(i) The handle's holonomy.** If an arc's cycle passes through the handle (a discrete homology choice), the cycle picks up the handle's holonomy. That is fixed by the handle and L, independent of the incoming phases, so it is T2/LT2-clean. But #428 R2 needs the exact inverse mismatch times −𝟙. A fixed handle gives one fixed holonomy while the mismatch varies continuously, so closure holds only on a positive-codimension set of incoming configurations (codimension 1 in the abelian case, up to 4 in 3+1). Per #427 those worlds are still admissible, and their weight under μ is open. No write follows.

**(ii) Which cycles does the rule govern?** L is direct and virtual, so the exclusion rule governs it (David, 5:14 PM definition). C1 and C2 are indirect; per David's 7:11 PM wording (relayed via Geometry) their phases need not match. #428 R1's premise, taken from David's 11:48 PM statement, implies C1 is governed too. **This is a conflict for David to rule on, not a ruling:**
- **Reading A, L only:** detection cycles are free, the detector supplies nothing, and the record-writing problem goes away.
- **Reading B, L and C1 (hence C2):** the codimension result in (i).

The handle does not settle it.

**(iii) Sign source** (conditional, since spin-½ is not adopted, L161):
- **L contractible:** the −1 comes from the 2π turn and is detector-fixed, but the handle plays no part.
- **L routed through the handle's class** (non-zero in H₁(M; ℤ₂)): the sign is the free spin-structure sign, i.e. world data (the S8 ℤ₂, #423), and both signs occur.

So it cannot be both; this is the same split as #428 R4.

**(iv) Persistence.** The handle persists by hypothesis, L is virtual, and the vertices at a and b have degree 3, so the graph is closed, with no uncapped edge and no net topology change. Geometry alone leaves nothing new. Any record would be matter or flux next to the handle (David 9:28 PM, #388), a matter-sector event the geometry does not fix. The wiring locates a deposit but does not guarantee one. Per David's 10:37 PM framing, this needs a model and a showing of "more than never".

## 4. The missing piece (named, not adopted)

**Write rule:** when the virtual L is wired across the handle's class at a and b, flux of the routes' charge is appended next to the handle.

**Its T2 test:** it may refer only to the handle, L and the wiring class, never to the incoming phases, and it must leave exactness alone.

## 5. Open items and guardrails

- David's ruling on (ii): Reading A (L only) or Reading B (L and C1, hence C2).
- A write rule, if any, passing the T2 test in §4, with a model showing "more than never".
- Whether the record forgets the attachment (#428 S2).
- No Born claim is made. μ is open; (M1) is untouched at L3; spin-½ is not adopted (L161); closure through the detector is a premise, not a ruling.

## 6. Ledger row and change log

| L180 | The smallest detector (smallest-detector.md; step approved by David 10:20 AM, direct in Creative Lead chat, not signed; Claude 025's next step on #428, queued by Physics Lead) | Geometry (10:21 AM, reviewer reading): in the minimal model (one #388 handle, one virtual loop L, theta graph C1, C2, L) nothing in the geometry ties the wiring to a #388 write. (i) Handle holonomy is detector-fixed (T2-clean) but closes only a positive-codimension set of incoming configurations (admissible; weight under μ open). (ii) Which cycles the rule governs is a conflict for David: Reading A (L only) vs Reading B (L and C1, hence C2). (iii) Contractible L: detector-fixed −1, handle idle; L through the handle's class: free spin-structure sign (world data); not both. (iv) Closed graph, no net topology change; any record is a matter-sector event the geometry does not fix. Missing piece named, not adopted: a write rule referring only to handle, L and wiring class | Geometry (reviewer reading); David (approval of the step) | reading | David's ruling on (ii); write rule (T2 test); record forgets attachment |

L180 was checked against every `creative/*` branch and is free. On merge into the stack's ledger, move this row there.

**Change log**
- 2026-10-15: note opened (Geometry's 10:21 AM analysis of the smallest detector; David's 10:20 AM approval); L180 added.
