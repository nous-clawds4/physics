# Review: `notes/m1-m2-decision-brief.md` (#266), neutrality and record check

**Verdict: HOLD (narrow).** Heads read: #266 head `a39a1d7`, base main `7fab909`. One file read: `public-papers/observer-space-framework/notes/m1-m2-decision-brief.md`. Sources were read at `7fab909`: `versions/v0.9-prose.md`, `reviews/born-rule-readiness.md`, `notes/zeno-mass-scoping.md`, `notes/born-litmus-test.md`, `reviews/born-litmus-merw-substitution-pressure-test.md`, #230 and #229 reviews, and Paper 1. Appendix B's MMWI and `Strayhorn3` page quotes were checked against the PDFs. Describe-only; this review makes no pick on (M1)/(M2) and has no lean.

The brief is close to even-handed. The HOLD is for two wrong section pointers, one dropped hedge, one dropped qualifier, a one-sided pedigree line and the attribution of the LT3 analysis. All are fixed by the exact strings below. Each OLD occurs once in the file at `a39a1d7`; applying all 13 in order was checked by rebuilding the file.

## Counts (`str.split`)

- At head: 1,547 words; 427 in the table, 1,120 outside. Confirmed.
- Table columns without the header row: (M1) 188, (M2) 204. Confirmed. 16/204 = 7.8%; relative to (M1) it is 8.5%.
- With all 13 strings applied: 1,745 words; table 543; (M1) 241, (M2) 260.
- Tilt scan (my own): "recommendation" (in the status line's "gives no recommendation"), factual "only", one "should" (§5 point 5, a question to David) and one "even". No evaluative adjectives on either side. "The MERW hazard" on the (M2) side is v0.9's own wording (§9, C36), unquoted.

## Findings

1. **Quotes.** Every quoted string resolves in its source at `7fab909`, including both §11 definitions, "This paper does not choose between them", "to be revisited if (M2) is chosen", "= T2 and (M1)/(M2)", "Neither fact is used to decide", "a readout, not a choice", "Gap 2's figures are EPP1 quantities", the F10 option names and FD3's wording. The one Paper 1 phrase, "countable at a grain", is verbatim. The phrase in #229 item 10 occurs four times in v0.9, as stated.
2. **Arithmetic.** Example 1 matches C12 (1/6, 1/6, 1/6, 1/2 against 1/4 each; prefix A 1/2 against 3/4). Example 2 matches the litmus note and the pressure test §1. P7 (1/2 → 1/2; 1/2 → 1/3) and the C13–C15 summaries match.
3. **Pointer error (required, A1, A2).** The table marked "Not carried under EPP1" is in v0.9 **§12**, not §11. The brief points to §11 twice.
4. **Symmetry, hedging (required, H1).** The (M2) cost "Re-anchoring gives up equal weight (C13)" drops v0.9's "in general ... at a fixed cut". As written it reads as unconditional. No (M1) cost is shortened in this way.
5. **Symmetry, Zeno qualifier (required, Z1).** The Zeno note says "only C35 changes" holds **under (A)**. Without an arrival rule, the model without (a) has a non-empty Zeno set. The brief drops the qualifier.
6. **Attribution of the LT3 analysis (required, L1–L3).** The LT3 bullet cited three times is in the litmus note's "Outcome mapping (Lead's draft, pending David)". That note says it "is **not David's wording** and is **pending David**". The brief cites it as "litmus note, LT3 bullet". Since LT3 itself is David's (relayed) wording, readers could take "met by construction" as the record's settled reading of David's test. The strings name the block.
7. **Item (5), pedigree (required for symmetry, P1, P2).** The (M1) "Case for" has "Pedigree: SHPMP 2008's Definition 3 (Appendix B)". (M2) has no pedigree, and SHPMP's rejection of the count appears only as an (M2) cost. v0.9 Appendix B gives a two-sided pedigree:
   - MMWI (24 January 2006) states the count (p. 11) and applies the per-split rule in its Fig. 1E argument (PDF p. 16). Both were checked against the PDF.
   - `Strayhorn3` states path counting, "the form of Paper 1's count" (PDF p. 4; checked).
   - SHPMP 2008: Definition 2 is the count; Definition 3 is the per-split rule. SHPMP rejected the count in its simple form, took the per-split rule as its transition rule and tied its other counts to it by axiom.
   - Paper 1 went back to the count.
   - Appendix B closes: "EPP1 takes the 2008 rule as its working postulate and (M2) would take Paper 1's; neither is chosen here."
   
   P1 and P2 move the pedigree into its own parallel row, one cell per side. It uses no chi wording, cites SHPMP's definitions by number only and does not state any weight as a result. Optional, not drafted: AFLB 2008 counts on a generation-regular tree, where the two rules coincide, so it bears on neither side (Appendix B).
8. **Item (4), status labels (recommended, S1).** v0.9's labels are: (M1) "Per-vertex EPP1, the working postulate here" (§11); EPP1 "It is adopted as a named postulate" (§9, l. 369). (M2) carries no status label; it is "Return to Paper 1's count ..." and "would carry the uniqueness thesis at that cut" (§11). The brief quotes (M1)'s label inside its definition and names the tension only under O1. A reader can take "working postulate" as a lean. S1 adds one sentence giving both sides' labels in parallel, placed under "undecided", and points to #230 F9, which leaves the status wording to David.
9. **Ordering (recommended, S2).** (M1) comes first in every row, example and list, with no stated reason. v0.9 §11 lists it first. S2 says so and says the order implies no ranking. The examples are balanced: Example 1 moves (M2) and Example 2 moves (M1).
10. **O1's basis (recommended, S3).** The readiness quote "no choice of (M1)/(M2)" is that document's own scope line, not a record basis for deferring. v0.9 §11's "This paper does not choose between them" is the basis.
11. **Zeno row (optional, S4).** The (M1) cell of the "Zeno note, (c)" row omits (Z-ii), whose table (c) entry gives (M1) both a property (weights stay functions of the current state) and a cost (positive weight on histories that item 8 ends). (Z-vi) is a mix of (Z-i) and (Z-ii) and can stay omitted.
12. **Options O1–O5.** Each has a record basis. None is a strawman, and costs are given for each. O4 cites "Neither fact is used to decide" as a cost; it reads as a basis, not a cost, but is accurate. Possible missing options, **flagged only, none pushed**:
    - (a) defer until a law of $R$ exists. O1 is an unconditional defer, while the brief's own (M1) "Closes" cell ties uneven single-decision weights to the law of $R$ (readiness §1.2).
    - (b) keep both as named alternatives in v1.0. Already covered by O2.
    - (c) SHPMP 2008's own route: one rule as the transition rule, with the counts tied to it by axiom (Appendix B, "it postulated agreement"). This is not in O1–O5.
13. **§5's six points.** All six are accurate and neutral:
    - 1 (N41, F10) is correct.
    - 2 (readiness stale item 11; the DW (a) row note) is correct.
    - 3 is correct; #261 has merged (`05b74bc`), so gap 4's "(Z-0)–(Z-viii)" is stale as stated.
    - 4 is accurate; the §11 #139 (b) row "= T2 and (M1)/(M2)" bears on it and is already cited in §3.
    - 5's "should" is a question to David, not advice.
    - 6 (F9) is correct.
14. **Guardrails.**
    - No law of $R$.
    - No Born rule, $|a|^2$ or 1/N presented as a result. (M2)'s $1/|C|$ is a definition, cited to §9.
    - No pick on (M1)/(M2), T1–T3, Q-D, #139 or Z.
    - No Everett-vs-Deutsch–Wallace framing, and Bell is not mentioned.
    - None of the banned words appears, before or after the strings.
    - Paper 1 is not edited.
    - No David words are quoted, so the relay-marking standard is not triggered; L1–L3 keep the pending-draft analysis from reading as his.

## Exact strings

Required: A1, A2, H1, Z1, L1, L2, L3, P1, P2. Recommended: S1, S2, S3. Optional: S4. Each OLD matches once in `notes/m1-m2-decision-brief.md` at `a39a1d7`, and the strings do not overlap, so any subset applies cleanly. P1 and P2 go together.

**A1** (required), in `notes/m1-m2-decision-brief.md`:

OLD:
```
which §11's table marks "Not carried under EPP1"
```
NEW:
```
which §12's table marks "Not carried under EPP1"
```

**A2** (required), in `notes/m1-m2-decision-brief.md`:

OLD:
```
The countability thesis stays uncarried (§11 table).
```
NEW:
```
The countability thesis stays uncarried (§12 table).
```

**H1** (required), in `notes/m1-m2-decision-brief.md`:

OLD:
```
Re-anchoring gives up equal weight (C13).
```
NEW:
```
Re-anchoring at each state removes this but in general gives up equal weight at a fixed cut (§11; C13).
```

**Z1** (required), in `notes/m1-m2-decision-brief.md`:

OLD:
```
  - Only C35 changes under the options (note, (b)).
```
NEW:
```
  - Under (A), only C35 changes under the options (note, (b)).
```

**L1** (required), in `notes/m1-m2-decision-brief.md`:

OLD:
```
(`notes/born-litmus-test.md`, "Outcome mapping", LT3 bullet;
```
NEW:
```
(`notes/born-litmus-test.md`, "Outcome mapping (Lead's draft, pending David)", LT3 bullet;
```

**L2** (required), in `notes/m1-m2-decision-brief.md`:

OLD:
```
met by construction (litmus note, LT3 bullet)
```
NEW:
```
met by construction (litmus note, Outcome mapping, LT3 bullet; Lead's draft, pending David)
```

**L3** (required), in `notes/m1-m2-decision-brief.md`:

OLD:
```
is met (litmus note, LT3 bullet)
```
NEW:
```
is met (litmus note, Outcome mapping, LT3 bullet; Lead's draft, pending David)
```

**P1** (required), in `notes/m1-m2-decision-brief.md`:

OLD:
```
 Pedigree: SHPMP 2008's Definition 3 (Appendix B). |
```
NEW:
```
 |
```

**P2** (required), in `notes/m1-m2-decision-brief.md`:

OLD:
```
| Costs | A named postulate (note 9).
```
NEW:
```
| Pedigree (Appendix B) | The per-split rule: applied in MMWI (2006) in the random-walk argument attached to its Fig. 1E; stated as SHPMP 2008's Definition 3, which SHPMP took as its transition rule, tying its other counts to it by axiom. | The count: stated in MMWI (2006, p. 11); path counting, the form of Paper 1's count, in `Strayhorn3` (2006); SHPMP 2008's Definition 2, which SHPMP rejected in its simple form; Paper 1 went back to the count. |
| Costs | A named postulate (note 9).
```

**S1** (recommended), in `notes/m1-m2-decision-brief.md`:

OLD:
```
Each evolution reaching the cut $C$ gets $1/|C|$ (§9).
```
NEW:
```
Each evolution reaching the cut $C$ gets $1/|C|$ (§9).
- **Labels.** v0.9 calls (M1) "the working postulate here" (§11), and of EPP1 says "It is adopted as a named postulate" (§9). (M2) carries no such label; v0.9 says it "would carry the uniqueness thesis at that cut" (§11). Both sit under "**The measure: undecided.**" How these labels read is #230 F9, which the record leaves to David.
```

**S2** (recommended), in `notes/m1-m2-decision-brief.md`:

OLD:
```
Sources are cited by path and §; proofs are cited, not restated.
```
NEW:
```
Sources are cited by path and §; proofs are cited, not restated. (M1) is listed first throughout because v0.9 §11 lists it first; the order implies no ranking.
```

**S3** (recommended), in `notes/m1-m2-decision-brief.md`:

OLD:
```
(v0.9 §11; readiness: "no choice of (M1)/(M2)")
```
NEW:
```
(v0.9 §11: "This paper does not choose between them")
```

**S4** (optional), in `notes/m1-m2-decision-brief.md`:

OLD:
```
(Z-iii)/(Z-vii): weights read $R$ ahead.
```
NEW:
```
(Z-ii): weights stay functions of the current state, with positive weight on histories that item 8 ends. (Z-iii)/(Z-vii): weights read $R$ ahead.
```

