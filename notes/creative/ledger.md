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
| L36 | measurement (CTC round trip) | **Batch 11 Set 1: consistency branches**: EKT-type multiple self-consistent solutions of the beacon round trip through the geon's CTC give distinct returned records = worlds | batch-11; David 4:17 PM; L7; L33 | **Revised** (#364, #365): replies lie beyond the observer's Cauchy horizon where the geon forms after a Cauchy slice (prefix or motion split; corrected by #367 (1): under the lock only a prefix, and the split is in the record); EKT gives infinitely many solutions; needs matter | Linear test signals probably give one reply (Friedman et al. 1990 shows existence, "benign"; uniqueness is Friedman–Morris 1991/1997); needs an interacting signal; 'solutions = worlds' needs content in the world or back-reaction. |
| L37 | measurement (extensions) | **Batch 11 Set 2: extension branches**: non-unique extensions past the geon's chronology horizon return or don't return the signal; the observer's record splits | batch-11; #361 | **Revised** (#364 (d)): the observer's own path depends on the extension (ends or diverges; corrected by #367 (1): under the lock it only ends or continues, and what diverges is the record); #352 relaxation approved (David 4:16 PM) | Unchecked that extensions differ on the signal path; uses #352 relaxed to $U$ (approved, David 4:16 PM). |
| L38 | survival beyond $H^+(S)$ | **Batch 12 (1):** in Misner/Taub–NUT the observer crosses the compact horizon in some extensions and ends in others; survival in all needs off-path ($C^\infty$) differences, i.e. a continuum | batch-12; #364 (d) | **Result** (#367: Misner verified for timelike; survival determined, not a fork; Taub–NUT unverified) | Positive reading holds among surviving branches; dropout is not an arm (§6.2). |
| L39 | outcome vs branch | **Batch 12 (2):** record partition coarsens the germ partition (analytic); they coincide only if worlds include content or back-reaction, and the reply map is injective | batch-12; batch 11 | **Result, corrected** (#367: record and germ partitions cross; case (d) same germ, different reply) | Can come apart: branch without outcome; outcome without branch; coarser outcome. |
| L40 | EKT countability | **Batch 12 (3):** generically countable (discrete traversal classes, isolated fixed points); continuum under symmetry or internal parameters | batch-12; #365 | **Result** (#367/#368 S3: smearing only for symmetric data; L27 tension softened; second source: Lossev–Novikov jinn loops) | Tension with L27: symmetric hosts give continua. |
| L41 | outcome vs branch (augmented state) | **Batch 13 (A):** in the germ+record state, the partitions nest: state branch ⊑ record class (outcome); outcome = a class of branches, refining as τ grows (fully only for n≤3, exact vectors, after full rank); 'branch := record class' would make outcome = branch by definition | batch-13; L29; #355, #359, #367 | **Result** (#370: cocompact Γ certifiable at finite τ; prior art Belnap 1992, #371) | Redefinition is a convention, not evidence (LT2): keep 'record branch' and 'state branch' both named. |
| L42 | survival (Taub–NUT, compact horizons, geons) | **Batch 13 (B):** Taub–NUT: a Misner-like dichotomy imprisoned geodesics are incomplete in one extension and cross in the other (no union of the two extensions is complete: comoving zero-momentum geodesics continue in neither, Misner–Taub 1969 §II C, relayed from external review, V-meta; confirmed by computation, #377; reported completeness of a non-Hausdorff maximal extension, Hájíček 1971, unchecked; corrected per #375 and Claude job 013 R5); only a measure-zero set is incomplete in both; compactly generated horizons: survival is a function of (extension, observer data), determined within each extension; Hadley hosts: open, and eternal geons may have no Cauchy surface | batch-13; #367 | **Result** (#370, #371: imprisonment relative; Misner = Geometry's computation; eternal geons: no Cauchy surface, comparison via germ+record) | Hawking–Ellis, Misner 1967, Hawking 1992: unchecked. |
| L43 | carrier | **Batch 14 Set 1:** interacting test body (matter pulse); null rays and linear fields give one reply per class (Friedman–Morris), so they cannot give EKT multiplicity; closes round-trip open item (a), conditionally | batch-14; David 7:45; #372 (a) | **live** | interaction is needed for multiplicity; matter law taken as given, not tuned (no law of R by fiat) |
| L44 | physical record | **Batch 14 Set 2C:** co-moving ledger of pre-existing geons; topology fixed from the start | batch-14; David 7:45 | **live** | answers "physical, encoded into spacetime" without topology change |
| L45 | topology-changing write | **Batch 14 Set 2A/2B:** write by topology change via CTCs (Geroch 1967 allows it with CTCs) or by non-Hausdorff splitting | batch-14; Geroch 1967, Tipler 1977, Borde 1994, Gibbons–Hawking 1992 (unchecked) | **parked** | 2A: CTCs at the observer, one per bit; also forbidden for reasonable sources (Tipler 1977, Borde 1994; single handles by Gibbons–Hawking 1992; #380), so it reopens only with exotic sources; 2B: circular (assumes the branching) |
| L46 | write mechanism | **Batch 14 Set 3:** integer winding of ledger bodies around a ledger handle, relative to a declared reference history (body-around-body is not topological in 3+1; #381), changed by carrier collisions; writes Type O only, beyond H⁺(S); ℤ/2 geons cannot write; positions and phases as exact-real record; deck labels and O/F flags are labels, not storage; flat holonomy parked (no write mechanism; stable under flat deformations, writable by curvature transients) | batch-14 | **conditional** (#380) | discrete only via capture into stable homotopy classes of bound orbits (raw winding advances under free motion; #380); the cut is a gauge; the write map must follow from dynamics |
| L47 | ledger in the state | **Batch 14 traps:** the ledger must be in the observer state (identical-state trap), so the state is the germ of the observer+ledger tube; this brings back #336's tube cost, with the scale set by the ledger's extent. #372 R2 concerns the observer's worldline germ; the observer-plus-ledger tube germ after a write does differ across worlds, by construction (#381) | batch-14; L29; #336; #352 | **open** | reconciles OP1 (where memory is stored) |
| L48 | handle orbits: pure Ellis | **Batch 15 Set 1:** massless Ellis has no bound timelike orbits and no stable circular orbits (V ≥ 1, maximum at the throat) | batch-15 [A, N] | **dead** (for the ledger) | nothing can be stored |
| L49 | handle orbits: Ellis–Bronnikov | **Batch 15 Set 2:** one stable class (attracting side); crossing the throat is escape on the repulsive side, i.e. ledger dropout; kick threshold √(V_b − V_c) (2.689 at m/k=0.3, L=6) | batch-15 [N] | **parked** | only one class |
| L50 | handle orbits: symmetric two-mouth toy | **Batch 15 Set 3:** discrete stable energy-band classes O±, T (throat-trapped), Th (bound, passing through the throat), Esc, separated by separatrices; not topological (slice S²×ℝ simply connected; #384); basins preserved under ±10⁻³ | batch-15 [N]; toy, exotic matter | **live (toy)** | discreteness from the wells, not a winding; Simpson–Visser, a geometry chosen first, whose source was identified afterwards (phantom scalar plus monopole, Bronnikov–Walia 2022, per Literature) (arXiv:1812.07114; NEC fails everywhere, ∫ = −πk+4m); radiation drives all classes to T |
| L51 | kick write | **Batch 15 Set 3:** one impulse reaches only bands open at the kick point (O+ → Th at proper speed 0.2677 for a physical boost, 0.1927 in the fixed-L convention; Th → Esc at 0.2907, L=3.8; #384); the record is the energy-band class at matched returns vs the unkicked reference, not the raw crossing count | batch-15 [N, A]; #381 | **live (toy), conditional** | test limit; radial kicks only |
| L52 | L47 tube scale | **Batch 15:** tube size set dynamically by the ledger's bound orbit (not chosen); geometric definition, not circular; the support moves with the record; Esc = ledger dropout needs a convention | batch-15; #336; L47 | **open** (acceptable in the toy) | answers #336's undefined scale here |
| L53 | ledger across the Cauchy horizon | **Batch 15:** joint crossing needs a common sign of p∥ (Taub–NUT) across the tube, an open condition for slow tubes; free ledger members keep their p∥ sign (Killing charge), so tear-off needs a binding force (#384); Misner: same-extension crossing survives, fixed-point geodesics end | batch-15 [A, sketch]; #367, #375, #377 | **open** | joint survival fixed by initial data; no Hadley geon reached |
| L54 | one-universe winding | **Batch 16 Set 1:** in a thin-shell handle on R³ (π₁ = ℤ), passages through a mouth give an integer winding w (signed: A +1, B −1, graze 0) of the closed loop with a reference sharing both endpoints; cut- and basepoint-free (#387); kick-writable (±1); constant while parked away from the mouths | batch-16 [A]; #381 | **live** | a true π₁ record (unlike batch 15's bands); exotic shell flagged |
| L55 | threading orbit | **Batch 16 Set 1:** the closed geodesic threading the handle is hyperbolic: trace 2(1+L/a) per passage, 4(1+L/a)²−2 over one full period of two passages (Lead ruling) (14, 62, 322 for L/a = 1, 3, 8); a 10⁻⁴ offset leaves after 5 passes | batch-16 [N] | **dead in the flat model; open with mouth mass** (#387) | mouths defocus like convex mirrors (derived, #387) |
| L56 | two mouths ⇒ CTCs | **Batch 16 Set 2:** a time offset between the mouths ≥ the outside light time gives CTCs (MTY 1988; Frolov–Novikov 1990, unchecked); the static symmetric host is CTC-free, non-generically with other masses nearby (Frolov–Novikov; V-text abstracts per #386) | batch-16 [M, A] | **noted** | ties the handle back to the geon CTC / chronology-horizon picture (exploration only) |
| L57 | flux record | **Batch 16 Set 3:** the electric flux through the handle (charge without charge) changes by ±q per signed passage of any charge and is dissipation-proof (d⋆F = J; radiation carries no net charge); readable by a Gauss surface enclosing exactly one mouth (#387); transcribes the carrier's winding (ΔΦ = qΔw) | batch-16 [A]; Misner–Wheeler 1957 (V-text per #386); non-co-orientable handles carry intrinsic charge (Sorkin 1977, Diemer–Hadley 1999) | **live** (exact-real) | survives radiation, unlike orbit classes |
| L58 | flux discreteness | **Batch 16 Set 3:** integer only as a difference from the reference, Φ − Φ_ref = n q₀, given one carrier species; Misner–Wheeler: "unquantized" (#386); no prior art; Dirac quantisation is quantum and excluded (5:00 PM) | batch-16 | **conditional** | an assumption about matter, near a law of R by fiat if chosen for the purpose |
| L59 | GW memory record | **Batch 16 Set 3:** permanent continuum record (Christodoulou 1991, V-meta per #380); mouth masses are not dissipation-proof (parked) | batch-16; #380 | **live** (continuum) | supplement only |
| L60 | ledger counts as "encoded in spacetime" | **David 9:28 PM ET 2026-10-12** (relayed by Physics Lead, Physics Lead chat, not signed; verbatim): "Yes, matter and flux next to fixed handles counts as encoded in spacetime for now." The analytic lock stays; the append-only matter-and-flux ledger next to fixed topological handles is the main line | David 9:28 PM; #388 | **ruling** | answers job 015's strongest reason to drop (#388) |
| L61 | persistence (definition) | **Batch 17 Set 1:** entry i persists from t_i to t′ iff a read-out map r_i (fixed in advance, same in all worlds) applied to the observer's later germ+record state (gauge classes, #324; reference and slot labels stored in the record) is correct on all of [t_i, t′] and witnessed to separate the alternatives written at t_i; append-only diary (#388), test-field limit | batch-17 | **live** | per entry; no weights; no tuning (no law of R by fiat) |
| L62 | ledger effectiveness | **Batch 17 Set 2:** preorder by inclusion of persistence sets (partial order on classes; same writes and exterior data) P(t′); grades G0 (never) to G3 (all permanent); no fractions or measures | batch-17; David 10:37 | **live** | graded without probability |
| L63 | existence: flux slot | **Batch 17 Set 3:** a charged passage changes the handle flux by ±q₀; read by a Gauss surface around one mouth with no charge between it and the throat; permanent (G2, over the observer's proper-time domain) with no later throat crossing (d⋆F = J; Misner–Wheeler V-text per #386) | batch-17; #385; #386; #387 | **live** (test-field limit) | "more than never" shown |
| L64 | losses as grades | **Batch 17 Set 4:** orbit decay and Claude 015 P1–P6 each downgrade affected slots (G2 → G1/G0) or are cost flags; none forces G0 everywhere | batch-17; #383; #388 (job 015) | **live** | persistence is graded, not all-or-nothing |
| L65 | where a world-dependent ledger can sit | **Batch 18 Set 1:** under the lock the germ fixes the simply connected analytic development; compatible worlds differ only by the deck group Γ and the extension (#370 (A)); the far side of a handle and connected regions outside the tube are fixed | batch-18 [A, sketch]; #370 | **live** | honest about what analyticity forbids |
| L66 | exact multiple ledger states | **Batch 18 Set 2:** flat lattice quotients R^{1,3}/Λ with ℓ_min > 2ρ give the same observer state, exact vacuum for the ledger (observer and flashes as test bodies; #394 F1), CTC-free; also moving lattices and the other compact flat quotients (F2); distinct Λ mod isotropy = distinct ledger states. Far-handle flux excluded (F cannot vanish on the tube under analyticity); flat Wilson-loop holonomy classically unreadable (excluded); Misner/Taub–NUT parked (read by survival only) | batch-18 [A] | **live (exact proof of concept only; main line stays geon/handle hosts, Lead ruling)** | answers Geometry's exactness objection (#388) |
| L67 | read-out as world revelation | **Batch 18 Set 3:** round trips through the topology return after time |g| with deck label g (Type O, no CTC needed); record classes nest; Γ certified in finite time for cocompact Λ (#370) | batch-18; #372 §2.6, R2; #370 | **live** | branch = record class (many worlds); one world per branch only after certification (cocompact Γ); nested |
| L68 | persistence of a pre-existing state | **Batch 18 Set 4:** Γ is constant (no topology change for reasonable sources in a CTC-free, time-orientable host; Tipler, Borde, Geroch per #380), so the ledger state is grade G3 (#390); the append-only diary (#388) only holds replies | batch-18; #380; #390; #394 F7 | **live** | G3 as re-readability by new flashes, not storage |
| L69 | batch 18 weak points | the strongest is that this is #370's Γ/extension freedom renamed; the lattice moduli are a continuum (uncountable; 6–9 real parameters, #394 F8) unless Γ ⊂ a fixed discrete group; the ledger is global, not nearby | batch-18 | **open** | |
| L70 | nearby-handle gluing as ledger state | **Batch 19 Set 1:** under the lock the handle's far side is fixed (L65); what can differ is the deck element closing the handle, an isometry of the fixed cover (twist R, time shift T, boost; a generic handle has only isolated choices, a continuum needs Killing symmetry; #398 F1/F7/F8); a static time shift gives CTCs at all times (F6); near region identical; read by Type O replies (rotation, delay); PT gluing gives Type F (unreadable); thin shells are outside the lock | batch-19 [A] | **live (conditional on an exact symmetric host)** | T above the light time gives CTCs (MTY), exploration only |
| L71 | Misner boost as ledger state | **Batch 19 Set 2:** Misner Taub region = Milne wedge {T < −|X|}/⟨B_β⟩ (the wedges X² > T² have CTCs); flat, so same germ for all β; β read by a round trip (Doppler e^{β} for both images; delay ∝ t_e, which also needs the boost centre) while the tube injects (βt > 2ρ, strictly before the Cauchy horizon T = −|X|; #397 M3/M4); co-moving readers are #375's incomplete family; exact | batch-19 [A, sketch] | **live** (exact, low-dimensional) | geon time-loop model |
| L72 | Γ beyond the forming geon's horizon | **Batch 19 Set 3:** replies beyond H⁺(S) depend on Γ (#367 (d)); the extension is read by survival only | batch-19; #364; #381; #398 F9 | **live** | Γ is present on S and readable before H⁺(S) if a round trip fits in D(S) |
| L73 | non-Hausdorff / inequivalent extensions | **Batch 19 Set 4:** exact but read by survival only; non-Hausdorff mechanism circular | batch-19; #379 | **parked** | |
| L74 | read-out, branching, persistence | **Batch 19:** branch = record class of gluings, refining with replies (fork = discovery, David 3:19/11:42); persistence G3 as re-readability within the read-out window (#398 F10) | batch-19; #390; #394; #398 | **live** | strongest weakness: exact examples are all symmetric, and then uncountable |
| L75 | which route without a record | **Batch 20 Set 1:** on a flat cylinder W_L, the route (deck class rel a declared reference) is fixed by (L, launch) in each world; it is a world fact, not a reception-history datum; asked of the record alone it is ill-posed unless constant on the record class | batch-20 [A, N]; #381; #399 | **live** | no fork within a world |
| L76 | record class of a hit | **Batch 20 Set 2:** with the launch known, a hit at x fits L_n = (X − x)/n (indexed by route; e.g. {5.0, 2.5}; finite for x > 0; continuum if x = X); arrival time carries no information | batch-20 [N]; Claude 017 | **live** | a hit narrows the worlds to one class; routes label worlds inside it, not branches; fixed-wrap two-slit case: two launches, n = 0 and n = −1 (11.32°, −2.85°), S1 |
| L77 | pattern from grouping | **Batch 20 Set 3:** x(L) piecewise linear with jumps at L = X/n (a periodic sawtooth only in X at fixed L), finite harmonic family Δ/n, periodicity in x; no density or fringes without a measure | batch-20 | **live (skeleton only)** | |
| L78 | two-slit obstacle | **Batch 20 Set 4:** one route per hit; under non-negative weights that ignore the routes not taken, the routes add, and no band is darker than a single route makes it; fringes need waves by hand (excluded), a self-field round the other routes (beyond the free test particle), or a weighting that depends on the whole set of routes, fixed in advance (parked; (M1) untouched; counting by route is the labelled conjecture; LT2); step-2 baseline stated in advance: a passive which-route record leaves hits unchanged and splits only the record class (S4) | batch-20 | **open** | strongest obstacle |
| L79 | David 1:17 AM | "This is all very encouraging. Let's proceed with the 2-slit work." (relayed by Physics Lead, Physics Lead chat, not signed; verbatim) | David 1:17 AM | **ruling** | starts the two-slit line |
| L80 | Lemma A (two-slit, weights) | **Batch 21 Set A:** if p^{both}(w) = λ p^{n_w}(w) (configuration-independent up to normalisation), then I_both = λ(I_0 + I_−1) and lies between the one-slit patterns pointwise: no dark spot | batch-21 [A] | **live (lemma)** | one launch, one route makes the sum split; min/max bound for normalised patterns (convex combination weighted by one-slit totals M_n) |
| L81 | configuration-dependent weights | **Batch 21 Set A:** dark spots need weights that depend on the open-aperture set and on the hit point (route-length difference); topology-only and route-counting weights are configuration-independent; no independent motivation found | batch-21 | **closed (LT2 fail if tuned)** | a phase-like profile is \|a\|² in disguise |
| L82 | self-field on the cylinder | **Batch 21 Set B:** for a uniformly moving test charge, image forces from ±m cancel exactly (Heaviside field; numeric ~1e-16); straight paths are self-consistent; hits are monotone in θ (density ~ launch weighting × D sec²θ): no bands | batch-21 [A, N] | **closed for eternal uniform motion** | wrapped radiation after launch/slit crossing (path memory, returns ~mL) open |
| L83 | droplet comparison | **Batch 21 Set B:** droplet patterns need a driven, persistent guiding wave with memory (Pucci et al. 2018; Andersen et al. 2015 non-replications; bibliographic); path memory: Fort et al. PNAS 2010, Eddi et al. JFM 2011 (bibliographic); for eternal uniform motion the image field gives no path memory; wrapped radiation memory after launch/slit crossing open | batch-21; #403; Claude 017 | **noted** | open |
| L84 | David 8:46 AM | "Explore both escapes side by side in step 2." (widget answer; relayed by Physics Lead, Physics Lead chat, not signed; verbatim) | David 8:46 AM | **ruling** | |
| L85 | echo model | **Batch 22:** charged test particle on a flat cylinder; retarded LW image fields (m≠0) at O(ε); Landau–Lifshitz reduced order for the local part (absorbed into the prescribed launch); first-order deflection at the screen; 3+1, space R²×S¹, motion in z=0; pre-launch image acceleration = 0 (Geometry fix); M-doubling 12/24/48 converges to ~5% | batch-22 [N] | **computed** | weak coupling ε ≪ 1; tail-term analogue (DeWitt–Brehme; Quinn–Wald; bibliographic) |
| L86 | echoes → bands? | **Batch 22:** Δx_hit ≈ linear in θ (weak converging lens, mean δ/ε ≈ 1.24 at L=2.5, v=0.5; ~50× smaller than first reported, bug fixed) plus a smooth trend; fine jitter is step-size noise (dt check); no periodic bands; caustic only at ε of order 1 | batch-22 [N] | **no bands (first order)** | τ not scanned; first order only |
| L87 | scaling | **Batch 22:** \|δ\| ∝ ~L^−1.3 (2.91, 1.24, 0.50 for L=1.25, 2.5, 5), weak v dependence (1.38 vs 1.24 for v=0.3, 0.5), linear in ε; no natural wavelength | batch-22 [N] | **noted** | |
| L88 | two-slit / records | **Batch 22:** neutral, kick-only apertures (modelling choice) leave per-world weights unchanged → Lemma A (L80); conducting walls need Lemma A re-proved (open): no point below both one-slit patterns; passive record changes nothing; active record adds smooth deflection; no bands to kill | batch-22 [A, N] | **noted** | conducting slits not computed |
| L89 | David 9:10 AM | "Let's have creative lead model the returning echoes." (relayed by Physics Lead, Physics Lead chat, not signed; verbatim) | David 9:10 AM | **ruling** | |
| L90 | Lemma A' | **Batch 23:** with one route per world, non-negative weights, and the two-route world set = union of the one-route sets, no dark spot (unnormalised: I_both ≥ each I_i). Exits: exclusion, contextual dynamics (conducting walls), multiplicity (several histories per launch), changed read-out map | batch-23 [A]; Geometry #407 | **live (lemma)** | exclusion is not the only door |
| L91 | Set 1: loop regularity | **Batch 23:** a condition around the two-route curve; on the flat cylinder there is no x-dependent holonomy, and the curve is the handle's own cycle, present with either slit open; Misner 8πN is a time period (Misner 1963); a period supplied by hand is tuning; no ħ-free aperture-cycle condition is known (Berry et al. 1980 needs a wave; Keller 1958 needs ħ) | batch-23; Geometry/Literature #407 | **dead pending a source, L0** | |
| L92 | Set 2: EKT multiplicity | **Batch 23:** EKT 1991 (verified, Crossref): infinitely many solutions for dangerous launches, none reported zero; lever = multiplicity (breaks (i)), reopens counting; needs offset-mouth host (#385 L56) and a self-interacting particle; Friedman et al. 1990 abstract only | batch-23; #407 | **proposed, rank 1, L1** | CTC exploration only |
| L93 | Set 3: screen as ledger | **Batch 23:** a hit = persistent readable entry (#399); readout ambiguity with both routes open might exclude hits | batch-23 | **proposed, rank 3, L1** | likely dead if persistence is local; dips at overlap, not periodic |
| L94 | Set 4: richer hit record | **Batch 23:** counting distinct full observer states is subadditive, max-type; no dips | batch-23 [A] | **dead for dips, L0** | record-dependent non-additivity noted |
| L95 | Set 5: count observer histories | **Batch 23:** 1/\|class\| weights are reweighting; without exclusion, no dips | batch-23 | **proposed, rank 5, L0–L1** | expected dead |
| L96 | Set 6 / Set 7 / Set R | **Batch 23:** Set 6 (loosened lock) reduces to Set 1, ill-posed as counting (dead pending a source). Set 7: conducting slit walls, contextual dynamics, rank 2, L0–L1. Rejected: "both routes"; negative weights (LT2; prior art Wigner 1932, Feynman 1987, not endorsed) | batch-23; #407 | **6 dead; 7 proposed; R rejected** | |
| L97 | David 9:36 AM | "Step back: have Creative Lead propose new idea sets for where interference could come from." (widget answer; relayed by Physics Lead, Physics Lead chat, not signed; verbatim) | David 9:36 AM | **ruling** | |

## Lesson L15 (after batches 01–02)

Every set so far fails the same way. Free-fall continuation is unique (`papers/geodesic-lifts.md` Prop 3.2; no monodromy along a single path, #331 §0, #332 R2). So the "branching" each set finds turns out to be **which host we are in** (the ensemble $E(O)$), not the motion. Rule for batch 03 onward: a set must name which hypothesis of Prop 3.2 it breaks and give an independent physical reason for breaking it. Otherwise it only feeds the ensemble.

## Summary after batches 01–03 (plain language)

Nine sets in, the lesson is the same every time. As long as the world is analytic and observers follow geodesics (Prop 3.2 / Cor 3.1 in `papers/geodesic-lifts.md`), a traveller's path never forks. Every apparent branching we found (seams, tubes, handles, patch edges, loops) turned out to be about which host world we are in, not about the motion. The only routes to a genuinely forking path break that starting point: a different motion law, a non-manifold world, or a law whose paths are not analytic curves (escaping via H5, which dodges Cor 3.1). Each of these reopens the lock "W is real-analytic; observers follow geodesics", so the high-level question for David is whether to reopen it, and if so, which part.

## Ruling (David Strayhorn, 2026-10-12 3:14 PM ET, relayed via Physics Lead, not signed)

> Yes, Creative Lead may propose ideas that relax the analytic/geodesic lock, as exploration only.

Recorded in `notes/creative/charter.md` (addendum). Batch 04 is the first batch run under it.

## Lesson L19 (batch 04)

No set survived the rules once the lock was relaxed (see `batch-04.md`). Two failure modes recur. (i) When ODE uniqueness breaks for a physical reason, the alternatives form a continuum (Peano-type non-uniqueness, free data on a null surface, extensions past a Cauchy horizon in $C^\infty$). (ii) Where the alternatives are discrete (sheets, eigen-frames, branch counts), the branch locus has codimension ≥2 and is rarely hit (#336, #341), or the alternatives disappear rather than fork. The analytic/geodesic lock was not the only barrier.

## Reframing (David Strayhorn, 2026-10-12 3:19 PM ET, relayed via Physics Lead, not signed; paraphrase, confirmed by Physics Lead as paraphrase only)

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

## David on (M1) and branches as geometries (2026-10-12 3:43 PM ET, relayed via Physics Lead, not signed; paraphrase, confirmed by Physics Lead as paraphrase only)

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

## Geon hosts: CTCs and non-time-orientability (David, 4:16 PM ET 2026-10-12, in Physics Lead's chat, relayed by Physics Lead, not signed, answering "Should worlds containing geon particles be allowed to have time loops, as Hadley requires?"; verbatim)

> Yes, allow CTCs and non-time-orientability in geon hosts, as exploration only.

This is the approval that relaxes #352 for geon hosts (exploration only). Also recorded in `charter.md`.

## Central hypothesis (David, 2026-10-12 4:17 PM ET, relayed by Physics Lead, Physics Lead chat, not signed; verbatim)

> Hmm, maybe that’s what it means to observe a particle? A signal goes from the observer to the particle’s CTC and comes back to the observer, communicating information about the particle’s state?

Central hypothesis of batch 11 (L36, L37). Measurement = round trip of the beacon signal through the geon's CTC region, back into the observer's time-oriented record. Also recorded in `charter.md`.

## Signal round trip is the main line (David, 4:28 PM ET 2026-10-12, relayed by Physics Lead, Physics Lead chat, not signed; verbatim)

> No, I like the original idea of the signal sent out by the observer. I can wrap my head around that.

> a fork in the observer's future (a branch in observer space) is exactly what we are looking for.

The signal round trip stays the main line; there is no observer-through-the-loop set. Also recorded in `charter.md`.

## Naming: backscattering (David, 4:37 PM ET 2026-10-12, relayed by Physics Lead, Physics Lead chat, not signed; verbatim, answering a proposal)

Physics Lead's proposal: "backscattering" as the plain-language name for the measurement round trip, "round trip" as the precise defined term.

David's answer:

> Yes, I'm happy with that.

Caveat: no in/out S-matrix is assumed; the model is classical. Where the geon forms after a Cauchy slice, the return lands beyond the observer's Cauchy horizon; eternal geons have no Cauchy surface.

## Classical model (David, 5:00 PM ET 2026-10-12, relayed by Physics Lead, Physics Lead chat, not signed; verbatim) — guiding constraint for future batches

> Keeping our measurement model classical is exactly the right thing. Our expectation (and hope) is that quantum statistics follows inevitability [read: inevitably; Lead editorial gloss] from a picture that is fundamentally classical at the deeper level. No need for us to inject it by hand, which is what Hawking did.

**Guiding constraint for future batches:** the measurement model stays classical; no quantum statistics is injected by hand.

## Signal and record (David, 7:45 PM ET 2026-10-12, relayed by Physics Lead, Physics Lead chat, not signed; verbatim)

> Should we delve into the details of what constitutes the signal and how it gets recorded? If the observer is going to record data, then it needs to be physical, which means encoded into spacetime itself. Perhaps some sort of ledger composed of particles of nontrivial topology that is distinct from the observer but travels in close proximity?

## Ledger encoded in spacetime (David, 9:28 PM ET 2026-10-12, relayed by Physics Lead, Physics Lead chat, not signed; verbatim)

> Yes, matter and flux next to fixed handles counts as encoded in spacetime for now.

The analytic lock stays; the append-only matter-and-flux ledger next to fixed topological handles is the main line.

## Persistence (David, 10:37 PM ET 2026-10-12, relayed by Physics Lead, Physics Lead chat, not signed; verbatim)

> On the topic of persistence, we might adopt the position that some pieces of matter are highly effective ledgers, other pieces of matter might be less effective, where more effective means that the matter keeps a record of many of its observations, and less effective means it keeps a record of fewer of them. So the fact that some observations don't persist should not be considered fatal to our endeavor. At this point, all we need is a clear model for what persistence means, how it happens, and that it can happen and is sufficiently well defined. Persistence doesn't need to happen all the time, everywhere; it merely needs to happen more than never.

## Ledger states that differ by world (David, 10:43 PM ET 2026-10-12, relayed by Physics Lead, Physics Lead chat, not signed; verbatim)

> Perhaps we need to consider whether it is possible for more than one ledger-state to be consistent with any given observer-state. I am imagining some topological detail inside the ledger, with World A containing Ledger state A, B containing B, etc.

Widget answer (same relay, verbatim):

> Yes, have Creative Lead build a batch on pre-existing topological ledger states that differ by world.

## Fork = discovery; flat example as proof of concept (David, 11:42 PM ET 2026-10-12, relayed by Physics Lead, Physics Lead chat, not signed; verbatim)

> Completely flat universes with the universe as the ledger is quite the different picture than the one we have been dealing with. Are we so eager to abandon our previous line of thought? Also, you say that it's a discovery, not a fork. What exactly is the difference? In my mind, a fork and a discovery are the same thing. If an observer travels down path B but not A of a fork, the observer discovers he is compatible with world B but not A.

Lead rulings: a fork is the discovery of which world one is in (per 3:19 PM); at finite time a branch is a record class of many worlds, refining with replies. The flat-quotient example (batch 18) is an exact proof of concept only; the main line stays geon/handle hosts.

## Two-slit work (David, 1:17 AM ET 2026-10-13, relayed by Physics Lead, Physics Lead chat, not signed; verbatim)

> This is all very encouraging. Let's proceed with the 2-slit work.

## Step back (David, 9:36 AM ET 2026-10-13, relayed by Physics Lead, Physics Lead chat, not signed (widget answer); verbatim)

> Step back: have Creative Lead propose new idea sets for where interference could come from.

## Returning echoes (David, 9:10 AM ET 2026-10-13, relayed by Physics Lead, Physics Lead chat, not signed; verbatim)

> Let's have creative lead model the returning echoes.

## Two-slit step 2 (David, 8:46 AM ET 2026-10-13, widget answer, relayed by Physics Lead, Physics Lead chat, not signed; verbatim)

> Explore both escapes side by side in step 2.

## Taub–NUT/Misner union (resolution, Literature via Physics Lead)

Resolved (reviews/misner-union-completeness-geometry-literature.md): in Misner, geodesics through the boost's fixed point are incomplete in both extensions and in every union (as a set of geodesics: closed, nowhere dense, Lebesgue-null in the covering chart's initial data (no measure on observer space adopted); every point of the Taub region still lies on one). The two-extension non-Hausdorff union is not complete: generic geodesics entering a CTC region hit its second horizon. Among unions of the four half-plane pieces, only the full quotient (R^2\{0})/B is complete modulo the fixed-point geodesics; helicoidal coverings give further non-Hausdorff maximal extensions with the same exception (Rieger, arXiv:2402.09312). Taub-NUT has no boost fixed point, but its comoving (zero-momentum) geodesics continue in neither extension (Misner–Taub 1969, §II C, relayed from external review, V-meta; confirmed by computation, #377), so no union of the two is complete. (PR #375; "measure zero" replaced by Lead ruling; Misner "only" and Taub–NUT clause edited per external review.) Reported Taub–NUT completeness: Hájíček 1971 (unchecked). Resolves the #367 vs #371 conflict (measurement-model-v0 open problem 13).

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
- 2026-10-12: batch 12 (L38–L40): survival, outcome vs branch, EKT countability.
- 2026-10-12: David's 4:16 PM geon-host approval recorded verbatim with its question (ledger, charter); #368 S1–S3 and #367 verdicts applied to batch 12.
- 2026-10-12: David's 4:28 PM words (ledger, charter); batch 13 (L41, L42).
- 2026-10-12: #371 S1–S6 and #370 verdicts applied to batch 13.
- 2026-10-12: David's 4:37 PM naming ruling (first recorded as a paraphrase; now verbatim); #367/#371 union conflict resolved (Literature via Physics Lead; Hájíček 1971).
- 2026-10-12: open problem 13 replaced verbatim per PR #375.
- 2026-10-12: 4:37 PM ruling now verbatim ("Yes, I'm happy with that.", answering Physics Lead's proposal); OP13 wording per Lead ruling ('Lebesgue-null in the covering chart').
- 2026-10-12: David's 5:00 PM classical-model ruling recorded verbatim (guiding constraint for future batches).
- 2026-10-12: L42 / batch 13 Taub–NUT completeness claim corrected per #375 and Claude job 013 R5 (matches #372 OP13).
- 2026-10-12: David's 7:45 PM question recorded verbatim (ledger, charter); batch 14 (L43–L47).
- 2026-10-12: Literature #380 applied to batch 14 (S1–S5; L46 conditional; L43, L44, L47 survive; 2A still parked).
- 2026-10-12: Geometry #381 applied to batch 14 (R1–R9; R3 merged into #380's text; holonomy parked for lack of a mechanism; write constraints).
- 2026-10-12: batch 15 (L48–L53): orbit classes around wormhole handles (numeric), L47 tube scale, ledger across the Cauchy horizon.
- 2026-10-12: Literature #383 applied to batch 15 (S1–S7; Simpson–Visser identification; radiation drives classes to T; L53 Misner premise fixed; prior art).
- 2026-10-12: Geometry #384 applied to batch 15 (boost threshold 0.268; Simpson–Visser NEC; energy bands, not winding; p∥ conserved; L52 OK).
- 2026-10-12: Lead ruling: SV described as a geometry chosen first, source identified afterwards (batch 15, L50).
- 2026-10-12: batch 16 (L54–L59): one-universe winding (integer, parked), threading orbit unstable (numeric), MTY CTC tie-back, flux-through-handle record (dissipation-proof).
- 2026-10-12: Geometry #387 and Literature #386 applied to batch 16 (signed winding; trace 2(1+L/a) per passage, 4(1+L/a)²−2 per period; one-mouth Gauss surface; weak point 7 rewritten; citation upgrades).
- 2026-10-12: David's 9:28 PM ruling recorded verbatim (L60).
- 2026-10-12: Lead ruling (Physics Lead): trace convention is 2(1+L/a) per passage, 4(1+L/a)²−2 over one full period of two passages; batch 16 and L55 aligned.
- 2026-10-12: David's 10:37 PM persistence words recorded verbatim (ledger, charter); batch 17 (L61–L64).
- 2026-10-12: Geometry #392 applied to batch 17 (F1–F7; F2 merged with Literature M2; interval persistence; gauge-invariant read-out; preorder; G-nesting).
- 2026-10-12: David's 10:43 PM words and widget answer recorded verbatim (ledger, charter); batch 18 (L65–L69).
- 2026-10-12: Geometry #394 applied to batch 18 (F1–F9).
- 2026-10-12: Literature #395 applied to batch 18 (M1–M3; ghost-image prior art).
- 2026-10-12: David's 11:42 PM words recorded verbatim; Lead rulings on #393 (fork = discovery; flat example as proof of concept).
- 2026-10-12: batch 19 (L70–L74): world-dependent gluing of a nearby handle; Misner boost; Γ beyond the horizon.
- 2026-10-12: Geometry #398 applied to batch 19 (F1, F3–F11; F2 withdrawn).
- 2026-10-13: 3:19 PM entry relabelled as paraphrase (confirmed by Physics Lead as paraphrase only; Physics Lead ruling).
- 2026-10-13: David's 1:17 AM words recorded verbatim (ledger, charter); batch 20 (L75–L79).
- 2026-10-13: Geometry #402 applied to batch 20 (F1–F7); Literature #403 applied (M1: the principle marked as paraphrase; prior art added).
- 2026-10-13: Claude job 017 applied to batch 20 (R1–R4, S1–S4, N1–N6; Lead ruling).
- 2026-10-13: David's 8:46 AM widget answer recorded verbatim (ledger, charter); batch 21 (L80–L84).
- 2026-10-13: Geometry M1–M4 and Literature M1 applied to batch 21; Literature M2 merged with Geometry (no 'memoryless'; Set B closed for eternal uniform motion only; wrapped radiation memory open); L80, L82, L83 updated.
- 2026-10-13: David's 9:10 AM words recorded verbatim (ledger, charter); batch 22 (L85–L89).
- 2026-10-13: batch 22 Geometry M1–M8 (pre-launch acceleration bug fixed, rerun, M-doubling) and Literature M1–M2 applied; L85–L88 updated (converging lens, ~L^−1.3, weak v, caustic at ε ~ 1).
- 2026-10-13: David's 9:36 AM words recorded verbatim (ledger, charter); batch 23 brainstorm (L90–L97).
- 2026-10-13: batch 23 Geometry M1–M9 and Literature M1–M4 applied (Geometry M7 and Literature M3 merged); Set 1/6 dead pending a source; Set 2 and new Set 7 (conducting walls) ranked up; L90–L92, L96 updated; __pycache__ removed.
