# Literature and claim check: V-topology audit (#303)

**Heads read (re-checked before filing):** #303 head `50528d0` (one commit, open, not merged), off main `7fdd4f0`; main `7fdd4f0`. **Verdict: HOLD (narrow).** The audit's main claim stands: v0.9.1 puts no topology or distance on $V$. Three strings are required:
- R1 is a disclosure about Thm 3 that bears on #301's neutrality.
- R2 and R3 fix two proposed rewordings that change a claim, contrary to the note's "None of these rewordings changes a claim".

There are five optional strings.

**Scope.** The diff touches only `notes/v-topology-audit.md` and `notes/v-topology-audit-scripts/` (`classify.py`, `run.sh`, `expected/hits.md`). Paper 1 (`papers/observer-space-ontology.md`) and v0.9.1 are untouched. The note is 1,064 words (str.split).

## 1. Candidate claims against the record

- **Curvelet / segment (§5).** The quote is exact: §5 line 182 reads "the unique curve in $V$ traced by the geodesic from $(p,u)$ in the patch $P(O)$ (Prop. 3.2 and Thm 3 of `papers/geodesic-lifts.md`)". The Thm 3 paraphrase is accurate. However, Thm 3 continues: "Equivalently, each projection of $\gamma$ to a finite-order jet space $J^k$ is a real-analytic map $I\to J^k$, so $\gamma$ is real-analytic as a map into the inverse limit (a Fréchet space of jets)."
  - So the one-curvelet continuity comes from the inverse-limit topology on jets, in that curve's own Fermi coordinates.
  - `papers/fermi-distance.md` line 17 builds the Fermi-slice distance from the same structure ("The inverse-limit topology on $J^\infty$ is metrizable").
  - The note's conclusion holds: v0.9.1 uses this only along one curve and never passes it to $V$. Comparing states on different curvelets needs a common slice modulo $O(3)$, which is Thm 16's added step.
  - But the note doesn't say this. A reader of #301 could take "continuity along a curvelet is already defined" to mean (T1)'s inverse-limit variant is already implicit. **R1** discloses it neutrally.
- **Germ (§4).** "Equal or not; nothing says how close" is accurate, and §4 defines no closeness. On the jet-patch lock: analytic continuation (§7, `papers/analytic-patch-from-jet.md`) does use the sheaf of germs of the analytic metric *over a given world*, and that sheaf's étale space carries the germ topology. That topology lives over the spacetime $M$, one world at a time. It does not descend to $V$, whose points are germs modulo pointed analytic diffeomorphism across all worlds. So no closeness on $V$ is smuggled in. Optional N2 says so.
- **(a) test (§8.2).** Accurate: line 313 defines "(a)-admissible $\iff O'^{u'}\in F(O)\setminus\{\gamma_{O^u}(\tau):\tau\ge0\}$", and line 138 defines $F(O)$ as the germs reached along future-directed timelike geodesics. It is a yes/no membership test.
- **Jump rule, $\varepsilon$ and $\ell$ (§7).** These are spacetime lengths along the jump path. Accurate.
- **"Does not match $K$".** `notes/throat-well-posedness.md` line 11 reads "picks targets by geodesic continuation, not by matching $K$". Accurate.
- **§9 "limit"/"converge".** Line 395 reads "depth-$n$ counts converge to per-vertex weights on every cylinder set iff siblings are asymptotically balanced". These are limits of numbers on trees. Accurate.
  - **Histories.** David's question as relayed covers histories as well as $V$. (M1)'s measure (ruled by David at L3, 2026-10-10, relayed, not signed) is defined on cylinder sets of finite prefixes. The shared-prefix structure is the one closeness-like notion the record puts on histories. It is used only measure-theoretically, through the cylinder σ-algebra. v0.9.1 never uses a topology on histories, and none on $V$ follows from it. The note doesn't mention it; optional N1 adds it.
- **(J2) and T3.** Line 411 reads "within a stated tolerance of the continuation in a named topology *on curvelets*, not merely on germs at the vertex". Line 485 reads "Formalising 'near' belongs to *Mathematical Foundations*". Accurate.
- **§8.1 "$C^\infty$ path" (critic Q2).** Line 263 reads "The traveller may switch worlds at a shared oriented germ, the path in $V$ is $C^\infty$". A switch at a shared oriented germ continues the same curvelet (`geodesic-lifts.md`: "the simply-connected patch determines a unique curvelet"). So the one-curvelet reading is adequate, and nothing more is presupposed.

## 2. Completeness: independent grep

The classifier's vocabulary reproduces: 290 hits, plus 13 substring-only hits dropped (9 in v0.9.1 and 4 in Paper 1, which matches the note).

I grepped v0.9.1 and Paper 1 independently for small, perturb, approximat, dense/density, compact, generic, stable, robust, arbitrar, "tends to", sufficiently, infinitesimal, approach, adjacent, local/locality, connected, boundary, accumulat, uniform, discrete, curve, and ε–δ phrasing. Hits that are absent from the table and could bear on closeness:

| Where | Text | Judgement |
|---|---|---|
| v0.9.1 §11, line 474 | "Refine into small moves: no such structure; the proper time of small moves (T1)" | Flagged open: the text itself says "no such structure" |
| v0.9.1 §10, lines 433/435/477 | "Obs-local", "Locality in $V$" (3×) | Defined without topology: "the arm set and weights at a state $(O^u,a)$ depend only on that state and $R$" (line 433) |
| v0.9.1 §11, line 443 | "'local' as the no-teleport intuition", "local in note 6's sense" | Flagged open: the same paragraph sends the nearness reading to T3 |
| v0.9.1 §5, §8.2, lines 200/337 | "open maximal domain", "compact proper-time interval", "accumulation" | Topology on the $\tau$-line only |
| v0.9.1 §4, line 166 | "generic smooth metrics" | Spacetime metrics, not $V$ |
| Paper 1 §2, line 29 | "A history is a curve" | One-curvelet sense: Paper 1 has no jumps |
| Paper 1 §6, line 125 | "discrete, or discrete at a physically relevant grain", "continuum … with no such grain" | Cardinality and grain, explicitly left open ("a grain the later dynamics will have to specify") |
| Paper 1, lines 17/33/59/75 | "approximations", "approximated by this", "nearest wrong cousins" | Physics-approximation programme language, and an idiom |

No hits for perturb, robust, stable, sufficiently, infinitesimal or ε–δ phrasing. None of the missed hits assumes a topology on $V$, so the 8-row ill-posed list is complete for this vocabulary. Adding these terms to the classifier is optional; I'm not asking for it.

## 3. Sample of "fine" verdicts

- **All 6 curvelet rows** (48, 158–160, 258, 261) are right. Rows 158–160 are §11's "Next: discrete step or continuous" row, where "a continuous curve has no 'next'" is about the parameter. That is borderline but fair.
- **All 11 flagged-open rows** (131, 132, 137, 146, 149, 156, 170, 171, 173, 176, 242) are right: each sits in text that names "near"/nearness or (J2)'s topology as open.
- **15 random rows** (seed 303: 17, 49, 51, 66, 75, 85, 104, 127, 139, 140, 223, 226, 232, 268, 290) are all right. Examples: "continuum" as cardinality, "long-path limit", "closed timelike curves" (spacetime), "cross-continuation jumps" (spacetime).

**One inconsistency:** row 156 (line 474, "a move to a near observer") is flagged open, but row 169 (line 483, "without making any jump near") is marked ill-posed. The very next sentence after row 169 reads "Whether that meets the no-teleport intuition depends on what 'near' means, which is a question for *Mathematical Foundations* and an open call". By the classifier's own standard, row 169 is flagged open. Reclassifying it would change the counts (283/7) and the pins, so I don't require it. R3 instead fixes its rewording.

## 4. The 8 ill-posed rows

The six "discontinuous" verdicts are right: no topology on $V$ means discontinuity between states is undefined. Critic Q1's conditional is correct: in any Hausdorff topology where curvelets are continuous, a type-(ii) jump at fixed accumulated $\tau$ is discontinuous, because the target differs from the source.

| Line | OLD (v0.9.1) | Proposed NEW (note) | Check |
|---|---|---|---|
| 55 | "histories are now discontinuous, and their jumps carry no proper time" | "histories now include type-(ii) jumps, which leave the curvelet and carry no proper time" | Accurate; no claim changes |
| 184 | "At a type-(ii) jump a history is **discontinuous in oriented observer space**." | "… **leaves its curvelet in oriented observer space**." | Accurate: type (ii) means the target is not $\gamma_{O^u}(\tau)$, $\tau>0$ (line 186) |
| 278 | "Joins are discontinuous type-(ii) jumps plus incidence in a graph." | "Joins are type-(ii) jumps plus incidence in a graph." | Accurate |
| 474 | "Short jumps: near at the vertex, not (J2)." | "Short jumps: small $\varepsilon$ at the vertex (a spacetime length), not (J2)." | **Changes the claim.** "Near at the vertex" is the counterpart of (J2)'s "not merely on germs at the vertex" (line 411), so it means nearness of germs at the vertex, not spacetime shortness. **R2.** |
| 474 | "whether a short discontinuous move counts as teleporting is open" | "whether a short jump counts as teleporting is open" | Accurate; keeps "is open" |
| 483 | "each jump is still discontinuous in oriented observer space" | "each jump still leaves its curvelet" | Accurate |
| 483 | "So the transient reduces how often the observer jumps without making any jump near." | "So the transient reduces how often the observer jumps, not what a jump does." | **Changes the claim.** The (a)-restriction does change which jumps occur (C30, C33). It also drops the "near" that the next sentence refers back to ("depends on what 'near' means"). **R3** restates only what the paragraph already says. |
| 550 (C10) | "Type (ii) is discontinuous in oriented observer space, not necessarily in $\mathrm{Obs}$ (§5)" | "Type (ii) leaves the oriented curvelet, and need not change the lump in $\mathrm{Obs}$ (§5)" | Accurate: keeps the hedge ("need not"), and §5 says "The lump path in $\mathrm{Obs}$ may stay constant" |

## 5. Paper 1

0 ill-posed hits, confirmed. "Countable at a grain" and "discrete at a physically relevant grain" (line 125) do not presuppose a topology. Countability is cardinality, and the grain is left explicitly to "the later dynamics". A grain could be a partition as well as a topology, and Paper 1 does not say which. "A history is a curve" (line 29) is the one-curvelet sense, since Paper 1's motion has no jumps (v0.9.1 line 55).

## 6. Scripts

- I made a fresh `git clone`, checked out `50528d0`, aliased `python` to Python 3.13.5, and ran `sh run.sh`. The output is **byte-identical** to `expected/hits.md`.
- All three pins match: `classify.py` `e54427b9304d`, `run.sh` `f3d20e7aab11`, `expected/hits.md` `63955d707b7f`.
- The totals reproduce: 290 = 85 + 6 + 180 + 11 + 8; Paper 1: 30 + 2 + 16.
- There are no secrets and no absolute paths. The script uses relative repo paths, and `run.sh` `cd`s to the repo root.

## 7–8. Neutrality, terms, guardrails

- **Neutrality.** The note makes no (T0)–(T3) pick, and nothing on Zeno, the throat convention, F11, gauge or grain. David's question is "relayed by the Physics Lead (not signed)". (M1) is not cited, and if N1 is applied it carries its tag. With R1, the Thm 3 point no longer reads as (T1) being already implicit.
- **Terms.** Mostly defined by § pointer. "CWS" is used without definition (N3). "T3" is used for v0.9.1 §11's nearness tension in the same note that names #301's (T3), so N4 disambiguates.
- **Guardrails.** 0 χ/\chi and 0 forbidden words. No Born, $|a|^2$ or 1/N result; no Everett-vs-DW framing; no law of $R$.

## Strings (each OLD occurs once in `notes/v-topology-audit.md` at `50528d0`)

**R1** (required; disclosure)
OLD: `but continuity in $\tau$ along a single segment is defined (Thm 3).`
NEW: `but continuity in $\tau$ along a single segment is defined (Thm 3). Thm 3 gets it from the inverse-limit (Fréchet) topology on jets, taken in Fermi coordinates along that one geodesic. The same jet-space topology underlies (T1)'s inverse-limit variant (`papers/fermi-distance.md`), but v0.9.1 uses it only along one curve and never passes it to $V$, so this neither adopts nor favours (T1).`

**R2** (required; the rewording kept the wrong sense)
OLD: `| "Short jumps: small $\varepsilon$ at the vertex (a spacetime length), not (J2)." |`
NEW: `| "Short jumps: near at the vertex only in some topology on germs there (none is named; small $\varepsilon$ is a spacetime length), not (J2)." |`

**R3** (required; the rewording changed the claim)
OLD: `| "So the transient reduces how often the observer jumps, not what a jump does." |`
NEW: `| "So the transient reduces how often the observer jumps; each jump still changes the orbit by $O(1)$ and still leaves its curvelet." |`

**N1** (optional; histories)
OLD: `"Smooth segments" is right, and the record's own sense is stronger: segments are analytic.`
NEW: `"Smooth segments" is right, and the record's own sense is stronger: segments are analytic. Histories carry one further structure: (M1)'s measure (ruled by David at L3, 2026-10-10, relayed, not signed) is defined on cylinder sets of finite prefixes (§9). Sharing a long prefix is a closeness of histories only in that measure-theoretic sense; v0.9.1 uses no topology on histories, and none on $V$ follows from it.`

**N2** (optional; jet-patch lock)
OLD: `**Spacetime structure.** Two germs are equal or not; nothing says how close.`
NEW: `**Spacetime structure.** Two germs are equal or not; nothing says how close. Analytic continuation uses the sheaf of germs over one world, whose étale topology lives over that spacetime, not on $V$.`

**N3** (optional; term)
OLD: `tree limits, CWS)`
NEW: `tree limits, Continuous World Switching (CWS, §8.1))`

**N4** (optional; label collision with #301)
OLD: `| (J2), T3 "near" (§9, §11) |`
NEW: `| (J2), §11's T3 "near" (§9, §11; not #301's (T3)) |`

**N5** (optional; no string). Reclassify row 169 (line 483 "near") as flagged open, consistent with row 156. This needs a `classify.py` override plus new pins and counts (283/7). If it is done, drop R3's table row instead.
