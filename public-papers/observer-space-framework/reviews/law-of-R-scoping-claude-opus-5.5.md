# Exploratory critique: law-of-R scoping note
Reviewer: Claude Opus 5.5 (external critic)
Date: 2026-09-28
Verdict: none (exploratory critique)

**Target:** `public-papers/observer-space-framework/reviews/law-of-R-scoping.md` on `main` (merged via #178, `a82b920`), a note marked **SCOPING ONLY, NOT A CLAIM**.
- **Brief:** `reviews/law-of-R-scoping-claude-cover.md` (#181), read first. Its questions 1–4 are answered in order below; everything else is in the separate part.
- **Sources read:**
  - v0.7.1-prose (§§2, 4.2, 4.3, 5.1–5.4, 7, 9; Appendix A);
  - my own #154 §1 instance rows, and #155 §4;
  - #169 and #176;
  - `papers/cheat-sheet.md` and `papers/remainder.md`;
  - the theorem files for Prop. 13 and Thms 17–19, 22, 23, 29 and 31 (statements and status lines);
  - the L12 files (their "extra / not a grain" wording only);
  - `papers/B-ge2-minimal-toy.md` and `reviews/born-rule-readiness.md` (#159);
  - Paper 1 §9.

**Stance.** Independent. I propose no law of $R$, and I neither pick nor rank (M1)/(M2). I decide none of T1–T3. I use no Born rule, $|a|^2$ or $1/N$, answer no Q-D or #139 item, and propose no edits to `versions/` or `public-essays/`. Labels are the cover's: **Substantive** (a derivation, tag, number or family that is wrong or missing, with its source), **Clarification** (changes no entry), **Nit** (wording).

**What I recomputed.** The note's scripts are not in the repo, so I used my own code from the v0.7 and v0.7.1 rounds, extended here:
- the whole §3 table, exactly;
- the per-jump readout ($D_1/c$ and $D_{10}/D_1$);
- the C33 law at $c=0.01$;
- K4's $K=80/27$, by hand.

Anything not recomputed or not read is listed as unchecked at the end.

---

## Summary

- **Q1.** Most rows are right and correctly tagged. Eight are not.
  - **Grain claim.** The Answer, L3 and the §1 summary say a lock-side readout gives a singleton or a continuum "unless a grain is added". That overreaches the cited theorems, which disclaim a blanket "no map", and the note's own F1 contradicts it: a lock-side readout with finite stars and no grain.
  - **L8.** "A countably branching tree still has a continuum of rays" contradicts the note's own I3/F2 (C33: countable histories under (a)).
  - **L11** presents "edges carry no proper time" as a consequence of Thm 23. It is a convention, and `remainder.md` lists a type-(ii) clock as Open.
  - **L4** misfiles Thm 22, which is about counting needing a slice (a grain is itself one of its failing candidates).
  - **I3** holds only at periastra.
  - **I6** tags a quotient the paper calls "not optional" as a revisable convention.
- **Q2.** Four families that the repo names or leaves open are missing from §2:
  - the general class of slice-sourced lock-side readout maps, of which F1 is one member;
  - target-avoiding readouts (arrival option (C) as a family);
  - sub-ensemble-timed sources (K1's named alternative);
  - history-dependent laws (Open in `remainder.md`).
- **Q3.** Every number in the §3 table reproduces exactly, and "does not separate" follows mechanically from it. But:
  - the SEPARATES branch was unreachable. At $c=0.01$, every final orbit has $\Delta\ge8.90$ because stuck orbits are narrow and almost all lie inside $[10,20]$, where $\Delta=10-\text{width}$ exactly;
  - so the readout measures the (a)-filter's circularisation, not the size-versus-count trade-off;
  - the conclusion that F3 "is not a separate survivor" overreaches. Over any fixed observed window, which is how v0.7.1 states (J1)/(J2), the note's own per-jump readout puts F3 on the (J2) side and F2 on the late-window (J1) side.
- **Q4.** A fixed-window (J2) test of F2 against F3, with inputs, an exact observable and thresholds fixed now. It is cheap. I have not run it.

---

## Question 1: is the constraint inventory correctly derived and tagged?

| # | Row | Finding | Label |
|---|---|---|---|
| 1.1 | Answer bullet 2; L3; "Summary of §1" bullet 2 | These say a lock-side readout gives "a singleton or a continuum unless a grain is added (Thms 17, 18, 24–30)", and L3 adds "A countable star needs a grain". The sources do not support that. See the note below the table. | **Substantive** |
| 1.2 | L4 (Thm 22 part) | Thm 22 (`counting-needs-a-slice.md`) is about making the walk count $N(p,\cdot)$ a probability of type-(ii) targets. Its failing candidates include **a grain itself** ("4. a grain ($d$, or finite $V$ put in by hand)"), and its conclusion is that a **finite slice** is needed. "None of the following finite-supports $R$ without a grain" misstates both the subject and the missing ingredient. It belongs with L8–L10: "named non-slices, a grain among them, do not make $N(p,\cdot)$ a probability without a finite slice". | **Substantive** |
| 1.3 | L4 (Thm 29 part) | Thm 29 says Morse critical points, conjugate loci and cut loci do not supply a countable set "as a lock-side subset of $S(O)$, without a grain". Its proof adds that isolated critical points need a Morse condition, which is itself extra. So the qualifier is "without a further extra (Morse), not only a grain". One more clause would help: along a single curvelet, one-variable analyticity makes critical points isolated for free (K2). That is how slice sources avoid L3–L6. | Clarification |
| 1.4 | L8 | "A countably branching tree still has a continuum of rays" is false as a universal. It is true of the binary tree, the example in `countable-outdegree.md`, whose sentence carries the same loose wording. It is contradicted inside the note: under (a) on the instance, the finitely branching history tree has **countably many** completed histories (I3, F2; C33). At $c=0.1$ they are "jump at decision $k$" plus the pure geodesic. Correct reading: "can still have (binary tree; C16 without (a)); under (a) on the instance it does not (C33)". | **Substantive** |
| 1.5 | L11 | "Hitchhiker $\tau$ does not timestamp type (ii), **so** edges carry no proper time (**hence** strict alternation)" derives two conventions from a theorem that does not imply them. See the note below the table. | **Substantive** |
| 1.6 | I3 | "The Kretschmann outward edges fail (a) and the inward edges pass" holds **at periastra only**. At the apastron of $[10,20]$, the outward target passes and the inward target fails: $23.2368$ and $16.7925$ at $c=0.1$ (v0.7.1 §5.4); $20.3225$ and $19.6778$ at $c=0.01$. On the instance, the edge leaving the orbit's radial range passes and the edge into it fails. #154 rows 3–4, which I3 cites, contain both cases. v0.7.1 §4.2's own sentence is scoped by its periastron examples; I3 drops that scope. | **Substantive** |
| 1.7 | I6 | Tagged "convention, pinned". v0.7.1 §2 argues necessity: "The quotient is not optional. A lump has no canonical tangent space, so without the quotient the successor sets, branch sets and EPP1 weights below would not be functions of physical data." That is part of the object as read ($u$ modulo isotropy), not a revisable convention. Tag: "proved (necessity for invariant stars), pinned (C9)". | **Substantive** (tag) |
| 1.8 | K1 | (i) The source "V\*/Option F" conflates two retired devices. V\* (ensemble-timed vertices, `papers/Vstar-extend-vs-not.md`) is K1's source; Option F (finite-jet matching) belongs to K3 (C27). (ii) Only the continuum (C24, C25) is proved. "$R$'s source set must come from a lock-side slice or an explicit discrete sub-ensemble" is the paper's declared constraint (v0.7.1 Firewall; §4.2 item 1, "a declared constraint … named-extra status"), and the either/or is not proved exhaustive. That half should be tagged convention. | Clarification |
| 1.9 | I7 | "Type (ii) is visible only in oriented observer space" goes beyond C10. C10 shows that a type-(ii) pair (a bare boost at a fixed lump) **can** leave the lump path constant, not that type (ii) is always invisible in Obs; Kretschmann jumps change the lump. Scope it to C10's case. | Clarification |
| 1.10 | I10 | "A rule with two jump options" misdescribes C16, whose options are continue or one jump ("toward 10"), proved under (H1)–(H7) for that rule. The general principle, ≥2 first-edge-distinct arms at infinitely many decisions along an invariant non-Zeno family, is the generalisation, and C16 is its instance. | Clarification |
| 1.11 | I12 | $dK/d\tau=-288M^2u^r/r^7$ is the Schwarzschild formula (v0.7.1 C38 now names the idealisation). Add "in a Schwarzschild field". | Clarification |
| 1.12 | I9; K3 | I9 needs "with finite stars" (v0.7.1 §7; C15). K3 should be "prohibitive for curvature-changing jumps at $k\ge2$" (v0.7.1 §4.2; C27), not prohibitive outright. | Nit |
| 1.13 | L12 | The Source range "`uniform-law-of-r.md` … `converse-well-founded-r.md`" ends before the list's last item (no dead ends: `dead-ends-and-rays.md`). "Extra-on-extra" is marked only on measurable selection (#63), but the files also give it to Markov, compact stars, properness, transitivity, asymmetry, totality and selection theorems. The "(#46)"-style labels are PR numbers; say so. Otherwise checked: every L12 file says "not a grain" or "does not grain", and "named, not adopted". | Nit |

*Note on 1.1.*
- Thm 17's own status line says countability "still needs a grain, **or some other discrete cut**".
- Thm 18 is about the value classes of finitely many continuous invariants on a connected open set, that is, partitions.
- Thm 19 and `law-of-r.md` say, twice, "Not a blanket 'no map'". The note's own L2 repeats that disclaimer.
- v0.7.1 §4.3 says: "Locked data *can* determine off-curvelet stars: the Kretschmann rule's stars are a readout of the germ."
- The note's own F1 is the counterexample: "stated, uniform, lock-side readout; finite stars ($\le3$)", with a named constant $c$ and no grain (C11, C29).

Accurate version: the **named selection devices** give one class or a continuum unless a grain or another discrete cut is named. Those devices are neighbourhoods, value classes of continuous invariants, named subsets of $S(O)$, and loci. **Explicit lock-side maps on a slice** can give finite stars without a grain. What they lack is motivation (K9), not finiteness.

*Note on 1.5.*
- Thm 23(1) removes one candidate clock, the hitchhiker $\tau$.
- Thm 23(2b) supplies a lock-side in-patch Lorentzian distance.
- `remainder.md` "Open" lists "A slice / clock for type (ii); whether in-patch Lorentzian distance (sup) is used at all".
- Under (a), the realising geodesic has a proper time ($19.312$ for C3's pair), which v0.7.1 **declines** to count (§4.2 "No proper time").

So zero-duration jumps are a convention (v0.7.1 §4.2 item 2). Strict alternation is option (A), chosen among (A), (B) and (C) to stop jump chains piling up at one accumulated $\tau$ (C5); zero duration does not imply it. Tag: "proved (Thm 23(1)); zero-duration jumps and alternation are conventions".

**Rows checked and found right:**
- I1, I2, I4, I5, I8, I11, I13;
- K2, K5, K6, K7, K8, K9;
- L1, L2, L5, L6, L7, L9, L10.

**K4 checks by hand.** For dust FLRW with $a=(1-t)^{2/3}$ at $t=0$, $H=-2/3$ and $\ddot a/a=-2/9$, so $K=12[(2/9)^2+(2/3)^4]=80/27$.

---

## Question 2: is any candidate family missing?

Four families are missing. The §1 constraints do not exclude any of them, and each is named in the repo.

**2.1 Slice-sourced lock-side readout maps: the general class of which F1 is one member. (Substantive)**
- **Sources:**
  - v0.7.1 §4.3: "Locked data *can* determine off-curvelet stars … What the germ does not supply is *which* readout, so a countable star is a new physical choice";
  - §5.1's scalar class ($K$, $R$, $R_{ab}R^{ab}$, $R_{ab}u^au^b$, $W$) and "Which member of the class, and critical point versus level, is a named extra";
  - the note's own K2, and its §4 gap ("a second slice scalar … e.g. the Bel–Robinson $W$ … was not tried").
- **Meets:** lock-side; finite stars without a grain are possible (F1 exhibits them); sources are discrete per curvelet (K2); the conventions of I4 and I5 apply.
- **Leaves open:** K9; (a), which depends on the map; (J1)/(J2) (I13); the slice's blind spots (I7, I11: no source on locally symmetric lumps, or for $K$ on flat ΛCDM); per-map completeness in the sense of K8.
- **Why it matters:** §2 lists only the Kretschmann member. Together with finding 1.1, the inventory then reads as if the class did not exist.

**2.2 Target-avoiding readouts, $R\subseteq V^\tau\times(V\setminus V^\tau)$. (Substantive)**
- **Source:** v0.7.1 §4.2, arrival option (C). It is rejected there only because "it excludes the only worked instance, whose targets are all turning points". That is a reason of convenience, not a §1 constraint.
- **Meets:**
  - the process is Markov on $O^u$ alone, with no arrival flag. This bears on T1; I cite that, and do not decide it;
  - per-history clause (2) needs no strict alternation, because jump targets are not vertices;
  - lock-side, if the map is.
- **Leaves open:** it has no instance (every Kretschmann target is a turning point, C5); K9; (a); (J1)/(J2).

**2.3 Sub-ensemble-timed sources: a grain on $E_W$. (Substantive)**
- **Sources:**
  - v0.7.1 §5.1: ensemble-timed selection "requires an explicitly chosen discrete sub-ensemble, which is a grain on $E_W$";
  - the Firewall: "Discrete branch points need a named extra: a lock-side $\tau$-slice or a chosen sub-ensemble";
  - the note's own K1 names it.
- **Meets:** K1, by construction.
- **Leaves open:** it is a timing vote, which v0.7.1 §2 calls E-smuggling and "not used"; a grain on $E_W$; no instance; K9; (a); (J1)/(J2).
- It is declined but named, so §2 should at least list it alongside F4.

**2.4 History-dependent laws, including final-condition laws. (Substantive)**
- **Sources:** `papers/remainder.md` "## Open": "whether the law is Markov vs history-dependent"; the note's L12; §L.5, which observes that "no §2 family is of this kind".
- **Meets:** nothing in §1 excludes it.
- **Leaves open:** v0.7.1 §9's Obs-local Hope, whose definition requires dependence only on $(O^u,a)$ and $R$; Problem note 6 (as v0.7.1 cites it) is strained; K9; (J1)/(J2).
- F7 lists "Markov" as a property, but the complementary family is not listed.

---

## Question 3: is the cheap test well posed as an exploratory readout?

**3.1 The numbers reproduce exactly.** My own code (census and exact EPP1 recursion with the lock-side (a) test; not the note's scripts) gives every entry in the §3 table:

| $c$ | support | $E[\text{jumps}]$ | $cE$ | finals | $E[\Delta]$ | $E[r_{p,f}]$, $E[r_{a,f}]$ | mean proper width |
|---|---|---|---|---|---|---|---|
| 0.1 | {1} | 1 | 0.100 | 2 | 10.863 | 11.764, 14.481 | 2.92 |
| 0.05 | {2} | 2 | 0.100 | 4 | 8.386 | 12.414, 15.247 | 3.06 |
| 0.03 | {4} | 4 | 0.120 | 16 | 8.583 | 13.144, 14.727 | 1.71 |
| 0.02 | {6, 7} | 6.4486 | 0.129 | 92 | 9.053 | 13.656, 14.645 | 1.07 |
| 0.01 | {12, 13, 14} | 13.8418 | 0.138 | 14,478 | 9.559 | 13.935, 14.376 | 0.48 |

- The ratio is $0.880$, and the initial proper width is $10.78$.
- The per-jump readout also reproduces. $D_1/c=234.2$ (inward at periastron) and $99.9$ (outward at apastron) at $c=10^{-4}$. $D_{10}$ is about $10$ at $c=0.01$ (saturation): $10.09$ inward and $9.53$ outward.
- So "does not separate" follows mechanically from the table ($0.880\ge0.5$).

**3.2 The SEPARATES branch was unreachable. (Substantive)**
- For any final orbit, the triangle inequality gives $\Delta=\lvert r_{p,f}-10\rvert+\lvert r_{a,f}-20\rvert\ge10-w_f$, with **equality when the final orbit lies inside $[10,20]$** ($w_f$ is the coordinate width).
- At $c=0.01$, 99.97% of the final mass is nested, and $E[\Delta]=9.559=10-E[w_f]$ to three decimals.
- The widest final orbit has $w_f=1.567$, so the bound alone gives $\Delta\ge8.43$ for every final orbit. The computed minimum over final orbits is $8.897$.
- SEPARATES needed $E[\Delta](0.01)\le0.2\times10.863=2.17$. Once branching stops only on narrow orbits, the ratio cannot fall below $0.78$ by the bound, and is at least $0.82$ as computed.

So the observable measures how far the (a)-filter's circularisation carries the orbit, to near-circular at $r\approx14$. That is essentially independent of $c$. It cannot tell "many small jumps" from "one large jump": both end on a narrow orbit with $\Delta\approx10-w_f$. The readout is well defined, but it does not isolate the trade-off it is used to show ("shrinking $c$ trades jump size for jump count").

**3.3 The conclusion overreaches the paper's (J1)/(J2). (Substantive)** v0.7.1 states both conditions over **observed windows**: "if typical histories are to show geodesic motion over an observed window $[0,T]$". Over any fixed window, the two families end up on different sides of the disjunction.

- **F3 meets (J2) as $c\to0$.** This follows from the note's own per-jump readout, which I reproduced:

  | | $c=10^{-4}$ | $c=0.01$ |
  |---|---|---|
  | $D_{10}$, inward | $0.20$ | $10.1$ |
  | $D_{10}/D_1$, inward | $8.6$ | — |
  | $D_{10}/D_1$, outward | $12.6$ | — |

- **F3 fails (J1)** over any window shorter than its transient, which lengthens as $1/c$. While branching lasts, every turning point carries an edge.
- **F2 at fixed $c$** meets late-window (J1) and fails (J2).

The two coincide only on the whole-history endpoint that §3 measures. The note's own §2 F3 row states this balance correctly ("per-jump deviation → 0 linearly in $c$ over a fixed window … curvelet deviation grows with the window"). The §3 headline ("F3 is not a separate survivor: (J2) per jump is bought at the cost of (J1)") and the Answer paragraph do not.

**3.4 Clarification.** "This is the history-level form of (J2)" overstates. (J2) is a per-jump condition "in a named topology on curvelets". $\Delta$ is an endpoint aggregate that mixes (J1) and (J2). "An endpoint (whole-history) aggregate" would be accurate.

**3.5 Clarification.** The $c=0.1$ baseline is a degenerate one-jump case. $E[\Delta](0.1)$ comes from two final orbits, $[8.9332,10.1029]$ and $[17.425,23.2368]$, with weights $2/3$ and $1/3$. **Both lie outside $[10,20]$** (the overshoot of a single jump). So the ratio compares one overshooting jump with nested circularisation. With $c=0.05$ as the baseline ($8.386$), the ratio would be $1.14$. That is not decisive, but it shows the criterion depends on its baseline.

**3.6 Nit.**
- "$D_{10}\approx8.6\,D_1$" is true of the inward jump. The outward jump gives $12.6$ at $c=10^{-4}$.
- §2's "$\approx90c$–$235c$" does not match §3's $99.9c$–$234.2c$. I get $99.5$–$99.9c$ outward and $219$–$234c$ inward for $c\le0.01$. The $90c$ end, presumably at $c>0.01$, is unchecked.

---

## Question 4: the single most discriminating next test

**Families separated:**
- **F2** at fixed $c$: the transient, late-window (J1) route.
- **F3**: the same rule with $c\to0$, the short-jump (J2) route.

The test is judged by the paper's own windowed (J2), which §3's endpoint observable could not reach (3.2, 3.3).

- **Inputs.**
  - Rule and filter: v0.7.1 §5.4's Kretschmann rule, restricted by §4.2's lock-side (a) test (the target geodesic's $r$-range must contain the source $r$).
  - Root and weights: the $r=10$ periastron of $[10,20]$ with $a=\mathrm{seg}$; EPP1, so each decision is a fair coin, since $m\le1$ under (a).
  - Window: **fixed now** at $W=5$ radial periods of the root orbit ($T=5\times425.13=2125.7$).
  - Grid: $c\in\{0.1,\,0.01,\,0.003,\,0.001\}$.
- **Observable.**
  - $Q(c)=E_{\rm EPP1}\big[\sup_{\tau\in[0,T]}\lvert r_h(\tau)-r_0(\tau)\rvert\big]$, where $r_h$ is the history's areal radius (jumps instantaneous in $\tau$) and $r_0$ is the pure continuation. This is the note's own sup-norm curvelet topology, taken over a fixed window.
  - Computed **exactly** by enumerating every history inside the window: at most about 10 decisions fall in 5 periods, and $m\le1$, so there are at most about $2^{10}$ histories for every $c$.
  - Secondary readout, reported but not in the criterion: $E[\text{jumps in the window}]$ for each $c$, as the (J1) side.
- **Criterion (fixed here, before any run).**
  - **SEPARATES** if $Q(0.001)/Q(0.01)\le0.2$: windowed deviation falls at least in proportion to $c$, so F3 meets windowed (J2) where F2 fails it;
  - **DOES NOT SEPARATE** if $Q(0.001)/Q(0.01)\ge0.5$: accumulation or saturation keeps the windowed deviation of order one;
  - otherwise **INCONCLUSIVE**.
- **Cost: cheap.**
  - The tree inside the window is bounded independently of $c$, so there are at most about 1024 histories per $c$, each needing at most about 10 target computations.
  - $r(\tau)$ comes from the closed form $d\tau/d\chi=p^{3/2}\sqrt{p-3-e^2}\,/\,\big[(1+e\cos\chi)^2\sqrt{p-6-2e\cos\chi}\big]$. I checked that it reproduces the pinned half period $212.567$.
  - I have **not** run the test, so that the criterion stays fixed in advance.

---

## Separate part

### Other findings (not questions 1–4)

- **S1. "What survives" turns on the window. (Clarification)**
  - F1 is "excluded as a candidate by I13 (it fails both (J1) and (J2))". But F2 also fails early-window (J1) (share $1/2$) and (J2) at fixed $c$, and survives only because (J1) holds over late windows.
  - I13's aim ("typical histories look geodesic") is a named constraint that is conditional on the aim, as the note's own I13 tag says ("a stated target"). It is not a proved constraint.
  - So both F1's exclusion and F2's survival rest on counting late windows as observed. Say so where F1 is excluded, so a conditional target is not read as a theorem.
- **S2. Consistency with the note's own tags. (Clarification)** Findings 1.1 and 1.4 are internal contradictions: F1 and I3 (both "pinned") against the Answer, L3 and L8. Fixing the rows removes them without changing any family's status.

### Independent read of §L (Literature's section)

**Overall.** §L is well scoped: every item says where it does not apply, and nothing is proposed, adopted or ranked. It does not bear on (M1)/(M2). Its structural lessons are apt:
- GRW fixes a law's *constants* empirically, the K9 empirical-target branch;
- classical sequential growth narrows a law to a family by axioms, which is the motivation test's "up to named constants";
- DGTZ select jump rates by a principle within a named class;
- consistent histories restate the grain and slice problem as set selection.

Three points:

- **L-a. (Clarification)** §L.1 says "CSL makes the process continuous and couples it to mass density". The cited CSL papers (Pearle 1989; Ghirardi, Pearle and Rimini 1990) couple to the smeared **number** density of identical particles. The mass-density coupling is the later mass-proportional CSL (to my knowledge Pearle and Squires 1994, and Ghirardi, Grassi and Benatti 1995; not checked against the texts). Also, "stochastic jump laws" fits GRW, but CSL and Diósi's model are continuous diffusions, and Penrose's proposal is a collapse-time estimate rather than a stochastic law.
- **L-b. (Substantive)** §L.5 says a final-condition law "would take the history-dependent side of L12's 'Markov versus history dependence' and fail F7's 'Markov'". That is not so in general.
  - Conditioning a Markov process on a final condition gives a **Markov** process (Doob's $h$-transform): $P(x\to y)\,h_{n+1}(y)/h_n(x)$.
  - Its kernel depends on the time remaining and on the final condition. It is time-inhomogeneous, not history-dependent.
  - What such a law strains is memorylessness in Problem note 6's sense, and Obs-locality, unless the final condition and the time-to-go are folded into the state. §L.5's next sentences say this correctly.
  - The same kind of dependence ("depends on where the cut sits") is what v0.7.1 §9 records for a fixed cut. I note the parallel as a fact about both, not as a ranking.
- **L-c. (unchecked)**
  - §L.4: "Rideout and Sorkin note that a classical stochastic dynamics reproducing quantum effects would have to drop Bell causality". I could not confirm this remark is in Rideout and Sorkin (2000).
  - §L.7: the description of Weidner's method ("small-signal truncation … counts surviving branches") is unchecked. The pointer "Paper 1 §9 firewalls it" **checks**: "It is not Weidner … Weidner is not an ally".
  - The bibliographic details of §L's references were not independently fetched. As the cover notes, Literature's #178 reviews are not an independent check of Literature's own §L.

---

## Unchecked

- **The note's scripts** (not in the repo). The §3 table and per-jump figures were recomputed independently (3.1). §2's lower value $90c$ (for $c>0.01$) was not.
- **Theorem proofs.** Thms 20, 21, 24–28 and 30–33, and the L12 files, were checked against their statements and status lines (via `cheat-sheet.md`, `remainder.md` and the files' own status lines), not against their proofs.
- **#159 P1** (the sampled jump share 0.6672) was not re-run this round; I reproduced it at $N=200{,}000$ in #168.
- **§L citations:** see L-c.

## Provenance

- **Scripts** (python 3, numpy, scipy, fractions; kept outside the repo, not committed):
  - `sec3.py`: census, and an exact EPP1 recursion for the §3 observables and the lower-bound check;
  - `perjump.py`: $D_1$ and $D_{10}$ via the closed-form $d\tau/d\chi$;
  - `exact.py` (from the v0.7.1 round): the C33 law;
  - `core.py`: Schwarzschild orbits, Kretschmann targets, and the lock-side (a) test.
- **Workflow:** none. All checks ran in the foreground.
