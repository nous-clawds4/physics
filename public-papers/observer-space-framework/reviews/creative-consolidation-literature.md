# Literature pass: measurement model v0 consolidation, PR #372

Reviewer: Literature agent. PR head re-checked: `07d8912` (base `creative/batch-13`). File: `notes/creative/measurement-model-v0.md`. Do not merge. This is a check of citation status, prior-art fairness and the rulings table against #362, #365, #368 and #371 and the records. No new physics was claimed, and none was checked.

## 1. Citation status and corrections carried

| Item | Required (source) | In the note | OK? |
|---|---|---|---|
| Hadley 1997: CTCs essential | V-text, #362 S3 | §2.2 "contains CTCs (Hadley 1997, V-text per #362)" | yes |
| Time-orientability global, Hadley 2000 only | #362 S2 | Not restated. Type O/F (§2.3) uses $w_1$, consistent with it | yes (implicit) |
| EKT: infinitely many solutions | V-text abstract, #365 S2 | §4.3 | yes |
| Uniqueness for linear fields is Friedman–Morris | V-meta, #365 S1 | §4.5 "Friedman & Morris (1991, 1997; #365)" | yes |
| Symmetry gives a continuum only for symmetric data; jinn | #368 S3 | §4.3 | yes |
| Chruściel–Isenberg is V-meta (abstract only) | #332, #368 S2 | §2.5 "the extensions are non-isometric (**verified**, #332)" | **no (S1)** |
| Taub–NUT imprisonment is extension-relative | #371 S1–S4 | §2.5 | yes |
| Eternal geon host: no Cauchy surface | #371 S5 | §2.8 | yes |
| Misner dichotomy | computed (#367; recomputed in #368) | §2.5 "not a verified source" | acceptable (a computation, not a citation) |
| Taub–NUT sign dichotomy | V-meta, "correct" per #371 | §2.5 and §4.6 "unverified" | acceptable but conservative. #371 found it correct at V-meta |

**S1.** #332 marked Chruściel–Isenberg V-meta (abstract only; the full text was unreachable). The abstract says "many of the familiar extensions are isometric". Non-isometric maximal extensions exist in the Taub family, but "the extensions are non-isometric (verified)" claims both too much and the wrong status.

## 2. Prior-art fairness

- **Fair overall:**
  - Hadley 1997 is named as the closest prior art for the round trip (§2.2).
  - Belnap 1992 is named for outcomes as classes of histories (§2.6, §4.12).
  - Hájíček, McCabe, Earman, Placek–Belnap and Müller are listed (§4.12).
  - Everett appears only as a framing *hazard* (§4.11; #332 N1, Sebens–Carroll per #350), not as a frame. Correct.
- **One unfair compression (S2).** The plain-language section names Belnap 1992 as "the nearest earlier idea" overall. For the measurement model itself, the nearest is Hadley 1997 (#365). Belnap is nearest only for the outcome-as-class-of-branches part.

## 3. Rulings table (14 rows)

I checked each quote and attribution programmatically against `notes/creative/ledger.md` and `charter.md` at 07d8912, with the M1 row checked against v0.10.1.
- **13 dated 2026-10-12 rows (3:14–4:28 PM): exact match**, quote and attribution both. That includes:
  - 3:28 PM and 3:30 PM: the ledger section header carries no time, but the ledger's bullets give 3:28 and 3:30 PM;
  - 3:43 PM and 3:47 PM, the counting words;
  - 4:06 PM, "I don’t recall ruling out geons";
  - 4:16 PM, which matches the known record: "Yes, allow CTCs and non-time-orientability in geon hosts, as exploration only.";
  - 4:28 PM, both sentences.
- **L3 row:** the quote and the attribution "Ruled (M1) by David, 2026-10-10, at L3; relayed, not signed" match `versions/v0.10.1-prose.md` §11 (origin/main, line 485, V-text). They also match the #266 brief's hold text (11:46 PM ET; the ruling itself is 11:45 PM).
- All rows are relayed, and none is signed. (M1) stays at L3.
- No geon ruling is claimed: the 4:06 row says only that David does not recall ruling geons out.
- I cannot check primary chat records beyond these repo records, except the 4:16 PM text supplied as known.

## 4. Strings (`notes/creative/measurement-model-v0.md`; each OLD occurs once at 07d8912)

S1
- OLD: `the extensions are non-isometric (verified, #332)`
- NEW: `non-isometric maximal extensions exist (Chruściel–Isenberg 1993, V-meta, abstract only, per #332/#368; the abstract also notes many familiar extensions are isometric)`

S2
- OLD: `The nearest earlier idea in the literature is Belnap's 1992 branching picture.`
- NEW: `The nearest earlier ideas in the literature are Hadley's 1997 4-geon causal link between apparatus and preparation (for the measurement) and Belnap's 1992 branching picture (for outcomes as classes of branches).`

## Guardrails
- No forbidden symbol (none in this file or in the note).
- No Born/$|a|^2$/$1/N$ result. The 3:47 quote mentions Born only as David's verbatim words, and counting stays a labelled conjecture.
- Everett appears as a hazard or prior art only.
- No pick among M1/M2/T-options or on CTCs.
- Paper 1 untouched.

## Verdict
**PASS with two strings.**
- The corrections from #362, #365, #368 and #371 are carried, except Chruściel–Isenberg's status (S1).
- Prior art is fair except one plain-language compression (S2).
- The rulings table is verbatim against the ledger, charter and v0.10.1 in all 14 rows.
