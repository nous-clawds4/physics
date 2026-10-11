# Literature claim and record check: completed histories versus Paper 1's evolutions (#292)

**Verdict: HOLD (narrow).** The mathematics holds, the script reproduces byte for byte, and no pick is made. Five text strings are needed (R1–R5):

- R1: Paper 1 *does* state an identity criterion for evolutions as curves, and calls it that.
- R2: (M1) needs its relay status.
- R3 and R5: D1 is presented as Paper 1's own premise, and the oriented-germ step is not disclosed.
- R4: bare § pointers are ambiguous; there is no Paper 1 §6.2.

Optional strings N1–N7 follow.

**Heads read (re-checked before filing).**

- #292 head is `69676f5`: two commits (`8e37034`, `69676f5`) on main `5e05692`.
- The diff is exactly four added files: the note, `cvse.py`, `run.sh` and `expected/cvse.txt`.
- Paper 1 (`papers/observer-space-ontology.md`) and v0.9.1 are untouched.
- This file is a one-file PR from `5e05692`.
- #290 is **merged** (`175893c`), and so is #285 (`5e05692`, which is this PR's base), so neither is still under review. The note cites only #290 (T3), which is correct on the base. It makes no $m\le1$ claim, so the "proved given one computed fact" status (#290 §5) does not arise.
- I merged nothing and messaged no one.

## 1. Record grounding

**Paper 1.** Sections are §1–§11; there is **no §6.2**.

- **§4.** It contains the note's quote verbatim: "An evolution is a curve in observer space, parametrized by proper time. Two evolutions are the same until the simply-connected analytic patches disagree. They split at the first $\tau$ at which those patches disagree … That is a premise. It is not a candidate, and it is not reopened below." "Not reopened" is accurate.
- **§6** restates it: "Distinct means physically distinct in the sense of §4: same evolution until the simply-connected analytic patches disagree; distinct at the first $\tau$ those patches disagree."
- **§10** names it: "The identity criterion of §4 is a premise: two evolutions split at the first $\tau$ the simply-connected analytic patches disagree."
- **§3:** "It branches when the simply-connected analytic patches disagree."
- **Search result.** Paper 1 contains no `\sim` or `~` at all. Its only identity criterion for evolutions is this one, for curves parametrised by proper time.
- **The note's sentence.** "Paper 1 defines no $\sim$-equivalence" is true of the symbol. As written, though, it reads as if Paper 1 lacked the equivalence, and Paper 1 explicitly has one. What Paper 1 lacks is a criterion for graph paths whose jumps carry no $\tau$, which is exactly the plan's ILL flag on item 3: "no stated identity criterion on graph paths". **R1.**
- **§2.** The jet–patch "two presentations … the same thing" is as cited.
- **§5–§6.** The antecedent "if distinct evolutions are countable" is in §5 ("if those evolutions are countable") and is named "the antecedent" in §6. Optional N5.

**Other papers.**

- **`papers/analytic-split.md`.** Theorem 2 (§3): two real-analytic curves $I\to\mathrm{Obs}$ that agree on a set with an accumulation point are equal. This supports "curvelets agreeing on $(0,\delta)$ agree at $0$". `\sim` is used there for curves (§1, §5), and $E(O)$ is "not folded into $\sim$" (lines 7 and 67). Both are as cited.
- **`papers/analytic-patch-from-jet.md`.** Theorem A (germs) and Theorem B (maximal simply-connected continuation) are both proved, as cited.
- **`papers/type-ii-adopted.md`.** Definition 8 is delayed forks ("common prefix, then distinct vertices"). Proposition 12 says these graph paths are not analytic curves, so Theorem 2 does not forbid them. As cited.
- **`papers/irreflexive-r.md`.** "Irreflexivity is a weaker extra: no self-loops … Not adopted"; "Named leftover". The note's "a named extra and not adopted" is accurate.

**v0.9.1** (bare § and C pointers in the note are to v0.9.1).

- §8.2 item 2: jumps carry no $\tau$, and a history "is no longer Paper 1's curve parametrised by proper time".
- Item 3: no type-(i) pairs in $R$.
- Item 5: first-edge equivalence for continuations.
- Items 6–7: $B_R$, and the arrival flag.
- Item 8: no-Zeno; a history "ends there".
- §6.2: "a history that ends and one that continues through the same oriented germs count as one evolution". This is **v0.9.1 §6.2**, not Paper 1 (R4).
- §4: "$V$ … *is* Paper 1's observer space, with Paper 1's 'time direction' read as $u$. That is a reading, stated as such."
- §9: completed histories are maximal paths from the root.
- C-rows: C7 (no Zeno on the instance), C11 (3 classes at the $r=10$ periastron), C16 (continuum without (a), proof) and C33 (countable under (a)) are as cited. C35 is the $X$/$Y$ Zeno toy.
- **(M1).** v0.9.1 §11 records it as "Ruled (M1) by David, 2026-10-10, at L3; relayed, not signed". The note's header says only "ruled at L3" (**R2**).

**Zeno note.** The mass-only list (Z-0)/(Z-i), (Z-ii), (Z-iii), per-vertex (Z-iv), (Z-v), (Z-vi), (Z-viii) is consistent with `notes/zeno-mass-scoping.md`. Counting (Z-iv) is correctly left out, since it was dropped under (M1). (Z-vii) is arm pruning. (Z-ix) is limit continuation: proposed by David, relayed, with "exists" marked ILL (N-a; plan item 2). The term "partner row" is the Zeno note's (N-b), and the note does not define it (N3).

## 2. D1 and D2, and the comparison

- **D2** is §8.2 item 5 iterated, and that is faithful. Item 5 is one-step equivalence of continuations; applying it at every decision gives equality of decision paths.
- **D1 is grounded in Paper 1 §4 but goes beyond it in two ways.**
  - It extends "curve" to a trace with $\tau$-less jumps. This is disclosed as a cost.
  - It compares **oriented germs**, so $u$ counts. Paper 1 §4 compares *patches*, and $u$ enters only through v0.9.1 §4's stated reading. A bare orientation change at a fixed lump (§5, C10) would be D1-distinct but is not a patch disagreement. This is not disclosed. **R5.** It does not affect the Kretschmann conclusion, because every Kretschmann edge changes $r$.
- **"Paper 1's own premise."** §4 ("Options and costs") lists this as D1's *For*. That presents D1 as Paper 1's own, while D1 is that premise extended (**R3**). Elsewhere the note is neutral: it gives costs on both sides, "no pick", and critic question 1 asks exactly whether either definition is Paper 1's.
- **Proposition** (D2 → D1 onto; one-to-one iff no reachable self-loop). Correct.
  - At a first-differing decision, two distinct edges have distinct targets, since $R$ is a relation.
  - Continue versus edge differ at $\tau_0$ under the right-continuous trace, unless the target is $O^u$ itself.
  - After a self-loop the arrival flag forces "continue", so the two traces coincide.
- **Case 1.** (a) excludes $\gamma_{O^u}(\tau)$ for $\tau\ge0$, which includes $O^u$. Correct.
- **Case 2.** The note calls its type-(i) step a "reading". It is in fact v0.9.1 §5's definition ("Oriented split": type (i) iff $O'^{u'}=\gamma_{O^u}(\tau)$ for some $\tau>0$ in the curvelet's maximal analytic domain). So case 2 rests on the record, not on a reading, and critic question 2 is answered by §5 as written. Optional N1.
- **Case 3.** Irreflexivity is needed and not adopted. Correct.
- **Kretschmann rule.** A target is the source germ iff $r'=r_0$, since #290 (T1) keeps $v$.
  - A direct path moves $r$.
  - Under "through", $\varepsilon=2\Delta\ell$ has **two** roots at $c=0.1$: $2786.4692$, and a near-throat apastron at $r_0\approx2.000361$ (#290 §2). The note names only the first (N2).
  - The argument still covers both. A decision is reached along a segment, so its orbit is bound. Every apastron below 6 is on a plunging orbit, and such an apastron is reached only by the jump that lands on it, since jump targets are turning points (#290 T1). There the arrival flag allows no decision.
  - So "D1 and D2 coincide on the Kretschmann rule, with or without (a), under either throat convention" follows from cases 1–2 and v0.9.1 §5.
- **Table.**
  - The C16 and C33 rows follow because there are no self-loops.
  - "Paper 1 §5's antecedent fails without (a), holds under (a)" follows from C16 and C33. C33's countability is a computed result (#290 §5), and the note does not claim it is proved.
  - "(M1) weight of an evolution = sum over its D2-classes" is correct. Where a D1-class holds uncountably many D2-classes, "sum" means the path measure of the set.
  - "D1 undefined on toys" is correct: C35 and V0–V2 carry no germs.
  - "D2 countable ⇒ D1 countable" is correct.
- **Zeno.** The (Z-vii) claim on C35 is correct. All histories below $Y$ are Zeno (mass $1/2$, binary branching), so pruning leaves the root's arm set $\{X\}$. The wording "histories … shrink to $\{X\}$" conflates histories with arms (N6). The (Z-ix) items depend on an ILL-flagged term, and the note does not say so (N4).

## 3. Terms before use (well-posedness)

- **Defined before use:** D1, D2, completed history, trace, self-loop and the three cases.
- **Used without definition** (N3):
  - $T_h$;
  - $z$ (the Zeno mass);
  - $f$ (C16's map);
  - V0–V2 (the Zeno note's toys);
  - "partner row";
  - "(T1)" (v0.9.1 §11's T1, plan item 5);
  - bare "item 8" (§8.2 item 8).
- **ILL.** "The plan's ILL flag" is defined in the plan (#285 line 5).

## 4. Scripts

From a fresh clone at `69676f5`:

- **Pins.** sha256 prefixes `cvse.py` `9c11df39fe7d`, `run.sh` `3eea1ec3f8cb` and `expected/cvse.txt` `e0787dee6204` all match.
- **Output.** `sh run.sh` (1.2 s) reproduces `expected/cvse.txt` **byte for byte** (`cmp`).
- **Interpreter.** `run.sh` calls `python`, and this box has only `python3`. I ran it with a `python` alias on PATH (Python 3.13.5). Optional N7 says so in the note rather than changing a pinned file.
- **Contents.** There are no secrets and no absolute paths; `run.sh` does `cd "$(dirname "$0")"`.
- **Results match the note:**
  - 0 self-loops and 0 coincident targets in all 6 runs;
  - (a), $c=0.01$: 29,119 orbits and 29,118 decisions, matching C33's 29,118 passing away edges, with maximum apastron $25.3669$;
  - no (a), $c=0.1$, depth 8, "through": 10,092 decisions, 240 through-throat edges, minimum $|r'-r_0|/r_0=0.000882378$.

## 5. Picks and guardrails

- **No picks.** Nothing is picked on the Zeno readings, the throat convention, F11, gauge or grain. "No pick" appears in the header and in §4.
- **Forbidden words.** χ, `\chi`, egalit, cartoon, GRW, 4-geon, spin-foam: all 0.
- **Other guardrails:**
  - no Born, $|a|^2$ or 1/N result;
  - no Everett-vs-Deutsch–Wallace framing;
  - no law of $R$;
  - nothing recorded as signed;
  - Paper 1 and v0.9.1 untouched;
  - the diff is only these four files.

## Exact strings (file `notes/completed-vs-evolutions.md`; each OLD occurs once at `69676f5`)

**R1 (required: Paper 1's identity criterion).**
OLD: `Paper 1 defines no $\sim$-equivalence (the symbol appears, for curves, in `papers/analytic-split.md`).`
NEW: `Paper 1 does state an identity criterion for evolutions as curves: "Two evolutions are the same until the simply-connected analytic patches disagree" (§4, restated in §6 and called "the identity criterion of §4" in §10). It writes no $\sim$ (the symbol appears, for curves, in `papers/analytic-split.md`), and it gives no criterion for graph paths whose jumps carry no $\tau$.`

**R2 (required: relay status of (M1)).**
OLD: `(M1) is cited as ruled at L3;`
NEW: `(M1) is cited as ruled by David at L3 (2026-10-10; relayed, not signed);`

**R3 (required: D1 is not Paper 1's own).**
OLD: `*For:* it is Paper 1's own premise;`
NEW: `*For:* it applies Paper 1's own premise (§4), extended to traces with jumps;`

**R4 (required: which document a bare § means).**
OLD: `v0.9.1 unedited.`
NEW: `v0.9.1 unedited. Bare § and C pointers are to v0.9.1; sections of Paper 1 (`papers/observer-space-ontology.md`) are marked "Paper 1".`
OLD: `§6.2 (ending and continuing are one evolution, encoded by "common domain")`
NEW: `v0.9.1 §6.2 (ending and continuing are one evolution, encoded by "common domain")`

**R5 (required: D1 compares oriented germs).**
OLD: `*Cost:* "curve" is extended to a trace with jumps that carry no $\tau$.`
NEW: `*Cost:* "curve" is extended to a trace with jumps that carry no $\tau$. The trace also compares oriented germs, so $u$ counts, where Paper 1 §4 compares patches; $u$ enters through v0.9.1 §4's reading of Paper 1's time direction. A bare orientation change at a fixed lump (§5, C10) is D1-distinct but not a patch disagreement. On the Kretschmann rule every edge changes $r$, so this does not bite there.`

**N1 (optional: case 2 is §5's definition).**
OLD: `This reads a type-(i) pair as any $(O^u,\gamma_{O^u}(\tau))$ with $\tau>0$.`
NEW: `This is v0.9.1 §5's oriented split: $(O^u,O'^{u'})$ is type (i) iff $O'^{u'}=\gamma_{O^u}(\tau)$ for some $\tau>0$ in the curvelet's maximal analytic domain.`
(If applied, critic question 2 is answered by §5 as written. Whether to keep it is the Lead's call.)

**N2 (optional: second root).**
OLD: `gives it only at apastra with $\varepsilon=2\Delta\ell$ (#290 (T3); $r_0=2786.4692$ at $c=0.1$).`
NEW: `gives it only at apastra with $\varepsilon=2\Delta\ell$ (#290 (T3); at $c=0.1$, $r_0=2786.4692$ and a near-throat apastron at $r_0\approx2.000361$).`

**N3 (optional: terms used before definition).**
- OLD: `on $[0,T_h)$.` NEW: `on $[0,T_h)$, where $T_h\le\infty$ is $h$'s total accumulated proper time.`
- OLD: `A path that item 8 ends at a Zeno accumulation is one too.` NEW: `A path that §8.2 item 8 ends at a Zeno accumulation is one too.`
- OLD: `Histories with no limit take the partner row.` NEW: `Histories with no limit state take the value of (Z-ix)'s partner reading (Zeno note, N-b).`
- OLD: `which exceeds Paper 1's object (T1)` NEW: `which exceeds Paper 1's object (T1 of v0.9.1 §11; plan item 5)`
- OLD: `an edge to $f(r)\neq r$` NEW: `an edge to $f(r)\neq r$ (C16's $f_{\rm in}$, $f_{\rm out}$)`
- OLD: `| Toys with no germs (C35, V0–V2) |` NEW: `| Toys with no germs (C35; the Zeno note's V0–V2) |`

**N4 (optional: (Z-ix) is ILL-flagged).**
OLD: `- **(Z-ix)** continues a history where a limit state $T$ exists.`
NEW: `- **(Z-ix)** continues a history where a limit state $T$ exists ("exists" needs a named topology: Zeno note N-a; plan item 2 marks (Z-ix) ILL).`

**N5 (optional).**
OLD: `| Paper 1 §5's antecedent on the instance |`
NEW: `| Paper 1 §5–§6's antecedent (distinct evolutions countable) on the instance |`

**N6 (optional: arms, not histories; define $z$).**
OLD: `On C35 the uncountably many D2 Zeno histories below $Y$ shrink to $\{X\}$, so countability can depend on the reading where $z>0$.`
NEW: `On C35 the root's arm set shrinks to $\{X\}$, which removes the uncountably many D2 Zeno histories below $Y$, so countability can depend on the reading where the Zeno mass $z$ at the state is positive.`

**N7 (optional: interpreter name).**
OLD: `- **Run:** `sh run.sh`, with Python 3.13.5 and the standard library only.`
NEW: `- **Run:** `sh run.sh`, with Python 3.13.5 and the standard library only (`run.sh` calls `python`; where only `python3` exists, put a `python` alias on the PATH).`
