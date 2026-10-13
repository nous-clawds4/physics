# Batch 24: Set 2 first kill check: does a second slit change self-consistent multiplicity? (Creative Lead; do not merge)

**Status.** CTC exploration only. Structure only, with no weights; classical; no Born rule; no $|a|^2$; (M1) untouched at L3. Nothing goes into `versions/` or `papers/`. Stacked on batch 23 (#407 at 16e0b45). Ledger rows L98–L101. Script: `notes/creative/batch-24/ekt.py` (sha256 `d65230e5012f2b113fd7ddfebb713ae5be196005d14e34f64d59dba8496e9d94`); output: `results.txt` (sha256 `1cf75b631550fac2c507ed89667bc87816ff61f9740254ac05e86e9cea621106`).

**Lead ruling** (Physics Lead, 9:45 AM ET 2026-10-13; a Lead ruling, not David's): batch 24 runs Set 2's first kill check, in the offset-mouth host (#385 L56) with an EKT-style hard-sphere billiard, structure only and with no weights.

---

## For David (plain summary)

- **The question.** In a world with a time-shifted wormhole, a ball can come back and knock its own younger self. Some launches then have more than one self-consistent story. Does opening the second slit change how many stories a launch *through the first slit* has?
- **First try: void.** Our first model wormhole was glued wrongly: balls came out *into* the far mouth instead of out of it. Geometry caught this, so those results don't count. They are kept below only as a record.
- **Rerun with a correctly glued wormhole**, in two versions. We found every consistent story with at most one trip and one knock, using a root-finder, for launches through slit 1, with slit 2 closed and then open. We used nine wormhole setups that really allow time travel, and dropped one that doesn't.
- **What we found.**
  - Extra stories exist: some launches have two, the plain one and one self-knock story.
  - In one setup, a narrow band of launches about 0.16° wide had *no* story within our search. That would be a forbidden launch, but it is probably a gap in our search, which doesn't include stories with more trips.
  - **Opening slit 2 never changed anything for a slit-1 launch.** That held in all setups and both wormhole versions.
- **Verdict.** In this check, Set 2 does not give the needed effect. Slit 2 could only matter if one of the ball's straight pieces of path happened to cross the barrier at slit 2, and none did.

---

## Model, regime and simplifications

- **Space and bodies.** 2D, nonrelativistic, with unit launch speed. Equal-mass hard spheres (discs) of radius r = 0.1 and elastic collisions, in the style of Echeverria–Klinkhammer–Thorne (PRD 44 (1991) 1077; verified, Crossref, per Literature; readings per #365).
- **Idealised mouth.** Two circles of radius s = 0.5, A and B. A ball centre reaching B at B + s e(φ), at time t with velocity w, emerges at A + s e(φ) at time t − T with the same velocity. This is a pure translation by d = B − A plus a time shift: no rotation, no lensing, no throat dynamics. **Defect (Geometry, #408 review):** since entry needs w·e < 0, this rule sends the ball into disc A, so it glues the exterior of B to the interior of A and is not an exterior-to-exterior wormhole. A valid gluing reverses the normal (reflection w ↦ w − 2(w·e)e, or point inversion A − s e, −w). The results below are void until rerun with such a gluing. It is the offset-mouth host, #385 L56. Per #398 and Literature M1 (#408), a fixed time shift T gives CTCs only if T exceeds the mouth separation |d| (c = 1). Host A = (−1.8, −3) has |d| = 9 > T = 8, so it is **not a CTC host**; host A = (4, 0.5) has |d| ≈ 7.99, just below T = 8 (marginal). It is a different host from the cylinder toy either way.
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
- **Friedman et al. 1990** (PRD 42, 1915; abstract only): the Cauchy problem in spacetimes with CTCs; for free (non-interacting) fields and particles, consistent evolution of initial data exists, and non-uniqueness needs interaction. Linear-field uniqueness: Friedman–Morris, PRL 66 (1991) 401 and CMP 186 (1997) 495 (bibliographic only, per Literature).
- **Prior art** (bibliographic only, per Literature): Novikov, PRD 45 (1992) 1989; Lossev–Novikov, CQG 9 (1992) 2309; Mikheeva–Novikov, PRD 47 (1993) 1432; Carlini et al., IJMPD 4 (1995) 557; Carlini–Novikov, IJMPD 5 (1996) 445. None of them treats slits as boundary data.

## Results [N] (results.txt)

| host A, T | H0 fails | launches with H1 (one / two slits) | structure differs | of which slit-1 launches |
|---|---|---|---|---|
| (−4.2, 10), 8 or 15 | 0 | 0 / 0 | 0 | 0 |
| (3, 8), 8 | 0 | 4 / 20 | 16 | **0** (16 via slit 2) |
| (3, 8), 15 | 0 | 4 / 20 | 16 | **0** (16 via slit 2) |
| (1, 12), 8 or 15 | 0 | 0 / 0 | 0 | 0 |
| (−1.8, −3), 8 or 15 | 0 | 0 / 0 | 0 | 0 |
| (4, 0.5), 8 or 15 | 0 | 0 / 0 | 0 | 0 |

- **Multiplicity: void.** The script accepted H1 in host (3, 8) for 20 launches, but in every accepted H1 point the older ball's pre-collision path crosses a mouth disc (gluing defect, see Model). No valid H1 survives. Also unchecked: the older ball's post-collision re-entry into A or B.
- **Exclusion: not tested.** The older ball in H0 also emerges into disc A, so "H0 never fails" says nothing about a wormhole host. Compare with EKT, who report no initial trajectory without a consistent solution (not a quotation; per #407).
- **Dependence on slit 2 for slit-1 launches: none found** (0 of 161 × 10 host-launches). Every difference is a slit-2 launch, which a closed slit 2 simply blocks.

**Why (a structural reason) [A, partial].**
- In H1, the older ball's pre-collision velocity is w = (d + 2rn)/T. Its path therefore runs from A + s e roughly *along d*, toward and past B, to the collision point on the launch line.
- For a slit-1 launch to have an H1 that needs slit 2, that path must cross the barrier through slit 2 while the launch line crosses slit 1.
- That fixes a narrow relation between A, B, T and the slit positions. It is possible in principle, but only for specially placed mouths, and none of the ten scanned hosts had it.
- This is not a proof of impossibility, and it assumes w ≈ d/T, which fails under a valid gluing (w_old = S_e w_post). Redo it after the rerun. A dense host scan is the next check, and root-count edges should be refined (bisection in θ).


## Rerun (valid gluing): `ekt2.py`

Script: `notes/creative/batch-24/ekt2.py` (sha256 `eb6d28cb57f6b09b317f58a209e8f3bdfed5acd2c1384b3743fe5d95a9434591`); output: `results2.txt` (sha256 `97dc9d767b68eaa403b4ec15a1c681c6c4403e85e5aa0468b6a33545e6cc66ea`). `ekt.py` and `results.txt` are kept as the void record.

**Gluings.** Both are exterior-to-exterior, and both were run because it was cheap (about 70 s).
- **G1 reflect:** B + s e ↦ A + s e, w ↦ w − 2(w·e)e. This is the minimal fix to the translation rule: same point label, normal reversed, tangent kept.
- **G2 invert:** B + s e ↦ A − s e, w ↦ −w (point inversion).
- In 2D both are orientation-reversing handles, as noted; an orientable mirror gluing was not run.

**Solver.** An H1 history has unknowns t_c, the contact angle α, and q = w_old·n. Equal-mass elastic contact gives the young ball the outgoing velocity w_p = (v0·t)t + q n.
- **Equations:** w_em·n = q, and Q + w_em(t_c − t_e) = v0 t_c + 2rn. That is 3 equations in 3 unknowns, so roots are discrete (the continuum was the translation artefact, F5).
- **Root-finding:** scipy `root` (hybr) from 288 starts per launch, then deduplicated.
- **Checks on each root:**
  - approach, and t_e < t_c;
  - the young ball's path before and after the collision, against both mouth discs and the barrier;
  - the older ball's path **before and after** the collision, against both discs;
  - no earlier contact and no second contact.

  An older post-collision path that re-enters a mouth makes the history "multi": reported, not counted.
- **Slits:** roots don't depend on the slits, since the barrier only filters, so roots are computed once per launch.
- **Scan:** 33 launches across the slit-1 window (−20.56° to −12.68°, width 7.88°). Edges in the root count were refined by 8 bisections in θ.

**Hosts.** As before. The non-CTC host A = (−1.8, −3), T = 8 (|d| = 9 ≥ T) is **dropped**. Its T = 15 version is a CTC host and was run; it had no H1. Host (4, 0.5), T = 8 is marginal (|d| = 7.99).

**Results [N].**
- **Multiplicity: yes, small.** The root-finder found 266 valid H1 histories across the hosts (counting one and two slits together). No launch has more than one valid H1, so the multiplicity is at most 2 (H0 + H1).
  - Under G1 most hosts have H1 for part of the window.
  - Under G2, only host (−4.2, 10), T = 8 has H1 (3 launches), and there H0 fails, so the multiplicity is 1 (H1 only).
  - Several hosts have zero raw roots from the start grid. A miss is possible, since the start grid does not guarantee completeness.
- **Exclusion: one candidate.** In G1, host (3, 8), T = 8, launches with θ between −19.20° and −19.04° (refined edges) have H0 failing and no valid one-collision H1. That is a zero-solution launch *within the enumeration*. Since histories with several traversals or collisions are not enumerated, this is **not** evidence against EKT, who report no initial trajectory without a consistent solution (not a quotation; per #407). It is most likely truncation.
- **Dependence on slit 2 for slit-1 launches: none.** The total over all CTC hosts and both gluings is **0**. Every refined edge, including the candidate exclusion band, sits at the same θ with one slit or two.

**Slit-2 argument, redone (no w ≈ d/T) [A].**
- Each history is four straight segments: the young ball before and after the collision, and the older ball before and after.
- The slits enter *only* through the barrier filter on those segments: the roots themselves are slit-independent. So for a slit-1 launch, slit 2 matters iff some valid segment crosses y = 2 inside slit 2, or a segment blocked at slit 2 when it is closed becomes a needed path when it is open.
- In every root found, no counted segment crossed at slit 2. The young ball's paths go through slit 1 or stay above the barrier, and the older ball's paths stay above it or are absorbed after the collision, which changes nothing.
- This is a statement about the scanned hosts. A host where the older ball's pre-collision path threads slit 2 would need A and the emergent direction to line up with slit 2, and none of ours does.

## Which-route kill condition

- **What a record would be.** A which-route record at the slits is part of the world and of the consistency map.
- **Passive record.** One that does not change any ball's motion, such as a pointer flipped without recoil in the test limit, leaves every consistency equation and so every multiplicity unchanged. It only labels histories.
- **Active record.** One that exerts a force, or is a hard body, enters the collision geometry. It can create or destroy H1 families.
- **Kill condition:** a slit-2-dependent multiplicity (none found in the rerun), if one were found, would be removed by any record that blocks or deflects the older ball's slit-2 passage. A record that only labels it would not remove it. Whether that labelling changes a *pattern* depends on a counting rule over multiple histories (#399), which this batch does not supply.

## Answer to the kill check

- **First run:** void (gluing defect), with no verdict from it.
- **Rerun:** Set 2's lever, multiplicity, exists, at most 2 here. One exclusion candidate turned up, but it is probably an artefact of truncating the enumeration.
- **Neither multiplicity nor exclusion depends on slit 2 for any slit-1 launch** in 9 CTC hosts × 2 gluings.
- **Set 2 is weakened: L1 → L0–L1.** Reopen only if a host is found whose older-ball path threads slit 2, together with a counting rule over histories (#399).

## Weak points

1. Idealised translation mouth. It gives continuum H1 families only because the gluing commutes with a shift along w in space and time (#398: a continuum needs a symmetry). Any normal-reversing gluing makes the emergent velocity depend on the entry point, and the generic count (4 unknowns, 4 equations) gives discrete families [A]. The translation rule is also not exterior-to-exterior (see Model). EKT's spherical mouths, with lensing, give discrete or infinite families, which were not modelled.
2. Only one traversal and only one collision. Multi-traversal histories ("multi" counts) are not enumerated.
3. Absorbing, point-like slit edges. Reflecting walls would add bounce paths.
4. Ten hosts and 0.5° launches; the t_c grid has 600 steps up to 40. The structural argument suggests special hosts exist, so a dense scan is the next check.
5. 2D and nonrelativistic.

6. The rerun enumerates only one traversal and one collision. Root-finding from a start grid is not guaranteed to be complete. No orientable mirror gluing was run.

Ledger: L98–L102 (L101 records the Lead ruling).
