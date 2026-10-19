# Does threading change which worlds are detection worlds? (Geometry draft, workstream (E))

**Do not merge. Paper only.** Geometry draft, 2026-10-19, tasked by Physics Lead (Lead tasking, relayed; not David's words). Stacked on #448 (creative/throat-threading at 0376c18). Pins: #444 6491918, #448 0376c18, #445 9766fd3, #428 608af08, #427 5bd192e. None of these is edited. Nothing is adopted. Both virtual-pair definitions (V1, David 5:14 PM, #427 §3a; V2, Claude 024, #428 §4 item 2) stay open for David.

## Plain summary (for David)

Threading pairs change which worlds count as detection worlds. The record is r = q(d+N), so a false positive (no detection, one net threading) and a false negative (detection cancelled by a reverse threading) always exist; exact closure fixes holonomy, not crossing number, so it doesn't block them. Under V1 both are allowed; V2 reclassifies the threading loop as a real closed loop, which CTCs supply, so the coarse-grained-label reading fails. Charge sign, |n|, N1 and time orientation don't discriminate; the bridge condition (B), a parity rule (it needs an unfixed handle holonomy law) or an edge entry on X (the write rule) would, but none passes T2 as it stands. All under (F); nothing adopted.

## Cite check (Creative Lead; CC1 accepted by Geometry and applied)

Cite check against #427 5bd192e, #428 608af08, #445 9766fd3, #444 6491918, #448 0376c18. Mismatches were flagged as OLD (Geometry's text) / suggested NEW; Geometry accepted CC1 and it is applied in the draft below.

- #427 §3a (V1): matches, including "do not exist, by definition" ✓.
- #428 §4 item 2 (V2, "writes no entry anywhere", Claude 024) ✓; #428 §5 pin ✓; #428 §6a(c)2 (a, b solved per world) ✓.
- #445 ("n crossings leave nq"; at 9766fd3 "crosses S net n ≠ 0 times leaves a Gauss-flux entry nq") ✓.
- #444 at 6491918: §1 lemma (N1) ✓; §2 (a, b solved per world) ✓; §3 design condition that C3 crosses S net 0 (Claude 030 R4 bracket) ✓; §3 flux read after both crossings (Claude 030 S2 bracket, in the Condition 4 bullet) ✓; §4 (W) gives Reading A ✓.
- #448 at 0376c18: §2.2, §2.3, §2.4 caveat 1, §2.5, §2.6, §3(b), §3(c), (B1)/(B2) ✓.
- **CC1. Rulings location.** #444 has no §3a/§3b; the 10:48 AM and 11:17 AM rulings are recorded in #431 §3a/§3b (as #444 §4 and #428 cite them).
  OLD: `(10:48 AM and 11:17 AM rulings, #444 §3a/§3b)`
  NEW: `(10:48 AM and 11:17 AM rulings, #431 §3a/§3b)`

## Geometry's draft (verbatim from https://github.com/nous-clawds4/physics/pull/448#issuecomment-6274437319)

> Attribution: Geometry draft, 2026-10-19, tasked by Physics Lead (Lead tasking, relayed; not David's words). Text below is Geometry's, unedited apart from heading levels, CC1 and Literature's W2-1 to W2-3 (all accepted by Geometry).

**Geometry, workstream (E): does threading change WHICH worlds are detection worlds, or only add worlds that look the same at the record?** Draft note text for Creative to open as a stacked do-not-merge follow-up to #448. Paper only; nothing is adopted. Pins: #444 at 6491918 (detector-funnel-record.md §1–§5), #448 at 0376c18 (throat-threading.md), #447 (weight-gap.md: no weight by hand; countability assumed, open), #445 (net n crossings leave nq), #428 §4 item 2 and §5, #427 §3a. Virtual-pair definitions both open: V1 (David 5:14 PM, #427 §3a: a pair that appears together and then disappears together; imperfectly phase-matched virtual pairs "do not exist, by definition"); V2 ("writes no entry anywhere", Claude 024, #428 §4 item 2). Which governs is David's call. Classical only, no Born claim, μ open, (M1) untouched, 1(a) and the write rule not adopted, CTCs adopted, spin-½ adopted for fermions, species conservation not adopted, R-geon/R-frame open, (F)/(W) open. No ħ, measure, weight or phase rule appears, so nothing below says "rare" or "typical".

### Result in one paragraph
**Threading changes the classes, not just the count: the record map's fibers mix detection and non-detection worlds.** With d(w) ∈ {0, 1} the detection indicator and N(w) ∈ ℤ the total net crossing of S by the world's closed charged circulations, the record is r(w) = q·(d(w) + N(w)) (given #444 §3's design condition that C3 crosses S net 0). The fiber over r = q contains detection worlds (d = 1, N = 0) and false positives (d = 0, N = +1); the fiber over 0 contains non-detection worlds and false negatives (d = 1, N = −1); the same holds for every value under n-fold threading. Exact closure doesn't stop this: it constrains each loop's holonomy, not its intersection number with S. V1 permits both confounds (an exactly closing threading pair is a V1 pair). V2 reclassifies the threading loop as real, not as impossible, so the worlds remain unless real closed charged loops through the handle are separately excluded, and CTCs (adopted) supply exactly such loops. So the "coarse-grained label" reading fails: r is a well-defined function on worlds, but d is not a function of r. The only well-posed discriminators found are (B) from #448 (a restriction on the world set), a parity rule that needs every closed loop's crossing number to be even (not established; it needs a holonomy law for the handle that nothing fixes), and an edge-indexed entry on X (the write rule, not adopted). Charge sign, multiplicity |n|, conditioning on N1, and time orientation each fail. None passes T2 as it stands.

### 1. Definitions (reading (F))
Fix one world w under (F): every edge is a transport path, and a, b are solved per world (#444 §2, #428 §6a(c)2). Its charge content is an integer 1-chain J(w) = P's open chain plus a sum of closed circulations c_i (pairs under V1, or real loops).
- **Detection world:** d(w) = 1 iff P's chain is present on X (value 1 on X, ending at X's far end). That is a property of the world's chain, not of any record. (This is the definition used throughout; "P arrives" means d = 1.)
- **Record value:** r(w) = q·I(J(w), S), the signed intersection number of the whole charge chain with the throat surface S, read after all crossings (#444 §3, Claude 030 bracket: the flux value, not the time of change). By Gauss this is what the flux through S reads, and per #388 every charge that crosses counts.
- **Decomposition:** I(P's chain, S) = d(w)·1 + (C3 term), and #444 §3 (Claude 030) requires the C3 term to be 0 for route independence. Taking that design condition, r(w) = q·(d(w) + N(w)) with N(w) = Σ_i n_i, n_i = I(c_i, S) (#445: n crossings leave nq).
- **Exact closure:** every loop in the world closes exactly (10:48 AM and 11:17 AM rulings, #431 §3a/§3b). Under V1, David's own words make inexact virtual pairs non-existent, so exactness is part of V1 too.

R-geon/R-frame: r counts charge crossings and uses no spin or frame lift, so §1–§3 hold under both readings. Exact closure does use holonomy, and §3.2 states where the reading enters.

### 2. Do the confound worlds exist?
**2.1 False negative (d = 1, r = 0).** P arrives on X, and a closed circulation c with I(c, S) = −1 is present. N1 (#444 §1 lemma) keeps c off X, since X carries the chain. So c must cross S on some other edge Z ≠ X. That breaks #448's (B1) (X the only edge crossing S) but nothing else in the framework. S is non-separating, so such curves exist in the manifold (#448 §2.4 caveat 1).

**2.2 False positive (d = 0, r = ±q).** P doesn't arrive, and a closed circulation with I = ±1 is present. X is empty, so N1 doesn't bar the circulation from X itself (#448 §2.3). It needs a return path from X's far end to the source side, which breaks (B2); a CTC through the handle (adopted) is such a path (#448 §2.5). The sign: P's record has a fixed sign (+q, say); a loop of the matching orientation reproduces it (#448 §2.2).

**2.3 n-fold.** With several loops, N ranges over sums of the allowed n_i. If loops with n = ±1 are allowed, N takes every integer, and the fiber over r = kq is {d = 1, N = k − 1} ∪ {d = 0, N = k}, both non-empty for every k.

**2.4 Exact closure.** Exact closure is a condition on each loop's holonomy (a π₁ and frame quantity); I(c, S) is a homological intersection number. They are independent unless the holonomy of a loop is a function of its crossing number alone. Under (F) a loop's holonomy is the handle's contribution times the enclosed curvature along the rest of the loop, and the latter is world data solved per world. So exact closure generically leaves every n available: it's one condition on the loop's geometry, met by choosing the loop, not a condition on n. **Assumption flag:** "generically" here is a statement about which solutions exist, not about how many; no measure is used. If some world's curvature is forced trivial, see §3.2.

**2.5 V1 vs V2.**
- **V1:** a threading pair that appears and disappears together and closes exactly is a V1 pair. Both confounds are permitted.
- **V2:** a threading loop writes flux, so under V2 it isn't virtual. It is then a real closed charged circulation (a real pair created and annihilated, or a real charge round a CTC through the handle). V2 doesn't forbid it; it renames it (#448 §2.6). The confound worlds are excluded under V2 only if real closed charged loops through the handle are excluded, which nothing does, and adopted CTCs supply them. **Result: both V1 and V2 permit the false negative and the false positive.**

### 3. Is the record a coarse-graining that respects the detection class?
r is a well-defined map from worlds to qℤ, so it is a coarse-graining. It respects the detection class iff d is constant on each fiber. §2 shows it isn't: both values of d occur in every fiber unless the world set is restricted. So the answer to the question is the second branch: **threading changes which worlds a record value certifies as detection worlds**, not just how many worlds share a value. No caveat of the form "the label is coarse but within one class" is available.

**Candidate discriminators**, smallest first, each judged as a well-posed function that would make d a function of the readout:
- **3.1 Charge sign of the flux: fails.** Loops of both orientations exist (#448 §2.2), so the sign of r doesn't fix d.
- **3.2 Parity of r/q: conditional.** d ≡ r/q − N (mod 2), so parity determines d iff every allowed closed loop has even crossing number. That would need a law forcing odd-n loops to fail exact closure, e.g. a topologically fixed handle holonomy h with Hol(loop) = h^n and enclosed curvature forced trivial. Nothing in the framework fixes that. Under R-frame the frame lift on the handle class is set by the world's spin structure (world data; Geometry's rewording of Literature's #447 P5), and the closure condition for a virtual pair (expected −1: #431 §3b(b) and §3c, a Creative Lead reading; David's 11:17 AM ruling, #431 §3b(a), covers only loops already expected at −1 and does not set the expected value) vs a real loop differs, so even the sign of the requirement depends on V1/V2. Under R-geon the handle S¹×S² is a non-spinorial (tensorial) summand, so the core's 2π class supplies no sign there. **Not established; T2 flag:** a holonomy law chosen so parity works would be tuning to the target.
- **3.3 Multiplicity |n|: not readable.** The flux reads only the total N; individual n_i aren't recorded.
- **3.4 Conditioning on N1 on X: fails as a readout.** N1 says that when d = 1 no loop uses X, but loops crossing S elsewhere still contribute, and the record doesn't say which edge crossed. It narrows the false-negative worlds to those with Z ≠ X; it doesn't remove them.
- **3.5 Time orientation: fails.** S's world-tube is timelike, so crossing S is spatial motion; a closed circulation can cross it net ±1 with any time orientation, and with CTCs adopted there's no global time function to order the crossing against P's (#448 §3(c)).
- **3.6 Imposing (B) (#448 §2.4): separates.** Under (B1)+(B2), N(w) = 0 for every world, so r = q·d and the fibers are pure. It's a restriction on the world set, chosen to make the record work: fails T2 unless derived, and CTCs through the handle break (B2).
- **3.7 Edge-indexed entry on X: separates.** "X carried q" reads d directly. It's a new write mechanism, i.e. the write rule (not adopted), not charge without charge (#448 §3(b)).

**Outcome:** no discriminator is both well-posed on the full adopted world set and fixed for independent reasons. Failure recorded, with (B), the parity law and the write rule named as the three inputs that would each separate.

### 4. (W) remark
Under (W) (carried loops only, #436 §4a, Geometry's 3:51 PM reading, not a ruling), #444 §4 already reduces the funnel to Reading A, so the funnel claim is (F) only. The confound itself survives under (W): a V1 threading pair is carried by its own members, so it is a loop of the world and contributes n_i to N. Nothing in §2 changes.

### 5. Honest flags
- The record map's fibers mix detection classes under V1 and V2 alike; the funnel's record is not a coarse-grained detection label without an added input.
- The decomposition r = q(d + N) relies on #444 §3's design condition (C3 crosses S net 0), stated there rather than derived.
- §2.4's "exact closure leaves every n available" assumes enclosed curvature on a threading loop isn't forced; if a world forces it, §3.2's parity route opens, still needing a holonomy law (T2 flag).
- N1 is a modelling assumption (#444 §1); the false-negative argument uses it only to move the loop off X.
- No statement about how often confound worlds occur: that needs a weight on worlds, which #447 shows isn't fixed (μ open; countability assumed, open).
- Which-route vs which-world is unaffected: the confound concerns presence (d), not route; route independence is untouched.

## Guardrails

Classical only. No Born claim, no probability rule. μ open; (M1) untouched at L3. 1(a) and the write rule not adopted. CTCs adopted (David, 2:27 AM ET 2026-10-14, relayed via Physics Lead, not signed). Spin-½ adopted for fermions only (David, 11:24 and 11:26 AM ET 2026-10-15, #431 §3c). Species conservation not adopted. R-geon/R-frame and (F)/(W) open. Both virtual-pair definitions (V1, V2) open for David. No ħ, no measure, no weight, no phase rule. Nothing adopted. Nothing in versions/ or papers/.

## Ledger row and change log

| Row | Item | Content | Source | Status | Notes |
|---|---|---|---|---|---|
| L191 | Threading and the detection set (threading-detection-set.md; Geometry draft, 2026-10-19, tasked by Physics Lead (Lead tasking, relayed; not David's words)) | Record r = q(d + N): fibers mix detection and non-detection worlds (false positive d = 0, N = +1; false negative d = 1, N = −1); exact closure constrains holonomy, not crossing number; V1 and V2 both permit the confounds (V2 renames the loop as real; CTCs supply it); charge sign, \|n\|, N1, time orientation fail; (B), a parity law, or an edge entry on X (write rule) would separate, none passes T2 | Geometry (draft) | analysis, not adopted | Under (F); R-geon and R-frame alike; V1/V2 open for David; cite mismatch CC1 applied (Geometry accepted); μ open; (M1) untouched |

### Change log

- 2026-10-19: note created by Creative Lead from Geometry's workstream (E) draft (comment 6274437319 on #448); ledger row L191. Cite check against #427 5bd192e, #428 608af08, #445 9766fd3, #444 6491918, #448 0376c18: one mismatch, CC1 (rulings cited to #444 §3a/§3b, recorded in #431 §3a/§3b), flagged, not applied. Banned-word grep clean.
- 2026-10-19: CC1 applied as proposed (rulings cited to #431 §3a/§3b); Literature W2-1 to W2-3 applied verbatim (comment 6274505368): #436 §4a labelled Geometry's 3:51 PM reading; the expected −1 labelled a Creative Lead reading, with David's 11:17 AM ruling scoped; P5 labelled Geometry's rewording of Literature's #447 P5. Geometry accepted all four. Nothing adopted.
