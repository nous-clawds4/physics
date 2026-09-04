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

We considered several sets of postulates for the equations of motion through Obs. The primary tension under consideration is whether world switching is allowed. In a type-(i) paradigm, the answer is no: the observer must stay in one world. In a type-(ii) paradigm, the answer is yes: the observer is allowed to switch worlds. 

The framework we currently favor is a type-(ii) framework, with an added continuity condition, which we call *Continuous World Switching*.

### Continuous World Switching

We allow the traveling observer to switch from one spacetime (one world) to another: the observer can travel an infinitesimal distance from $O_i$ to $O_j$ along a geodesic in one world $W_z$, then from $O_j$ to $O_k$ along a geodesic in a different world, $W_z$. In other words, allowed paths are those that are piecewise geodesic lifts. We require that the path through observer space must be $C-\infty$ and that orientation cannot be changed. (Alternative rule: it can be changed, but only infinitesimally, and any change must be $C-\infty$.)

Our hope is that we can assume equal probability at branch points in Obs, and from there, we can -- counterintuitively, I might add -- prove that Born rule is an unavoidable result: not in observer space of course, but in spacetime.

[1] Note: we have not yet imbued $Obs$ with a tangent space. How best to do this is an open question.

[2] When we wish to compare the Ensembles $E_i$ and $E_j$ of two distinct observers $O_i$ and $O_j$, it will likely be more interesting to compare spacetime ensembles than world ensembles, given that the intersection of world ensembles $E_i$ and $E_j$ will be trivially empty because they are not occupying the same points $p$.
