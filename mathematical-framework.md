Mathematically speaking, our goals are to create a precise mathematical description of the observer $O$ and the equations of its evolution through Observer space. 

We begin with the following definitions:

| Name | Symbol | What it is |
|---|---|---|
| observer | $O=j_p^\infty$ | Infinite jet of a real-analytic Lorentzian metric $g$ at a point $p$. The observer may also be identified as the *local germ* of the metric at $p$.  |
| oriented observer | $O^u = (O, u)$ | an observer $O$ paired with a unit vector $u$ that specifies the direction of motion of the observer. |
| orientation in spacetime | $u$ | the *orientation* of an oriented observer. It is a spacetime vector that lives in $T_pM$ |
| orientation in observer space | $V = Lift(u)$ | If $Obs$ has a tangent space [1], then a path $\gamma(\tau)$ on $Obs$ has a tangent $V = \gamma'(\tau)$. That $V$ is the lift of $u$. It is a vector in $T_OObs$. |
| Observer space | $\mathrm{Obs}$ | the set of all possible local germs |
| Spacetime | $M$ | A real-analytic Lorentzian 4-manifold imbued with metric, any global topology, connected but not necessarily simply connected. Distinct spacetimes may have distinct fundamental group. |
| World | $W(O) = (M, p)$ | a spacetime $M$ plus a point $p$ in $M$ at which the observer is located |
| anchor point, a.k.a. point of view | $p_0$ | Given $W(O) = (M, p)$, $p$ is referred to as the observer's *anchor point* in $M$ for the world $W$. It may also be referred to as the observer's *point of view* on the world. |
| World Ensemble of an observer | $E_W(O)$ | The set of all worlds $W = (M, p)$ such that the germ at $p$ equals $O$. Note that the same spacetime $M$ may appear multiple times in $E$ if there are multiple distinct $p$ in $M$ such that the germ at $p$ equals $O$. |
| Spacetime Ensemble of an observer | $E_M(O)$ | The same as $E_W(O)$, except that each world $W = (M, p)$ has been replaced by its corresponding spacetime $M$. If $N$ worlds in $E_W(O)$ are characterized by the same spacetime $M$, then that $M$ occurs $N$ times in $E_M(O)$. [2] |
| Geodesic in spacetime | $\sigma:I\to M$ | A causal geodesic of $M$ parameterized by proper time $\tau$. A path *through spacetime* |
| Curve in observer space | $\gamma:I\to\mathrm{Obs}$ | $\tau\mapsto j_p^\infty(\tau)$. A path *through observer space* |
| sibling points | | Consider an observer $O$ with world ensemble $E$ and $W = (M,p_0)$ in $E$. If $O$ exists at multiple distinct points $p_i$ in $M$, with each $p_i$ distinct from $p_0$, each $p_i$ is said to be a *sibling point* to the anchor point, $p_0$. |
| compatibility | $O_i \Leftrightarrow O_j$ | Consider two distinct, non-oriented observers $O_i$ and $O_j$. $O_j$ is considered an *allowable future state* of $O_i$ if there exists at least one spacetime $M$ such that $O_i$ can evolve into $O_j$ via a geodesic in $M$. More specifically, there exists at least one spacetime $M$, with two points $p_1$ and $p_2$ in $M$, such that the germ at $p_1$ is $O_i$ and the germ at $p_2$ is $O_j$, and there exists at least one finite geodesic $\sigma$ that connects $p_1$ to $p_2$. If $O_i$ is an allowed future state of $O_j$ and if the reverse is also true, $O_j$ is an allowable future state of $O_i$, then we say $O_i$ and $O_j$ are compatible observers. |
| $S(M)$ || the set of germs that occur in the manifold $M$|

## The equations of motion through observer space: Initial Postulates

We considered several sets of postulates from which to derive the equations of motion through Obs. The primary tension under consideration is whether world switching is allowed. In a type-(i) paradigm, the answer is no: the observer must stay in one world. In a type-(ii) paradigm, the answer is yes: the observer is allowed to switch worlds. 

The framework we currently favor is a type-(ii) framework, with an added continuity condition, which we call *Continuous World Switching*.

### Continuous World Switching

We allow the traveling observer to switch from one spacetime (one world) to another: the observer can travel an infinitesimal distance from $O_i$ to $O_j$ along a geodesic in one world $W_1$, then from $O_j$ to $O_k$ along a geodesic in a different world, $W_2$. In other words, allowed paths are those that are piecewise geodesic lifts. We require that the path through observer space must be $C^\infty$ and that orientation cannot be changed. 

We believe $C^\infty$ plus piecewise geodesic lifts is strong: at a switch the two lifts must match in Obs to infinite order in $\tau$, not just share a germ. This may force fewer switches than one might initially imagine from EKT.

#### Alternative: Direction Switching

Alternative rule: the direction can be changed, but only infinitesimally, and any change must be $C^\infty$. This is not our current paradigm, but may be considered if we find that we need the flexibility.

### Branches under Continuous World Switching

Equal probability needs a definite notion of branch. Until that is fixed, the Equal Probability Postulate has nothing to act on.

**Allowed continuation at $O$.** Fix an oriented observer $O^u$ (or a non-oriented $O$ together with a choice of $u$). An *allowed continuation* at $O$ is a germ of a path $\gamma:[0,\varepsilon)\to\mathrm{Obs}$ with $\gamma(0)=O$ such that:
1. $\gamma$ is $C^\infty$ as a map into $\mathrm{Obs}$ (once a notion of smoothness on path space or on charts is chosen; see tangent-space options in Goals);
2. $\gamma$ is a piecewise geodesic lift in the sense of Continuous World Switching: on each piece it is the Obs-lift of a causal geodesic in some world, and world switches are allowed at shared germs;
3. orientation is preserved: $V(\tau)=\mathrm{Lift}(u(\tau))$ does not jump (no Direction Switching).

**Branch set.** Two allowed continuations are *equivalent* if they agree to infinite order in $\tau$ at $0$ (same jet of the Obs-path), or, weaker working option, if they agree after reparameterization on some common initial interval. The *branch set* $B(O)$ (or $B(O^u)$) is the set of equivalence classes of allowed continuations at $O$.

A *branch point* is an $O$ at which $|B(O)|\ge 2$. The Equal Probability Postulate applies only at branch points, and only when $B(O)$ is discrete (finite or countable). It does not assign weight to a continuum of directions.

**What $B(O)$ is not.** $B(O)$ is not the Fermi-slice neighborhood of $O$ (typically a continuum). It is not $E_M(O)$ or $E_W(O)$. It is not a delayed fork of one analytic geodesic lift in a single world (still forbidden by analyticity inside one $M$). A split in $B(O)$ is a split among allowed world-switching continuations in $\mathrm{Obs}$.

**Stress test: EKT billiard.** Let $O_i$ be an early oriented observer for whom red and blue worlds still share germs, and let $O^*$ be a candidate break point where some $M$ leaves the ensemble. Questions to answer before trusting equal weight:
1. Is $O^*$ a branch point under the definition above? That is, are there at least two inequivalent allowed continuations at $O^*$?
2. Is $B(O^*)$ finite (e.g. $\{O_{\mathrm{red}}, O_{\mathrm{blue}}\}$), countably infinite, or a continuum?
3. Does the strong $C^\infty$ matching condition at switches collapse the EKT cartoon to a single continuation, force a discrete split, or leave a continuum?
4. If $B(O^*)$ is countably infinite, what exhaustion or limit is used so that equal weight still yields well-defined ratios (see Goals)?

Until (1)–(2) are settled for the billiard, do not treat equal probability as producing Born weights in spacetime.

### Equal Probability Postulate

In addition to the above postulates, we will also add the equal probability postulate: that branch points in Observer space are followed with equal probability. We envision that these branches will be discrete and countable. Finite would be nice, although I suspect they will be (at least in some cases) infinite. For the EPP to be tractable, we would probably require the various infinities to cancel in some manner, something that might relate in some fashion to its countability.

Alternative form of the EPP would be that the probability of a branch is proportional to the number of Worlds in the Ensemble associated with the branch. We might even consider that the regular EPP and the alternative EPP will yield the same answer. Although this is mentioned as nothing more than simple speculation at this point. 

### Goals

Our hope is that given the above paradigm, we can -- counterintuitively, one might say -- prove that the Born rule is an unavoidable result: not in observer space of course, but in spacetime.

Likewise, we can hope for a second, perhaps even more surprising result, which would be to derive Einstein's field equations. Note that we have deliberately not assumed Einstein's field equations on the spacetime manifolds $M$. Adding those equations by hand to our spacetime manifolds would not be entirely unreasonable, and we might consider doing that if we discover that we must. 

In addition to Born Rule and Einstein field equations, we may hope to derive equations of motion through Observer space. At this point, I have no idea what form those might take. It is worth noting that we have not yet imbued Observer space with a tangent space. We might consider three options: (1) no tangent space — work with path space and $C^\infty$ curves only; $V=\mathrm{Lift}(u)$ stays informal; (2) Fermi $k$-jets or infinite jets — charts, ordinary or Fréchet tangent spaces; (3) topology only (Fermi-slice) — neighborhoods without $T_O$. We will need to consider what CWS actually needs: matching jets in $\tau$ may need (1) or (2); equal branch weight needs discrete branches more than it needs a tangent space.

### Changes to these postulates

If we discover that we need to alter any of these initial postulates, then we will do so, but we will do so consciously and deliberately.

## Notes

[1] Note: we have not yet imbued $Obs$ with a tangent space. How best to do this is an open question. 

[2] When we wish to compare the Ensembles $E_i$ and $E_j$ of two distinct observers $O_i$ and $O_j$, it will likely be more interesting to compare spacetime ensembles than world ensembles, given that the intersection of world ensembles $E_i$ and $E_j$ will be trivially empty because they are not occupying the same points $p$.
