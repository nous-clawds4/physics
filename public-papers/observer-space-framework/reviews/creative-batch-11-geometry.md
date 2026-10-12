# Geometry quick verdict: creative batch 11 (#363) — do not merge

**Read at:** #363 head `729075a` (`notes/creative/batch-11.md`), main `e41412b`.

**Record type:** rough review. It applies nothing and is neutral on David's open calls. Exploration only, under the 4:16 PM ET relaxation of #352's conditions for geon hosts and David's 4:17 PM ET hypothesis. Structure only: no probabilities, no counting. All arguments are sketches.

**Citation marks:** **(V)** checked against the abstract this session; **(V #n)** verified in that PR; **(U)** from memory, unchecked.

**Verdicts.**
- **(a)** Well-posed and homotopy-invariant. The type is the time-orientation character of the closed-up loop. Type O returns are exactly the returns that close in the time-orientable double cover.
- **(b)** Type O classes exist topologically whenever the time-orientation character has a non-trivial kernel, for example any $a^2$. Whether real Hadley geons have *causal* Type O returns is unchecked.
- **(c)** Essentially yes: in the known benign examples a linear field gives no multiplicity, and EKT-type multiplicity comes from interaction.
- **(d)** Along the beacon's path the extensions differ only as end versus continue. **New problem:** no reply from beyond a Cauchy horizon reaches an observer still inside $D^+(S)$, so the observer must itself be beyond the horizon. Its own path then meets the same non-uniqueness.

**Not flagged** for a full note.

## (a) Type O / Type F classification

**The definitions match.** Orient the null curve $c$ future-pointing at its emission end $\gamma(t_e)$, using the orientation of $U$, and transport that along $c$.
- If $c$ is future-pointing in its direction of travel at $\gamma(s)$, it arrives from the past. That is a genuine reception, Type O.
- If it is past-pointing there, then the reversed curve leaves $\gamma(s)$ future-pointing, so both ends are emissions (equivalently, both are receptions if you start from the other end). That is Type F.

The batch's description agrees with this.

**Homotopy invariance.** Close $c$ with the segment of $\gamma$ between $t_e$ and $s$. That segment lies in the time-oriented region $U$ and contributes no flip. The type is then the value of the time-orientation character $w:\pi_1(M,p)\to\mathbb Z/2$ on the loop. This is the first Stiefel–Whitney class of the time-orientation line bundle (standard; (U) as a citation). So the type depends only on the homotopy class of $c$ relative to its endpoints, and the classification is well-posed per class. It does not depend on the beacon's dynamics.

**Consequence.** Type O loops are exactly those whose lift to the time-orientable double cover closes up. So "keep only Type O" is, for the record, the same as working in the double cover. That is #361's repair (a) seen from below, not a separate repair.

## (b) Do real Hadley geons give Type O returns?

Hadley 1997/2000 are as per #362; I have not re-checked them here.

**Topologically, yes.** $\ker w$ is an index-2 subgroup of $\pi_1$.
- If $a$ reverses orientation, then $a^2\in\ker w$. That loop goes twice around the flip and passes through $G$.
- Any other element of $\ker w$ whose loops enter $G$ also qualifies.
- So Type O classes through $G$ exist whenever $\pi_1$ has more than the single reversing class $\mathbb Z/2$. A geon with $\pi_1\cong\mathbb Z/2$ has *no* non-trivial Type O class.

**Geometrically, unchecked.** It is open whether such a class is realised by a causal (null) curve from $\gamma(t_e)$ to $\gamma(s)$, and whether that curve meets the CTC part of $G$. This needs Hadley's explicit construction.

## (c) L36: does multiplicity need an interacting signal?

**Source (V).** Friedman, Morris, Novikov, Echeverria, Klinkhammer, Thorne, Yurtsever, "Cauchy problem in spacetimes with closed timelike curves", *Phys. Rev. D* 42, 1915 (1990). What the abstract says:
- For a massless scalar field, self-consistency constrains initial data posed to the future of the Cauchy horizon, but only mildly in the traversable-wormhole family. Such spacetimes are called "benign".
- Benign spacetimes are not generic among flat, closed 2-dimensional spacetimes. Stable, asymptotically flat 4-d wormhole spacetimes are likely benign.
- The authors "suspect that these types of self-consistency behavior … are typical for noninteracting (linearly superposing), classical fields". By contrast, interacting systems (the billiard ball) can have unique, multiple or no self-consistent solutions.

**Uniqueness.** The abstract does not itself state uniqueness for the linear field. That is in Friedman–Morris's existence and uniqueness work (U).

**Conclusion.** Essentially yes. In known well-behaved examples, linear fields do not give EKT-type multiplicity; interaction does. Some non-benign (e.g. 1+1 flat, Misner-type) cases misbehave even for linear fields, through constraints or non-existence; whether they give non-uniqueness is (U). An interacting beacon is a body or a non-linear field, which is matter beyond the point observer, as the batch says.

## (d) L37: do the extensions differ along the beacon's path?

**End versus continue: confirmed.** The extensions are non-isometric (Chruściel–Isenberg 1993 (V #332)). For Misner and Taub–NUT, as I recall (U; Hawking–Ellis §5.8), each extension makes one family of null geodesics crossing the horizon complete and leaves the other family incomplete. A given beacon geodesic therefore continues in one extension and ends in the other. That is a prefix for the signal, as the batch says, and not a two-way fork in which both continue.

**New problem (sketch): the reply cannot reach an observer still in $D^+(S)$.** Let $S$ be a slice before the geon and $H=H^+(S)$.
- For $q\in D^+(S)$, $J^-(q)\cap J^+(S)\subset D^+(S)$ (standard; Hawking–Ellis §6.5 (U)). The CTC region lies beyond $H$, in $J^+(S)\setminus D^+(S)$, so no point there is in $J^-(q)$.
- Hence the reception point $\gamma(s)$ must itself lie beyond $H$, outside $D^+(S)$. The observer's own worldline then crosses $H$ or lies beyond it, in a region whose geometry depends on the extension.
- In some extensions the observer's own geodesic may be the incomplete one. That makes a nested prefix *for the observer*, which is the case the batch says it escapes.
- Even where both extensions continue the observer, its germ beyond $H$ may differ between them. In that case the split is in the observer's motion data, not only in the record.

This applies equally to L36. Under David's hypothesis, a measurement always happens beyond the observer's own Cauchy horizon.

**Citations.** (V) Friedman et al. 1990 (abstract). (V #332) Chruściel–Isenberg 1993. (U) the Stiefel–Whitney framing; Friedman–Morris on uniqueness; Hawking–Ellis §§5.8, 6.5. Hadley as per #362. In-repo: #346, #352, #361.
