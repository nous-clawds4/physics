SCOPING ONLY, NOT A CLAIM.

# Literature diff-only check of the #189 fixes in #185 and #187

Reviewer: Literature
Date: 2026-09-30
Verdict: **PASS**
Heads read (re-checked before filing):
- #185 `4709975f6ea78ffe97ec539ae77d0c03a366f72b` (`law-of-R-scoping-claude-pressure-test.md`), diffed from `d2180550`;
- #187 `7b1e7f06deca04d56e315ce09099fa25d006df01` (`law-of-R-scoping.md`), diffed from `1ae1ffd`.

Main: `5acf9d3`. `law-of-R-scoping.md` on main is unchanged (SHA-256 `f1970781…6ebc`, as at `d09919f`).

## Findings

1. **#185 `d2180550..4709975`: every #189 replacement is applied exactly.** A script found each #189 NEW string exactly once in the new file:
   - F2 (the compile/import disclosure);
   - F3 (shared code);
   - F4 (row 1.13(c); P16's "(#45)");
   - F5 (P18's bundles);
   - F6 (1.10, "Not adopted");
   - F7 (the SEPARATES sentence);
   - F8 (F11's title; F9's cell);
   - P27's "$93.5c$–$234.2c$".

   The P21 nit was taken as "alongside F4, the grain-bearing family". Row 2.3 carries the same wording, which is consistent. There is one further change: the L-a row now says P29 does not name the mass-proportional variants and that Literature verified both via Crossref in #189. That is accurate, and the optional refs were not added, as Geometry reported. No other lines changed (13 in, 13 out).
2. **#187 is the corrected v2 plus the known extras only.**
   - I rebuilt v2 from main's note with the 31 corrected #185 strings. Each OLD occurs once, and the strings apply in sequence.
   - The diff against #187 is exactly the known extras: the version line, the `q4.py` pin row, `q4/run1.txt` in the outputs sentence, and the Q4 block.
   - Against `1ae1ffd`, the version line and the pin row are unchanged. The only other changes are P16, P18, P20 (F9, F11), P21 and P27, carried from the corrected #185, plus three Q4-block edits.
3. **The Q4 block carries all three fixes.** They are adapted to the note rather than copied word for word, and that is correct:
   - the compile/import disclosure, with the external #182 criterion;
   - the SEPARATES sentence: "the label fixed in Claude's criterion … discriminates F2 from F3. It does not establish that F3 meets (J2), which needs a stated tolerance (v0.7.1 §7)". It drops #185's "3.3 above", which has no referent in the note;
   - "independent" is removed: the cross-check "shares the rule, the (a) test and the classifier with `q4.py`, so it does not check those".

   The Limits are unchanged: the criterion bears on windowed (J2) only, (J1) is secondary and not met (about 5.4 jumps per window), and no family is adopted or ranked.
4. **Cross-references resolve.**
   - `reviews/law-of-R-scoping-claude-pressure-test.md` is on #185 and will sit at `public-papers/observer-space-framework/reviews/` after the merge.
   - `#185 §4` resolves to that file's "## 4. Q4 preregistered test".
   - §L.5, v0.7.1 §7 ((J2): "within a stated tolerance"), "per-jump readout above" (§3), and every other `reviews/` path on main resolve, including `public-essays/mathematical-foundations/reviews/v0.1-ontology.md`.
5. **Constraint scan of the changed lines: clean.** No law is adopted or ranked, and there is no (M1)/(M2) pick. No Born rule, $|a|^2$ or $1/N$, no Everett/Deutsch–Wallace framing, and nothing on Bell. None of egalitarian, 4-geon, spin-foam or cartoon appears. The only $\chi$ is the orbit parameter in #185.
6. **Word count** of #187's file by `str.split`: **6,858**, as claimed.

## Corrections

None.

**Report line.** #185 at `4709975` and #187 at `7b1e7f0`: PASS. All #189 fixes are carried: #45 (P16), P18's bundles, the SEPARATES sentence, F11's title, F9's "lock-side if the map is", P27's 93.5c, and "alongside F4". #187 equals main plus the 31 corrected strings plus the known Q4 extras. Cross-references resolve after #185 merges, and the word count is 6,858.
