# MERW eigenvector and the Born litmus test: scoping note (options and costs only)

**Read at:** main `f920ca3` (`versions/v0.9-prose.md` §2, §8.2, §8.4, §9, §11, §12; C26, C33, C36); `notes/born-litmus-test.md` (L3) as merged in #248 (`001dde2`). **Record:** `reviews/born-rule-readiness.md` (§1.2; v0.9 refresh), `notes/zeno-mass-scoping.md`. **Status:** scoping only; no pick, no derivation, no law of $R$; nothing in `versions/` or the essays edited. **Scope (David's qualifier to the L3 answer, recorded in `notes/born-litmus-test.md`, "Scope and outcomes"):** LT1–LT4 apply only once a Born-type result is claimed. This note claims none, so nothing here passes or fails; each finding says what a future claim would have to show. Literature only as v0.9 cites it (Burda et al. 2009; Duda 2011; Faber 2024).

## (a) Which operator, and what an amplitude-like $\psi$ would need

"Amplitude-like" (LT1): $\psi$ superposes, evolves linearly and interferes (so it can cancel). Perron–Frobenius makes $\psi$ real, positive and unique for a nonnegative irreducible operator, with $\psi^2$ MERW's stationary density when the operator is the symmetric adjacency matrix of a finite connected graph, the only case Burda et al. (2009) treat (§9). Positivity excludes cancellation: $(a\psi_1+b\psi_2)^2\ge a^2\psi_1^2+b^2\psi_2^2$ for $a,b\ge0$.

| Candidate operator | Automatic | To be added | Possible source, not by hand |
|---|---|---|---|
| O1 Adjacency of the jet graph $(V,R)$ | Nothing: $V$ is uncountable and $R$ is directed | A measure on $V$ or a truncation (a named extra); a spectral theory | none identified |
| O2 Transfer operator on the worked rule's state graph (orbit, turning point, flag $a$; §8.2 item 7) | Nonnegative, finite under the (a)-restriction (C33) | Irreducibility. The graph is reducible (computed below), so no unique $\psi$ exists | A different $R$ (law of $R$) |
| O3 Symmetrised adjacency $\mathcal A+\mathcal A^{\!\top}$ (Burda et al. assume an undirected graph: a symmetric 0/1 adjacency, finite and connected) | Unique positive $\psi$ on a connected graph; MERW | Backward pairs in $R$ (open, §11) | Only if a law of $R$ supplies backward pairs |
| O4 EPP1 kernel $P_{ij}=\mathcal A_{ij}/d_i$ | Stochastic; the leading right vector is constant | — (no square arises; MERW is the $\psi$-transform of $\mathcal A$, not of $P$) | — |
| O5 Hermitian phase variant $H_{ij}=\mathcal A_{ij}e^{i\theta_{ij}}$, $\theta_{ji}=-\theta_{ij}$ | Real spectrum; complex $\psi$; cancellation is possible | Phases $\theta$, Hermiticity (backward pairs), and a composition law along histories | Jumps carry no $\tau$ (§8.2 item 2), so a jump phase has no lock-side source; a phase $\propto\tau$ needs a scale not in the lock; the path-integral route is out of scope (readiness §1.2) |

## (b) LT1–LT4: what a future claim would have to show, and what it waits on

| Test | Before any claim (the test does not apply yet) | Waits on | Pointers |
|---|---|---|---|
| LT1 Identity | A claim would have to exhibit an object that superposes, evolves linearly and interferes; O1–O4 supply no object that superposes or cancels (readiness §1.2) | Amplitude-like structure (readiness gap 6; no listed call); law of $R$ | §8.2 item 1; C36 |
| LT2 Prior inputs | A claim would have to meet the §8.4 motivation clause; no rule meets it now (C26) | Law of $R$ and slice; (M1)/(M2) (MERW is a long-path count, an (M2)-side object); (a)/(b) (countable graph under (a), C33; continuum without, C16) | §8.2 item 1; §8.4; §6.1 |
| LT3 Robustness | A claim would have to be robust to cut depth, classifier and later splitting; the first two are probed in (c); counts are not invariant under later splitting (readiness P7) | (M1)/(M2), completed versus cut; (Z-0)–(Z-v) where a cut meets accumulation | §8.3; §9; C13–C15, C36 |
| LT4 Novel prediction | A claim would have to give correct weights in a second, unrelated setup, or interference not put in; no setup exists to state this now | A measurement model ("same outcome"; readiness gap 5) and a law of $R$ | §4 "Measurement, informally"; §11 |

## (c) Cheap probes, run

R1–R3: operator O2 on the (a)-restricted rule from the $r=10$ periastron of $[10,20]$, uniform weight on length-$L$ walks from the root (C36's root count). R4: small graphs, O3 and O5. Enumeration, no sampling.

- **R1, the spectrum (LT1 and LT3).**
  - At $c=0.01$ (87,356 states, 29,119 orbits) the strongly connected components are exactly the 29,119 orbit 2-cycles; jumps are acyclic (C33). Spectral radius 1, multiplicity 29,119: no unique Perron vector, so **MERW's $\psi^2$ is undefined here**. The test does not apply yet; a future claim through O2 would first have to supply an $R$ with a unique leading eigenvector.
  - Walk counts grow polynomially: $\log_2(N_{2000}/N_{1000})=14.185$ (longest chain 14); $0.999$ at $c=0.1$ (3 orbits, chain 1).
- **R2, the long-path count (LT3, cut depth).**
  - $c=0.01$: the root's jump-arm share is 0.400, 0.381974, 0.381966, 0.308087, 0.137830, 0.011828, 0.005865 at $L=2$, 10, 20, 50, 100, 1000, 2000: near $1/\varphi^2=0.381966$ for $L\le20$, then toward 0. The walks' jump count concentrates on 14 (0.8931 at $L=200$; 0.9909 at $L=2000$).
  - $c=0.1$: jump share 0.000500 at $L=2000$; concentration on 1 jump (0.9995).
  - **A MERW- or count-based claim at this grain would not be robust (LT3): the count is not stable in $L$, and its limit is set by the longest chain, which depends on $c$.**
- **R3, the classifier (LT3).** `kr.classify` against `c33r.py`: one state differs (87,357 against 87,356); shares agree to 6 decimals, jump-count laws to 4 figures. **The computed shares are robust to the classifier, so such a claim would be too on this point.**
- **R4, composition on toys (LT1).** Two $P_4$ joined by an edge: $\psi$ has overlap 0.933865 with $(\psi_1+\psi_2)/\sqrt2$, a fixed symmetric sum. $P_4$ joined to $K_4$ localises, a toy analogue of the localisation Burda et al. (2009) show on weakly diluted lattices: $\psi^2$ mass on $P_4$ is 0.042369, then $5.68\times10^{-3}$, $7.60\times10^{-4}$, $1.02\times10^{-4}$ with 1–3 bridge vertices, winner-take-all rather than superposition. Disjoint $P_4\sqcup P_4$: degenerate, $\psi$ not unique. $C_4$ with flux $\theta=0,\pi/2,\pi$ (O5): $\mathrm{tr}\,H^4=32,24,16$; cancellation appears only once phases are supplied. A future LT1 claim through O3 would have to show superposition that these toys do not.

**Limits.** One unmotivated rule (C26), one instance; a walk-length cut, not proper time; dead ends drop out; without (a) (C16) the graph is a continuum. **Not run:** an O3 (symmetrised) census, minutes of compute, which needs backward pairs no rule supplies.

## FOR DAVID (neutral options; nothing edited)

**F-M1. "Hazard, not a route".** It appears in v0.9 §2 ("a named hazard for (M2), not a route taken"), §9 ("a hazard for (M2), not a Born claim"), §12's MERW row, and `reviews/born-rule-readiness.md` l.56 and refresh gap 6; C36's cell does not use it. Options: (i) keep; (ii) keep "hazard" and add "whether it could pass LT1–LT4 is scoped in `notes/merw-litmus-scoping.md`"; (iii) replace with "not adopted; its status against LT1–LT4 is open". (ii) and (iii) change firewall text and a hold-level reading.

**Costs.** O2: none to state, but a claim through it would first need a unique $\psi$, which (a) does not give (R1). O3: backward pairs (§11) and an irreducibility proof per $R$. O5: a lock-side phase source and a composition law (new theory).

## Questions for an outside critic

1. Is any irreducible $R$ compatible with strict alternation and the arrival flag (§8.2 items 2, 7), or does R1's block structure hold in general?
2. Is R2's $1/\varphi^2$ plateau a property of the rule, or a C36-type Fibonacci effect of the root orbit?
3. Once a claim through a Perron vector is made, does its positivity bear on LT1 at all, given that failure means the rule was put in by hand, or would only O5's hand-supplied phases count as an LT1 failure?
4. Does O3's symmetrisation count as a prior input in LT2's sense, or as tuning?
5. Is "robust to the classifier" (R3) the right reading of LT3's "grain", or is the grain here $L$, where R2 shows a claim at this grain would not be robust?

## Pins and scripts

- `/workspace/g249/merw_rule.py` `8ba694f70b4cba5b2e930e1e4e7fcf60a9b23f77d3e0c7c6f2238e61bb82d871` (R1–R3; args `c classifier`). It imports `g154/kr.py` `0432cc20` and `g168/c33r.py` `f9e9c31b` (definitions only).
- `/workspace/g249/merw_toy.py` `56b0366e14dbc3291ada56d95c040bdf7a0c727ca1c47dc5199b497d736a81eb` (R4).
- Python 3.13 (`/workspace/g128/venv`); on the shared machine, outside the repository.
