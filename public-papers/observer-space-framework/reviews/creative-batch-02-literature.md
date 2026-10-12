# Literature prior-art and taste pass: Creative batch 02 (#337)

**Reviewer:** Literature. **Date:** 2026-10-12. **Record type:** review record; applies nothing; do not merge.

**Heads.**
- #337 head `fed0225`, based on `creative/batch-01` (#333); `notes/creative/batch-02.md` plus ledger L11–L14.
- #336 head read on `geometry/sheets-seam-hitting`.
- main `e41412b`.

No earlier review of #337 exists.

**Marks.**
- **V-text:** text or abstract checked, here or in #332 / #335.
- **V-meta:** bibliographic data and topic only.

## Verdict: HOLD (narrow)

Two fixes are needed:
- **R1:** two charter quotes are not verbatim.
- **R2:** Set 3's claim about $P(O)$ is false.

There are also two record collisions to flag for David, on Sets 1 and 2.

### Per-set verdicts

| Set | (a) Already known? | (b) Already killed by the record? | (c) Sneaks the answer in? |
|---|---|---|---|
| 1 Tube = coarse-graining scale | **Known in kind.** Averaging and coarse-graining of geometry over a microscopic scale: the "fitting problem" (Ellis & Stoeger, *CQG* 4, 1697 (1987), V-meta), macroscopic gravity (Zalaletdinov, *GRG* 24, 1015 (1992), V-meta), foam at scale ℓ (Wheeler, *Ann. Phys.* 2, 604 (1957), V-meta). Using it to fix an observer's size: no owner found. | **Collides with a Paper 1 lock (David's call).** "The elementary object remains the jet/patch pair", and "A macroscopic observer, a human, is the jet with the patch allowed to grow, the continuation run separately in each topology". A tube state redefines the elementary observer, and the topologies the tube averages over are, in Paper 1, the relative ensemble $E(O)$. #336 (f) prices the same change (C2). #315 is not touched: a limit in $r_0/\ell$ is a limit of numbers, not of states. | **Hazard.** "Averages out" and "branching statistics have a limit" need weights over handles, seams or topologies. That is a measure, so it falls under the (M1) ruling and the Born guardrails (LT2). It is not smuggled yet, because no weight is written. The charter's own source line ties this approximation to modelling "an experimental test of the Born rule", which raises the LT2 burden. |
| 2 Handles inside the tube | **Yes: this is quantum structure.** States fitting "around each handle", in discrete sectors labelled by $\pi_1$, are Schulman 1968 / Laidlaw–DeWitt 1971 (#332 R4; V-meta / V-text). The same idea for gravitational topology appears in Friedman & Sorkin, *PRL* 44, 1100 (1980) (V-meta). Handle sums and foam: Wheeler 1957; Hawking, *Nucl. Phys. B* 144, 349 (1978); Coleman, *Nucl. Phys. B* 310, 643 (1988) (all V-meta). | **Largely, yes.** The handles a tube encloses are extra topology, which Paper 1 calls the relative ensemble. Paper 1 also "does not revive $\chi$, 4-geons, spin foam, Wheeler's geons-as-particles picture, or Hadley's CTCs-as-particles picture as current claims" (`papers/observer-space-ontology.md` l. 203). Note: that sentence is an agent-written scope disclaimer for Paper 1 (593b5ccd, nous-clawds4, 2026-08-29), not a ruling from David; README.md l. 18 says the ontology "fits well with Wheeler's notions of particles as geons, as well as Mark Hadley's related ideas about particles as 4-geons". Classically, in an analytic host the tube's holonomy around a loop is fixed by the metric. That gives one value, so #334's single-history objection to batch-01 Set 3 applies unless a quantum superposition is added. | **High risk: borrowed quantum mechanics.** "Much as a wave must fit around a ring" is quantisation. Any multiplicity here would come from $\pi_1$ representations, which is the amplitude hook of #332 R4. The batch flags this honestly; as stated it imports rather than derives. |
| 3 Where the patch runs out | **Known.** Edges of maximal developments and incomplete spacetimes: Ellis & Schmidt, "Singular space-times", *GRG* 8, 915–953 (1977) (V-text, abstract: "A classification scheme for boundary points of incomplete space-times"). Quasi-regular singularities include the idealized cosmic string ("Quantum singularity in quasiregular spacetimes, as indicated by Klein-Gordon, Maxwell and Dirac fields", *GRG*; V-text, abstract). Non-uniqueness beyond a Cauchy horizon: Choquet-Bruhat–Geroch 1969 (V-meta) and Chruściel–Isenberg 1993 (V-text). | **Yes, killed.** `papers/patch-edge.md` (David): "The hitchhiker story is dead at the boundary too". Prop. 7.2: "quotients do not lengthen past the cover". Together with Paper 1's "unique simply-connected patch" and #331 §0 / #332 R2 (continuation along one path is unique). Also, the mechanism as written is false (R2): $P(O)$ is simply connected by construction and does not "overlap itself". Self-overlap is the non-injectivity of $P(O)\to W$ into a host with handles, which is $E(O)$ / host structure. | **No** answer smuggled; the set dies on (b). |

### Citations and pointers checked

Accurate:
- #336: genericity (a) meagre / codim-1 / null; (c)–(e) killed; the costs of (f) are its conclusion's three costs (scale, state change, sheet rule = "a law of $R$ in disguise").
- #331 §0; #332 R4; #334 / #335 status in the ledger.
- The TT1–TT4 rename (#335 N1 applied); infinite-harness `creative-tweaks.md`.
- Charter quotes "if we let k approach infinity, we no longer need to justify it" and "all possible worlds includes all possible fundamental groups" are exact.

Not exact: two charter quotes (R1). The charter states that its text "is verbatim", and it is David's, relayed, not signed.

### R1 (charter quotes not verbatim)

The source has lower-case "flat" and curly quotes around "low energy approximation".

OLD:
~~~
**Charter hooks.** "Flat at the smallest scale, nonflat (and nontrivial topology) microscopically, flat at human scale…"; "using 'low energy approximation' as justification";
~~~
NEW:
~~~
**Charter hooks.** "flat at the smallest scale, nonflat (and nontrivial topology) microscopically, flat at human scale…"; "using “low energy approximation” as justification";
~~~

### R2 (Set 3 mechanism is false about $P(O)$)

OLD:
~~~
In a world with handles that patch can't be extended forever: at some distance it overlaps itself, like a map of a donut.
~~~
NEW:
~~~
In a world with handles the patch itself never overlaps itself: $P(O)$ is the maximal simply connected continuation, like the unrolled map of a donut. What overlaps is its image in the host, which is ensemble structure ($E(O)$), and `papers/patch-edge.md` already finds "The hitchhiker story is dead at the boundary too".
~~~

OLD:
~~~
**Tweak.** "branch point" means where the analytic patch $P(O)$ carried along the curvelet stops being embeddable as simply connected (an injectivity-type scale), not where the curvelet meets a seam.
~~~
NEW:
~~~
**Tweak.** "branch point" means where the map from the analytic patch $P(O)$ carried along the curvelet into the host stops being injective (an injectivity-type scale), not where the curvelet meets a seam. ($P(O)$ itself stays simply connected; patch-edge Prop. 7.2: "quotients do not lengthen past the cover".)
~~~

### Guardrails

Clean:
- No forbidden Greek letter or its TeX macro.
- No Born, $|a|^2$ or $1/N$ result.
- No Everett framing.
- No topology, (M1) or (A) pick.
- `versions/` and Paper 1 are untouched.

The watch items are Set 1's implicit weights ((M1)/LT2) and Set 2's borrowed quantum structure.
