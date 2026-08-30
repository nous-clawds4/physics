# Observer space: jet-patch equivalence, the locked cut, and open geometric questions

David Strayhorn

A geometry note. Companion to the ontology draft (`papers/observer-space-ontology.md` on `paper1-ontology-draft`). It does not rewrite that draft.

---

## 0. Purpose

This note writes the locked elementary object and the locked standard of distinctness in math, and lists the geometric questions left open. For each open question it says what would count as an answer. It does not answer them. It does not recover quantum mechanics or general relativity. It does not derive the Born rule. It does not write an equation of motion. It does not reconstruct a completed four-manifold.

---

## 1. Elementary observer: infinite jet, equivalently simply-connected analytic patch

At an instant, an elementary observer is a pair \((j_\infty,u)\).

- \(j_\infty\) is the infinite jet, at a point \(p\), of a real-analytic Lorentzian metric.
- \(u\) is a future-directed unit timelike vector relative to the \(0\)-jet: \(g(u,u)=-1\) in the mostly-plus convention (the opposite convention is an equivalent rewrite).

Equivalently, the same object is the unique simply-connected real-analytic patch \(P(j_\infty,u)\) obtained by analytic continuation of that jet, with the time direction \(u\).

**Locked equivalence.** On simply-connected real-analytic patches,

\[
j_\infty \;\text{determines}\; P(j_\infty,u)
\qquad\text{and}\qquad
P \;\text{determines}\; j_\infty.
\]

Those are two names for one lump. Finite \(k\)-jets do not suffice: a \(k\)-jet does not determine the germ. \(C^\infty\) does not suffice: by Borel's lemma, every infinite jet is realized by some smooth metric, so a smooth jet does not determine a germ. Real-analyticity is what makes the infinite jet a local geometric object rather than a formal list of derivatives.

The continuation is local. It produces a patch. It is not adopted as analytic continuation of the jet to a completed four-manifold \(W\). That was the 2008 reconstruction. \(W\) is not the object.

Write \(\mathrm{Obs}\) for the space of elementary observers: pairs \((j_\infty,u)\), equivalently simply-connected real-analytic patches with time direction. That is a name for the set. The precise mathematical home of the space of infinite jets of Lorentzian metrics (Fréchet, inverse limit, analytic radius constraints), and how \(u\) sits in it, is open (§4.1). Do not identify a finished manifold for the multi-topology ensemble of §1.1.

Gielen and Wise's observer space is the seven-manifold of future-directed unit four-velocities of a given Lorentzian spacetime. The object here includes the metric jet / patch as part of the point. Same English words, different set.

### 1.1 Relative ensemble, not extra elementary observers

If simple connectedness is dropped, one jet can determine several patches, one per topology / monodromy of the continuation. Those patches are the *relative ensemble* of that elementary observer. They are not extra elementary observers. They are not additional points of \(\mathrm{Obs}\).

Do not fold the ensemble into \(\sim\). The locked cut of §2 compares elementary objects. Topology labels of ensemble patches do not enter that formula. Do not treat the union of ensembles as Hilbert space. Do not identify a finished manifold whose points are the multi-topology patches.

---

## 2. Histories, and the locked cut

A history, or evolution, is a curve in observer space, parametrized by proper time. For an interval \(I=[0,T]\) with \(T\in(0,\infty]\), an evolution is a map

\[
\gamma: I \to \mathrm{Obs},\qquad
\tau\mapsto \gamma(\tau)=\bigl(j_\infty(\tau),\,u(\tau)\bigr)
\;\simeq\;
P\bigl(j_\infty(\tau),u(\tau)\bigr).
\]

The parameter \(\tau\) is proper time along that evolution, with a chosen origin \(\tau=0\). Write \(O:=\gamma(0)\) and \(O(\tau):=\gamma(\tau)\). Restriction of an evolution to a subinterval \([0,\tau]\subset I\) is again an evolution.

**Locked individuation cut.** Let \(\gamma:I\to\mathrm{Obs}\) and \(\gamma':I\to\mathrm{Obs}\) be two evolutions on the same proper-time interval, with the same origin convention. Then

\[
\gamma \sim \gamma'
\quad\text{iff}\quad
\forall\,\tau\in I:\quad
\bigl(j_{\infty,\gamma}(\tau),\,u_\gamma(\tau)\bigr)
=
\bigl(j_{\infty,\gamma'}(\tau),\,u_{\gamma'}(\tau)\bigr).
\]

Equivalently, the simply-connected analytic patches agree at every \(\tau\):

\[
\gamma \sim \gamma'
\quad\text{iff}\quad
\forall\,\tau\in I:\quad
P\bigl(j_{\infty,\gamma}(\tau),u_\gamma(\tau)\bigr)
=
P\bigl(j_{\infty,\gamma'}(\tau),u_{\gamma'}(\tau)\bigr).
\]

They are distinct at the first proper time those local data disagree:

\[
\tau_*
\;=\;
\inf\bigl\{\tau\in I:\ 
(j_{\infty,\gamma}(\tau),u_\gamma(\tau))
\ne
(j_{\infty,\gamma'}(\tau),u_{\gamma'}(\tau))\bigr\},
\]

with \(\inf\emptyset=\infty\), and \(\gamma\nsim\gamma'\) iff \(\tau_*<\infty\).

Topology labels do not enter the formula. Amplitude does not enter the formula. Global 4-manifold names, charts, and coordinate tables are presentations of the lump, not further data. Hilbert-space weight does not make two evolutions the same, and does not make them different. A decoherence branch is a different kind of object; it is not what \(\sim\) quotients. Ensemble patches of §1.1 are not what \(\sim\) quotients.

**Gauge.** Stay agnostic on presentations of the same lump. Equality in the cut is equality of elementary objects \((j_\infty,u)\), equivalently of simply-connected analytic patches. A later Diff/frame story, if one is written, must be a presentation of that equality, not a replacement of the object by a quotient space, and not a gauge-fixed jet space adopted in order to proceed. Do not silently quotient. Do not treat a coordinate-table equality as a well-posedness theorem.

If the domains differ, compare on the overlap after aligning origins. Prefixes of an evolution are earlier nodes of the same history, not a second history.

---

## 3. The unique rooted tree, as a set of curves

Fix a root \(O\in\mathrm{Obs}\). Let \(\mathrm{Evol}(O)\) be the set of evolutions with \(\gamma(0)=O\), taken modulo \(\sim\). Order them by extension. That poset is a tree: any two elements have a greatest common prefix. Distinctness at first disagreement \(\tau_*\) is the branching time.

The tree is unique as a set of identity classes of elementary evolutions from a given root. The physical continuation from a node is not unique. Non-uniqueness of evolution is part of the ontology. \(\Phi\) is open (§4.5). Echeverria, Klinkhammer, and Thorne (1991) is the picture for "doesn't know / knows": first disagreement of the simply-connected patch \(P\). It is not the mechanism of non-uniqueness, and it is not \(\Phi\).

Nothing in this section supplies a measure. Countability is still conditional.

---

## 4. Open geometric questions

Each item states what is open, and what would count as an answer. An answer is a construction or a theorem that meets the criterion. A preference, a 2008 habit, or a costume is not an answer.

Finite jet order, as a question about which \(k\) constitutes the observer, is closed as a candidate: finite \(k\) does not suffice. \(C^\infty\) is closed as a candidate: it does not suffice. The object is the real-analytic infinite jet, equivalently the simply-connected analytic patch. What remains is to house that object, to prove the equivalence as a theorem rather than a locked identification, and to say what "knows" is on \(P\).

### 4.1 Space of infinite jets, and how \(u\) sits in it

**Open.** \(\mathrm{Obs}\) is named as the space of pairs \((j_\infty,u)\). The precise space of infinite jets of Lorentzian metrics is not identified. Candidates, none adopted: the inverse limit \(\varprojlim J^k\) of \(k\)-jets of symmetric \(2\)-tensors at a point, cut down to Lorentzian \(0\)-jets and to jets of real-analytic metrics (finite radius of convergence); a Fréchet space containing that inverse limit; some other locally convex space. How \(u\) sits in it (unit timelike sphere in the \(0\)-jet, or an extra factor) is part of the same question. This is not a finished manifold identification, and it is not a home for the multi-topology ensemble.

**What would count as an answer.** A specified mathematical space \(\mathcal{J}\) of infinite jets of real-analytic Lorentzian metrics, and a specified place for \(u\), such that:

1. \(\mathrm{Obs}\) is identified with that space of pairs, forced by the objects of §1, not chosen for convenience.
2. Formal series with zero radius of convergence are not included, or are included only with a stated reason (they are not germs of real-analytic metrics).
3. The identification is a presentation of the lump, not a silent Diff/frame quotient and not a gauge-fixed jet space adopted in order to proceed.
4. The multi-topology ensemble of §1.1 is not smuggled in as extra points of \(\mathcal{J}\).

A modelling preference for "Fréchet because jets are Fréchet" does not count until (1)--(4) are checked.

### 4.2 Existence and uniqueness of \(P(j_\infty,u)\)

**Open.** The locked equivalence says that, on simply-connected real-analytic patches, \(j_\infty\) determines \(P\) and \(P\) determines \(j_\infty\). That is the identification of the two names. Existence, uniqueness, radius, and maximality of \(P(j_\infty,u)\) as a simply-connected analytic patch are not proved here.

**What would count as an answer.** Theorems, in named function spaces, that:

1. *Existence.* For each elementary observer \((j_\infty,u)\) there is a simply-connected real-analytic Lorentzian patch \(P\) whose infinite jet at the basepoint is \(j_\infty\) and whose time direction is \(u\).
2. *Uniqueness.* Any two such simply-connected patches agree on a common simply-connected neighbourhood of the basepoint, or on a stated maximal domain.
3. *Radius / maximality.* The domain of \(P\) is specified (radius of analyticity, maximal simply-connected analytic domain, or an equivalent), and is a patch, not a completed four-manifold \(W\).
4. The converse, \(P\mapsto j_\infty\), is the infinite jet at the basepoint, which is the easy direction and must still be stated.

A slogan that "analytic jets determine germs" does not count. A construction that continues the jet to a completed \(W\) does not count. A uniqueness claim that drops simple connectedness (and therefore collides with §1.1) does not count.

### 4.3 \(\varepsilon\to 0\) versus the analytic patch

**Open, and the object is not \(\varepsilon\).** The simply-connected analytic patch already has volume. Size is whatever radius / maximal domain §4.2 supplies. \(\varepsilon\) is not a second object, and not a second observer. The earlier candidate of an arbitrarily small worldtube of radius \(\varepsilon\), taken independently of the analytic patch, is retired as a second object.

**What would count as an answer.** A statement, with proof, of the relation between the analytic patch \(P(j_\infty,u)\) and any \(\varepsilon\to 0\) limit:

1. Either \(\varepsilon\to 0\) is redundant, because \(P\) is already the local object, or the limit is defined and shown not to replace \(P\) by a point-jet of finite order.
2. "Knows" (§4.4) is a predicate on \(P\), not on an auxiliary \(\varepsilon\)-tube, unless that tube is identified with \(P\).
3. The limit is not a completed \(W\).

An assertion that "arbitrarily small means a point, so a finite jet" does not count. Finite jets do not suffice.

### 4.4 Causal entry / "knows," as first disagreement of \(P\)

**Open.** "Knows" is first disagreement of the simply-connected analytic patch \(P\). It is a fact about local geometric data. It is not Hilbert-space amplitude. EKT 1991 is the picture, not the definition, not the mechanism, and not \(\Phi\).

**What would count as an answer.** A predicate, equivalent to first disagreement \(\tau_*\) of \(P\), such that:

1. Two evolutions from a common root "know" a difference at \(\tau_*\), and not before, iff their simply-connected patches first disagree at \(\tau_*\).
2. The predicate does not mention \(|a|^2\), decoherence, or topology labels of ensemble patches.
3. Light-crossing / causal structure may be used if it is a causal relation in \(P\), not a global 4-manifold label and not a signal defined only on \(W\).

A slogan that the observer "sees" an outcome when the wavefunction decoheres does not count.

### 4.5 Equation of motion

**Held.** Motion is classical in character: a geometric curve, not a superposition. It is not unique. \(\Phi\) still waits. The 2008 geodesic / parallel-transport law is a candidate, not a result. EKT 1991 is not \(\Phi\). Do not identify a finished manifold for the multi-topology ensemble in order to write \(\Phi\).

The law, whatever it is, must take an elementary observer \((j_\infty,u)\) equivalently \(P(j_\infty,u)\), and push it forward in its own proper time. It must not first reconstruct \(W\) and then run geodesics on \(W\). Matter fields are open in the ontology; a law that needs them is not writable until they are named.

**What would count as an answer, later.** A map, or a multi-valued map,

\[
\Phi: \mathrm{Obs}\times\mathbb{R}_{\ge 0} \;\to\; \mathcal{P}(\mathrm{Obs}),
\]

such that:

1. \(\Phi(O,0)=\{O\}\).
2. \(\Phi(O,\tau)\) may have more than one element for \(\tau>0\). Non-uniqueness is a theorem or an explicit branching rule, not an accident of coordinates.
3. The domain is the elementary object of §1, not \(W\), and not the multi-topology ensemble.
4. The law does not mention Hilbert space.
5. The set of solution curves from a root \(O\) is exactly \(\mathrm{Evol}(O)\), or differs from it by a stated and justified restriction.
6. The law is gauge-agnostic on presentations of the same lump. A \(\Phi\) that is well-defined only after a silent quotient, or only on one coordinate table, does not count.

---

## 5. Flagged: would change the ontology, or would revive a discarded reconstruction

These issues are not adopted.

**Silent \(W\).** Analytic continuation of \(j_\infty\) to a completed four-manifold \(W\) is the 2008 reconstruction. The locked equivalence uses continuation only to a simply-connected local patch. A later construction that completes \(P\) to \(W\) and then treats \(W\) as the observer is a change of object.

**Silent quotient.** A Diff/frame quotient that replaces the lump by a gauge-fixed jet space, or by an equivalence class adopted in order to proceed, is a different object. Presentations of the same lump are allowed. Replacement is not.

**Folding the ensemble into \(\sim\).** Treating multi-topology patches as extra elementary observers, or putting topology labels into the cut, would change what is counted. The relative ensemble is not \(\mathrm{Obs}\). Union of ensembles is not Hilbert space.

**Grain-classes as the things counted.** If a later measure counts grain-classes while §2 still calls elementary identity-classes the distinct evolutions, the uniqueness argument is being run on a different set. That is extra structure or a change of object. It is not adopted here.

**Finite \(k\) or \(C^\infty\) as the object.** Either would contradict the locked equivalence. They are not available as a retreat if §4.2 is hard.

**Paper 1's wording.** If the ontology draft still names a finite-order jet, or a jet without real-analyticity and simple connectedness, that wording does not match this note. This note does not rewrite Paper 1. Geometry waits on Ontology (or David) for the draft to use the same elementary object. Do not silently keep a finite jet under analytic-patch language.

No claim in §§1--4 is a recovery of quantum mechanics or of general relativity. No claim is a derivation of the Born rule. \(\chi\), 4-geons, and spin foam stay on the shelf.

---

## 6. Hold

\(\Phi\) still waits. Do not identify a finished manifold for the multi-topology ensemble. The precise space of infinite jets (§4.1) and the existence/uniqueness theorem for \(P(j_\infty,u)\) (§4.2) are the geometric jobs that would make the locked equivalence a theorem. They are not done here.

If later work on "knows," the tree, or a limiting measure continues while \(\Phi\) is held, it must be gauge-agnostic on presentations of the same lump, and it must be flagged. Do not silently quotient. Do not silently reconstruct \(W\).

When those holds lift, the order of real constructions, unless David changes it, remains:

1. A specified space of real-analytic infinite jets, and how \(u\) sits in it (§4.1).
2. Existence, uniqueness, radius / maximality of \(P(j_\infty,u)\) as a simply-connected analytic patch (§4.2).
3. "Knows" as first disagreement of \(P\) (§4.4).
4. A candidate \(\Phi\), checked against §4.5, or an honest statement that \(\Phi\) is still missing.
5. The rooted tree of §3 as the solution set of that \(\Phi\).
6. A discretization and a limit, or a proof that countability fails.

Until those exist, counting is the unique reasonable measure only as a conditional. The antecedent is not supplied by this note. This note does not start \(\Phi\), and it does not start \(W\).

---

## References

Borel, E. Sur quelques points de la théorie des fonctions. *Annales scientifiques de l'École Normale Supérieure* 12 (1895) 9--55. (Borel's lemma: every formal power series is the jet of a \(C^\infty\) function.)

Echeverria, F., Klinkhammer, G., and Thorne, K. S. Billiard balls in wormhole spacetimes with closed timelike curves: Classical theory. *Physical Review D* 44 (1991) 1077--1099.

Gielen, S. and Wise, D. K. Lifting general relativity to observer space. *Journal of Mathematical Physics* 54 (2013) 052501.

Strayhorn, D. The observer as a physical object. Draft, `papers/observer-space-ontology.md`, branch `paper1-ontology-draft`.
