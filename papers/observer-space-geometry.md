# Observer space: the locked cut, and what would count as answering the open geometric questions

David Strayhorn

A geometry note. Companion to the ontology draft (`papers/observer-space-ontology.md` on `paper1-ontology-draft`). It does not change that ontology.

---

## 0. Purpose

The ontology names an object, a space, a standard of distinctness, and a measure claim that is conditional on countability. This note writes the locked standard of distinctness as a mathematical identity criterion, and lists the geometric questions the ontology left open. For each open question it says what would count as an answer. It does not answer them. It does not recover quantum mechanics or general relativity. It does not derive the Born rule. It does not write an equation of motion.

Where a precise mathematical home for the objects would require changing what the ontology counts as the same observer, the issue is flagged and not adopted.

---

## 1. Instantaneous observer

Fix a signature convention only as notation: Lorentzian, mostly plus, so a vector \(u\) is timelike when \(g(u,u)<0\). The opposite mostly-minus convention is an equivalent rewrite, not a different theory.

At an instant, an observer is a pair \((j,u)\).

- \(j\) is a jet of a Lorentzian metric at a point. For a finite order \(k\in\mathbb{N}\cup\{0\}\), a representative of \(j\) in some coordinates is the collection of derivatives of a metric \(g_{\mu\nu}\) at that point through order \(k\):

  \[
  j \;=\; \bigl( \partial_{\alpha_1\cdots\alpha_m} g_{\mu\nu}(p) \bigr)_{0\le m\le k}.
  \]

  The \(0\)-jet is required to have Lorentzian signature. The value of \(k\) is not fixed here (§4.1).

- \(u\) is a future-directed unit timelike vector relative to that \(0\)-jet: \(g(u,u)=-1\), future-directed in the time orientation that \(u\) itself supplies.

This is the whole of the instantaneous object. It is not a ray in Hilbert space. It is not a four-velocity on a spacetime that has already been given. It is not the infinite jet used as a germ of an entire four-manifold. Analytic continuation from the jet to a reconstructed \((M,g)\) is not used, and is not permitted as a hidden step.

Write \(\mathrm{Obs}_k\) for the set of such pairs at a fixed finite order \(k\). Write \(\mathrm{Obs}\) for observer space in the sense of the ontology: the space of all such objects, at whatever order is eventually chosen, including the possibility that the order is infinite. \(\mathrm{Obs}\) is not identified with any of the \(\mathrm{Obs}_k\). The coordinate formula is a presentation of a representative, not a decision that \(\mathrm{Obs}\) is the space of raw jets rather than a Diff/frame quotient. David left that gauge question open. Dimension of \(\mathrm{Obs}\) is not identified with the number of coordinate components of a \(k\)-jet; that number is coordinate data, and §4.2 waits.

Gielen and Wise's observer space is the seven-manifold of future-directed unit four-velocities of a given Lorentzian spacetime. The object here includes the metric jet as part of the point. Same English words, different set.

---

## 2. Histories, and the locked cut

A history, or evolution, is a curve in observer space, parametrized by proper time. For an interval \(I=[0,T]\) with \(T\in(0,\infty]\), an evolution is a map

\[
\gamma: I \to \mathrm{Obs},\qquad \tau\mapsto \gamma(\tau)=\bigl(j(\tau),\,u(\tau)\bigr).
\]

The parameter \(\tau\) is proper time along that evolution, with a chosen origin \(\tau=0\). Write \(O:=\gamma(0)\) and \(O(\tau):=\gamma(\tau)\). Restriction of an evolution to a subinterval \([0,\tau]\subset I\) is again an evolution.

**Locked individuation cut.** Let \(\gamma:I\to\mathrm{Obs}\) and \(\gamma':I\to\mathrm{Obs}\) be two evolutions on the same proper-time interval, with the same origin convention. Then

\[
\gamma \sim \gamma'
\quad\text{iff}\quad
\forall\,\tau\in I:\quad
j_\gamma(\tau)=j_{\gamma'}(\tau)
\;\text{and}\;
u_\gamma(\tau)=u_{\gamma'}(\tau).
\]

They are distinct when they disagree at some proper time:

\[
\gamma \nsim \gamma'
\quad\text{iff}\quad
\exists\,\tau\in I:\quad
j_\gamma(\tau)\ne j_{\gamma'}(\tau)
\;\text{or}\;
u_\gamma(\tau)\ne u_{\gamma'}(\tau).
\]

This is equality of maps into \(\mathrm{Obs}\). Hilbert-space amplitude does not appear, and does not get a vote. Weight \(|a|^2\) does not make two evolutions the same, and does not make them different. A decoherence branch is a different kind of object; it is not what \(\sim\) quotients.

The cut is a premise of the ontology. Grain does not reopen it. Same curve or not is settled as equality of \((j,u)\) at every \(\tau\). How fine the jet is, and when a numerical difference is a physically different disagreement, are separate questions (§4.1, §4.3). They are not a second identity criterion.

That equality is the identity criterion. It is not a theorem that the equality is well-posed independently of coordinates or of frame. Gauge is open. Do not read the formula as settling well-posedness, and do not absorb a Diff/frame quotient into the objects in order to make it well-posed (§4.2, §5).

If the domains differ, compare on the overlap after aligning origins, and treat a proper extension as distinct from its restriction in the usual way for curves: the restriction and the extension are not the same map. Prefixes of an evolution are earlier nodes of the same history, not a second history.

---

## 3. The unique rooted tree, as a set of curves

Fix a root \(O\in\mathrm{Obs}\). Let \(\mathrm{Evol}(O)\) be the set of evolutions with \(\gamma(0)=O\), taken modulo \(\sim\). Order them by extension: \([\gamma]\preceq[\gamma']\) when \(\gamma'\) extends \(\gamma\). That poset is a tree: any two elements have a greatest common prefix, namely the restriction of either to the largest initial interval on which they agree.

The tree is unique as a set of identity classes of curves from a given root. The physical continuation from a node is not unique. Non-uniqueness of evolution is part of the ontology. The mechanism is open (§3.5). Echeverria, Klinkhammer, and Thorne (1991) is an existence proof that classical geometric evolution need not be unique. It is not the mechanism, and it is not this tree.

Nothing in this section supplies a measure. A tree of curves can be uncountable. Countability is still conditional.

---

## 4. Open geometric questions

Each item states what is open, and what would count as answering it. An answer is a construction or a theorem that meets the criterion. A preference, a 2008 habit, or a costume is not an answer.

### 4.1 Jet order

**Open.** The ontology needs a local geometric object, not a viewpoint. It does not fix \(k\). Finite \(k\), a specific \(k\), or the inverse limit \(k\to\infty\) are all unset. Infinite order is not a licence to reconstruct a four-manifold by analytic continuation. Analyticity is itself open, and is not assumed.

**What would count as an answer.** One of the following, with a proof that the other options are redundant or ill-posed for the later jobs (grain, tree, limiting measure, equation of motion):

1. A specific finite \(k\), forced by the equation of motion or by the grain construction: the law uses derivatives through order \(k\) and is ill-posed at every smaller order, and extra order is gauge or padding.
2. A theorem that every later construction is independent of \(k\) for all \(k\ge k_0\), with \(k_0\) named.
3. A well-posed use of the inverse limit (infinite jets) that still does not reconstruct a spacetime, together with a proof that finite truncations do not suffice.

A number written down because ten metric components, or because curvature needs second derivatives, is a candidate, not an answer, until it is forced by (1)--(3).

### 4.2 Dimension of observer space

**Open.** \(\mathrm{Obs}\) might be finite-dimensional, a countable discrete set, a Banach or Fréchet manifold, an inverse limit of jet spaces, or something that is not a manifold. The number of coordinate components of a \(k\)-jet of \(g_{\mu\nu}\) plus a unit timelike vector is not the dimension of \(\mathrm{Obs}\). That number still includes coordinate and gauge redundancy, which the ontology has not quotiented.

**Held.** David left gauge open: raw jets versus a Diff/frame quotient is not decided in this note, and \(\mathrm{Obs}\) is not identified with a specified mathematical space. This item waits.

**What would count as an answer, later.** An identification of \(\mathrm{Obs}\) with a specified mathematical space, forced by the objects as defined in §1--§2, not chosen for convenience. The identification must say whether the space is a set of raw jets or a set of equivalence classes. If it is a set of equivalence classes, that is a change to the objects of §1, and it is not an answer until Ontology (or David) adopts the quotient (§5). A modelling preference for "the smallest manifold that holds the data" does not count. A construction that picks one side of the fork in order to proceed does not count.

### 4.3 Grain of "disagree"

**Open.** The locked cut uses equality. Two evolutions that differ in any component of the jet, at any \(\tau\), are distinct. A physically relevant grain would say which of those mathematical differences are physically different disagreements, and which are coordinate artifacts, numerical noise, or the same observer under a change of frame.

Grain is not a second identity criterion. The ontology split them on purpose. The danger is that a grain used for counting will quietly replace the objects of §2 with coarser objects.

**What would count as an answer.** A relation or a partition on \(\mathrm{Obs}\), or on \(\mathrm{Evol}(O)\), that is independent of Hilbert-space amplitude, together with an explicit statement of which of the following it is:

1. *Gauge of the objects themselves:* a quotient that changes what "agree" means in §2. That is an ontology change. It does not count as an answer here; it is a flag (§5).
2. *A coarse-graining for the measure only:* identity classes remain the objects; grain-classes are the things whose counting measure is later taken. Then the uniqueness argument of the ontology (counting is what remains when nothing else is added) must be re-run on grain-classes, and it must be shown that the grain is not a further weighting rule. If it cannot be shown, grain-counting is a different theory.
3. *A physically forced discreteness:* the dynamics produces only a discrete subset of \(\mathrm{Obs}\), and equality on that subset is already the locked cut. Then grain is not extra. That would be an answer, and it would sit in §4.5 as much as here.

Success includes a test: given two jets that differ by a coordinate change at the point, and two jets that differ by a curvature invariant, the grain must say which of those differences is disagreement in the sense that counting will use. If it cannot say, it is not yet a grain.

### 4.4 Limiting procedure from a discretized tree to a measure

**Open.** The program wants a unique rooted tree and a limit from a discretized tree to a measure. The ontology's measure claim is conditional: if distinct evolutions are countable, counting is the unique reasonable measure. Countability is not proved. Three live possibilities remain: exact countability of identity classes; countability only after a grain; a continuum with no such grain. In the last case the uniqueness argument fails in the Bertrand way, and that is a failure of the program, not a small omission.

There is no countably additive probability measure on a countably infinite set that gives each point the same positive weight. Finite ratios, or a grain at which the collection is finite, are what countability still supplies. Wording does not solve that.

**What would count as an answer.** A construction with all of the following, or a proof that some item cannot be had:

1. A directed family of discretizations of the rooted tree of §3, with named cutoffs (jet order, grain, time step, depth), each discretization finite or countable.
2. On each discretization, the counting measure on identity classes (or, if grain-classes are used, an explicit admission that the objects being counted are grain-classes, and a check against §4.3(2)).
3. A limit of those counting measures, in a stated topology or along cylinder sets, that exists.
4. Uniqueness of that limit among limits of the same family, and independence of inessential discretization choices.
5. A proof that the limit does not introduce a weighting rule that the ontology does not contain. In particular, \(|a|^2\) is not a uniqueness proof.

**What would falsify "counting is the unique reasonable measure."** Any of: two discretizations whose counting measures have inequivalent limits; a forced continuum of identity classes with no grain, leaving Bertrand's freedom intact; a uniqueness argument that uses Hilbert-space amplitude to cut the continuum down to size; a redefinition of one outcome as a multitude of copies whose number is set equal to \(|a_n|^2\).

This note does not carry out the limit. A picture of a tree is not a limit.

### 4.5 Equation of motion

**Open.** Motion is classical in character: a geometric curve, not a superposition. It is not unique. The 2008 papers used the geodesic equation / parallel transport in proper time. The ontology states the same qualitative claim and does not write an equation. That geodesic law is a candidate, not a result.

The law, whatever it is, must take a local geometric object and push it forward in its own proper time. It must not first reconstruct a four-manifold by analytic continuation and then run geodesics on that manifold. Matter fields are open in the ontology; a law that needs them is not writable until they are named.

**What would count as an answer.** A map, or a multi-valued map, from an observer and a time increment to a set of possible later observers,

\[
\Phi: \mathrm{Obs}\times\mathbb{R}_{\ge 0} \;\to\; \mathcal{P}(\mathrm{Obs}),
\]

such that:

1. \(\Phi(O,0)=\{O\}\).
2. \(\Phi(O,\tau)\) may have more than one element for \(\tau>0\). Non-uniqueness is a theorem or an explicit branching rule, not an accident of coordinates.
3. The domain is the object of §1, not a reconstructed spacetime.
4. The law does not mention Hilbert space.
5. The set of solution curves from a root \(O\) is exactly \(\mathrm{Evol}(O)\), or differs from it by a stated and justified restriction.

Labelling the geodesic equation as the law counts as an answer only if (1)--(5) are checked for it, including (2). Existence of some classical model with non-unique geodesics (EKT 1991) checks that (2) is possible in classical geometry. It does not check (1)--(5) for observer space, and it does not supply \(\Phi\).

A \(\Phi\) that is well-defined only for raw jets, or only on a quotient, does not count while gauge is open. The law must still make sense if a quotient is adopted later, or it must wait with §4.2. Do not write \(\Phi\) on one side of that fork.

---

## 5. Flagged: would change the ontology

These issues are not adopted. They are listed so that a later construction does not repair them silently.

**Gauge and "agree."** Equality of jets, as written in §2, is equality of coordinate data, or of whatever presentation of a jet one has chosen. Two presentations that differ by a diffeomorphism, or by a change of frame at the point, may be the same physical observer. If they are, \(\mathrm{Obs}\) is a quotient, and the locked cut is equality of equivalence classes, not equality of representatives. That changes the objects. It is not used here. A later answer to §4.2 or §4.3 that needs the quotient must wait on Ontology (or David).

**Grain-classes as the things counted.** If the measure counts grain-classes while §2 still calls identity-classes the distinct evolutions, the uniqueness argument is being run on a different set than the set the cut individuates. That is either extra structure (a weighting / coarse-graining rule) or a change of object. It is not adopted here.

**Proper-time origins for unrelated roots.** The cut compares \(\gamma(\tau)\) and \(\gamma'(\tau)\) at equal \(\tau\). For two continuations of one root this is the natural parameter. A global identity relation on all curves in \(\mathrm{Obs}\), not sharing a root, needs a convention about origins. The locked cut is not being rewritten to supply one.

**Infinite jets as spacetimes.** An infinite jet, even if §4.1 selects it, is still a jet. Treating it as a four-manifold by analytic continuation is the 2008 reconstruction, which the ontology left on the shelf. It would change the object from a local jet to a global spacetime.

No claim in §§1--4 is a recovery of quantum mechanics or of general relativity. No claim is a derivation of the Born rule. Union of ensembles is not Hilbert space.

---

## 6. Hold: home for \(\mathrm{Obs}\)

The next geometric job is a mathematical home for \(\mathrm{Obs}\) (§4.2). That job is held. David left gauge open. Do not decide raw jets versus a Diff/frame quotient. Do not identify \(\mathrm{Obs}\) with a specified space. Do not write a \(\Phi\) that only makes sense on one side of that fork.

If later work on grain, the tree, or a limiting measure continues while this hold is in force, it must be gauge-agnostic: it must still make sense if a quotient is adopted later, and it must be flagged. Do not silently quotient.

When the hold lifts, the order of real constructions, unless David changes it, remains:

1. A mathematical home for \(\mathrm{Obs}\) (§4.2, §5).
2. A candidate \(\Phi\), checked against §4.5, or an honest statement that \(\Phi\) is still missing.
3. The rooted tree of §3, now as the solution set of that \(\Phi\), not as an abstract poset of all maps.
4. A discretization and a limit, or a proof that countability fails.

Until (1)--(4) exist, counting is the unique reasonable measure only as a conditional. The antecedent is not supplied by this note. This note does not start (1).

---

## References

Echeverria, F., Klinkhammer, G., and Thorne, K. S. Billiard balls in wormhole spacetimes with closed timelike curves: Classical theory. *Physical Review D* 44 (1991) 1077--1099.

Gielen, S. and Wise, D. K. Lifting general relativity to observer space. *Journal of Mathematical Physics* 54 (2013) 052501.

Strayhorn, D. The observer as a physical object. Draft, `papers/observer-space-ontology.md`, branch `paper1-ontology-draft`.
