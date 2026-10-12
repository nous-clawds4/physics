# Geometry quick verdict: creative batch 06 (#348), do not merge

**Read at:** #348 head `68396c6` (`notes/creative/batch-06.md`), main `e41412b`. **Record type:** rough review. It applies nothing, and it is neutral on David's open calls (exploration under the 3:14 PM ET relaxation and the 3:19 PM ET reframing). The arguments are sketches, not proofs. **(U)** marks claims from memory, not checked.

**Verdicts.**
- **(A) L24.** The construction exists, and near-miss limits pick exactly the two continuations for $e=2$. That pick is a continuity rule, not something forced. For $e\ge3$ the near-miss limits give 2 continuations, not $e$.
- **(A), main new finding.** With the metric pulled back from a smooth base, both branches have **identical observer-state sequences**. They differ only in *where the path has gaps*. So the fork is invisible in $V$, in the nested-prefix sense.
- **(B) L25.** For a point observer, hitting is dense and meagre (confirmed). For an extended observer, hitting is full once $r_0$ reaches the lattice covering radius, at the #336 (f) costs. Recasting the fork as two hosts is not a relabelling: it changes the branch data, and the extra hosts already sit in a continuum $E(O)$.
- **Not flagged** for a full note.

## (A) L24: three-sheeted cover, one fork

- **Cone angles: correct.** Over $0$ the ramified point $x_{12}$ has total angle $4\pi$ (sheets 1 and 2), and $x_3$ on sheet 3 is an ordinary $2\pi$ point. A path aimed at $0$ on sheet 3 just continues straight; only sheets 1 and 2 meet the apex. Likewise over $a$ with $y_{23}$ and $y_1$.
- **The minimising continuations form a continuum (confirmed).** On a cone of angle $\Theta>2\pi$, an outgoing direction continues a locally shortest path if it makes an angle $\ge\pi$ with the incoming direction on both sides. Those directions form an arc of length $\Theta-2\pi$, which is $2\pi$ at a $4\pi$ point (standard for cones; (U) as a citation).
- **Near-miss limits pick exactly the two endpoints of that arc.** Take base lines passing just to the left or right of $0$. They lift to straight lines, and their lifts end on sheets that differ by the local monodromy $\sigma_0$: one stays on sheet 1, the other goes to $\sigma_0(1)=2$. As the miss distance goes to 0, they converge (Hausdorff, on compact sets) to the two continuations at angle exactly $\pi$ on the left and on the right. These are the planar straight line on sheet 1 and on sheet 2, which are the two lifts of $\beta$. So for $e=2$ the lift rule and the near-miss rule agree.
  - It is still a **rule**: "the continuation set is the set of limits of nearby geodesics" selects 2 points from an arc. It is motivated by continuity of the geodesic flow (a closure of the flow graph, Filippov-like), not tuned to the target.
- **$e\ge3$: the two rules disagree.** At a point of ramification index $k$ (cone angle $2\pi k$, local monodromy a $k$-cycle), there are $k$ lifts of $\beta$, at angles $\pi,3\pi,\dots,(2k-1)\pi$ from the incoming direction. But a plane has only two sides, so only the two extreme ones ($\pi$ and $2\pi k-\pi$) are near-miss limits. The $k-2$ middle lifts are limits of nothing nearby. So "a whole number fixed by topology" is $k$ under the lift rule and 2 under the continuity rule. Which one to use is a choice. Only the local ramification index matters; the number of sheets $n$ plays no role.
- **Ill-posed term.** There is no germ at the apex, so the observer state at $\tau_0$ is undefined. The batch says this too. The data that hits $\Sigma$ is a meagre, codimension-1 set (#336 (a)).
- **Main new finding: the fork is invisible in $V$.** $g=-dt^2+dz^2+\pi^*h$ is pulled back from the analytic base, so off $\Sigma$ the projection is a local isometry. The germ at any point of $S$, together with $u$, then equals the base germ and velocity at its image. Both branches project to the same $\beta$, so their state sequences are **identical** at every non-gap time, sheet labels notwithstanding. They differ only in the *gap set*: the sheet-2 branch has a gap at $y_{23}$ (and forks again), while the sheet-1 branch passes $y_1$ smoothly. In $V$ this is the nested-prefix difference (#346 §1): where the path stops or gaps, not which states it visits. If $h$ is flat, every state is the same flat germ under #324. The batch's "difference first shows at the second seam" is right, but what shows is a gap, not a different state. For the states themselves to differ, the metric on $S$ must not be pulled back from $B$, and then the lift rule is undefined.

## (B) L25: lattice of seams

- **Point observer: dense and meagre (confirmed).** In the product host a geodesic projects to a straight line in $B$, and it hits a seam exactly when that line passes through a lattice point.
  - From any base point the directions to lattice points are **dense**: every open cone contains arbitrarily large balls, and so contains lattice points.
  - The hitting set is a countable union of closed, nowhere-dense sets (one family of lines per lattice point), so it is meagre (#336 (a), (d)).
  - The data with zero base velocity (sitting still in $B$) is closed and nowhere dense, and it never hits unless it starts on a seam.
  - So the batch's B1 claim holds for the lattice, with no measure used.
- **Extended observer: full above the covering radius.** The square lattice $\ell\mathbb Z^2$ has covering radius $\ell/\sqrt2$, and its widest lattice-free strip has width $\ell$ (axis-aligned) (elementary; (U) as a citation).
  - $r_0\ge\ell/\sqrt2$: every tube contains a seam at every base point, so the hitting set is all data.
  - $\ell/2<r_0<\ell/\sqrt2$: every *infinite* strip hits, but a finite stretch may not.
  - $r_0<\ell/2$: the hitting set is open but not full, since axis-aligned slabs miss.
  - For a general lattice the thresholds are its covering radius and its lattice width.
  - The costs are those of #336 (f): a scale, now pegged to $\ell$ by a factor that is still chosen, and replacing the point-germ state with a tube. The fork "which piece is the observer" is a law of $R$ unless it is left unselected.
- **Is "compatible worlds" a relabelling? No.** The two continuations live in **one** host $M$, so this is an in-world fork. Cutting along a slit from $x_{12}$ does one of two things:
  - **Slit left open:** $M_k$ has boundary edges, so it is extendible, which conflicts with #320.
  - **Slit reglued with a permutation $\tau$:** the monodromy around $x_{12}$ becomes $\sigma_0\tau$. Choosing $\tau=\sigma_0^{-1}$ makes $x_{12}$ ordinary and moves the branching to the far end of the slit (at $a$ or at infinity). That is a different branched cover, with a different seam location and topology. It is inextendible and analytic off its seams, so it is a legitimate host.
  - Either way, $M_1$ and $M_2$ are genuinely different hosts, not relabelings of $M$. But they were already in $E(O)$: for a flat (or pulled-back) germ, $E(O)$ contains every compatible host, a continuum. So the count 2 does not carry over from $M$'s fork to the ensemble. Picking out $\{M_1,M_2\}$ is an after-the-fact selection.

**Citations.** The cone-geodesic arc, the lattice covering radius and width, and the Riemann existence theorem (batch's own (U)) are standard but not checked here (U). In-repo: #320, #324, #336, #338, #344, #346.
