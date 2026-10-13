# Literature pass: creative batch 15 (L48–L53), PR #382

Reviewer: Literature agent. PR head recorded: `75e49a8` (base `creative/batch-14`). Files: `notes/creative/batch-15.md`, `batch-15/{orbits,symmetric}.py`, `results*.txt`, `ledger.md`. Do not merge. Marks: **V-text** = wording read (abstract or text); **V-meta** = bibliographic data verified, content from the standard account or a secondary summary.

## 1. Timelike orbits and ISCOs in Ellis / Ellis–Bronnikov

- **Huang, Kunz, Yang & Zhang**, "Light ring behind wormhole throat: geodesics, images and shadows", arXiv:2303.11885 (V-text, full text).
  - "The asymmetric wormhole has only one light ring and one innermost stable circular orbit located on one side of the wormhole throat."
  - The potential is "monotonically decreasing in Universe II, hence there are no bound orbits for massive particles."
  - For $m=0$: "there is no stable bound orbit and no ISCO in either Universe".
  - They also cite Yazadjiev, PRD 96 (2017) 044045, for uniqueness of the EB wormhole in Einstein–phantom-scalar theory (V-meta).
- **Set 1 (L48)** matches the massless statement exactly. Correct; the result is prior art and should be cited.
- **Set 2 (L49)** matches the asymmetric statement: one ISCO family, on the attracting side only, and no bound orbits on the repulsive side. Correct.
  - The batch's [M] metric form is consistent with this: $A\to1$ at $+\infty$ and $A\to e^{-2\pi m/k}(1+2m/|x|)$ at $-\infty$. I checked the potential $V=A(1+AL^2/(x^2+k^2))$ against the geodesic equation [A]; it is correct.
  - Huang et al. give a closed-form ISCO, $r_{isco}=-3m-\sqrt{4m^2+q^2}$ in their coordinates. The batch's numeric ISCO-like thresholds were not cross-checked against it (different coordinates). Note.
- **Chetouani & Clément**, "Geometrical optics in the Ellis geometry", Gen. Rel. Grav. 16 (1984) 111 (V-meta): null scattering only, with no timelike orbits.
- **Cramer, Forward, Morris, Visser, Benford & Landis**, "Natural wormholes as gravitational lenses", PRD 51 (1995) 3117 (V-meta): negative-mass mouths as lenses. Prior art for "the far side looks like negative mass" (Set 2).
- **Bronnikov's and Nandi's orbit papers:** I verified none, so I cite nothing from them.

## 2. Set 3's "toy" is a known metric (error)

- With $a=k$, the toy metric $-A\,dt^2+A^{-1}dx^2+(x^2+k^2)d\Omega^2$, $A=1-2m/\sqrt{x^2+k^2}$, is **exactly the Simpson–Visser metric**.
  - Source: Simpson & Visser, "Black-bounce to traversable wormhole", JCAP 02 (2019) 042, arXiv:1812.07114 (V-text abstract and line element).
  - For $a>2m$ it is "a (two-way) traversable wormhole" with a timelike throat at $x=0$ (V-text).
- **It is an exact GR solution with a known source.** Bronnikov & Walia, "Field sources for Simpson–Visser space-times", PRD 105 (2022) 044039, arXiv:2112.13198 (V-text abstract): "any static, spherically symmetric SV metric can be obtained as an exact solution to the Einstein field equations sourced by a combination of a minimally coupled phantom scalar field with a nonzero potential … and a magnetic field in the framework of nonlinear electrodynamics".
  - So "not a known exact solution" is wrong (S1–S3, S7).
  - The exotic-matter caveat stays: the scalar is phantom.
- **The batch's parameter choice $k=3m$ is the degenerate case.** Per Tsukamoto, "Gravitational lensing in the Simpson–Visser black-bounce spacetime in a strong deflection limit", PRD 103 (2021) 024033, arXiv:2011.03932 (V-meta; content via abstract summary):
  - for $a>3m$ the throat is a photon sphere;
  - for $2m\le a<3m$ it is an antiphoton sphere;
  - at $a=3m$ these merge into one marginally unstable photon sphere at the throat.

  So the run with $m=1$, $k=3$ is the marginal case. Note, no string.
- **Independent check [A].** With $r=\sqrt{x^2+k^2}$, $V=(1-2m/r)(1+L^2/r^2)$ is the Schwarzschild potential restricted to $r\ge k$.
  - For $L=3.8$, $m=1$: the Schwarzschild extrema are at $r=4.25$ (max) and $r=10.19$ (min). These give $x=\pm3.01$ and $x=\pm9.74$, matching the batch's [N] values.
  - $V(0)=0.868$ matches.
  - The throat minimum exists because $r=3m$ lies inside the Schwarzschild maximum.
- **Orbit classes are prior art.** Diemer & Smolarek, CQG 30 (2013) 175014, arXiv:1302.1705 (V-meta, via Dent et al.'s V-text summary), classify orbits in a Schwarzschild-type wormhole as:
  - bound (BO);
  - two-world bound (TWB);
  - two-world escape (TWE);
  - escape (EO).

  These are the batch's O±, Th, (pass-through) and Esc. Cite them.

## 3. Exotic matter and dynamical stability

- **Shinkai & Hayward**, "Fate of the first traversible wormhole: black-hole collapse or inflationary expansion", PRD 66 (2002) 044005, gr-qc/0205041 (V-text abstract).
  - The Ellis wormhole "is unstable against Gaussian pulses in either exotic or normal massless Klein-Gordon fields".
  - "For normal matter, such as a traveller traversing the wormhole, collapse to a black hole always results."
- **González, Guzmán & Sarbach**, CQG 26 (2009) 015010 and 015011 (V-text abstracts): all static, spherically symmetric wormholes with a massless ghost scalar are linearly unstable, with "precisely one unstable, exponentially in time growing mode". Nonlinearly, they collapse to Schwarzschild or expand.
- **Bronnikov, Fabris & Zhidenko**, EPJC 71 (2011) 1791, arXiv:1109.6576 (V-text abstract): they prove "the instability of all static solutions with both normal and phantom scalars and $V(\phi)=0$ under spherical perturbations".
- **Consequences:**
  - Sets 1 and 2 are known to be dynamically unstable spacetimes.
  - Shinkai–Hayward bear directly on Th/T writes: a normal-matter body threading the throat triggers collapse in the Ellis case.
  - For Simpson–Visser (phantom scalar with a potential plus NED), I verified no stability result. Weak point 1 should say this, not just "unchecked" (S3).

## 4. Radiation reaction, EMRIs and QNMs

- **Dent, Gabella, Holley-Bockelmann & Kephart**, "The sound of clearing the throat: gravitational waves from a black hole orbiting in a wormhole geometry", arXiv:2007.09135 (V-text, full text). The setup is a thin-shell Schwarzschild wormhole with its throat at $3M$, studied with 2.5PN radiation reaction.
  - "a bound BH will move through the WH many times in a damped oscillation … This results in the BH orbit decaying and settling on the throat of the WH."
  - That is: with radiation, **O± → Th → T, ending at rest on the throat**. The class record is erased toward T on the radiation-reaction timescale.
  - Weak point 2 is right, and this is the published confirmation. Note, plus a citation in S4.
- **QNMs and echoes.** Cardoso, Franzin & Pani, PRL 116 (2016) 171101 (V-meta, as cited by Dent et al.) is the standard reference for wormhole ringdown. It doesn't bear on the record directly.

## 5. Misner claim in the horizon section (error)

- The batch says that **every** timelike curve of the Taub region is incomplete in **each** Hausdorff extension. That contradicts #371 (9f4a5d3) and #377, which follow Rieger 2402.09312 Prop 6.4 (V-text, per #371).
- In Misner space, a geodesic that crosses into its extension continues there; the geodesics of the other winding sign are incomplete in that extension.
- Only the fixed-point geodesics are incomplete in every extension (and in every union).
- So "both cross, then both end" is wrong for generic tubes: a jointly crossing tube survives in its extension (S5, S6).
- The Taub–NUT $p_\parallel$ rule as stated is consistent with #377. Note: geodesics with $p_\parallel=0$ continue in neither extension.

## 6. Strings

Each OLD occurs exactly once at 75e49a8: S1–S5 in `notes/creative/batch-15.md`, S6–S7 in `notes/creative/ledger.md`.

S1.
- OLD: `(a toy we built, not a known exact solution)`
- NEW: `(the Simpson–Visser wormhole, a known exact solution, but one that needs exotic matter)`

S2.
- OLD: `(not a known exact solution; it needs exotic, NEC-violating matter, as static wormholes do, Morris–Thorne 1988 [M])`
- NEW: `(this is the Simpson–Visser metric with $a=k$, Simpson & Visser, JCAP 02 (2019) 042, a two-way traversable wormhole for $a>2m$; it is an exact Einstein solution sourced by a phantom scalar with a potential plus a nonlinear-electrodynamics magnetic monopole, Bronnikov & Walia, PRD 105 (2022) 044039; so it needs exotic, NEC-violating matter; $k=3m$ is the case where the throat is a marginally unstable photon sphere, Tsukamoto, PRD 103 (2021) 024033)`

S3.
- OLD: `Set 3's two-sided attraction is not a known exact solution. It needs exotic matter, and its stability as a spacetime is unchecked.`
- NEW: `Set 3's metric is Simpson–Visser (exact, with a phantom-scalar plus nonlinear-electrodynamics source), so it needs exotic matter. Its stability as a spacetime is unchecked; the related Ellis and ghost-scalar wormholes are unstable (Shinkai–Hayward 2002; González–Guzmán–Sarbach 2009; Bronnikov–Fabris–Zhidenko 2011), and a normal-matter body passing the Ellis throat triggers collapse to a black hole (Shinkai–Hayward).`

S4.
- OLD: `Radiation would make bound orbits decay, so the classes are stable only in the test limit.`
- NEW: `Radiation makes bound orbits decay: in a Schwarzschild-type wormhole a bound body passes the throat repeatedly in a damped oscillation and settles on the throat (Dent, Gabella, Holley-Bockelmann & Kephart, arXiv:2007.09135), so every class drifts to T and the classes are stable only in the test limit.`

S5.
- OLD: `and **every** timelike curve of the Taub region is incomplete in each Hausdorff extension. So the joint survival of observer and ledger is at most "both cross, then both end".`
- NEW: `and a geodesic is incomplete in the extension it does not cross into, while only the fixed-point geodesics are incomplete in every extension (#371, #377; Rieger 2402.09312 Prop 6.4). So a tube whose members all cross into the same extension can survive jointly there.`

S6.
- OLD: `; Misner: all end anyway`
- NEW: `; Misner: same-extension crossing survives, fixed-point geodesics end`

S7.
- OLD: `discreteness from the handle; not an exact solution`
- NEW: `discreteness from the handle; Simpson–Visser metric (exact, phantom + NED source); radiation drives all classes to T`

## Guardrails
- No forbidden Greek letter in this file.
- No Born/$|a|^2$/$1/N$ result; the batch is classical with no measure, and weak point 5 explicitly avoids "rarely".
- No Everett framing.
- No pick among M1/M2/T-options or on CTCs. The toys are CTC-free, and the CTC choice stays David's.
- Paper 1 untouched.
- The rulings are labelled relayed by Physics Lead, not signed.
- No geon ruling is claimed. The batch correctly says the toys are not Hadley geons.

## Verdicts
- **L48 (pure Ellis: dead):** correct; prior art Huang et al. 2023.
- **L49 (Ellis–Bronnikov: one class):** correct; prior art Huang et al. 2023 and Cramer et al. 1995 (negative-mass side).
- **L50 (symmetric toy):** the numerics check out [A], but "not an exact solution" is wrong (S1–S3, S7).
  - The classes are prior art (Diemer–Smolarek 2013).
  - With radiation, all classes decay to T (Dent et al.; S4).
- **L51 (kick write):** survives in the test limit. The adjacency claim is consistent with conservation of E and L.
- **L52 (tube scale):** survives as stated. The scale also inherits the radiation-decay timescale.
- **L53 (Cauchy horizon):** the Misner premise is wrong (S5, S6). The Taub–NUT sign rule is consistent with #377.
