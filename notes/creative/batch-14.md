# Batch 14: the signal, the physical record, and the write (Creative Lead; do not merge)

**Status.** Exploration only. It works under David's 3:14 PM, 3:53 PM and 4:16 PM rulings, the 5:00 PM classical constraint and the 7:45 PM question below (all relayed by Physics Lead, not signed). It uses structure only: no Born rule, no probability input and no measure. CTCs and non-time-orientability appear as exploration only. Nothing goes into `versions/` or `papers/`. **Every outside citation is unchecked** unless marked otherwise. Base: `notes/creative/measurement-model-v0.md` (#372). Ledger rows L43–L47.

**Prompt (David, 7:45 PM ET 2026-10-12, relayed by Physics Lead, Physics Lead chat, not signed; verbatim):**
> Should we delve into the details of what constitutes the signal and how it gets recorded? If the observer is going to record data, then it needs to be physical, which means encoded into spacetime itself. Perhaps some sort of ledger composed of particles of nontrivial topology that is distinct from the observer but travels in close proximity?

---

## For David (one minute)

Yes, and it can be done without creating new handles in spacetime. Three pieces:

- **The signal** should be a small physical body (a "pulse" of matter), not a light ray. A light ray comes back the same way every time. A body that can collide with itself inside the time loop can come back in several self-consistent ways. That is where the countable menu of replies comes from (Set 1).
- **The diary** is your idea: a little flock of geons travelling with the observer. They are made at the start and never created or destroyed (Set 2).
- **Writing** to the diary is the hard part. Making a new handle is close to forbidden in classical gravity: you get time loops or a singularity. So we don't. A returning signal **nudges** the flock instead. It changes which way the geons wind around each other (a whole number) or where they sit relative to one another (Set 3). The whole-number version gives a record that is discrete and stable for free.

The catch: the diary is now part of the world, so its different entries are different worlds. That is exactly your "branch A = world A". It also forces the observer to be a small tube rather than a point, which is a known cost (#336).

---

## Set 1: the carrier (closes round-trip open item (a), conditionally)

**Plain summary.** A light flash returns in only one way per route, so it can label *which route* but cannot offer a menu. A small body that can hit its own earlier self inside the time loop has several consistent histories (the classic "billiard ball" puzzle). That is the source of the countable multiplicity. So the carrier should be a body that interacts.

| Carrier | Replies per deck class | Can it write? | Verdict |
|---|---|---|---|
| Null geodesic | one (ODE uniqueness; Prop 3.2-type) | no: no energy or momentum transfer in the test limit | label-only; **insufficient** |
| Linear test field (EM, linearised GW) | one: existence and uniqueness among solutions that die off in time (Friedman–Morris 1991, 1997, V-meta per #377) | no backreaction at test order | **insufficient** for multiplicity |
| Gravitational wave beyond linear order | possibly several; no theorem known to us | yes, in principle | open; too hard to check now |
| **Matter pulse / interacting test body** | countable families of self-consistent histories (Echeverria–Klinkhammer–Thorne 1991; batch 12 L40) | yes: momentum transfer by collision | **live (preferred)** |
| Small geon as carrier | inherits multiplicity if it interacts | yes | emitting it is topology change (Set 2 obstacle); **parked** |

- **Why "interacting" is needed.** A linear carrier gives the round trip a unique reply per class (Friedman–Morris). Only interaction lets the CTC consistency condition have several solutions (EKT). This is the item-(a) answer: an interacting beacon.
- **Cost.** The multiplicity is a property of the matter law plus the CTC. We must not pick the matter law to get a particular count, which would be a law of R by fiat. Billiard-ball elastic collisions are the standard example, and we take them as given.
- **Status: live.** It closes (a) as "interacting test body", conditional on Set 3 using the same body to write.

---

## Set 2: the physical record (co-moving ledger geons)

**Plain summary.** The diary is a small group of geons that travel next to the observer. They exist from the start, and nothing ever creates or destroys a handle. The diary is "spacetime itself", as you asked, but it never changes its topology.

**The obstacle (topology change under classical evolution; all unchecked):**
- Geroch 1967: a compact, time-orientable spacetime interpolating between spatial slices of different topology contains closed timelike curves.
- Tipler 1977: with the weak energy condition and generic conditions, topology change produces a singularity (no CTC-free, non-singular route).
- Borde 1994: extends the singularity/causality obstruction to non-compact settings.
- Gibbons–Hawking 1992: spin structure constrains which changes are allowed (a mod-2 condition on created handles).

**Loopholes and their cost.**
- **(2A) Topology-changing write through CTCs.** Geroch's theorem permits topology change *with* CTCs, and CTCs are allowed in geon hosts (4:16 PM, exploration only). Cost: the CTCs must now sit in the ledger region, next to the observer, not just inside the measured geon. The observer's own neighbourhood loses chronology. Also, every write needs a fresh CTC region, so the record pays a causality cost per bit. **Parked.**
- **(2B) Non-Hausdorff branching as the write.** A trousers-type non-Hausdorff spacetime "writes" by splitting. Cost: that is the branching we are trying to *derive*. Using it as the write mechanism assumes the result (circular). Under the lock, non-Hausdorff unions also do not fork a single geodesic (#367). **Parked.**
- **(2C) No topology change: the ledger's topology is fixed at the start.** The geons are eternal or formed before the first measurement. Writes change a non-topological datum (Set 3). **Live.**

**Status: 2C live; 2A and 2B parked.**

---

## Set 3: the write mechanism (no topology change)

**Plain summary.** The returning body bumps the diary geons. The bump changes something that can change without new handles: how many times one geon has wound around another (a whole number), or their relative positions and phases (ordinary numbers). The whole-number version is the most promising, because whole numbers are naturally stable and discrete.

| Candidate record | Changeable by a classical write? | Discrete? | Stable? | Verdict |
|---|---|---|---|---|
| Deck-class labels of ledger loops | **no**: fixed by topology | yes | yes | a *label of a reply*, not a writable state; **feeds Set 1 only** |
| Holonomy / Wilson-loop-like data of ledger geons | flat holonomy is a point of the representation variety of π₁ and moves only continuously; a jump needs a disconnected variety and a non-continuous evolution | only if the variety is discrete, but then it is unwritable | yes | stability and writability conflict; **parked** |
| Relative positions / phases among ledger geons | yes: a collision transfers momentum | **no** (continuum) | marginal (neutral directions drift) | live as the **exact-real** record (#355); discreteness comes only from which deck class replied |
| Type O/F flag | per-return property of the loop | yes | n/a | a label, not storage; **recorded as part of each entry, not a mechanism** |
| **Winding count** of one ledger body around another (or around a ledger handle) | yes: a kick sends the body once more around the loop | **yes (ℤ)** | **yes**: homotopy-invariant between kicks | **live (preferred)** |

**Winding-count write (Set 3 main line).**
- A ledger body orbits, or is trapped near, a ledger geon. Its integer winding relative to a fixed cut is a homotopy invariant of its worldline segment.
- An incoming carrier (Set 1) collides with it. Whether the winding then advances by 0, 1, … follows from the collision dynamics. **It is not chosen.**
- Discreteness is for free (ℤ). Stability holds because, between kicks, the winding changes only if the body crosses the cut, which free motion does at definite times.
- **No topology change.** The handles are fixed (2C), and only the worldlines move.

**Can a write be a change in a non-topological invariant?** Yes, but only for *worldline* invariants (winding, linking of ledger trajectories). Invariants of the ledger *geometry itself* (deck labels, flat holonomy) are either fixed or continuous-only. Writes live in the matter on the fixed topology, not in the topology.

---

## Traps checked

- **Nested-prefix trap (#367 (1); §2.4 of #372).** Under the lock, the observer's germ does not fork across worlds; the record does. A physical ledger fits this: the ledger *is* the record, so what branches is the ledger state, not the observer's motion. **Passes**, as long as the ledger is not used to make the observer's geodesic fork.
- **Identical-state trap.** If two worlds differ only in the ledger's state, and the ledger is outside the observer state, they look identical to the observer, and nothing has branched for it. So **the ledger must be part of the observer state.** That is L29's germ+record, now physically realised: $\hat O=(O,\text{germ of the ledger tube})$.
- **Cost of including the ledger.** The state becomes the germ of a finite tube containing observer + ledger. That brings back #336's finite-size-observer cost: an undefined tube scale and a changed state definition. It is cheaper here, because the scale is set by the ledger's physical extent, not chosen. **Open.**
- **Law of R by fiat.** It is avoided only if the write map (carrier collision → winding change) follows from the matter law plus the geometry. Choosing the threshold or the cut by hand would be fiat. The cut is a gauge choice: the *difference* of windings is cut-independent. **Passes, conditionally.**
- **Locality vs memory (#352).** A physical ledger makes the record local again, near the observer. That partly answers OP1 ("where the memory is stored", David 3:53).
- **Classical only (5:00 PM).** No quantum structure is used. Multiplicity comes from classical CTC consistency (EKT), not amplitudes.

---

## Weak points

1. **EKT multiplicity** is shown for billiard balls in simple wormhole spacetimes, not Hadley geons (unchecked transfer).
2. **Ledger stability**: a co-moving flock of geons in a vacuum host may not be a bound, long-lived configuration. No known solution provides one.
3. **Tube scale** (#336) returns in milder form.
4. **The cut** for winding counts needs a canonical choice, or else the record must be stated as differences only.
5. **Countability** relies on batch 12's (L40) generic countability of EKT families; non-generic continua are possible.
6. **Topology-change citations** (Geroch 1967, Tipler 1977, Borde 1994, Gibbons–Hawking 1992) are all unchecked; the exact hypotheses (compactness, energy conditions, spin) matter for whether 2A is really closed.
7. **Collision writes need the carrier to reach the ledger** after the round trip, so the reply must return to the ledger, not just to γ. That adds a geometric condition to the round-trip definition.
