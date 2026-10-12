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

| L24 | analytic (seam) | **Sheets existence (batch-06 A):** explicit non-regular 3-sheeted branched cover, codim-2 timelike seams, transposition monodromy; an aimed path forks into $e=2$ sheets carrying identical germs (second seam on one branch only gives a gap or end, not a different state; #348 review R1) | batch-06; #331 A; #336 | **Parked** (#349; #350 R1–R3) | Breaks H1, H5. Fork is in one host; the lift rule picks $e$ of a continuum of minimising directions (weak point); seam matter undefined. |
| L25 | analytic (seam) + observer extent | **Sheets typicality (batch-06 B):** point observers: hitting dense and meagre (missing residual); observers of extent $\sim\ell$: hitting open dense | batch-06; #336 (a),(d),(f); L11 | **Template** (#349, #350): B1 live as template (dense but meagre, KMS analogue); B2 parked (#336 (f) costs; jet/patch lock); B2 radius thresholds per #349: $\ge\ell/\sqrt2$ always hits, $\ell/2$–$\ell/\sqrt2$ in strips, $<\ell/2$ missing open | Topological, no measure. B1's density claim is a sketch; B2 owes #336 (f) C1–C3, and the fork is which torn piece is the observer (law-of-R risk, L23). |

| L27 | topology (static) | **Symmetry bound (batch-07 Set 1):** the germ fixes the cover $\tilde M$; $\pi_1$ must be a free, proper, non-timelike discrete subgroup of $\mathrm{Isom}(\tilde M)$ | batch-07; Theorems A–B; Prop 7.2 | **Awaiting final verdict** (#352, #353; pending David) | Constrains without fixing. Multiplicity only on symmetric covers; countable for finite-volume hyperbolic quotients (Mostow), continuum if flat or infinite-volume; no split by itself. #352: countable only for cocompact hyperbolic, dim ≥3 (Mostow/Prasad); 'generic' topological only. Known (#353): Clifford–Klein, Wolf. |
| L28 | observer state (memory) | **Self-signal return (batch-07 Set 2):** the observer's own light returns around a handle at a proper time $\tau_\Gamma$ fixed by the geometry, splitting the compatible set by $\pi_1$ | batch-07; creative-tweaks (the ant's trail) | **Lead set** (David 3:53 PM; awaiting final verdict, #352, #353) | Escapes the nested-prefix and identical-state traps only by adding a record (memory) to the state; needs an emitting body; ensemble narrowing, not motion; under (M1) the shares per arm are equal, not ∝ number of worlds. #352: genuine split (learning which world, not motion); countable, not necessarily finite; lock and split-rule questions are David's call. Known in spirit (#353): Ellis small universe, CSS observer copies. |
| L29 | observer state + split rule | **L28 developed (batch-08):** memory-augmented state $(O,\rho)$ with self-signal records; split rule by records; finite partition at each $\tau$ and countable cumulatively for crystal covers; counting by index exhaustion (conjecture: count gives Born (to be derived, not assumed)) | batch-08; L28; #352, #353 | **Live** (counting degenerate: L30, #355) | Sketches only. Needs crystal covers; count needs exhaustion-independence; flat stays a continuum; accelerating hosts few or no splits; conflicts with Paper 1's $\sim$ (working assumption 2). |
| L31 | counting (conditional shares) | **Batch 09:** exact conditional echo-record shares in $\mathbb Z^2$, $\mathbb Z^3$ crystal covers (HNF enumeration); index, covering-radius and word-length listings | batch-09; L29; L30 | **Result** (degenerate) | Shares are 0/1: 'no new echo' → 1 before full rank, a single world after; listings agree only trivially; no Born-like structure. Conjecture label applies; separate from (M1). |
| L33 | particle | **Batch 10 Set 1 (lead): Hadley 4-geon** as the particle; position read from scattered beacon returns; hosts split by geon placement | batch-10; David 4:06 PM | **Pending David on CTCs** (relaxing #352 for geon hosts; #361, #362) | Hadley content unchecked; time-orientation/CTC questions open; position uncertainty needs relaxed analyticity or Set 2's reading. |
| L34 | particle (topological) | **Batch 10 Set 2: position as gluing**: partner-mouth location = which Γ; under the analytic lock the only uncertain position is topological | batch-10; L27, L28 | **Reduces to self-echo** (L28/L29; #361) | Needs exact mouth isometry; returning loop. |
| L35 | particle (news) | **Batch 10 Set 3: radar to a localised feature** in a $C^\infty$ host | batch-10; batch 05; #346 | **Live, needs a reflector** (#361) | Breaks H1; null-boundary claim unverified (#346). |
| L36 | measurement (CTC round trip) | **Batch 11 Set 1: consistency branches**: EKT-type multiple self-consistent solutions of the beacon round trip through the geon's CTC give distinct returned records = worlds | batch-11; David 4:17 PM; L7; L33 | **Revised** (#364, #365): replies lie beyond the observer's Cauchy horizon (prefix or motion split); EKT gives infinitely many solutions; needs matter | Linear test signals probably give one reply (Friedman et al. 1990 shows existence, "benign"; uniqueness is Friedman–Morris 1991/1997); needs an interacting signal; 'solutions = worlds' needs content in the world or back-reaction. |
| L37 | measurement (extensions) | **Batch 11 Set 2: extension branches**: non-unique extensions past the geon's chronology horizon return or don't return the signal; the observer's record splits | batch-11; #361 | **Revised** (#364 (d)): the observer's own path depends on the extension (ends or diverges); #352 relaxation approved (David 4:16 PM) | Unchecked that extensions differ on the signal path; uses #352 relaxed to $U$ (approved, David 4:16 PM). |

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

## Lesson L26 (batch 06)

A fork that's real in the geometry but invisible in the states is the nested-prefix pattern again. For branches to differ in the states, the sheets must differ in their metric, and then nothing natural picks the continuation.

Batch 07 is held pending David's measure answer: whether a continuum of worlds with (M1) weights is acceptable, versus requiring countable branches. L26 makes that answer decisive.

## David on (M1) and branches as geometries (2026-10-12 3:43 PM ET, relayed via Physics Lead, not signed; verbatim)

> Can you explain in simple terms what M1 means? Are we saying the weight is proportional to the number of worlds? If so, that is acceptable. I do not consider that to be circular reasoning. Also, if branching coincides with different geometries in each branch, that has always been my intuition: branch A means geometry (fundamental group) A, B means B, and so on. Somehow, the local state teaches the observer something about the global state. Which seems impossible, but only because we haven’t yet figured out how to make it possible.

**L23 status: pending David's answer.** Counting is not relied on as a rule. Open, flagged for David. His 3:43 PM acceptance of weighting by counting worlds was conditional on (M1) meaning that; (M1) as recorded is per-vertex EPP1, which is not counting worlds. Whether he accepts (M1) as recorded, or a world-counting rule (EPP2 or (M2)), is his call; until then L23's status is unchanged.

**(M1) as recorded** (v0.10.1 §11): "**(M1)** Per-vertex EPP1, the working postulate here, ruled by David at L3. It needs no named cut: it is the count at the depth-1 cut anchored at the current state, so its weights are functions of that state (Problem note 6)." EPP1 (v0.10.1 §1): "at a branch point, equal weight on each arm in force. … **EPP2**, weight by ensemble size, is kept as a foil." v0.10.1 §1: "Per-vertex equal weight is not Paper 1's count: at a named finite cut the two agree iff $\prod_{w<v}\deg(w)$ is constant on the cut."

**(M1) in plain language.** (M1) says: whenever the observer reaches a branch point, each way onward gets an equal share, and a whole history's weight is the product of the shares along it. That share does not depend on how many worlds lie behind each way onward, so (M1) is **not** literally "weight proportional to the number of worlds". That rule is EPP2 ("weight by ensemble size"), which v0.10.1 keeps only as a foil; Paper 1's count of distinct evolutions at a cut is the not-adopted (M2). The two agree only in special cases: at a given cut, exactly when every history to it passed through branch points with the same product of arm counts. If David means "count the worlds", that is EPP2 or (M2), not (M1), and which one he intends is his call.

## David on counting and the Born rule (2026-10-12 3:47 PM ET, relayed via Physics Lead, not signed; verbatim)

> Counting doesn’t make it circular. If counting produces the Born rule, that’s not circular. That’s the goal. It is acceptable for us to conjecture that the count produces the Born Rule, and that’s circular if we stop our work, but that’s an intermediate step in our work. The next step will be to look for a reason that the Born rule is inevitable, inescapable, at which point we stop putting it in by hand.

**Physics Lead's Lead reading (relayed).** Counting worlds is allowed as a working conjecture in creative sets, labelled "conjecture: count gives Born (to be derived, not assumed)". It is kept separate from (M1), which is unchanged at L3. L23 is not lifted as a settled rule.

## Standing rule (counting)

Any creative set that uses counting worlds must (i) carry the label "conjecture: count gives Born (to be derived, not assumed)"; (ii) state what would make the count inevitable; and (iii) state how the worlds become countable. (M1) is unchanged at L3, and counting is never presented as (M1).

## Working assumptions for exploration (David Strayhorn, 2026-10-12 3:53 PM ET, relayed by Physics Lead, Physics Lead chat, not signed; verbatim; not changes to the paper)

1. "Memory: yes, let’s run with that. But we will need eventually to consider how the memory is stored - is it part of the state itself? - but for now let’s just say yes, it can remember received signals."
2. (On splitting with identical patches) "Again, let’s say yes and see where that takes us."

**Open item.** How memory is stored (is it part of the state itself?).

**Lead reading (Physics Lead).** Learning which world is acceptable, per David's 3:19 framing. L28 is the lead set; batch 08 develops it (L29).

## Lesson L30 (batch 08; Geometry #355)

Degeneracy: under natural cutoffs (index or volume), counting worlds in crystal covers gives the "no echo yet" share 1 at each fixed time. For $\mathbb Z^3$, subgroups of index $\le N$ grow like $N^3$, those containing a given element only like $N^2$. A systole cutoff gives no finite sets; diameter is likely the same (unverified); word length is ill-posed until generators are named. The count is over $E_{\mathcal W}$ (pointed worlds), not $E_M$.

## Lesson L31 (batch 09)

In crystal covers, counting worlds gives only 0/1 conditional shares: degenerate before the echoes span full rank, deterministic after. A non-trivial share would need a host class whose record-consistent subgroup counts grow like the total (not $\mathbb Z^n$), or records that stay ambiguous at full rank.

## David on focus (2026-10-12 4:03 PM ET, relayed by Physics Lead, Physics Lead chat, not signed; verbatim)

> Let’s focus on our successes. I am encouraged by the fact that branching can happen at all, and that the fundamental group can play a part. We shouldn’t worry yet about the precise probabilities, especially considering that we have not yet created a model of how the observer can measure the position of an external particle.

**Status.** The old batch 10 (non-abelian count) is cancelled. The probability and counting line (L29's counting, batches 08–09) is **parked**; L30 and L31 stand as results (with #358, #359).

## Successes so far

- **Branching by world exists** (L28, L29). With a memory record in the state (David's 3:53 working assumption), compatible hosts that agree on the observer's germ split genuinely when their records differ: not a nested prefix, not an in-host fork, and with free fall deterministic in each world (branch A = world A).
- **$\pi_1$ enters through returning records.** The observer's own signals return around handles at times and directions fixed by the geometry. So the fundamental group is what the compatible worlds differ in, and what the record reveals step by step (L27 bounds which $\pi_1$ are possible; L28 and L29 split by it).

## David on geons (2026-10-12 4:06 PM ET, relayed by Physics Lead, Physics Lead chat, not signed; verbatim)

> Rule out geons? I don’t recall ruling out geons. I like Hadley’s 4-geons.

Hadley's 4-geons are the lead particle model for batch 10. Paper 1 contains a geon remark (#339) whose provenance Literature is checking; David does not recall ruling geons out. Hadley references stay unchecked until Literature verifies them.

**Note.** README line 18 says 4-geons live in spacetimes that admit CTCs; Hadley 1997 requires CTCs (#362 S3).

## Central hypothesis (David, 2026-10-12 4:17 PM ET, relayed by Physics Lead, Physics Lead chat, not signed; verbatim)

> Hmm, maybe that’s what it means to observe a particle? A signal goes from the observer to the particle’s CTC and comes back to the observer, communicating information about the particle’s state?

Central hypothesis of batch 11 (L36, L37). Measurement = round trip of the beacon signal through the geon's CTC region, back into the observer's time-oriented record. Also recorded in `charter.md`.

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
- 2026-10-12: #350 strings and #349 corrections applied to batch 06; L24 parked; L25 kept as template (B1 live, B2 parked); lesson L26; batch 07 held.
- 2026-10-12: David's 3:43 PM words recorded; (M1) quoted and explained; L23 no longer a blocker in itself; batch 07 (L27, L28).
- 2026-10-12: #353 S1–S4 and #352 repairs applied to batch 07; L23 pending David; L27/L28 awaiting final verdict; David's 3:47 PM words, Lead reading, counting standing rule; Items for David.
- 2026-10-12: David's 3:53 PM working assumptions recorded; memory-storage open item; L28 lead set; batch 08 (L29).
- 2026-10-12: #356 S1–S2 and #355 corrections applied to batch 08; L29 live with counting degenerate; lesson L30; 3:53 citation changed to 'relayed by Physics Lead, Physics Lead chat'.
- 2026-10-12: batch 09 (L31): conditional shares computed for Z^2, Z^3; degenerate 0/1.
- 2026-10-12: #358/#359 verdicts on batch 09; David's 4:03 PM words; counting line parked; Successes so far.
- 2026-10-12: David's 4:06 PM words on geons; batch 10 (L33–L35), structure only.
- 2026-10-12: #362 S1–S3, Hadley marks and prior art; #361 corrections; L33 pending David on CTCs, L34 reduces to self-echo, L35 live (needs a reflector).
- 2026-10-12: David's 4:17 PM hypothesis (ledger, charter); batch 11 (L36, L37).
- 2026-10-12: #365 S1–S3 and #364 verdicts on batch 11; L36/L37 revised (#364 (d)); #352 relaxation for geon hosts approved by David at 4:16 PM.
