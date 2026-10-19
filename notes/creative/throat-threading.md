# Can a threading virtual pair be told apart from route X at the throat? (Geometry draft, workstream (D))

**Do not merge. Paper only.** Geometry draft, 2026-10-19, tasked by Physics Lead (Lead tasking, relayed; not David's words). Stacked on #444 (creative/detector-funnel-record at 8e8000e). Pins: #444 8e8000e, #445 9766fd3, #428 608af08, #427 5bd192e. #444, #445, #428 and #427 are not edited. Nothing is adopted. Both virtual-pair definitions (V1, David 5:14 PM; V2, Claude 024) stay open for David.

## Plain summary (for David)

Mostly a clean negative: charge, orientation, CTCs and the edge lemma don't exclude a virtual pair threading the detector throat, because one member circling the handle changes the flux by q. The only exclusion is a bridge condition (X is the only edge crossing S and lies on no cycle); it is a restriction on which worlds count, not a derivation, and imposed as a law it fails T2; CTCs through the handle break it. Separating the two needs more structure: a write on X (the write rule is not adopted), a second handle, or a global time function, which is in tension with CTCs. This is under (F), and holds for both R-geon and R-frame.

## Known error (inherited from #444; now corrected in both)

#444 says "cycle rank 3, cycles C1, C2, L, C3", which lists four cycles for a rank-3 basis (7 edges, 5 vertices), so one of the four is a sum of the others. Geometry's corrected basis is now in §2.4 of the draft below: A basis is C1, C2 and a new C3 = E0 · Yb · Ya⁻¹; L = C1 · C2⁻¹ in cycle space (taking A1, A2 as L's two arcs from a to b), so {C1, L, C3} is an equivalent basis. This is consistent with Hol(C1) = −Hol(C2) in #444 §4 (with Hol(L) = −𝟙). No other conclusion changes. #444 is now corrected at its new head f2a5d0f (Claude job 030 R6, applying Geometry's correction from #444 comment 6273048224), merged forward into this branch.

## Cite check (Creative Lead; M1–M3 accepted by Geometry and applied)

Cite check against pinned heads (#427 at 5bd192e, #428 at 608af08, #445 at 9766fd3). Mismatches were flagged with OLD (Geometry's text) and a suggested NEW; Geometry accepted M1–M3 and they are applied in the draft below.

- **#428 §4 item 2 (V2):** matches. "A virtual pair is then one that writes no entry anywhere (Claude 024)." ✓
- **#428 §5:** cited as a pin only; the §5 sentence exists at 608af08 ✓.
- **#427 weight gap:** matches (#427 §1/§4, "honest gap") ✓.
- **#445 "a loop crossing S net n times leaves nq":** matches in substance (#445 at 9766fd3: "crosses S net n ≠ 0 times leaves a Gauss-flux entry nq") ✓.
- **M1, V1 (#427 §3a).** #427 records David's 5:14 PM words as "appear together and then disappear together" (adopted 5:17 PM); "exact" is a Creative Lead reading there, and "closed circulation" is not #427's wording.
  OLD: `V1: the 5:14 PM exact-closure definition, a closed circulation created and annihilated as a pair`
  NEW: `V1: David's 5:14 PM definition (#427 §3a, adopted 5:17 PM): a pair that appears together and then disappears together (exact by definition, a Creative Lead reading there; "closed circulation created and annihilated as a pair" is Geometry's graph rendering)`
- **M2, #428 §6a(c)2.** §6a(c)2 says the separation of a and b is solved per world, not that each world's whole graph is.
  OLD: `(B) is about each world's graph, which is solved per world (#428 §6a(c)2).`
  NEW: `(B) is about each world's graph, which is world data; the attachment points a and b are solved per world (#428 §6a(c)2).`
- **M3, #445 and the curvature branch.** #445 at 9766fd3 gives "either such threading must be excluded, or the record needs further structure not yet given"; it does not name the branch where L's −1 comes from enclosed curvature. That branch is #444 §5 only.
  OLD: `That is the second branch of #444 §5 / #445, where L's −1 comes from enclosed curvature.`
  NEW: `That is the second branch of #444 §5, where L's −1 comes from enclosed curvature (#445 records only the exclusion option).`

## Geometry's draft (verbatim from https://github.com/nous-clawds4/physics/pull/444#issuecomment-6272990835)

> Attribution: Geometry draft, 2026-10-19, tasked by Physics Lead (Lead tasking, relayed; not David's words). Text below is Geometry's, unedited apart from heading levels, M1–M3 (accepted by Geometry) and Geometry's corrected cycle basis in §2.4.

**Geometry, workstream (D): can a threading virtual pair be told apart from route X at the throat?** Draft note text for Creative Lead to open as a stacked do-not-merge follow-up, separate from #444. Paper only; nothing is adopted. Pins: #444 at 8e8000e, #445 at 9766fd3; #428 §4 item 2 and §5; #427, both virtual-pair definitions kept open (V1: David's 5:14 PM definition (#427 §3a, adopted 5:17 PM): a pair that appears together and then disappears together (exact by definition, a Creative Lead reading there; "closed circulation created and annihilated as a pair" is Geometry's graph rendering); V2: "writes no entry anywhere", Claude 024). Which governs is David's call. Classical only, no Born claim, μ open, (M1) untouched, 1(a) and the write rule not adopted, CTCs adopted, spin-½ adopted for fermions, species conservation not adopted, R-geon/R-frame open, (F)/(W) open. No ħ, measure or phase rule appears.

### Result in one paragraph
**Mostly negative.** Charge conservation, orientation and CTCs don't exclude a threading pair. The edge lemma (N1) bars a loop from X only in worlds where the route chain is on X. The one structural exclusion is combinatorial: if X is the only edge of the world that crosses S, and X is a bridge of that world's graph, then every closed circulation crosses S net 0 and no pair threads. This is #444's minimal graph, where X lies on no cycle. But S is non-separating, so the manifold always allows a return path. The bridge condition is a restriction on which worlds are counted, not a consequence of the framework. It also requires L not to thread S. Under V2 a threading pair writes an entry, so by definition it isn't virtual; the confound comes back as a real threading loop. Within one handle, every candidate for added record structure is either not append-only (it needs a write rule, not adopted), adds topology (a second handle), or needs a time order (in tension with adopted CTCs). None is fixed for independent reasons (T2).

### 1. Setting
The throat surface S is a non-separating surface in the fixed handle. #444 §3: when a charge q crosses S net once and doesn't return, the Gauss flux through S changes by q. That entry is topological and append-only. #445: a loop crossing S net n times leaves nq. On a graph, the net crossing of a circulation c is Σ over edges e crossing S of ±c(e), with the sign from orientation. The reading is (F) throughout. Under (W), #444 §4 already reduces the detector to Reading A, so the question carries no constraint there. R-geon/R-frame: nothing below uses spin or the frame lift, so the argument holds under both readings.

### 2. Candidate exclusions
**2.1 Charge conservation: no.** A pair has net charge 0, but the flux counts the crossings of one member. Create a pair at a point p, carry +q around the handle across S once, carry −q along a path that doesn't cross S, and annihilate them. The net crossing of S by charge is +1 (the −q member contributes 0), and the flux changes by +q. Charge is conserved at every vertex. The flux is a winding number, not a charge total, so conservation doesn't constrain it.

**2.2 Orientation: no.** Reversing the loop gives −q. Both signs occur. P's record is a fixed sign ±q (#444 §3), and a pair with n = ±1 of the matching sign reproduces it exactly.

**2.3 Edge lemma (N1): only on X, and only when X is occupied.** The lemma says no virtual loop shares an edge with the route chain. In a world where P exits through X, X is carried at value 1, so no loop uses X. A threading loop that crosses S on a different edge isn't touched. In a world where P doesn't arrive, X is empty and N1 doesn't bar a loop on X either. **Result: N1 bars it only if the loop uses X and the chain is present.**

**2.4 Funnel geometry: conditional exclusion (bridge condition B).** Suppose (B1) X is the only edge of the world that crosses S, and (B2) X is a bridge of the world's graph. A circulation on a bridge is 0 (cut the bridge; conservation across the cut forces c(X) = 0). So every closed circulation crosses S net 0, and no pair threads, under V1 or V2. #444 §2's graph satisfies (B): X lies on no cycle (cycle rank 3). A basis is C1, C2 and a new C3 = E0 · Yb · Ya⁻¹; L = C1 · C2⁻¹ in cycle space (taking A1, A2 as L's two arcs from a to b), so {C1, L, C3} is an equivalent basis. **Caveats:**
- S is non-separating, so the manifold contains a closed curve crossing S once. Any world that includes a return path from X's far end back to the source side breaks (B2). (B) excludes such worlds; nothing excludes them. That makes it a restriction on the world set, an arbitrary assumption against T2 unless it's derived.
- (B1) requires L not to thread S. That is the second branch of #444 §5, where L's −1 comes from enclosed curvature (#445 records only the exclusion option). Under #431 §3 (iii), where L threads S, (B1) fails by construction.
- (B) is about each world's graph, which is world data; the attachment points a and b are solved per world (#428 §6a(c)2). The detector fixes x, X and the throat, not the absence of other edges in the handle.

**2.5 CTCs (adopted): neutral to slightly worse.** The argument in 2.4 is graph-theoretic and doesn't use time order, so CTCs don't break it. They don't help either. A CTC through the handle is exactly a return path, so it breaks (B2). CTCs being adopted therefore makes (B2)-violating worlds part of the admitted class.

**2.6 V2 by definition.** Under V2, a threading loop writes flux, so it isn't a virtual pair. That doesn't separate anything. The same loop is then a real threading circulation with the same ±q, and the confound comes back under a different name. Under V1 it stays a virtual pair, and #445 applies as written.

### 3. Smallest added record structure (if (B) is not imposed)
Each candidate, with its cost:
- **(a) A second surface S′ in the same handle: fails.** Any S′ homologous to S is crossed net n times by the same loop (homology invariance), so it duplicates the reading. A non-homologous S′ needs a second handle that X threads and the pair doesn't. That is added topology, a design choice (T2 flag), and a pair could thread that handle too, which puts the problem back one level.
- **(b) An edge-local write on X: not append-only.** Flux through a patch of S around X's piercing point isn't topological, since only the total over the closed S is fixed by Gauss. An edge-indexed entry ("X carried q") is a new write mechanism, which amounts to the write rule (not adopted). It is the smallest structure that separates, but it isn't charge without charge.
- **(c) Time order of the flux change relative to occupation of Ya/Yb: needs a time function.** "Flux changed after x was occupied" requires an order on events across the graph. Classical (F) worlds with adopted CTCs have no global time function. A local causal order along the chain exists, but a threading pair can be placed at any position in it. The approach also needs a record of the occupation of Ya/Yb, and #444's condition 4 requires Ya and Yb to write nothing that differs between them. A presence-only write at x would be (b) again. T2 flag: the time function and the occupation write are both inputs added for this purpose.
- **(d) Imposing (B) as a law: it separates, but it is chosen to hit the target.** That fails T2 as it stands. It would pass only if (B) followed from something independent, e.g. the lock forbidding return paths in the handle. No such derivation exists.

**Ranking by added structure (no recommendation):** (b) adds one per-edge entry but requires the write rule; (d) adds nothing to the ledger but restricts the world set; (a) adds a handle; (c) adds a time function and an occupation write.

### 4. Honest flags
- The bridge condition (B) is the only structural exclusion, and it's a restriction, not a derivation. It also fixes #444 §5's branch choice (L not threading S).
- CTCs (adopted) supply return paths, so they work against (B2).
- Under V2 the exclusion is definitional and moves the confound rather than removing it.
- Every separating structure either adopts something not adopted (write rule, time function) or adds topology. None passes T2 as it stands.
- N1 is still a modelling assumption (#444 §1).
- #427's weight gap isn't touched. Nothing here weights worlds with (B) against worlds without it, and that weighting would be needed to say how often the confound occurs (μ open).

## Guardrails

Classical only. No Born claim, no probability rule. μ open; (M1) untouched at L3. 1(a) and the write rule not adopted. CTCs adopted (David, 2:27 AM ET 2026-10-14, relayed via Physics Lead, not signed). Spin-½ adopted for fermions only (David, 11:24 and 11:26 AM ET 2026-10-15, #431 §3c). Species conservation not adopted. R-geon/R-frame and (F)/(W) open. Both virtual-pair definitions (V1, V2) open for David. No ħ, no measure, no phase rule. Nothing adopted. Nothing in versions/ or papers/.

## Ledger row and change log

| Row | Item | Content | Source | Status | Notes |
|---|---|---|---|---|---|
| L190 | Throat threading (throat-threading.md; Geometry draft, 2026-10-19, tasked by Physics Lead (Lead tasking, relayed; not David's words)) | Mostly negative: charge conservation, orientation, CTCs and the edge lemma don't exclude a virtual pair threading the throat; only exclusion is bridge condition (B) (X the only edge crossing S, a bridge), a restriction on worlds, not a derivation (fails T2 as a law; CTCs break it); separating needs a write on X (write rule not adopted), a second handle, or a global time function (tension with CTCs) | Geometry (draft) | analysis, not adopted | Under (F); R-geon and R-frame alike; V1/V2 open for David; cite mismatches M1–M3 applied (Geometry accepted); #444 cycle basis corrected here (Geometry), #444 itself flagged, unedited; μ open; (M1) untouched |

### Change log

- 2026-10-19: note created by Creative Lead from Geometry's workstream (D) draft (comment 6272990835 on #444); ledger row L190. Cite check against #427 5bd192e, #428 608af08, #445 9766fd3: mismatches M1 (V1 wording vs #427 §3a), M2 (#428 §6a(c)2 scope), M3 (#445 does not name the curvature branch) flagged as OLD/NEW for Geometry, not applied. Known error inherited from #444 (four cycles listed for a rank-3 basis) noted; a PR comment flags it on #444.
- 2026-10-19: M1, M2 and M3 applied to Geometry's draft as proposed (Geometry accepted all three). §2.4's four-cycle phrase "(cycle rank 3, cycles C1, C2, L, C3)" replaced with Geometry's corrected basis (C1, C2, C3; L = C1 · C2⁻¹; {C1, L, C3} equivalent), adapted to the sentence. Known-error note updated: consistent with Hol(C1) = −Hol(C2) in #444 §4; no other conclusion changes; #444 unedited. Geometry passes #448 with M1–M3 applied.
- 2026-10-19: merged #444 forward at f2a5d0f (Claude job 030 R1–R6, S2, S3, S5 applied there). Known-error note updated: #444 is now corrected at f2a5d0f. No change to Geometry's (D) draft.
