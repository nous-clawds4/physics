# Literature pass: creative batch 19 (world-dependent handle gluings; L70–L74), PR #396

Reviewer: Literature agent. PR head recorded: `c78fe65`, stacked on #393 (head `43fd7ed`). Do not merge. Marks: **V-text** = wording read by us; **V-meta** = bibliographic data verified (Crossref or index), content from the standard account.

## Verdict

**Passes with must-fixes M1–M5.**

Errors:
- Set 2 puts Misner space's Taub region in the wrong wedge. $\{X^2>T^2\}$ is the boost-orbit (CTC) region; the Taub region is $\{T^2>X^2\}$.
- Set 2 also misplaces the Cauchy horizon ($T=0$).
- The status line attributes a Lead ruling to David.
- #393 presents the 3:43 PM link as if it were David's wording.

Missing:
- The chronology-protection caveats for MTY.

## 1. David's words

- **11:42 PM:** the quote is identical in `charter.md` and `ledger.md`, labelled "relayed by Physics Lead, Physics Lead chat, not signed; verbatim". **Flag:** we have no original, so it is unverified by us.
- **Error (M1):** `batch-19.md`'s status line lists, under "David's rulings … including 11:42 PM", the statements "a fork is the discovery of which world one is in, and the main line stays geon/handle hosts".
  - The 11:42 PM text asks questions ("Are we so eager to abandon our previous line of thought?") and equates fork and discovery.
  - `ledger.md` correctly records "the main line stays geon/handle hosts" as **Lead rulings**, not David's.
- **3:43 PM link (#393 at 43fd7ed, batch-18 For-David catch 1):** "This is the "which handle structure are we in" idea you had at 3:43 PM". The inner quotation marks make it read as David's words. Physics Lead confirms it is accurate only as a paraphrase, so it must say so (M2).
  - Batch 19 does not use the 3:43 PM link.
  - It cites "your 3:19 PM and 11:42 PM point" without quotation marks, so it reads as a paraphrase. I cannot verify 3:19 PM against an original. Flag.

## 2. MTY and chronology protection (Set 1, weak point 4)

- **Morris, Thorne & Yurtsever, PRL 61 (1988) 1446 (V-text abstract per #386):** a wormhole "can be converted into a time machine". The threshold "$T$ > outside light time" is the standard account (V-meta). The batch's use is correct.
- **Frolov & Novikov, PRD 42 (1990) 1057 (V-text abstract per #386):** generic interaction "almost inevitably transforms it into a time machine". Weak point 4 uses this correctly.
- **Missing caveats:**
  - **Chronology horizon.** As the shift $T$ grows past the threshold, CTCs appear first at a compactly generated chronology (Cauchy) horizon. A time-shift gluing with $T$ above threshold therefore puts the observer's world behind a chronology horizon, not merely "with CTCs".
  - **Kim & Thorne, "Do vacuum fluctuations prevent the creation of closed timelike curves?", PRD 43 (1991) 3929 (V-meta, Crossref):** renormalized stress-energy diverges at the chronology horizon of a wormhole time machine.
  - **Hawking, "Chronology protection conjecture", PRD 46 (1992) 603 (V-meta, Crossref):** the conjecture that physics, through back-reaction of vacuum polarization, prevents CTCs from forming. It is quantum and a conjecture, so it does not bind the classical model. It should still be cited as the standard caveat (M5).
- **CTCs stay exploration only;** the batch says so, and no CTC pick is made.

## 3. Misner (Set 2): apply #371

- **Misner 1967** ("Taub–NUT space as a counterexample to almost anything", in *Relativity Theory and Astrophysics I*, Lect. Appl. Math. 8, 160) is V-meta only, so it stays "unchecked". Hawking–Ellis §5.8 is V-meta per #377.
- **Error (M3).** In 2D Minkowski with the boost $B_\beta$:
  - The boost orbits in the wedges $|X|>|T|$ are timelike hyperbolae, so the quotient of $\{X^2>T^2\}$ contains CTCs. That is the non-Taub (Misner/NUT-like) region.
  - The globally hyperbolic Taub-like region is the Milne wedge $\{T^2>X^2\}$, with closed spacelike circles of length $\beta t$, $t=\sqrt{T^2-X^2}$.
  - The Cauchy horizon is the light cone $T=\pm X$ (i.e. $t\to0$), not "$T=0$".
  - For the horizon to lie ahead of a co-moving observer, take the past (contracting) wedge $T<-|X|$.
- **Read-out (sketch) [A].** In the Milne wedge, comoving separation $\beta$ means a photon emitted at $t_e$ reaches the image observer at $t_r=t_e e^{\mp\beta}$ (contracting / expanding). So the Doppler factor is $e^{\pm\beta}$, and the delay is $|t_r-t_e|$, proportional to $t_e$. The batch's "delay and Doppler $e^{\pm\beta}$" is consistent once the region is fixed (M4).
- **#371 corrections:**
  - In each Hausdorff extension, geodesics of the crossing sign are complete there, and those of the other sign are incomplete and imprisoned/spiralling.
  - Only the fixed-point geodesics are incomplete in every extension and every union. The union of the two extensions is not complete (Rieger 2402.09312 Prop 6.4, per #371).
  - The batch's "Survival is fixed per extension (#367, #375), and the ledger state β is the same in both extensions" is consistent and makes no "all end" claim. Note: a co-moving observer at the read-out crosses only if its geodesic has the crossing sign; otherwise it is imprisoned in that extension. The read-out happens before the horizon, so this does not affect it.

## 4. Twist gluings and the exactness claim

- **Prior art:** no prior art is used or cited for rotation or boost gluings of a one-universe handle, and I verified none. The idea that twisted identifications of a flat quotient are distinct worlds is standard for the platycosms (Conway–Rossetti, math/0311476, V-text per #395). Note: cite it for the flat case.
- **"A static, axially symmetric, analytic, two-mouth, one-universe wormhole solution is not known to us (unchecked)":** acceptable as stated. I verified no counterexample.
- **Thin shells are not analytic, so they are outside the lock:** correct (Visser NPB 328, V-text abstract per #386: a stress-energy layer on the junction).

## 5. Carry-overs

- **Tipler/Borde/Geroch (#395):** applied. "no topology change for reasonable sources in a CTC-free, time-orientable host; per #380" matches #395 M3.
- **Persistence G3 as re-readability (#390/#391):** consistent.
- **Misner same-extension (#383/#388):** consistent.
- **Simpson–Visser, the per-passage vs per-period trace, Dent et al.:** not restated, so no error.

## Must-fixes (each OLD occurs once at the stated head)

M1. `notes/creative/batch-19.md` (c78fe65)
- OLD: `including 11:42 PM: a fork is the discovery of which world one is in, and the main line stays geon/handle hosts.`
- NEW: `including 11:42 PM (in which David equates a fork with a discovery: "In my mind, a fork and a discovery are the same thing."), and the Lead rulings that followed (ledger: a fork is the discovery of which world one is in; the main line stays geon/handle hosts).`

M2. `notes/creative/batch-18.md` (#393, 43fd7ed)
- OLD: `This is the "which handle structure are we in" idea you had at 3:43 PM`
- NEW: `This is, in paraphrase (not your words), the "which handle structure are we in" idea from your 3:43 PM message`

M3. `notes/creative/batch-19.md` (c78fe65)
- OLD: `The Taub region of 2D Misner space is $\{X^2>T^2,\ T>0\}/\langle B_\beta\rangle$`
- NEW: `The Taub region of 2D Misner space is the Milne wedge $\{T<-|X|\}/\langle B_\beta\rangle$ (closed spacelike circles; the wedges $X^2>T^2$ contain the boost orbits, which are timelike, so their quotient has CTCs)`

M4. `notes/creative/batch-19.md` (c78fe65)
- OLD: `before the Cauchy horizon $T=0$ is reached from the past`
- NEW: `before the Cauchy horizon $T=-|X|$ (Milne time $t\to0$) is reached`

M5. `notes/creative/batch-19.md` (c78fe65)
- OLD: `So the CTC-free regime is non-generic.`
- NEW: `So the CTC-free regime is non-generic. Above threshold, CTCs first appear at a compactly generated chronology horizon, where renormalized vacuum stress-energy diverges (Kim–Thorne, PRD 43 (1991) 3929); Hawking's chronology protection conjecture (PRD 46 (1992) 603) is quantum and does not bind this classical model, but it is the standard caveat.`

## Guardrails
- No forbidden Greek letter in the batch or in this file.
- **CTCs only as exploration.** The batch labels the time-shift and Misner beyond-horizon CTCs as exploration only. The read-outs use no CTC. M5 adds caveats, not a pick.
- No CTC pick; no topology pick. Gluings are examples, and a continuum is admitted (weak point 1).
- **No count or measure.** Branches are record classes that refine and nest. There is no 1/N, no Born rule and no weights.
- No M1/M2 pick; (M1) stays at L3. No T-option pick.
- No Everett framing.
- Paper 1 untouched; nothing goes into `versions/` or `papers/`.
- David's words are labelled relayed by Physics Lead, not signed. Ruling attribution is fixed by M1.
- No geon ruling. Misner is "a model of the geon's time-loop region, not a Hadley geon".

## Rows
- **L70:** live (conditional on a host). Add M5.
- **L71:** live after M3/M4.
- **L72:** live.
- **L73:** parked; consistent.
- **L74:** live.
