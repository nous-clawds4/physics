# Geometry review of Creative batch 15 (#382 @ 75e49a8) — do not merge

Reviewer: Geometry. Exploration-only content; no rulings adopted. Stacked context: #381 (winding only around a handle; record = deviation from declared reference), #375/#377 (Taub–NUT p∥=0 lost in both extensions and union).

## (1) Numerics — OK (reproduced byte-for-byte), two nits

Environment: Python 3.13.5, numpy/scipy as on box. Run from `notes/creative/batch-15/` on 75e49a8:

| file | sha256 |
|---|---|
| orbits.py | 5844de255f4f720eb714198149548ed15a64e02f071450b650fccd4e0f0809d6 |
| symmetric.py | e0d6fd4c0df86685395dda6a34538e8fe6771c5071cf2056d00d15f75bca644b |
| results.txt | d20dd6e3a5f5a6349996ab8795d6f210ef253bc39e1756d964cb4512c31ca11f |
| results-symmetric.txt | 2f5302602f4adcab643ec598ce0bf7cbc0ff0eb602c459df06116e524530aa01 |

Invocation `python3 orbits.py | diff - results.txt` and `python3 symmetric.py | diff - results-symmetric.txt`: both empty diffs.

Independent check: `reviews/creative-batch-15-geometry/check15.py` (sha256 641f458c496b0607300621c29ae1a50d56972fa7994a8ee4d6e42257ce6d855a), run `python3 check15.py` (sympy + mpmath, 30 digits), output `check15-output.txt` (sha256 e4001c042ea350b37830c1a5700ddb055e7677786fab3aefc25bb139cb9e7a7e). Effective potential re-derived: for \(-A dt^2+A^{-1}dx^2+R^2d\Omega^2\), \(E=A\dot t\), \(L=R^2\dot\phi\), the timelike shell gives \(\dot x^2=E^2-A(1+L^2/R^2)\) exactly (no approximation). Exact extrema, L=3.8: wells x=±9.7361801, V=0.91549999; barriers x=±3.0133699, V=0.95264816; throat V=0.86814815. Thresholds (fixed L, \(\dot x=dx/d\tau\)): 0.1927386 and 0.29068885. Matches.

Nits: (a) the duplicated entries at x=0 (and m=0.1, L=4) are grid artefacts (a grid point lands on the root); (b) for Ellis–Bronnikov m=0.1, L=6 and 8 the stable orbit lies beyond the ±200 search window, so "only unstable" there is an artefact, not physics. Neither affects a claim in the note.

**Fix (kick convention).** The script holds L fixed and adds \(\dot x\). A physical impulse that is radial in the orbiting body's own frame boosts its 4-velocity, which rescales both E and L by \(\gamma\). With that convention the thread threshold (proper speed in the orbit frame) is **0.26774487**, not 0.19274; the escape threshold is unchanged, **0.29068885** (since \(\gamma^2V_c=1\iff v^2=1-V_c\)). The order of the bands, and so the class structure, survives.

- OLD: `  - O+ → Th at $\dot x_0=0.19274$: at 0.9× the body stays O+ (0 crossings); at 1.1× it becomes Th (x ∈ [−42, 42]).`
- NEW: `  - O+ → Th at $\dot x_0=0.19274$ in the fixed-$L$ convention (impulse with $\Delta L=0$; $\dot x=dx/d\tau$); for a physical radial boost in the orbiting frame (E and L both scale by $\gamma$) the threshold is proper speed 0.26774 (Geometry check, #382 review). At 0.9× the body stays O+ (0 crossings); at 1.1× it becomes Th (x ∈ [−42, 42]).`

## (2) The symmetric metric — fix: it is a known geometry; NEC numbers

Line element intended (and used): \(ds^2=-A\,dt^2+A^{-1}dx^2+(x^2+k^2)d\Omega^2\), \(A=1-2m/\sqrt{x^2+k^2}\), \(x\in\mathbb R\). This is exactly the **Simpson–Visser** metric (arXiv:1812.07114, JCAP 02 (2019) 042; V-text of the abstract), which for \(k>2m\) is a two-way traversable wormhole. Checks: areal radius \(R=\sqrt{x^2+k^2}\ge k\), minimum (throat) at x=0, smooth in x; \(A\ge 1-2m/k=1/3>0\), so no horizon (k=3>2m=2); both ends asymptotically Schwarzschild with mass +m; reflection \(x\to-x\) is an isometry; static, so \(t\) is a global time function (time-orientable, no CTC).

NEC (sympy, \(G^\mu{}_\nu=8\pi T^\mu{}_\nu\)): \(8\pi(\rho+p_r)=-2k^2(R-2m)/R^5=-2k^2A/R^4\) (the printed factor reduces to this since the numerator is \(R(R-2m)^3\)). So NEC fails **everywhere**, not only near the throat; at the throat \(8\pi(\rho+p_r)=-2(k-2m)/k^3=-0.0741\); tail \(\sim -2k^2/x^4\), the same fall-off as pure Ellis (\(-2k^2/R^4\)): it is the Ellis profile multiplied by \(A\). Integrated, \(\int(\rho+p_r)\,4\pi R^2dx=-\pi k+4m\) (= −5.4248 at m=1, k=3) vs \(-\pi k\) for Ellis. The mass reduces the violation by about 42% here but it is still order k and not more localized than Ellis. Verdict on "how bad": exactly as bad as a standard Morris–Thorne wormhole of the same throat size, no worse.

- OLD: `- **Toy metric** (not a known exact solution; it needs exotic, NEC-violating matter, as static wormholes do, Morris–Thorne 1988 [M]):`
- NEW: `- **Toy metric** (the Simpson–Visser metric, arXiv:1812.07114, in its traversable-wormhole range $k>2m$; it is a chosen geometry, not a solution with a named source, and violates the NEC everywhere: $8\pi(\rho+p_r)=-2k^2A/R^4$, integrated $-\pi k+4m$, Geometry check on #382):`
- OLD: `1. **Toy metric.** Set 3's two-sided attraction is not a known exact solution. It needs exotic matter, and its stability as a spacetime is unchecked.`
- NEW: `1. **Toy metric.** Set 3 uses the Simpson–Visser wormhole ($k>2m$). It needs NEC-violating matter everywhere (same fall-off as Ellis, total about $-\pi k+4m$), and its stability as a spacetime is unchecked.`

## (3) Classes — OK as energy-band classes; fix the topology line

At fixed (E,L) the classes are the connected components of \(\{x: V(x)\le E^2\}\). L=3.8: \(V_0<E^2<V_c\): T only; \(V_c<E^2<V_b\): three components O−, T, O+; \(V_b<E^2<1\): one component Th; \(E^2\ge1\): Esc. So five labels, well-defined off the separatrix values \(E^2\in\{V_0,V_c,V_b,1\}\) (measure zero in (E,L), and no measure is adopted, consistent with weak point 5). Gauge: E and L are Killing charges with \(A\to1\) at **both** ends, so band boundaries are invariant; the only convention is the side label O+ vs O− (reflection isometry), which is removed by stating the record relative to the reference ("same side / other side"). So "class relative to unkicked reference" is gauge-free. OK.

But it is **not** a winding record in the #381 sense. The spatial slice is \(S^2\times\mathbb R\), which is simply connected: there is no non-trivial \(\pi_1\), and "threading" (crossing x=0) is not a homotopy invariant. The record here is **which-band / which-well**, a dynamical invariant of a static Hamiltonian, not a topological one. A #381-style winding needs both mouths in one asymptotic region (an intra-universe handle, \(\pi_1\supset\mathbb Z\)), which breaks the exact static spherical symmetry; and even then a T orbit oscillating through the throat has net winding alternating 0/±1, so only Th-type traversals in a fixed direction would carry a winding count.

- OLD: `- **Topological content.** Th and T orbits thread the handle, so their worldline classes are non-trivial in π₁ of the region. O± orbits circle the throat without threading, which is not topological in 3+1 (#381). The handle supplies the discreteness, and the kick supplies the change.`
- NEW: `- **Not topological.** The spatial slice is $S^2\times\mathbb R$, simply connected, so no orbit class here is a $\pi_1$ class. The record is the energy band (which well), a dynamical invariant of the static Hamiltonian, gauge-free relative to the reference. A winding record in the #381 sense needs both mouths in one universe (an intra-universe handle), which this static toy does not model. The handle supplies the wells, and the kick supplies the change.`

## (4) Taub–NUT p∥ condition — OK on the sign rule; fix the "rotating momentum" sketch

The sign rule matches #377 item 6: with \(p_\parallel=4l^2U(\dot\psi+\cos\theta\,\dot\phi)\) conserved, the divergent term cancels for exactly one sign, so the sign of \(p_\parallel\) (relative to the crossing direction) picks the extension; \(p_\parallel=0\) members continue in neither (#375). So "all members share a nonzero sign of \(p_\parallel\)" is the right condition, and it is open. But \(p_\parallel\) is a Killing charge: it is **constant** along each free (geodesic) member. A freely moving ledger body cannot rotate its \(p_\parallel\) into the other sign. Tear-off happens only if the ledger is held in orbit by a non-gravitational force or by a source that breaks the U(1) symmetry, which exact Taub–NUT does not have. For geodesic members the condition is fixed by initial data, not by orbital speed at the crossing.

- OLD: `- **An orbiting ledger** has momentum that rotates. If its orbital speed exceeds the observer's $p_\parallel$ component, some ledger bodies take the other sign and **tear off into the other extension** [A, sketch]. Joint survival favours slow, tightly bound ledgers, which pulls against Set 3's need for well-separated wells.`
- NEW: `- **An orbiting ledger.** For free (geodesic) members $p_\parallel$ is a conserved Killing charge, so each member's sign is fixed by its initial data and does not rotate with the orbit; the joint-crossing condition is "all members have nonzero $p_\parallel$ of one sign", and members with $p_\parallel=0$ are lost in both extensions (#375). Tear-off by orbital motion needs a binding force or source that breaks the U(1) symmetry, which exact Taub–NUT lacks [A, sketch].`
- OLD: `and **every** timelike curve of the Taub region is incomplete in each Hausdorff extension.`
- NEW: `and the timelike geodesics of the Taub region are incomplete in each Hausdorff extension (generic ones hit the second horizon; the fixed-point ones never cross, #375); accelerated curves are not checked.`

## (5) Hadley geon — not reached (honest no)

Nothing here reaches a Hadley geon. All three hosts are static, spherically symmetric, time-orientable (global time function t), CTC-free, with spatial topology \(S^2\times\mathbb R\), and Set 3 needs NEC-violating matter everywhere. A Hadley geon is a non-time-orientable topology meant to avoid exotic matter (topological censorship is evaded by non-time-orientability, not by NEC violation). Weak point 3 already says this; it should stay. OK.

## L52 (tube size) — OK

Tube scale set by the outer well radius (x≈9.74 at L=3.8; 21.30 at L=5, k=3) is dynamical, not chosen; not circular. Note that a Th write makes the tube contain the throat and both mouths, and Esc is ledger dropout, as the note says.

## Summary

(1) OK + kick-convention fix; (2) fix: Simpson–Visser, NEC everywhere, \(-\pi k+4m\); (3) OK as bands, fix: not topological; (4) sign rule OK, fix the rotating-momentum line and the Misner "every curve" line; (5) no Hadley geon; L52 OK.
