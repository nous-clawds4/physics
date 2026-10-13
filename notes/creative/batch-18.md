# Batch 18: pre-existing topological ledger states that differ by world (Creative Lead; do not merge)

**Status.** Exploration only, under David's rulings (all relayed by Physics Lead, not signed). Classical only (5:00 PM); no Born rule, no probability, no measure; (M1) unchanged at L3; CTCs as exploration only. Citations are unchecked unless verified earlier. Nothing goes into `versions/` or `papers/`. Stacked on batch 17 (#390); ledger concept #388. Ledger rows L65–L69. **No test-field limit is needed for the ledger state itself** (see Set 2).

**David (10:43 PM ET 2026-10-12, relayed by Physics Lead, Physics Lead chat, not signed; verbatim):**
> Perhaps we need to consider whether it is possible for more than one ledger-state to be consistent with any given observer-state. I am imagining some topological detail inside the ledger, with World A containing Ledger state A, B containing B, etc.

**Widget answer (same relay, verbatim):**
> Yes, have Creative Lead build a batch on pre-existing topological ledger states that differ by world.

**Motivation.** Geometry's exactness objection (#388): under the analytic lock, two worlds that agree near the observer agree on the whole connected tube, metric and $T_{ab}=G_{ab}/8\pi$ included. So an exact *write* cannot change anything near the observer. The idea here: **nothing is written.** The ledger states differ by world from the start, and the returning signal *reveals* which world.

---

## For David (plain summary)

- **Yes, several ledger states can fit one observer state, exactly.** Picture a universe that is flat everywhere but wraps around, like a video-game screen where leaving one edge brings you back at the other, in three directions. Different wrap-around patterns are different worlds. Near the observer they look **exactly** the same: same geometry, same (zero) matter. No approximation is needed.
- **The wrap pattern is the ledger state.** It is topological, it was there from the start, and nothing has to write it. World A has pattern A, world B has pattern B.
- **Reading it is just a round trip.** Send a light pulse out in some direction. In a wrapped universe it comes back from the other side after a delay equal to the length of that wrap. The arrival times and directions spell out the pattern. Before the first pulse returns, all patterns are still possible. As replies come in, the possibilities narrow. That is exactly "branch A = world A", with branches that only split, never merge.
- **Persistence is free.** Topology can't change classically (that would need time loops or a singularity), so the ledger state is permanent: every entry is kept forever.
- **The honest catches.**
  1. This is the "which handle structure are we in" idea you had at 3:43 PM, and batches 08–09 and Geometry's #370 already found it. It is the same ledger seen from a new angle.
  2. The ledger is the whole world's shape, not an object travelling next to the observer.
  3. Without a further assumption, the set of possible patterns is a continuum, not a list.

---

## Set 1: where can the distinguishing detail sit?

**Plain summary.** Analyticity forbids a lot, but not everything. Following the world outward from the observer along any path gives a unique answer. What it does not fix is how the paths are glued together globally, or how the world continues past a horizon. Those are the only places a world-dependent ledger can hide.

**What analyticity forbids [A, sketch; #370 (A)].** Fix the observer's germ at $\tau=0$. Analytic continuation along any path from the observer is unique (the developing-map argument). So:
- the **simply connected analytic development** $\tilde M$ (the universal cover of any compatible world, up to extension) is fixed by the germ;
- every compatible world is $W=\tilde M_{\rm ext}/\Gamma$, with $\Gamma$ a discrete group of isometries acting freely, and $\tilde M_{\rm ext}$ a choice of extension past non-unique continuation points (#370);
- there are **no** local differences anywhere along a path from the observer, including on the far side of a handle (the far side is reached by a path), and including regions outside the tube that connect to it.

**What analyticity does not forbid.**

| Candidate location | Allowed under the lock? | Notes |
|---|---|---|
| Global topology: deck group Γ (quotient of $\tilde M$) | **yes** | locally invisible; batch 08 L28/L29, #359, #370 |
| Inequivalent maximal extensions (Misner, Taub–NUT) | **yes**, beyond the Cauchy horizon only | Chruściel–Isenberg 1993 (V-meta per #332/#368); #367, #375 |
| Non-Hausdorff branching | as a union of extensions only | circular as a mechanism (#379 2B) |
| Far side of a nearby handle | **no**, except through Γ or the extension | the throat is a path, and continuation through it is unique |
| Region outside the tube, connected to it | **no** (same reason) | |
| A disconnected component | allowed but irrelevant | causally inaccessible; never readable |

- **Status: live** (L65). Under the lock, the exact ledger state is the pair $(\Gamma,\ \text{extension})$.

## Set 2: existence: one observer state, several exact ledger states

**Plain summary.** Flat wrapped-around universes give a clean, exact example. Every pattern looks identical near the observer, there is no matter at all, and the patterns are different worlds.

**Statement [A].** Let $\tilde M=\mathbb R^{1,3}$ (Minkowski). For a lattice $\Lambda\subset\mathbb R^3$ of spatial translations, let $W_\Lambda=\mathbb R^{1,3}/\Lambda$, a flat spatial 3-torus times time. Let an observer be at rest, with tube radius $\rho$. Then:
1. If the shortest nonzero vector of $\Lambda$ satisfies $\ell_{\min}(\Lambda)>2\rho$, the tube embeds isometrically in $W_\Lambda$. All such $W_\Lambda$ give the **same** observer state at $\tau=0$: the same germ and the same tube data. Metric flat, $T_{ab}=0$, **exact vacuum, no test-field limit.**
2. $W_\Lambda\cong W_{\Lambda'}$ (isometric, carrying the observer to itself) iff $\Lambda'=R\Lambda$ for a rotation $R$ fixing the observer's frame data. Since the frame is fixed modulo isotropy (#324), up to $\Lambda'=\Lambda$ modulo the isotropy group. So distinct lattices modulo isotropy are distinct ledger states.
3. Each $W_\Lambda$ is time-orientable, with a global time function and **no CTCs**.

**Other candidates checked.**
- **Misner / Taub–NUT extensions.** They are exact, but they differ only beyond the horizon, and each observer crosses into at most one extension (#367, #375). The ledger state "which extension" is read by **survival**, not by a reply: a nested prefix (#372 R3). That is weaker. **Parked** as the second example.
- **Flux through a far handle (vacuum Maxwell).** A nonzero flux needs $F\neq0$ on every sphere around the mouth. Under full analyticity (analytic fields), $F=0$ on the tube's open set forces $F\equiv0$ on the connected world. So **the field cannot vanish on the tube**, which changes $T_{ab}$ there, and the lock excludes it [A].
- **Flat U(1) connection, Wilson loop around a handle** ($F=0$ everywhere, nonzero holonomy). Exact: $T_{ab}=0$ and the metric is unchanged. But classically **unreadable**: the Lorentz force vanishes, and only quantum phases (Aharonov–Bohm) see the holonomy. **Excluded** by the 5:00 PM classical constraint.
- **Gravitational holonomy** (rotation or boost part of a deck element). It is part of Γ. Classically readable: a ray returning round the loop comes back rotated. **Included in Γ.**
- **Status: live** (L66). An exact existence example (flat lattice quotients), with no test limit.

## Set 3: reading the state out: replies reveal the world

**Plain summary.** A light pulse that goes round the wrap comes back after a definite delay, from a definite direction. That reply tells you one lattice vector. Collect enough replies, and you know the pattern. Each reply rules worlds out, so the set of worlds still possible only shrinks.

- **Read-out [A].** In $W_\Lambda$, a ray emitted at $\tau_e$ in direction $\hat n$ returns to the observer iff $\hat n\parallel g$ for some $g\in\Lambda$. It arrives at $\tau_e+|g|$ (for a radar-sense round trip of the image), from direction $-\hat n$, and with deck label $g$. The record entry is (arrival time, emission stamp, direction, deck element), exactly #372 §2.1/§2.2's entry.
- **Type O**, since the host is time-orientable (#364). It needs **no** CTC and no geon: the "round trip" is through the topology, not a time loop (contrast with #372 §2.2).
- **World revelation.** Record class at τ: $[W]^R_\tau=\{\Lambda:\ \text{all returns up to }\tau\text{ agree}\}$.
  - For $\tau<\ell_{\min}$ there are no returns, so all Λ are compatible.
  - It refines as τ grows, so the record only grows and branches nest (#372 §2.6). Under the lock the germ is shared, so state branch = record class (#372 R2).
  - "Branch A = world A" holds in the limit: Γ is fixed, and certifiably so, once τ exceeds a generating set's lengths and about twice the quotient diameter (#370, sketch). For cocompact Λ that is a finite time.
- **No write, so no $T_{ab}$ problem.** Γ is topological, and no carrier energy can change it. The signal is a null geodesic; its own energy is a test quantity, but that does not touch the ledger state.
- **Status: live** (L67).

## Set 4: relation to persistence (#390) and to the append-only diary (#388)

**Plain summary.** Nothing is written, so nothing can fade. The pattern lasts as long as the world does. The old diary is still useful, but only as a place to keep the replies; the "ledger" itself is now the shape of the world.

- **Persistence.** The ledger state Γ is constant: topology change is excluded classically (Geroch 1967; Tipler 1977; Borde 1994; per #380). In #390's terms, every "entry" (each $g\in\Lambda$) is readable on every interval once its first return has arrived. **Grade G3** for the ledger state, not just G2.
- **Read-out map** (#390 Set 1). $r_g(\hat O(\tau))$ = "a return with deck label g is in the record". It is fixed in advance and gauge-invariant modulo isotropy (#324). It needs repeated beacon emission, and it stores its result in #372's record.
- **The append-only diary (#388)** becomes optional: its role shrinks to holding replies, i.e. #372's record ρ. The exact ledger state is the world's Γ, so batch 14–17's write mechanisms are not needed for existence.
- **Status: live** (L68).

---

## Weak points (strongest first)

1. **This is #370's result, not a new mechanism (strongest).** Under the lock, the only world-dependent data are Γ and the extension (#370 (A)). The "pre-existing topological ledger" is that same freedom, renamed. It reconnects to batches 08–09 (crystal covers), whose share computations were degenerate (0/1, #359). Probabilities stay parked.
2. **A continuum of states.** Flat lattices form a continuous moduli space, against the standing rule (discrete or countable options, no continuum). Countability needs a further assumption, e.g. Γ a subgroup of a fixed discrete group (a known crystal cover; #359, #370). That is an input, not derived.
3. **Not "next to the observer".** David's 7:45 PM ledger travels in close proximity. Here the ledger is the global topology. A nearby handle's far side is fixed by continuation (Set 1), so it cannot hold a world-dependent state unless it closes up through Γ.
4. **Non-cocompact Γ (e.g. a single handle in an open universe)** is not certifiable (#370). Its replies narrow the class but may never fix it.
5. **The Misner/Taub–NUT extension ledger** is readable only through survival, a nested prefix, not a reply (#372 R3).
6. **The classical Wilson-loop holonomy is unreadable**, which excludes the most "ledger-like" field datum.
