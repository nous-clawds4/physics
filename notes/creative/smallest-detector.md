# Note: the smallest detector (one #388 handle, one virtual loop)

*DO NOT MERGE. Paper only, exploration (notes/creative/). Based on creative/detection-indirect-pairing at d16ff07 (#428). Classical; no Born input or claim; no squaring by hand. μ is open; (M1) untouched at L3. Spin-½ is a candidate, not adopted (L161). Closure of the loop through the detector is a premise (#428 R1, from David's 11:48 PM statement), not a ruling. Ledger row L180 is in §6 (this stack has no `notes/creative/ledger.md`).*

## Plain summary (for David)

We took the smallest detector we could: one fixed ledger handle (#388) and one virtual loop, with the two routes wired into the loop. The question was whether anything in the geometry makes that wiring write a record. In this model, nothing does. The handle can give a turn that belongs to the detector and not to the incoming routes, which is clean. But a fixed turn closes the loop only for special incoming setups. It cannot give both a fixed −1 and a record. The graph closes up and leaves no new topology behind, so any record has to be a matter event next to the handle, and the geometry doesn't fix whether one happens. Geometry names the missing piece, a "write rule", without adopting it. There is also a question for you: does the exact-closure rule govern only the detector's own virtual loop, or also one loop through the routes? (Not both loops through the routes: if two loops close exactly at −1, the third is fixed at +1.) The handle doesn't settle that.

**Update (10:48 AM, §3a):** you ruled that within a world every loop must close exactly, the detector ones included, and only approximately in shadow space. That is neither Reading A nor B. Because the three loops' turns multiply, they cannot all close at −1: two at −1 force the third to +1. So the ruling works if "exact" for a loop means a fixed value, +1 or −1. **The question for you now is: what value counts as exact closure for each detector loop?** One option (our proposal, not adopted): the detector's virtual loop closes at −1, and the two route loops take the values that forces, say −1 and +1, named in advance; choosing that by hand would need its own justification.

## 1. Attribution

- **David's approval, 10:20 AM ET 2026-10-15** (direct in Creative Lead chat, not signed; verbatim as reported by Creative Lead; unverified by Literature, no original seen): "Yes, let's start that."
- **The step** is Claude 025's suggested next step on #428 ("Strongest obstacle and next step"), queued by Physics Lead.
- **The analysis** (§2–§4) is Geometry's, 10:21 AM ET 2026-10-15: a reviewer reading, not a ruling. Recorded by Creative Lead.

## 2. Verdict (Geometry)

In this minimal model, nothing in the geometry ties the wiring to a #388 write. The handle gives detector-fixed data (T2-clean), but it cannot supply both a detector-fixed −1 and a record. A write needs a new rule (named in §4, not adopted).

## 3. Setup and analysis (Geometry, reviewer reading)

**Setup.** A theta graph with vertices a and b, and edges E0 (route 1 reversed, then route 2), A1 and A2. The cycles are C1 = E0·A1, C2 = E0·A2 and L = A1·A2⁻¹. Hol(L) = Hol(C2)⁻¹·Hol(C1) up to conjugation, so the holonomies on any two cycles fix the third. For central values this holds exactly, with no conjugation caveat, and it fixes signs: if two cycles have spinor lift −𝟙, the third has lift (−𝟙)(−𝟙) = +𝟙 and so is not exact (#428 §6a(c)3). At most two of C1, C2, L can close exactly. Per #428 R5, the separation of a and b matters only through the enclosed curvature or topology.

**(i) The handle's holonomy.** If an arc's cycle passes through the handle (a discrete homology choice), the cycle picks up the handle's holonomy. That is fixed by the handle and L, independent of the incoming phases, so it is T2/LT2-clean. But #428 R2 needs the exact inverse mismatch times −𝟙. A fixed handle gives one fixed holonomy while the mismatch varies continuously, so closure holds only on a positive-codimension set of incoming configurations (codimension 1 in the abelian case; in 3+1, 4 in the flag form and 6 for the full holonomy, #428 T3; moving a or b along flat stretches of L adds no parameter, #428 R5). Per #427 those worlds are still admissible, and their weight under μ is open. No write follows.

**(ii) Which cycles does the rule govern?** L is direct and virtual, so the exclusion rule governs it (David's ruling, 3:33/3:40 PM, confirmed 3:58 PM, #424 §4a; L is a virtual pair by David's 5:14 PM ET 2026-10-14 definition, adopted 5:17 PM; direct in Creative Lead chat, not signed; #427 §3a). C1 and C2 are indirect; per Geometry's paraphrase of David's 7:07–7:13 PM proposal (#428 §2 item 3; relayed via Geometry, not signed; not David's verbatim words, and not the 7:11 PM item, which is the 'unpaired' correction, §2 item 6) their phases need not match. #428 §5 (Claude 025 R1, applied under Lead ruling) reads this as the routes' own mismatch, with the closure condition covering the whole loop through the detector: in effect Reading B, as a premise, not a ruling. #428 R1's premise, taken from David's 11:48 PM ET 2026-10-14 problem statement (direct in Creative Lead chat, not signed; verbatim as reported by Creative Lead; unverified by Literature, no original seen; not a ruling), implies C1 is governed too. **This is a conflict for David to rule on, not a ruling:**
- **Reading A, L only:** detection cycles are free, the detector supplies nothing, and the record-writing problem goes away.
- **Reading B, L and one detector cycle (say C1):** the codimension result in (i). C2 is then fixed at lift +𝟙 (Z1), so Reading B must govern only one of C1, C2, and the rule must say which, fixed before phases are compared (V1). "L, C1 and C2 all exact" has no solution.

The handle does not settle it.

**(iii) Sign source** (conditional, since spin-½ is not adopted, L161):
- **L contractible:** the −1 comes from the 2π turn, which under parallel transport needs curvature that L encloses (#428 R5), and is detector-fixed, but the handle plays no part.
- **L routed through the handle's class** (non-zero in H₁(M; ℤ₂)): the sign is the free spin-structure sign, i.e. world data (the S8 ℤ₂, #423), and each world has one sign; across the two spin structures, both occur.

So it cannot be both; this is the same split as #428 R4.

**(iv) Persistence.** The handle persists by hypothesis, L is virtual, and the vertices at a and b have degree 3, so the graph is closed, with no uncapped edge and no net topology change. Geometry alone leaves nothing new. Any record would be matter or flux next to the handle (David, 9:28 PM ET 2026-10-12, relayed via Physics Lead, not signed: "matter and flux next to fixed handles counts as encoded in spacetime for now"; #388), a matter-sector event the geometry does not fix. The wiring locates a deposit but does not guarantee one. Per David's 10:37 PM ET 2026-10-12 persistence words (relayed via Physics Lead, not signed; verbatim in the stack ledger: "it merely needs to happen more than never"), this needs a model and a showing of "more than never".

## 3a. David's ruling on (ii) (10:48 AM, 2026-10-15)

### (a) David's words

**10:48 AM ET 2026-10-15** (direct in Creative Lead chat, not signed; verbatim as reported by Creative Lead; unverified by Literature, no original seen). **Status:** David's ruling, no hold level stated.

> "In the context of an individual World, we require exact closure everywhere, for all the loops, including the detector ones. In shadow space, we do not require exact closure, only approximate."

### (b) Creative Lead reading

- This is neither Reading A nor Reading B. All three cycles (C1, C2, L) must close exactly within a world, and only approximately in shadow space. This matches David's #424 rulings (3:58 PM / 4:05 PM, 2026-10-14).
- Per Z1, holonomies multiply. If "exact" means spinor lift −𝟙 for every cycle, there is no solution, because two −𝟙 cycles force the third to +𝟙.
- So the ruling is consistent only if "exact closure" for a cycle admits some fixed central value (±𝟙). Which value each cycle needs is now the open question for David.
- **A natural option (Creative Lead proposal, not adopted):** the virtual L closes at −𝟙 (the cancellation sign), and the detector cycles take whatever exact values the identity fixes; for example C1 at −𝟙 and C2 at +𝟙, with the rule naming which is which before any phases are compared. Choosing that assignment by hand would need T2 justification.

No Born claim is made; μ is open; (M1) is untouched at L3; spin-½ is not adopted (L161).

## 4. The missing piece (named, not adopted)

**Write rule:** when the virtual L is wired across the handle's class at a and b, flux of the routes' charge is appended next to the handle.

**Its T2 test:** it may refer only to the handle, L and the wiring class, never to the incoming phases, and it must leave exactness alone.

## 5. Open items and guardrails

- ~~David's ruling on (ii): Reading A or Reading B~~ Ruled by David at 10:48 AM (§3a): exact closure for all loops within a world, including the detector ones; approximate only in shadow space. **New question for David:** what value counts as exact closure for each detector cycle (a fixed central value, ±𝟙)? With central lifts, C1, C2 and L cannot all be −𝟙 (Z1).
- A write rule, if any, passing the T2 test in §4, with a model showing "more than never".
- Whether the record forgets the attachment (#428 S2).
- No Born claim is made. μ is open; (M1) is untouched at L3; spin-½ is not adopted (L161); closure through the detector is a premise, not a ruling.

## 6. Ledger row and change log

| L180 | The smallest detector (smallest-detector.md; step approved by David 10:20 AM, direct in Creative Lead chat, not signed; Claude 025's next step on #428, queued by Physics Lead) | Geometry (10:21 AM, reviewer reading): in the minimal model (one #388 handle, one virtual loop L, theta graph C1, C2, L) nothing in the geometry ties the wiring to a #388 write. (i) Handle holonomy is detector-fixed (T2-clean) but closes only a positive-codimension set of incoming configurations (admissible; weight under μ open). (ii) Which cycles the rule governs is a conflict for David (its 'need not match' side is Geometry's paraphrase of David's 7:07–7:13 PM proposal, #428 §2 item 3, not his 7:11 PM words; Literature V6): Reading A (L only) vs Reading B (L and one detector cycle; with central lifts the third cycle is then +𝟙, so all three cannot be exact). (iii) Contractible L: detector-fixed −1, handle idle; L through the handle's class: free spin-structure sign (world data); not both. (iv) Closed graph, no net topology change; any record is a matter-sector event the geometry does not fix. Missing piece named, not adopted: a write rule referring only to handle, L and wiring class | Geometry (reviewer reading); David (approval of the step) | reading | (ii) ruled by David 10:48 AM (direct in Creative Lead chat, not signed; no hold level): exact closure for all loops within a world, including detector cycles; approximate only in shadow space. Open: what value (±𝟙, central) counts as exact closure for each detector cycle; CL proposal, not adopted: L at −𝟙, C1/C2 at the values the identity fixes, named in advance (T2); write rule (T2 test); record forgets attachment |

L180 was checked against every `creative/*` branch and is free. On merge into the stack's ledger, move this row there.

**Change log**
- 2026-10-15: note opened (Geometry's 10:21 AM analysis of the smallest detector; David's 10:20 AM approval); L180 added.
- 2026-10-15: Literature V1–V6 and Geometry Z1–Z9 applied. Z1 corrects Geometry's own 10:21 AM claim ('exactness on any two cycles forces it on the third'): with central lifts, two cycles at −𝟙 fix the third at +𝟙, so at most two of C1, C2, L can close exactly. The question to David is corrected accordingly (Reading B = L and one detector cycle; Z3, Z4, Z5, Z9). Merges: Z2 supersedes V5 (same string); Z6 and V3 merged (Z6's ruling cite with V3's date and adoption labels); V6 applied as a note in L180. V1: 'phases need not match' is Geometry's paraphrase (#428 §2 item 3), not David's 7:11 PM words.
- 2026-10-15: §3a added: David's 10:48 AM ruling on (ii) (exact closure for all loops within a world, including the detector ones; approximate only in shadow space), with a Creative Lead reading (neither Reading A nor B; with central lifts all three cannot be −𝟙, so 'exact' must admit a fixed ±𝟙 per cycle; option L at −𝟙, not adopted). §5, plain summary, L180 updated; the question to David is now what value counts as exact closure for each detector cycle.
