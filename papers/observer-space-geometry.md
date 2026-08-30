# Observer space: hitchhiking patches, the locked cut, and open geometric questions

David Strayhorn

A geometry note. Companion to the ontology draft (`papers/observer-space-ontology.md` on `paper1-ontology-draft`). It does not change that ontology by itself. Where this note uses a locked object that the ontology draft still named as a jet, that is flagged, not papered over.

---

## 0. Purpose

The ontology names an object, a space, a standard of distinctness, and a measure claim that is conditional on countability. This note writes the locked object and the locked standard of distinctness in math, and lists the geometric questions left open. For each open question it says what would count as an answer. It does not answer them. It does not recover quantum mechanics or general relativity. It does not derive the Born rule. It does not write an equation of motion.

The locked object is not a jet at a point. Do not identify observer space with a gauge-fixed jet space.

---

## 1. Instantaneous observer

At an instant, an observer is a pair \((P,u)\).

- \(P\) is an arbitrarily small spacetime patch riding a trajectory. "Hitchhiking" means the patch is carried along that trajectory: it is the observer's own local region at that instant, not a fixed region of a named background manifold, and not a point.
- \(u\) is a future time direction for that patch.

This is the whole of the instantaneous object. It is not a ray in Hilbert space. It is not a four-velocity on a spacetime that has already been given. It is not a \(k\)-jet of the metric at a point. It is not an infinite jet used as a germ of an entire four-manifold. Analytic continuation from local data to a reconstructed \((M,g)\) is not used, and is not permitted as a hidden step.

What data specify \(P\) is open (§4.1). Candidates (none adopted): a small 4-ball; a worldtube of radius \(\varepsilon\) about the trajectory; induced metric plus second fundamental form on a small 3-slice. Listing a 4-ball as a candidate is not a revival of 4-geons, \(\chi\), or spin foam.

Write \(\mathrm{Obs}\) for observer space: the space of all such pairs. Home-for-\(\mathrm{Obs}\) is "the space of patches plus time direction." That is a name for the set, not a finished identification of \(\mathrm{Obs}\) with a specified manifold, Banach space, or jet space. Dimension of \(\mathrm{Obs}\) is not identified here (§4.5).

Gielen and Wise's observer space is the seven-manifold of future-directed unit four-velocities of a given Lorentzian spacetime. The object here includes the patch as part of the point, and does not inherit a spacetime already given. Same English words, different set.

---

## 2. Histories, and the locked cut

A history, or evolution, is a curve in observer space, parametrized by proper time. For an interval \(I=[0,T]\) with \(T\in(0,\infty]\), an evolution is a map

\[
\gamma: I \to \mathrm{Obs},\qquad \tau\mapsto \gamma(\tau)=\bigl(P(\tau),\,u(\tau)\bigr).
\]

The parameter \(\tau\) is proper time along that evolution, with a chosen origin \(\tau=0\). The patch \(P(\tau)\) is the hitchhiking patch at that instant. Write \(O:=\gamma(0)\) and \(O(\tau):=\gamma(\tau)\). Restriction of an evolution to a subinterval \([0,\tau]\subset I\) is again an evolution.

**Locked individuation cut.** Let \(\gamma:I\to\mathrm{Obs}\) and \(\gamma':I\to\mathrm{Obs}\) be two evolutions on the same proper-time interval, with the same origin convention. Write \(D(P)\) for the patch's own geometric data (whatever those data turn out to be: §4.1). Then

\[
\gamma \sim \gamma'
\quad\text{iff}\quad
\forall\,\tau\in I:\quad
D\bigl(P_\gamma(\tau)\bigr)=D\bigl(P_{\gamma'}(\tau)\bigr)
\;\text{and}\;
u_\gamma(\tau)=u_{\gamma'}(\tau).
\]

They are distinct at the first proper time the patch disagrees:

\[
\gamma \nsim \gamma'
\quad\text{iff}\quad
\tau_* < \infty,
\]

where

\[
\tau_*
\;=\;
\inf\bigl\{\tau\in I:\ 
D\bigl(P_\gamma(\tau)\bigr)\ne D\bigl(P_{\gamma'}(\tau)\bigr)
\;\text{or}\;
u_\gamma(\tau)\ne u_{\gamma'}(\tau)\bigr\},
\]

with the convention \(\inf\emptyset=\infty\). Global 4-manifold labels do not enter the formula. Which named spacetime a patch might be said to sit in, which chart, and which coordinate table, are not data of \(D(P)\). Hilbert-space amplitude does not appear, and does not get a vote. Weight \(|a|^2\) does not make two evolutions the same, and does not make them different. A decoherence branch is a different kind of object; it is not what \(\sim\) quotients.

The cut is a premise. Grain does not reopen it. Same curve or not is settled as agreement of the patch's own geometric data and time direction at every \(\tau\). What those data are, and when a difference of data is a physically different disagreement, are separate questions (§4.1, §4.4). They are not a second identity criterion.

**Gauge.** The object is the physical patch. Equality in the cut is equality of patches, not of coordinate tables. A later Diff/frame story, if one is written, must be a presentation of that equality, not a replacement for it. Do not silently quotient. Do not absorb a Diff/frame quotient into the objects in order to make a coordinate formula look well-posed. Do not treat a coordinate-table equality as settled well-posedness of the cut. The cut is already stated as patch equality; well-posedness of a particular presentation of \(D(P)\) is a later job for §4.1, not a reason to change the object.

If the domains differ, compare on the overlap after aligning origins, and treat a proper extension as distinct from its restriction in the usual way for curves: the restriction and the extension are not the same map. Prefixes of an evolution are earlier nodes of the same history, not a second history.

---

## 3. The unique rooted tree, as a set of curves

Fix a root \(O\in\mathrm{Obs}\). Let \(\mathrm{Evol}(O)\) be the set of evolutions with \(\gamma(0)=O\), taken modulo \(\sim\). Order them by extension: \([\gamma]\preceq[\gamma']\) when \(\gamma'\) extends \(\gamma\). That poset is a tree: any two elements have a greatest common prefix, namely the restriction of either to the largest initial interval on which they agree. Distinctness at first disagreement \(\tau_*\) is what supplies the branching time.

The tree is unique as a set of identity classes of curves from a given root. The physical continuation from a node is not unique. Non-uniqueness of evolution is part of the ontology. The mechanism is open (§4.7). Echeverria, Klinkhammer, and Thorne (1991) is the picture for "doesn't know / knows": a finite-size object along a trajectory that has not yet, or has, a signal in its own patch. It is not the mechanism of non-uniqueness, and it is not \(\Phi\).

Nothing in this section supplies a measure. A tree of curves can be uncountable. Countability is still conditional.

---

## 4. Open geometric questions

Each item states what is open, and what would count as an answer. An answer is a construction or a theorem that meets the criterion. A preference, a 2008 habit, or a costume is not an answer. Jet order, as a question about how many derivatives of \(g_{\mu\nu}\) at a point constitute the observer, is retired. The object is not that jet.

### 4.1 What data specify a patch

**Open.** \(D(P)\) is named in the cut and not specified. Candidates, none adopted: a small 4-ball; a worldtube of radius \(\varepsilon\) about the trajectory; induced metric plus second fundamental form on a small 3-slice; some other intrinsic specification of an arbitrarily small region.

**What would count as an answer.** A list of data \(D(P)\) such that:

1. \(D(P)\) is data of the patch itself, not a global 4-manifold label, not a chart, and not Hilbert-space amplitude.
2. Agreement of \(D(P)\) is what the locked cut uses. Two presentations (coordinate tables, frames) of the same patch give the same \(D(P)\), or the answer says honestly that they do not and waits, rather than silently quotienting.
3. The specification is usable for §4.2 and §4.3: it has a size \(\varepsilon\), or an analogue of size, and it has an interior that a signal can have entered or not.
4. It is not a reconstructed spacetime, not an infinite jet used as one, and not a 4-geon / \(\chi\) / spin-foam packaging.

A choice written down because it is familiar (Cauchy data, a ball) is a candidate, not an answer, until (1)--(4) are checked.

### 4.2 The \(\varepsilon\to 0\) limit, and whether "knows" survives

**Open.** The patch is arbitrarily small, not zero. Let \(\varepsilon\) be its size in whatever sense §4.1 supplies. The limit \(\varepsilon\to 0\) may look like a point, or like a jet, or like nothing well-defined. The "knows" / "doesn't know" distinction of §3 and §4.3 occupies the interior of the patch. A point has no interior.

**What would count as an answer.** A theorem, or a counterexample, that says what happens to the "knows" distinction along \(\varepsilon\to 0\):

1. Either "knows" survives in a stated sense (a limit object still has a causal-entry predicate, independent of amplitude), or it does not, and the theory is then a theory of finite \(\varepsilon\), with \(\varepsilon\to 0\) not taken.
2. The limit, if taken, is not identified with a gauge-fixed jet space in order to recover the retired object.
3. The limit is not a reconstructed 4-manifold.

An assertion that "arbitrarily small means a point, so a jet" does not count. That is a change of object.

### 4.3 When a signal has entered the patch

**Open.** "Knows" is a causal fact about the patch: a signal has entered, or it has not. Light-crossing of a region of size \(\varepsilon\) is the obvious scale. The criterion must be independent of Hilbert-space amplitude.

**What would count as an answer.** A predicate \(K(P,s)\) ("signal \(s\) has entered patch \(P\)") such that:

1. \(K\) is a causal / light-crossing relation involving only the patch's own geometry and the signal's causal character. Not \(|a|^2\). Not a decoherence functional.
2. \(K\) is false when no causal curve from the signal's source meets \(P\), and true when one has.
3. \(K\) is defined for the data \(D(P)\) of §4.1, not for a global 4-manifold label.
4. EKT 1991 may be used as a picture of \(K\). It may not be used as \(\Phi\), and it may not be used as the mechanism of non-uniqueness.

A slogan that the observer "sees" an outcome when the wavefunction decoheres does not count.

### 4.4 Grain of "disagree"

**Open.** The locked cut uses equality of \(D(P)\) and of \(u\). A physically relevant grain would say which differences of those data are physically different disagreements.

Grain is not a second identity criterion. The danger is that a grain used for counting will quietly replace the objects of §2 with coarser objects.

**What would count as an answer.** A relation or a partition on \(\mathrm{Obs}\), or on \(\mathrm{Evol}(O)\), independent of Hilbert-space amplitude, together with an explicit statement of which of the following it is:

1. *A presentation of patch equality:* coordinate or frame differences that are not differences of \(D(P)\). That is already required by §2 (equality of patches, not of tables). It is not a new quotient of the objects.
2. *A coarse-graining for the measure only:* identity classes remain the objects; grain-classes are the things whose counting measure is later taken. Then the uniqueness argument of the ontology must be re-run on grain-classes, and it must be shown that the grain is not a further weighting rule. If it cannot be shown, grain-counting is a different theory.
3. *A physically forced discreteness:* the dynamics produces only a discrete subset of \(\mathrm{Obs}\), and equality on that subset is already the locked cut. Then grain is not extra. That would sit in §4.7 as much as here.

Success includes a test: given two patches that differ only by a coordinate table, and two patches that differ by a causal-entry fact of §4.3, the grain must say which difference the count uses. If it cannot say, it is not yet a grain.

### 4.5 Home for observer space

**Open, and not finished here.** \(\mathrm{Obs}\) is the space of patches plus time direction. That is not an identification with a specified mathematical space (finite-dimensional manifold, countable discrete set, Banach or Fréchet manifold, jet space, ...). Do not identify a gauge-fixed jet space.

**What would count as an answer, later.** An identification of \(\mathrm{Obs}\) with a specified mathematical space, forced by the objects of §1--§2, not chosen for convenience, and not a jet space adopted in order to reuse an older formula. A modelling preference for "the smallest manifold that holds the data" does not count. A construction that replaces patches by jets, or that picks a gauge-fixed jet space in order to proceed, does not count.

### 4.6 Limiting procedure from a discretized tree to a measure

**Open.** The program wants a unique rooted tree and a limit from a discretized tree to a measure. The ontology's measure claim is conditional: if distinct evolutions are countable, counting is the unique reasonable measure. Countability is not proved. Three live possibilities remain: exact countability of identity classes; countability only after a grain; a continuum with no such grain. In the last case the uniqueness argument fails in the Bertrand way, and that is a failure of the program, not a small omission.

There is no countably additive probability measure on a countably infinite set that gives each point the same positive weight. Finite ratios, or a grain at which the collection is finite, are what countability still supplies. Wording does not solve that.

**What would count as an answer.** A construction with all of the following, or a proof that some item cannot be had:

1. A directed family of discretizations of the rooted tree of §3, with named cutoffs (patch data of §4.1, size \(\varepsilon\), grain, time step, depth), each discretization finite or countable.
2. On each discretization, the counting measure on identity classes (or, if grain-classes are used, an explicit admission that the objects being counted are grain-classes, and a check against §4.4(2)).
3. A limit of those counting measures, in a stated topology or along cylinder sets, that exists.
4. Uniqueness of that limit among limits of the same family, and independence of inessential discretization choices.
5. A proof that the limit does not introduce a weighting rule that the ontology does not contain. In particular, \(|a|^2\) is not a uniqueness proof.

**What would falsify "counting is the unique reasonable measure."** Any of: two discretizations whose counting measures have inequivalent limits; a forced continuum of identity classes with no grain, leaving Bertrand's freedom intact; a uniqueness argument that uses Hilbert-space amplitude to cut the continuum down to size; a redefinition of one outcome as a multitude of copies whose number is set equal to \(|a_n|^2\).

This note does not carry out the limit. A picture of a tree is not a limit.

### 4.7 Equation of motion

**Held.** Motion is classical in character: a geometric curve, not a superposition. It is not unique. \(\Phi\) still waits. The 2008 papers used the geodesic equation / parallel transport in proper time. That geodesic law is a candidate, not a result. EKT 1991 is not \(\Phi\).

The law, whatever it is, must take a hitchhiking patch with a time direction and push it forward in its own proper time. It must not first reconstruct a four-manifold by analytic continuation and then run geodesics on that manifold. It must not be well-defined only on a jet space. Matter fields are open in the ontology; a law that needs them is not writable until they are named.

**What would count as an answer, later.** A map, or a multi-valued map,

\[
\Phi: \mathrm{Obs}\times\mathbb{R}_{\ge 0} \;\to\; \mathcal{P}(\mathrm{Obs}),
\]

such that:

1. \(\Phi(O,0)=\{O\}\).
2. \(\Phi(O,\tau)\) may have more than one element for \(\tau>0\). Non-uniqueness is a theorem or an explicit branching rule, not an accident of coordinates.
3. The domain is the object of §1, not a reconstructed spacetime and not a jet space.
4. The law does not mention Hilbert space.
5. The set of solution curves from a root \(O\) is exactly \(\mathrm{Evol}(O)\), or differs from it by a stated and justified restriction.
6. The law still makes sense under any later presentation of patch equality (gauge-agnostic). A \(\Phi\) that is well-defined only after a silent quotient, or only on one coordinate table, does not count.

---

## 5. Flagged: would change the ontology

These issues are not adopted. They are listed so that a later construction does not repair them silently.

**Paper 1's named object.** The ontology draft on `paper1-ontology-draft` named the instantaneous observer as a jet of the metric plus a time direction. The locked object in this note is a hitchhiking patch plus a time direction, not a jet at a point. That is a change of object if the draft is read as still current. This note does not rewrite Paper 1. Geometry waits on Ontology (or David) for the draft to use the same object. Do not silently keep a jet space under patch language.

**Gauge as a replacement object.** Equality is equality of patches. A Diff/frame quotient that replaces the patch by an equivalence class of jets, or by a gauge-fixed jet, is a different object. It is not used here. A later presentation of patch equality in coordinates is allowed. A replacement of the object is not.

**Grain-classes as the things counted.** If the measure counts grain-classes while §2 still calls identity-classes the distinct evolutions, the uniqueness argument is being run on a different set than the set the cut individuates. That is either extra structure or a change of object. It is not adopted here.

**Proper-time origins for unrelated roots.** The cut compares \(\gamma(\tau)\) and \(\gamma'(\tau)\) at equal \(\tau\). For two continuations of one root this is the natural parameter. A global identity relation on all curves in \(\mathrm{Obs}\), not sharing a root, needs a convention about origins. The locked cut is not being rewritten to supply one.

**Infinite jets, or patches, as spacetimes.** A patch is still a patch. Treating it as a four-manifold by analytic continuation, or as a 4-geon, is the 2008 reconstruction. It would change the object from a hitchhiking local region to a global spacetime.

**EKT as mechanism.** Using EKT 1991 as the mechanism of non-uniqueness, or as \(\Phi\), would rest multiplicity on wormholes and CTCs. The ontology left that on the shelf. The picture "doesn't know / knows" is kept. The mechanism is not.

No claim in §§1--4 is a recovery of quantum mechanics or of general relativity. No claim is a derivation of the Born rule. Union of ensembles is not Hilbert space.

---

## 6. Hold

Home-for-\(\mathrm{Obs}\) is the space of patches plus time direction. That job is not a finished manifold identification, and it is not a jet-space identification. \(\Phi\) still waits.

If later work on grain, the tree, causal entry, \(\varepsilon\to 0\), or a limiting measure continues while \(\Phi\) and the manifold identification are held, it must be gauge-agnostic: it must still make sense if a later presentation of patch equality is adopted, and it must be flagged. Do not silently quotient. Do not identify a gauge-fixed jet space.

When those holds lift, the order of real constructions, unless David changes it, remains:

1. Data \(D(P)\) that specify a patch (§4.1), usable for causal entry and for \(\varepsilon\).
2. Home for \(\mathrm{Obs}\) as a specified space of those objects (§4.5), if and only if that identification is forced and is not a jet space.
3. A candidate \(\Phi\), checked against §4.7, or an honest statement that \(\Phi\) is still missing.
4. The rooted tree of §3, now as the solution set of that \(\Phi\), not as an abstract poset of all maps.
5. A discretization and a limit, or a proof that countability fails.

Until those exist, counting is the unique reasonable measure only as a conditional. The antecedent is not supplied by this note. This note does not start a jet-space construction, and it does not start \(\Phi\).

---

## References

Echeverria, F., Klinkhammer, G., and Thorne, K. S. Billiard balls in wormhole spacetimes with closed timelike curves: Classical theory. *Physical Review D* 44 (1991) 1077--1099.

Gielen, S. and Wise, D. K. Lifting general relativity to observer space. *Journal of Mathematical Physics* 54 (2013) 052501.

Strayhorn, D. The observer as a physical object. Draft, `papers/observer-space-ontology.md`, branch `paper1-ontology-draft`.
