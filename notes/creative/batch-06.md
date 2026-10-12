# Creative batch 06: Sheets revived (Creative Lead; proposal, do not merge)

**Status.** Exploration only, under David's 3:14 PM ET ruling. Nothing goes into `versions/` or `papers/`. This replaces the hold on batch 05. Revives L3 (#331 Candidate A; #336). All outside citations are **unchecked**. In-repo pointers: `papers/geodesic-lifts.md` (Prop 3.2, Cor 3.1), H1–H5 in `batch-03.md`, #324 (gauge quotient), #336, batch-02 Set 1 (L11).

**David's words (2026-10-12, relayed via Physics Lead, not signed; verbatim):**
- 3:28 PM ET: "What’s wrong with special aim? If our desired style of branching can happen by special aim, then that’s still progress, right?"
- 3:30 PM ET: "Yes, revive sheets. Maybe you need special aim to hit the patches. On the other hand, maybe you need special aim to miss them! Is the glass half empty or half full?"

The two questions are recorded separately: **(A) existence** (can a seam-hitting path fork into a whole number of sheets at all?) and **(B) typicality** (is hitting special, or is missing special?).

---

## Verdicts (Geometry #349, Literature #350)

- **L24 (Part A): parked.** Its continuations carry identical germs (a nested prefix, #350 R1; #349). The count comes from a rule (#350 R2), and it would default to $1/e$ weights (#350 R3).
- **L25 (Part B): kept as a typicality template.**
  - B1 is **live as a template**: a point observer's hitting set is dense but meagre, the analogue of the Kerckhoff–Masur–Smillie picture for translation surfaces (KMS 1986; Masur 1986; per #350).
  - B2 is **parked**: it owes #336 (f)'s costs, and its tube collides with the jet/patch lock (#350, #339).
- **Everett risk (#350; #332 N1): high.** A fork into sheets inside one host is the branching-spacetime picture (Belnap 1992; McCabe 2005). B2's "which torn piece is the observer" is the self-locating-uncertainty problem of Everettian probability (Sebens & Carroll, *BJPS* 69 (2018) 25). That is the Carroll–Sebens framing the guardrails exclude: flagged as a hazard, not borrowed.

### Geometry corrections (#349)

- **The 4π apex.** The admissible continuation set is a $2\pi$ arc of directions. Its endpoints, the near-miss limits, match the lift rule, but by continuity, not because anything forces it.
- **Higher ramification.** At ramification index $k$ there are $k$ lifts against 2 near-miss limits. The total sheet count $n$ is irrelevant. The apex state is undefined.
- **The pullback.** The metric is a pullback, so the state sequences are identical (a nested prefix). A non-pullback metric would leave the lift rule undefined.
- **Extended observer (L25 B2).** With seam spacing $\ell$, a radius $\ge\ell/\sqrt2$ always hits; a radius between $\ell/2$ and $\ell/\sqrt2$ hits in strips; below $\ell/2$, missing is open.
- **Recasting as worlds.** This is not a mere relabelling, and it fails for three reasons. The slit hosts are extendible, which conflicts with #320. They are already in $E(O)$. They form a continuum.

## Part A: existence (L24) — parked

### In a minute
Picture a multi-storey spiral car park with no walls, where the levels meet along a central pole. Away from the pole every level is perfectly ordinary flat ground, and a car driving straight is completely predictable. A car aimed straight through the pole has a genuine choice when it comes out the other side: it can come out on any of the levels that meet there. The number of choices is a whole number fixed by how the levels are joined (two, three, …), not by us. We can build an explicit example where the choices really lead to different futures: on one level the car later meets a second pole, and on another it doesn't. So forking paths exist, given special aim. This fork happens inside one world, though. Matching it to David's "branch A = world A" is a separate step (below).

### Setup
- **Base.** $B=\mathbb R^2$ with an analytic Riemannian metric $h$ (flat is allowed). Points $0$ and $a\neq0$ in $B$.
- **Cover.** $S\to B$ is a connected 3-sheeted branched cover, branched over $\{0,a\}$, with monodromy a transposition $\sigma_0=(1\,2)$ around $0$ and $\sigma_a=(2\,3)$ around $a$. Monodromy around a large loop is $\sigma_0\sigma_a$, a 3-cycle, so the cover extends over infinity as well; we only need it over a bounded region. The monodromy group is $S_3$ acting on 3 sheets, so the cover is **not** regular (not Galois). That matters below. (Riemann existence theorem for branched covers with given monodromy, unchecked.)
- **Host.** $M=\mathbb R_t\times\mathbb R_z\times S$ with $g=-dt^2+dz^2+\pi^*h$. It is analytic off $\Sigma=\mathbb R_t\times\mathbb R_z\times\pi^{-1}\{0,a\}_{\text{ramified}}$.
- **Seam.** $\Sigma$ consists of timelike 2-surfaces, so it has **codimension 2**: cosmic-string-like worldsheets with cone angle $4\pi$ at each ramified point (ramification index $e=2$). Over $0$ the fiber is $\{x_{12}, x_3\}$: $x_{12}$ is ramified (sheets 1 and 2 meet there) and $x_3$ is an ordinary point of sheet 3. Over $a$ the fiber is $\{y_1, y_{23}\}$, with $y_{23}$ ramified.
- **Matter.** If $h$ is flat, $g$ is flat off $\Sigma$ and $\Sigma$ carries a concentrated (negative-deficit) source. That is the #332 R3 caveat: not a Geroch–Traschen distribution. The field equations on $\Sigma$ stay undefined, as in #331.

### The path and its fork
- Take a timelike geodesic whose $B$-projection is the base geodesic $\beta$ from a point $q$ through $0$ and on to $a$. With $h$ flat, this is a straight line through $0$ and $a$. The aim is special twice.
- Lift it on sheet 1 so that it reaches $x_{12}$ at proper time $\tau_0$.
- **What "through the seam" means.**
  - At $\tau_0$ there is no observer state: points of $\Sigma$ are not states ($p\notin\Sigma$, as in #331), so the curvelet has a gap at $\tau_0$.
  - The base geodesic $\beta$ is analytic straight through $0$, because $B$ is smooth there.
  - So a **continuation** is defined as a lift of $\beta|_{\tau>\tau_0}$ that starts at $x_{12}$. The lifts of the outgoing germ of $\beta$ at $0$ number exactly the ramification index $e=2$: one leaves on sheet 1 and one on sheet 2.
  - Sheet 3 is not reachable: its point over $0$ is $x_3\neq x_{12}$.
  - So, under the lift rule below, the options are **a whole number, $e=2$**, read off the cycle length of $\sigma_0$. The number is topology; that only these $e$ directions count is a rule (diffraction from a cone point populates a continuum of directions).
- **Why not more, or a continuum.** In the cone of angle $4\pi$ every outgoing direction that makes an angle $\ge\pi$ on both sides with the incoming one is locally length-minimising, and those directions form an interval: a continuum (standard for cone points of angle $>2\pi$, unchecked). The lift rule picks the $e$ directions in that interval whose projections continue $\beta$ analytically. **This is a rule, and it is the weak point of Part A.** It is the natural one, since it is analytic continuation in the base, which the host's own covering structure supplies (the local isometry to $B$ is canonical up to deck/sheet relabelling). But it is not forced by the geodesic equation on $M$. Limits of near-miss geodesics give only the two extreme directions (angle exactly $\pi$ on one side); for $e=2$ these are exactly the two lifts, so here the rule and the limit agree. For $e\ge3$ they disagree: the lifts sit at $\pi,3\pi,\dots,(2e-1)\pi$, and the $e-2$ middle lifts are not near-miss limits.
- **The futures really differ (why non-regular).**
  - If the cover were regular, a deck isometry would map one branch onto the other, and the oriented germs would be equal up to isometry. Under the #324 gauge quotient the two futures would be the *same* state sequence, and the fork would be invisible.
  - Here, the branch on sheet 2 reaches $y_{23}$ over $a$: it meets a second seam, which is a second fork or no continuation.
  - The branch on sheet 1 reaches $y_1$, an ordinary point, and continues analytically past $a$.
  - But the two state sequences do not differ as states. Every germ depends only on its base point and velocity, since the projection is a local isometry, and both continuations project to the same base geodesic $\beta$. So they carry identical germs at every $\tau$ off $\Sigma$, before and after $a$. The only difference is a gap (or, without a rule, an end) at the second seam, which is the nested-prefix pattern, not a split of patches (Paper 1's criterion; `papers/patch-edge.md`).

### Checks
- **Prop 3.2.** Holds on each sheet off $\Sigma$. It is not contradicted, because $\gamma_O$ in $P(O)$ ends at $\tau_0$ (the patch ends at $\Sigma$).
- **Cor 3.1.** The two continuations agree on $(\tau_0-\epsilon,\tau_0)$ and differ later. That is a shared trunk then divergence, which Cor 3.1 forbids *for analytic curves in Obs*. It is escaped because the curve is not defined at $\tau_0$.
- **Hypotheses broken.**
  - **H1:** the germ does not fix a patch through $\Sigma$, since there is no germ at $\Sigma$.
  - **H5:** the lift is not one analytic curve across $\tau_0$.
  - H2 is kept (free fall on each side), and so are H3 and H4 off $\Sigma$. The continuation rule at $\Sigma$ is an added clause of the motion law (see weak points).
- **One host or several?** **One host.** Both continuations live in the same $M$. This is a fork inside one world, which is not David's 3:19 ideal ("Within world A or world B, branching doesn't occur").
- **Restating it in David's terms.** Cut $M$ along a slit from $x_{12}$ and reglue so that the outgoing path is forced onto sheet $k$. This gives two hosts $M_1$, $M_2$. They agree on the observer's past (the slit can be placed outside it) and differ along the future path. So the fork becomes "branch $k$ = world $M_k$". But the regluing is a choice of host made after the fact, and the slit changes the topology. Whether that is a legitimate pair of compatible hosts or a relabelling of an in-host fork is **open for Geometry**.

---

## Part B: half full or half empty? (L25) — template; B1 live, B2 parked

### In a minute
Suppose the universe is full of these poles at a tiny but finite spacing, David's "microscopically violent topology". There are two honest answers, depending on what the observer is.
- **If the observer is a point:** hitting a pole still needs perfect aim, but only a tiny bit of aim. Every path passes very close to poles over and over, so every path can be nudged, by as little as you like, into one that forks. Forking paths are everywhere-close, while non-forking paths are still "most" of them in the topological sense. The glass is half empty, but the water is everywhere.
- **If the observer has a size about equal to the spacing**, the same size the tangle sets: then you can't avoid poles, and missing them all would take special aim, or would be impossible. The glass is half full. The cost is that a sized observer gets torn across levels, and we must say which piece "is" the observer. That must not be a weighting by hand.

### B1. Point observer: hitting is dense, missing is residual (no measure)
- **Seams.** $\Sigma=\bigcup_i\Sigma_i$ is a locally finite family of closed codim-2 seams with transverse spacing $\sim\ell$ (#336 (d), countable case; not dense, so the definition holds).
- **Recorded result (#336 (a), (d)).** The hitting set $H$ is a countable union of nowhere-dense sets, so it is meagre, and its complement is residual. Missing is generic at every finite $\ell$.
- **New claim (Creative Lead sketch, unchecked; for Geometry).** $H$ is also **dense** in the data whenever every timelike geodesic passes within $\sim\ell$ of seams on every stretch of proper time $\sim\ell$. Near any datum, a small change of initial direction, of size about $\ell/L$ after proper time $L$, aims at a nearby seam.
- **Topology answer.** Forking data are dense and meagre; non-forking data are residual. Hits need special aim, but arbitrarily little of it. "Arbitrarily little aim" is a topological statement, not a probability.
- **The density hypothesis is not automatic.** It needs seams spread throughout spacetime, for example a periodic arrangement in a cover of the charter's microscopic region. Which arrangement is a choice of host, not a measure.

### B2. Observer of extent $\sim\ell$: hitting is open dense
- **Replacement.** The observer is the tube of radius $r_0$ around $\gamma$, with $r_0$ tied to the same scale: $r_0\ge c\,\ell$ for the seam spacing $\ell$. "Hit" means the tube meets $\Sigma$. That is an open condition (#336 (f)), and with $r_0\gtrsim\ell$ every tube meets a seam within proper time $\sim\ell$. So $H$ is open, and its complement is empty or has empty interior: **missing needs special aim, or is impossible.**
- **How this differs from batch-02 Set 1 (L11, parked).**
  - There is no $r_0/\ell\to\infty$ limit and no "branching statistics" (#338's $(r_0/\ell)^2$ divergence is not used).
  - Nothing is averaged, so no weights are needed (the #339 hazard).
  - $r_0$ is not a new constant: it is pegged to the seam spacing, i.e. to the host's own scale.
- **Costs still owed (#336 (f)).**
  - C1: the factor $c$ is still a choice. Taking $r_0$ to be the observer's analytic patch radius would make it host-given, but that radius *equals* the distance to the nearest seam. Then the tube always touches a seam, and "hit" needs a sharper definition (unchecked).
  - C2: the state becomes a tube, not a germ at a point.
  - C3: the tube's own evolution is deterministic. Its geodesics pass on both sides of a seam and land on different sheets, so the tube is torn into $e$ pieces. The fork is "which piece is the observer". The count is topological ($e$, or the number of distinct sheets reached), but **picking a piece is a law of $R$ unless it is left as ensemble.**
- **L23 trap.** No weight is written, but by L23 and Paper 1 §6 a countable set of $e$ distinct continuations would default to counting ($1/e$ each); that default must be named, not denied. "Which piece" is left unweighted and unselected. Any rule that picks a piece, or weights pieces by size, is a law of $R$ and a measure by hand, and is excluded here.

---

## Weak points (for review)
1. **The A-rule.** "Continue by lifting the base geodesic" picks $e$ directions out of a continuum of locally length-minimising ones. It is natural but not forced by $M$'s geodesic equation. For $e=2$ it agrees with near-miss limits; for $e\ge3$ that is unchecked.
2. **The fork is in one host.** Recasting it as compatible hosts by cutting and regluing may be a relabelling, not a genuine pair of hosts.
3. **Seam matter.** The field equations on $\Sigma$ are undefined (#332 R3), and an excess angle needs a negative-tension-like source.
4. **B1's density claim** is a sketch and depends on a seam arrangement chosen as part of the host.
5. **B2** owes all three #336 (f) costs. Its fork is observer identity, which borders on a law of $R$.
6. **Framing.** Keep clear of Everett-style branching readings (#332 N1).

## Lesson L26

A fork that's real in the geometry but invisible in the states is the nested-prefix pattern again. For branches to differ in the states, the sheets must differ in their metric, and then nothing natural picks the continuation.

**Batch 07 is held** pending David's measure answer: whether a continuum of worlds with (M1) weights is acceptable, versus requiring countable branches. L26 makes that answer decisive.
