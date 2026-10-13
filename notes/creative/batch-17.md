# Batch 17: persistence of the ledger (Creative Lead; do not merge)

**Status.** Exploration only, under David's rulings (all relayed by Physics Lead, not signed), including 9:28 PM (the lock stays; the append-only matter-and-flux ledger next to fixed handles is the main line; #388) and 5:00 PM (classical only). No Born rule, no probability, no measure; (M1) unchanged at L3. **Test-field limit throughout** (#388, Geometry's T_ab point). Citations are unchecked unless verified in earlier reviews. Nothing goes into `versions/` or `papers/`. Stacked on batch 16 (#385). The ledger concept note is #388, which branches off main. Ledger rows L61–L64.

**David (10:37 PM ET 2026-10-12, relayed by Physics Lead, Physics Lead chat, not signed; verbatim):**
> On the topic of persistence, we might adopt the position that some pieces of matter are highly effective ledgers, other pieces of matter might be less effective, where more effective means that the matter keeps a record of many of its observations, and less effective means it keeps a record of fewer of them. So the fact that some observations don't persist should not be considered fatal to our endeavor. At this point, all we need is a clear model for what persistence means, how it happens, and that it can happen and is sufficiently well defined. Persistence doesn't need to happen all the time, everywhere; it merely needs to happen more than never.

---

## For David (plain summary)

- **What persistence means.** An entry written at time *t* persists until a later time *t′* if, at *t′*, the observer can still read it off from what it has then: it can tell "this was written" apart from "this was not written". That's the whole definition. It's a yes/no fact about each entry and each pair of times.
- **Better and worse ledgers.** A ledger is "more effective" than another if the set of entries it keeps contains the other's. This is a comparison of sets, not a percentage: no probabilities, no counting weights. Two ledgers can also be incomparable, and that's fine.
- **It happens more than never.** The electric flux through a wormhole handle is a clean example. A charged pulse that passes through the handle changes the flux by its charge, and radiation cannot undo that, since it carries no net charge; only another charge crossing the same mouth can change it. Read with a Gauss surface around one mouth, that entry persists **forever** in the idealised limit we work in.
- **Losses are grades, not failures.** Orbits that decay, handles that wobble, stray charges: each one makes some entries unreadable, which lowers the ledger's grade. None of them stops *some* entries from persisting. That is your "more than never".
- **Scope.** All of this is in the limit where the diary's own weight doesn't bend spacetime (the test-field limit). Hadley-type handles (time-flipping) need extra care.

---

## Set 1: what persistence means

**Plain summary.** An entry persists if, later on, the observer can still read it. "Read" means there is a definite rule turning the observer's later data into "written" or "not written", and the rule gets it right.

- **Setting** (#388 working design). An append-only diary with capacity $N$ fixed at the start: slots $i=1,\dots,N$, each a fresh, pre-placed body or handle, in the test-field limit. A write at $t_i$ sets slot $i$ to datum $d_i\in D_i$, measured relative to its reference: a passage count or a flux step relative to a reference rule fixed once, before the horizon (#388 S5). $d_i=0$ means "not written".
- **Observer's later data.** $\hat O(t')$: the germ + record state (L29), i.e. the germ of the observer+ledger tube at $t'$ (L47).
- **Read-out map.** A map $r_i:\ \hat O(t')\mapsto D_i$, fixed **in advance** and the same in every world. It must not be tuned to a world after the fact, or it would be a law of R by fiat.
- **Definition.** Entry $i$ **persists from $t_i$ to $t'$** in world $W$ iff $r_i(\hat O_W(t'))=d_i^W$, and the same holds in every world $W'$ that agrees with $W$ up to $t_i$ but wrote a different $d_i^{W'}$.
  - In other words, the read-out separates the alternatives written at $t_i$.
  - It is a property of (entry, $t'$, world), with no weights.
  - Persistence to $t'$ means the separation holds at every $t''\in[t_i,t']$ (a later opposite crossing can restore a corrupted read-out, so a single-time condition would not be monotone); with this interval definition, persistence to $t'$ implies persistence to every earlier $t''$.
- **Persistence set.** $P_W(t')=\{i:\ \text{entry } i \text{ persists to } t'\text{ in } W\}$.
- **Why append-only matters.** With one slot per write, losing slot $j$ cannot corrupt slot $i$. Persistence is entry-by-entry, and branches stay nested (#388 R1).
- **Status: live** (L61).

## Set 2: grading ledgers without probabilities

**Plain summary.** Compare ledgers by which entries they keep. If ledger A keeps every entry that B keeps (and maybe more), A is at least as effective. No numbers needed.

- **Order.** For two ledger designs $\mathcal L,\mathcal L'$ run on the same writes in the same world: $\mathcal L\succeq\mathcal L'$ at $t'$ iff $P^{\mathcal L}_W(t')\supseteq P^{\mathcal L'}_W(t')$. This is a partial order (set inclusion), and incomparable designs are allowed.
- **Across worlds.** $\mathcal L\succeq\mathcal L'$ **uniformly** iff the inclusion holds in every world reaching $t'$. Nothing is averaged.
- **Over time.** $\tau\mapsto P_W(\tau)$ is non-increasing among already-written entries (by the interval definition in Set 1). A ledger's **persistence profile** is the family of these sets.
- **Grades** (used in Set 4). G0: $P=\varnothing$ for all $t'>t_i$ (never persists). G1: some entry persists for a finite time. G2: some entry persists for all later $t'$ (permanent). G3: every entry persists permanently. These are ordered by inclusion of what they guarantee, **not** by fractions.
- **Explicitly excluded:** fractions of persisting entries, rates, likelihoods, typicality. Any of these needs a measure, which is parked (#383 guardrails).
- **Status: live** (L62).

## Set 3: existence: the handle flux persists (more than never)

**Plain summary.** Pass a charged pulse through a wormhole handle, and the handle's electric flux goes up by that charge for good. The observer reads it with a Gauss surface around one mouth. That entry is permanent in our idealised limit, so persistence happens at least once.

- **Slot.** One pre-placed one-universe handle per slot (#385 Set 1; append-only, #388), with flux reference $\Phi^{\rm ref}_i$ declared before the horizon.
- **Write.** A charged carrier of the single species $q_0$ passes through slot $i$'s mouth A. Then $\Phi_i-\Phi^{\rm ref}_i$ changes by $+q_0$ (or $-q_0$ through B; a graze gives 0) (#385 Set 3, #387).
- **Read-out.** $r_i=(\Phi_i-\Phi^{\rm ref}_i)/q_0\in\mathbb Z$, measured by a Gauss surface enclosing **exactly one** mouth, with no charge between the surface and the throat (#387). The surface lies inside the observer+ledger tube (L47).
- **Persistence [A, sketch].** $d\star F=J$. Off charges, the flux through any sphere homologous to the throat is constant. Radiation is sourceless and carries no net charge. So $r_i$ is unchanged for all $t'>t_i$ unless another charge crosses that mouth. **With no later crossing, the entry persists for all $t'$: grade G2.** Misner–Wheeler 1957 (V-text per #386): "the wormhole flux remains invariant. This constant of the motion represents the charge."
- **Separation.** Written ($r_i=\pm1$) and not written ($r_i=0$) give different read-outs, so the Set 1 condition holds.
- **Caveats.**
  - **Test-field scope.** Under the lock, the metric and total $T_{ab}$ on the tube are fixed, and a charge passage changes the current. So this is a test-field statement only (#388, Geometry's second pass).
  - **Hadley-type handles.** Not orientable or not time-orientable: the handle can carry charge of its own (Sorkin 1977; Diemer–Hadley 1999, per #386), and a time-reversing loop makes the carrier read −q (#387, sketch). The reference must absorb the intrinsic charge, and the sign convention must be fixed per slot. In forming hosts the diary handles are not Hadley-type anyway (#388 R3).
  - **Integrality** needs a single charge species (L58). Without it, $r_i$ is an exact real, and the entry still persists (G2), just not as an integer.
  - **Stray charge** crossing the same mouth corrupts slot $i$ only (append-only). That lowers the grade of that entry, not of the others.
- **Status: live**, existence shown in the test-field limit (L63).

## Set 4: losses as grades, not failures

**Plain summary.** Each known problem makes some entries fade. Listing what each one does to the grade shows that none of them pushes every ledger to "never".

| Loss mechanism | Affects | Effect on grade | Why not fatal |
|---|---|---|---|
| Orbit decay toward the throat (Dent et al., 2007.09135, per #383) | passage/orbit records (#382, #385 Set 1) | G2 → G1: entries readable until decay; a falling body may add a stray passage | flux slots (Set 3) do not depend on orbits |
| **P1** exotic matter, no Hadley escape (Hochberg–Visser 1997, relayed from external review, Claude 015; not verified by us) | all handle slots | a cost, not a loss: grade unchanged in the test-field limit | a cost flag; persistence still holds |
| **P2** clock drift to a time machine (Frolov–Novikov 1990, per #386) | handles beside other masses | may make the diary's own motion non-unique (EKT setting); affected entries drop to G1 or become unreadable | isolated, well-separated flux slots keep G2 for as long as there is no drift |
| **P3** a write may destroy its handle (Shinkai–Hayward, per #383; thin shells unknown) | the written slot | that slot → G0 or G1 | append-only: other slots unaffected; an unwritten slot can't be harmed |
| **P4** radiation and decay; stray charges | orbits (G1); flux slots hit by a stray charge | per-slot downgrade | flux survives radiation (#386, #387) |
| **P5** integrality needs one species (L58) | flux read-out values | integer → exact-real; persistence grade unchanged | the definition (Set 1) needs separation, not integers |
| **P6** co-moving drift (nothing holds mouths and bodies in place) | read-out geometry (Gauss surface placement, L52) | entries readable while the mouth stays in the tube: G1 | a slot whose mouth stays inside the tube keeps its grade |

- **Conclusion.** No item forces G0 for every slot. At least one design (isolated flux slots, no stray charge, test-field limit) is G2 for its written entries. That gives "more than never".
- **Status: live** (L64).

---

## Weak points

1. **The test-field limit is essential.** Beyond it, a write must leave $T_{ab}$ unchanged, and a charge passage does not (#388).
2. **The read-out map's continuity** (for monotonicity) is a sketch.
3. **"No later crossing"** is a condition on the world, not a theorem. Grades are per world.
4. **The Gauss surface must stay in the tube**, which needs the co-moving problem (P6) solved for at least one slot.
5. **Hadley-type hosts** need a per-slot reference that absorbs the handle's intrinsic charge, which has no worked example.
6. **The grades are coarse** (G0–G3). Finer order-theoretic profiles are possible but not needed for "more than never".
