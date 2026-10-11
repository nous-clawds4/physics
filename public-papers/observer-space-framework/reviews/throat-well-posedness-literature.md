# Literature claim check: throat well-posedness (#297)

**Verdict: HOLD (narrow).** The geometry is right, the record is read faithfully, and the script reproduces byte for byte. Four text strings are required:

- R1: the finding bears on C37's claim text, and the note does not say so.
- R2: a dropped numeric check is not disclosed.
- R3: the "standing rule" in critic Q1 has no source.
- R4: the jet–patch lock is uncited.

Six optional strings follow (N1–N6).

**Heads read (re-checked before filing).** #297 head is `899fafe`, one commit on main `8e99afd`. Main is unchanged. The diff is four added files: the note (921 words by `str.split`), `twp.py`, `run.sh` and `expected/twp.txt`. Paper 1 and v0.9.1 are untouched. This file is a one-file PR from `8e99afd`. I merged nothing and messaged no one.

## 1. The note's reading of v0.9.1

- **$V$ names no chart.** §4 says: "$V$ is the space of oriented observers $O^u$"; $O$ "is presented as the simply-connected analytic patch $P(O)$ obtained by analytic continuation of that jet. This is a germ-level identification of presentations, not a claim that a maximal global manifold is unique." The note's summary is accurate.
- **Targets come by continuation along the path.** §7 says: "The target germ is reached by continuing the jet analytically along the spacelike geodesic from $p$ with initial tangent $\pm\hat n$ for proper length $\varepsilon$ (analytic continuation along a path; no completed 4-manifold is used), with $u$ parallel-transported."
  - §7 does not literally say "not by matching $K$". That gloss is a fair reading of the definition.
  - The F3 pointer is accurate. `reviews/v0.7-outline-geometry.md` line 118 says that continuing along the path "is the same operation §3 already uses for a curvelet's maximal analytic domain". That §3 is the v0.7-outline numbering, which is v0.9.1 §5's oriented split.
- **No completed 4-manifold.** This is quoted above from §7, and also in §4 ("not a claim that a maximal global manifold is unique").
- **Throat.** §7 says the path "meets the bifurcation 2-sphere, a regular point of the continued metric". It quotes the reflection formula with "the same static-frame speed" and says "'Which exterior' is not a property of the target". §7 also says the rule gives no target "at every vertex on the Schwarzschild bifurcation 2-sphere", which is the note's last line of §3. All quoted correctly.
- **'Stop'.** §7: "Named alternative: the target is undefined when the path meets the bifurcation surface … This adds a case clause keyed to an instance feature."

**Geometry of the path.** I confirm it: the jump path is a slice path, not a horizon-crossing timelike or null curve.

- At a turning point, $u=\gamma(e_{\hat t}+v\,e_{\hat\varphi})$. $\hat n=\pm e_{\hat r}$ is orthogonal to $u$ and to the static Killing field.
- So the radial spacelike geodesic with that tangent lies in the $t=$ const slice through $p$.
- That slice is the image of $T=0$ under the Killing boost, which fixes the bifurcation sphere. On $T=0$, $r=2$ only at $X=0$.
- The path is spacelike throughout. It meets $r=2$ only at the bifurcation sphere, never enters $r<2$, and crosses neither the future nor the past horizon elsewhere.
- Pin (2) checks that the $T=0$ radial line is a geodesic, with $n$ and $e_\varphi$ parallel along it.
- The note calls this "the time-symmetric slice", but it does not state the boost step that covers a source at any $t$ (N3).

## 2. Further checks

- **Kruskal facts.**
  - The metric is $(32/r)e^{-r/2}(-dT^2+dX^2)+r^2d\Omega^2$, with $(r/2-1)e^{r/2}=X^2-T^2$, so $r=2(1+W(z/e))$.
  - $r$ is analytic at $z=0$. Its branch point $z=-1$ is $r=0$.
  - $F(2)=16/e$ and $K(2)=3/4$. All correct.
  - The note carries no citation. Kruskal (1960) and MTW ch. 31 are the standard ones (N5).
  - $F$, $W$, $(T,X)$ and regions I and III are used but not defined in the note (N4).
- **Uniqueness and the jet–patch lock.**
  - "Continuation along a fixed path is unique wherever it exists, by the identity theorem" is correct; see `papers/analytic-patch-from-jet.md` §4, Step 2.
  - "The source germ determines its patch, and the far side lies in it" needs Theorem B: $P(O)$ is the maximal simply-connected realizing patch. Kruskal ($\cong\mathbb R^2\times S^2$) is simply connected and realizes the germ, so it immerses in $P(O)$.
  - Theorem B is stated as proved via complexification ("blocked as a purely real maximal-continuation theorem until that lemma is written"). It is applied within its hypotheses: a real-analytic jet of positive radius, $u$ future unit timelike.
  - The note cites neither Paper 1 §2 ("the unique simply-connected real-analytic patch determined by that jet") nor Theorem B (**R4**). Theorem A (germ uniqueness) is implicit in step 2.
- **E-smuggling and hole lifetimes** (table, row 2).
  - §5: "A world-dependent lifetime is not used, because punching holes makes lifetimes arbitrary."
  - §4: "any load-bearing use of a particular ensemble member E-smuggling … It is not used."
  - Using a punched world to deny the target would be such a use. The claims are accurate.
- **Future timelike $u$ on the far side.**
  - $u=\gamma(n+v\,e_\varphi)$ with $n=F^{-1/2}\partial_T$. Kruskal $\partial_T$ is future-directed on the whole slice, and parallel transport keeps $u$ future in the continued time orientation.
  - The note states the flip: "The static Killing field flips time orientation across the sphere; $u$ does not." That is correct and disclosed. In region III, $\partial_t$ is past-directed.
  - The gauge row maps the far germ to the near-exterior germ at $r'$ by $X\mapsto-X$, $\theta\mapsto\pi-\theta$. This map takes $\partial_T$ to $\partial_T$ and region III's $\partial_t$ to minus region I's, so the image is a region-I turning point with the same $v$. That is consistent with the record's formula and with #290 A6.
- **Reachability.** "No future causal curve runs from region I to region III" is standard. Jumps are type (ii) and carry no $\tau$ (§8.2 item 2). "Under (a) the thresholds are never reached on the instance (C33)" matches §7.
- **Pick or finding?**
  - The note says plainly "This note neither adopts nor rejects it". §7 itself already calls "stop" a case clause added for an instance feature. So "'stop' survives only as an added rule" is a well-posedness finding, not a pick.
  - "Survives only" reads as a demotion, though (optional neutral wording, N2).
  - The header's list of unpicked items omits the throat convention (N1).
- **Bearing on C37.** C37's claim text is "The inward Kretschmann jump path can meet the bifurcation sphere; the rule needs a throat convention (§7)". The note finds that the rule as stated already defines the through target, so a convention is needed only to adopt "stop". That is a substantive consequence for a C-row, and the note does not mention it (**R1**). Whether C37's wording should change is not for this note.
- **Critic Q1's "standing rule".** "Continue to whatever state exists" occurs nowhere in the repository. The nearest record is David's (Z-ix) sentence in `notes/zeno-mass-scoping.md`: "But if it can be defined and it does exist, then it follows the same rule that we use everywhere else" (relayed by the Physics Lead, not otherwise recorded). The note gives no source (**R3**).
- **David's question** is attributed "as relayed by the Physics Lead". That is consistent with the relay standard, although it omits "not recorded here; not signed" (N6).
- **Gauge, grain, F11, Zeno.** Nothing is picked. The gauge rows show existence for both gauge readings and note that only identifications turn on gauge.

## 3. Scripts, and the dropped check

**Scripts** (fresh clone at `899fafe`):

- Pins match: `twp.py` `656757f1c7dc`, `run.sh` `1b51c5ec761f`, `expected/twp.txt` `549d0a9486be`.
- `sh run.sh` reproduces `expected/twp.txt` byte for byte (6 s, Python 3.13.5, mpmath 1.3.0, sympy 1.14.0).
- `run.sh` calls `python`, as the note says. I ran it with a `python` wrapper around a venv interpreter.
- No secrets and no absolute paths.
- The output matches the note: the series, $F(2)=16/e$, $K(2)=3/4$, all Christoffels and covariant derivatives zero, and path lengths $6242.68717543$ and $1201.40570707$ with zero deviation.

**The dropped third check** ($c=0.01$, $r_0=300{,}000$):

- I reproduced it with the script's own integrand. With `mp.linspace(s1, s0, 40)` the length minus $\varepsilon$ is $-1.5468$. Adding breakpoints at the integers in $[-20,20]$ makes the difference exactly $0$ at dps 40, with $r'=324{,}244.030469$ (as in #290) and $\varepsilon=624{,}268.71754317$.
- The cause is quadrature resolution. The 40 equal subintervals each span about $4\times10^3$ in $s$, while the integrand varies on a scale of order 1 near the throat ($X=0$). At $r_0=3000$ and $1000$ the range is about 100 times shorter, and the adaptive rule copes.
- It does not bear on the claim. Under the repository's disclosure norm, a check that was run and dropped should still be stated. A note that pins its numerics should say what was run and left out (**R2**).
- Alternatively, Geometry could add the breakpoints, include the case and re-pin. If so, R2's last sentence changes.

## 4. Guardrails

- χ, `\chi`, egalit, cartoon, GRW, 4-geon, spin-foam, Everett, Deutsch, Wallace and Born: 0.
- No $|a|^2$ or 1/N; no law of $R$.
- (M1) is not cited, and nothing is recorded as signed.
- Paper 1 and v0.9.1 are untouched, and the diff is only the four files.

## Exact strings (file `notes/throat-well-posedness.md`; each OLD occurs once at `899fafe`)

**R1 (required: bearing on C37).**
OLD: `This note neither adopts nor rejects it.`
NEW: `This note neither adopts nor rejects it. It bears on C37's claim text ("the rule needs a throat convention"): on this reading the rule as stated already defines the through target, so a convention is needed only to adopt "stop". v0.9.1 is not edited here; whether C37's wording changes is for the Lead.`

**R2 (required: dropped check).**
OLD: `and the two path lengths equal to $\varepsilon=6242.68717543$ and $1201.40570707$.`
NEW: `and the two path lengths equal to $\varepsilon=6242.68717543$ and $1201.40570707$. A third case ($c=0.01$, $r_0=300{,}000$) was run and dropped. With 40 equal subintervals the quadrature was off by about 1.5. This is a resolution artefact at the throat: the subintervals span about $4\times10^3$ in $s$, while the integrand varies on a scale of order 1 near $X=0$. With breakpoints added at the integers in $[-20,20]$, the length equals $\varepsilon=624268.71754317$ at dps 40. The pinned run omits this case.`

**R3 (required: source of the "standing rule").**
OLD: `The standing rule ("continue to whatever state exists") is stated for an observer's continuation.`
NEW: `The standing rule ("continue to whatever state exists") is not quoted from the repository. Its nearest record is David's (Z-ix) sentence, relayed by the Physics Lead and not signed: "But if it can be defined and it does exist, then it follows the same rule that we use everywhere else" (`notes/zeno-mass-scoping.md`). It is stated for an observer's continuation.`

**R4 (required: cite the jet–patch lock).**
OLD: `Under the jet–patch lock, the source germ determines its patch, and the far side lies in it.`
NEW: `Under the jet–patch lock (Paper 1 §2; `papers/analytic-patch-from-jet.md`, Theorem B, proved there via complexification), the source germ determines its maximal simply-connected patch $P(O)$. Kruskal is simply connected and realizes the germ, so it immerses in $P(O)$, and the far side lies in it.`

**N1 (optional: the throat convention is not picked).**
OLD: `Gauge, grain, F11 and the Zeno readings stay open and unpicked.*`
NEW: `Gauge, grain, F11, the Zeno readings and the throat convention stay open and unpicked; §2 gives a well-posedness finding only.*`

**N2 (optional: neutral wording).**
OLD: `and "stop" survives only as an added rule.`
NEW: `and "stop" is an added rule, as §7 already says ("a case clause keyed to an instance feature").`

**N3 (optional: why the slice).**
OLD: `so the inward path is the radial geodesic of the time-symmetric slice.`
NEW: `so the inward path is the radial geodesic of the time-symmetric slice. $\hat n=\pm e_{\hat r}$ is orthogonal to $u$ and to the static Killing field, and every $t=$ const slice is the image of $T=0$ under the Killing boost, which fixes the bifurcation sphere. The path is spacelike and crosses no horizon away from the sphere.`

**N4 (optional: terms).**
OLD: `In Kruskal coordinates, $r=2(1+W(z/e))$ with $z=X^2-T^2$.`
NEW: `In Kruskal coordinates $(T,X)$ the metric is $F(r)(-dT^2+dX^2)+r^2d\Omega^2$ with $F=(32/r)e^{-r/2}$, and $r=2(1+W(z/e))$ with $z=X^2-T^2$ ($W$ the principal Lambert function). Region I ($X>|T|$) is the source's exterior; region III ($X<-|T|$) is the far exterior.`

**N5 (optional: citation).**
OLD: `so $r=2$ is a coordinate singularity of the Schwarzschild chart, not a curvature one (pin (1)).`
NEW: `so $r=2$ is a coordinate singularity of the Schwarzschild chart, not a curvature one (pin (1); Kruskal 1960, Phys. Rev. 119, 1743; Misner, Thorne & Wheeler 1973, ch. 31, for the Kruskal–Szekeres coordinates and the Einstein–Rosen bridge).`

**N6 (optional: relay standard).**
OLD: `answering David's well-posedness question as relayed by the Physics Lead.`
NEW: `answering David's well-posedness question as relayed by the Physics Lead (not recorded in this repository; not signed).`

## Addendum (2026-10-11): fix pass, #297 `899fafe` → `5778591`

**Verdict: PASS with notes.** One string is recommended (L1, in two places).

**Heads (re-checked before filing).**

- #297 is at `5778591`, open and not merged. Its commits are `899fafe` and `5778591`, and the latter was committed at 4:06 PM ET.
- Main is still `8e99afd`.

**Diff scope.**

- Two files changed: `notes/throat-well-posedness.md` and `notes/v0.10-plan.md`. The plan gains one added line.
- The scripts folder is byte-identical (`git diff --quiet`), so the pins hold without a rerun.
- v0.9.1, Paper 1 and `papers/` are untouched.
- Words by `str.split`: the note has 1,243 and the plan 840, as stated.

**Strings.**

- **Applied as written.** R2 (the disclosure option), R3, R4, N1, N3, N4, N5 and N6 each match their NEW text exactly. Nothing else in the note changed apart from the two amendments below.
- **N2, amended.** The verdict's second sentence now reads: "So, on this reading, the rule already defines the through-throat target; "stop" would be an additional rule, as §7 already says ("a case clause keyed to an instance feature")."
  - The quote is verbatim from v0.9.1 §7: "This adds a case clause keyed to an instance feature."
  - The new wording is more neutral than "survives only" and stays a well-posedness finding.
- **R1, amended.** My two sentences are kept verbatim. The added clause reads: "By the Physics Lead's ruling (relayed; not signed), that wording is superseded on this reading and is to be revised in v0.10 (`notes/v0.10-plan.md` item 12); v0.9.1 is not edited here."

**Attribution of the C37 ruling.**

- **It is the Lead's, not David's.** The ruling is attributed to the Physics Lead. Nothing phrases it as David's.
- **Tag.** The repository's Lead-ruling form is "**Lead ruling (2026-10-11, under David's delegation of 12:34 PM ET; relayed, not signed)**", used 10 times on main, plus one "**Lead ruling (2026-10-11, delegated)**". So "relayed, not signed" is the established tag for Lead rulings too, not only for David's words. The amendment is right to use it.
- **What the amendment lacks.**
  - It has no date.
  - It uses a semicolon where the repository form has a comma.
  - It gives no basis. Is the ruling under a delegation, or within the Lead's own remit?
  - I cannot verify the relay itself, because the ruling is not recorded anywhere else in the repository.
- **Is it David's call?** The record says no. I quote it:
  - David's 12:34 PM delegation covered the open litmus-test items (#283). His 12:46 PM confirmation extends it to F-M1 and Zeno FD1/FD2 (#289). Neither mentions the throat convention or C37.
  - #230's FOR DAVID rule (`reviews/v0.8.1-prose-full-claude-pressure-test.md` §0, after #225 §1) reads: "A finding is FOR DAVID if it adds, removes or rewords what is said about any of these: a side, cost, framing or history of (M1)/(M2); T1 …; Q-D1 …; a hold level." Its F1–F12 list has no throat item; F11 is the #203 lemma.
  - The only throat flag addressed to David is v0.7-outline's "Flagged for David / Physics Lead" list: "**F3. Throat convention (default proposed).** The default proposed is continuation along the jump path … It concerns only the unadopted example, and only the model without (a)." It is addressed jointly, and it concerns the *choice* of default. Geometry's #157 F3 then confirmed that default "in substance". Item 12 keeps the choice open ("The choice between 'continue through' and 'stop' stays open").
  - So rewording C37's claim text without picking a convention falls in no FOR DAVID category. It reads as a Lead editorial decision for v0.10, within the Lead's planning remit. It is not under David's delegation, and nothing in the record requires David's sign-off.
- **The note should say so** rather than leave the basis implicit (L1).

**"Superseded on this reading."** This does not overstate.

- It is scoped to "this reading" (targets are germs continued along the path).
- The same clause says "v0.9.1 is not edited here" and defers the revision to v0.10.
- The convention itself is not picked: §2 still says "This note neither adopts nor rejects it", the header lists the throat convention as unpicked, and item 12 keeps the choice open.

**Plan item 12.** The item is accurate and follows the plan's format.

- It uses the seven columns: # | Item | Pointer | Value | Cost | Needs | Check.
- Its values match items 10–11 in register: Value "Low: one C-row's claim text; no pin moves"; Cost "≈0"; Needs "v0.10 text edit"; Check "WP✓", with #297's finding.
- The pointers (§7; C37; #297) resolve.
- The plan contains no item count ("eleven", "1–11" and so on) that would need updating.
- No F11 pick: item 12 does not concern F11, and items 1 and 10 are unchanged.
- It carries the same undated "Lead ruling, relayed, not signed" tag as the note (L1).

**Guardrails.** The note and the added plan line contain 0 χ/`\chi`, egalit, cartoon, GRW, 4-geon, spin-foam, Everett, Deutsch, Wallace or Born, and no $|a|^2$ or 1/N. There is no law of $R$, no (M1) citation, and nothing recorded as signed. David's question keeps "relayed … not signed".

**Recommended string L1** (each OLD occurs once at `5778591`)

In `notes/throat-well-posedness.md`:
OLD: `By the Physics Lead's ruling (relayed; not signed), that wording is superseded on this reading and is to be revised in v0.10`
NEW: `By a Lead ruling (2026-10-11; a v0.10 wording decision within the Lead's remit, not under David's delegation and in no FOR DAVID category of #230 §0; relayed, not signed), that wording is superseded on this reading and is to be revised in v0.10`

In `notes/v0.10-plan.md`:
OLD: `(Lead ruling, relayed, not signed; #297)`
NEW: `(Lead ruling, 2026-10-11, relayed, not signed; #297)`

If the Lead did intend the ruling to rest on David's delegation, the basis should instead cite the delegation and show that it covers C37. As quoted above, the record does not show that it does.
