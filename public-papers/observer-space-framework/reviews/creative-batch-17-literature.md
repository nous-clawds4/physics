# Literature pass: creative batch 17 (persistence; L61–L64), PR #390

Reviewer: Literature agent. PR head recorded: `172bdf6`, stacked on #385. Files: `notes/creative/batch-17.md`, `charter.md`, `ledger.md`. Do not merge. Marks: **V-text** = wording read by us (abstract or text); **V-meta** = bibliographic data verified, content from the standard account; **relayed from external review** = another reviewer's reading, not ours.

## Verdict

**Passes with must-fixes M1–M5.**
- The persistence definition and the flux existence result are sound in the test-field limit.
- Two statements overclaim irreversibility or monotonicity. A later opposite crossing restores a flux slot, so persistence is not monotone in $t'$ as defined.
- One citation is an external reviewer's reading and is presented without that label.
- One carry-over error survives in the ledger changelog.

## 1. David's 10:37 PM words

- The quote is identical, character for character, in `batch-17.md`, `charter.md` and `ledger.md`.
- It is labelled "relayed by Physics Lead, Physics Lead chat, not signed; verbatim" each time.
- It agrees in substance with Physics Lead's paraphrase:
  - some matter is a more effective ledger, some less;
  - fading records are not fatal;
  - what's needed is a clear model of what persistence means and how it happens;
  - it must happen "more than never".
- **Flag:** I have no original record of the 10:37 PM message, so I cannot verify the verbatim text beyond the paraphrase and internal consistency.

## 2. Flux existence result (Set 3, L63)

- **Misner & Wheeler, Ann. Phys. 2 (1957) 525, p. 534 (V-text per #386):** "the wormhole flux remains invariant. This constant of the motion represents the charge." The batch quotes this correctly.
  - M–W also say the flux is "unquantized" (V-text). The batch handles this through L58 and P5, so it is consistent.
- **Sorkin 1977 and Diemer–Hadley 1999 caveat (V-text abstracts per #386):** applied correctly in the Hadley-type caveat. The −q reading is credited to #387 as a sketch.
- **The passage rule $\Delta\Phi=\pm q_0$ [A]** is correct, with the Gauss surface around exactly one mouth and no charge between it and the throat.
- **However:** a later crossing of the opposite sign through the same mouth returns $r_i$ to its earlier value.
  - Set 3 says so ("unless another charge crosses that mouth").
  - The For-David summary's "nothing classical can undo that" contradicts it (M1).

## 3. Orbit decay (Set 4)

- Credited to Dent, Gabella, Holley-Bockelmann & Kephart, arXiv:2007.09135 (V-text per #383). Correct: under radiation, a bound body ends up settled on the throat.
- The grade G2 → G1 for orbit or passage records is consistent with that. The batch's "a falling body may add a stray passage" is also consistent.

## 4. P1–P6 mapping

- **P1** "Hochberg–Visser 1997 abstract, per Claude 015": we have not read this source. It must be labelled as relayed from external review (M3).
  - The content attributed to it (exotic matter at any wormhole throat, generic) is the standard account of Hochberg–Visser, PRD 56 (1997) 4745. I have not verified the bibliographic data, so I give no mark.
- **P2:** Frolov–Novikov 1990 (V-text abstract per #386). Correct: a time offset is generic once external fields are present.
- **P3:** Shinkai–Hayward 2002 (V-text per #383) is about the Ellis wormhole: a normal-matter body crossing the throat triggers collapse.
  - The "thin shells unknown" hedge is correct.
  - Visser NPB 328 (1989) (V-text abstract per #386) has only a partial stability analysis, which constrains the shell's equation of state. Note.
- **P4–P6:** these are the batch's own reasoning, with no citations. The grade logic is fine.
- **Conclusion "no item forces G0 everywhere":** sound for the stated design (isolated flux slots, no stray charge, test-field limit).

## 5. Set 1 and Set 2 internal logic

- **The monotonicity claim (Set 1) and the non-increasing claim (Set 2) are false as defined.** "Persists to $t'$" is evaluated at the single time $t'$. A stray charge crossing mouth A at $t_1$ and another crossing back at $t_2$ makes $r_i$ wrong on $(t_1,t_2)$ but right again after $t_2$.
- **Fix:** define persistence over the whole interval, so that it holds at every $t''\in[t_i,t']$. Then monotonicity and the non-increasing profile hold by definition (M2, M4).
- The grade definitions G0–G3 need no change once persistence is interval-based.
- No measure is used, and the read-out is fixed in advance, so this is not a law of R by fiat.

## 6. Carry-overs (#380, #383, #386, #388)

- **Tipler / Borde / Geroch:** not restated in batch 17. No error.
- **Simpson–Visser:** not restated. No error.
- **Misner same-extension:** not restated. No error.
- **Trace per passage vs per period:** `ledger.md`'s changelog still records "one-period trace 2(1+L/a)" (M5, the same error as #388's must-fix).
  - $2(1+L/a)$ is per passage.
  - Over one full period of two passages the trace is $4(1+L/a)^2-2$ (14, 62, 322; #386 [A]).

## Must-fixes (each OLD occurs once at 172bdf6)

M1. `notes/creative/batch-17.md`
- OLD: `and nothing classical can undo that: radiation carries no net charge.`
- NEW: `and radiation cannot undo that, since it carries no net charge; only another charge crossing the same mouth can change it.`

M2. `notes/creative/batch-17.md`
- OLD: `Monotone: if it persists to $t'$, it persists to every earlier $t''\in[t_i,t']$, by the append-only property and continuity of the read-out (sketch).`
- NEW: `Persistence to $t'$ means the separation holds at every $t''\in[t_i,t']$ (a later opposite crossing can restore a corrupted read-out, so a single-time condition would not be monotone); with this interval definition, persistence to $t'$ implies persistence to every earlier $t''$.`

M3. `notes/creative/batch-17.md`
- OLD: `(Hochberg–Visser 1997 abstract, per Claude 015)`
- NEW: `(Hochberg–Visser 1997, relayed from external review, Claude 015; not verified by us)`

M4. `notes/creative/batch-17.md`
- OLD: `is non-increasing among already-written entries.`
- NEW: `is non-increasing among already-written entries (by the interval definition in Set 1).`

M5. `notes/creative/ledger.md`
- OLD: `one-period trace 2(1+L/a)`
- NEW: `trace 2(1+L/a) per passage, 4(1+L/a)²−2 per period`

## Guardrails
- No forbidden Greek letter in the batch or in this file.
- No Born/$|a|^2$/$1/N$ result. Fractions, rates and likelihoods are explicitly excluded, and (M1) stays at L3.
- No Everett framing.
- No pick among M1/M2/T-options or on CTCs; P2 is a loss mapping only.
- Paper 1 untouched; nothing goes into `versions/` or `papers/`.
- David's words are labelled relayed by Physics Lead, not signed.
- No geon ruling. The Hadley-type caveat is conditional.
- The read-out is fixed in advance, so there is no law of R by fiat.

## Rows
- **L61:** live, after M2.
- **L62:** live, after M4.
- **L63:** live in the test-field limit. Citations correct.
- **L64:** live, after M3.
