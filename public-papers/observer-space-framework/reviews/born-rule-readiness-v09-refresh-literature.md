# Literature check: born-rule-readiness v0.9 refresh (#246)

**Verdict: HOLD (narrow).** Two strings are required: gap 4's Zeno costs are one-sided, and gap 3's "harmless" overstates C37. Two more are recommended. Everything else checks. **Heads read:** #246 head `430a8b9` (`reviews/born-rule-readiness.md`); base and main `b327a7b` (`versions/v0.9-prose.md`, `notes/zeno-mass-scoping.md` with #245's strings 1–4 merged). I re-checked the head before filing.

## Findings

- **F1 (append only): PASS.** The file at `b327a7b` is a byte prefix of the file at `430a8b9` (17,645 bytes, then 24,334). The appended section is 1,081 words by `str.split`, as claimed. No other file is touched, and Paper 1 is unchanged.
- **F2 (C-rows and pointers): PASS except F5 and F6.**
  - I ran `brr_check.py` (SHA-256 `e95ac2a6…73d1`, as pinned) on my own copies at `b327a7b`: 0 failures.
  - I also checked independently:
    - Rows C5, C6, C12–C14, C16, C17, C26, C28–C30, C33, C34, C36 and C37.
    - The §8.2 items: item 1 constrains R's sources, item 7 is (A), and item 8 is no-Zeno, with its range in §8.3.
    - §8.3's branch-point definition, §8.4's "later bar", §10, and §11's open calls ("Without being fully deterministic", T1–T3) and Hopes.
    - #230's F5 (Duda wording), F7 (T1, (B) scope), F9, F10 and F11 (the #203 lemma).
    - (Z-0)–(Z-v) against the merged note.
  - "Bertrand" is inherited from old-map gate 1 and does not appear in v0.9. This is acceptable as a gloss.
- **F3 (the nine stale items): PASS.** Each is stale at `b327a7b`, and l.9, 41, 46, 52, 78, 91, 97, 106, 110 and 127 all match. Item 7's figures match the scan's §1.1: 77 of 1,505,887 relabelled, 31 germs changed for $n\ge6$, and $n\le5$ unchanged. Q5's "71 of 77 at $r>10^4$" matches the scan's large-radius note. Item 10 holds: P6's 1.098432 appears as 1.0984 in C16, P9 matches C9, and P3, P7 and P8 have no v0.9 row.
- **F4 (14,477 vs 14,478): reproduced.** In a scratch venv:
  - `g154/agraph.py 0.01` (SHA-256 `edf42d6e…8f6`, `kr.classify`) prints 29,119 reachable orbits and 14,477 stuck.
  - `g168/c33r.py` (`f9e9c31b…dcd45`) reproduces the C33 law and prints 29,119 orbits and 14,478 stuck. It replaces `kr.classify` with a classifier that deflates the cubic by the known root $r_p$ at 50 digits.
  - So the one-orbit difference is a single target classified differently by the two classifiers. I did not identify which target.
  - The old P4 row already flags 14,477 as a classifier artefact, and it is #173 that set the pin to 14,478. Stale item 5 is accurate. String 3 names both scripts and credits the row's own caveat.
- **F5 (required): gap 4's cost cell is one-sided.** It quotes the note's (d) costs only for (Z-iii) and counting (Z-iv). Both are readings that do not give the per-vertex $1/2$. The costs of (Z-0)/(Z-i), (Z-ii) and (Z-v) are left out, which tilts the cell. String 1 lists every reading's cost from the merged note.
- **F6 (required): gap 3, "The throat window is harmless (C37)".** C37 says the rule needs a throat convention. Under (a) the thresholds are not reached, and without (a) the convention moves the $c=0.1$ bound fraction by about 0.1 pp. "Harmless" is too strong (string 2).
- **F7 (recommended): the heading "Gaps between v0.9 and a Born-type result".** It can read as distance to a derivation. The old map's answer is that a Born *question* cannot yet be stated. String 4 aligns the heading with that. The body does not frame closing gaps as progress. There is no Born, $|a|^2$ or $1/N$ result, and no (M1)/(M2), T, Q-D, #139 or Z pick. There is no Everett-vs-Deutsch–Wallace framing and no Bell claim. Gap 0's cost is two-sided, and "cannot be derived" matches v0.9's "not derivable (Prop. 13)".
- **F8 (Geometry's flag (a)): the word is "cartoon".** It is at old-map l.46, in the DW (b) row: "(§6 is a cartoon; matter open)". It is inherited, not new: `git blame` gives d8f35a29 (#159, 2026-09-27 PT). The refresh does not repeat it; stale item 3 only notes it. It should go, but removing it is an edit above the section, which this append-only PR should not make. It does not block #246. A follow-up one-line edit is given as F-string A below.
- **F9 (the critic questions): PASS.** All five are well-posed, answerable, unloaded and consistent with the body. Q1 asks about the gating order and does not assert progress.
- **F10 (banned words in the appended section): none.** The list checked: egalitarian, cartoon, the GRW acronym, 4-geon, spin-foam, chi, "natural", "preferred" and "best".

## OLD/NEW (file `public-papers/observer-space-framework/reviews/born-rule-readiness.md` at `430a8b9`; each OLD occurs once)

1. (required) OLD: `As in §11's symmetric cost lines, plus the note's (d) costs: (Z-iii) reads $R$ ahead; counting (Z-iv) needs a cut family and a proof that the limit exists`
   NEW: `As in §11's symmetric cost lines, plus the note's (d) cost for each reading: (Z-0)/(Z-i) need a per-state no-Zeno proof, and one measure-zero Zeno history leaves weights undefined; (Z-ii) needs an existence citation and a scoped item 8; (Z-iii) reads $R$ ahead; counting (Z-iv) needs a cut family and a proof that the limit exists; (Z-v) fixes a value once the weight type is fixed`
2. (required) OLD: `The throat window is harmless (C37)`
   NEW: `Under (a) the throat thresholds are not reached; without (a) the rule needs a throat convention (C37)`
3. (recommended) OLD: ``5. **l.78 (P4):** `agraph.py` itself prints 14,477 under `kr.classify`. The pinned 14,478 is the corrected-classifier figure (`g168/c33r.py`, `f9e9c31b`; #169, #173), which C33 now pins. The pin row names the uncorrected script.``
   NEW: ``5. **l.78 (P4):** the row names `g154/agraph.py 0.01`, which prints 14,477 stuck under `kr.classify` (the row itself flags this as a classifier artefact). The pinned 14,478 is the corrected-classifier figure (`g168/c33r.py`, `f9e9c31b`; #169, #173), which C33 now pins. Both scripts give 29,119 orbits. The pin row names only the uncorrected script.``
4. (recommended) OLD: `### Gaps between v0.9 and a Born-type result`
   NEW: `### Gaps before a Born-type question can be posed`

I applied all four mechanically. Each matches once, the pre-section bytes are unchanged, and the section goes from 1,081 to 1,150 words.

**Follow-up (out of scope for #246, separate edit) — F-string A:** OLD `(§6 is a cartoon; matter open)` → NEW `(v0.6 §6 is an informal picture, not ontology; matter open)` (once, l.46).
