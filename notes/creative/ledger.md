# Creative-tweak ledger (Creative Lead; working, do not merge)

**Status.** Working record, not adopted. Nothing here changes `public-papers/observer-space-framework/versions/v0.10.1-prose.md` (the current draft) or any topology, throat convention, law of $R$, (M1) or (A).

**Method.** infinite-harness `docs/lessons/creative-tweaks.md` (David, 2026-10-12, relayed): change **one** concept a little, then judge by taste: TT1 well-posed; TT2 motivated for its own sake (LT2); TT3 small and natural; TT4 smuggles no measure, count or target. Check existing structure first.

**Charter.** `notes/creative/charter.md` (David's notes, verbatim). **Reviews.** Geometry #334, Literature #335.

**Sources.** S1 = `creative-tweaks.md` (David's words and examples). S2 = physics #331 (Geometry, `notes/branching-regularity-tweaks.md`). S3 = physics #332 (Literature review of #331). D = v0.10.1 prose (§8.1 CWS singleton, §8.2 Option E residue, §11 open list). Entries marked **CL** are Creative Lead proposals with no source behind them yet and no literature check.

**Goal (S1, S2 header).** "Mostly deterministic": deterministic stretches, discrete branch points, no CTCs, by changing the meaning of one word.

| # | Word | Tweak | Source | Status | Taste notes |
|---|---|---|---|---|---|
| L1 | observer dimension / embedding | observer of higher dimension than spacetime, or a postulated embedding (the ant) | S1 | **Parked** | Fails TT1 unless the ambient space is physically singled out; embeddings are not unique (Nash, Clarke; per S1). |
| L2 | (none: check before adding) | intrinsic before extrinsic: marked trail, holonomy, area count give $\pi_1$ intrinsically | S1 | **Standing rule** | Applied to every set below. |
| L3 | analytic | analytic off a thin codim-2 branch set $\Sigma$ (branched cover, sheet count $n$) | S2 §2 (Candidate A); batch-01 Set 1 | **Live, ranked first** (#334, #335); per #336, ensemble only unless an observer tube is added (L11) | Only candidate with discreteness from a topological integer. Costs: $\Sigma$ is a host choice; hits are non-generic; sheet rule undefined; string source not a Geroch–Traschen distribution (S3 R3); amplitude hook is borrowed QM on multiply connected spaces (S3 R4). Conical defect gives a continuum. |
| L4 | smooth | piecewise analytic, $C^k$ junctions (Option F) | S2 §3; D §8.2 | **Dead** | Already ruled: finite-order matching cannot create a branching edge (v0.6 banner; D §8.2). Branching would come from the graph, not the tweak. |
| L5 | analytic | Gevrey $G^s$, $s>1$: agree on a region, then diverge | S2 §4; S1 | **Reframed** | Corrected by S3 R1/R2: agree-then-diverge is standard GR non-uniqueness (Choquet-Bruhat–Geroch 1969; Chruściel–Isenberg 1993, analytic cases too) and the bump argument works in any non-quasianalytic class, $C^\infty$ included, so Gevrey is not doing the work. It is host non-uniqueness, not branching of motion. Gives a continuum. David liked the *kind* of idea (S1); the live residue is L8. |
| L6 | quasianalytic | other quasianalytic (Denjoy–Carleman) classes | S2 §4 | **Dead** | Keep "jet determines germ", so nothing new (S2). |
| L7 | determinism (global) | EKT-style: local law deterministic, multiplicity from a global consistency condition with several solutions, without CTCs | S1; S2 §0 | **Parked, open for recycling** (#334; recycled in L12) | Template only (Echeverria–Klinkhammer–Thorne 1991). No candidate condition yet. |
| L8 | observer state | **CL.** In a non-quasianalytic host class, "observer = infinite jet" and "observer = germ" come apart (S2 §4). Take the jet as the state. Then CWS switching at a shared *jet* rather than a shared germ would no longer force the singleton of D §8.1. | S2 §4 + D §8.1; CL; batch-01 Set 2 | **Parked** (#334, #335): collides with Paper 1's 'smooth is not enough' lock; reopening is David's call | Branching in motion, not just host (answers S3 R2). But continuum (any bump), so it needs a discreteness rule (TT4 risk). Must recheck §8.1's (E1)/(E2) argument; unchecked. |
| L9 | CTC | **CL.** Move "closed curve" from spacetime to observer space $V$: consistency conditions on loops of states (cf. self-loops $(O^u,O^u)$, D §11) instead of loops in spacetime. | S1 word list; D §11; CL; batch-01 Set 3 | **Parked** (#334): a free-fall loop has only one consistent history | Gives L7 a home without spacetime CTCs. Undefined: what "consistent" means on $V$. TT2 risk: could become a disguised law of $R$. |
| L10 | analytic | **CL.** Branching from the host's own analytic continuation: monodromy around complex singularities of the maximal analytic extension, where real-path continuation stays unique | CL | **Parked** | Probably fails: S2 §0 and S3 R2 say continuation along one real path has no monodromy. Recorded so it is not reinvented. |
| L11 | observer state | **CL.** State = coarse-grained state at the host's own topology/seam scale ℓ; $r_0$ set by the host; test the $r_0/\ell\to\infty$ limit (charter: low-energy approximation, k→∞ pattern) | #336 (f); charter; CL | **Parked** (batch-02 Set 1; #338, #339): no finite limit, since counts grow like $(r_0/\ell)^2$; needs a sneaked-in measure | Answers #336 cost C1 if the limit exists; C2 is the tweak; C3 remains. |
| L12 | consistency (recycles L7) | **CL.** Consistency around $\pi_1$ loops inside the observer tube | L7; charter; CL | **Parked** (batch-02 Set 2; #338, #339): holonomy is single-valued in free fall; borrows quantisation | Discrete from $\pi_1$. High borrowed-QM hazard (#332 R4); must avoid #334's single-history objection. |
| L13 | branch point | **CL.** Branch where the map $P(O)\to$ host stops being injective ($P(O)$ itself stays simply connected, #339 R2) | CL | **Parked** (batch-02 Set 3; #339): already killed by `papers/patch-edge.md` ("The hitchhiker story is dead at the boundary too"; Prop. 7.2 "quotients do not lengthen past the cover") | Likely only ensemble structure (#331 §0, #336). |
| L14 | seam hitting | point-observer hits on codim-2 seams | #336 (a)–(e) | **Dead** for motion | Meagre, codim-1 in data; no focusing; walls have no sheets. Sheets (L3) reduce to host-ensemble monodromy unless L11 or #336 (f) is adopted. |
| L16 | manifold | Lattice geodesic ties (batch-03 Set 1) | batch-03 | **Parked** (#341, #342) | Ties are two-point, not initial-value: the endpoint is a law of $R$ in disguise; diverges as ℓ→0; drops H1; tie counts as weights = count by fiat. Reopens the geodesic-lifts lock (David's call). |
| L17 | motion law | Ride the matter, fork at degeneracies (batch-03 Set 2) | batch-03 | **Parked** (#341, #342 R2) | Continuum at degeneracies, not discrete; frame undefined in vacuum; degeneracies rarely hit. Reopens the lock (David's call). |
| L18 | motion law | Self-force needs memory (batch-03 Set 3) | batch-03 | **Parked** (#341, #342 R1) | Third order only for charge; for mass a past-path tail (Quinn–Wald); reduction of order restores uniqueness. Reopens the lock (David's call). |
| L20 | analytic (host) | Finitely describable piecewise-analytic hosts: compatible hosts diverge across null junctions into a countable set (batch-05 Set 1) | batch-05; CL | **Parked** (#346; #347 R2; TT2) | Breaks H1, H5. #346: step/sandwich waves exist, but impulsive and Aichelburg–Sexl waves are $C^0$ (excluded by $C^{1,1}$); vacuum $C^{1,1}$ seams are forced null, and non-null seams need an Israel shell (matter); real parameters give a continuum, countable only by restricting constants (a choice) and still dense; "finitely definable" is ill-posed until a class is named; free fall across a seam is unique. #347 R2: countability brings a measure by fiat (Paper 1 §6 counting; Solomonoff-style prior). TT2: free choice of class. |
| L21 | (dropped, batch 05) | E1–E8 | batch-05 | **Dead** | Continuum (C^∞/Gevrey, k-jets, microstructure, unrestricted junctions), no divergence (quasianalytic, topology only), no shared $O$ (discrete solitons), or off-target (forks inside a host). |

| L24 | analytic (seam) | **Sheets existence (batch-06 A):** explicit non-regular 3-sheeted branched cover, codim-2 timelike seams, transposition monodromy; an aimed path forks into $e=2$ sheets with different futures (second seam on one branch only) | batch-06; #331 A; #336 | **Proposed** | Breaks H1, H5. Fork is in one host; the lift rule picks $e$ of a continuum of minimising directions (weak point); seam matter undefined. |
| L25 | analytic (seam) + observer extent | **Sheets typicality (batch-06 B):** point observers: hitting dense and meagre (missing residual); observers of extent $\sim\ell$: hitting open dense | batch-06; #336 (a),(d),(f); L11 | **Proposed** | Topological, no measure. B1's density claim is a sketch; B2 owes #336 (f) C1–C3, and the fork is which torn piece is the observer (law-of-R risk, L23). |

## Lesson L15 (after batches 01–02)

Every set so far fails the same way. Free-fall continuation is unique (`papers/geodesic-lifts.md` Prop 3.2; no monodromy along a single path, #331 §0, #332 R2). So the "branching" each set finds turns out to be **which host we are in** (the ensemble $E(O)$), not the motion. Rule for batch 03 onward: a set must name which hypothesis of Prop 3.2 it breaks and give an independent physical reason for breaking it. Otherwise it only feeds the ensemble.

## Summary after batches 01–03 (plain language)

Nine sets in, the lesson is the same every time. As long as the world is analytic and observers follow geodesics (Prop 3.2 / Cor 3.1 in `papers/geodesic-lifts.md`), a traveller's path never forks. Every apparent branching we found (seams, tubes, handles, patch edges, loops) turned out to be about which host world we are in, not about the motion. The only routes to a genuinely forking path break that starting point: a different motion law, a non-manifold world, or a law whose paths are not analytic curves (escaping via H5, which dodges Cor 3.1). Each of these reopens the lock "W is real-analytic; observers follow geodesics", so the high-level question for David is whether to reopen it, and if so, which part.

## Ruling (David Strayhorn, 2026-10-12 3:14 PM ET, relayed via Physics Lead, not signed)

> Yes, Creative Lead may propose ideas that relax the analytic/geodesic lock, as exploration only.

Recorded in `notes/creative/charter.md` (addendum). Batch 04 is the first batch run under it.

## Lesson L19 (batch 04)

No set survived the rules once the lock was relaxed (see `batch-04.md`). Two failure modes recur. (i) When ODE uniqueness breaks for a physical reason, the alternatives form a continuum (Peano-type non-uniqueness, free data on a null surface, extensions past a Cauchy horizon in $C^\infty$). (ii) Where the alternatives are discrete (sheets, eigen-frames, branch counts), the branch locus has codimension ≥2 and is rarely hit (#336, #341), or the alternatives disappear rather than fork. The analytic/geodesic lock was not the only barrier.

## Reframing (David Strayhorn, 2026-10-12 3:19 PM ET, relayed via Physics Lead, not signed; verbatim)

> I want to see if I understand. You say that an observer in free fall has exactly one way to continue, so anything that branches turns out to be uncertainty about which world we’re in, not a fork in the observer’s own path. Are you saying this is a good thing or a bad thing? The best case scenario is that exactly what you describe. Within any one world, there is deterministic free fall without branching. Within observer space, branching happens due to uncertainty over which world we’re in. Branch A means the observer is in world A; branch B means the observer is in world B. Within world A or world B, branching doesn’t occur.

## Lesson L22 (batch 05)

Under the reframing, "how does the motion branch?" becomes "what class of data may arrive from outside the observer's shared past?" Analytic and quasianalytic classes give no branching; $C^\infty$ and Gevrey give a continuum. Countable branching needs a countable data class with a physical reason, and that reason is the open problem.

*Context (Geometry's caveat, 2026-10-12 3:22 PM ET, relayed via Physics Lead):* under the current lock, histories are nested prefixes, never forks, because some hosts' geodesics end early (Taub–NUT style). Compatible hosts give the same sequence of states for as long as each lasts; they differ only in where it stops.

## Lesson L23 (batch 05; with David via Physics Lead)

Under David's framing, any physical restriction that makes the compatible futures countable also chooses the measure. So the real question may be the measure, i.e. whether a continuum of compatible hosts with (M1) per-vertex weights is acceptable, rather than how to force countability.

## David on special aim (2026-10-12, relayed via Physics Lead, not signed; verbatim)

- 3:28 PM ET: "What’s wrong with special aim? If our desired style of branching can happen by special aim, then that’s still progress, right?"
- 3:30 PM ET: "Yes, revive sheets. Maybe you need special aim to hit the patches. On the other hand, maybe you need special aim to miss them! Is the glass half empty or half full?"

Batch 06 revives L3 as L24 (existence) and L25 (typicality), recorded separately.

## Change log
- 2026-10-12: created (batch 01).
- 2026-10-12: moved to notes/creative/; charter added; TT1–TT4 rename (#335 N1); verdicts from #334/#335 applied (L3 live and ranked first; L8, L9, L7 parked); #335 R1 applied in batch-01.
- 2026-10-12: batch 02 after #336: L11–L14 added; L7 open for recycling; L3 note per #336.
- 2026-10-12: batch-02 verdicts (#338, #339): L11–L13 parked; lesson L15 added.
- 2026-10-12: batch-03 verdicts (#341, #342): L16–L18 parked; summary after batches 01–03 added.
- 2026-10-12: David's 3:14 PM ruling recorded; batch 04 drafted, all candidates dropped; lesson L19.
- 2026-10-12: David's 3:19 PM reframing recorded (verbatim, replacing an earlier paraphrase); batch 05 (Set 1 proposed, L20; drops L21); lesson L22. batch-04 D7/D8 updated per #344.
- 2026-10-12: #347 R1–R3 and #346 repairs applied to batch-05; L20 parked; lesson L23.
- 2026-10-12: David's 3:28 and 3:30 PM words recorded; batch 06 (L24, L25).
