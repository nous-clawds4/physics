# Literature prior-art and taste pass: Creative batch 05 (#345)

**Reviewer:** Literature. **Date:** 2026-10-12. **Record type:** review record; applies nothing; do not merge.

**Heads.** #345 head `797c960`, based on `creative/batch-04`; files `notes/creative/batch-05.md` and the ledger. main `e41412b`. No earlier review of #345 exists.

**Context.**
- David's 3:14 PM ET ruling permits exploratory relaxation of the lock.
- His 3:19 PM ET reframing is recorded in the ledger, verbatim, relayed, not signed.

**Marks.**
- **V-text:** text or abstract checked this session.
- **V-meta:** bibliographic data and topic only.

## Verdict: HOLD (narrow)

Three fixes:
- **R1:** a "verified" citation was only checked bibliographically.
- **R2:** Paper 1 §6 is misread, and the misreading hides the main measure hazard.
- **R3:** a $C^{1,1}$ host cannot carry impulsive waves.

## Creative Lead's questions

1. **Countable or finitely describable classes of spacetimes.** Yes, in neighbouring forms; none as a rule for observer motion.
   - **Computable analysis.** Pour-El & Richards, "The wave equation with computable initial data such that its unique solution is not computable", *Adv. Math.* 39 (1981) 215–239 (V-text, title and bibliographic data), and the book *Computability in Analysis and Physics* (Springer 1989) (V-meta).
   - **Warning from Pour-El–Richards for L20.** A "finitely definable" class need not be closed under evolution. The counterexample uses low-regularity data. For analytic computable data, Cauchy–Kovalevskaya keeps solutions computable (V-meta). So the class must be shown closed within each piece and across junctions.
   - **Countably many hyperbolic 3-manifolds and Mostow rigidity** (E4): Mostow, *Publ. Math. IHÉS* 34 (1968) 53–104 (V-meta). Correct as cited.
2. **Piecewise-analytic solutions glued across null hypersurfaces.** Yes, well developed.
   - Penrose, "The geometry of impulsive gravitational waves", in *General Relativity: Papers in Honour of J. L. Synge* (OUP 1972) 101–115: cut-and-paste (V-meta).
   - Khan & Penrose, *Nature* 229 (1971) 185: colliding impulsive plane waves (V-meta).
   - Dray & 't Hooft, *Nucl. Phys. B* 253 (1985) 173 (V-meta).
   - Clarke & Dray, "Junction conditions for null hypersurfaces", *CQG* 4 (1987) 265–275 (V-meta).
   - Barrabès & Israel, "Thin shells in general relativity and cosmology: the lightlike limit", *PRD* 43 (1991) 1129–1142 (V-text, abstract).
   - Characteristic initial-value problem: Rendall, *Proc. R. Soc. A* 427 (1990) 221 (V-meta).

   Two corrections follow:
   - (i) Free data does sit on null hypersurfaces, as the batch says.
   - (ii) **Regularity (R3).** Impulsive waves and null shells have a metric that is only $C^0$, with a delta in curvature. A $C^{1,1}$ junction allows only a curvature *jump* (step or shock waves). Null shells are generally matter shells, not vacuum.
3. **Physical motivation for "finite description".** Weak.
   - The nearest physics is finite-information bounds: Bekenstein, *PRD* 23 (1981) 287; Lloyd, *PRL* 88 (2002) 237901 (both V-meta).
   - These bound information in a region. They do not make exact geometry finitely definable. TT2 stays the main risk, as the batch says.
4. **Matches with existing work.** In spirit, yes:
   - Digital physics: Zuse, *Rechnender Raum* (1969); Fredkin, *Physica D* 45 (1990) 254 (V-meta).
   - Tegmark's Computable Universe Hypothesis: *Found. Phys.* 38 (2008) 101 (V-meta).
   - Schmidhuber: *LNCS* 1337 (1997) 201; *IJFCS* 13 (2002) 587 (V-meta).
   - Algorithmic probability: Solomonoff, *Inf. Control* 7 (1964) 1–22, 224–254; Kolmogorov, *Probl. Inf. Transm.* 1 (1965) 1–7 (V-meta).

   No one I found uses a countable host class to make observer branching countable.

## Measure check (the key point)

- **"Countable" is not measure-neutral in this framework.** Paper 1 §6 says: "If distinct evolutions are countable, counting is the unique reasonable measure on observer space." On a countably infinite set it uses counting measure "to form ratios along finite initial segments". L20 makes that antecedent true *by choice of class*. Ratios along initial segments then need an enumeration, and "finite description" supplies one: description length.
- **That is the algorithmic-prior route.** A universal (Solomonoff / $2^{-K}$) prior, or any length-ordered enumeration, is weights by fiat. It falls under (M1) and the Born guardrails (LT2: inputs "not tuned until |psi|^2 appears").
- The batch's "Measure: none" cites Paper 1 §6 for the opposite point (R2). The math sentence (no uniform countably additive probability on a countable set) is true. But it is not what §6 says, and it hides this hazard.

## Per-set verdicts

| Item | (a) Known? | (b) Killed in the record? | (c) Sneaks the answer in? |
|---|---|---|---|
| **L20** finite-description hosts | Partly: null gluing and computable physics are known (above). The combination is new. | **Not killed.** Under the 3:14 PM ruling the relaxation is permitted for exploration. The reframing matches Paper 1's split criterion ("the first $\tau$ at which those patches disagree"). Geometry's ledger caveat (nested prefixes under the current lock) still applies to the analytic case. Needs Geometry (a)/(b). | **Hazard (R2).** Countability activates Paper 1 §6's counting measure, and finite description supplies the enumeration. Not done yet; must be flagged as a named step under (M1). |
| E1 $C^\infty$/Gevrey | Known (#332) | Killed (continuum; #334) | — |
| E2 quasianalytic | Known (Denjoy–Carleman; #331 §4) | Killed (no divergence) | — |
| E3 order-$k$ → ∞ | Known pattern | Killed (continuum / analytic limit) | — |
| E4 topology-only | Known (Mostow; quotients) | Killed (`patch-edge` Prop 7.2; geodesic-lifts) | — |
| E5 scale hierarchy | Known (#339) | Killed (continuum, weights) | Weights (#339) |
| E6 discrete solitons | Known: Bartnik & McKinnon, *PRL* 61 (1988) 141, Einstein–Yang–Mills, not vacuum (V-meta) | Killed (no shared $O$) | — |
| E7 unrestricted junctions | Known (impulsive-wave profiles are free functions) | Killed (continuum) | — |
| E8 bifurcations etc. | Correct: smooth ODE bifurcations are sensitivity, not non-uniqueness (standard; e.g. Strogatz, *Nonlinear Dynamics and Chaos*, V-meta) | Off-target | — |
| **L22** lesson | Sound: it restates the characteristic-data picture | — | Same caveat as L20 |

## Structural observation

- **Right in outline.** Hosts that agree on $U$ agree on the domain of dependence (Choquet-Bruhat–Geroch 1969, V-meta). Free data enters across null boundaries (characteristic IVP).
- **One caveat.** "Timelike hypersurfaces are covered by … unique continuation" is not established for $C^\infty$ vacuum Einstein in general. Smooth unique continuation across timelike hypersurfaces can fail (Alinhac's non-uniqueness examples, *Ann. Math.* 117 (1983) 77, V-meta). Holmgren-type results need analyticity. The batch already marks it unchecked; keep it so.

## Strings (each OLD occurs once in `notes/creative/batch-05.md` at `797c960`)

**R1**

OLD:
~~~
(Choquet-Bruhat–Geroch 1969, verified in #332)
~~~
NEW:
~~~
(Choquet-Bruhat–Geroch 1969; bibliographic check only, V-meta, in #332)
~~~

**R2**

OLD:
~~~
- Measure: none. A countably infinite set carries no uniform countably additive measure (Paper 1 §6), so any later weighting is a separate, named step.
~~~
NEW:
~~~
- Measure: none written, but countability is not neutral here. Paper 1 §6: "If distinct evolutions are countable, counting is the unique reasonable measure on observer space", with ratios along finite initial segments. A finite-description class supplies an enumeration (by description length), which is an algorithmic prior by another name. Any such weighting is a separate, named step under (M1) and LT2.
~~~

OLD:
~~~
TT4: no measure; but the set is countable *and dense*
~~~
NEW:
~~~
TT4: no measure written, but countability triggers Paper 1 §6's counting measure (see Measure above); and the set is countable *and dense*
~~~

**R3**

OLD:
~~~
Only null (characteristic) junctions carry free data, as in impulsive waves (Penrose cut-and-paste, unchecked).
~~~
NEW:
~~~
Only null (characteristic) junctions carry free data (characteristic initial-value problem; null gluing: Penrose 1972 cut-and-paste, Dray–'t Hooft 1985, Clarke–Dray 1987, Barrabès–Israel 1991). Impulsive waves and null shells need a metric that is only $C^0$ across the junction; a $C^{1,1}$ junction allows only a jump in curvature (step waves), so the regularity class must be chosen to match.
~~~

## Guardrails

Clean:
- No forbidden Greek letter or its TeX macro.
- No Born, $|a|^2$ or $1/N$ result.
- No Everett framing. "Branch A *is* world A" is David's reframing, recorded verbatim and relayed. It describes which host the observer is in, not a many-worlds reading, but it should be kept clear of #332 N1.
- No topology, (M1) or (A) pick.
- `versions/` and `papers/` are untouched.
