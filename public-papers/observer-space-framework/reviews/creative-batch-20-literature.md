# Literature pass: creative batch 20 (two-slit step 1; L75–L79), PR #401

Reviewer: Literature agent. PR head recorded: `3a6fdbc`, stacked on #399. Files: `notes/creative/batch-20.md`, `batch-20/cylinder.py`, `results.txt`, `charter.md`, `ledger.md`. Do not merge. Marks: **V-text** = wording read by us; **V-meta** = bibliographic data verified (Crossref), content from the standard account; **unverified** = not checked by us.

## Verdict

**Passes with one must-fix (M1).**
- The toy is correct.
- I re-ran the numbers [A]: $X=10\tan35^\circ=7.0021$; for $L=2.5$, $x=2.0021$ and $n=2$; the inverse class of $x=2.0021$ is $\{5.0\ (n=1),\ 2.5\ (n=2)\}$, since $L_3=1.667<x$.
- The script is a straight forward map with fixed inputs (θ = 35°, D = 10, and an L grid). It fits nothing and tunes to no target.
- The batch claims no fringes, no density and no weighting.

What's needed:
- One attribution to David ("your ill-posed-question principle") has no quoted source, so it must be labelled a paraphrase (M1).
- David's 1:17 AM words have no original, so they are unverified.
- The batch cites no prior art. The items below are recommended context.

## 1. Attributions

- **1:17 AM** ("This is all very encouraging. Let's proceed with the 2-slit work."): identical in `batch-20.md` and ledger L79, and labelled relayed by Physics Lead, not signed, verbatim.
  - **Flag: unverified.** There is no original, and it has not been confirmed by Physics Lead to us.
  - Recording it as a **ruling** (L79) is fine: it only starts the line of work.
- **"your ill-posed-question principle"** (For David): this is attributed to David with no time and no quote, and I find no recorded David text for it. It must be marked as a paraphrase or a Lead term (M1).

## 2. Prior art: path integrals on multiply connected spaces (recommended context)

- **Schulman, "A path integral for spin", Phys. Rev. 176 (1968) 1558 (V-meta).** In the standard account, the path integral on a multiply connected configuration space splits into a sum over homotopy classes of paths.
- **Laidlaw & DeWitt, "Feynman functional integrals for systems of indistinguishable particles", PRD 3 (1971) 1375 (V-meta).** The homotopy classes carry phases given by a one-dimensional representation of $\pi_1$.
- **Relevance:**
  - The batch's "routes = deck classes rel a declared reference" is exactly the classical skeleton of the Schulman / Laidlaw–DeWitt decomposition.
  - The relative-to-reference point (#381) matches the standard need for a base path.
  - These are quantum results: the phases and amplitudes are added by hand, which is what the batch excludes. Cite them as **prior art for the index set only**, not as support for any intensity.
- **Aharonov & Bohm, "Significance of electromagnetic potentials in the quantum theory", Phys. Rev. 115 (1959) 485 (V-meta).** This is the quantum phase from flat-connection holonomy. It is consistent with #393's exclusion of classical Wilson-loop read-outs. Prior art only.

## 3. Classical analogues of two-slit experiments (pilot-wave hydrodynamics)

- **Couder & Fort, "Single-particle diffraction and interference at a macroscopic scale", PRL 97 (2006) 154101 (V-meta).** Walking droplets reported to build up single- and double-slit patterns statistically.
- **Andersen et al., "Double-slit experiment with single wave-driven particles and its relation to quantum mechanics", PRE 92 (2015) 013006 (V-meta).** In the standard account, they did not reproduce the interference pattern.
- **Pucci, Harris, Faria & Bush, "Walking droplets interacting with single and double slits", JFM 835 (2018) 1136 (V-meta; Crossref issue date 2017).** In the standard account, they did not reproduce single-particle interference.
- **Relevance:** the only classical analogues that claim fringes get them from a real **wave field** that guides the particle (a physical wave, not one added by hand), and even those claims did not survive replication. The batch's conclusion is consistent with this: with classical point particles and no wave, there are no fringes. Cite as context.
- **Not used:** I verified no paper on classical test-particle "route" statistics on a flat cylinder. No novelty claim is made, and none should be.

## 4. Internal checks

- **Set 1:**
  - $n=\lfloor D\tan\theta/L\rfloor$ rel the declared strip reference is correct.
  - "Fixed by the world, ill-posed from the record" is consistent with #381/#399.
- **Set 2:** "timing carries no information" is correct for this flat, static cylinder, since the cover distance is the same in every $W_L$.
- **Set 3:**
  - The structure listed (sawtooth, harmonic $\Delta/n$, periodicity, finite set for a discrete Γ-family) needs no measure. This is correct.
  - "No density, fringes or bands without counting or weighting" is stated, which is the right guard.
- **Carry-overs:**
  - The handle round trip (#399 R4) is consistent.
  - The need for an extra input for a discrete family (#398 F7) is consistent.
  - No Tipler/Misner/Simpson–Visser/flux statements are restated.

## Must-fix (OLD occurs once at 3a6fdbc)

M1. `notes/creative/batch-20.md`
- OLD: `(your ill-posed-question principle)`
- NEW: `(the ill-posed-question principle, in paraphrase; not a quoted ruling of yours)`

## Guardrails (strong watch, two-slit)

- **No Born, $|a|^2$ or $1/N$ result.** None appears. $|a|^2$ occurs only in the exclusion clause.
- **No interference from classical counting.** Set 3 and Set 4 explicitly deny density and fringes without a weighting. The harmonic family is a list of worlds, not intensities.
- **No M1/M2 pick.** (M1) stays untouched at L3, and the weighting stays parked.
- **No Everett framing.** "Many worlds per hit" means record-class membership (#372), not branching amplitudes. Everett is not cited. If it is ever mentioned, it should be as prior art only.
- **Script and results are not tuned to a target.** Fixed inputs, a closed-form map, and no fitting.
- No forbidden Greek letter in the batch or in this file.
- No CTC or topology pick: the cylinder is a toy.
- Paper 1 untouched; nothing goes into `versions/` or `papers/`.
- David's words are labelled relayed by Physics Lead, not signed. They are unverified (flagged above).
- No geon ruling.

## Rows
- **L75:** live.
- **L76:** live.
- **L77:** live (skeleton only). Cite Schulman / Laidlaw–DeWitt as the quantum counterpart of the index set.
- **L78:** open. Consistent with the walking-droplet replications.
- **L79:** a ruling; the text is unverified.
