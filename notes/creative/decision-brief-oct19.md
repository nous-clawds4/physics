# Decision brief for David: seven open calls (Mon 2026-10-19)

*DO NOT MERGE. Paper only. Workstream (B), assigned by Physics Lead on Mon 2026-10-19 at 12:56 PM ET (Lead tasking, relayed; not David's). Stacked on #438 (creative/fermion-is-fs-geon at b61ccfa). Ledger: L186. This brief lays out calls; it adopts nothing and decides nothing. Classical only; no Born claim, no probability rule; μ open; (M1) untouched at L3; 1(a) and the write rule not adopted; spin-½ adopted for fermions (#431 §3c); CTCs adopted (L162).*

## Plain summary (for David)

Seven questions are waiting on you. Each section below says what the question is in plain words, what the options are, what each option would cost or open up, and where it comes from. A recommendation is given only where Geometry and Literature have both agreed in writing on the PRs. I searched their comments on #410, #417, #418, #421, #424, #427, #428, #432, #434, #436, #437 and #438 and found no joint recommendation on any of the seven, so every section says "No joint recommendation". On the three items from last week (calls 2, 3 and 5), both reviewers explicitly said they stay open and that they make no ruling (Geometry, #438 comment 6206123511; Literature, #436, #437 and #438 passes of 2026-10-15).

How to read the labels: "Claude 027/028" are review items; "Geometry" and "Literature" are reviewer readings, not rulings; "CL" is Creative Lead. David's words are quoted only where the repo already records them, with the labels they carry there.

## 1. Should species be conserved by postulate?

**Plain explanation.** You asked whether the geometry itself keeps count of fermion-like geons. Geometry's answer (#434) is no. The only rule the geometry supplies (Gibbons–Hawking) conserves a different number: how many prime pieces of space have an odd number of independent mod-2 loops (odd dim H₁(P; ℤ₂)), counted mod 2. That number is unrelated to whether a piece is spinorial. A single spinorial piece (the Poincaré sphere P) can appear from an ordinary 3-sphere, P can vanish alone, and one P can split into two, all without kinks (#434 §4, §6). So if each species is to be conserved, that has to be added as a rule.

**Options and what they imply.**
- *(a) Add a species-conservation postulate* (each species conserved, P̄ counting −1; #432 §3a (T-b) already treats this as a postulate, not a result). Consequence: the spinorial count is then conserved mod 2 (#434 §6). Cost, recorded for you (#434 §7, Claude 027 S5, not adopted): a geon-free slice could only produce an even number of non-trivial primes, so the odd n-tuples in your 1:36 AM ET 2026-10-14 closure family (Creative Lead paraphrase, L153), such as a triple appearing together, would be excluded; nested splittings (1 → 3 → 1) would not. It is an added rule, so it carries a T2 risk (#434 §6).
- *(b) No postulate.* The geometry then conserves only the odd-dim H₁(ℤ₂) total. #432 §3a (T-b)'s "P cannot vanish without P̄" would not hold (#434 §6), and any record or bookkeeping that relies on a particle persisting (for example #436's "P on X" record, which lasts only under the postulate, #436 §4a (V-c)) loses that support.
- *(c) Look for a physical restriction that yields it* (for example only pair-creation cobordisms, or a link between the frame's spin structure and geon spinoriality). This is #434 §7's open item; nothing has been found. Kinks only relax the rule, and Dowker–Sorkin's result is quantum and gives a spin–statistics correlation, not a conservation law (#434 §6, Claude 027 R2).

**Source.** #434 §6 (Verdict, "The program's class"), §7 (open items, incl. "Cost of a species postulate"); Claude 027 R2, S5; #432 §3a (T-b). **No joint recommendation.**

## 2. Which ℤ₂ is the fermion's −1?

**Plain explanation.** There are two different yes/no signs in play. One is the frame's spin lift: the World's spin structure gives every loop a ±1, whatever the loop carries; this is the sign exact closure uses (#431 §3a–§3c). The other is a spinorial core's own class: whether rotating the core by 2π can be undone, a property of the slice (its mapping class group), not of loops. Under the reading where the fermion is an FS geon (R-geon, #437 §4), one must say which of these is "the fermion's −1". How the two relate is an open question (#434 §7). Geometry adds (Geo-G3, #437 §4) that the Dirac box in shadow space has the frame lift's −1 by construction, so "the Dirac box copies the geon's sign" holds only if, far from the geon, the shadow map sends the core's class to the frame lift.

Your naming, as recorded (5:37 PM ET 2026-10-15, direct in Creative Lead chat, not signed; verbatim as reported by Creative Lead; unverified by Literature, no original seen; no hold level stated): "Yes, that is what I meant. FS geon names the world object, and Dirac box names its shadow-space stand-in." (#437 §1.) The naming does not by itself choose between the options below (#437 §2, CL observation).

**Options and what they imply.**
- *(a) The frame lift.* Fits what exact closure already uses and the Dirac box's sign. But the core then supplies a label, not the sign (#437 §4, Claude 028 R1), and every tube has this lift whatever its topology, so the adopted spin-½ does not single out cores (#438 §3a (Q-b)). Under this choice untraced loops carry the sign too, which bears on (F) vs (W) (#438, Claude 028 S2; call 5).
- *(b) The core's 2π class.* Makes the fermion's sign topological, as R-geon intends, and is classical (Giulini, Quantum Gravity (Birkhäuser), §3, as cited in #437 §4). Cost: the World's spin structure still adds a ±1 on every loop, so there are two signs to reconcile, and the Dirac box copies the geon's sign only if the far-field shadow map sends the core's class to the frame lift, which is #434 §7's open item (Geo-G3).
- *(c) Defer:* keep both as world data until #434 §7's relation is worked out. R-geon and R-frame stay "two readings, not picked" (#437 §4, L184).

**Source.** #437 §4 (R-geon) with Claude 028 R1 and Geo-G3 (Geometry comment https://github.com/nous-clawds4/physics/pull/438#issuecomment-6206123511); #434 §7, last item; L184 (OPEN for David). **No joint recommendation.** (Geometry states this item stays open and makes no ruling, comment 6206123511.)

## 3. Is "exactly one spinorial core" the definition of a fermion?

**Plain explanation.** Following your 6:32 PM inclination that the particle *is* the FS geon (#438 §1), Geometry suggested the wording "fermion = exactly one spinorial core plus any number of tensorial features" (#438 §3a (Q-b)). Classically, though, a piece of space with two spinorial cores (P#P) is still spinorial, just as P is (Giulini, IJTP 33, 913 (1994), §1, cited in #438 §3a). The statement "(−1)(−1) = +1", which would make two cores behave as a non-fermion, assigns each core's rotation the value −1. That is a quantization (sector) choice of the kind Friedman–Sorkin opened, not classical topology (#438 §3a (Q-b), Claude 028 R1, Literature J2). So "exactly one core" would be a definition, not a consequence of the topology or of the spin-½ adoption.

**Options and what they imply.**
- *(a) Adopt it as a definition.* Gives a clean species picture: one spinorial core decides "fermion", tensorial features (lens spaces, S¹×S²) distinguish species, and two cores count as two fermions (#438 §3a (Q-b)). Cost: it imports a sector choice from the quantum side into a classical model, so it should be labelled as a choice; and it interacts with call 2 (the spin-½ adoption is the frame lift and does not supply it, Claude 028 R1).
- *(b) Do not adopt; keep the classical statement only* (a spinorial slice can carry a −1; how many cores make a fermion is left open). Nothing further is fixed, and #438's species construction stays a CL proposal.
- *(c) Decide after call 2:* if the fermion's −1 is the frame lift (call 2(a)), the core count matters less for the sign; if it is the core's class (call 2(b)), this definition becomes central.

**Source.** #438 §3a (Q-b), Claude 028 R1, Lit-J2; L185 (OPEN for David). **No joint recommendation.** (Geometry, comment 6206123511: "exactly one core" is a definition, "That's all fine"; this agrees on the description, not a recommendation to adopt.)

## 4. Geometry's restatement: "pair-created at c, not mutually annihilated"

**Plain explanation.** Your 3:39 PM proposal asked whether the detector loop "becoming real" could be the record (#436 §1). Geometry pointed out that "becoming real" is not a change within one world: in a given world, a pair either appears and disappears together or it does not (#436 §4a (V-d)). Geometry's restatement is that L's two members are created together at a point c but do not annihilate each other; the antiparticle annihilates the incoming particle at its arrival point, and the particle carries on along an outgoing edge X. This is recorded as "proposed wording for David to confirm, not adopted". Per Physics Lead's tasking (relayed), it was put to you on a question card that was not answered.

**Options and what they imply.**
- *(a) Confirm the restatement.* "Virtual becomes real" then needs no new definition beyond "pair-created, not mutually annihilated". Claude 028 adds what confirming it commits to: c must lie in the causal past of the arrival point in both route worlds, and calling c "the same" in two worlds needs the cross-world identification #428 §6a(c)3 points to. One detector-fixed placement (c = the virtual L's own creation vertex) is listed, not adopted. For a topological particle, each vertex region contains CTCs (Geroch), consistent with CTCs adopted (L162), and passes #434's rule (Geo-G2).
- *(b) Reject or reword it,* and give "virtual becomes real" a different definition. #436's record idea then has no agreed formulation.
- *(c) Leave it open* until call 5 is settled, since what the record does to the detector loops depends on (F) vs (W).

**Source.** #436 §4a (V-d), with Claude 028 S1 and Geo-G2; L183. **No joint recommendation.** (Literature's #436 pass notes only that the restatement "stays proposed wording for David".)

## 5. Under (W), where does batch 23's exclusion live?

**Plain explanation, with the (F) vs (W) choice as context.** Once the detector loop is no longer a virtual pair, there are two readings of which loops count (#436 §4a (V-a)). Under **(F)**, every edge is a transport path whether or not anything travels it, so all three detector cycles remain and must close exactly; but nothing now supplies the extra turn (the −1) that L used to give. Under **(W)**, a loop exists only if a particle runs round it, so the detector has no cycles left in a detection world and asks nothing of the routes. Claude 028's consequence for (W): since a no-which-way record then removes the detector cycles as fully as a which-route record would, the exclusion behind any dark spot cannot sit in them; batch 23's kill rule (batch 23's term) would have to be met by virtual pairs away from the detector (#428 §5, last item). Claude marks these "questions for David, not results".

**Options and what they imply.**
- *(F)* Keeps the detector's closure demands, and the dark-spot exclusion can still sit in the detector cycles, but leaves L with no expected value (by 11:17 AM, exact means equal to the expected value) and the routes' mismatch to be compensated by mechanisms not yet shown (#428 §6a(c)2). The empty route's curve must also be specified (#432 §3a (T-c)).
- *(W), with the exclusion in virtual pairs away from the detector.* Removes the detector's demands cleanly, but a detection world then has one carried route, not a pair, while the adopted proposal makes every detection a pairing of two routes (#428 §2 item 1), a tension to resolve. It also requires a model of where those distant virtual pairs are and why they produce the dark spots.
- *(W), but a no-which-way record may not remove loops the way a which-route record does* (#436 §4a, "a question for David"). This needs a rule saying why, which is not yet written.
- Related: call 2(a) (the frame lift as the fermion's −1) puts a sign on untraced loops too, which weakens #438 (Q-d)'s lean towards (W) (Claude 028 S2 on #438).

**Source.** #436 §4a (V-a), (F) and (W) bullets with Claude 028 R1; #428 §2 item 1, §5; L183 (OPEN for David). **No joint recommendation.**

## 6. S4: does a frame coupled at v_a make exact alignment generic?

**Found in the repo.** "S4" here is Claude 023's suggested next step on #424 (batch 34), review of 2026-10-14: "on paper, before any new toy …, settle whether anything in the adopted structure makes exact alignment generic. The candidate is a frame coupled at v_a (#421 open item 1), with γ's closing arcs fixed by that coupling rather than chosen. If nothing does, record that the pairing picture shows cancellation only for a μ that gives weight to a set of worlds of codimension ≥ 1." Batch 34 holds it as your scope call (#424, "Held for David (scope call, #421 §8)"), and #427 §2 repeats that it stays your call.

**Plain explanation.** v_a is the vertex where a closed pair's two members meet and the pair is capped (#421 §1, batch 32). With a passive frame (one that does not act on anything), nothing at v_a forces the two transported frames to match; exact matching then holds only on a thin set of routes (#421 §8, the "dilemma"; #427). The question is whether the frame couples to something at v_a, so that its matching is imposed by dynamics and holds on an open set of routes.

**Options and what they imply** (#427 §2 and §4).
- *(a) Pursue S4.* If a coupling at v_a made exact alignment hold on an open set of routes, closure worlds would meet no extra conditions, and ambient genericity would no longer give them zero weight; it would also be a route to deriving the exclusion rule from the geometry (#427 open items; Claude 023 R5). #428's detector gluing raises the same coupling question in the detector's matter (#428, Claude 024).
- *(b) Do not pursue it now.* #427's answer ("exact closure is a law, not a coincidence") stands without it for the "invalid" half; per Claude 023, record that the pairing picture shows cancellation only for a μ that weights a codimension ≥ 1 set of worlds. μ stays open.

**Source.** Claude 023 review of #424 (review 5524433551), S4; #424 batch-34.md "Held for David"; #427 §2 and open items; #421 §8 open item 1. **No joint recommendation.** (Geometry's pass on Claude 023 on #424 agreed with R1–R5; I found no written Geometry or Literature position on S4.)

## 7. λ_E and Rec₀

**Found in the repo.** Both come from the low-energy approximation (LEA) work: batch 26 (#410), the LEA consolidation (#417), batches 28–30 (#413, #415, #418).

**λ_E (explicitly your call).** λ_E is the particle's dynamical resolution scale in the LEA's energy window ℓ ≲ λ_E ≪ L (ℓ the micro-handle scale, L the lab scale): "low" energy lets the coarse flat description apply to the apparatus; "not too low" keeps the particle coupled to the microstructure (#410 batch-26.md, condition 7). It is a placeholder: a free test particle follows the same geodesic at every energy, so λ_E needs a length from the classical particle model (its size, or the range of a self-field), and reading it as a de Broglie wavelength would put ħ in by hand (#410; #417 §4, Claude 018 R5). All runs so far use a point particle, which is the λ_E ≲ ℓ case (#417; #415). Batch 30 (#418) lists candidate particles with their natural λ_E: a point test body (none), an extended lump or geon (its size), a handle (its mouth size), a record-defined particle (the record's resolution), and a class of world-tubes (the tube width set by τ and ε); its next step 1 was "Ask David to choose λ_E and the particle candidate (suggest (c) with (e) for identity)", a CL suggestion. Choosing λ_E means choosing a particle model; a particle with a length must re-derive the point-particle results (#417 §9 item 2). The clock-rate item on #437 §5 notes the same: choosing a scale like λ_E is David's call.

**Rec₀ (open; not marked as your call in the repo).** Rec₀ is "the observer's prior record": the worlds that count are those "compatible with Rec₀" (#410, renamed from 𝓡₀). It "must be defined; at least, the lab bodies' images match the reference configuration within τ/2 and the diaries hold Rec₀", and the definition must say which data may differ between worlds and which Rec₀ fixes (#410). In the toys it is modelled only as "direction to τ/R, offset free below ℓ" (#413 batch 28, open item 3), and it sets the upper edge of batch 29's ballistic window (#415; #417 §9 item 1, "Rec₀. Not defined."). If Rec₀, or the particle model (λ_E), fixed the launch below ℓ, batch 28's finding would change (#413).

**Options and what they imply.** For λ_E: choose a particle model from #418's list (which fixes λ_E and the action it carries), or keep the point particle (λ_E ≲ ℓ) and accept that the LEA's energy window stays a placeholder. For Rec₀: the repo records it as an open definition, not as a choice put to you; defining it fixes which launch data are free across worlds and so moves the window's upper edge.

**Source.** #410 batch-26.md (plain summary, condition 7, §W definition); #417 lea-consolidated.md (§4, §9 items 1–2); #413 batch-28.md open item 3; #415 batch-29.md; #418 batch-30.md (candidates table, §7 step 1). **No joint recommendation.**

## 8. Ledger row and change log

| Row | Item | Status | Open |
|---|---|---|---|
| L186 | Decision brief for David, 2026-10-19 (decision-brief-oct19.md; Physics Lead tasking 12:56 PM ET 2026-10-19, relayed, not David's) | Brief only: lays out seven open calls (species postulate; which ℤ₂; "exactly one spinorial core"; V-d restatement; exclusion under (W), with (F) vs (W); S4 at v_a; λ_E and Rec₀); no joint Geometry–Literature recommendation found for any; nothing adopted | All seven calls open for David; L183, L184, L185 remain OPEN; species conservation a postulate (not adopted here); 1(a) and write rule not adopted; spin-½ adopted for fermions; CTCs adopted; μ open; (M1) untouched |

L186 was checked against every `creative/*` branch and is free. On merge into the stack's ledger, move this row there.

**Change log**
- 2026-10-19: brief written (Physics Lead tasking, Workstream (B), 12:56 PM ET 2026-10-19, relayed). Sources for S4 (Claude 023 on #424), λ_E and Rec₀ (#410, #413, #415, #417, #418) located in the repo; Geometry and Literature comments on #410–#438 searched for written joint recommendations; none found. L186 added.
