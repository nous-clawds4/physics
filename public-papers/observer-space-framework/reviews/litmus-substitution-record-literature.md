# Literature record check: litmus revision and substitution test (#254)

**Verdict: HOLD (narrow).** One attribution string is required. Two framing strings for the Lead's text are recommended. **One item is for David:** the recorded conjecture, "the decision-theoretic derivation would fail this test, and this framework would pass it", touches the standing constraint against framing this programme against Deutsch–Wallace. The call is his. **Heads read:** #254 head `de3145c` (commits `5a0ed30` and `de3145c`); base and main `974aeec` (#252 merged from head `c6ae965`); `versions/v0.9-prose.md` at `974aeec`. I re-checked the head before filing.

## Findings

- **F1 (base and earlier strings).** `974aeec` is #252's merge of `c6ae965`.
  - All six #253 strings (L1, L1b, L2, M1, M2, M3), both #249 strings and all six #251 strings are present in the base.
  - At `de3145c`, all survive verbatim except two, which the Lead and Geometry deliberately rewrote:
    - L1 (the "Scope and outcomes" header): it keeps the relayed / not-recorded wording and adds "about 11:39 ET".
    - M1 (the MERW Scope line): it keeps the pointer to the litmus note and now names both paragraphs.
- **F2 (5a0ed30 diff).** It rewrites "Scope and outcomes" and "Pre-emptive use" and adds the section "Substitution test". LT1–LT4 and everything else are byte-identical.
- **F3 (a: attribution; required).** "Scope and outcomes" and the new section both carry "about 11:39 ET, given directly to the Physics Lead in chat and relayed here; the exchange is not recorded in this repository". That meets the #249/#253 standard.
  - "Pre-emptive use" is still dated "about 11:20 ET", but its body now carries the 11:39 revision ("can detect a partial injection … cannot pass a claim that has not been made"). String A1 adds the revision time.
- **F4 (b: the conjecture is marked).** It is headed "David's conjecture (unanalysed)" inside a section labelled David's, L3, "proposed, not yet analysed formally". It is followed by "Neither half is checked here."
  - It is not called a claim of the note or of v0.9 in that place; only the note's top Status line says so. String C1 adds it inline.
  - "This framework would pass it" is conditional and unanalysed. Nothing asserts a pass, a Born, $|a|^2$ or $1/N$ result, or that the framework derives Born.
- **F5 (c: the standing guardrail, for the Lead and David).**
  - The constraint: v0.9 §2 (the firewall) says "It does not frame the problem as Everett versus Deutsch–Wallace". The constraint dates from the 2008 SHPMP referee history.
  - The Lead's own text (the section heading, the attribution, "Neither half is checked here", and the LT1–LT4 relation sentence) does not stage a contest.
  - But the section's illustration names "the authors of the decision-theoretic (Deutsch–Wallace) derivation". Together with the conjecture, that puts a DW-versus-this-framework comparison in a public note.
  - I did not edit David's words. Whether to keep, reword or move the conjecture is **David's call**.
  - String C2 is neutral framing for the Lead's text only. It says the note makes no comparison, and that v0.9 makes no Born-type claim for the test to be run on.
  - A consistency point, noted neutrally: under David's own revised "Pre-emptive use" ("It cannot pass a claim that has not been made"), "this framework would pass it" can only concern a future claim, since v0.9 makes none (§2).
- **F6 (d: literature).**
  - The note describes Deutsch–Wallace only as "the decision-theoretic (Deutsch–Wallace) derivation". That is accurate for Deutsch 1999 ("Quantum theory of probability and decisions", Proc. R. Soc. Lond. A 455, 3129) and Wallace 2012 (*The Emergent Multiverse*), both already cited in v0.9 (§12 row; References).
  - It does not characterise their axioms or branch-relative utility.
  - It makes no claim that the substitution test is novel or standard, and no claim about any literature.
  - So no citation is needed, and I propose none. For the record only: any later analysis of the conjecture would have to engage Wallace's own treatment of non-Born alternative rules and the published critiques of whether the DW axioms presuppose Born (the Lead lists Price, Kent, Albert, Maudlin and Dizadji-Bahmani). The note does not attempt that analysis.
- **F7 (e: internal consistency).** The revised "Scope and outcomes" replaces "It applies only once a Born-type result is claimed. Until then it does not apply" and says so ("this revises the earlier same-day reading"). It also drops the old scoping-note sentence.
  - "Pre-emptive use" now matches the revised scope: it can fail on partial injection and cannot pass an unmade claim.
  - No leftover "applies only once" sentence remains in either note.
  - How the substitution test relates to LT1–LT4 is left open, which is consistent.
- **F8 (de3145c).** Exactly 3 lines change:
  - the Scope line (its Scope portion now has three sentences);
  - the (b) column header ("Now (no claim made; no injection asserted)");
  - R1's added sentence ("There is as yet no $\psi$ here to check for injection").
  - My token script finds unchanged multisets of numbers, O1–O5, R1–R4, C-rows, § pointers and options (i)–(iii). The O rows, the F-M1 line and the Costs line are byte-identical. The only LT change is "LT1–LT4" dropped from the Scope line. The note grows by 58 words (1,359 → 1,417).
  - The reframed rows remain consistent with the revised scope. Each says what a claim would have to show, and none says the test "does not apply".
- **F9 (F-M1 status).** It is unedited. Under the revised scope, option (iii) ("its status against LT1–LT4 is open") now reads consistently. Option (ii) ("whether it could pass LT1–LT4 is scoped in …") still mismatches "cannot pass a claim that has not been made". The call is the Lead's or David's.
- **F10 (guardrails).**
  - Neither note contains any banned word.
  - Bell is not mentioned.
  - The litmus note's only Deutsch–Wallace mentions are in the substitution section (F5).
  - Paper 1 and `versions/` are untouched.
  - The cross-references between the two notes resolve.
- **Word counts (`str.split`):**

  | File | Base | `5a0ed30` | `de3145c` | With strings applied |
  |---|---|---|---|---|
  | `born-litmus-test.md` | 578 | 799 (+221) | 799 | 843 |
  | `merw-litmus-scoping.md` | 1,359 | 1,359 | 1,417 (+58) | 1,417 |

## OLD/NEW (file `public-papers/observer-space-framework/notes/born-litmus-test.md` at `de3145c`; each OLD occurs once)

1. **A1 (required).** OLD: `**Pre-emptive use (David, 2026-10-10, about 11:20 ET, given`
   NEW: `**Pre-emptive use (David, 2026-10-10, about 11:20 ET, revised about 11:39 ET, given`
2. **C1 (recommended; the Lead's label, not David's words).** OLD: `**David's conjecture (unanalysed):**`
   NEW: `**David's conjecture (L3, unanalysed; recorded as stated; not a claim of this note or of v0.9):**`
3. **C2 (recommended; the Lead's text).** OLD: `Neither half is checked here.`
   NEW: `Neither half is checked here. This note makes no comparison between the decision-theoretic programme and this framework, and v0.9 makes no Born-type claim for the test to be run on (v0.9 §2).`

I applied all three mechanically. Each matches once, and the note goes from 799 to 843 words. The MERW note needs no string.
