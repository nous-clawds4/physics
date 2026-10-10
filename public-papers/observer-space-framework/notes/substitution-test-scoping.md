# Substitution test: scoping and outline for a separate companion paper (options and costs only)

**Status.** This is the scoping and outline for a **separate companion paper**, per David's ruling of about 11:48 ET on 2026-10-10, relayed by the Physics Lead. That exchange is not recorded in this repository.
Circularity discussion stays out of the main paper, which raises it only to pre-empt an expected accusation. The v0.9 §2 firewall ("It does not frame the problem as Everett versus Deutsch–Wallace") governs v0.9, which this note leaves untouched. No Born derivation, no law of $R$, no (M1)/(M2) pick, no verdict on David's conjecture.

**Markers.** **[L]**: needs Literature's record check (not already in Paper 1, v0.9 or the reviews). **[PJ]**: could be read as pre-judging the conjecture.

**Read at:** main `f8917fb` (#254 merged): the litmus, MERW and Zeno notes, `reviews/born-rule-readiness.md` (with the v0.9 refresh), `reviews/law-of-R-scoping.md`, `versions/v0.9-prose.md`.

## The test as recorded, and an operational form

The test (`notes/born-litmus-test.md`): swap a rule $W'$ into a derivation of $W$; if it slides in with nothing else changing, the rule was put in by hand (failure); a genuine derivation breaks an input, lemma or symmetry upstream. Failure means circular injection in whole or in part; no technicality yields a pass. David's conjecture (DW fails, this framework passes) is quoted there and not analysed here.

**One operational form (option T-a).** For a derivation $D$ of $W$ and a substitute $W'$, record:
- **(S1)** the break list: the premises, lemmas or symmetries of $D$ that are inconsistent with $W'$;
- **(S2)** the minimal edit to $D$ that yields $W'$;
- **(S3)** whether each broken item is independently motivated, or is $W$ (or a special case of $W$) restated.

"Slides in" means that S1 is empty, or holds only items judged under S3 to be restatements. "In part" means that some item restates $W$ on a sub-case, such as equal weights, or is a parameter tuned to $W$.

**Option T-b** keeps David's informal wording ("slides in / does not"). **Cost:** under T-a every valid derivation has a non-empty S1 by logic, so the content lies in S3, an LT2-type judgement.

## (i) Deutsch–Wallace: structure, described only

**Framing caution.** The companion paper would use Deutsch–Wallace (DW) as a worked case for the test, not as a rival frame. Paper 1 says these objects "are not Everett worlds"; v0.9 §12 keeps DW as a firewall row ("Not this frame"). No side-by-side may suggest an Everettian alternative.

**Origin.** Deutsch (1999), cited in v0.9: the values a player assigns to quantum games, with additive payoff utilities and a zero-sum rule, give an equal-amplitude superposition its mean value; unequal amplitudes are then reduced to equal ones by splitting with an auxiliary system, which yields $|a|^2$ weights. Barnum et al. (2000; readiness refs) charge a hidden probabilistic assumption.

**Wallace (2012)**, ch. 5, "Symmetry, Rationality, and the Born Rule", cited in v0.9 and readiness §1.1; the axiom statements below follow the preprint version (Wallace 2010, arXiv:0906.2718, §§4–7). The premises:
- rationality axioms, including ordering and **diachronic consistency**;
- **richness** axioms (reward availability, branching availability, erasure and problem continuity);
- **state supervenience** (preferences between acts depend only on the physical state each act leaves the agent's branch in);
- **branching indifference** (indifference to branching that leaves payoffs unchanged);
- **macrostate indifference** and **solution continuity** (the other two axioms specific to the Everettian setting).

A **representation theorem** (the "Born rule theorem" of Wallace 2010) then gives a utility function, unique up to affine transformations, such that acts are ranked by expected utility computed with the quantum-mechanical weights $|a|^2$. Readiness §1.1 records the two conditions as they bear on a branch measure: (a) invariance under symmetries swapping equal-amplitude branches, and (b) fine-graining invariance.

**Running the test (outline).**

| Substitute $W'$ | Candidate break points a run would examine | What a run would have to decide (S3) |
|---|---|---|
| Uniform branch counting | Branching indifference with diachronic consistency (the combination Wallace says branch counting violates) / fine-graining invariance; readiness §1.1 notes that (b) "excludes branch counting by assumption" (Dizadji-Bahmani 2015) | Whether that premise is independently motivated or excludes the rival by axiom. Contested in the literature (Dizadji-Bahmani 2015; Wallace 2012, ch. 5, and Wallace 2010, §9, on alternative rules; Albert 2010, Price 2010 and Kent 2010 in *Many Worlds?*; Maudlin 2014, a critical study of Wallace 2012) |
| $\lvert a\rvert^p$, $p\ne2$ | Splitting a branch of amplitude $a$ into $n$ of amplitude $a/\sqrt n$ gives total weight $n^{1-p/2}\lvert a\rvert^p$, which matches the original only at $p=2$. So the candidate break points are additivity under splitting, and the norm's role in the equivalence lemma (erasure with state supervenience) | Whether the norm's role is an independent input (unitarity) or a restatement of $W$ on equal-amplitude sub-cases (the "in part" form). **[PJ]**: either answer bears on the conjecture's first half. None is given |

**Cost.** Exact premises and which lemma uses each **[L]**, then the critique literature **[L]**: weeks of Literature work; the framing risk is managed only by the companion-paper placement.

## (ii) This framework: component by component

v0.9 makes no Born-type claim (§2), so there is no derivation to swap into. The test can only be run pre-emptively, asking for each component where a target weight could enter. **[PJ]**: no row is a pass or a fail.

| Component (pointer) | The swap | What would or would not break | What "in part" injection would look like |
|---|---|---|---|
| EPP1 = (M1), per-vertex $1/\lvert A\rvert$ (§9; §11; C12) | Any other per-arm weight | Nothing upstream: EPP1 is a **named postulate** (§11). Whether a declared postulate is "put in by hand" in the test's sense is open **[PJ]** | Choosing arm multiplicities to reproduce a target; v0.9 §2 excludes this |
| (M2), count at a named cut (§11; C13, C14) | Another cut or grain | Nothing: the cut is a named extra. Weights depend on it (C14: $2/3$ against $1/2$) | A cut or grain chosen so that counts hit a target weight |
| Zeno convention (§8.3; C35; zeno note) | (Z-0)–(Z-v) | Only C35 moves (undefined, $1/2$, $1$). Instance pins are unchanged (C7) | Choosing a reading for the weight it gives |
| Law of $R$ and slice (§8.2 item 1; §8.4; C26; law-of-R scoping F0–F11) | Another rule | Weights follow tree shape only (readiness scan) | A rule tuned until counts match a target: Paper 1's trivial scheme (§10); the §8.4 motivation clause is LT2's check |
| Arrival flag, (a)/(b) (§8.2 item 7; C6, C30, C33) | (A) against a replacement; (a) against (b) | They shape the tree (countable or continuum, C33/C16), not the weight rule | A realisation chosen for its weights |
| MERW route (§9; C36; MERW note O2–O5) | $\psi^2$ to $\psi^p$ | For a symmetric operator, MERW's stationary density is $\psi_i^2$ (Burda et al. 2009), the left and right Perron vectors coinciding, so $p=2$ comes from the uniform-path definition. **[PJ]**: whether that counts as an upstream break is the S3 question | Symmetrisation (O3, backward pairs) or phases (O5) supplied by hand; a truncation chosen for its density |

**Cost.**
A pre-emptive audit is cheap (days; existing C-rows, nothing recomputed). A proper run needs a Born-type claim, which waits on readiness gaps 1–6.

## Relation to LT1–LT4

The options are:
- **(R-a)** a refinement of **LT2**. LT2 checks where the inputs come from, and S3 asks the same of each broken item;
- **(R-b)** a separate test (an LT5). It checks counterfactual dependence of the output on the inputs, which LT2 does not;
- **(R-c)** a procedure for running LT1–LT4:
  LT1's amplitude work elsewhere adds uses that break under $p\ne2$; LT3's "irrelevant further splitting" parallels DW's fine-graining premise; LT4's second setup adds independent breaks.

**Adds** under any option: a concrete counterfactual, named substitutes $W'$ and a record format (S1–S3). **Cost:** (R-b) needs an S3 criterion distinct from LT2, or it reduces to (R-a).

## Questions for an outside critic

1. Since every valid derivation breaks something under a swap, does the test have content beyond S3, and is S3 just LT2 under another name?
2. In DW, is the equal-amplitude symmetry an independent input, or the Born rule restricted to a sub-case (the "in part" form)? Is this already settled in the literature **[L]**?
3. Is a declared postulate such as EPP1 "put in by hand" in the test's sense, or outside its scope because it claims nothing about Born?
4. Does the $p=2$ in MERW's density (a left-times-right Perron product) count as breaking something upstream, or as the definition restating the target?
5. Can a companion paper run the test on DW without staging the framing v0.9 §2 excludes?
