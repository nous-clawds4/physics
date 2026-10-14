# Creative batch 10: how the observer measures an external particle's position (Creative Lead; proposal, do not merge)

**Status.** Exploration only, under David's 3:14 PM ET ruling and his 3:53 PM ET working assumptions (memory; splitting with identical patches). **Structure only: no probabilities and no counting** (David, 4:03 PM ET). Nothing goes into `versions/` or `papers/`. Builds on L28/L29. All outside citations are **unchecked**. Hadley references are marked per #362: V-text for *Found. Phys. Lett.* 10(1) 43–60 (1997), arXiv quant-ph/9706018, and *CQG* 17(20) 4187–4194 (2000), gr-qc/0004029; V-meta for the 1997 Warwick thesis, quant-ph/9609021. README line 18 says 4-geons live in spacetimes that admit CTCs. Everything here is a sketch.

**Geons.** David (4:06 PM ET, ledger): "Rule out geons? I don’t recall ruling out geons. I like Hadley’s 4-geons." Paper 1 contains a geon remark (#339) whose provenance Literature is checking; David does not recall ruling geons out. Hadley's 4-geons are the lead particle model here.

## For David (one minute)

A particle here is a tiny knot in spacetime itself (Hadley's 4-geon), not a separate object placed in it: a small region where the topology is twisted. The observer "sees" it the same way it learned about handles: it sends out light, some of it scatters off or passes through the knot and comes back, and the observer writes the arrival time and direction in its diary. "Where the particle is" is then just "which world we're in": worlds that look identical to the observer now, but have the knot in different places, write different diaries the moment the scattered light returns. The apparatus is the observer's own beacon, clock and direction reference. The pointer is the diary entry. Nothing in the motion forks, and no rule picks the result; the result is fixed by which world it is. What we haven't done is say how likely each result is. That is deliberately left for later.

---

## Verdicts (Geometry #361, Literature #362)

**Statuses.**
- L33: **pending David on CTCs** (relaxing #352 for geon hosts).
- L34: **reduces to self-echo** (L28/L29).
- L35: **live, needs a reflector**.

**L33, Hadley 4-geon (#361).**
- *Ill-posed as stated.* A return through the time-orientation flip arrives past-pointing, so "received" is undefined for exactly those returns.
- "Reversed handedness" is the wrong flip: it is a space orientation, not a time orientation.
- It conflicts with #352: CTCs are required (#362 S3).
- #320 is not the obstacle, but extension past a chronology horizon is non-unique.
- Three repairs, listed **without recommending one**:
  1. pass to a time-orientable double cover;
  2. keep only returns that stay in the orientable region;
  3. drop #352's conditions for geon hosts.

**L34, position as gluing (#361, #362).**
- The uncertain datum is the **pointed Γ**. A "mouth" is not geometric in an analytic quotient; deck displacements are.
- There is a second uncertainty: extensions beyond Cauchy horizons are non-unique.
- So L34 is the self-echo renamed. It measures $\pi_1$, not an external particle.
- Correcting my mild overclaim: under the lock, "the only uncertain position is topological" is too strong. Continuations beyond the patch edge (patch-edge Prop 7.2) and non-unique extensions beyond Cauchy horizons also leave room for uncertainty, so the uncertain data are the pointed Γ **and** the choice of extension, not Γ alone.
- Prior art (#362): Misner–Wheeler; Morris–Thorne; Visser; Friedman–Sorkin.

**L35, radar to a feature (#361, #362).**
- The record depends only on the causal past, so there is no split before the path crosses $H^+(S)$. After it, positions form a continuum unless a resolution grain is added.
- Geometric-optics rays do not reflect off curvature, so returns need matter, a junction, or wave effects.
- Prior art (#362): Bondi's k-calculus; Dolby–Gull; Perlick.

## Common structure (all sets)

- **State.** As in L29: $\hat O(\tau)=(O(\tau),\rho(\tau))$, where $\rho$ records received signals as arrival time, emission stamp and isotropy-invariant direction data (#355: continuous arrival curves, with a definite beacon switch-on).
- **New ingredient.** Signals that return *by scattering off, or passing through, an external feature* are recorded alongside pure self-echoes. Comparing the two kinds gives relative position, as in radar ranging; Bondi k-calculus is the standard picture (unchecked).
- **Apparatus.** The beacon, plus the observer's clock (proper time) and direction reference (Fermi–Walker frame modulo isotropy, #324).
- **Pointer.** The record entry for the returned signal, e.g. round-trip proper time and direction. How it is stored is the open memory item (David, 3:53).
- **Outcome.** The class of compatible hosts with that record (L29 split rule). **Branch A = world A**: a different position of the feature is a different host.
- **Motion.** Free fall stays deterministic in each host (Prop 3.2 untouched). No law of $R$: no rule selects an outcome; it is fixed by the host.

---

## Set 1 (lead): Hadley 4-geon as the particle (L33)

**Particle.** A Hadley 4-geon: a topologically non-trivial region of spacetime that is localised in space (particle-like: Hadley 1997, Axiom 2) and persisting in time as a world tube (Hadley 2000: $S^2\times\mathbb R$). As I recall Hadley's proposal (unchecked; to be verified by Literature), Hadley 1997 defines the 4-geon by non-trivial topology and causal structure with CTCs as "an essential feature" (Conjecture 1), and does not discuss time-orientability; Hadley 2000 adds that the fermion region is not time orientable, a global property ("time is not orientable around at least one class of non-contractable closed curves"), not a local failure (V-text, #362). Its behaviour depends on global boundary conditions, including the future measurement setup, which is his route to quantum-logic structure.

**How it enters the record.**
- Beacon light meets the geon region and returns.
- The return time gives the geon's distance.
- The return direction gives its direction.
- The *character* of the return (e.g. an orientation flip, if light passing through a non-time-orientable region returns with reversed handedness; unchecked) identifies it as the geon rather than an ordinary echo.

**How worlds split by position.** Consider hosts that share the observer's germ and record up to τ, but place the geon at different positions outside the observer's past light cone. They write different records when the first scattered return arrives. Position is read out as the host class.

**Traps.**
- **Nested prefix:** escaped. The hosts all continue, and they differ in a record entry (L29).
- **Identical states:** escaped only via the record (L28).
- **Analyticity:** under the analytic lock the germ fixes the universal cover, so a geon *inside* the analytic cover has a fixed position. Position uncertainty therefore needs either the geon to sit in a region the germ does not fix, i.e. relaxed analyticity (3:14 ruling), or Set 2's reading, where the uncertain datum is the gluing.
- **Time orientation:** v0.10.1's observers carry a future time direction (§4). A non-time-orientable geon must stay away from the observer's worldline, and returning signals must be compared consistently. Sketch, unchecked.
- **#320 inextendible hosts:** needs checking for geon spacetimes (unchecked).
- **CTCs:** Hadley's construction needs closed timelike curves: "The assumed existence of CTCs as an integral part of the structure ... is an essential feature of the manifold" (Hadley 1997, V-text), and his Axiom 4 (measurement sets boundary conditions) rests on them. It therefore conflicts with the deck-element no-CTC condition (#352) if the geon's topology is realised as a quotient, and otherwise with any chronology assumption of the host class (#362 note).
- **Retrocausal flavour:** in Hadley's model the outcome depends on the future measurement setup. In "branch A = world A" that is natural, because the host includes the future apparatus. But it must not be read as the observer *choosing* the world.

**Weak points.** The Hadley content is from memory. The time-orientation and CTC questions are open. Position uncertainty and analyticity have to be reconciled.

## Set 2: position as gluing: a wormhole-mouth pair under the analytic lock (L34)

**Particle.** One mouth of a handle whose partner mouth is far away. A sketch:
- Under analyticity the germ fixes the universal cover $\tilde M$, including every mouth-shaped region.
- What it does **not** fix is how they are glued, i.e. Γ (L27).
- The "particle position" is the location of the partner mouth that a nearby mouth is glued to.

**How it enters the record.** Beacon light enters the near mouth, exits the partner, and returns through any route that brings it back. That needs a loop, i.e. a deck element. Its arrival time and direction encode the partner's location.

**Split by position.** Hosts with different gluings (different Γ) give different records when that return arrives. This is L28's self-echo mechanism read as a position measurement.

**Structural observation (sketch; corrected per #361/#362 above).** Under analyticity, the position of any *local geometric* feature inside $P(O)$ is fixed by the germ. The uncertain data are the pointed Γ (topological) and, beyond the patch edge or Cauchy horizons, the choice of extension. So under the lock, measuring a position is learning $\pi_1$, which matches David's "branch A means geometry (fundamental group) A".

**Weak points.**
- Gluing needs an exact isometry between mouth neighbourhoods (L27's symmetry cost).
- The mouths are identical, which echoes identical particles (not pursued).
- It requires a returning loop.

## Set 3: radar to a localised feature in a smooth host (relaxed analyticity) (L35)

**Particle.** Any localised feature (a lump, a defect, or a 4-geon) in a $C^\infty$ host, outside the observer's domain of dependence. Its position is genuinely open: news (batch 05's structural observation, with #346's caveats).

**How it enters the record.** Radar. The beacon pulse reflects or scatters, and the round-trip time and direction give position (unchecked as a full construction in curved hosts).

**Split by position.** At the first return the hosts split by position, and positions can be a continuum. That is fine for structure; counting is parked.

**Traps.** It breaks H1 (the lock is relaxed, as allowed by 3:14). The divergence is on the null boundary of the shared domain of dependence (#346: not verified in general).

**Weak points.** It gives up analyticity. Reflection needs the feature to interact with the test field, which is a matter or junction question.

---

## Summary of the measurement structure

| | Particle | Uncertain datum | Record entry (pointer) | Lock |
|---|---|---|---|---|
| Set 1 | Hadley 4-geon | geon placement | return time, direction, character | needs relaxed analyticity or Set 2's reading |
| Set 2 | glued mouth pair | Γ (gluing) | return via the handle | analytic lock kept |
| Set 3 | localised feature | position (news) | radar return | relaxed analyticity |
