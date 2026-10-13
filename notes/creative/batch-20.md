# Batch 20: two-slit step 1: two routes, no record (Creative Lead; do not merge)

**Status.** Exploration only, under David's rulings (all relayed by Physics Lead, not signed). Classical only; test-body limit; no Born rule; no $|a|^2$ and no superposition of waves by hand; (M1) untouched at L3; CTCs as exploration only. Citations are unchecked unless verified earlier. Nothing goes into `versions/` or `papers/`. Stacked on #399 and uses its definitions: **world** (spacetime $\tilde M_{\rm ext}/\Gamma$ plus the observer's own test bodies, here including source and screen), **record** = reception history, **record class**, **handle round trip** (#399 §3, R2–R4). Ledger rows L75–L79. Script: `notes/creative/batch-20/cylinder.py` (output `results.txt`).

**David (1:17 AM ET 2026-10-13, relayed by Physics Lead, Physics Lead chat, not signed; verbatim):**
> This is all very encouraging. Let's proceed with the 2-slit work.

---

## For David (plain summary)

- **The toy.** A small classical particle goes from a source to a screen in a world that wraps around once, like a cylinder. It can reach a screen point "directly" or "by going round" the wrap one or more times. Those are the two (or more) routes. In one world with one launch only one of them is taken; reaching the same screen point by a different route needs a different launch angle. Nothing records which route it took.
- **"Which route?" without a record.** In any one world, the route is fixed: the launch and the wrap size settle it. So it isn't a fork, and it isn't undefined; it is a fact about the world. But a route number only means something relative to a declared reference route. Asked of the observer's records alone, "which route" is not a well-posed question (your ill-posed-question principle): the hit point fits more than one (world, route) pair.
- **What differs at the screen.** Across compatible worlds, which differ in how wide the wrap is, the same launch lands at different screen points. Conversely, one observed hit fits a short **list** of wrap sizes (finite, except at the straight-through point), one per route: the wrap could be 5.0 (one wind) or 2.5 (two winds) in our example. That list is the hit's record class. It is finite for a hit off the straight-through point; a hit exactly at the straight-through point fits every wide-enough wrap (a continuum). So a hit splits the worlds into separate groups, indexed by how many times the particle went round.
- **A pattern?** Yes, a structural one. Hit position against wrap size is piecewise linear with jumps (teeth crowding toward small wraps), and the compatible wrap sizes for a hit form a harmonic list (Δ, Δ/2, Δ/3, …), stopping before the wrap gets smaller than the hit's offset, so it is finite. The exception is a hit at the undeflected point, which fits every wide-enough wrap. But **no fringes**: in each world the particle makes one point hit. Turning "many worlds per hit" into brighter and darker bands would need a way to weight worlds, which we have deliberately not chosen.
- **The obstacle.** Classical particles give point hits. Fringes need either waves added together (excluded) or a weighting of worlds (parked). What we do get is the discrete skeleton a pattern would sit on.

---

## Set 1: is "which route" well-posed without a record?

**Plain summary.** The route is fixed in each world, but it is a world fact, not a record fact. It needs a declared reference to be a number at all.

- **Setting.** Cover: the flat plane $(x,y)$, with time suppressed (static). World $W_L$: $x\sim x+L$ (one handle direction, $\Gamma=L\mathbb Z$). Source at $(0,0)$, screen line $y=D$. A test particle is launched at angle θ, which is test matter in the world (#399 R2). There is no diary on either route.
- **Route = deck class rel reference.** A path from the source to a screen point has no absolute winding: an open segment is cut-dependent (#381, #387). The route number $n$ is defined only relative to a declared reference path, here "the straight segment inside the fundamental strip $[0,L)$". With that declared, the cover lift of the hit is $X=x+nL$ with $x\in[0,L)$ the arc length along the oriented screen from the foot point $(0,D)$, so $n=\lfloor D\tan\theta/L\rfloor\in\mathbb Z$ (negative for $\theta<0$) [A, N]. The cut sits at the source, so absolute $n$ shifts with the cut, and the reference is a rule-defined, different segment in each $W_L$. Only differences $n-n'$ between routes are cut- and basepoint-free (#381, #387).
- **Is it fixed by the world?** Yes, because the launch is part of the world (#399 R2). Given $(L,\theta)$, the geodesic is unique, so $n$ is unique: no fork within a world (#399 §3). For a fixed screen point instead, each $n$ has its own geodesic, launched at $\theta_n=\arctan((x+nL)/D)$, so $n$ labels a route; two-slit-style "two routes to one point" means two launches in one world, not one launch across worlds.
- **Is it the same as which world?** Not quite. For a fixed launch, $n$ is a function of the world $L$. For an observed hit $x$ without the launch recorded, many $(L,\theta,n)$ fit. "Which route" is a **coarse function of the world**, not a datum of the reception history.
- **Ill-posed-question principle.** Asked of the observer's record alone, "which route" is ill-posed unless $n$ is constant on the record class. In the example below it is not: one hit is compatible with $n=1$ and with $n=2$.
- **Status: live** (L75).

## Set 2: what differs at the screen; record classes of hits

**Plain summary.** One hit point is consistent with a discrete set of wrap sizes, one for each route.

- **Forward [N]** (θ = 35°, D = 10, so the cover hit is $X=7.0021$): screen point $x(L)=X \bmod L$, class $n(L)$. For example:
  - L = 2.5 gives x = 2.0021, n = 2;
  - L = 4 gives x = 3.0021, n = 1;
  - L = 7.5 gives x = 7.0021, n = 0.

  As a function of L this is piecewise linear, $x=X-nL$ with slope $-n$ on $(X/(n+1),X/n]$, jumping at $L=X/n$, with teeth crowding toward $L\to0$. It is a periodic sawtooth only in $X$ at fixed $L$.
- **Inverse: the record class of a hit [A, N].** With the launch known (so the cover hit $X=D\tan\theta$ is known), a hit at $x$ is compatible with $X-x=nL$. If $x\neq X$ (and $X>x$, the θ>0 convention): $L_n=(X-x)/n$, $n=1,2,\dots$, subject to $L_n>x$ (and $L_n>2\rho$ for the tube, #399), so $n<(X-x)/x$: a **finite** list for $x>0$, infinite (accumulating at 0, cut by the tube) only for $x=0$. If $x=X$: $n=0$ and every $L>\max(X,2\rho)$ fits, a **continuum**, so the record class is not always discrete. For the hit $x=2.0021$: $L\in\{5.0\ (n=1),\ 2.5\ (n=2)\}$. **A discrete record class, indexed by route.**
- **Timing carries no information.** The arrival time $D/(v\cos\theta)$ is the same in every $W_L$, so only position separates the worlds.
- **Branching.** A hit splits the prior class (all L) into a discrete family $\{L_n\}$. Further hits (other launches) refine it further, nested (#372 §2.6). Fork = discovery of Γ.
- **Status: live** (L76).

## Set 3: does anything pattern-like arise from grouping worlds?

**Plain summary.** There is a definite skeleton: hit position against wrap size is piecewise linear with jumps, and a finite harmonic list of compatible wrap sizes per hit. But there is no intensity.

- **Structure that exists without a measure:**
  - (i) the piecewise-linear, jumping $x(L)$ (a periodic sawtooth only in $X$ at fixed $L$);
  - (ii) the harmonic family $L_n=\Delta/n$ for a hit at offset Δ;
  - (iii) periodicity of hits in $x$ with period $L$ inside one world, across launches;
  - (iv) for a discrete Γ-family (Γ ⊂ a fixed lattice, #359), a finite set of hit points.
- **What does not exist:** a density of hits, fringes, or brighter and darker bands. Any of these needs counting or weighting worlds or launches, and that is parked: (M1) is untouched and there is no measure (#383 guardrails, #399).
- **Caustics.** A flat cover has no focusing, so none. A curved handle (batch 15/16) would give caustics, but those are geometric-optics features of a single world, not of grouping.
- **Status: live (skeleton only)** (L77).

## Set 4: the strongest obstacle

- **Point hits, no fringes (strongest).** A classical test particle makes one hit per world. Interference-like bands require either waves added by hand (excluded) or a weighting over the record class (parked; (M1) untouched). The model supplies the **discrete index set** (routes = deck classes) on which such a weighting would act, and nothing more. Counting worlds by route would be the labelled counting conjecture (#399), separate from (M1), which stays unchanged. A weighting chosen because it yields fringes is a T2 risk and must be fixed in advance. Even a weighting acts on a finite set of wrap sizes per hit, with no phase, so it gives weighted points, not bands.
- **Status: open** (L78).

---

## Weak points

1. **No intensity** (Set 4): the main gap.
2. **The source's launch is test matter in the world** (#399 R2). If it is unrecorded, the record class is even larger: $(L,\theta)$ pairs form a continuum.
3. **One handle direction, flat, static.** A Misner-style boost gluing (#396) would add a Doppler label per route, not computed here.
4. **The route needs a declared reference** (#381). Without it, "which route" is gauge.
5. **A discrete Γ-family needs an extra input** (fixed lattice), as in #398 F7.

Ledger: L75–L79 (L79 records David's 1:17 AM words).
