# Creative batch 11: measurement as a round trip through the geon's CTC (Creative Lead; proposal, do not merge)

**Status.** Exploration only, under David's 3:14 PM ruling and 3:53 PM working assumptions. Structure only: no probabilities, no counting (4:03 PM). Nothing goes into `versions/` or `papers/`. Hadley marks are per #362; all other outside citations are **unchecked**. Everything is a sketch.

**Central hypothesis (David, 4:17 PM ET, relayed by Physics Lead, Physics Lead chat, not signed; verbatim):** "Hmm, maybe that’s what it means to observe a particle? A signal goes from the observer to the particle’s CTC and comes back to the observer, communicating information about the particle’s state?"

## For David (one minute)

Your idea, made concrete: to observe a particle is to send a signal into the particle's little time-loop and get it back. Inside the loop the signal can meet itself. As in the famous billiard-ball puzzle, the laws there can allow more than one self-consistent way for that to happen. Each consistent way sends a different reply back to the observer. Different replies mean different diary entries, and different diary entries mean different worlds: branch A is world A. So the branching would come from the time-loop's multiple consistent solutions, and nothing in the observer's own motion forks. Two honest catches came up. A plain light signal that just passes through probably has only *one* consistent solution, so the signal has to interact with itself or with the particle inside the loop. And it is open whether the different solutions count as different worlds or as different events in one world.

---

## Definition: measurement = round trip

- **Setting.** The host has a geon region $G$ containing CTCs (Hadley 1997, V-text: CTCs are "an essential feature"). The observer's region $U\supset\gamma$ is time-oriented and chronological. Time orientation fails only globally, around loops through $G$ (Hadley 2000, V-text).
- **Round trip.** A beacon signal leaves $\gamma(t_e)$, enters $G$, and comes back to $\gamma(s)$.
- **Content.** What returns (arrival time, direction, and any modification of the signal by what it met in $G$) is entered in the record $\rho$ (L29). It is "information about the particle's state".

## Reorganised problems (from #361's three L33 issues)

### (1) What "returns" means across the orientation flip

Take an unoriented null curve $c$ from $\gamma(t_e)$ to $\gamma(s)$ through $G$. Orient it to be future-pointing at one end using $U$'s orientation, and transport that orientation continuously along $c$.
- **Type O (orientation-preserving loop).** It is then also future-pointing at the other end. One end is an emission and the other a reception, so this is a **round trip**, and the only kind that counts as a measurement.
- **Type F (orientation-reversing loop).** At the other end it is past-pointing. Seen from $U$, *both* ends are receptions, or both are emissions. Nothing goes "out and back". The observer at most records two correlated receptions (or makes two emissions) with no beacon content returned. #361's "received is undefined" is exactly this case. Type F is **recorded as a correlation, not a measurement** (sketch).
- This is repair (ii) of #361 refined: keep Type O returns. Type F is classified rather than discarded. It makes no use of the double cover (repair i) or of dropping #352 (repair iii).

### (2) CTCs versus #352

- The hypothesis *needs* CTCs inside $G$ (#362 S3).
- #352's condition (no deck element maps a point into its own chronological future) would have to be **restricted to $U$**, i.e. relaxed for geon hosts.
- **That is David's call** (L33 status). Nothing here assumes it.

### (3) Non-unique extension past the chronology horizon: a source of branches

- Hosts with a geon have a chronology (Cauchy) horizon $H$ around the CTC region. Extensions past $H$ are non-unique (#361; Chruściel–Isenberg 1993, V-text per #332).
- **Under the hypothesis this non-uniqueness is a candidate source of the branches, not an obstacle.**
  - Different extensions are different hosts.
  - A signal crossing $H$ may return in one extension and not in another. In Taub–NUT-type examples, different extensions continue different families of geodesics (unchecked as stated for signals).
  - The observer survives in both, so its record differs ("reply" vs "no reply"). That is a genuine split, **not a nested prefix for the observer**, even though for the *signal* it is a prefix (#345 caveat applies to the signal, not to the observer).
  - Branch A = world A directly.

## EKT multiplicity: does it give the branches?

- **The template.** Echeverria–Klinkhammer–Thorne 1991 (V-meta): billiard balls through a wormhole time machine have several self-consistent trajectories for the same initial data. Locally the motion is deterministic; the multiplicity comes from global consistency (ledger L7; #331 §0).
- **Linear signals: probably no multiplicity.** For free test fields on some CTC spacetimes the initial-value problem appears well-posed, with unique solutions (Friedman–Morris and Friedman et al. 1990; unchecked). A beacon that is a linear test field passing through $G$ would then give **one** consistent reply: no branching from consistency.
- **What multiplicity needs.** The signal must interact inside $G$: with itself (the billiard-ball case) or with the geon's own content. That makes the "signal" a body or a non-linear field, like EKT's balls, not a test field. That is an added cost and must be named.
- **Do solutions count as worlds?** Neutrally, the options are:
  - (a) *World = geometry only.* Several solutions on one host are an **in-host** multiplicity of field histories, not "branch A = world A".
  - (b) *World = geometry plus content.* Each self-consistent solution is a world.
  - (c) *Back-reaction.* The solutions source different geometries, so they are different hosts.

  Only (b) and (c) match David's framing. Which one applies is open.
- **No law of $R$.** No rule picks a solution. The record is fixed by which world it is. Prop 3.2 is untouched for the observer's free fall.

## Candidate sets

1. **Consistency branches (L36).** The branches are EKT-type multiple self-consistent round-trip solutions, read as worlds via (b) or (c).
   - Needs an interacting signal.
   - Linear signals give one reply.
2. **Extension branches (L37).** The branches are the non-unique extensions past the geon's chronology horizon.
   - The return is present in one and absent in another, so the observer's record splits.
   - Keeps the beacon linear.
   - Needs the extensions to differ *on the signal's path* (unchecked) and needs #352 relaxed to $U$.

## Traps checked

- **Nested prefix:** for the observer, both sets give genuine record splits. For the signal, Set 2 is a prefix, which is harmless.
- **Identical states:** escaped via the record (L28).
- **Law of $R$ by fiat:** none.
- **#320:** not the obstacle (#361). Extensions past $H$ must each be inextendible.
- **Prop 3.2:** the observer's motion is unchanged.
- **Everett framing:** none. The solutions and extensions are alternative worlds, not co-existing branches (#332 N1).

## Weak points

1. Type F returns carry no measurement. Whether real geons give any Type O returns is unchecked.
2. Set 1 needs an interacting signal, a body, against the beacon-as-test-field picture.
3. "Solutions are worlds" requires choosing (b) or (c).
4. Set 2's claim that extensions differ on the signal's path is unchecked.
5. Both need #352 relaxed for geon hosts, which is David's call.
6. EKT and Friedman et al. results are cited from memory.
