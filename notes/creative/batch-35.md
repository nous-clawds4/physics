# Batch 35 — Guidelines for choosing a probability rule (paper only, DO NOT MERGE)

Paper only, exploration only; nothing in versions/ or papers/. Classical only: no Born input, no |a|². (M1) stays untouched at L3. Citations unchecked unless marked. Labels: **[CL]** = Creative Lead proposal or reading.

Note on location: this branch is cut from main, which has no `notes/creative/` ledger. The ledger row is therefore given in §7, to be carried into `notes/creative/ledger.md` when the creative stack lands.

## Plain summary for David

You asked how to choose a probability rule without cheating. We wrote down six guidelines (our draft, for you to approve or change), as guidelines and not a pass/fail test, as you asked at 4:24 PM:
1. **State the rule first,** before trying it on any two-path or fringe setup.
2. **Use only what one world contains** (its geometry, topology, spin structure and records). No adding phases across worlds, no squaring, nothing that exists only in the shadow spacetime.
3. **Prefer a rule that doesn't depend on how we slice things up**: counting paths, worlds or branch points, and blurring into the shadow spacetime, should ideally agree. Agreement between counting worlds and the observer-space branch structure is a hope, not a requirement. "Slicing" still needs a precise definition.
4. **Stay consistent with (M1)**, or give an independent reason to revisit it, out in the open.
5. **No free numbers.** Constants come from the geometry or from normalisation, never from fitting.
6. **Aim for a rule the geometry forces**, not one it merely allows. List every candidate that fits 1–5; if several survive, say so, and don't pick one because of its answer.

After that, and only after, compare with batch 34's leftover count (Geometry's reading in #424 is that its floor survives projection; not yet reviewed by Claude) and report whatever comes out. Note: under (M1), only your third candidate is (M1)-type; trying the first two would mean revisiting (M1), and we would say so openly. Your three candidates (count paths, count worlds, branch points with equal probability) are listed but not evaluated. My intuition, since you asked: the most likely place for the geometry to force a choice is guideline 3. If the counts must agree across slicings and across the shadow projection, only a few rules can survive. Whether one is left is open.

## 1. David's words (verbatim as reported by Creative Lead, direct in Creative Lead chat, not signed; unverified by Literature, no original seen)

- David, 4:15 PM ET 2026-10-14: "The review has been queued for Claude. It feels like we are approaching the point where we consider adding the probability rule, which we have not yet done. There are several candidates that come to mind: count the number of paths, count the number of Worlds, analyze the branch points in Observer space and apply the accompanying equal probability postulate. This is where it would be easy to “cheat”: select the rule that produces the Born rule. Let's try to resist that temptation. Ideally, we will discover that the choice of probability rule is not arbitrary, but is, somehow, forced upon us by the geometry. Whether we will realize this hope is hard to say. What does your intuition tell you?"
- David, 4:24 PM ET 2026-10-14: "Let's write this down as a set of guidelines we should follow, but not as a rigid test we need to pass. It would be particularly nice if we get the same answer counting worlds or analyzing branch structure in observer space, but let's not be too rigid about that expectation."

## 2. Guidelines (Creative Lead proposal, written as guidelines, not a test, per David's 4:24 PM instruction; the content of G1–G6 is not yet approved by David)

- **G1. State the rule blind.** Say what it counts and how it is normalised before applying it to any two-path or fringe setup.
- **G2. World data only.** Metric, topology, spin structure, records. No cross-world phase sums (#419 R5: a sum of e^{iφ} across worlds is a complex weight on W), no squared quantities, nothing defined only in the shadow spacetime (the projection itself, the apparent tolerance of #424 §4a). World data here means: the metric (under the lock only approximately flat in a lab with handles, #410), Γ and deck elements, twist θ, the spin-structure ℤ₂ (#423), Hol(γ) once γ is fixed (#421 §3), and records. Two cross-world structures are unavoidable and allowed: the identification of detectors [d_i] through the LEA chart and a shared reference within τ/2 (#410), without which "the probability of d_i" is undefined, and the measure μ (open).
- **G3. Prefer slicing-independence.** Counting paths, worlds or branch points, and coarse-graining to the shadow spacetime, should give the same answer. Agreement between world counting and observer-space branch structure is a hope, not a requirement (paraphrase of David, 4:24 PM; verbatim in §1). **Flag:** "slicing" is not yet precisely defined. It may mean the choice of cut τ, the grain of the record, the identification class in the LEA, or the foliation, which with CTCs need not exist globally. Status under the lock with CTCs adopted (Geometry): a Cauchy foliation or global time function does not exist in a world with CTCs, only on globally hyperbolic or stably causal subregions; an (M2)-type cut is defined only as a partial achronal cut in a CTC-free region (avoiding the vertex regions); the shadow slicing is well-defined (Minkowski slices, frame fixed up to O(3) and time translations by the anchoring fit, to within εR + ℓ); observer-space and Fermi slices are local only (micro-handles cap the injectivity radius near ℓ, #410), and the observer's proper-time order of branch points is defined if its worldline is not on a CTC. So independence should be required over a family of partial cuts in CTC-free regions, or for the shadow slicing, not over a global foliation.
- **G4. Consistent with (M1)**, or give an independent reason to revisit it. Never override it quietly. (M1) stays at L3. (M1) is the per-vertex rule (an equal share for each way onward, a history's weight the product of the shares); it is not world counting (EPP2, a foil), and the cut count (M2) is not adopted. So of David's candidates (§3), only 3 is (M1)-type. Evaluating 1 (paths) or 2 (worlds) is a revisit of (M1) and must be recorded as one.
- **G5. No free numbers.** Constants are fixed by geometry or normalisation, never fitted.
- **G6. Forced rather than merely allowed.** List the candidates that fit G1–G5. If several survive, say so; do not choose one by its Born output.
- **Then:** compare the result with batch 34's leftover count (#424: leftover ≥ resultant for exact closure within one phase set; Geometry's reading in #424 (L3) is that the floor survives projection; not yet reviewed by Claude) and report it, whatever it is.

## 3. Candidate rules named by David (candidates only; not evaluated)

1. Count the number of paths.
2. Count the number of worlds.
3. Analyse the branch points in observer space and apply the accompanying equal-probability postulate.

No candidate is evaluated here. Each would first need G1's blind statement: what is counted (paths at which grain? worlds in which W? branch points at which cut?) and how it is normalised.

## 4. Relation to the litmus test and FD1

- The guidelines are a working discipline. The **litmus test** (LT1–LT4, David's T1–T4; `public-papers/observer-space-framework/notes/born-litmus-test.md`, L3) remains the check.
- **David's FD1 "Purpose" ruling** (David, 2026-10-11, about 10:03 AM ET, given to Physics Lead and relayed, not signed; L3; recorded in that note; review `reviews/born-litmus-fd1-ruling-literature.md`): the litmus test is designed to detect cheating, i.e. whether the result was put in by hand. Passing means no cheating was detected; it does not show that the Born rule was derived.
- **Overlap [CL]:** G2/G5/G6 serve LT2 (prior inputs fixed independently, not tuned); G3 serves LT3 (robustness to grain, cut and further splitting), which under the per-LT sort (Lead ruling, 2026-10-11, under David's delegation of 12:34 PM ET; relayed, not signed) is an emergence/completeness check, not a cheating signal; the cheating test proper is LT2 plus the substitution test; G1 is the pre-commitment LT2's motivation clause asks for. The guidelines do not replace any LT and are not a test themselves.

## 5. Ill-posed questions to avoid

- "Which rule gives the Born rule?": aiming at the answer (LT2).
- "The probability of d_i" before G1 states what is counted.
- "The number of worlds" when W is a continuum and μ is open.
- "Do counting worlds and branch structure agree?" before "slicing" is defined (G3).

## 6. Prior art (bibliographic data checked by Literature, #426; texts unread)

Everett, Rev. Mod. Phys. 29, 454 (1957); DeWitt, Physics Today 23(9), 30 (1970) and DeWitt–Graham (eds.), The Many-Worlds Interpretation of Quantum Mechanics (Princeton 1973) (world counting); Deutsch, Proc. R. Soc. A 455, 3129 (1999) / Wallace, The Emergent Multiverse (OUP 2012) (decision theory); Zurek, Phys. Rev. A 71, 052105 (2005) (envariance); Vaidman, Int. Stud. Phil. Sci. 12, 245 (1998) (self-location). Context only. None is imported, and the Everett framing is not adopted.

## 7. Ledger row (to carry into notes/creative/ledger.md)

| L173 | probability-rule guidelines (Creative Lead proposal, written as guidelines, not a test, per David 4:24 PM; content not yet approved by David) | batch 35 (revised per Geometry P1–P3, Literature M1–M5): G1 blind statement; G2 world data only; G3 slicing-independence preferred (world vs branch-structure agreement a hope; 'slicing' undefined); G4 (M1)-consistent or openly revisited; G5 no free numbers; G6 forced not allowed, list survivors; then compare with batch 34's leftover. Candidates (paths, worlds, branch points + equal probability) listed, not evaluated; only the third is (M1)-type, so evaluating 1–2 is a recorded revisit of (M1). G2 allows the [d_i] identification and μ as the only cross-world structure. G3 independence over partial cuts in CTC-free regions or the shadow slicing. Batch 34 floor: Geometry's reading (#424 L3) that it survives projection, not yet reviewed by Claude. David 4:15/4:24 PM (direct in Creative Lead chat, not signed; verbatim as reported by Creative Lead; unverified by Literature, no original seen) | David 4:15/4:24 PM | **guidelines** | open |
