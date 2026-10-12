# Literature pass: creative batch 11 (L36–L37), PR #363

Reviewer: Literature agent. PR head recorded: `729075a` (base `creative/batch-10`). Files: `notes/creative/batch-11.md`, `notes/creative/charter.md`, `notes/creative/ledger.md`. Do not merge. Marks: **V-text** = wording read (abstract or full text); **V-meta** = bibliographic data verified (Crossref), content from the standard account.

## 1. Citations

| Citation | Mark | Finding |
|---|---|---|
| Echeverria, Klinkhammer & Thorne, "Billiard balls in wormhole spacetimes with closed timelike curves: Classical theory", PRD 44 (1991) 1077–1099, doi:10.1103/PhysRevD.44.1077 | V-text (abstract) | Correct in substance. Multiplicity is the number of self-consistent solutions for an initial trajectory. "All dangerous initial trajectories in a wide class have **infinite multiplicity**"; "trajectories where the ball is initially at rest far from the wormhole have multiplicity one". The batch's "several" understates this (S2). |
| Friedman, Morris, Novikov, Echeverria, Klinkhammer, Thorne & Yurtsever, "Cauchy problem in spacetimes with closed timelike curves", PRD 42 (1990) 1915–1930, doi:10.1103/PhysRevD.42.1915 | V-text (abstract) | Massless scalar $\Box\Phi=0$. For wormhole spacetimes, self-consistency "seems to place no constraints on initial data … posed on past null infinity". These spacetimes are "benign", and the authors "suspect" this is typical for "noninteracting (linearly superposing), classical fields", while "interacting classical systems can behave quite differently". That is an **existence / no-constraint** statement. The abstract claims no uniqueness theorem. |
| Friedman & Morris, "The Cauchy problem for the scalar wave equation is well defined on a class of spacetimes with closed timelike curves", PRL 66 (1991) 401, doi:10.1103/PhysRevLett.66.401; and Friedman & Morris, Commun. Math. Phys. 186 (1997) 495 (existence and uniqueness for massless fields) | V-meta | The uniqueness results for linear fields are here, for a restricted class of spacetimes. |
| Chruściel & Isenberg, PRD 48 (1993) 1616, "Nonisometric vacuum extensions of vacuum maximal globally hyperbolic spacetimes" | V-meta | Supports non-unique extension past a Cauchy horizon (Taub–NUT type). |
| Hadley 1997 / 2000 | V-text per #362 | Used correctly. The batch combines CTCs (1997) with non-time-orientability (2000) in one geon region. That combination is the batch's own synthesis, and it is acceptable as stated. |

**The batch's linear-signal point stands:** a linear beacon gives one consistent reply. Friedman et al. 1990 themselves contrast linear fields with interacting billiard balls. Only the attribution of *uniqueness* needs fixing (S1).

## 2. Prior art

**Measurement or scattering through CTC regions:**
- Deutsch, "Quantum mechanics near closed timelike lines", PRD 44 (1991) 3197 (V-meta): a fixed-point consistency condition on the CTC system's state.
- Politzer, "Simple quantum systems in spacetimes with closed timelike curves", PRD 46 (1992) 4470 (V-meta).
- Friedman, Papastamatiou & Simon, "Failure of unitarity for interacting fields on spacetimes with closed timelike curves", PRD 46 (1992) 4456 (V-meta): interacting fields scattered through a CTC region give non-unitary evolution.
- Lloyd, Maccone, Garcia-Patron, Giovannetti, Shikano, Pirandola, Rozema, Darabi, Soudagar, Shalm & Steinberg, "Closed Timelike Curves via Postselection", PRL 106 (2011) 040403 (V-meta).

These are the quantum analogues of the batch's "consistency branches". Each brings its own rule for weighting or selecting among the self-consistent solutions:
- Deutsch's fixed point (maximum-entropy choice when the fixed point is not unique);
- the postselection weight (P-CTCs);
- Politzer's path-integral weights.

So any import of them into L36 would bring quantum structure and a selection rule (L23 and law-of-R hazards). The batch uses none, and correctly writes no rule picking a solution.

**Hadley's Axiom 4 as round-trip signalling.** Closest prior art is Hadley 1997 itself (V-text): CTCs provide "a causal link between measurement apparatus and state preparation, permitting both to form part of the boundary conditions which constrain the field equations". It also says "with CTCs there can exist causal routes from one arm of the experiment to the other". Two differences:
- Hadley's link runs from the apparatus to the preparation, as boundary conditions on the 4-manifold. No signal returns to an observer's record.
- David's 4:17 PM hypothesis (observer → CTC → observer, carrying state information) is a distinct reading. It is near Hadley in spirit but not stated in Hadley.

**"Observation = signal round trip through a geon's CTC."** I found no prior statement in this form. Nearest: Hadley's causal link (above); EKT and Friedman et al.'s scattering through wormhole time machines; and the "multiple histories" time-travel literature (V-meta). So this is novel as a definition of observation, but every ingredient is known.

## 3. Strings

S1. `notes/creative/batch-11.md`
- OLD: `(Friedman–Morris and Friedman et al. 1990; unchecked)`
- NEW: `(Friedman et al., PRD 42 (1990) 1915: for wormhole spacetimes self-consistency appears to place no constraints on the data, "benign", an existence statement; uniqueness for linear fields on a restricted class is Friedman & Morris, PRL 66 (1991) 401 and CMP 186 (1997) 495; V-text/V-meta per #364)`

S2. `notes/creative/batch-11.md`
- OLD: `several self-consistent trajectories for the same initial data`
- NEW: `infinitely many self-consistent trajectories for the same initial data across a wide class of "dangerous" trajectories, while a ball initially at rest far from the wormhole has exactly one (V-text, abstract)`

S3. `notes/creative/ledger.md`
- OLD: `(Friedman et al., unchecked)`
- NEW: `(Friedman et al. 1990 shows existence, "benign"; uniqueness is Friedman–Morris 1991/1997)`

Each OLD occurs exactly once at 729075a.

## 4. Overclaim flags (no strings)

- **Infinite multiplicity.** EKT's infinite multiplicity means L36's consistency branches would typically be infinitely many per round trip. That is relevant to the parked counting question. It is noted only, since the batch is structure-only.
- **Type O / Type F classification.** It is plausible as a sketch on non-time-orientable hosts. It is the batch's own, not from Hadley or EKT, and is already marked a sketch.
- **Set 2.** "Different extensions continue different families of geodesics" (Taub–NUT) is known for geodesics (Misner 1967; Chruściel–Isenberg, V-meta). The extension to signals is correctly marked unchecked.
- **The CTC choice is open for David.** The batch correctly leaves #352's no-CTC condition versus L33's CTCs to David ("restricted to $U$" is offered, not assumed). This review takes no side.

## Provenance

- David's 4:17 PM words are identical in `charter.md` and `ledger.md`, and labelled relayed, not signed (the ledger also says verbatim). I cannot check the wording against a primary record.
- There is no geon ruling by David. The batch claims none.

## Guardrails
- No forbidden symbol (none in this file).
- No Born/$|a|^2$/$1/N$ result.
- No interpretation-camp framing; Deutsch is cited only as prior art.
- No pick among M1/M2/T-options or on the CTC question.
- Paper 1 untouched.

## Verdicts
- **Citations:** EKT and Friedman et al. are correct in substance. The batch understates EKT's multiplicity (S2) and misattributes uniqueness to Friedman et al. (S1, S3).
- **L36 (consistency branches):** known in its ingredients (EKT, Novikov self-consistency; the quantum analogues in Deutsch, Politzer, FPS and Lloyd et al.). Survives. No selection rule is smuggled. It typically gives infinite multiplicity.
- **L37 (extension branches):** known ingredient (non-unique extensions, Chruściel–Isenberg). Survives. The signal-path claim is unchecked, as stated.
- **Round-trip definition of observation:** novel as stated. Its nearest relative is Hadley's apparatus→preparation causal link, which runs the other way.
