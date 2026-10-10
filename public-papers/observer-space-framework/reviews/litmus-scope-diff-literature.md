# Literature diff-only check: litmus scope qualifier and MERW reframe (#252)

**Verdict: HOLD (narrow).** Three strings are required:
- the qualifier names a source that cannot be found in the repository ("in this chat");
- the MERW note's Scope line points to a branch;
- the LT1 row turns "superposes, evolves linearly, interferes" into "superposes or cancels".

Three are recommended. Every number, operator, probe, option and F-M1 line is unchanged, and every #251 Burda fix survives. **Heads read:** #252 head `bc86d8c` (commits `6013d66` and `bc86d8c`); base and main `b1a62b7` (#250 merged). I re-checked the head before filing.

## Findings

- **F1 (bases): all strings present.** `b1a62b7` is the merge of #250. All six #251 strings are present verbatim in its `merw-litmus-scoping.md`, which is 1,152 words. All six are still verbatim at `bc86d8c`. The litmus note's #249 strings are untouched: the Status line marked as relayed by CoS, and the (M1)/(M2) completed-versus-cut pairing.
- **F2 (6013d66): only the stated paragraph.** It adds one paragraph, "Scope and outcomes", after LT4, plus one blank line. Nothing else changes.
  - The paragraph says David's ruling was given "in this chat". The PR body says "given directly in chat". Nothing in the repository records it, and "this chat" does not resolve in a repository file. By #249's standard it needs the relayed treatment (string L1).
  - The last sentence ("A scoping note that finds no candidate object … not that it failed") reads as an application of the ruling. If it is the Lead's wording rather than David's, it should be marked as such. That is for the Lead to say; no string is given.
  - The paragraph is consistent with the working answer: "needs YES on all four" is a necessary condition, and "success does not prove emergence" says it is not sufficient.
- **F3 (bc86d8c): the edits.** It adds the scope sentence (line 3) and changes 13 other chunks.
  - 11 rewrites: the (b) heading, the column header, the LT1–LT4 cells, the R2 and R3 bold lines, the O2 cost, Q3 and Q5.
  - 2 added sentences: one after R1's bold line, one after R4.
  - "14" matches if the LT3 cell is counted as two sentences.
  - My token script finds the same multisets of numbers, C-rows, §-pointers, R1–R4 and options (i)–(iii) before and after. O2 and O3 each gain one mention in new sentences, but no operator definition changes. The O1–O5 rows, the F-M1 line and the Costs line are byte-identical. +185 words (1,152 → 1,337).
- **F4 (substance kept, except F5 and F6).** These hard results stay verbatim:
  - "Spectral radius 1, multiplicity 29,119: no unique Perron vector, so MERW's $\psi^2$ is undefined here".
  - "the count is not stable in $L$, and its limit is set by the longest chain".
  - "winner-take-all rather than superposition".
  - "cancellation appears only once phases are supplied".
  - The "would have to" sentences are conditional and do not say X is achievable. "No rule meets it now (C26)" and "no setup exists to state this now" keep the facts. There is no pick.
- **F5 (required): the LT1 row.** "A claim would have to exhibit an object that superposes or cancels" states LT1 more weakly than David's wording, which reads "superposes, evolves linearly, interferes". It also drops the original fact that O1–O4 supply no object that superposes *or* cancels. String M2 restores both.
- **F6 (recommended): R3.** "Such a claim would be robust to the classifier" moves a computed fact about the shares onto a hypothetical claim. String M3 states the fact first.
- **F7 (required): the Scope pointer.** "on `lead/litmus-scope`" names a branch that will not outlive the merge. String M1 points instead to the litmus note's "Scope and outcomes" paragraph.
- **F8 (F-M1): unedited, with a mismatch.** F-M1 is byte-identical. Its options (ii) "whether it could pass LT1–LT4 is scoped in …" and (iii) "its status against LT1–LT4 is open" read as if the tests apply now. Under the new qualifier they apply only once a Born-type result is claimed. Whether to change this is for the Lead or David to decide. If they want wording that matches the qualifier, one neutral option set, not a pick, would be:
  - (ii′) "… add 'LT1–LT4 would apply only if a Born-type claim were made through it; see `notes/merw-litmus-scoping.md`'";
  - (iii′) "replace with 'not adopted; LT1–LT4 do not apply unless a Born-type claim is made'".
- **F9 (cross-references): one stale pointer.** The litmus note's "Where it connects" still calls `notes/merw-litmus-scoping.md` "(in preparation)" and says it scopes whether MERW "could pass LT1–LT4". That is stale after #250 and at odds with the qualifier (string L2, recommended). The merw note's Read-at line names the litmus note at `001dde2`, before the qualifier. That is acceptable once M1 points to the paragraph.
- **F10 (questions and guardrails).** Q3 and Q5 are still two-sided and well-posed. There is no Born, $|a|^2$ or $1/N$ result and no pick. The banned words are absent from both files. There is no Everett-vs-Deutsch–Wallace framing and no Bell claim. Paper 1 and `versions/` are untouched.
- **Word counts (`str.split`):**
  - `notes/born-litmus-test.md`: 356 → 454 (+98); 475 with L1 and L2 applied.
  - `notes/merw-litmus-scoping.md`: 1,152 → 1,337 (+185); 1,359 with M1–M3 applied.

## OLD/NEW (each OLD occurs once at `bc86d8c`)

File `public-papers/observer-space-framework/notes/born-litmus-test.md`:

- **L1 (required).** OLD: `(David, 2026-10-10, in this chat; part of the L3 answer)`
  NEW: `(David, 2026-10-10, given directly to the Physics Lead in chat and relayed here; the exchange is not recorded in this repository; part of the L3 answer)`
- **L2 (recommended).** OLD: ``notes/merw-litmus-scoping.md` (in preparation), which scopes whether the MERW squared-eigenvector density could pass LT1–LT4.``
  NEW: ``notes/merw-litmus-scoping.md`, which scopes what a Born-type claim through the MERW squared-eigenvector density would have to show under LT1–LT4.``

File `public-papers/observer-space-framework/notes/merw-litmus-scoping.md`:

- **M1 (required).** OLD: ``**Scope (L3's qualifier, David, on `lead/litmus-scope`):**``
  NEW: ``**Scope (David's qualifier to the L3 answer, recorded in `notes/born-litmus-test.md`, "Scope and outcomes"):**``
- **M2 (required).** OLD: `A claim would have to exhibit an object that superposes or cancels; O1–O4 supply none now (readiness §1.2)`
  NEW: `A claim would have to exhibit an object that superposes, evolves linearly and interferes; O1–O4 supply no object that superposes or cancels (readiness §1.2)`
- **M3 (recommended).** OLD: `**Such a claim would be robust to the classifier.**`
  NEW: `**The computed shares are robust to the classifier, so such a claim would be too on this point.**`

All five were applied mechanically; each matches once.
