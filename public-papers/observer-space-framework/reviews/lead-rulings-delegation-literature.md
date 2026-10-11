# Review: Lead rulings under David's delegation (#283), record and diff check

**Verdict: HOLD (narrow).** Heads read: #283 head `b3a9091` (commits `89371eb` and `b3a9091`), base main `4d1fb11`. Describe-only; this review makes no pick and has no lean.

**#281 history.** #281 merged as `4d1fb11` with #282 G1 applied (`3b65211`). #282 merged as `b685034`.

The rulings are clearly the Lead's, not David's, and David's L3 text is byte-identical. Two text points block:
- **FD4's failure rule leaves out the empty-S1 case.** David's text says a rule that slides in "with nothing else changing" fails, but the Lead's "if and only if" makes that case a pass. Commit 2 does not close this. X1 and X2 fix it.
- **FD3 states David's 10:33 principle in paraphrase without marking it as one.** X3 fixes it.

Two scope questions are flagged, not strung (§3).

## 1. David's L3 text

Byte-identical, checked by substring against main at `b3a9091`:
- `## The question` through the "Genuine emergence" quote, including the LTs, "Genuine emergence needs YES on all four", "Scope and outcomes", "Pre-emptive use" and the "Purpose" quote;
- the whole of David's "Substitution test" text, including the conjecture. Main's section text is an exact prefix of the head's.

The FD4 and FD5 Lead rulings are appended inside the `## Substitution test (... part of the L3 answer ...)` section. Each carries its own Lead label, so they are not attributed to David, but they sit under a heading that says "part of the L3 answer".

## 2. Attribution, delegation and hold level

- **Labels.** All nine rulings carry "**Lead ruling (2026-10-11, under David's delegation of 12:34 PM ET; relayed, not signed)**" in full where they are recorded, and "Lead ruling (2026-10-11, delegated)" in pointers. None is phrased as David's.
- **Delegation quote.** In the Labels line it is verbatim as relayed ("I've told you how the test works. I want you to answer those questions as best you can."), at about 12:34 PM ET, given directly to the Physics Lead in chat and relayed here, and not recorded in this repository. The Labels line does not say "not signed"; X4 adds it (recommended).
- **Authority level.** No hold level is claimed for any Lead ruling. The rulings sit at the delegation's level, revisable by David. The only new "hold" token is "holds" in the quoted T-a definition.
- **Consistency with David's quotes.**
  - The per-LT sort fits "genuine emergence needs a yes on all 4": LT1, LT3 and LT4 stay necessary for genuine emergence as emergence conditions. It also fits "designed to detect cheating and that's it": only LT2, plus the substitution test, can return a fail.
  - The LT2 clause "not yet fixed ... cannot pass either" matches "Pre-emptive use" ("It cannot pass a claim that has not been made").
  - FD5 matches "Scope and outcomes". (M1) at L3 is untouched.
  - "The cheating test proper is LT2 plus the substitution test" bears on the open relation of the substitution test to LT1–LT4, for which no R-option is picked. It is compatible with several of them, including (R-a), (R-b) and (R-d). X6 (recommended) adds a pointer.
- **The well-posedness principle (FD3).** It is cited with a time and as relayed. But after the colon the text reads as David's principle while giving the Lead's application ("a test term that is not defined cannot be applied"), and it carries no "paraphrased" or "not signed" mark. **X3 (required)** marks the paraphrase.
  - The route "given directly to the Physics Lead" is not verifiable from my brief, which says only "relayed, not in the repo".

## 3. Scope of the delegation (flagged, no string)

The delegation's words refer to "those questions" about "the test" (the litmus test), but the record does not show which questions those were.
- **F-M1.** #264 FD6 says "F-M1 itself stays David's call". F-M1's own text says options (ii) and (iii) "change firewall text and a hold-level reading". The ruling edits the v0.9.1 §2 firewall: the hazard sentence gains the scoping clause, so the firewall is **not** byte-identical (disclosed in the PR body and P14).
- **Zeno FD1 and FD2.** These are #259's Zeno/readiness items, not litmus-test items.
- Whether "those questions" covers F-M1 and the two Zeno items is for David or the Lead to confirm. If it does not, the §2 hazard-sentence edit is the one change to the firewall text.

## 4. FD4 and Ontology's flag 3

- **"in whole or in part"** is David's own wording, in "Scope and outcomes" (2026-10-10, about 11:39 ET, relayed, part of the L3 answer): "**Failure** means circular reasoning that injects the Born rule directly, in whole or in part."
- **Commit 1's tension (the PR body's own judgement call):** an item in S3's "both" cell is independently motivated yet restates $W$ on a sub-case. It failed under the "if and only if" sentence, but its "breaks only independently motivated items ... pass" sentence could read as a pass.
- **Commit 2 resolves that tension.** The pass sentence now requires that none of the items "restates the target rule on any sub-case". This is faithful to "in part" and to T-a's own "In part" definition. It is identical in both notes, as is the "if and only if" sentence. The substitution note's [PJ] "left open" now points to the ruling ("restating $W$ on a sub-case is a fail"), which is accurate. Whether a given item restates $W$ remains S3's judgement (critic question 2).
- **A second gap remains: empty S1.**
  - T-a's definition, quoted in the ruling itself, says ""Slides in" means that S1 is empty, or holds only items judged under S3 to restate $W$".
  - David's text says "If it could be slid in with nothing else changing, the rule was put in by hand, and the test fails."
  - The ruling's "fails if and only if some item broken by the swap ... is ... restated" does not fail an empty S1, and its pass sentence is met vacuously when nothing breaks.
  - T-a's cost note says every valid derivation has a non-empty S1 where $W'$ conflicts with $W$, so the case is narrow, but the rule as written contradicts David's words.
  - **X1 and X2 (required)** add it.
  - The separate question of declared postulates with an empty break column (substitution note, section (ii), critic question 3, [PJ]) is untouched and stays open.

## 5. Markers, Resolution lines and pointers

- **Markers.** The changed and unchanged markers in the PR body match the diff.
  - In the #264 review, §3's heading gains the resolution note and seven Resolution lines are added. The FD texts, l.4, l.42 (the B1 row) and l.88 are unchanged.
  - In the Zeno review, §3's heading gains the note and two Resolution lines are added. The FD texts and l.63's cell are unchanged.
- **Resolution pointers.** All resolve:
  - FD1 → *Per-LT sort*;
  - FD2 → *LT2's inputs (#264 FD2)*;
  - FD3 → *LT3 (#264 FD3)*;
  - FD4 → the litmus note's "Substitution test" section and the substitution note's "The test as recorded, and an operational form";
  - FD5 → "Substitution test";
  - FD6 → the MERW note's F-M1 "Resolution" and P14;
  - FD7 → the substitution note's Status.
  - The Zeno review's FD1(i) and FD2(i) match the options as written there. The zeno-mass note's pointer goes to that review's §3.
- **FD7.** The gloss sits in the substitution note's Status line, at the note's only use of "main paper". It is accurate as a ruling: the next sentence already confines the v0.9 firewall to v0.9.
- **Ontology's flag 2.** Fixed in commit 2. `m1-m2-decision-brief.md` l.20 now cites the litmus note's current "Outcome mapping" heading exactly. It belongs here only as a pointer repair; the brief's body is otherwise unchanged (+11 words).
- **Readiness.** The F-M1 clause is added at l.56 (§1.2 (M2) item), which is above the v0.9 refresh. The refresh's Scope line says "Nothing else above is edited." X5 (recommended) records the exception.

## 6. v0.9.1 and guardrails

- **P14 and its edits** are status and text only: a pointer clause, with no physics claim, pin or number.
- **Byte-identical:** Appendix A and the circularity-wall line. "Locality in $V$" still occurs 3 times.
- **Not byte-identical:** the §2 firewall, by the hazard-sentence clause only (§3 above).
- **"cartoon".** The readiness l.135 "cartoon" is pre-existing on main and untouched; it sits in a historical quote ("(§6 is a cartoon; matter open)"). **v0.9.1 has no "cartoon"** at main or at head. Line 23 is the "Not applied" line at main and P11 at head, so the commit-2 note about a "cartoon" at v0.9.1 l.23 has no referent.
- **Word deltas (`str.split`, whole file):** all match the PR body and commit 2.

  | File | Delta |
  |---|---|
  | litmus | 2,891 → 3,265 (+374) |
  | MERW | +84 |
  | substitution | 3,824 → 3,958 (+134) |
  | Zeno note | +12 |
  | #264 review | +168 |
  | readiness | +28 |
  | Zeno review | +75 |
  | v0.9.1 | 20,064 → 20,196 (+132) |
  | brief | 2,153 → 2,164 (+11) |

- **New tokens:** labels, times and dates only (2026-10-11, 12:34, 10:33, #264, #279, 0.9.1, P14, section numbers). No number is removed, except one "0.9" and one "6" in the litmus note, from the replaced LT1 draft bullet; both remain elsewhere in the file.
- **Forbidden words:** 0 introduced.
- **Other guardrails:**
  - No Born, $|a|^2$ or 1/N result. New "Born" uses are "Born-type claim".
  - No Everett-vs-Deutsch–Wallace framing; the counts are unchanged.
  - Paper 1 and `papers/` are untouched.
  - Every new "signed" is "not signed".

## 7. Exact strings

Each OLD occurs once in its file at `b3a9091`. All were applied together by script: litmus 3,265 → 3,332 words; substitution 3,958 → 3,976; readiness 5,137 → 5,154.
- Required: X1, X2, X3.
- Recommended: X4, X5, X6.

**X1** (required), `notes/born-litmus-test.md`, FD4 ruling in "Substitution test":

OLD:
```
The test fails if and only if some item broken by the swap (S1) is, under S3, the target rule (or a special case of it) restated, or a parameter tuned to it. If the swap breaks only items that are independently motivated and none of which restates the target rule on any sub-case, that is a pass on this point.
```
NEW:
```
The test fails if and only if the swap breaks nothing (S1 is empty: the rule slides in), or some item broken by the swap (S1) is, under S3, the target rule (or a special case of it) restated, or a parameter tuned to it. If the swap breaks at least one item, and every item it breaks is independently motivated and none of them restates the target rule on any sub-case, that is a pass on this point.
```

**X2** (required), `notes/substitution-test-scoping.md`, FD4 ruling:

OLD:
```
The test fails if and only if some item broken by the swap (S1) is, under S3, the target rule (or a special case of it) restated, or a parameter tuned to it. If the swap breaks only items that are independently motivated and none of which restates the target rule on any sub-case, that is a pass on this point.
```
NEW:
```
The test fails if and only if the swap breaks nothing (S1 is empty: the rule slides in), or some item broken by the swap (S1) is, under S3, the target rule (or a special case of it) restated, or a parameter tuned to it. If the swap breaks at least one item, and every item it breaks is independently motivated and none of them restates the target rule on any sub-case, that is a pass on this point.
```

**X3** (required), `notes/born-litmus-test.md`, *LT3 (#264 FD3)*:

OLD:
```
under David's well-posedness principle (2026-10-11, about 10:33 AM ET, given directly to the Physics Lead in chat and relayed here; the exchange is not recorded in this repository): a test term that is not defined cannot be applied.
```
NEW:
```
under David's well-posedness principle (2026-10-11, about 10:33 AM ET, given directly to the Physics Lead in chat and relayed here, not signed; the exchange is not recorded in this repository; paraphrased here, not quoted: every term of a question should be defined, and an ill-posed question is rejected rather than answered), a test term that is not defined cannot be applied.
```

**X4** (recommended), `notes/born-litmus-test.md`, Labels line:

OLD:
```
("I've told you how the test works. I want you to answer those questions as best you can."; given directly to the Physics Lead in chat and relayed here; the exchange is not recorded in this repository)
```
NEW:
```
("I've told you how the test works. I want you to answer those questions as best you can."; given directly to the Physics Lead in chat and relayed here, not signed; the exchange is not recorded in this repository)
```

**X5** (recommended), `reviews/born-rule-readiness.md`, refresh Scope line:

OLD:
```
Nothing else above is edited.
```
NEW:
```
Nothing else above is edited, except that the §1.2 (M2) item (l.56) later gained F-M1's scope clause (Lead ruling (2026-10-11, delegated); `notes/merw-litmus-scoping.md`).
```

**X6** (recommended), `notes/born-litmus-test.md`, *The conjecture's "pass"*:

OLD:
```
How the substitution test relates to LT1–LT4 is open (options (R-a) onward in `notes/substitution-test-scoping.md`, none picked).
```
NEW:
```
How the substitution test relates to LT1–LT4 is open (options (R-a) onward in `notes/substitution-test-scoping.md`, none picked); the per-LT sort's "the cheating test proper is LT2 plus the substitution test" (Lead ruling (2026-10-11, delegated)) bears on it but picks no option.
```

## Addendum: fix pass `b3a9091..b2cf06b`

**Verdict on the fix pass: HOLD (narrow), one string.** Heads read: #283 head `b2cf06b` (one fast-forward commit on `b3a9091`), main `4d1fb11`, and Geometry #288 (`reviews/lead-rulings-283-geometry.md`) at `1b666a2`. The commit touches 4 files: the litmus note, the substitution note, the brief and readiness. Every change in it is accounted for below. Nothing else changed.

### FD4

- **Wording:** the final FD4 sentence pair is identical in the litmus and substitution notes (one regex match in each).
  - Each note has exactly one "if and only if" sentence and one "pass on this point" sentence.
  - No earlier pass wording remains ("breaks only independently motivated items", "every item it breaks").
- **David's sentence:** "If it could be slid in with nothing else changing, the rule was put in by hand, and the test fails." is byte-exact against David's Substitution-test text in the litmus note. That text appears twice in the litmus note (L3 text and FD4) and once in the substitution note (FD4).
- **Logic: now right.**
  - Empty S1 fails.
  - A non-empty S1 fails if any broken item is, under S3, the target rule (or a special case or sub-case of it) restated, or a parameter tuned to it.
  - A pass on this point needs at least one break, with every break independently motivated and none restating the target rule on any sub-case.
  - "or sub-case" agrees with T-a's "In part".
- **Note, no string:** a non-empty S1 containing only S3 "neither" items (not independently motivated, not a restatement) is neither a fail nor a pass on this point. That is consistent with "Purpose" (only injection fails), and such an item bears on LT2's "fixed for independent reasons" instead.
- **Reconciliation:** X1/X2's content is carried in full, and P1/P2's NEW text replaces their phrasing (PR body). This is as described.

### X3–X6 and Geometry #288

- **X3, X5, X6:** each NEW is present once, verbatim, and no OLD remains.
- **R1, R2 (brief l.38), O1 (brief l.20), O2 (readiness l.56) and O3 (brief l.45):** each NEW is present once, verbatim.
- **X4:** "not signed" is applied, with one departure: a scope clause is inserted after it ("scope as relayed: LT sorts, FD2–FD7, F-M1, Zeno FD1/FD2"). This is the one open point, below.

### Delegation scope (open)

- **The quote lists no items.** It reads "I've told you how the test works. I want you to answer those questions as best you can."
- **No relay source is given.** The PR body says only that the scope "is added right after" X4's "not signed". Neither the body nor any file says who relayed the scope, or when.
- **It reads as David's.** Placed inside the parenthesis that attributes the quote to David ("given directly to the Physics Lead in chat and relayed here, not signed; scope as relayed: ..."), "scope as relayed" reads as part of David's relayed message rather than as the Physics Lead's account of its scope.
- **Confirmation is pending.** As this review reported at `b3a9091` (§3), the record does not show which questions the delegation covers. F-M1 (#264 FD6: "F-M1 itself stays David's call") and Zeno FD1/FD2 (#259 items) are the ones in question. As of this addendum, David's confirmation that they are covered is pending.
- **S1 (required)** marks the scope as the Physics Lead's relay, not David's words, and records that confirmation is pending.

### Text, counts and guardrails

- **David's L3 text:** byte-identical. From `## The question` through the "Genuine emergence" quote, and the whole Substitution-test text including the conjecture, it is unchanged against main (substring and prefix checks).
- **Word changes against main** (`str.split`, whole file): all match the claims.

  | File | Against main | Within this commit |
  |---|---|---|
  | litmus | +473 | +99 |
  | substitution | +175 | +41 |
  | brief | +35 | +24 |
  | readiness | +51 | +23 |

- **New tokens:** the claim that #263 and #264 in the brief are the only new label tokens is incomplete, though every new token is a label or a date:
  - brief: #263 (×2), #264, 2026-10-11, and FD3/LT3's "3";
  - litmus: 2026-10-11 (X6), and the 2 and 7 of "FD2–FD7";
  - readiness: 2026-10-11, §1.2 and l.56 (X5).
  No number is removed.
- **Guardrails:**
  - No forbidden token is added; the readiness "cartoon" is unchanged.
  - No Born, $|a|^2$ or 1/N result; no Everett-vs-Deutsch–Wallace framing.
  - Paper 1 and v0.9.1 are untouched by this commit.
  - Every new "signed" is "not signed".

### String

The OLD occurs once at `b2cf06b`. Applied by script: litmus 3,364 → 3,394 words.

**S1** (required), `notes/born-litmus-test.md`, Labels line:

OLD:
```
given directly to the Physics Lead in chat and relayed here, not signed; scope as relayed: LT sorts, FD2–FD7, F-M1, Zeno FD1/FD2; the exchange is not recorded in this repository)
```
NEW:
```
given directly to the Physics Lead in chat and relayed here, not signed; the exchange is not recorded in this repository; the items it covers are as the Physics Lead relays the delegation's scope, not David's words and not listed in the quote: LT sorts, FD2–FD7, F-M1, Zeno FD1/FD2; David's confirmation that F-M1 and Zeno FD1/FD2 are covered is pending)
```
