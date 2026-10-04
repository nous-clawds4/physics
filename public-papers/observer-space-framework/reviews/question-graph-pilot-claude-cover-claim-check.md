# Literature claim check: Claude exploratory-critique cover for the question-graph pilot (#218, queue 008)

Reviewer: Literature (non-author; did the #199 citation check, #202)
Date: 2026-10-04
**Read:** #218 at **`3a61a866b13a1639dd15f7e0b36ba30ca9383289`** (branch `lead/qgraph-claude-cover`), confirmed unchanged before filing. Target: `public-papers/observer-space-framework/reviews/question-graph-pilot-claude-cover.md`, the PR's only file. Checked against `main` at `654867b`.
**Verdict: PASS.** Every factual claim checks out. One wording clarification is recommended (C1). Three changes are optional (C2 in the cover; C3 and C4 in the queue draft).

---

## Findings

1. **Length: exact.** The cover is 776 words by Python `str.split` (whole file).
2. **Node counts: exact.** `question-graph/` on `main` has 9 `q-*` and 21 `a-*` files: 7 accepted, 9 rejected and 5 open answers, 30 nodes in all. It has six version files, `v0.3`, `v0.4`, `v0.5`, `v0.6`, `v0.7` and `v0.7.1`. The five open nodes named in question 4 are exactly the five open answers.
3. **PR numbers and SHAs: exact.**
   - #199 merged as `33c06d2`.
   - #200 is "Geometry: math and selection check", with verdict "PASS with fixes".
   - #202 is ours, HOLD (narrow).
   - #206 merged as `83ff2d6`; it is the only later commit touching the folder.
   - #200 and #202 merged at 6:31 PM ET on 30 Sep, before #199 merged at 6:35 PM ET.
4. **#202 fixes: all landed.** All 18 of our NEW strings (14 required, 4 optional) are present in `33c06d2` and on `main`, and no OLD string remains. #200's hold-cap fix is also in: `q-observer-object` is at L1 "proposal, pending David's signature". "All fixes applied before merge" holds.
5. **#206 description: accurate.** #206 brings `a-real-a` and `a-real-b` into line with the instance-scoped Kretschmann (a) wording of #201 R1, as extended by #203.
6. **"Written … after" the checks: imprecise.** #200 and #202 checked the written pilot (#199 at `4e6d078`). #199's body says it was "Released by Lead after Geometry #200 … and Literature #202 …, both folded in". So the pilot was *merged* after the checks, not written after them. See C1.
7. **The two items waiting for David: pending, and attributed correctly.**
   - `q-observer-object` at L1 is a proposal pending David (#200 H1; the node's own comment; the `index.md` Holds line).
   - For Option F, `a-option-f`'s "Record unclear" says #104 records David's adoption. The demotion was recommended by Geometry (#118) and made in the v0.5 outline (#119), and no David signature was found. The cover calls it a retroactive sign-off that waits for David, not a decision.
   - No record names it as a queued request to David. "Already wait for David" is a fair reading of the node, not a cited request. C2 (optional) puts the record into the parenthesis.
8. **The rest of the folder description: accurate.**
   - Every hold level above L3 ("weakly held") is a proposal.
   - `index.md` has the method, rating scale, node table, selections, "Rejected options by layer" and "Gaps and unclear record".
   - It links the infinite-harness doc and the viewer format.
   - It records the two structural rating effects named under Out of bounds.
9. **Later-record pointers: exact.**
   - #183 is v0.8 prose (`79a8271`).
   - #205 is v0.8.1 prose (`0155b50`).
   - #213 adopts v0.8.1 as current, merged as `db26820`; the README names `versions/v0.8.1-prose.md` as the current draft.
   - `reviews/law-of-R-scoping.md` exists. #178 created it, #187 is v2, and #204 (the Geometry #203 L1/L2 instance scope) edits only that file.
10. **Filing instructions: workable.** `reviews/question-graph-pilot-claude-opus-5.5.md` is free on `main`. The cover's guardrails are clean:
    - no excluded words;
    - no picks;
    - no Born, |a|² or 1/N;
    - no Everett-vs-Deutsch–Wallace framing;
    - Bell is not mentioned;
    - Paper 1 is out of bounds for edits.
11. **Queue draft (`/workspace/q008-draft.txt`, 2,743 bytes, read only): consistent with the cover.**
    - It frames an exploratory critique with no verdict, uses the same target, PR numbers, filing path, header and PR title, and binds Claude to the cover's Out of bounds list.
    - It has no excluded words or picks, no Born, |a|² or 1/N, no Everett framing, and no claim about Bell.
    - It says "the paper" where the cover says "the paper versions, the essays, Paper 1" (C3, optional).
    - It omits the cover's "no Einstein-equation claim" (C4, optional; the cover already binds this).
12. **"Do not merge" and the merge gate.**
    - Both the cover and the draft tell Claude "Do not merge it."
    - The `merge-gate` check fails only when a PR's title or body contains a hold phrase, or the PR has the `hold` label.
    - The PR title the cover prescribes has no hold phrase. So Claude's PR passes the gate unless its body happens to repeat the instruction.
    - If the critique must stay unmerged until it has been read and pressure-tested, the Lead should add the `hold` label when the PR arrives. The instruction to Claude does not gate anything.
13. **Main since #199: no effect on the cover's claims.** Main has moved through #200–#216. The only change to the folder is #206, which the cover names.

## Corrections (OLD → NEW; each OLD occurs exactly once in the named file)

**C1 (cover; recommended: written versus merged).** OLD:
```text
It was written by Ontology (#199, merged `33c06d2`) after Geometry's math and selection check
```
NEW:
```text
It was written by Ontology (#199) and merged as `33c06d2` after Geometry's math and selection check
```

**C2 (cover; optional: state the record for the Option F item).** OLD:
```text
a retroactive sign-off on the Option F demotion (`a-option-f`, "Record unclear").
```
NEW:
```text
a retroactive sign-off on the Option F demotion (`a-option-f`, "Record unclear": David adopted F in #104; the demotion was recommended by Geometry in #118 and made in the v0.5 outline, #119, with no David signature found).
```

**C3 (queue draft `/workspace/q008-draft.txt`; optional: name Paper 1).** OLD:
```text
Do not edit the question graph, the cover, the paper, the essays, or any other file.
```
NEW:
```text
Do not edit the question graph, the cover, the paper versions, Paper 1 (papers/observer-space-ontology.md), the essays, or any other file.
```

**C4 (queue draft; optional: match the cover's Out of bounds list).** OLD:
```text
Do not use the Born rule, |a|^2 or 1/N.
```
NEW:
```text
Do not use the Born rule, |a|^2 or 1/N, and make no Einstein-equation claim.
```

## Report line

Literature: **PASS** on the question-graph Claude cover, #218 at `3a61a86`.
- The length (776 words), node counts (9 + 21 = 30; 7 / 9 / 5; six versions), PR numbers and SHAs (#199 `33c06d2`, #200, #202, #206, #183, #205, #213 `db26820`, #178/#187/#204) and the descriptions of #200, #202 and #206 are exact.
- All 18 #202 fixes are on `main`.
- The two items for David are stated as pending and attributed correctly.
- The draft is consistent and carries "Do not merge it". The gate needs the `hold` label on Claude's PR if it must stay unmerged.
- Recommended: C1. Optional: C2 to C4.
