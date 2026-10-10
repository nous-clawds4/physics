# Literature check: substitution-test scoping note (#256)

**Verdict: HOLD (narrow).** The [L] items check out against primary sources, but four record descriptions are inaccurate or incomplete:
- the state-supervenience paraphrase;
- the incomplete axiom list;
- the Deutsch 1999 summary;
- the break point for branch counting, which omits diachronic consistency.

The critics also need named works. Eight strings are required and three recommended. The framing is neutral: DW is described, not argued against, and there is no verdict on David's conjecture.

**Heads read:** #256 head `6cc40ee` (`notes/substitution-test-scoping.md`, 1,333 words by `str.split`); base and main `f8917fb` (#254 merged from head `e833651`, with all three #255 strings landed); `versions/v0.9-prose.md`, `reviews/born-rule-readiness.md`, the litmus and MERW notes, and Paper 1, all at `f8917fb`. I re-checked the head before filing.

## [L] Record findings (sources quoted)

**Sources read.**
- Wallace 2010 preprint, arXiv:0906.2718v1, "A formal proof of the Born rule from decision-theoretic assumptions" (the *Many Worlds?* chapter "How to prove the Born rule"). Read in full.
- Wallace 2007, arXiv:quant-ph/0312157v2.
- Deutsch 1999, arXiv:quant-ph/9906015.
- Kent, arXiv:0905.0624v3.
- Crossref for all bibliographic data.

I did not have access to the book text of Wallace 2012. Chapter-level statements below come from Crossref and from secondary reviews (NDPR; Wallace's own book page). Axiom wording is quoted from the preprint, which the book's chapter follows. Safest wording: cite "Wallace (2012), ch. 5" with statements "as in Wallace (2010)".

- **[L1] Wallace 2012, chapter 5.**
  - Crossref gives the chapter as "Symmetry, Rationality, and the Born Rule" (doi:10.1093/acprof:oso/9780199546961.003.0007).
  - The preprint (§4, "The quantum decision problem"; §5, "The dictates of rationality"; §7, "Formal statement of the axioms") gives:
    - **Richness axioms:** "Reward availability", "Branching availability", "Erasure", "Problem continuity".
    - **General rationality axioms:** "Ordering" and "Diachronic consistency". The latter reads: "if the agent's future self in the ith branch will prefer Vi to Vi′, then the agent prefers performing U followed by the Vi s to performing U followed by the Vi′ s".
    - **Axioms specific to the Everettian setting:** "Macrostate indifference", "Branching indifference" ("An agent doesn't care about branching per se: if a certain measurement leaves his future selves in N different macrostates but doesn't change any of their rewards, he is indifferent as to whether or not the measurement is performed"), "State supervenience" ("An agent's preferences between acts depend only on what physical state they actually leave his branch in") and "Solution continuity".
  - The note's list matches on ordering, diachronic consistency, richness and branching indifference. It has two defects:
    - Its state-supervenience gloss, "the quantum state and the reward", is not Wallace's statement (L3).
    - It omits macrostate indifference and solution continuity (L4). The richness gloss is acceptable, but naming the four axioms is safer (L2).
  - NDPR's review of the book (Peter Lewis) confirms the same structure for ch. 5. It describes standard ordering and diachronic consistency, "uncontroversial axioms concerning the richness", and four Everett-specific axioms.
- **[L2] The representation theorem.** The preprint reads: "Born rule theorem: There is a utility function on the set of rewards, unique up to affine transformations, such that one act is preferred to another iff its expected utility, calculated with respect to this utility function and to the quantum-mechanical weights of each reward, is higher." It is proved formally in the preprint's §8. The note's "expected utility with weights $|a|^2$" is correct but compressed (L5). Readiness §1.1's conditions (a) and (b) are quoted accurately at note l.35.
- **[L3] Wallace on non-Born rules.**
  - The preprint's §9, "Other proposed strategies for action", says: "all contradict the Born rule, and so all violate the decision-theoretic axioms".
  - On branch counting: "it violates the combination of branching indifference and diachronic consistency". The example gives utilities r/2 and 2r/3.
  - Albert's "fatness rule" violates diachronic consistency. Price's rule, "on natural precisifications … either violates continuity or is not actually a counterexample".
  - Wallace also says branch count is not well defined in quantum mechanics: "There is no such thing as 'branch count'".
  - The book's ch. 5 ends with the same survey (NDPR: "the rule according to which the each branch gets an equal probability violates the combination of the diachronic consistency and branching indifference axioms").
  - So the note's break point for uniform counting should name diachronic consistency too (L7).
  - No $|a|^p$ rule is treated in either preprint. The note does not say otherwise: its $|a|^p$ row is the programme's own arithmetic.
  - **Banned word:** the note does not use the term in question. Neither preprint uses it either ("Branch counting"), so no quotation issue arises. Keep "branch counting".
  - **Arithmetic:** $n\cdot|a/\sqrt n|^p=n^{1-p/2}|a|^p$, which equals $|a|^p$ for all $n\ge2$ (with $a\ne0$) iff $p=2$. I checked numerically: $n=2$, $p=1,2,3,4$ give $\sqrt2$, 1, $1/\sqrt2$, $1/2$. The note's statement is right.
  - "The norm in state supervenience" is imprecise. In Wallace, equal moduli enter through the equivalence lemma, via erasure together with state supervenience ("we actually require … that $|\alpha|=|\beta|$") (L9).
- **[L4] The critics.** Verified via Crossref:
  - Albert, D. Z. (2010), "Probability in the Everett Picture", in Saunders, Barrett, Kent and Wallace (eds), *Many Worlds?*, OUP, pp. 355–368, doi:10.1093/acprof:oso/9780199560561.003.0013.
  - Price, H. (2010), "Decisions, Decisions, Decisions: Can Savage Salvage Everettian Probability?", ibid., pp. 369–390, doi:…003.0014.
  - Kent, A. (2010), "One World Versus Many: The Inadequacy of Everettian Accounts of Evolution, Probability, and Scientific Confirmation", ibid., pp. 307–354, doi:…003.0012, arXiv:0905.0624.
  - Maudlin, T. (2014), "Critical Study: David Wallace, *The Emergent Multiverse*", *Noûs* 48(4), 794–808, doi:10.1111/nous.12072.

  Each is a critique of the DW programme:
  - **Albert and Price:** Wallace himself says they "sought to undermine the possibility of a proof by proposing other, (allegedly) equally rationally justifiable alternatives to the Born rule".
  - **Kent:** his abstract says "Wallace's proposed decision theoretic axioms … and claimed derivation of the Born rule are examined".
  - **Maudlin:** the text is paywalled. I verified it only as a critical study of the book, not specifically its treatment of the decision-theoretic argument. Safest wording: "Maudlin 2014, a critical study of Wallace 2012" (L8).

  The note names the four only by surname with [L] marks; L8 supplies the works. Dizadji-Bahmani 2015 is used, via readiness §1.1, and it is in readiness's references (BJPS 66(2), 257–283; Crossref doi:10.1093/bjps/axt035). Barnum et al. 2000 is also in readiness's references (Crossref doi:10.1098/rspa.2000.0557).
- **[L5] Deutsch 1999 (not [L]-marked, but a record claim).** The note says "symmetry under swaps of equal-amplitude branches, plus additivity under splitting". Deutsch's premises are different:
  - additive payoff utilities ("indifferent between receiving two separate payoffs with utilities x1 and x2, and receiving a single payoff with utility x1 + x2");
  - a "zero-sum rule";
  - a proof that equal-amplitude superpositions have the mean value;
  - then unequal amplitudes, handled by splitting with an auxiliary system.

  "Additivity under splitting" is not Deutsch's premise (L6).

## Other findings

- **F1 (framing, PASS).**
  - The note describes DW and does not argue against it. Its "Framing caution" places DW as a worked case, "not as a rival frame". It cites Paper 1's "they are not Everett worlds" (verbatim) and v0.9 §12's "Not this frame".
  - "Contested in the literature" cites both sides.
  - There is no verdict on David's conjecture; it is only pointed to.
  - Nothing frames the programme as undercutting DW. Critic Q5 raises the risk openly.
  - The standing constraint is managed by placing this material in a separate companion paper, which is David's ruling.
- **F2 ([PJ] flags).** There are four in-text flags (l.42, l.48, l.52, l.57) plus the legend (l.6). All are correctly placed and neutrally worded.
  - The l.48 flag ("no row is a pass or a fail") covers the whole (ii) table. That includes the unflagged "Nothing" in the (M2) row and "not the weight rule" in the arrival row. I see no unflagged pre-judgement outside it.
  - (R-c) "is DW's fine-graining premise" asserts an identity between David's LT3 and a DW premise. "Parallels" is safer (R1, recommended).
- **F3 (pointers, PASS).**
  - v0.9: C6, C7, C12–C14 (2/3 against 1/2), C16, C26, C30, C33, C35 (undefined, 1/2, 1), C36; §2 (no Born-type claim); §8.2 items 1 and 7; §8.3; §8.4; §9; §10 (trivial scheme); §11 (EPP1 a named postulate); §12.
  - Other files: readiness §1.1 and the scan; `law-of-R-scoping.md` F0–F11; the litmus note at `f8917fb` (David's revised scope, the substitution test, the conjecture); the MERW note's O2–O5.
  - The (ii) rows match v0.9 and the notes and pick nothing: no (M1)/(M2), T, Q-D, #139 or Z pick, and no law of R.
  - The MERW row's "product of the left and right Perron vectors" is true for a symmetric operator, where the two coincide. But Burda et al. state the density as $\psi_i^2$ and say nothing about left/right products (#251), so M1 restates it (recommended).
- **F4 (attribution, PASS).** "per David's ruling of about 11:48 ET on 2026-10-10, relayed by the Physics Lead. That exchange is not recorded in this repository." This meets the #249/#253 standard.
- **F5 (guardrails, PASS).**
  - No Born, $|a|^2$ or $1/N$ result is claimed for the framework.
  - The banned words are absent (the banned label for the counting rule, chi, 4-geon, spin-foam, cartoon, the GRW acronym).
  - Bell is not mentioned.
  - Paper 1 and `versions/` are untouched.
- **Word count.** 1,333 (`str.split`); 1,451 with all eleven strings applied.

## OLD/NEW (file `public-papers/observer-space-framework/notes/substitution-test-scoping.md` at `6cc40ee`; each OLD occurs once)

- **L1 (required).** OLD: `**Wallace (2012)**, cited in v0.9 and readiness §1.1. The premises **[L: names, exact statements and chapter]**:`
  NEW: `**Wallace (2012)**, ch. 5, "Symmetry, Rationality, and the Born Rule", cited in v0.9 and readiness §1.1; the axiom statements below follow the preprint version (Wallace 2010, arXiv:0906.2718, §§4–7). The premises:`
- **L2 (required).** OLD: `- **richness** axioms (enough available acts, including erasure-type operations);`
  NEW: `- **richness** axioms (reward availability, branching availability, erasure and problem continuity);`
- **L3 (required).** OLD: `- **state supervenience** (preferences depend only on the quantum state and the reward);`
  NEW: `- **state supervenience** (preferences between acts depend only on the physical state each act leaves the agent's branch in);`
- **L4 (required).** OLD: `- **branching indifference** (indifference to branching that leaves payoffs unchanged).`
  NEW: `- **branching indifference** (indifference to branching that leaves payoffs unchanged);` + newline + `- **macrostate indifference** and **solution continuity** (the other two axioms specific to the Everettian setting).`
- **L5 (recommended).** OLD: `A **representation theorem** then gives expected utility with weights $|a|^2$ **[L]**.`
  NEW: `A **representation theorem** (the "Born rule theorem" of Wallace 2010) then gives a utility function, unique up to affine transformations, such that acts are ranked by expected utility computed with the quantum-mechanical weights $|a|^2$.`
- **L6 (required).** OLD: `an agent's preferences over quantum games, plus symmetry under swaps of equal-amplitude branches, plus additivity under splitting, yield $|a|^2$ weights.`
  NEW: `the values a player assigns to quantum games, with additive payoff utilities and a zero-sum rule, give an equal-amplitude superposition its mean value; unequal amplitudes are then reduced to equal ones by splitting with an auxiliary system, which yields $|a|^2$ weights.`
- **L7 (required).** OLD: `| Branching indifference / fine-graining invariance; readiness`
  NEW: `| Branching indifference with diachronic consistency (the combination Wallace says branch counting violates) / fine-graining invariance; readiness`
- **L8 (required).** OLD: `Wallace's own treatment of alternative rules **[L]**; Price, Kent, Albert, Maudlin **[L]**)`
  NEW: `Wallace 2012, ch. 5, and Wallace 2010, §9, on alternative rules; Albert 2010, Price 2010 and Kent 2010 in *Many Worlds?*; Maudlin 2014, a critical study of Wallace 2012)`
- **M1 (recommended).** OLD: `For a symmetric operator, MERW's density is the product of the left and right Perron vectors, so`
  NEW: `For a symmetric operator, MERW's stationary density is $\psi_i^2$ (Burda et al. 2009), the left and right Perron vectors coinciding, so`
- **R1 (recommended).** OLD: `LT3's "irrelevant further splitting" is DW's fine-graining premise;`
  NEW: `LT3's "irrelevant further splitting" parallels DW's fine-graining premise;`
- **L9 (recommended).** OLD: `and the norm in state supervenience`
  NEW: `and the norm's role in the equivalence lemma (erasure with state supervenience)`

I applied all eleven mechanically. Each matches once. The note goes from 1,333 to 1,451 words.
