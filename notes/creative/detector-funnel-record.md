# A detector-fixed funnel record that leaves L virtual (Geometry draft, workstream (A))

**Do not merge. Paper only.** Geometry draft, 2026-10-19, tasked by Physics Lead (Lead tasking under David's delegation, relayed; not David's words). Background: David asked Physics Lead for full-blast physics until 8 PM ET 2026-10-19 (relayed by Physics Lead, not signed; paraphrase, no verbatim words recorded; unverified by Literature, no original seen; a work instruction, not a ruling on content; no hold level stated). Stacked on #438 (creative/fermion-is-fs-geon at b61ccfa). Nothing here is adopted.

## Plain summary (for David)

Before, every design that recorded the detection cost the detector loop L its virtual status. Geometry's lemma says why: with a conserved unit charge and at most one particle per edge, no virtual loop can share an edge with the route chain. Geometry's candidate routes the chain around L instead, through a detector-fixed funnel a→x, b→x, then an exit X through the fixed handle's throat; the Gauss flux write of the charge q on X is the same in both route worlds and reads presence only, so L stays virtual and keeps its expected −1. This holds under (F) only. The costs: a new cycle C3 with no expected value; under (W) it reduces to Reading A; the funnel is detector design, not a law; and #427's weight gap is untouched. Geometry also flags that a virtual pair threading the throat leaves flux too, so #428 §5's "a virtual pair writes none" needs a qualifier; that is recorded as a flag for the stack, and #428 is not edited.

## Geometry's draft (copied faithfully from https://github.com/nous-clawds4/physics/pull/438#issuecomment-6272583462)

> Attribution: Geometry draft, 2026-10-19, tasked by Physics Lead (Lead tasking under David's delegation, relayed; not David's words). Text below is Geometry's, unedited apart from heading levels.

**Geometry, workstream (A): a record fixed by the detector that leaves L virtual.** Draft note text for Creative Lead to open as a stacked do-not-merge PR. Paper only; nothing is adopted. Classical only, no Born claim, μ open, (M1) untouched, 1(a) and the write rule not adopted, CTCs adopted, spin-½ adopted, species conservation not adopted, R-geon/R-frame open, (F)/(W) open. No ħ, measure or phase rule appears.

### Result in one paragraph
**Outcome (i): a smallest candidate exists, but only under (F).** The record and the detector's −1 don't have to share edges. Keep L as a closed virtual circulation that never carries the routes' flow. Add a detector-fixed exit: a vertex x joined to the arrival points a and b by edges Ya and Yb that avoid L's arcs, and an outgoing edge X from x that passes once through the fixed handle's throat. P's chain then writes a Gauss-flux record of ±q on X, the same in both route worlds. L keeps its virtual status and its expected −1. Under (W) the record still exists, but the detector then constrains nothing (Reading A). The mechanism doesn't touch #427's gap: nothing here gives exact-closure worlds weight.

### 1. Why #431/#436 lost L (lemma)
**Setting:** conserved unit charge, and at most one particle per edge (Geometry N1, a modelling assumption).

**Lemma.** If an edge carries the route chain, no virtual loop can use that edge.

**Proof.** A virtual loop is a pure circulation c on its arcs. On a shared arc the value would be 1 + c, with both 1 + c and c in {0, 1}, so c = 0. ∎

So any design where the route chain leaves through L's arcs (#431 wiring, #436 zigzag) costs L its virtual status. The only escape is for the route chain to avoid L's arcs entirely. That is a geometric fact, not a choice.

### 2. The candidate (smallest graph)
- **Vertices:** a and b (on L, where routes 1 and 2 arrive), x (the exit junction), X's far end, and the source.
- **Edges:** routes 1 and 2 (E0 = route 1 reversed, then route 2), A1, A2, Ya (a→x), Yb (b→x), X.
- **Cycle rank:** 5 vertices (source, a, b, x, X's far end) and 7 edges (route 1, route 2, A1, A2, Ya, Yb, X) give 7 − 5 + 1 = 3. The cycles are C1, C2, L and a new C3 = E0 · Yb · Ya⁻¹. X lies on no cycle.
- **Flow in the route-1 world:** route 1 → a → Ya → x → X, value 1. A1, A2 and Yb carry 0 route flow. L carries its own circulation, created and annihilated as a pair, so it stays virtual under the 5:14 PM definition. The route-2 world is symmetric through b and Yb.
- **Detector-fixed:** x, X and the throat are part of the detector, fixed before phases are compared, as #436 condition 1 requires. a and b remain solved per world (#428 §6a(c)2).
- **Well-posedness item:** a and b are vertices shared by L's members and the route chain. The model must say that sharing a vertex is not an interaction (no annihilation at a or b). Here it is taken not to be. Otherwise the design falls back to #436.

### 3. The record (#388 write, classical)
**Charge without charge (Wheeler).** When a charge q crosses a non-separating throat surface S of a fixed handle and doesn't return, the flux through S changes by q. By Gauss's law it stays at that value: a topological, append-only entry next to the fixed handle. That is #388's write, as in Claude 026 #431 R3.

The record is placed on X, so it is:
- **Route-independent:** X is common to both worlds and crosses S once, so the record is +q in both. There is no which-way information.
- **Presence-only:** it reads P's charge and presence, not the arrival time, Ya versus Yb, or P's frame or sign. This meets #436 condition 2 and Claude 026 S2.
- **Persistent:** it uses charge conservation (Maxwell, once matter is coupled), not species conservation. It lasts as long as P doesn't pass back through S, which meets the "more than never" bar.
- **Meets #436 condition 3:** the signed throat crossing is the same in both worlds.
- **Condition 4 (4-momentum):** Ya and Yb must write nothing that differs between them. That is a design condition on the detector, stated rather than derived.

### 4. What each reading gives
- **(F) frame graph:** every edge is a transport path, so C1, C2, L and C3 all bind under the 10:48 AM ruling. L is still virtual, so its expected −1 survives (#431 §3b), and with it Hol(C1) = −Hol(C2) up to conjugation (#428 §6a(c)1). This is the first design in the stack that keeps the −1 and has a detector-fixed record. **New cost:** C3 needs an expected value under 11:17 AM, and nothing supplies one yet. It is world data, like the solved attachment points.
- **(W) carried loops only:** the carried subgraph is the open path route → a → Ya → x → X, plus L's own carried circulation. L binds itself, but no carried cycle contains a route, so the detector asks nothing of the routes. The record exists, but this is Reading A (#431 §3 (ii)).
- **R-geon versus R-frame:** nothing in §1–§3 depends on the choice. The record is a flux datum, not a sign. If P is topological, L's pair vertices contain Geroch CTCs (#436 R3), and pair creation always passes #434's rule.

### 5. A flag the stack should check (Geometry, not a ruling)
A virtual pair whose loop threads the handle class (crosses S net once) leaves throat flux ±q after it annihilates. That is the same charge-without-charge mechanism. So #428 §5's "a virtual pair writes none" holds only if L does not thread S. If L does thread S (one route to its −1, #431 §3 (iii)), L writes flux in every world whether or not P arrives. That entry is not a detection record. The detector's ledger then has a baseline set by L, and P's record is the extra ±q on X. So the record criterion must read the change due to X, or L must be kept from threading S, with its −1 coming from enclosed curvature instead.

### 6. What this doesn't do
- It doesn't give exact-closure worlds weight (#427's honest gap). No count or measure is proposed.
- It doesn't fix C3's expected value.
- The funnel (x, Ya, Yb, X through the throat) is detector design, which the detector must be shown to have. It is not a law.
- (F) versus (W) stays David's call. This design only shows that under (F) the record and the −1 are compatible.


## Citations (Creative Lead; outside Geometry's text)

- Charge without charge / wormhole flux charge: C. W. Misner and J. A. Wheeler, "Classical physics as geometry", Ann. Phys. 2, 525–603 (1957), doi:10.1016/0003-4916(57)90049-0 [V-meta; text not read]; J. A. Wheeler, Geometrodynamics (1962) [V-meta, publisher and pages not checked]. The Gauss-flux append-only record on X is Geometry's argument (with Claude 026 #431 R3), not a result of these works.
- Prior art only (quantum; nothing imported): Scully, Englert, Walther, Nature 351, 111 (1991), doi:10.1038/351111a0; Englert, PRL 77, 2154 (1996), doi:10.1103/PhysRevLett.77.2154 (which-way and complementarity); Wick, Wightman, Wigner, Phys. Rev. 88, 101 (1952), doi:10.1103/PhysRev.88.101; Aharonov, Susskind, Phys. Rev. 155, 1428 (1967), doi:10.1103/PhysRev.155.1428 (charge superselection). Literature found no published topological-flux which-way-free record.

## Guardrails

Classical only. No Born claim, no probability rule. μ open; (M1) untouched at L3. 1(a) and the write rule not adopted. CTCs adopted (David, 2:27 AM ET 2026-10-14, relayed via Physics Lead, not signed). Spin-½ adopted for fermions only (David, 11:24 and 11:26 AM ET 2026-10-15, #431 §3c); Geometry's "spin-½ adopted" means this. Topology gives only the ±1 lift. (F) is not adopted; this draft is conditional on it. Species conservation not adopted. R-geon/R-frame open; (F)/(W) open. No ħ, no measure, no phase rule. The #428 §5 qualifier is a flag for the stack only; #428 is not edited here. Nothing in versions/ or papers/.

## Ledger row and change log

| Row | Item | Content | Source | Status | Notes |
|---|---|---|---|---|---|
| L187 | Detector-fixed funnel record (detector-funnel-record.md; Geometry draft, 2026-10-19, tasked by Physics Lead (Lead tasking under David's delegation, relayed; not David's words)) | Lemma: with a conserved unit charge and at most one particle per edge, no virtual loop shares an edge with the route chain. Candidate: funnel a→x, b→x, exit X through the fixed handle's throat; Gauss flux write of q on X route-independent, presence-only; L stays virtual and keeps its −1; under (F) only | Geometry (draft) | candidate, not adopted | Costs: new cycle C3 with no expected value; under (W) reduces to Reading A; funnel is detector design, not a law; #427 weight gap untouched. Flag for the stack: a virtual pair threading the throat leaves flux, so #428 §5 'a virtual pair writes none' needs a qualifier (#428 not edited). R-geon/R-frame and (F)/(W) open; species conservation not adopted; 1(a) and write rule not adopted; CTCs adopted (2:27 AM ET 2026-10-14, relayed, not signed); spin-½ adopted for fermions only (#431 §3c); (F) not adopted, candidate is conditional on it; μ open; (M1) untouched |

### Change log

- 2026-10-19: note created by Creative Lead from Geometry's workstream (A) draft (comment 6272583462 on #438); ledger row L187 (L186 taken by creative/decision-brief-oct19, #442). Stacked on #438 at b61ccfa.
- 2026-10-19: Literature M2-1 to M2-4 applied (comment 6272868316 on #444): David background labels, Citations section, CTC and spin-½ labels in Guardrails and L187. Geometry nit applied to the plain summary ('keeps its expected −1'); Geometry's verbatim draft unchanged. Nothing adopted.
