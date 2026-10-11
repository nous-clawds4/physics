# Geometry check: Lead rulings recorded in #283 (consistency and math)

**Verdict: HOLD (text only), on two stale pointers in `notes/m1-m2-decision-brief.md` (R1, R2).** Findings 1–4 are otherwise consistent, and every script check passes. One gap in the recorded FD4 ruling is given as a **proposal for the Lead** (P1, P2). It is not required, because these are the Lead's rulings and are not for Geometry to decide.

## Commit read

- PR #283 head **`b3a9091`**, a fast-forward of `89371eb`, against main `4d1fb11`. Two commits:
  - `89371eb`: 8 files.
  - `b3a9091`: "FD4 fail reading governs (pass sentence, [PJ] pointer); brief heading citation". This touches the litmus note, the substitution note and `m1-m2-decision-brief.md`.
- #274 is merged, at 2026-10-11 09:54 ET, so the Zeno note's $z>0$ scoping is on main.
- Script: `/workspace/g283/chk.py` (sha256 `646ed7722a7c65fd…`): section byte-identity, the §2 substitution, numeric-token multisets for all 9 files, and word counts. Also `diff`/`--word-diff` on both commits, and a whole-tree `rg` at `b3a9091` for stale markers.

## Script checks

| Check | Result |
|---|---|
| v0.9.1 Appendix A | byte-identical |
| Circularity sentence | its line is byte-identical (1 occurrence) |
| v0.9.1 §2 | identical to main once `not a route taken.` is replaced by `not a route taken; what a Born-type claim through it would have to show is scoped in \`notes/merw-litmus-scoping.md\`.`, so only the hazard sentence changes |
| v0.9.1 §3–§8, §10, §11 | byte-identical (so §11's two "MERW hazard" mentions are unchanged) |
| v0.9.1 words | 20,064 → 20,196, and 15,828 → 15,960 before Appendix A: **+132** both ways |
| Numbers | no value number changed in any file. All added tokens are labels, dates or times (2026, 12:34, 10:33, P14, #264, #279, (M2), §9, §12, 0.9.1). The litmus note's `0.9` and `6` each drop by one, which is the removed "readiness v0.9 refresh, gap 6" pointer; both tokens remain in the file |
| David's L3 text (litmus note) | lines 1–4 and 7–41 are byte-identical to main (title, "The question", the working answer, "Scope and outcomes", "Pre-emptive use", "Purpose", "Genuine emergence", and "Substitution test" with the conjecture). Line 5, the Labels line, is not David's text |
| Other word deltas | litmus note +374, substitution note +134, brief +11 (these include `b3a9091`'s additions); the rest are as in the PR body |
| Born / \|a\| / 1/N in v0.9.1 | 21→25 / 4 / 3. The four new "Born" are "Born-type claim" in the F-M1 clause; none is a claim |

## (1) F-M1 clause: consistent

- **The five places agree.** §2 (the hazard sentence only), §9 (a new sentence after the bold hazard sentence), the §12 MERW row, readiness l.56 and the gap 6 row all carry the same clause, verbatim. The P14 line describes exactly these changes. The changelog lead's "no physics claim, pin or number added" holds.
- **It agrees with the MERW note.** The clause scopes what a claim "would have to show". It does not say that a $\psi^2$ density exists on the worked rule. That fits R1:
  - at $c=0.01$, eigenvalue 1 has algebraic multiplicity 29,119 and geometric multiplicity 14,478;
  - every left–right Perron product vanishes, so MERW's density is undefined there;
  - nonnegative Perron and walk-count vectors cannot cancel (LT1 row).
- **It agrees with C36.** C36 is a finite-graph example ($P_4$, $K_{2,3}$). The clause adds no number and no instance claim.
- **§11's two (M2) "MERW hazard" mentions are fine as they are.** "The MERW hazard of §9" and the call row's "MERW hazard" still point at §9 text that keeps the word "hazard", and §9 now carries the clause. F-M1 itself raised this issue only for option (iii). P14 names them as unchanged.
- **The §2 change stays inside the firewall's protected text** (script above). The added clause is conditional ("would have to show") and makes no claim, so the firewall's "makes no Born claim" stands.
- **A pre-existing imprecision, optional (O2):** readiness l.56 says "path counting yields a squared-eigenvector density". By the MERW note §(a) and R1, that holds for a symmetric operator. A directed graph gives $\psi^{\rm L}\psi^{\rm R}$, and the worked rule gives none.

## (2) FD4 / T-a: the "both" tension is resolved at `b3a9091`; one gap remains (proposal)

- **At `89371eb` it was a real inconsistency, not a matter of reading.** S3 makes motivation and restatement two separate judgements, and its "both" cell is non-empty by definition. On that cell the "iff … restated" sentence gave FAIL, while "breaks only independently motivated items … pass" gave PASS.
- **At `b3a9091` the two sentences are consistent.** The pass sentence ("items that are independently motivated and none of which restates the target rule on any sub-case") now implies the iff sentence's non-failure condition. The "both" cell fails under both sentences.
  - The "neither" cell (not motivated, not a restatement, not tuned) is not a failure under the iff, and the pass sentence does not cover it. That is not a contradiction, since the pass sentence is sufficient, not necessary, and is scoped "on this point".
- **The T-a marker now points to the FD4 ruling, and it is accurate.** It says "Restating $W$ on a sub-case is a fail", which matches T-a's own "In part" definition. "Critic question 2" stays as the place where the judgement is made.
- **Remaining gap: empty S1 (a proposal for the Lead).** David's L3 text says: "If it could be slid in with nothing else changing, the rule was put in by hand, and the test fails". T-a's own "Slides in" begins "S1 is empty, or …", and the ruling quotes that in the litmus note.
  - With S1 empty, no item is restated, so the iff sentence gives "not a fail".
  - With nothing broken, the pass sentence is vacuously met.
  - So the recorded condition does not reach the case David's text names first. Note that by S1's definition (premises, lemmas or symmetries inconsistent with $W'$), a $W$ written in as a premise or lemma is itself an S1 item and fails. S1 is empty only when $D$ does not actually use $W$ anywhere it could break, which is the "slides in" case.
  - This is a real gap between the ruling and David's L3 text, not a matter of reading. P1 and P2 close it, but whether to take them is the Lead's call.

## (3) Per-LT sort and FD3: consistent

- **The sort follows from David's FD1 ruling** ("This litmus test is designed to detect cheating and that's it"; a pass means no cheating detected):
  - LT2 is the cheating signal;
  - LT1, LT3 and LT4 are completeness or emergence gaps;
  - anything they show was put in to match is routed to LT2 or the substitution test.
- **LT2's "not yet fixed" case matches "Pre-emptive use".** A NO there "cannot pass either, since no claim has yet been made", which is "It cannot pass a claim that has not been made".
- **FD3 matches its own analysis.** "LT3 is on the emergence side, so it does not affect the cheating verdict" fits the sort. "Not yet well defined, to be defined when a Born-type claim is made" fits the analysis bullet's "'Irrelevant' is not defined" and readiness gap 5. LT3's wording is not restated.
- **FD2's gloss is consistent too.** It widens LT2's inputs without editing David's sentence, and the "Where it connects" exception matches it.
- **No Born claim.** There is no Born, $|a|^2$ or $1/N$ claim. "|psi|^2" appears only as an example of an inserted square.

## (4) Zeno FD1 and FD2 Resolution lines: consistent, and no v0.9.1 edit is needed

- **FD1, option (i).** v0.9.1 §8.2 item 8 reads "A history whose branch points accumulate at finite accumulated $\tau$ … ends there". C5's chains (infinitely many branch points at one accumulated $\tau$) fall under it literally, so leaving it as written is consistent with C5's row ("clause (2) fails per history").
  - The Zeno note's pointer is placed after "(Z-ix) does not reach T1 through C5", and the note already gives option (i)'s consequence: "C5's chains are Zeno histories by item 8 and (Z-ix) applies to them".
  - This is consistent with the $z>0$ scoping from #274. The chains carry total mass 0 (the note's own $(2/3)^{n+1}$ bound), so $z=0$ on the instance and no $z>0$ clause is triggered.
- **FD2, option (i).** Readiness gap 4 is unchanged. Of the readiness file, only l.56 and the gap 6 row differ from main.

## Stale pointers

- `notes/m1-m2-decision-brief.md` line 20: **fixed at `b3a9091`.** The quoted heading matches litmus l.46 verbatim. It cites "LT3 bullet", but the section now has two LT3 bullets, *LT3 (#264 FD3)* and the *LT3.* analysis bullet, so O1 is an optional fix to disambiguate.
- `notes/m1-m2-decision-brief.md` line 38: **stale, twice** (R1, R2). It still reads "(litmus note, Outcome mapping, LT3 bullet; Lead's draft, pending David)". The litmus Status now says "the analysis bullets from *Outcomes* on are the Lead's reasoning from #263, not rulings".
- `notes/m1-m2-decision-brief.md` line 45: "A pick does not answer FD3." This is still true, but FD3 is now ruled (O3, optional).
- The "pending David" hits in `reviews/*` (#264 and #259 pressure tests, the Literature records, #266/#269 reviews) are historical records. The PR body lists them, and leaving them is fine.

## Fixes (each OLD occurs exactly once at `b3a9091` in the file named)

### Required

**R1** (`notes/m1-m2-decision-brief.md`, l.38, first cell)
- OLD: `a same-vertex split moves (M1) as it moves (M2) (litmus note, Outcome mapping, LT3 bullet; Lead's draft, pending David)`
- NEW: `a same-vertex split moves (M1) as it moves (M2) (litmus note, Outcome mapping, *LT3.* analysis bullet; the Lead's reasoning from #263, not a ruling)`

**R2** (`notes/m1-m2-decision-brief.md`, l.38, second cell)
- OLD: `asymptotic sibling balance (C15) (litmus note, Outcome mapping, LT3 bullet; Lead's draft, pending David)`
- NEW: `asymptotic sibling balance (C15) (litmus note, Outcome mapping, *LT3.* analysis bullet; the Lead's reasoning from #263, not a ruling)`

### Proposals for the Lead (FD4 is a Lead ruling; not required, not decided here)

Apply both in **each** of `notes/born-litmus-test.md` and `notes/substitution-test-scoping.md`. Each OLD occurs once per file.

**P1**
- OLD: `The test fails if and only if some item broken by the swap (S1) is,`
- NEW: `The test fails if and only if S1 is empty (the rule slides in with nothing else changing) or some item broken by the swap (S1) is,`

**P2**
- OLD: `If the swap breaks only items that are independently motivated`
- NEW: `If the swap breaks at least one item, and only items that are independently motivated`

### Optional

**O1** (`notes/m1-m2-decision-brief.md`, l.20)
- OLD: `per-LT sort Lead ruling (2026-10-11, delegated))", LT3 bullet;`
- NEW: `per-LT sort Lead ruling (2026-10-11, delegated))", *LT3.* analysis bullet;`

**O2** (`reviews/born-rule-readiness.md`, l.56)
- OLD: `path counting yields a squared-eigenvector density a referee may read as Born`
- NEW: `path counting on a finite connected undirected graph yields a squared-eigenvector density a referee may read as Born`

**O3** (`notes/m1-m2-decision-brief.md`, l.45)
- OLD: `A pick does not answer FD3.`
- NEW: `A pick does not answer FD3, which is now a Lead ruling (2026-10-11, delegated; litmus note, *LT3 (#264 FD3)*).`

None of these fixes changes a number, David's L3 text, v0.9.1 or Appendix A.
