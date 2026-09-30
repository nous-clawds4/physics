SCOPING ONLY, NOT A CLAIM.

# Law-of-$R$ scoping note: pressure test of Claude's critique (#182)

Author: Geometry
Date: 2026-09-29
Read at: `main` = `d09919f` (#182 merge). Target: `reviews/law-of-R-scoping.md` (unchanged since #178, `a82b920`). Critique: `reviews/law-of-R-scoping-claude-opus-5.5.md` (SHA-256 `0697909b…d729`), read in full.

Rules followed:
- This is a review only. The note is not edited here: the v2 is to be built later from the OLD/NEW strings in §2.
- No law of $R$ is adopted, and no family is adopted or ranked. No paper or essay text. No (M1)/(M2) pick, no T1–T3 decision.
- No Born rule, no $|a|^2$, no $1/N$. Q-D1–Q-D5 and #139 are not touched.
- Corrected classifier throughout (`c33r.py`; #169, #174).

**Outcome.**
- **Rulings on 32 items:**
  - 24 CONFIRM, 8 CONFIRM REWORDED, 0 whole-item DECLINE;
  - three sub-claims are declined inside reworded items: 1.10's generalisation, 1.13(b)'s list of single properties, and 3.3's unqualified "F3 meets (J2)".
- **Q3.2 verified.** The §3 SEPARATES branch was unreachable. At $c=0.01$ every final orbit has $\Delta\ge8.897$, so the ratio is $\ge0.819$ for **any** weights. The v2 must say that the exploratory readout could not have separated.
- **Q4 run exactly as Claude specified, preregistered: SEPARATES.**
  - $Q(0.001)/Q(0.01)=0.157144$, against $\le0.2$.
  - Jumps per window stay $\approx5.4$ at every $c\le0.01$.
  - Pre-run SHA-256 `7f230434…e2a5`, registered 2026-09-29 16:21:36 ET. No post-run fixes.

---

## 1. Rulings

Key: **C** = CONFIRM; **CR** = CONFIRM REWORDED. "P*n*" points to §2.

| # | Claude's item | Ruling | Checked against / reason | Patch |
|---|---|---|---|---|
| 1.1 | "Unless a grain" overreaches (Answer, L3, §1 summary) | C | Thm 17's status line: "still needs a grain, or some other discrete cut". Thm 19 and `law-of-r.md`: "Not a blanket 'no map'". v0.7.1 §4.3: "Locked data *can* determine off-curvelet stars". The note's own F1 has finite stars ($\le3$) and no grain; its named extra is the slice (Firewall). Claude's "accurate version" is adopted. | P1–P3 |
| 1.2 | Thm 22 misfiled in L4 | C | `counting-needs-a-slice.md`: named non-slices, a grain among them (item 4), do not make $N(p,\cdot)$ a probability of type-(ii) targets without a finite slice. The theorem is about counting, not finite support. Moved to L10. | P4, P5 |
| 1.3 | Thm 29: Morse is a further extra; one-variable analyticity per curvelet | C | Thm 29's proof needs a Morse condition for isolated critical points. v0.7.1 §5.1: "one-variable analyticity gives discreteness per curvelet" (K2). | P4 |
| 1.4 | L8 "continuum of rays" is false as a universal | C | Thm 31's file (binary tree) has the same loose sentence. Under (a) on the instance, completed histories are countable (C33, I3). | P6 |
| 1.5 | L11 derives conventions from Thm 23 | C | Thm 23(1) only removes the hitchhiker clock. `remainder.md` Open: "A slice / clock for type (ii) …". v0.7.1 §4.2 item 2 ("No proper time") is a convention. Alternation is option (A), chosen against (B) and (C) because of C5. | P7 |
| 1.6 | I3 holds only at periastra | C | Recomputed at $[10,20]$ (`q3check.py`). $c=0.1$: at $r=10$, out $11.0813$ FAIL, in $8.9332$ PASS; at $r=20$, out $23.2368$ PASS, in $16.7925$ (plunge) FAIL. $c=0.01$: at $r=10$, out $10.1075$ FAIL, in $9.8926$ PASS; at $r=20$, out $20.3225$ PASS, in $19.6778$ FAIL. #154 rows 3–4 not re-read. | P8 |
| 1.7 | I6 mis-tagged as a convention | CR | v0.7.1 §2: "The quotient is not optional …"; C9. It is an invariance argument in prose, not a theorem file, so the tag names it as that. | P9 |
| 1.8 | K1: (i) V\*/Option F conflated; (ii) the either/or is a declared constraint | C | (i) Option F = finite-$k$ ($C^k$) join plus graph incidence (`piecewise-geodesic-Ck-graph.md`). Its banner carries K3's "vacuous at $k=1$, prohibitive at $k\ge2$". V\* (`Vstar-extend-vs-not.md`) was a pressure test *under* Option F, and both are demoted. (ii) v0.7.1 §4.2 item 1: "a declared constraint on $R$'s *source* set … named-extra status". | P10, P11 |
| 1.9 | I7 goes beyond C10 | CR | C10's claim column is itself general ("Type (ii) is discontinuous in oriented observer space, not in Obs"), so the note copied v0.7.1. Claude's reason ("Kretschmann jumps change the lump") does not apply to I7, which is about locally symmetric lumps only. The correct scope: a pair *within one such world* keeps the lump; a cross-world edge (without (a)) need not. | P12 |
| 1.10 | I10 misdescribes C16 | CR | C16: rule "jump toward 10", where $\{0,1\}^{\mathbb N}$ (continue/jump) injects, under (H1)–(H7). **Not adopted:** Claude's "general principle", offered as C16's generalisation (not as row text); the repo proves only C16's rule, so the row states that. | P13 |
| 1.11 | I12: add "in a Schwarzschild field" | C | C38 names the idealisation. | P14 |
| 1.12 | I9 "with finite stars"; K3 wording | C | v0.7.1 §7: "With finite stars, depth-$n$ counts converge …". v0.7.1 §4.2: "prohibitive for curvature-changing" jumps; C27: "only forbids". | P15, P11 |
| 1.13(a) | L12 source range stops before the last file | C | `dead-ends-and-rays.md` exists and is L12's last item. #181's brief already reads "from `uniform-law-of-r.md` to `dead-ends-and-rays.md`". | P19 |
| 1.13(b) | "Extra-on-extra" also given to Markov, compact stars, properness, transitivity, asymmetry, totality, selection theorems | CR | Grep of the files. It is given to **selection theorems** and to a **history-dependent law** (`markov-law-of-r.md`). For the others it is given to **bundles** (closed + compact-valued (+ properness); irreflexive + transitive (+ asymmetric); asymmetric + total; totality + countable degrees), not to the single property. **Declined:** Claude's list as stated. | P16–P18 |
| 1.13(c) | "(#46)"-style labels are PR numbers | C | #54, #55, #57, #58, #59, #63 are PRs whose titles match the rows. #46 is Theorem 31 (countable out-degree); uniformity is #45 (uniform-law-of-r.md), so P16 corrects "(#46)" to "(#45)". | P16, P18 |
| 1.14 | Rows found right (I1, I2, I4, I5, I8, I11, I13; K2, K5–K9; L1, L2, L5–L7, L9, L10) | C | No disagreement. L10 gains Thm 22 through P5. | — |
| 1.15 | K4 $K=80/27$ by hand | C | $a=(1-t)^{2/3}$ at $t=0$: $\dot a/a=-2/3$, $\ddot a/a=-2/9$, so $K=12[(2/9)^2+(2/3)^4]=240/81=80/27$. | — |
| 2.1 | Missing: slice-sourced lock-side readout maps (class) | C | v0.7.1 §4.3; §5.1 scalar class and "Which member … is a named extra"; K2; note §4 gap. | P20 (F8), P21 |
| 2.2 | Missing: target-avoiding readouts (option (C)) | C | v0.7.1 §4.2 line 209: "Markov on $O^u$ alone, but it excludes the only worked instance". Rejected for convenience, not by a §1 constraint. | P20 (F9) |
| 2.3 | Missing: sub-ensemble-timed sources | CR | Named in §5.1, the Firewall and K1. But it **fails** a convention in force: v0.7.1 §2 "timing vote … E-smuggling. It is not used". It is listed as named and failing (alongside F4, the grain-bearing family), not as "leaves open". | P20 (F10), P21 |
| 2.4 | Missing: history-dependent laws, including final-condition laws | C | `remainder.md` Open: "whether the law is Markov vs history-dependent"; `markov-law-of-r.md` ("extra-on-extra"); strains §9's Obs-local Hope. | P20 (F11), P21 |
| 3.1 | §3 numbers reproduce | C | Same table as `jtest_out.txt` and `disp_out.txt`, including $D_{10}(0.01)=10.088$ (in) and $9.534$ (out). | — |
| 3.2 | SEPARATES branch unreachable | C | Verified (§3 below). Ratio $\ge0.819$ for any weights. | P22, P24 |
| 3.3 | "F3 is not a separate survivor" overreaches under windowed (J1)/(J2) | CR | v0.7.1 states (J1)/(J2) over "an observed window $[0,T]$". Per-jump deviation, and now Q4 (§4), put F3 on the windowed-(J2) side, while windowed (J1) fails (≈5.4 jumps per 5 periods). **Declined:** "F3 meets (J2)" without a tolerance; the note's F3 row already lists "a window and tolerance for (J2)" as a cost. The wording is neutral, with no ranking. | P22, P28 |
| 3.4 | "History-level form of (J2)" overstates | C | (J2) is per jump, "in a named topology on curvelets". $\Delta$ is an endpoint aggregate. | P23 |
| 3.5 | $c=0.1$ baseline degenerate | C | Final orbits $[8.9332,10.1029]$ (2/3, $\Delta=10.9639$) and $[17.425,23.2368]$ (1/3, $\Delta=10.6618$), both outside $[10,20]$. With a $c=0.05$ baseline: $9.559439/8.386402=1.139874$. | P25 |
| 3.6 | $D_{10}/D_1$ inward only; "90c–235c" mismatch; $90c$ unchecked | CR | At $c=10^{-4}$: $D_{10}/D_1=8.62$ (in), $12.59$ (out). $D_1/c$ over $10^{-4}\le c\le0.1$ runs from $93.5$ ($c=0.1$, out) to $234.2$; Claude's $99.5$–$99.9$ (out) and $219$–$234$ (in) hold for $c\le0.01$. | P26, P27 |
| Q4 | Fixed-window (J2) test, F2 vs F3 | run | §4: preregistered, run as written. | — |
| S1 | "What survives" turns on the window; I13 is a target | C | I13's own tag: "a stated target". | P21 |
| S2 | 1.1 and 1.4 are internal contradictions | C | Removed by P1–P3 and P6; no family's status changes. | — |
| L-a | CSL couples to number density; CSL and Diósi are diffusions; Penrose gives a time estimate | CR | Wording is corrected. The mass-proportional variants Claude names (Pearle–Squires 1994; Ghirardi–Grassi–Benatti 1995) are **not** added as references here, since P29 does not name them (Literature verified both via Crossref in #189). | P29, P30 |
| L-b | A final-condition law is Markov, time-inhomogeneous (Doob $h$-transform) | C | Standard: $P^h(x\to y)=P(x\to y)h_{n+1}(y)/h_n(x)$ is Markov with an $n$-dependent kernel. §L.5's following sentences already say the rest. | P31 |
| L-c | Rideout–Sorkin remark and Weidner method unchecked | C (checked; the note stands) | arXiv gr-qc/9904062 contains "we would have to abandon Bell causality if our aim were to reproduce quantum effects from a classical stochastic dynamics". arXiv 2504.06495 adds a small-signal truncation and counts surviving branches. No patch. | — |

Tally: 33 rows, 32 rulings (Q4 was run, not ruled): **24 C, 8 CR (1.7, 1.9, 1.10, 1.13(b), 2.3, 3.3, 3.6, L-a), 0 whole-item declines**; three sub-claims declined (1.10, 1.13(b), 3.3).

---

## 2. OLD/NEW strings for v2 of `reviews/law-of-R-scoping.md`

- Each OLD occurs **exactly once** in the note at `d09919f`.
- The 31 patches also apply in sequence without conflict (`oldnew.py`, output `ALL OK 31 patches`).
- P20's OLD is the end of the F7 row, including its line break; its NEW appends rows F8–F11 to the §2 table.

**P1 (1.1)**

```text
OLD:
- A lock-side readout gives a singleton or a continuum unless a grain is added (Thms 17, 18, 24–30).

NEW:
- The named lock-side selection devices (neighbourhoods, value classes of continuous invariants, named subsets of $S(O)$, loci) give one class or a continuum unless a grain or another discrete cut is named (Thms 17, 18, 24–30). An explicit lock-side map on a slice can give finite stars without a grain (F1); what it lacks is motivation (K9).
```

**P2 (1.1)**

```text
OLD:
give one class or a continuum. A countable star needs a grain |

NEW:
give one class or a continuum. A countable star from these devices needs a grain "or some other discrete cut" (Thm 17); an explicit map on a slice is not among them (v0.7.1 §4.3; F1) |
```

**P3 (1.1)**

```text
OLD:
- a readout of the germ gives stars that are singletons or continua unless a grain is named (L3–L6);

NEW:
- the named selection devices give stars that are singletons or continua unless a grain or another discrete cut is named (L3–L6); an explicit slice-sourced map can give finite stars, with the slice as its named extra (F1, K2);
```

**P4 (1.2, 1.3)**

```text
OLD:
| L4 | None of the following finite-supports $R$ without a grain: named non-slices; Fermi distance (a continuous scale); lock-side subsets of $S(O)$; Morse, conjugate and cut loci; $I^+$, vacuum and energy conditions | Thms 22, 24, 28, 29, 30 |

NEW:
| L4 | None of the following finite-supports $R$ without a grain: Fermi distance (a continuous scale); lock-side subsets of $S(O)$; Morse, conjugate and cut loci (isolated critical points need a Morse condition, itself extra, Thm 29; along one curvelet one-variable analyticity gives them, K2); $I^+$, vacuum and energy conditions | Thms 24, 28, 29, 30 |
```

**P5 (1.2)**

```text
OLD:
on a DAG with finitely many walks it is well defined | Thms 20, 21 (`fusion-and-path-counting.md`) |

NEW:
on a DAG with finitely many walks it is well defined. It is a probability of type-(ii) targets only with a finite slice, which named non-slices (hitchhiker $\tau$, Fermi balls, continuous $f$, a grain) do not supply | Thms 20, 21 (`fusion-and-path-counting.md`), 22 (`counting-needs-a-slice.md`) |
```

**P6 (1.4)**

```text
OLD:
A countably branching tree still has a continuum of rays | Thms 31, 33 |

NEW:
A countably branching tree can still have a continuum of rays (the infinite binary tree; C16 without (a)); under (a) on the instance, completed histories are countable (C33) | Thms 31, 33 |
```

**P7 (1.5)**

```text
OLD:
| L11 | Hitchhiker $\tau$ does not timestamp type (ii), so edges carry no proper time (hence strict alternation, §4.2) | Thm 23 (`type-ii-clock.md`) | proved; alternation is a convention |

NEW:
| L11 | Hitchhiker $\tau$ does not timestamp type (ii). Zero-duration edges and strict alternation are conventions, not consequences: v0.7.1 §4.2 item 2 ("No proper time"); alternation is option (A), chosen over (B) and (C) because of C5; a type-(ii) clock is Open (`remainder.md`) | Thm 23 (`type-ii-clock.md`); v0.7.1 §4.2 | proved (Thm 23(1)); zero duration and alternation are conventions |
```

**P8 (1.6)**

```text
OLD:
| I3 | The Kretschmann outward edges fail (a) and the inward edges pass;

NEW:
| I3 | At periastra the Kretschmann outward edges fail (a) and the inward edges pass; at the apastron the reverse (on the instance, the edge leaving the orbit's radial range passes);
```

**P9 (1.7)**

```text
OLD:
| row 8, C9 | convention, pinned |

NEW:
| row 8, C9 | proved (invariance argument, v0.7.1 §2: "The quotient is not optional"), pinned |
```

**P10 (1.8)**

```text
OLD:
| V\*/Option F, C24, C25 | proved |

NEW:
| V\* (`papers/Vstar-extend-vs-not.md`, superseded), C24, C25; v0.7.1 Firewall, §4.2 item 1 | continuum proved (C24, C25); the slice-or-sub-ensemble requirement is a declared constraint (convention), not proved exhaustive |
```

**P11 (1.8, 1.12)**

```text
OLD:
| K3 | Finite-jet matching cannot create an edge: vacuous at $k=1$, prohibitive at $k\ge2$ | C27 |

NEW:
| K3 | Finite-jet matching (Option F's finite-$k$ join, demoted) cannot create an edge: vacuous at $k=1$, prohibitive for curvature-changing jumps at $k\ge2$ | C27; `papers/piecewise-geodesic-Ck-graph.md` banner |
```

**P12 (1.9)**

```text
OLD:
A slice-sourced $R$ therefore has no source there, and type (ii) is visible only in oriented observer space |

NEW:
A slice-sourced $R$ therefore has no source there. A type-(ii) pair within one such world leaves the lump path constant, so it shows only in oriented observer space (C10, ESU bare boost) |
```

**P13 (1.10)**

```text
OLD:
| I10 | Without (a), a rule with two jump options on an invariant window has a continuum of completed histories |

NEW:
| I10 | Without (a), the sub-rule "jump toward 10" (continue or one jump at each decision) on an invariant window has a continuum of completed histories, under (H1)–(H7) |
```

**P14 (1.11)**

```text
OLD:
| I12 | For a freely falling near-flat lab,

NEW:
| I12 | For a freely falling near-flat lab in a Schwarzschild field,
```

**P15 (1.12)**

```text
OLD:
| I9 | Depth counts converge to per-vertex weights iff

NEW:
| I9 | With finite stars, depth counts converge to per-vertex weights iff
```

**P16 (1.13)**

```text
OLD:
uniformity (#46); locality; Markov versus history dependence;

NEW:
uniformity (#45); locality; Markov versus history dependence (a history-dependent law is "extra-on-extra");
```

**P17 (1.13)**

```text
OLD:
measurable selection (#63, "extra-on-extra"); selection theorems;

NEW:
measurable selection (#63, "extra-on-extra"); selection theorems ("extra-on-extra");
```

**P18 (1.13)**

```text
OLD:
acyclicity, finite ancestors; no dead ends |

NEW:
acyclicity, finite ancestors; no dead ends. Bundles are "extra-on-extra": closed + compact-valued (+ properness leftover (1)); irreflexive + transitive (+ asymmetric); asymmetric + total (a tournament; a linear order further); total + countable out- and in-degree. Numbers in parentheses are PR numbers |
```

**P19 (1.13)**

```text
OLD:
`uniform-law-of-r.md` … `converse-well-founded-r.md`; `remainder.md`

NEW:
`uniform-law-of-r.md` … `dead-ends-and-rays.md` (L12's order); `remainder.md`
```

**P20 (Q2)**

```text
OLD:
| each is a named extra |

NEW:
| each is a named extra |
| **F8. Slice-sourced lock-side readout maps** (the class; F1 is one member) | A stated map from $(O^u,a)$ at slice vertices to targets, with the scalar from §5.1's class ($K$, $R$, $R_{ab}R^{ab}$, $R_{ab}u^au^b$, $W$) | lock-side; finite stars possible without a grain (F1); sources discrete per curvelet (K2); I4, I5 apply | (a) and (J1)/(J2) depend on the map (I13); slice blind spots (I7, I11); per-map throat clause (K8); only the Kretschmann member has an instance | the scalar, critical point versus level, the map and its constants (v0.7.1 §4.3, §5.1) |
| **F9. Target-avoiding readouts** (arrival option (C)) | $R\subseteq V^\tau\times(V\setminus V^\tau)$ | Markov on $O^u$ alone, no arrival flag (v0.7.1 §4.2); per-history clause (2) needs no strict alternation, since targets are not vertices; lock-side if the map is | no instance (every Kretschmann target is a turning point, C5); rejected in v0.7.1 §4.2 only for that reason; (a) and (J1)/(J2) open | a map that avoids the slice |
| **F10. Sub-ensemble-timed sources** (K1's named alternative) | Sources where members of a chosen discrete sub-ensemble of $E_W$ end | K1 by construction | fails a convention in force: a timing vote, "E-smuggling. It is not used" (v0.7.1 §2); no instance; (a) and (J1)/(J2) open | a grain on $E_W$ (v0.7.1 §5.1, Firewall) |
| **F11. History-dependent laws** (final-condition laws only when not recast as time-inhomogeneous Markov laws, §L.5) | The successor law depends on the path so far, or on a late boundary condition | nothing in §1 excludes it; open in `remainder.md` ("Markov vs history-dependent") | strains v0.7.1 §9's Obs-local Hope (dependence on $(O^u,a)$ and $R$ only) and Problem note 6's memorylessness; no instance; (J1)/(J2) open | a law on $\mathrm{Path}$ ("extra-on-extra", `markov-law-of-r.md`) |
```

**P21 (S1, Q2)**

```text
OLD:
F1 is excluded as a candidate by I13 (it fails both (J1) and (J2)) and by (a) if Compatibility is kept. It stays useful as a consistency witness for the schema without (a).

NEW:
F1 is excluded as a candidate by I13 (it fails both (J1) and (J2)) and by (a) if Compatibility is kept. I13's aim is a stated target, not a theorem, so this exclusion, like F2's survival (late windows only), is conditional on that aim and on which windows count as observed. F1 stays useful as a consistency witness for the schema without (a). F8 and F9 are not excluded by §1; F10 fails a convention in force and is listed as named, alongside F4, the grain-bearing family; F11 is not excluded by §1 but strains the Obs-local Hope.
```

**P22 (3.2, 3.3)**

```text
OLD:
on the grid it **does not separate** them. Shrinking the scale $c$ shrinks each jump in proportion to $c$, but the expected number of jumps grows in inverse proportion. The orbit's net displacement when the jumps end stays at about 9–11 radial units for every $c$ on the grid.

NEW:
on the grid its endpoint observable does not separate them, but it **could not have**: every final orbit at $c=0.01$ has $\Delta\ge8.90$, so the ratio is $\ge0.82$ for any weights (§3). Shrinking $c$ shrinks each jump in proportion to $c$ while the expected number of jumps grows in inverse proportion, and the net displacement when the jumps end stays at about 9–11 radial units. A preregistered fixed-window follow-up is in `reviews/law-of-R-scoping-claude-pressure-test.md` (Q4).
```

**P23 (3.4)**

```text
OLD:
This is the history-level form of (J2): how far

NEW:
This is an endpoint (whole-history) aggregate that mixes (J1) and (J2): how far
```

**P24 (3.2)**

```text
OLD:
**Result (exploratory readout, not preregistered): does not separate.**

NEW:
**Result (exploratory readout, not preregistered): does not separate, and the SEPARATES branch was unreachable.** For any final orbit $\Delta\ge10-w_f$ ($w_f$ its coordinate width), with equality inside $[10,20]$. At $c=0.01$, 99.97% of the final mass is nested, the widest final orbit has $w_f=1.567$ and the smallest final $\Delta$ is $8.897$, so $E[\Delta](0.01)/E[\Delta](0.1)\ge0.82$ for any weights ($\ge0.78$ from the width bound alone), against the $0.2$ needed. This readout could not have separated the two readings.
```

**P25 (3.5)**

```text
OLD:
The ratio $E[\Delta](0.01)/E[\Delta](0.1)=0.880$.

NEW:
The ratio $E[\Delta](0.01)/E[\Delta](0.1)=0.880$. The $c=0.1$ baseline is a one-jump case whose two final orbits, $[8.9332,10.1029]$ (weight $2/3$) and $[17.425,23.2368]$ (weight $1/3$), both overshoot $[10,20]$; with $c=0.05$ as baseline the ratio would be $1.140$.
```

**P26 (3.6)**

```text
OLD:
- Over ten periods, $D_{10}\approx8.6\,D_1$ at small $c$,

NEW:
- Over ten periods, $D_{10}\approx8.6\,D_1$ (inward) and $12.6\,D_1$ (outward) at $c=10^{-4}$,
```

**P27 (3.6)**

```text
OLD:
$\approx 90c$–$235c$ radial units, §3

NEW:
$\approx 93.5c$–$234.2c$ radial units over $10^{-4}\le c\le0.1$, §3
```

**P28 (3.3)**

```text
OLD:
- So on this grid F3 is not a separate survivor: (J2) per jump is bought at the cost of (J1).

NEW:
- So on this grid F2 and F3 coincide on the whole-history endpoint. Over a fixed window they fall on different sides of (J1)/(J2): per-jump deviation falls linearly in $c$ (windowed (J2)), while jumps per window do not fall (windowed (J1) fails); F2 at fixed $c$ meets late-window (J1) and fails (J2). The pressure test's Q4 is a preregistered fixed-window check.
```

**P29 (L-a)**

```text
OLD:
CSL makes the process continuous and couples it to mass density.

NEW:
CSL makes the process continuous and couples it to the smeared number density of identical particles (Pearle 1989; Ghirardi, Pearle and Rimini 1990); mass-proportional coupling is a later variant.
```

**P30 (L-a)**

```text
OLD:
All are stated, uniform stochastic jump laws whose constants are fixed by experiment.

NEW:
All are stated, uniform stochastic laws (jumps for GRW, continuous diffusions for CSL and Diósi; Penrose's proposal is a collapse-time estimate) whose constants are fixed by experiment.
```

**P31 (L-b)**

```text
OLD:
Such a law would take the history-dependent side of L12's "Markov versus history dependence" and fail F7's "Markov".

NEW:
Conditioning a Markov law on a final condition gives a Markov but time-inhomogeneous law (Doob's $h$-transform), whose kernel depends on the final condition and the time remaining; it is not history-dependent as such, and is "Markov" in F7's sense only with that inhomogeneity.
```

---

## 3. Q3.2 check: could the §3 readout have separated?

**No.** For any final orbit $[r_p,r_a]$, $\Delta=\lvert r_p-10\rvert+\lvert r_a-20\rvert\ge10-w_f$, where $w_f=r_a-r_p$. Equality holds when the orbit lies inside $[10,20]$.

Figures from `q3check.py`, exact EPP1 law:

| $c$ | finals | $E[\Delta]$ | $10-E[w_f]$ | nested mass | min $\Delta$ | max $w_f$ |
|---|---|---|---|---|---|---|
| 0.1 | 2 | 10.863169 | 7.282942 | 0 | 10.661756 | 5.811757 |
| 0.05 | 4 | 8.386402 | 7.167025 | 2/3 | 6.896221 | 5.471471 |
| 0.01 | 14,478 | 9.559439 | 9.558567 | 0.999659 | 8.896751 | 1.566652 |

- SEPARATES needed $E[\Delta](0.01)\le0.2\times10.863169=2.1726$.
- Since every final orbit at $c=0.01$ has $\Delta\ge8.896751$, $E[\Delta](0.01)/E[\Delta](0.1)\ge0.81898$ for **any** weights on those orbits. The width bound alone gives $\ge(10-1.566652)/10.863169=0.77632$.
- The ratio can therefore reach neither $0.2$ nor $0.5$ from below. Only DOES NOT SEPARATE was reachable.
- The v2 says so (P22, P24).

---

## 4. Q4 preregistered test

**Spec (Claude, #182 "Question 4", quoted verbatim; lines 183–207, `spec_verbatim.md`):**

> - **Inputs.** Rule and filter: v0.7.1 §5.4's Kretschmann rule, restricted by §4.2's lock-side (a) test (the target geodesic's $r$-range must contain the source $r$). Root and weights: the $r=10$ periastron of $[10,20]$ with $a=\mathrm{seg}$; EPP1, so each decision is a fair coin, since $m\le1$ under (a). Window: **fixed now** at $W=5$ radial periods of the root orbit ($T=5\times425.13=2125.7$). Grid: $c\in\{0.1,\,0.01,\,0.003,\,0.001\}$.
> - **Observable.** $Q(c)=E_{\rm EPP1}\big[\sup_{\tau\in[0,T]}\lvert r_h(\tau)-r_0(\tau)\rvert\big]$, where $r_h$ is the history's areal radius (jumps instantaneous in $\tau$) and $r_0$ is the pure continuation. […] Computed **exactly** by enumerating every history inside the window […]. Secondary readout, reported but not in the criterion: $E[\text{jumps in the window}]$ for each $c$, as the (J1) side.
> - **Criterion (fixed here, before any run).** **SEPARATES** if $Q(0.001)/Q(0.01)\le0.2$: windowed deviation falls at least in proportion to $c$, so F3 meets windowed (J2) where F2 fails it; **DOES NOT SEPARATE** if $Q(0.001)/Q(0.01)\ge0.5$: accumulation or saturation keeps the windowed deviation of order one; otherwise **INCONCLUSIVE**.

(The sub-bullets are joined into lines here. The script header and `PREREG.txt` carry the full text unabridged.)

**Discipline.**
1. `/workspace/lawR/q4/q4.py` was written first, with the full spec quoted in its header.
2. Its SHA-256, `7f230434ef71b8aad91f47d7511e5a7a4d620290fa77ca5fe4066f48defce2a5`, was recorded in `PREREG.txt` with the verbatim criterion and the resolutions A1–A10, **registered 2026-09-29 16:21:36 ET**, before any Q4 run. (`q4.py` was compiled or imported once at 16:21:21 ET, per its `__pycache__` file, which a run as `__main__` does not write. No Q4 output predates 16:21:39.) The order rests on file timestamps on the shared machine. The criterion, grid, window and observable were fixed independently in #182, merged at 16:18:28 ET.
3. It was run once (run 1, 16:21–16:22 ET, 51 s). The script is byte-identical to the pre-run hash (snapshot `q4_run1_snapshot.py`).
4. **No bug was found, and nothing was changed after the output.** Criterion, thresholds, grid and observable are as written.

**Ambiguity resolutions (fixed before the run; the most literal reading):**
- **A1 Window length.** $T=5T_r$, with $T_r$ computed: $T_r=425.134$, $T=2125.670$. Claude's 2125.7 is read as a rounding.
- **A2 Window end.** The window is closed, $[0,T]$. Only the never-jumped history has a decision exactly at $T$; that decision counts. A sensitivity value without it is reported but is not in the criterion.
- **A3 Arrival.** Arrival rule (A) (C6): a germ reached by a jump has one arm. The next decision is at the target orbit's other turning point.
- **A4 $r_0$.** $r_0$ is the root geodesic from rest at $r=10$.
- **A5 $r_h$.** $r_h$ is piecewise geodesic, each segment starting from rest at a turning point (C5). The target value at the jump instant is inside the sup.
- **A6 "Exactly".** Exhaustive enumeration with exact rational EPP1 weights. The sups are numerical: DOP853, rtol = atol = $10^{-11}$, $\ge4000$ samples per half period, then refinement.
- **A7 Non-bound targets.** Rule stated in advance; not triggered (all targets bound).
- **A8 Weights.** $1/(1+m)$. Not triggered beyond $m\le1$.
- **A9 Rule and classifier.** `kr.target`, THROAT = `cross`, `kr.admissible`, with `c33r.classify_robust` (the corrected classifier) patched in.
- **A10 Criterion.** Only the unrounded $Q(0.001)/Q(0.01)$ is used.

**Result: SEPARATES.** $Q(0.001)/Q(0.01)=0.157144153$, which is $\le0.2$. SEPARATES is the label fixed in Claude's criterion. On this grid it means the windowed deviation falls at least in proportion to $c$. It does not establish that F3 meets (J2), which needs a stated tolerance (v0.7.1 §7; 3.3 above).

| $c$ | $Q(c)$ | $Q(c)/c$ | $E[\text{jumps in window}]$ (exact) | histories | A2 sensitivity |
|---|---|---|---|---|---|
| 0.1 | 11.734389597 | 117.3 | $2047/2048=0.99951$ | 12 | 11.733868702 |
| 0.01 | 5.949795274 | 595.0 | $22333/4096=5.45239$ | 2104 | 5.949742841 |
| 0.003 | 2.597517343 | 865.8 | $5519/1024=5.38965$ | 1822 | 2.597501605 |
| 0.001 | 0.934975538 | 935.0 | $11041/2048=5.39111$ | 1825 | 0.934970292 |

- **Weights and jump counts are exact rationals; $Q$ is numerical** (A6).
- **Contingencies.** $m\le1$ at every decision and every target is bound, so A7 and A8 were not triggered. Excluding the decision at $\tau=T$ (A2) moves the ratio by less than $10^{-5}$.
- **Independent cross-check, run after run 1** (`q4check.py`). It uses the closed-form $d\tau/d\chi$ parametrisation, with no ODE and a separate stack enumeration. It shares `kr.target`, `kr.admissible`, `kr.orbit_EL` and the corrected classifier with `q4.py`, so it checks the trajectories, sups and enumeration, not the rule or the (a) test. It gives the same half period ($212.567000$), the same $Q$ to six digits, the same exact jump expectations and history counts, and a ratio of $0.157144$.

**What it shows (neutrally).**
- On this orbit and root, over a fixed five-period window, the EPP1-expected sup-norm deviation from the continuation falls roughly in proportion to $c$ as $c$ goes from 0.01 to 0.001: $Q(0.001)/Q(0.01)=0.157$, $Q(0.001)/Q(0.003)=0.360$.
- The expected number of jumps in the window does not fall. It is $\approx5.4$ for every $c\le0.01$, so F3 still fails windowed (J1) over this window.
- At $c=0.1$ there is essentially one large jump per history.

**What it does not show.**
- Longer windows: the deviation grows with the window, since $D_{10}/D_1\approx8.6$–$12.6$.
- $c<0.001$, other orbits or roots, other slice scalars, other families.
- Any tolerance at which windowed (J2) would count as met.
- Motivation (K9), weights, Born or (M1)/(M2).
- It does not make F3 a survivor where F2 is not, or the reverse. No family is adopted or ranked.

---

## Pins

Python 3.13.5, numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0 (venv `/workspace/g128/venv`). Units $G=c=1$, $M=1$; source orbit $[10,20]$ with $E=0.969087424$ and $L=4.170288281$. Scripts stay on the shared machine; the repo holds no scripts. Everything is deterministic.

| file | SHA-256 | what it pins |
|---|---|---|
| `/workspace/lawR/q4/q4.py` | `7f230434ef71b8aad91f47d7511e5a7a4d620290fa77ca5fe4066f48defce2a5` | Q4 (pre-run hash; unchanged) |
| `/workspace/lawR/q4/PREREG.txt` | `6d23deb408ba3a4ac136b90a5180e23766eb1ef350f15adb2d9757134b5832f7` | preregistration, 2026-09-29 16:21:36 ET |
| `/workspace/lawR/q4/spec_verbatim.md` | `8a97df3642b14a964f94f04988732055097812b6ea5ff3a9ef9edbfe2a4cef57` | Claude's spec, lines 183–207 |
| `/workspace/lawR/q4/run1.txt` | `1e19d181f826bf73145ea6c62ef85d08cbab5f246e0e9a06e8c73d9dcbe23b78` | Q4 run 1 output |
| `/workspace/lawR/q4/q4check.py` | `a0c7fc5543190f287030ee73289757bbe313f5fc892e9056259fe651bde8ddb0` | Q4 independent cross-check (post-run) |
| `/workspace/lawR/q4/check.txt` | `2e18e0f9c6f4b9e36470fb49b7c8cabedb03a828c8c7a1d4ac7733bd33679fb2` | cross-check output |
| `/workspace/g182/q3check.py` | `44d4e8e2c990f5f5a46218e4413e92b25603d3f2195396c05122cbbad0f5fed6` | 1.6 table; 3.2 bound; 3.5 baselines |
| `/workspace/g182/q3check.txt` | `57a717aa612f7ba6e5216af567cdb6d4c7496e2d00c176791377008080bdb410` | its output |
| `/workspace/g182/oldnew.py` | `2201be8ae62d63d1c1f5e736807335ec5df4bb872feb75693e6e0656f8611e18` | OLD counts on `d09919f`; sequential apply |
| `/workspace/lawR/jtest.py` | `f9e9573fe708a72df22c53eee6a93e008b5f20a71b5f4be7aab7d4671d7b0631` | $D_1/c$, $D_{10}$ (3.1, 3.6) |

Imports:
- `/workspace/g168/c33r.py` `f9e9c31b61e9c3889245af8b70cec65bb4a105c50ccbd96c75fd488e431dcd45` (corrected classifier);
- `/workspace/g168/c33x.py` `4c02a785ed38c8c0b9fd9dd9b63d43b4bbc4074e9e9ffbebd4698fd1d5738d40`;
- `/workspace/g154/kr.py` `0432cc20f56afbc3ad862b16de8f825bf9e1d4a490cde07ad8e5740f9d872dee`.

Sources checked: v0.7.1-prose at `main` (§§2, 4.2, 4.3, 5.1, 7, App. A: C5, C9, C10, C16, C24, C25, C27, C38). `papers/`: `counting-needs-a-slice.md`, `neighborhood-uncountable.md`, `grain-not-from-invariants.md`, `law-of-r.md`, `type-ii-clock.md`, `critical-points-in-patch.md`, `countable-outdegree.md`, `Vstar-extend-vs-not.md`, `piecewise-geodesic-Ck-graph.md`, `remainder.md`, `cheat-sheet.md`, and the L12 files (grep only).
