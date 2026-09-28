**SCOPING ONLY, NOT A CLAIM.**

# Born-rule readiness: is it too early to ask?

Authors: Geometry, co-written with Literature (the obstacles in §1 are Literature's, lightly edited)
Date: 2026-09-28
Question (David): "is it too early to ask whether the Born rule is on the horizon?" No paper or essay edits; no choice of (M1)/(M2) or T1/T2/T3; no law of $R$; nothing put in by hand ($|a|^2$ appears only as the literature's target); Paper 1's object untouched; type (ii) abandonable.

**Answer.** Too early for any claim; the right time to frame the question. The framework cannot yet state a Born question: it has no amplitudes to attach $|a|^2$ to, no law of $R$ to produce a tree, and no measurement model saying which arms are "the same outcome". But it can now say what would have to exist for outcome counting to give anything other than uniform branch counting, which orders the §9 open items (§3), and one cheap test can run now.

---

## 1. The conditions

### 1.1 Obstacles in the literature (co-written with Literature)

For each approach: (i) the premise that takes it from counting to $|a|^2$ weights, stated as a condition a branch measure $\mu$ would have to meet; (ii) the standard objection; (iii) a citation.

**1. Deutsch–Wallace decision theory.**
(i) Rational preferences over quantum bets that are indifferent to branching which leaves payoffs unchanged. As a condition, $\mu$ must be (a) invariant under unitary symmetries that swap equal-amplitude branches, and (b) unchanged when a branch splits into sub-branches with the same payoff (fine-graining invariance). Together with the other rationality axioms, these fix the weights at $|a|^2$.
(ii) Condition (b) excludes branch counting by assumption, since counting is exactly the rule that changes under splitting. The rival is ruled out by an axiom, not an argument (Dizadji-Bahmani 2015). Deutsch's original derivation was also charged with a hidden probabilistic assumption (Barnum et al. 2000).
(iii) Deutsch (1999).

**2. Zurek envariance.**
(i) If a swap of system outcomes can be undone by a counter-swap on the environment alone, those outcomes are equiprobable. Unequal (rational) amplitude ratios are fine-grained through an ancilla into equal-amplitude states, and their probabilities are summed. As a condition, $\mu$ depends only on the system's reduced state, gives envariantly swappable outcomes equal weight, and is additive under fine-graining (plus continuity for irrational ratios).
(ii) The circularity charge: the link from state to probability, additivity, and "equal amplitude" as the unit of fine-graining are unstated assumptions that already encode the amplitude measure (Schlosshauer and Fine 2005).
(iii) Zurek (2005).

**3. Saunders and Vaidman: branch counting versus self-location.**
(i) *Saunders:* decoherent histories are regrouped into equal-norm units, and probability is the ratio of unit counts. As a condition, $\mu$ is a ratio of counts of equal-norm units that depends on the state and is continuous in the norm topology. *Vaidman:* between decoherence and observation, an observer is uncertain which branch they are on, and credence follows each branch's postulated "measure of existence" (Vaidman 2012). *Sebens–Carroll* replace the postulate with the condition that credence depends only on the observer's local reduced state, not on changes confined to the environment (Sebens and Carroll 2018).
(ii) Question-begging: equal-norm units are in effect taken as equiprobable. Saunders raises this objection himself and replies to it (Saunders 2021, §8). On the self-location side, Vaidman's measure is postulated, so self-location explains what the probability *means*, not its values. Whether Sebens–Carroll's locality principle is independently motivated is disputed: Dawid and Friederich (2022) argue that Sebens and Carroll's ESP-QM is not a less general version of the plausible Epistemic Separability Principle and can be motivated only by quantum mechanics' empirical success, Born rule included, so it cannot serve as a premise for deriving the Born rule (see also Kent 2015, who questions whether self-locating uncertainty makes sense in the universal wave function).
(iii) Saunders (2021), §§7–8.

**4. The measure problem: counting versus weighting.**
(i) Counting needs a finite branch number for each outcome, fixed by the state, whose ratios survive refinement of the coarse-graining and change only when the amplitudes do. As a condition, a count-based $\mu$ needs a privileged grain, or a limit that does not depend on the grain.
(ii) The incoherence objection: decoherence is approximate, so there is no finest branching structure and no fact about how many branches there are. Counts also change under irrelevant further splitting, and with an infinite count the ratios depend on the regulator.
(iii) Wallace (2012), §5.8.1 ("Branch counting").

### 1.2 What each premise becomes in the framework

Objects: the tree of evolutions on $(V,R)$; branch points (decisions on the slice $V^\tau$ with $\mathrm{succ}_R\neq\emptyset$); states $(O^u,a)$ with arrival flag $a$; EPP1 = (M1), the named postulate giving each arm an equal share; (M2), Paper 1's count at a named cut; depth or proper-time cuts.

| Premise | Condition on the framework's objects | Statable now? | Extra structure needed |
|---|---|---|---|
| DW (a): swap symmetry | A lock-side automorphism of $(V,R)$ exchanging two arms forces equal weight | Automorphism, yes; "equal amplitude", **no**. EPP1 and (M2) already weight all arms equally, symmetric or not, so the premise is idle | An amplitude-like invariant on arms |
| DW (b): fine-graining invariance | A prefix's weight is unchanged by *later* splitting of a descendant, and by *same-vertex* splitting of an arm into two with the same outcome | Later splitting, yes: (M1) meets it, (M2) fails (P7). Same-vertex splitting needs an outcome labelling, which does not exist (§6 is a cartoon; matter open); given one, both fail (P7) | A measurement model; agents (the observer is a germ) |
| Zurek: envariance; reduced-state dependence | Weights depend only on $(O^u,a)$ and $R$; outcomes swappable by an "environment" operation get equal weight | Locality half, yes (Obs-local; EPP1 meets it). Swap half, **no**: no system ⊗ environment split, since the germ fixes a whole patch. A union of ensembles $E_W$ is a set, not a Hilbert space: no superposition, inner product or reduced state | A tensor-factorised state space: new theory, not a reading of the lock |
| Saunders: equal-norm units | (M2) counts evolutions at a cut, at the grain fixed by $R$ and the slice | Counting, yes; "equal norm", **no** | A norm on evolutions |
| Vaidman / Sebens–Carroll: self-location | The co-existence weight is the "measure of existence" slot | Slot, yes (EPP1 or (M2) fills it by postulate). Post-branching uncertainty, **no**: distinct arms are distinct germs, so the germ fixes its arm; an observer coarser than the germ breaks the lock | Nothing lock-compatible; the flag $a$ is the only non-germ datum |
| Measure problem: grain or grain-free limit | Branch points are discrete per history (hard gate); (M2) needs a named cut; counts → per-vertex weights iff siblings are asymptotically balanced (C15) | **Yes, fully**: the one premise statable now | none, to state it |

**Where $|a|^2$ would attach: nowhere, today.** Every computable weight is a combinatorial function of a tree (plus a cut for (M2)). No amplitudes, phases or interference exist, so histories never cancel. A hand-drawn tree matching $|a|^2$ is Paper 1's trivial scheme (v0.6 §8). Amplitude structure would be a new postulate; reverse-engineering the path integral is out of scope, as is the action-principle route hoped for in `old-manuscripts/2007-10-20-OutcomeCounting.pdf`.

**How (M1) and (M2) bear on a Born question (neither chosen).**
- **(M1)** *For:* indifferent to later splitting, a DW-type property (P7); state-local, like Sebens–Carroll; cut-free. *Costs:* every single-decision weight is an equal share, so non-uniform outcome weights can come only from tree shape, i.e. the law of $R$; a named postulate (note 9); one chosen product measure on a continuum (C16, P6); in the countable (a) case, weights $2^{-k}$ meet Paper 1 §6's refusal case (C33).
- **(M2)** *For:* literally branch counting, Saunders's slot; carries Paper 1's uniqueness thesis at the cut. *Costs:* fails fine-graining invariance (P7; SHPMP's cut objection); needs a cut on infinite sets, and under (a) no uniform countably additive measure exists; the MERW hazard (path counting yields a squared-eigenvector density a referee may read as Born: a hazard, not a route; C36); a named cut (note 9).

---

## 2. Do the existing toys lean either way?

No. None has amplitudes or interference, so none bears on Born; they bear on counting versus weighting and on countability.

- **V\*/Option F (continuum result).** Under the public ensemble, extend-vs-not marks a continuum of vertex times (Minkowski minus a point: lifetimes fill $(0,\infty)$, C24). *Shows:* without a lock-side slice there is no grain, so neither counting nor EPP1 is defined (premise 4 failing at its root). *Does not show:* anything about weights. *Pin:* analytic; nothing to re-run.
- **$|B|\ge2$ toy** (`papers/B-ge2-minimal-toy.md`, retired to a digraph fact). *Shows:* its two arms (Minkowski continuation; type-(ii) jump to a dust FLRW germ) differ in lock-side invariants ($K=0$ vs $80/27$, P8), so no germ symmetry swaps them, yet EPP1 would weight them equally: the equality is postulated, and envariance has nothing to act on. The arm count itself depends on the isotropy quotient (3 vs 2, C9, P9). *Does not show:* any weight; none is assigned.
- **20-decision bound computation** (Kretschmann rule as stated, unadopted, without (a)). *Shows:* with $m=2$ jump arms per bound decision the jump share is $2/3$ in expectation (0.6672); at $c=0.1$, 6.58% remain bound after 20 decisions and leavers leave after 5.90 decisions on average; at $c=0.01$, 99.94% (P1, P2). These are branch-count consequences of a regular 3-star, and they move with the rule's constant $c$, not with anything amplitude-like. *Does not show:* Born; it shows jump dominance, which blocks stable records before any Born comparison.
- **(a)-transient.** *Shows:* $m\le1$, so the jump share is 1/2 while branching lasts (0.5015, 0.4999); one jump at $c=0.1$; 13–14 jumps, chain ≤14, 29,119 orbits and 14,477 stuck at $c=0.01$ (P3–P5); completed histories countable. This bears on the measure: (M1) gives unequal weights $2^{-k}$; (M2) has no uniform countably additive measure. *Does not show:* anything about $|a|^2$.

### Pins (all re-run for this note, 2026-09-28)

Python 3.13.5, numpy 2.5.3, scipy 1.18.1, sympy 1.14.0 (venv `/workspace/g128/venv`). Units $G=c=1$, $M=1$. The orbit is $[10,20]$, with $E=0.969087$ and $L=4.170288$. The library is `/workspace/g154/kr.py` with `THROAT='cross'`. As in #155 and #157, scripts stay on the shared machine (the repo holds no scripts); SHA-256 prefixes below.

| Pin | Script and arguments | Seed | Output (confirmed) |
|---|---|---|---|
| P1 | `g154/sim.py 0.1 stated 200000 20 7 cross` | 7 | jump share 0.6672; bound after 20 decisions 0.0658 (SE 0.0006); leavers' mean 5.902 decisions |
| P2 | `g154/sim.py 0.01 stated 20000 20 3 cross` | 3 | jump share 0.6669; bound 0.9994 (SE 0.0002) |
| P3 | `g154/agraph.py 0.1` | none (exact) | 3 reachable orbits; 0 turning points with 2 admissible edges; longest chain 1 |
| P4 | `g154/agraph.py 0.01` | none (exact) | 29,119 orbits; 0 turning points with 2 edges; 14,477 stuck; longest chain 14 |
| P5 | `g154/along.py` ($N=20{,}000$ each) | 5 | $c=0.1$: 1 jump in all histories, share 0.5015; $c=0.01$: 13 jumps (3,169) or 14 (16,831), share 0.4999 |
| P6 | `g154/c16.py` | none (exact) | $a=9.892616$, $b=10.107529$; min derivative 1.098432; image inside $[a,b]$: True |
| P7 | `born/pins/fg.py` | none (exact) | $w(A)$: base (M1) 1/2, (M2) 1/2; later split (M1) 1/2, (M2) 1/3; same-vertex split (M1) 1/3, (M2) 1/3 |
| P8 | `born/pins/flrw_k.py` | none (symbolic) | $K_{\rm FLRW}(0)=80/27\approx2.963$; $K_{\rm Mink}=0$ |
| P9 | `g128/misc.py` (item 3) | fixed | $\lvert B\rvert=3$ unquotiented, 2 modulo isotropy; $\dim H^3=3$ |

SHA-256 prefixes: kr `0432cc20`, sim `df306f17`, agraph `edf42d6e`, along `750def92`, c16 `dd6f6a0b`, misc (g128) `f131b3de`, fg `c83641c9`, flrw_k `3ee6f263`. New scripts: `fg.py` computes $w(A)$ under (M1) (product of $1/\deg$ over ancestors) and (M2) (fraction of depth-2 leaves) on three trees: base $\{A\to A_1, B\to B_1\}$; later split $B\to\{B_1,B_2\}$; same-vertex split adding $B'\to B'_1$ at the root. `flrw_k.py` evaluates $K=12[(\ddot a/a)^2+(\dot a/a)^4]$ for $a=(1-t)^{2/3}$ at $t=0$ in sympy.

---

## 3. What would settle it, in what order, and one cheap test

**Gating order** (§9 open items; each is needed before the next means anything):

0. **Keeping type (ii).** Abandoned, $|B|=1$ (CWS singleton): no weights to ask about.
1. **Law of $R$ and the slice**, with motivation among admissible pairs (else Bertrand). No tree without them.
2. **Jump dominance, (J1) or (J2).** Failing both gives jump-dominated histories (P1) and no stable records.
3. **(a) versus (b), and arrival semantics (T1).** Countable versus continuum histories; where EPP1 applies.
4. **The measure (M1)/(M2)**, with completed-vs-cut, the Zeno-mass convention and the weight's reading: per-vertex shares or counts.
5. **A measurement model, including matter.** Without "same outcome", neither DW (b) nor any frequency comparison is statable.
6. **Amplitude-like structure**: whether some germ or $R$ invariant plays the literature's $|a|^2$ role (the Hope "weights forced"). Born enters only here.

The measure-problem premise can be worked on now; everything else waits on gates 1–5.

**One cheap next test: continuous response.**
- *Question:* can a uniform, local, no-case-list rule make an outcome's weight depend on a continuous germ parameter while every single-decision branch count is identical?
- *Setup:* the worked Kretschmann rule as stated (unadopted), $c=0.1$, `kr.py` with `THROAT='cross'`; bound orbits with apastron 20 and periastron $r_p\in\{9.00,9.01,\dots,11.00\}$ (201 germs), starting at periastron. Outcome fixed in advance: $X_n$ = "still bound after $n$ decisions", $n=1,\dots,10$.
- *Computation:* exact enumeration memoised on the orbit $(r_{\min},r_{\max})$, at most $3^{10}$ paths, no sampling. $w_n^{M1}(r_p)$ = EPP1 weight of the bound depth-$n$ paths; $w_n^{M2}(r_p)$ = bound fraction of the depth-$n$ cut, dead ends kept (v0.6 §7). Depth counts decisions (jump-reached states do not branch under (A)); log $|A|$ at every decision to confirm it is 3.
- *PASS:* for some $n\le10$, $w_n^{M1}$ or $w_n^{M2}$ takes at least two values across the grid, with $|A|=3$ at every bound decision. *FAIL:* both constant in $r_p$ for all $n\le10$ (or $|A|\ne3$ somewhere, which voids the test).
- *PASS would show* that weights are counting at a grain set by $R$ and that a germ parameter can enter through tree shape alone. It would **not** show Born, $|a|^2$ or interference: the rule is unmotivated, the outcome is a picture, and at finite $n$ every $w_n^{M1}\in3^{-n}\mathbb Z$, so continuous response exists only as a limit (premise 4's grain problem, concretely). Whether (M1) and (M2) respond differently is a readout, not a choice.
- *FAIL would show* that on this instance weights are blind to the germ within the family, so Born-type state dependence would need an $R$ whose tree shape varies with the germ; it says nothing about other rules.
- *Cost:* one script, minutes; no postulate, no law of $R$. Not run for this note.

---

## References

- Barnum, H., Caves, C. M., Finkelstein, J., Fuchs, C. A., and Schack, R. (2000). Quantum probability from decision theory? *Proc. R. Soc. Lond. A* 456, 1175–1182.
- Dawid, R., and Friederich, S. (2022). Epistemic separability and Everettian branches: a critique of Sebens and Carroll. *Brit. J. Phil. Sci.* 73(3), 711–721. doi:10.1093/bjps/axaa002.
- Deutsch, D. (1999). Quantum theory of probability and decisions. *Proc. R. Soc. Lond. A* 455, 3129–3137.
- Dizadji-Bahmani, F. (2015). The probability problem in Everettian quantum mechanics persists. *Brit. J. Phil. Sci.* 66(2), 257–283.
- Kent, A. (2015). Does it make sense to speak of self-locating uncertainty in the universal wave function? Remarks on Sebens and Carroll. *Found. Phys.* 45(2), 211–217. doi:10.1007/s10701-014-9862-5.
- Saunders, S. (2021). Branch-counting in the Everett interpretation of quantum mechanics. *Proc. R. Soc. A* 477, 20210600.
- Schlosshauer, M., and Fine, A. (2005). On Zurek's derivation of the Born rule. *Found. Phys.* 35, 197–213.
- Sebens, C. T., and Carroll, S. M. (2018). Self-locating uncertainty and the origin of probability in Everettian quantum mechanics. *Brit. J. Phil. Sci.* 69(1), 25–74.
- Vaidman, L. (2012). Probability in the many-worlds interpretation of quantum mechanics. In Y. Ben-Menahem and M. Hemmo (eds.), *Probability in Physics*, Springer, 299–311.
- Wallace, D. (2012). *The Emergent Multiverse*. Oxford University Press, §5.8.1.
- Zurek, W. H. (2005). Probabilities from entanglement, Born's rule $p_k=|\psi_k|^2$ from envariance. *Phys. Rev. A* 71, 052105.
- Framework: `versions/v0.6-prose.md` §§7–9, App. A (C9, C15, C16, C24); `versions/v0.7-outline.md` App. A (C33, C36); `papers/B-ge2-minimal-toy.md`; `papers/Vstar-extend-vs-not.md`.
