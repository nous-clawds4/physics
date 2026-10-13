# Batch 24: Set 2 first kill check: does a second slit change self-consistent multiplicity? (Creative Lead; do not merge)

**Status.** CTC exploration only. Structure only, with no weights; classical; no Born rule; no $|a|^2$; (M1) untouched at L3. Nothing goes into `versions/` or `papers/`. Stacked on batch 23 (#407 at 16e0b45). Ledger rows L98–L101. Script: `notes/creative/batch-24/ekt.py` (sha256 `d65230e5012f2b113fd7ddfebb713ae5be196005d14e34f64d59dba8496e9d94`); output: `results.txt` (sha256 `1cf75b631550fac2c507ed89667bc87816ff61f9740254ac05e86e9cea621106`).

**Lead ruling** (Physics Lead, 9:45 AM ET 2026-10-13; a Lead ruling, not David's): batch 24 runs Set 2's first kill check, in the offset-mouth host (#385 L56) with an EKT-style hard-sphere billiard, structure only and with no weights.

---

## For David (plain summary)

- **The question.** In a world with a time-shifted wormhole, a ball can come back and knock its own younger self. Some launches then have more than one self-consistent story. Does opening the second slit change how many stories a launch *through the first slit* has?
- **What we did.** We built a simple 2D model: hard balls, an idealised wormhole, and a barrier with two slits. For each launch direction, we listed every consistent story with at most one trip through the wormhole, once with one slit open and once with two. We tried ten wormhole placements and time shifts.
- **What we found.**
  - Extra stories do exist. Some launches have the plain story *and* a whole family of self-knock stories, which is EKT's multiplicity.
  - No launch ever lost all its stories, matching EKT.
  - For launches through slit 1, opening slit 2 never changed anything in any of the ten setups. The only changes were for launches through slit 2 itself, which closing it simply blocks. That is trivial.
- **Verdict.** In this first check, Set 2 does not give the needed effect. It is not proven impossible, but the geometry makes it hard. The returning ball's path runs roughly along the line between the two mouths, so to reach a slit-1 launch it would have to pass through slit 2 by coincidence of placement. No scanned host had that.

---

## Model, regime and simplifications

- **Space and bodies.** 2D, nonrelativistic, with unit launch speed. Equal-mass hard spheres (discs) of radius r = 0.1 and elastic collisions, in the style of Echeverria–Klinkhammer–Thorne (PRD 44 (1991) 1077; verified, Crossref, per Literature; readings per #365).
- **Idealised mouth.** Two circles of radius s = 0.5, A and B. A ball centre reaching B at B + s e(φ), at time t with velocity w, emerges at A + s e(φ) at time t − T with the same velocity. This is a pure translation by d = B − A plus a time shift: no rotation, no lensing, no throat dynamics. It is the offset-mouth host, #385 L56. Per #398, a fixed time shift gives CTCs at every time, so this is a CTC host and not the cylinder toy.
- **Barrier.** The line y = 2, with slits at x = −0.6 (slit 1) and x = +0.6 (slit 2), each of half-width 0.15. The crossing test treats the centre as a point. A ball meeting a closed part of the barrier is absorbed, which ends that path; the walls don't reflect. Launches start from the origin; mouth B is at (−1.8, 6).
- **Histories enumerated** (at most one traversal):
  - **H0, the plain story:** no self-collision. It is consistent unless the older ball emerging from A touches the younger one.
  - **H1, one self-collision.** For equal masses, a collision in which the younger ball is deflected exactly onto the velocity w that the older one emerged with forces three things. The contact normal is n ∥ u = v0 − d/T. Approach requires |u| > 2r/T. The loop closes iff wT = d + 2rn, which then holds identically. So the collision time t_c is a free parameter. The consistent H1 histories form *intervals* in t_c: a continuum, which is an artefact of the translation mouth. For each t_c the script checks:
    - barrier passage on all four segments;
    - no earlier contact;
    - no other mouth entry;
    - time order t_e < t_c;
    - loop closure, numerically.
  - **Not enumerated:** launches entering A first, or histories with more than one traversal (counted as "multi").
- **Hosts scanned:** A ∈ {(−4.2, 10), (3, 8), (1, 12), (−1.8, −3), (4, 0.5)} × T ∈ {8, 15}, with launch angles −40° to 40° in 0.5° steps. Nothing was tuned; the hosts were fixed before the run.
- **Friedman et al. 1990** (PRD 42, 1915): interaction is needed for non-uniqueness. Cited from the abstract only.

## Results [N] (results.txt)

| host A, T | H0 fails | launches with H1 (one / two slits) | structure differs | of which slit-1 launches |
|---|---|---|---|---|
| (−4.2, 10), 8 or 15 | 0 | 0 / 0 | 0 | 0 |
| (3, 8), 8 | 0 | 4 / 20 | 16 | **0** (16 via slit 2) |
| (3, 8), 15 | 0 | 4 / 20 | 16 | **0** (16 via slit 2) |
| (1, 12), 8 or 15 | 0 | 0 / 0 | 0 | 0 |
| (−1.8, −3), 8 or 15 | 0 | 0 / 0 | 0 | 0 |
| (4, 0.5), 8 or 15 | 0 | 0 / 0 | 0 | 0 |

- **Multiplicity: yes.** In host (3, 8), 20 launches have H0 plus one H1 interval (t_c measure ≈ 1.2).
- **Exclusion: none.** H0 never fails, in agreement with EKT's "at least one solution".
- **Dependence on slit 2 for slit-1 launches: none found** (0 of 161 × 10 host-launches). Every difference is a slit-2 launch, which a closed slit 2 simply blocks.

**Why (a structural reason) [A, partial].**
- In H1, the older ball's pre-collision velocity is w = (d + 2rn)/T. Its path therefore runs from A + s e roughly *along d*, toward and past B, to the collision point on the launch line.
- For a slit-1 launch to have an H1 that needs slit 2, that path must cross the barrier through slit 2 while the launch line crosses slit 1.
- That fixes a narrow relation between A, B, T and the slit positions. It is possible in principle, but only for specially placed mouths, and none of the ten scanned hosts had it.
- This is not a proof of impossibility. A dense host scan is the next check.

## Which-route kill condition

- **What a record would be.** A which-route record at the slits is part of the world and of the consistency map.
- **Passive record.** One that does not change any ball's motion, such as a pointer flipped without recoil in the test limit, leaves every consistency equation and so every multiplicity unchanged. It only labels histories.
- **Active record.** One that exerts a force, or is a hard body, enters the collision geometry. It can create or destroy H1 families.
- **Kill condition:** a slit-2-dependent multiplicity, if one were found, would be removed by any record that blocks or deflects the older ball's slit-2 passage. A record that only labels it would not remove it. Whether that labelling changes a *pattern* depends on a counting rule over multiple histories (#399), which this batch does not supply.

## Answer to the kill check

Set 2's lever (multiplicity) exists in the host. But in a first scan, its dependence on the second slit appears only trivially, for launches through that slit. **Set 2 is not killed, but it is weakened: L1 → L0–L1.** Revival needs a host where the older ball's path threads the other slit, and then a counting rule over histories, which is also needed before any dark spot could be claimed.

## Weak points

1. Idealised translation mouth. It gives continuum H1 families. EKT's spherical mouths, with lensing, give discrete or infinite families, which were not modelled.
2. Only one traversal and only one collision. Multi-traversal histories ("multi" counts) are not enumerated.
3. Absorbing, point-like slit edges. Reflecting walls would add bounce paths.
4. Ten hosts and 0.5° launches; the t_c grid has 600 steps up to 40. The structural argument suggests special hosts exist, so a dense scan is the next check.
5. 2D and nonrelativistic.

Ledger: L98–L101 (L101 records the Lead ruling).
