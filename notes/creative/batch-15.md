# Batch 15: do stable bound orbit classes exist around a geon handle? (Creative Lead; do not merge)

**Status.** Exploration only, under the 3:14, 3:53, 4:16 and 7:45 PM rulings and the 5:00 PM classical constraint (all relayed by Physics Lead, not signed). It is classical, uses no probability and no measure, and treats CTCs as exploration only. **Citations are unchecked** unless marked. Nothing goes into `versions/` or `papers/`. Stacked on batch 14 (#379). Ledger rows L48–L53.
**Marks.** **[N]** = numeric, from this batch's scripts (`notes/creative/batch-15/orbits.py`, `symmetric.py`; outputs `results.txt`, `results-symmetric.txt`). **[A]** = short analytic check in this note. **[M]** = from memory, unchecked.

---

## For David (one minute)

We asked whether a small body can sit in one of several stable "parking orbits" around a wormhole-like handle, so that a kick could move it from one parking spot to another and that move would be the diary entry.

- **The plain Ellis wormhole: no.** It has no gravity pulling things in, so nothing can orbit it. Everything flies away.
- **Ellis with mass: only one parking spot.** It pulls on one side and pushes on the other. There is one family of stable orbits, on the pulling side. A strong enough kick throws the body through the throat and away for good. That is losing the diary, not writing it.
- **A wormhole that pulls on both sides** (a toy we built, not a known exact solution): **yes.** There are separate stable parking spots: outside on either side, trapped in the throat itself, and a "commuting" orbit that keeps passing through the throat. A kick has a sharp threshold, computed numerically. Below it the body stays put; above it it switches to commuting. Small nudges don't change the spot. This is the discrete, stable diary entry we were after, but only in this toy.

**The catches.** The toy needs exotic matter. These are test bodies, with no radiation. They are not Hadley geons: no time loops, no flips. One kick can only reach a neighbouring spot. The diary also sets the observer's size, which is acceptable but not free. And when observer and diary cross the time-loop horizon, they can be torn apart unless they move almost together.

---

## Set 1: pure Ellis drainhole (massless) — no bound orbits

**Plain summary.** No pull, so no orbits. Every body that comes near either passes through or leaves. Nothing can be stored.

- Metric $ds^2=-dt^2+dx^2+(x^2+k^2)d\Omega^2$ (the Morris–Thorne form with zero redshift; in Schwarzschild-like radius $r^2=x^2+k^2$, $b(r)=k^2/r$) [M for the identification].
- Timelike equatorial geodesics: $\dot x^2=E^2-V$, with $V=1+L^2/(x^2+k^2)$ [A].
- $V$ has a single extremum, a **maximum** at the throat $x=0$ (an unstable circular orbit), and $V\ge1$ everywhere. A bound orbit needs $E^2<V(\pm\infty)=1$, which is impossible. So **there are no bound timelike orbits and no stable circular orbits** [A; N: extrema at $x=0$ unstable for L = 0.5, 1, 2, 4].
- **Status: dead** for the ledger (L48).

## Set 2: Ellis–Bronnikov drainhole (with mass) — one stable class, plus loss

**Plain summary.** It attracts on one side and repels on the other. Stable orbits exist only on the attracting side. A kick past a threshold sends the body through the throat and off to infinity on the far side. That is losing the record, not changing it.

- Metric $-A\,dt^2+A^{-1}[dx^2+(x^2+k^2)d\Omega^2]$, with $A=e^{-(2m/k)(\pi/2-\arctan(x/k))}$. Mass $m>0$ is seen at $x\to+\infty$, and $A(-\infty)=e^{-2\pi m/k}<1$, so the far side looks like negative mass [M for the form].
- $V=A(1+AL^2/(x^2+k^2))$. **[N]** For $m/k=0.1$ and $0.3$: an unstable maximum near the throat ($x\approx0.2$–$0.8$) and one stable circular orbit on the $+$ side for $L\gtrsim0.6$ (m=0.1) and $L\gtrsim1.2$ (m=0.3), ISCO-like. **No minimum for $x<0$**: $V$ falls monotonically to $A(-\infty)$.
- **Kick [N]** ($m/k=0.3$, $L=6$): the circular orbit is at $x=118.78$, with $V=0.99749$; the throat barrier is $V=8.2288$. The radial-kick threshold is $\dot x_0=\sqrt{V_b-V_c}=2.6891$:
  - below it, the body reflects (and here escapes to $+\infty$, since the kick also unbinds it);
  - above it, it crosses and runs to $x\to-\infty$.
  - Small perturbations ($\dot x=10^{-3}$, $10^{-2}$) stay bound near the orbit (a basin).
- **One class only.** Crossing is **dropout of the ledger body**, not a second class (cf. v0.10.1 §6.2: dropout is not an arm).
- **Status: parked** (L49).

## Set 3: symmetric two-mouth toy — several discrete stable classes

**Plain summary.** If the handle pulls from both sides, there are separate stable parking places. Kicks have sharp thresholds, and small nudges don't change the class. This is the discrete, stable record batch 14 needed, in a toy.

- **Toy metric** (not a known exact solution; it needs exotic, NEC-violating matter, as static wormholes do, Morris–Thorne 1988 [M]): $-A\,dt^2+A^{-1}dx^2+(x^2+k^2)d\Omega^2$, with $A=1-2m/\sqrt{x^2+k^2}$, $k>2m$. Run with $m=1$, $k=3$, so $A(0)=1/3$.
- **Wells [N].**
  - For $L\le3$: one minimum, at the throat.
  - For $L=3.8$: three wells ($x=0$, with $V=0.8681$; $x=\pm9.736$, with $V=0.9155$) and two barriers ($x=\pm3.013$, $V=0.9526<1$).
  - For $L=5$: wells at $x=0$ ($V=1.2593$) and $\pm21.30$ ($V=0.9560$), barriers at $V=1.3032>1$.
- **Classes at fixed $L$**, separated by separatrices in $E^2$:
  - **O±** (outer, on either side; never crosses the throat);
  - **T** (trapped at the throat; oscillates through it, threading the handle: 242 crossings over the run [N] at L=5);
  - **Th** (bound and threading between both outer regions, $V_b<E^2<1$; exists when $V_b<1$, e.g. L=3.8);
  - **Esc** (unbound).
- **Kick thresholds [N]** (L=3.8, radial kick from the outer circular orbit):
  - O+ → Th at $\dot x_0=0.19274$: at 0.9× the body stays O+ (0 crossings); at 1.1× it becomes Th (x ∈ [−42, 42]).
  - Th → Esc at $0.29069$: at 1.1× the body crosses once and escapes.
- **Basins [N].** A Th orbit perturbed by ±10⁻³ keeps its class. The reference (a tiny kick) stays O+ with 0 crossings.
- **Reachability [A].** After an impulse, $E$ and $L$ are conserved. So one kick at the O+ orbit can only reach the energy bands open *at that position*: O+, Th or Esc. Reaching O− or T needs a second kick inside that well, or dissipation. At L=5 (barrier > 1) the outer and throat wells are disconnected for all bound energies; inward kicks of 0.9× and 1.1× the escape threshold stay outside [N].
- **The record** (batch 14 §3, #381), stated as a difference from a declared reference history at matched return events:
  - Reference: the unkicked O+ circular orbit (0 throat crossings).
  - Datum: the class (O+, Th, T, O−) at the matched return. In Th the raw crossing count advances every half-oscillation (5 in the 1.1× run, 3 in the mid run [N]), so it is **not** the record; the class is.
- **Topological content.** Th and T orbits thread the handle, so their worldline classes are non-trivial in π₁ of the region. O± orbits circle the throat without threading, which is not topological in 3+1 (#381). The handle supplies the discreteness, and the kick supplies the change.
- **Status: live (toy)** (L50, L51).

---

## L47: the ledger in the observer state and #336's tube cost

**Plain summary.** Including the diary makes the observer a small region rather than a point. Its size is set by the diary's orbit, which the physics fixes; we don't choose it. That is acceptable, but it isn't free, and if the diary is lost the region has no defined size.

- The tube scale is set by the outer well's radius (e.g. $x\approx9.7k$ at L=3.8; $21k$ at L=5 [N]), i.e. by $m$, $k$ and the ledger's $L$. It is **dynamical, not chosen**, which answers #336's "undefined scale" objection in this toy.
- **Circularity?** Defining the tube as "the smallest region containing the observer and the ledger's bound orbits" is a geometric definition. It does not presuppose the record's *value*, only that the ledger is bound. **Not circular.** But a Th or Esc write changes the tube's extent (Th spans both sides), so the state's support depends on the record. That is acceptable for a germ+record state (L29), since the record is part of the state, but the tube has no fixed size.
- Esc is ledger **dropout**: the state loses its record carrier. A convention is needed, as with observer dropout (#372 §2.6).
- **Status: open, acceptable in the toy** (L52).

## The ledger tube crossing the observer's Cauchy horizon

**Plain summary.** Passing the time-loop horizon, each body goes into whichever continuation its own motion picks. Observer and diary stay together only if they move almost in step. An orbiting diary body changes direction, so it can be torn away.

- **Misner** (#367/#375): which extension a timelike curve crosses into is fixed by its own data (winding sign), and **every** timelike curve of the Taub region is incomplete in each Hausdorff extension. So the joint survival of observer and ledger is at most "both cross, then both end".
- **Taub–NUT** (Misner–Taub 1969, V-meta; sign rule confirmed by computation, #377 item 6): the crossing extension is fixed by the sign of $p_\parallel$. A tube crosses jointly into one extension iff all its members have the same sign of $p_\parallel$ at the crossing. That is an open condition: it holds for a small tube whose velocity spread is below the observer's $|p_\parallel|$, off the zero-momentum set [A, sketch].
- **An orbiting ledger** has momentum that rotates. If its orbital speed exceeds the observer's $p_\parallel$ component, some ledger bodies take the other sign and **tear off into the other extension** [A, sketch]. Joint survival favours slow, tightly bound ledgers, which pulls against Set 3's need for well-separated wells.
- This toy is static, with no CTC and no Cauchy horizon. The horizon analysis applies only to forming-geon hosts (#364 (d), #372 §2.4), and the toy does not model one.
- **Status: open (sketch)** (L53).

---

## Weak points

1. **Toy metric.** Set 3's two-sided attraction is not a known exact solution. It needs exotic matter, and its stability as a spacetime is unchecked.
2. **Test bodies only.** There is no back-reaction and no gravitational radiation. Radiation would make bound orbits decay, so the classes are stable only in the test limit.
3. **Not a Hadley geon.** The toys are time-orientable, static, CTC-free handles. How a non-time-orientable, CTC-bearing geon behaves is untouched.
4. **One kick reaches only adjacent bands** (Set 3). A rich alphabet needs several kicks or dissipation, and the latter is a mechanism we don't have.
5. **Near separatrices** the class is sensitive to the kick. The unstable circular orbits form a separatrix of zero thickness; no measure is adopted, so we make no "rarely" claim.
6. **Equatorial, fixed-L analysis.** A kick generally changes $L$ too, and the class boundaries move with $L$. Only radial kicks are computed.
7. **Horizon crossing** is a sketch, and the toy has no horizon.
8. **Numerics.** Finite integration time (affine parameter 4000) and numerical derivatives. Crossing counts are over the run, not asymptotic.
