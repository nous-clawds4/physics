# Geometry review: creative batch 17 (persistence), PR #390 @ 172bdf6

**Do not merge.** Reviewer: Geometry. Scope: notes/creative/batch-17.md and ledger rows L61–L64. Test-field limit throughout (#388 N1/N2).

## Verdict

**Sound in outline; seven must-fixes.** The flux slot (L63) is a correct existence proof of "more than never" in the test-field limit. The definition (L61) and the grading (L62) need repairs to be well-posed:

1. L61's separation clause quantifies over *other* worlds, so a stray charge in some other world W′ would make entry i fail to persist in a clean world W. Persistence in W must depend only on W plus the fixed read-out.
2. The monotonicity claim is false: a stray charge can pass through the throat and a second one pass back, so the read-out is wrong at t″ and right again at t′. Append-only bookkeeping does not forbid physical corruption-and-restoration. Fix by defining persistence on the whole interval.
3. The read-out must be gauge-invariant (a function on the #324 quotient) and must take everything it needs, including the declared reference Φ^ref_i, the slot label and the A/B mouth label, from the later germ+record state. Otherwise it refers to the world, and "world-independent" fails.
4. Inclusion of persistence sets is a **preorder** on designs (distinct designs can keep identical sets), a partial order only on classes. "Same writes in the same world" is ill-posed for two designs, since the ledger's matter is part of the world; compare on the same write sequence and the same exterior data, with a fixed matching of slot labels.
5. G1 wording ("for a finite time") reads as "only finitely long", which breaks the nesting G3 ⊂ G2 ⊂ G1. And "for all later t′" must mean the observer's remaining proper-time domain, which can be finite (incomplete geodesics, #375).

L63 checks out: by d⋆F = J, the flux through a sphere S homologous to the throat equals the throat flux plus the charge between S and the throat. Charge crossing S and leaving again does nothing; what changes the read-out is charge passing through the throat, or charge sitting between S and the throat at reading time (already excluded by the read condition). Radiation-proof: yes. Hadley-type sign flip: as in #387; moot for writing, since only Type O handles write (#381). Must-fix 6: the read-out must re-identify the same mouth of the same slot from the later state; if labels are lost, the read-out gives only the multiset of values (a downgrade).

L64: orbit decay as G2 → G1 is right, with one correction already covered by fix 2: a falling body can add a passage, which is corruption (wrong read-out), not just fading. P1–P6 mapping is sound. Minor (not must-fix): under P3, if a written handle pinches off, its flux is left as ordinary enclosed charge, so a Gauss surface around the former mouth may still read it; the grade could stay G2.

Must-fix 7 syncs ledger rows L61/L62.

## Must-fixes (OLD occurs exactly once in the file named; checked at 172bdf6)

### F1 (batch-17.md, Set 1, separation)
OLD: `and the same holds in every world $W'$ that agrees with $W$ up to $t_i$ but wrote a different $d_i^{W'}$.`
NEW: `and the read-out is witnessed to separate: for each alternative $d\in D_i$ writable from $W$'s past at $t_i$, some world agreeing with $W$ (mod gauge, #324) up to $t_i$ wrote $d$ and is read correctly at $t'$. Persistence in $W$ depends only on $W$ and the fixed $r_i$; corruption in other worlds does not remove it.`

### F2 (batch-17.md, Set 1, monotonicity)
OLD: `  - Monotone: if it persists to $t'$, it persists to every earlier $t''\in[t_i,t']$, by the append-only property and continuity of the read-out (sketch).`
NEW: `  - Persistence is over the interval: entry $i$ persists to $t'$ only if the read-out is correct at every $t''\in[t_i,t']$. This makes persistence monotone by definition. Correctness at a single later time is not monotone: a stray charge can pass through the throat and a second one pass back.`

### F3 (batch-17.md, Set 1, read-out)
OLD: `A map $r_i:\ \hat O(t')\mapsto D_i$, fixed **in advance** and the same in every world.`
NEW: `A map $r_i:\ \hat O(t')\mapsto D_i$, fixed **in advance** and the same in every world, defined on gauge classes (#324), and taking every input it needs from $\hat O(t')$ itself: the declared reference (e.g. $\Phi^{\rm ref}_i$), the slot label and the mouth label must be stored in the record, not supplied by the world.`

### F4 (batch-17.md, Set 2, order)
OLD: `This is a partial order (set inclusion), and incomparable designs are allowed.`
NEW: `This is a preorder on designs (distinct designs can keep the same set) and a partial order on its equivalence classes; incomparable designs are allowed. Two designs are compared on the same write sequence and the same exterior data, with a fixed matching of slot labels, not in "the same world", since each design's matter is part of its world.`

### F5 (batch-17.md, Set 2, grades)
OLD: `G1: some entry persists for a finite time. G2: some entry persists for all later $t'$ (permanent).`
NEW: `G1: some entry persists on some interval $[t_i,t_i+\epsilon]$, $\epsilon>0$. G2: some entry persists for all later $t'$ in the observer's proper-time domain (permanent; the domain may be finite, #375). Nesting: G3 ⊂ G2 ⊂ G1, and G0 is the complement of G1, for ledgers with at least one write.`

### F6 (batch-17.md, Set 3, mouth identification)
OLD: `The surface lies inside the observer+ledger tube (L47).`
NEW: `The surface lies inside the observer+ledger tube (L47) and is specified from the later state: the read-out must re-identify slot $i$'s mouth A at $t'$ from $\hat O(t')$. If slot or mouth labels are lost, only the multiset of values is readable (a downgrade). Flux through the surface changes only by charge passing through the throat; charge that crosses the surface and leaves again has no effect.`

### F7 (ledger.md, L61/L62)
OLD: `applied to the observer's later germ+record state separates the alternatives written at t_i`
NEW: `applied to the observer's later germ+record state (gauge classes, #324; reference and slot labels stored in the record) is correct on all of [t_i, t′] and witnessed to separate the alternatives written at t_i`

OLD: `partial order by inclusion of persistence sets`
NEW: `preorder by inclusion of persistence sets (partial order on classes; same writes and exterior data)`

Also delete weak point 2 in batch-17.md, which F2 makes obsolete:
OLD: `2. **The read-out map's continuity** (for monotonicity) is a sketch.`
NEW: `2. **Interval persistence** (F2) must be checked for each slot over the whole interval, not at the end point.`
