# Geometry quick verdict: creative batch 03 (#340) — do not merge

**Read at:** #340 head `738674c` (`notes/creative/batch-03.md`), main `e41412b` (`papers/geodesic-lifts.md` §3). **Record type:** rough review; applies nothing; neutral on David's open calls. **Goal:** branching of ONE observer's motion on $, discrete, for an independent physical reason, with no smuggled measure. Per ledger L15, a set has to break a named hypothesis of Prop 3.2 or Cor 3.1.

**Ranking.** Set 2 > Set 1 > Set 3, the same order as the draft. **None is flagged for a full note.** Each set either moves the non-uniqueness into added data, which is a law of $R$ in disguise, or puts it where nothing is defined.

## 0. Is H1–H4 a faithful split?

**Mostly faithful, with two gaps.** The record's proof (geodesic-lifts §3): "Uniqueness of $\sigma_O$ is analytic ODE uniqueness on $P(O)$. Uniqueness of the germ of $g$ on $P(O)$ is Theorem A. The lift is Theorem 3. Local coincidence of all ensemble lifts is Corollary 3.1 plus the shared curvelet."

- H1 maps to Theorem A, and H3 to "analytic ODE uniqueness". The batch's gloss "Lipschitz suffices" is its own addition. It is correct (Picard–Lindelöf), but it is not in the record.
- H2 (the geodesic law) and H4 (a manifold with continuous $\tau$) are implicit in the record, not stated. Making them explicit is fair.
- **Gap 1.** The batch quote of Prop 3.2 is cut short without saying so. It drops the closing sentence: "In particular, geodesic evolution of one $O$ does not produce distinct analytic curves through $O$ that agree only at $\tau=0$."
- **Gap 2.** Cor 3.1 has its own hypothesis, and H1–H4 leave it out. Call it **H5**: the lifts are *analytic* curves in Obs (Theorem 3), so Theorem 2 of `papers/analytic-split.md` applies. The record states it as "they cannot agree on $[0,\tau_*]$ ... and disagree at some later $\tau$ while both lifts are still analytic." The batch's "or via a non-analytic curve in Obs" is the denial of H5. It should be named as such, because a law that keeps H1–H4 but produces non-analytic curves escapes Cor 3.1 and not Prop 3.2.
- The batch's reading of the §3 loophole matches the record. That loophole is a star meeting only at $\tau=0$, which "would be a different evolution law" that "is not written here".

## Set 1: Lattice geodesic ties (H3/H4)

**Rigorous?** No. On a graph there are no jets, germs, $P(O)$ or Theorem A, so H1 fails along with H4. The observer state and $V$ themselves become undefined (well-posedness principle), and the gauge quotient of #324 has no analogue.

**Defeats Prop 3.2?** Not for an initial-value law. The ties in the draft ("east-then-north ties with north-then-east"; longest chains in a causal set) belong to **two-point** problems, extremal paths between given endpoints. Free fall is an *initial-value* problem from $(p,u)$. On a regular lattice the straight continuation of a given direction is unique. Ties appear only once an endpoint is supplied, and the endpoint is added data that selects the branch. That is a law of $R$ in disguise.

**Where it breaks.**
- The network type is chosen, which is an LT2/TT2 burden.
- The number of tied paths grows combinatorially with length, so the continuum limit ℓ→0 has no finite count. This is the same divergence #338 found for Set 1 of batch 02.

**Gain.** It gives a discrete count, but of paths between endpoints, not of motions.

## Set 2: Ride the matter, fork at the degeneracies (H2)

**Rigorous?** Only where there is matter. In vacuum the Ricci tensor vanishes, so the field is undefined, which the draft itself flags. A Weyl-built replacement does not obviously exist. For Petrov type D the principal null directions span a timelike 2-plane, not a single timelike direction, so a boost freedom remains (standard Petrov classification; not re-checked).

**Defeats Prop 3.2?** Formally yes: it breaks H2, and $u$ is read off the jet, so it is no longer free data. That changes the observer-state definition, because $V$ loses its $u$ fibre. But for a perfect fluid the timelike Ricci eigenvector is the fluid velocity, and its eigenvalue is non-degenerate unless $\rho+p=0$. So the "degeneracies" sit where the matter vanishes or has $\rho+p=0$. There the field *stops being defined*. It does not split into a few branches.

**Where it breaks.**
- For a generic symmetric operator, eigenvalue coincidence has codimension 2 (the von Neumann–Wigner count; not re-checked). In 4-d the degeneracy set is therefore 2-dimensional, and integral curves generically miss it. That is #336 (a) again, and "almost every" would smuggle in a measure.
- Analytic line fields can continue analytically through a degeneracy. That has to be checked before any fork is claimed.
- The tie-break at a degeneracy is a rule choice, i.e. a law of $R$.

**Gain.** It has the best physical motivation, and the branching it gives is in motion. The cost is that branch points are undefined in vacuum and rarely hit where they are defined.

## Set 3: Self-force needs the acceleration (H2)

**Rigorous?** It is well-posed as a third-order ODE. But the state must carry the acceleration $a$, so the observer-state definition changes from $(j_\infty,u)$ to $(j_\infty,u,a)$. With that change the motion is unique again. Without it there is a 3-parameter continuum of continuations.

**Where it breaks.**
- The Abraham–Lorentz–Dirac equation (Dirac, *Proc. R. Soc. A* 167, 148 (1938)) has runaway and preaccelerating solutions. The standard cure is reduction of order (Landau–Lifshitz). Gralla, Harte and Wald (*Phys. Rev. D* 80, 024031 (2009)) derive the corrected motion perturbatively, where reduction of order is natural. That cure restores a second-order, unique law.
- The gravitational self-force (Mino, Sasaki, Tanaka, *Phys. Rev. D* 55, 3457 (1997); Quinn, Wald, *Phys. Rev. D* 56, 3381 (1997)) has a tail term that depends on the whole past worldline. The state would then need the past history, not just $a$.
- The framework's observer has no mass or charge, so self-force also adds a body.
- The continuum of initial accelerations is the "anything goes" end, and it is not discrete.

**Gain.** Its reason for breaking H2 is independent, but it gives no discreteness, and the physical cure kills the branching.

**Citations.** All outside citations are from memory, have not been re-checked this session, and are marked **unverified**: Dirac 1938; Mino–Sasaki–Tanaka 1997; Quinn–Wald 1997; Gralla–Harte–Wald 2009; von Neumann–Wigner; Petrov type D. In-repo: geodesic-lifts §3, #324, #336, #338.
