# Sheets: does a typical curvelet hit the branch seam? (proposal note, do not merge)

**Status.** Narrow follow-up to Set 1 of `creative/batch-01.md` (#333), approved by the Physics Lead after the Geometry verdict in #334. Nothing adopted. Sets 2 and 3 and all `versions/` drafts are untouched. Neutral on topology T0–T4, the throat convention, the law of $R$, (M1) and (A).

**Setting.** A host is $(M,g,\Sigma)$: $\Sigma\subset M$ is a closed embedded 2-surface in the 4-manifold $M$, $g$ is real-analytic on $M\setminus\Sigma$, and near $\Sigma$ the metric is an $n$-fold branched cover (cone angle $2\pi n$) or a conical defect (Vilenkin, *Phys. Rev. D* 23, 852 (1981); exact exterior: Hiscock, *Phys. Rev. D* 31, 3288 (1985); Gott, *Astrophys. J.* 288, 422 (1985)). States are germs plus $u$ at $p\notin\Sigma$. By `papers/geodesic-lifts.md` Prop 3.2/Thm 3 the curvelet is unique off $\Sigma$, and continuation along one path has no monodromy, so motion can branch only where the curvelet **meets** $\Sigma$ (#334). The question: is there a reason, not tuned to the Born target, that a typical curvelet meets $\Sigma$?

**Phase space used.** Fix one host. Let $U^+M'$ be the future unit timelike bundle over $M'=M\setminus\Sigma$, a 7-manifold, with geodesic flow $\phi_t$. The hitting set is $H=\{(p,u): \phi_t(p,u)\to\Sigma \text{ for some finite } t\}$. This works inside one host's tangent bundle and uses its manifold topology; it adopts no topology on $V$.

## (a) Genericity. Killed as a source of typical hits (proved)

**Claim.** $H$ is a countable union of images of smooth maps from 6-manifolds into the 7-manifold $U^+M'$. Hence (i) $H$ is meagre (first category) with empty interior, and (ii) $H$ is null for every measure that is absolutely continuous with respect to Lebesgue measure in charts.

**Proof sketch.** Geodesics that reach $\Sigma$ are the backward flow-outs of their limiting data on $\Sigma$. These data form a bundle $B$ over $\Sigma$ with fibre the 3-dimensional set of incoming unit timelike directions, so $\dim B=2+3=5$. The map $B\times(0,\infty)\to U^+M'$, $(b,t)\mapsto\phi_{-t}(b)$, is smooth on the domain where it is defined, and that domain is a 6-manifold. $B$ is σ-compact, so $H$ is a countable union of images of compact sets under a smooth map from a lower-dimensional manifold. Each such image is closed and nowhere dense, which gives (i) by Baire; Sard's theorem, or simply the lower dimension, gives (ii). In plain terms, $H$ has codimension 1 in the data. This is the "$1+2<4$" count of #334, sharpened: hits are not "far" (codimension 1, a wall in phase space), but they are atypical.

**Measure flag.** Statement (ii) uses a measure class. Lebesgue class is the smooth structure's own, but choosing it is still a choice, and "almost every" would smuggle it in. Statement (i) is measure-free and uses only the manifold topology of $U^+M'$, so the kill rests on (i). Neither statement says how $H$ sits inside $V$ across hosts; that would need a topology on $V$, which is not adopted.

## (b) Causal type of the seam. Killed (proved)

The count in (a) does not depend on the causal type of $\Sigma$. For timelike $\Sigma$ (a cosmic-string worldsheet), spacelike $\Sigma$ (an instantaneous 2-surface), or null $\Sigma$, the incoming-data bundle $B$ still has dimension $2+3=5$, so $H$ is still codimension 1. The only special case is a geodesic lying inside $\Sigma$. That is possible only for timelike or null $\Sigma$ that contains the geodesic, which needs $\Sigma$ totally geodesic along it; then the curve runs *along* the seam and is not a state ($p\notin\Sigma$). So no causal type makes hits typical.

## (c) Focusing by the cone. Killed (standard result, checked)

Outside $\Sigma$ the cosmic-string exterior is exactly flat: $ds^2=-dt^2+dr^2+(1-4\mu)^2r^2d\varphi^2+dz^2$ in Gott's form. There is no Ricci or Weyl curvature off $\Sigma$, so the Raychaudhuri equation gives no convergence of a geodesic congruence off the seam. Geodesics are straight lines in the unrolled wedge. A deficit yields double images of a source, from rays passing on both sides of the string (Gott 1985). It does not draw rays onto $r=0$. A $2\pi n$ excess (the branched cover) unrolls into $n$ flat sheets, again with straight lines and no attraction. A ray reaches $r=0$ only if it is aimed exactly there, which is the codimension-1 set of (a). For a smoothed, finite-width string (Gott's interior cap), the interior curvature focuses rays passing *through* the core, but the core is then a smooth region and not a branch seam. Killed.

## (d) Many seams. Killed for discreteness; no gain for countable families (proved)

- **Countable family** (a lattice, or locally finite seams). The hitting set is a countable union of the sets in (a), so it is still meagre and Lebesgue-null. A typical curvelet passes arbitrarily close to seams infinitely often and still never hits one. No gain.
- **Uncountable or dense family.** If the union of the seams is dense, then either it is not closed, and "$g$ analytic off a closed $\Sigma$" fails, or its closure has interior, and analyticity is lost on an open set. Hits can then become typical only by giving up the definition of the set. The branch data also stop being one integer per seam: there is a continuum of seams, and the seam density is a free parameter that bears on LT2.

## (e) Codimension-1 walls. Killed for sheets (proved)

A closed embedded hypersurface $W$ (a domain wall) is crossed transversally by every curvelet that reaches it. That is an open condition, so hits *are* typical. But $M\setminus W$ is locally disconnected near $W$, so there is no small loop around $W$, no monodromy and no sheets. A branch count at a wall would need several admissible continuations across the junction. That is the Option F situation, and its v0.6 banner (`papers/piecewise-geodesic-Ck-graph.md`) records that finite-order matching "cannot create a branching edge; …". With analytic continuation across $W$ (junction conditions of Israel type), continuation is unique. So walls trade the sheets away. Killed as a sheets mechanism.

## (f) Extended observer. Works, at the cost of an undefined scale and a change of state

If an observer is a worldtube of proper radius $r_0$ around the curvelet, then "hit" means the tube meets $\Sigma$. That condition is open in the data, and with seams present it has positive measure and nonempty interior, so hits can be typical. Two costs:

1. **The scale $r_0$ is undefined in the record.** Candidates would be the Planck length, or a curvature scale like the Kretschmann-rule length $c|K|^{-1/4}$. The latter is a model, not adopted, and it diverges near a flat string exterior, where $K=0$. Any choice is a new constant with an LT2 burden.
2. **The state changes.** The state is the germ at a point. If the tube meets $\Sigma$ while the centre curve does not, the centre's continuation is still unique, so nothing branches unless the state is redefined to be the tube. That is a change to the observer-state definition, not just a seam postulate. Which sheet is entered also still needs a rule, i.e. a law of $R$.

## Conclusion (neutral)

No independent reason was found. Within one host, curvelets that hit a codimension-2 seam form a codimension-1, meagre (and Lebesgue-null) set of data, whatever the seam's causal type. Conical deficits and branched excesses do not focus geodesics onto the seam. Countably many seams do not change this, and dense seams break the definition. Codimension-1 walls make hits typical but have no sheets.

The smallest addition found that would make hits typical is (f): a finite observer size $r_0$ together with a redefinition of the state from a germ at a point to a tube. Its costs are a new scale with no independent value in the record, a change to the elementary-observer definition, and a sheet rule that is a law of $R$ in disguise. The integer $n$ would remain the one non-tuned ingredient. Whether to pursue this is David's call. Without it, Set 1 reduces to ensemble structure (monodromy of hosts), not branching of motion.

**Citations.** Vilenkin 1981; Hiscock 1985; Gott 1985 (all checked against the abstracts this session). Raychaudhuri, Sard and Baire are standard results, not separately cited. #331, #332, #333 and #334 are in-repo.
