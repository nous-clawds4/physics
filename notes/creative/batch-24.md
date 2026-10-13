# Batch 24: Set 2 first kill check: does a second slit change self-consistent multiplicity? (Creative Lead; do not merge)

**Status.** CTC exploration only. Structure only, with no weights; classical; no Born rule; no $|a|^2$; (M1) untouched at L3. Nothing goes into `versions/` or `papers/`. Stacked on batch 23 (#407 at 16e0b45). Ledger rows L98–L101. Script: `notes/creative/batch-24/ekt.py` (sha256 `d65230e5012f2b113fd7ddfebb713ae5be196005d14e34f64d59dba8496e9d94`); output: `results.txt` (sha256 `1cf75b631550fac2c507ed89667bc87816ff61f9740254ac05e86e9cea621106`).

**Lead ruling** (Physics Lead, 9:45 AM ET 2026-10-13; a Lead ruling, not David's): batch 24 runs Set 2's first kill check, in the offset-mouth host (#385 L56) with an EKT-style hard-sphere billiard, structure only and with no weights.

---

## For David (plain summary)

- **The question.** In a world with a time-shifted wormhole, a ball can come back and knock its own younger self. Some launches then have more than one self-consistent story. Does opening the second slit change how many stories a launch *through the first slit* has?
- **First try: void.** Our first model wormhole was glued wrongly: balls came out *into* the far mouth instead of out of it. Geometry caught this, so those results don't count. They are kept below only as a record.
- **Rerun with correctly glued wormholes**, in three versions. One of them is the only kind that could describe a real (orientable) space. We found every consistent story with at most one trip and one knock, using a root-finder, for launches through slit 1, with slit 2 closed and then open. We used nine setups that really allow time travel, and dropped one that doesn't. (A second version in the earlier rerun was itself glued wrongly. It has been replaced.)
- **What we found.**
  - Some launches have two consistent stories, never more.
  - In two of the non-orientable versions, a narrow band of launches about 0.16° wide had *no* story within our search. That would be a forbidden launch. It may instead be a gap in our search, which doesn't include stories with more trips or knocks; we can't tell which until a deeper search is run. The orientable version has no such band.
  - **Opening slit 2 never changed anything for a slit-1 launch,** in any setup or any version.
- **Verdict.** In this check, Set 2 does not give the needed effect. Slit 2 could only matter if one of the balls' straight pieces of path crossed the barrier at slit 2, and none did.

---

## Model, regime and simplifications

- **Space and bodies.** 2D, nonrelativistic, with unit launch speed. Equal-mass hard spheres (discs) of radius r = 0.1 and elastic collisions, in the style of Echeverria–Klinkhammer–Thorne (PRD 44 (1991) 1077; verified, Crossref, per Literature; readings per #365).
- **Idealised mouth.** Two circles of radius s = 0.5, A and B. A ball centre reaching B at B + s e(φ), at time t with velocity w, emerges at A + s e(φ) at time t − T with the same velocity. This is a pure translation by d = B − A plus a time shift: no rotation, no lensing, no throat dynamics. **Defect (Geometry, #408 review):** since entry needs w·e < 0, this rule sends the ball into disc A, so it glues the exterior of B to the interior of A and is not an exterior-to-exterior wormhole. A valid gluing reverses the normal (reflection w ↦ w − 2(w·e)e at A + s e; or rotation by π, A − s e, w ↦ −w + 2(w·e)e. The earlier "A − s e, −w" was a review error and is not exterior-to-exterior). The results below are void until rerun with such a gluing. It is the offset-mouth host, #385 L56. Per #398 and Literature M1 (#408), a fixed time shift T gives CTCs only if T exceeds the mouth separation |d| (c = 1). Host A = (−1.8, −3) has |d| = 9 > T = 8, so it is **not a CTC host**; host A = (4, 0.5) has |d| ≈ 7.99, just below T = 8 (marginal). It is a different host from the cylinder toy either way.
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
- **Friedman et al. 1990** (PRD 42, 1915; abstract only): the Cauchy problem in spacetimes with CTCs; for wormhole spacetimes self-consistency "seems to place no constraints on initial data" for a free field; the authors "suspect" this is typical for non-interacting classical fields, while "interacting classical systems can behave quite differently" (V-text per #365); a suspicion, not a theorem. Linear-field uniqueness: Friedman–Morris, PRL 66 (1991) 401 and CMP 186 (1997) 495 (bibliographic only, per Literature).
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

Script: `notes/creative/batch-24/ekt2.py` (sha256 `c3e333dc4f88931644c47b396ab22bdd7c89746418706a44c7dd97e883d7abeb`); output: `results2.txt` (sha256 `ba8d32e1c470c4a972a8395955527b84915dc02c68e0ad00ac428338fb572a18`). `ekt.py` and `results.txt` are kept as the void record.

**Gluings.** G1 is exterior-to-exterior; G2 as run is not (see below). Both were run because it was cheap (about 70 s).
- **G1 reflect:** B + s e ↦ A + s e, w ↦ w − 2(w·e)e. This is the minimal fix to the translation rule: same point label, normal reversed, tangent kept.
- **G2 invert:** B + s e ↦ A − s e, w ↦ −w (point inversion). **Void (Geometry review 2):** at A − s e the outward speed is w·e < 0, so the ball emerges into disc A, the same defect as the first run. `first_mouth` misses it because it starts inside A. The correct rotation-by-π rule is w ↦ −w + 2(w·e)e. **Replaced in the final `ekt2.py`** by G2 'rot' (A − s e, w ↦ −w + 2(w·e)e), and G3 'mirror' was added; an assertion now checks that the outward speed at emergence is ≥ 0.
- Orientability: a handle is orientable iff the circle map reverses the boundary orientation. G1 (e ↦ e) and rotation by π (e ↦ −e) both preserve it, so both hosts are **non-orientable** (exploration only, stated). The orientable choice is the mirror along d̂ (e ↦ Me, w ↦ Mw, then the normal flip). Geometry's probe ran the mirror and corrected rotation-π gluings: 0 slit-1 launches depend on slit 2.

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
- **Multiplicity: yes, small.** The root-finder found 260 valid H1 histories under G1 across the hosts (counting one and two slits together). The 6 under G2 are void. No launch has more than one valid H1, so the multiplicity is at most 2 (H0 + H1).
  - Under G1 most hosts have H1 for part of the window.
  - G2 rows are void (wrong-side emergence). With a corrected rotation-π gluing (Geometry probe), several hosts have H1, and there is one zero-solution launch in the marginal host (4, 0.5), T = 8.
  - Several hosts have zero raw roots from the start grid. A miss is possible, since the start grid does not guarantee completeness.
- **Exclusion: one candidate.** In G1, host (3, 8), T = 8, launches with θ between −19.20° and −19.04° (refined edges) have H0 failing and no valid one-collision H1. That is a zero-solution launch *within the enumeration*. Since histories with several traversals or collisions are not enumerated, this is **not** evidence against EKT, who report no initial trajectory without a consistent solution (not a quotation; per #407). H0 failure here is a direct computation. Geometry re-solved H1 inside the band with 8100 starts and found the same 2 roots, both invalid, so the band is robust to seeding within one traversal and one collision. The band is absent under the orientable mirror gluing. It may be truncation, but that is untested: EKT's result (standard account) is for their own host, and the number of consistent solutions depends on the physics (Mikheeva & Novikov, PRD 47 (1993) 1432), so it need not transfer to these 2D, orientation-reversing gluings. Status: open, pending a search with multi-traversal and multi-collision histories; neither a dark spot nor a counterexample.
- **Dependence on slit 2 for slit-1 launches: none.** The total over all CTC hosts is **0** for G1 (G2 void), and also 0 for the corrected rotation-π and orientable mirror gluings (Geometry probe). Every refined edge, including the candidate exclusion band, sits at the same θ with one slit or two.

**Slit-2 argument, redone (no w ≈ d/T) [A].**
- Each history is four straight segments: the young ball before and after the collision, and the older ball before and after.
- The slits enter *only* through the barrier filter on those segments: the roots themselves are slit-independent. So for a slit-1 launch, slit 2 matters iff some valid segment crosses y = 2 inside slit 2, or a segment blocked at slit 2 when it is closed becomes a needed path when it is open.
- In every root found, no counted segment crossed at slit 2. The young ball's paths go through slit 1 or stay above the barrier, and the older ball's paths stay above it or are absorbed after the collision, which changes nothing.
- This is a statement about the scanned hosts. A host where the older ball's pre-collision path threads slit 2 would need A and the emergent direction to line up with slit 2, and none of ours does.


### Final rerun (three gluings, pinned above)

The 72dd731 rerun's hashes (`eb6d28cb…434591`, `97dc9d76…cc66ea`) are superseded: the hashes above are for the final script and output. G1 'reflect' (non-orientable), G2 'rot' (rotation by π, corrected; non-orientable), G3 'mirror' (orientable). All are exterior-to-exterior (asserted). There are 9 CTC hosts; 33 launches across the slit-1 window (7.88°); 288 starts per launch; edges bisected 8 times.

| gluing | valid H1 per host, one slit (hosts in order: (−4.2,10)/8, /15; (3,8)/8, /15; (1,12)/8, /15; (−1.8,−3)/15; (4,0.5)/8, /15) | total (one + two slits) | zero-solution launches | slit-1 launches depending on slit 2 |
|---|---|---|---|---|
| G1 reflect | 18, 16, 32, 0, 23, 12, 0, 29, 0 | 260 | 1 band: host (3,8)/8, θ ∈ (−19.20°, −19.04°) | **0** |
| G2 rot-π | 0, 0, 20, 4, 4, 15, 4, 7, 0 | 108 | 1 band: host (4,0.5)/8 (marginal CTC), θ ∈ (−14.43°, −14.28°) | **0** |
| G3 mirror | 2, 23, 26, 11, 4, 21, 2, 17, 0 | 212 | none (H0 fails at one launch each in (3,8)/8 and (4,0.5)/8, but a valid H1 exists there) | **0** |

- **Comparison with Geometry's probe.** These numbers match it exactly: 260 under G1, the same per-host H1 counts for rotation-π and mirror, a zero-solution launch in host (4, 0.5) under rotation-π, none under the mirror, and 0 slit-2 dependence for all three gluings. They are my own rerun, not copied.
- **Multiplicity** is at most 2 (H0 + one H1) in every gluing.
- **The orientable host has no zero-solution launch.**

## Which-route kill condition

- **What a record would be.** A which-route record at the slits is part of the world and of the consistency map.
- **Passive record.** One that does not change any ball's motion, such as a pointer flipped without recoil in the test limit, leaves every consistency equation and so every multiplicity unchanged. It only labels histories.
- **Active record.** One that exerts a force, or is a hard body, enters the collision geometry. It can create or destroy H1 families.
- **Kill condition:** a slit-2-dependent multiplicity (none found in the rerun), if one were found, would be removed by any record that blocks or deflects the older ball's slit-2 passage. A record that only labels it would not remove it. Whether that labelling changes a *pattern* depends on a counting rule over multiple histories (#399), which this batch does not supply.

## Answer to the kill check

- **First run:** void (gluing defect), with no verdict from it.
- **Rerun:** Set 2's lever, multiplicity, exists, at most 2 here. Exclusion candidates turned up, one band each in the two non-orientable gluings and none in the orientable mirror. They are robust to seeding within one traversal and one collision. Whether it survives multi-traversal or multi-collision histories is open (it is slit-independent either way).
- **Neither multiplicity nor exclusion depends on slit 2 for any slit-1 launch** in 9 CTC hosts × 3 valid gluings (G1, corrected rotation-π, orientable mirror).
- **Set 2 is weakened: L1 → L0–L1.** Reopen only if a host is found whose older-ball path threads slit 2, together with a counting rule over histories (#399).

## Weak points

1. Idealised translation mouth. It gives continuum H1 families only because the gluing commutes with a shift along w in space and time (#398: a continuum needs a symmetry). Any normal-reversing gluing makes the emergent velocity depend on the entry point, and the generic count (4 unknowns, 4 equations) gives discrete families [A]. The translation rule is also not exterior-to-exterior (see Model). EKT's spherical mouths, with lensing, give discrete or infinite families, which were not modelled.
2. Only one traversal and only one collision. Multi-traversal histories ("multi" counts) are not enumerated.
3. Absorbing, point-like slit edges. Reflecting walls would add bounce paths.
4. (Void first run.) Ten hosts at 0.5° launch steps with a t_c grid. The rerun instead uses root-finding, 33 launches across the slit-1 window with bisected edges, and 9 CTC hosts × 3 gluings. A dense host scan is still the next check.
5. 2D and nonrelativistic.

6. The rerun enumerates only one traversal and one collision. Root-finding from a start grid is not guaranteed to be complete (Geometry's 8100-start check in the G1 band agreed). The orientable mirror gluing was run only in Geometry's probe; it should be added to `ekt2.py` and pinned. **Done in the final rerun (see Final rerun).**

Ledger: L98–L101 (L101 records the Lead ruling).
