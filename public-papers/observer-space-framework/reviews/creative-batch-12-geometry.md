# Geometry quick verdict: creative batch 12 (#366) — do not merge

**Read at:** #366 head `dbcfc18` (`notes/creative/batch-12.md`), main `e41412b`.

**Record type:** rough review. It applies nothing and is neutral on David's open calls. This is exploration under the rulings of 3:14, 3:53, 4:16 and 4:17 PM ET. It addresses structure only and assigns no probabilities. All arguments are sketches; the explicit Misner computation below is Geometry's own. **(V #n)** means verified in PR #n; **(U)** means from memory and not checked.

**Verdicts.**
1. **Survival.** Confirmed for Misner by explicit computation. Every timelike geodesic that does not pass through the boost's fixed point continues in exactly one of the two extensions. The ones through the fixed point end in both. Taub–NUT is (U).
2. **"Same germ ⇒ same reply".** False for exactly the replies of interest. Returns through the geon use non-trivial topology ($\Gamma$), which the germ does not fix. So record and germ partitions *cross*; neither is a coarsening of the other.
3. **Countability.** Countable classes are fine. The symmetry continuum is milder than stated: it needs the *initial data* to be invariant under a continuous subgroup. A flat torus's residual translations do not smear solutions for fixed data.
4. **Non-Hausdorff union.** In the Misner union no single geodesic bifurcates, so the motion still does not fork there. A general non-Hausdorff "branching" host does fork motion at a codimension-1 surface. But under analyticity the branches share germs along the path, and in the smooth case the union of compatible hosts is just #346's structure relabelled.
5. **Flag.** Nothing flagged as a mechanism. (4) is at most a reformulation note, low priority.

## (1) Misner: who survives?

Explicit sketch. Use null coordinates $U=t-x$, $V=t+x$ on $\mathbb R^{1,1}$. A boost acts as $(U,V)\mapsto(e^{-a}U,e^{a}V)$.

- **The spaces.** Misner's chronological region is $P=\{U<0,V<0\}/\text{boost}$; its horizon lies to the future. The two analytic extensions are $A=\{U<0\}/\text{boost}$ and $B=\{V<0\}/\text{boost}$. The boost acts properly on each half-plane (Misner 1967; Hawking–Ellis §5.8 (U)).
- **Geodesics in $P$.** A future timelike geodesic in $P$ lifts to a line $U=U_0+\alpha s$, $V=V_0+\beta s$ with $\alpha,\beta>0$. It reaches $V=0$ at $s_V=-V_0/\beta$ and $U=0$ at $s_U=-U_0/\alpha$.
  - **$s_V<s_U$.** The line crosses $V=0$ at a point with $U<0$, which lies in $A$, so it continues in $A$. In $B$, every lift approaches $V=0$, which is not in $B$, at finite parameter, so it is incomplete in $B$.
  - **$s_U<s_V$.** The same holds with $A$ and $B$ swapped.
  - **$s_U=s_V$.** The line passes through the origin, which is in neither extension, so it is incomplete in both. These lines form a codimension-1, meagre set of data (#336 (a)).
- **Conclusion.** The batch's claim holds for timelike observers, not only null geodesics. Every generic observer survives in exactly one extension. Which one is fixed by its own data (the sign of $s_U-s_V$), so it is determined, not forked.
- **Taub–NUT.** The analogous claim is plausible, but (U). Chruściel–Isenberg (V #332) establishes only the non-isometry.
- **Survival in all extensions.** The batch is right on both cases. Analytic: impossible, because two analytic extensions that both continue $\gamma$ share its germ there. Smooth: possible, but only through off-path differences, which form a continuum.

## (2) Outcome versus branch

The batch says the germ at $\gamma(s)$ fixes the local extension, so same germ means same reply. That holds only if the reply's causal past lies inside a region the germ fixes *as a subset of the host*.

$P(O)$ is the abstract simply connected patch. The germ fixes the cover, not the quotient (L27, L28; #355 (c)). A reply through the geon's CTC uses a non-trivial loop: in Misner, the CTCs are the boost quotient itself. Its timing and content depend on $\Gamma$, so two hosts with equal germs at $\gamma(s)$ and different $\Gamma$ give different replies.

The record partition is therefore **not** a coarsening of the germ partition; the two cross. Cases (a)–(c) still stand. Add:
- **(d) Same germ, different reply** (different $\Gamma$).

With (d) added, the injectivity condition in (ii) becomes a condition on pairs (extension, $\Gamma$), not on extensions alone.

## (3) Countability of self-consistent solutions

- **Discrete classes.** Traversal or winding classes are discrete, and so countable. Isolation within a class needs transversality of the specific round-trip map. "Generic $F$" is genericity in some space of maps or hosts, which is a topology, not a measure. The actual EKT map is (U).
- **The symmetry trap is narrower than stated.** A continuous isometry $h$ of the host maps a solution with initial data $d$ to a solution with data $hd$. For **fixed** data, solutions smear into a continuum only under the stabiliser of $d$.
  - The flat-torus residual translations (the centraliser of $\Gamma$, $U(1)^n$) move the ball's initial position. So they do not smear solutions for fixed data.
  - Rotations about an axis smear solutions only for on-axis data. That is special, codimension $\ge1$, data.
  - Caveat: EKT's "dangerous" head-on trajectories may be exactly such symmetric data (U).
  - Crystal covers, which have discrete Isom, avoid the trap entirely.
- **Seriousness.** Low for generic data. Real for symmetric set-ups and for continuous internal degrees of freedom (spin, inelasticity), which are (U).

## (4) The non-Hausdorff union of extensions

- **Misner union.** $A\cup_P B$ is non-Hausdorff (Hawking–Ellis §5.8 (U)). But by (1), each timelike geodesic in $P$ has a limit in exactly one of $A$ or $B$. Its lifts in the other extension approach a missing boundary and converge to nothing.
  - The non-separated pairs are reached only by *sequences* of points (approaching the boost's fixed point under different boost lifts), not along a single geodesic.
  - So **no geodesic bifurcates** in the Misner union, and motion still does not fork. This is Geometry's computation, a sketch.
- **General non-Hausdorff "branching" hosts.** These are of line-with-two-origins type across a spacelike hypersurface (Hájíček 1971; McCabe 2005; Luc–Placek 2020 (U)). There, every geodesic crossing the branching surface has one continuation in each branch.
  - That is a genuine fork of motion at a **codimension-1** surface, so it is hit in the typical case.
  - The number of continuations is the number of branches, which is discrete.
  - It breaks H4 (the manifold, i.e. the Hausdorff axiom) and nothing else. It is a one-word tweak with literature behind it.
  - Hazard: Everett framing (#332 N1).
- **Does the germ fail to determine the branch?**
  - *Under the analytic lock:* the two branches continue the same trunk germ analytically. So they agree near the branching surface, and their germs along $\gamma$ are identical until any later Cauchy horizon. The fork is then invisible in $V$, the same pattern as #349 (A). Where branches *do* differ (beyond a Cauchy horizon), the Misner computation shows that single geodesics do not bifurcate.
  - *Smooth case:* branches can differ right after the surface, so the germ fails to determine the branch. But the non-Hausdorff union of the compatible hosts is just #346's ensemble, glued along the agreement region. The fork is "which compatible Hausdorff host", and the count is decided by the data class: a continuum for smooth data. Dropping the Hausdorff axiom adds no discreteness by itself.
- **Flag.** Not promising as a mechanism. It is possibly worth a short reformulation note ("the ensemble as one non-Hausdorff host") if the Lead wants the picture. Low priority.

**Citations (U):** Misner 1967; Hawking–Ellis §5.8; the Taub–NUT geodesic dichotomy; the specifics of the EKT map; Hájíček 1971; Luc–Placek 2020. McCabe 2005 is cited in #332 N1 (V-text per #332). (V #332): Chruściel–Isenberg 1993. In-repo: #336, #346, #349, #355, #364.
