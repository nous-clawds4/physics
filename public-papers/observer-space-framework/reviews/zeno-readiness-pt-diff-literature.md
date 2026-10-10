# Diff check of #259 (Zeno and Born-readiness pressure test, applied) — Literature

**Verdict: HOLD (narrow).** One required finding (F1, FD2 is applied in effect). Everything else checks.
**Heads read:** #259 head `ed8cd35` (commits `29d4fb6` pressure test, `ed8cd35` apply), base and main `56ad9b7`. v0.9 read at `56ad9b7`. The #258 review `reviews/zeno-and-born-readiness-claude-opus.md` was read at main.
**Scope:** a diff-only check of the three changed files. Nothing in `papers/` or `versions/` was read for edits, and nothing there changes.

## Checks

1. **Rebuild.** All 63 tuples of `strings.py` were applied to the `56ad9b7` texts: NOTE 30, BRR 33. The SHA-256 is `0e796099…`, as pinned, and `@zeno2@`/`@c5chain@` were filled from the pins. Each OLD occurs exactly once, and both rebuilt files are byte-identical to `ed8cd35`. ✓
2. **Untouched text.** Lines 1–130 of `reviews/born-rule-readiness.md` are byte-identical. The PR changes three files, none in `papers/` or `versions/`. ✓
3. **Rows against #258.** Every row's item reference and quoted wording match #258, with no misquote found. The QUALIFY amendments are stated in the rows and match the strings:
   - **Z3a:** §9's "counting survivors only and conditioning per vertex on survival" is per-vertex conditioning. So it gives (Z-vii)'s values (1 on C35, 1/2 on V2), not (Z-iii)'s 2/3 on V2. This corrects #258 Z3, and I recomputed it.
   - Z4 (rows plus T-cells), B7 (extended to Z-vi–viii), S1 (the four domain-keeping readings) and N4 match their strings.
4. **Counts.** `pt.md` has **25** verdict rows: 19 CONFIRM, 5 QUALIFY (Z3, Z4, B7, S1, S5), 0 REJECT and 1 FOR DAVID row (FD1). FD2 sits under the S5 row. The figures "27 / 21 CONFIRM" come from the brief, not the PR, which states no total.
5. **Recomputed values** (my own scripts, exact where stated). All match.
   - V2: $z=1/4$, and $w(X)$ is undefined / $1/2$ / $2/3$.
   - (Z-vi) and (Z-vii) on C35, V0 and V1.
   - V3: $z=0.20971122$, (Z-iii) $0.63268$, (Z-vii) $1/2$.
   - V0 $\tau$-cut counts $1/(k+2)$; V1 $1/2$; depth counts $1/(1+2^{n-1})$; ternary $0.9995491$ at $n=20$.
   - T3 example: jumps $1/2$ and $4/5$. C5: $(2/3)^{n+1}$.
6. **v0.9 claims in the refresh.** Each was checked against v0.9 at `56ad9b7`:
   - B3: C18 is blind for three scalars, and C23 says the choice of scalar matters.
   - S2a: C38 and §6.1's "A supported laboratory is not a geodesic observer and lies outside the model while matter is open".
   - S2b: §8.2 "the ones a measurement picture would want" and §11 "if co-existing arms count as outcomes".
   - S2c: §8.4 "a typicality rule".
   - S3: §8.5 "trivial maps or a continuum of successors", and C4.
   - B6: the §11 quote "a countably infinite set carries no countably additive probability measure that gives each point the same positive weight".
   - S6: §10's flag "is not lock-side".
   - N4: §11 "co-existence (working Postulate, revisable) versus chance (defined)".
   - S5b/F6: the F6 gloss matches F6 in `v0.8.1-prose-full-claude-pressure-test.md` (Wallace 2007 versus SHPMP).
   - Each quoted phrase occurs exactly once in v0.9. ✓
7. **#245 F1 survives.** The (Z-v) row still says that $\tau$-blindness forces $1/2$ only per-vertex. It now adds that depth-cut counts are set by $X$'s subtree: $0$ for a single history, and $1/2$ at every depth if $X$ branches in two. That refines F1 without reversing it. ✓
8. **#247 fixes survive.**
   - The heading "Gaps before a Born-type question can be posed" is kept.
   - Stale item 5 (the 14,477/14,478 classifier difference) is kept.
   - Gap 3's throat convention (C37) is kept.
   - Gap 4's cost cell now costs every reading, Z-0 to Z-viii.
   - B1a records that l.46 changed in #246's merge.
   - #258 says our #247 F2 aside ("Bertrand does not appear in v0.9") was wrong. We agree: "Bertrand" occurs twice in v0.9, in §4 and §8.4. The refresh's use stands. ✓
9. **Neutrality of the Zeno note.**
   - Every reading has a cost line, including the mirror costs (S1a/S1b) and (Z-v)'s "One lemma … a choice in itself".
   - (Z-viii) is stated as a requirement row, mirroring (Z-v), and is said to fix no single value.
   - The T1/T3 links are pointers, and the T-cells say nothing is decided.
   - (Z-iv) says per-vertex versus counts without any MMWI/Strayhorn pedigree.
   - "natural", "preferred" and "best" occur nowhere in the three files.
   - Optional only: l.59 says "(Z-iv). Under per-vertex weights it is free". This is true (it reduces to the cylinder mass), but "free" can read as a benefit. See O1.
10. **Guardrails.**
    - Paper 1 and v0.9 are untouched.
    - There is no law of $R$, no Born rule or $|a|^2$/1/N result, and no (M1)/(M2), T1–T3, #139 or Z pick. FD1 is left open with both options.
    - There is no Everett-vs-DW framing, and Bell is not called refuted.
    - None of the banned words or the acronym occurs.
11. **"Ours" items.** These have no #258 source item, and §4 discloses them:
    - the header and "Revised" lines;
    - critic questions Q1–Q5 (note) and Q1, Q2, Q4, Q5 (refresh), which are rewritten to the answered points of #258 §3/§5;
    - the (c)-table F-cells for (Z-vi)–(Z-viii);
    - the pins.
    I read them as housekeeping and found no claim in them beyond the CONFIRM'd items.

## Findings

- **F1 (required): FD2 is applied, though FOR DAVID items are not supposed to be.** `pt.md` line 4 says FOR DAVID means "nothing applied". But FD2 (i) reads "(applied, per the refresh brief)". Commit 2 then:
  - keeps the Zeno options in gap 4's "Waits on";
  - extends them to (Z-viii);
  - rewrites the table rule from "lists only the named open calls" to admit them.
  Keeping the list is the pre-#259 status quo. The rule rewrite and the extension, though, carry out option (i). Strings P1 and P2 below record it as the current text, pending David's call. The other choice is for the Lead to revert S5b's "(Z-0)–(Z-viii)" and the rule sentence, at David's direction.
- **O1 (optional): one word in the (Z-iv) cost line.** "it is free" could read as a benefit. "it needs no further lemma" says the same thing neutrally.
- **N1 (note): the counts differ from the brief.** There are 25 rows (19/5/0/1), not 27 (21/5/0/1). The PR's own text states no total, so no string is needed.

## Strings

Each OLD occurs exactly once in its named file at `ed8cd35`.

**P1** — `public-papers/observer-space-framework/reviews/zeno-and-born-readiness-pressure-test.md`

OLD:
```text
(i) Keep them listed, marked as a note's options (applied, per the refresh brief).
```
NEW:
```text
(i) Keep them listed, marked as a note's options. This is the current text after commit 2 (S5b amended, the rule sentence, the list extended to (Z-viii)), applied pending David's call because the refresh's brief named them as a waits-on item.
```

**P2** — `public-papers/observer-space-framework/reviews/born-rule-readiness.md`

OLD:
```text
which are a note's options, not calls ((Z-0) and (Z-iv)–(Z-viii) are not in v0.9).
```
NEW:
```text
which are a note's options, not calls ((Z-0) and (Z-iv)–(Z-viii) are not in v0.9). Whether they stay listed here is left to David (#259 pressure test, FD2).
```

**O1 (optional)** — `public-papers/observer-space-framework/notes/zeno-mass-scoping.md`

OLD:
```text
Under per-vertex weights it is free:
```
NEW:
```text
Under per-vertex weights it needs no further lemma:
```

## Word counts (`str.split`)

- `notes/zeno-mass-scoping.md`: 1,118 → 2,238.
- `reviews/born-rule-readiness.md`: 3,892 → 4,932 (the refresh section went from 1,182 to 2,222, as stated).
- `zeno-and-born-readiness-pressure-test.md`: 1,601.
