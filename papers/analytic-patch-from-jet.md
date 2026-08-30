# Theorem: the simply-connected analytic patch from an infinite jet

David Strayhorn

First real theorem for the geometry note (`papers/observer-space-geometry.md`). It does not rewrite the elementary object. It does not write \(\Phi\). It does not reconstruct a completed four-manifold \(W\). It does not fold the multi-topology ensemble into \(\sim\).

**Status.** Proved: existence of a simply-connected realizing patch, uniqueness of the germ, and uniqueness of the maximal simply-connected continuation as a pointed real-analytic Lorentzian 4-manifold, up to unique isomorphism inducing the identity on the germ. Killed: uniqueness of \(P\) as a subset of a completed \(W\), or as a canonical simply-connected open subset of a fixed \(\mathbb{R}^4\). No new locked hypothesis: "infinite jet of a real-analytic Lorentzian metric" already means a convergent jet, not a formal series of radius zero.

---

## 0. Claim

Given a point \(p\), an infinite jet \(j_\infty\) of a real-analytic Lorentzian metric at \(p\), and a future unit timelike vector \(u\) compatible with the \(0\)-jet, there exists a unique (up to a stated equivalence) simply-connected real-analytic Lorentzian patch \(P(j_\infty,u)\) on which the metric realizes that jet and \(u\) is the time direction at \(p\).

Finite \(k\)-jets and \(C^\infty\) jets are already closed as candidates for the object (Borel). They are not reopened.

---

## 1. Hypotheses (none new)

The following are the locked object, unpacked so the proof has a place to start. They are not extra ontology.

1. A point \(p\). In a chart, \(p\in\mathbb{R}^4\). The chart is a presentation of the lump, not a completed spacetime \(W\).
2. An infinite jet \(j_\infty\) *of a real-analytic Lorentzian metric* at \(p\). That means: there is a formal Taylor series \(\sum_{\alpha} \frac{1}{\alpha!} (\partial^\alpha g_{\mu\nu})(p)\, x^\alpha\) for a symmetric \(2\)-tensor, the \(0\)-jet \(g(p)\) has Lorentzian signature, and the series has positive radius of convergence (it is the Taylor series of a real-analytic germ, not an arbitrary formal series).
3. A vector \(u\in T_p\) with \(g(p)(u,u)=-1\) (mostly-plus convention; the opposite convention is an equivalent rewrite) and future-directed relative to a chosen time orientation at \(p\). The vector \(u\) is data. It is not determined by \(j_\infty\).

If hypothesis 2 is read as "an arbitrary formal Lorentzian jet, possibly divergent," existence fails. That reading is not the locked object. Borel's lemma supplies a \(C^\infty\) metric for every formal jet, and that metric is not real-analytic in general, and is not unique as a germ. That is why \(C^\infty\) was closed.

---

## 2. Equivalence (the "up to" in uniqueness)

Two simply-connected real-analytic Lorentzian patches \((U,g,p,u)\) and \((U',g',p',u')\) are *equivalent as germs* if there exist connected open neighbourhoods \(V\ni p\) in \(U\) and \(V'\ni p'\) in \(U'\) and a real-analytic diffeomorphism \(\varphi:V\to V'\) with

\[
\varphi(p)=p',\qquad
d\varphi_p(u)=u',\qquad
\varphi^*g'=g\ \text{on }V.
\]

They are *equivalent as maximal simply-connected patches* if there is a real-analytic isometry \(\Phi:U\to U'\) of the whole patches with the same three identities. The uniqueness theorem uses germ equivalence for Theorem A and maximal equivalence for Theorem B.

This equivalence is a presentation of the same lump. It is not a silent Diff/frame quotient replacing the object, and it is not a topology label of an ensemble patch.

---

## 3. Theorem A (germs). Proved.

**Theorem A.** Under the hypotheses of §1:

1. *(Existence.)* There exists a simply-connected real-analytic Lorentzian patch \((U,g,p,u)\) whose infinite jet at \(p\) is \(j_\infty\) and whose time direction at \(p\) is \(u\).
2. *(Uniqueness of the germ.)* If \((U,g,p,u)\) and \((U',g',p,u)\) both realize \(j_\infty\) at \(p\), with the same \(u\), then there is a neighbourhood of \(p\) on which the two patches are equivalent as germs. In a common chart about \(p\), \(g=g'\) on the connected component of \(p\) in \(U\cap U'\).

**Proof of existence.** By hypothesis 2, each component \(g_{\mu\nu}\) is given by a power series centred at \(p\) with positive radius of convergence \(r>0\). The sums define a real-analytic symmetric \(2\)-tensor \(g\) on the open ball \(B=\{x:|x-p|<r\}\) (Krantz and Parks 2002, the local power-series characterisation of real-analytic functions). Lorentzian signature is an open condition on the \(0\)-jet, so after shrinking \(r\) if needed, \(g\) is Lorentzian on \(B\). A ball is simply-connected. The pair \((B,g)\) with basepoint \(p\) and vector \(u\) is a simply-connected real-analytic Lorentzian patch realizing \(j_\infty\). \(\square\)

**Proof of uniqueness of the germ.** In a common chart, the difference \(h=g-g'\) is real-analytic and has vanishing infinite jet at \(p\), so its power series at \(p\) is identically zero. Hence \(h\equiv 0\) on a neighbourhood of \(p\). Let \(U\) be connected and open, \(f\) real-analytic on \(U\). The set where \(f\) agrees with the zero function is open (vanishing jet implies vanishing on a ball) and closed (continuity). If \(U\) is connected and the jet at one point vanishes, \(f\equiv 0\) on \(U\). That is the identity theorem for real-analytic functions of several real variables, in the form that uses an infinite jet at a point, not the weaker one-variable form that uses an accumulation point of a zero set (Krantz and Parks 2002; the several-variable identity theorem requires an open set or a vanishing jet, not merely a set with an accumulation point). Apply this to each component of \(h\) on each connected component of \(U\cap U'\) that contains \(p\). The identity map of that neighbourhood is the germ equivalence, and it fixes \(p\) and \(u\). \(\square\)

Cauchy--Kovalevskaya is not used. The Einstein equation is not used. The data are the metric jet, not Cauchy data for a PDE.

---

## 4. Theorem B (maximal simply-connected continuation). Proved, as an abstract patch.

**Theorem B.** Under the hypotheses of §1, there exists a simply-connected real-analytic Lorentzian 4-manifold \((M,g)\) with marked point \(p\in M\) and marked vector \(u\in T_p M\), whose germ at \(p\) realizes \(j_\infty\), and which is maximal among simply-connected realizing patches: if \((M',g',p',u')\) is any other simply-connected real-analytic Lorentzian patch realizing the same germ, there is a unique real-analytic isometric immersion \(M'\to M\) sending germ to germ (in particular \(p'\mapsto p\) and \(u'\mapsto u\)). Any two such maximal objects are uniquely isomorphic. \(M\) is a patch, not a completed four-manifold \(W\).

**Proof sketch, with named theorems.**

*Step 1 (complexification of the germ).* A real-analytic germ at \(p\in\mathbb{R}^4\) is the restriction of a unique holomorphic germ at \(p\in\mathbb{C}^4\) (Krantz and Parks 2002; equivalently, the real power series is the restriction of the complex power series). Do this for each of the ten components \(g_{\mu\nu}\). Symmetry \(g_{\mu\nu}=g_{\nu\mu}\) is algebraic and continues. Nondegeneracy and Lorentzian signature of the real restriction persist on a real ball, by Theorem A.

*Step 2 (monodromy).* Analytic continuation of a holomorphic germ along a path is unique when it exists. If two paths from \(p\) to a point \(q\) are homotopic through paths along which continuation is possible, the continued germs at \(q\) agree. That is the monodromy theorem (Ahlfors 1979, Ch. 8, in one variable; Hörmander 1990, the several-variable form for holomorphic germs). Simple connectedness of the parameter domain makes every closed path homotopic to a constant, so continuation, when possible along every path, is single-valued.

*Step 3 (maximal continuation as a Riemann domain).* The sheaf of holomorphic germs of the complexified metric has an étalé space. The connected component of the given germ is the maximal (possibly multi-sheeted) holomorphic continuation, a Riemann domain over \(\mathbb{C}^4\), unique up to unique isomorphism fixing the germ. Restricting to the real locus and to the open set where the restriction is real and Lorentzian gives a real-analytic Lorentzian 4-manifold \(E\) with basepoint the given germ. If \(E\) is not simply-connected, replace \(E\) by its universal cover \(\widetilde{E}\). The metric and the pair \((p,u)\) lift. \(\widetilde{E}\) is simply-connected.

*Step 4 (universal property).* Let \((M',g')\) be any simply-connected real-analytic realizing patch. Complexify its germ (which agrees with \(j_\infty\) by Theorem A). Continuation along paths in \(M'\) is single-valued by the monodromy theorem, because \(M'\) is simply-connected. That defines a unique analytic isometric immersion \(M'\to\widetilde{E}\) sending germ to germ.

*Step 5 (not \(W\)).* \(\widetilde{E}\) is constructed from the germ. It is not a completion of a 4-manifold, not an analytic continuation "until the spacetime is whole," and not unique as a subset of some ambient \(W\). Completing, compactifying, or gluing on distant regions would leave the germ and would not be unique. That is the 2008 reconstruction, and it is not this object.

This is a sketch of a standard continuation argument, not a costume. The named theorems are the identity theorem, the power-series characterisation of real-analytic functions, complexification of real-analytic germs, the monodromy theorem, and the étalé-space / Riemann-domain construction of maximal holomorphic continuation. What is not supplied here is a fully written uniqueness proof for Hausdorffness of the real-analytic étalé space without passing through complexification. That is why Step 1 goes through \(\mathbb{C}^4\). If that route is refused, Theorem A still stands and Theorem B is blocked pending a Hausdorff real-analytic continuation lemma. The report for Theorem B is therefore: proved via complexification; blocked as a purely real maximal-continuation theorem until that lemma is written. \(\square\)

---

## 5. What is killed

**K1. Unique subset of a completed \(W\).** False, and not the object. Many analytic Lorentzian 4-manifolds share a germ. Uniqueness as "the spacetime" is the discarded reconstruction.

**K2. Unique maximal simply-connected open subset of a fixed \(\mathbb{R}^4\).** False. A ball works (Theorem A). The union of all simply-connected open realizing subsets of \(\mathbb{R}^4\) need not be simply-connected. There is no canonical largest simply-connected open in a fixed chart. Uniqueness lives at the germ (Theorem A) or as an abstract / Riemann-domain patch (Theorem B), not as a subset of the chart.

**K3. Existence for a divergent formal jet.** False. Borel supplies a \(C^\infty\) realization that is not a unique analytic germ. The locked object already excludes this by saying the jet is of a real-analytic metric.

**K4. Uniqueness if simple connectedness is dropped.** False in the sense of a single-valued patch. Continuation around non-contractible loops can produce distinct patches from one jet (monodromy). Those are the relative ensemble. They are not extra elementary observers. They are not folded into \(\sim\). Theorem B's universal cover is a simply-connected presentation of the elementary object, not a topology label in the cut.

**K5. Finite \(k\) or \(C^\infty\).** Already closed. Theorem A fails for both: a \(k\)-jet does not determine a germ of a metric, and a \(C^\infty\) jet does not determine a germ of a real-analytic metric.

---

## 6. What this does not do

It does not write \(\Phi\). It does not identify a finished manifold for the multi-topology ensemble. It does not prove countability. It does not recover quantum mechanics or general relativity. It does not derive the Born rule. Union of ensembles is not Hilbert space. \(\chi\), 4-geons, and spin foam stay on the shelf.

The cut in the geometry note compares elementary objects \((j_\infty(\tau),u(\tau))\), equivalently their simply-connected analytic patches. Theorems A and B say what that equivalence of patches is. They do not change the cut.

---

## 7. Report line

- **Proved:** Theorem A (existence of a simply-connected realizing patch; uniqueness of the germ).
- **Proved, via complexification:** Theorem B (maximal simply-connected continuation, unique up to unique pointed analytic isometry).
- **Blocked as a purely real maximal-continuation theorem** until a Hausdorff lemma for the real-analytic étalé space is written. Not blocked as a theorem about the locked object, because the complexification route is available and is the standard one.
- **Killed:** uniqueness inside \(W\); uniqueness as a subset of a fixed \(\mathbb{R}^4\); existence for divergent formal jets; uniqueness without simple connectedness (ensemble, not \(\sim\)).
- **Hypothesis:** none beyond the locked object. If \(j_\infty\) were read as a formal series, one extra hypothesis would be needed (positive radius of convergence). That reading is refused.

---

## References

Ahlfors, L. V. *Complex Analysis.* 3rd ed. McGraw--Hill, 1979. (Monodromy theorem.)

Borel, E. Sur quelques points de la théorie des fonctions. *Annales scientifiques de l'École Normale Supérieure* 12 (1895) 9--55. (Borel's lemma: every formal series is a \(C^\infty\) jet.)

Hörmander, L. *An Introduction to Complex Analysis in Several Variables.* 3rd ed. North-Holland, 1990. (Holomorphic continuation in several variables.)

Krantz, S. G. and Parks, H. R. *A Primer of Real Analytic Functions.* 2nd ed. Birkhäuser, 2002. (Real-analytic functions as convergent power series; identity theorem; complexification of real-analytic germs.)

Strayhorn, D. Observer space: jet-patch equivalence, the locked cut, and open geometric questions. `papers/observer-space-geometry.md`, branch `paper1-geometry-note`.
