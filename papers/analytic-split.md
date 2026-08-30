# Analyticity and the split: a theorem and an obstruction

David Strayhorn

The underpinnings question. Locked object unchanged. Companion: `papers/cheat-sheet.md`, `papers/observer-space-geometry.md`, `papers/analytic-patch-from-jet.md`.

It does not write $\Phi$. It does not reconstruct a unique $W$ from an observer. It does not fold the ensemble into $\sim$. It does not derive the Born rule.

**Status.** A coherent formulation exists, if three distinctions are kept. A fork of one analytic metric on a connected patch is killed. A fork of one real-analytic curve in observer space is killed. Multiplicity by topology lives in the ensemble $E(O)$, which is a different distinction. David’s “agree up to $\tau_*$, disagree after” for $N$ geodesics is therefore *not* a fork of one analytic $g$, and *not* a fork of one analytic $\gamma$, unless a hypothesis we have not locked is added (observer-space curves fail to be real-analytic across $\tau_*$).

---

## 0. The question

The hitchhiking observer, multiplicity $N$. $N$ geodesics, parameterized by proper time. Any two distinct ones should agree up to some $\tau_*$ and disagree after. Analyticity seems to forbid a fork of one metric. The proposed answer: they live in spacetimes of distinct topologies.

Keep a hard distinction: a path through spacetime is not a path through observer space. Spacetimes $W$ may have any global topology. Observer space is suspected to be simply connected; that is not assumed. There should be a mapping from a spacetime path to an observer-space path. Given a germ $O$, an ensemble $E(O)$ of spacetimes that contain that germ; if the germ occurs $M$ times in $W$, that $W$ is in the ensemble $M$ times. Distinct $W$ may be distinguished mainly by topology.

The hard piece: can two distinct curves in observer space agree on a finite initial interval, even though the metric is real-analytic?

---

## 1. Three objects that are not one

| | Lives in | Analyticity applies to | Fork of this is |
|---|---|---|---|
| Metric $g$ | one connected patch $P$, or one $W$ | $g$ as a function on a connected 4-domain | killed (identity theorem in several real variables) |
| Curve $\gamma$ | observer space $\mathrm{Obs}$ | $\gamma:I\to\mathrm{Obs}$ as a map of one real variable $\tau$ | killed, *if* $\gamma$ is real-analytic (identity theorem in one real variable) |
| Ensemble member $(W,\iota)$ | $E(O)$ | topology / monodromy of $W$, not a fork of $g$ | allowed; not $\sim$ |

The identity theorem applies to the metric as a function on a connected patch. It does not automatically apply to a curve of germs *across an ensemble*. It does apply, separately, to a real-analytic map from an interval into $\mathrm{Obs}$. Those are two theorems, not one.

---

## 2. Theorem 1. No fork of one analytic metric

**Theorem 1.** Let $U$ be a connected open set in a real-analytic 4-manifold, and let $g,g'$ be real-analytic Lorentzian metrics on $U$. If $g$ and $g'$ have the same infinite jet at one point of $U$, then $g=g'$ on $U$.

This is the identity theorem for real-analytic functions of several real variables, applied componentwise to $g_{\mu\nu}-g'_{\mu\nu}$, in the form that uses a vanishing infinite jet (Krantz and Parks 2002; `papers/analytic-patch-from-jet.md`, Theorem A). A set of accumulation points in $U$ is not enough in several variables; a vanishing jet, or agreement on a nonempty open set, is.

**Corollary.** There is no fork of one real-analytic metric on a connected patch. If two analytic metrics on a connected $P$ agree as germs at the hitchhiker’s location, they agree on $P$. Distinct topologies are not a fork of that $g$. They are a distinction among $W$’s that *contain* $P$.

The 2008 reconstruction would read Theorem 1 as “the germ determines a unique cosmos $W$.” That reading is refused. Theorem 1 determines $g$ on the *connected domain on which it is already given as a real-analytic tensor*. It does not construct a unique maximal spacetime of arbitrary topology.

---

## 3. Theorem 2. No fork of one analytic curve in observer space

For this theorem, “real-analytic curve in $\mathrm{Obs}$” means: in a presentation of the germ by jet coefficients (and the components of $u$) in a local frame along the trajectory, each coefficient is a real-analytic function of proper time $\tau$. That is the structure one actually has along a geodesic in a real-analytic $W$, in Fermi coordinates. It does not require a finished manifold identification of $\mathrm{Obs}$.

**Theorem 2.** Let $I\subset\mathbb{R}$ be a connected interval, and let $\gamma,\gamma':I\to\mathrm{Obs}$ be real-analytic as maps of one real variable in the sense just stated. If the set $\{\tau\in I:\gamma(\tau)=\gamma'(\tau)\}$ has an accumulation point in $I$, then $\gamma=\gamma'$ on $I$. In particular, if $\gamma$ and $\gamma'$ agree on a subinterval $[0,\tau_*]$ with $\tau_*>0$, they agree on every connected interval of $I$ that contains $[0,\tau_*]$.

**Proof.** Equality in $\mathrm{Obs}$ is equality of $(j_\infty,u)$. Each component of that pair, in the presentation, is a real-analytic real function of one variable $\tau$. For real-analytic functions of one variable, agreement on a set with an accumulation point in a connected interval implies identity on that interval (Krantz and Parks 2002; the one-variable identity theorem). $\square$

**Corollary.** Two *distinct* real-analytic curves in observer space cannot share a positive-length prefix. A tree of analytic $\mathrm{Obs}$-curves with shared trunks of positive duration does not exist.

This is not Theorem 1. Theorem 1 is about $g$ on a 4-domain. Theorem 2 is about a map from an interval into $\mathrm{Obs}$. Confusing them is the usual way to make analyticity “forbid multiplicity” in the wrong place.

---

## 4. What distinct topologies actually do

Let $O=(j_\infty,u)$ be an elementary observer, with simply-connected patch $P(O)$.

**Definition.** An *occurrence* of $O$ in a spacetime $W$ is an analytic isometric embedding of a neighbourhood of the basepoint of $P(O)$ into $W$ sending $u$ to a future unit timelike vector of $W$. The *ensemble* $E(O)$ is the class of pairs $(W,\iota)$, where $\iota$ is an occurrence. If $\iota_1,\ldots,\iota_M$ are distinct occurrences of $O$ in the same $W$, that $W$ contributes $M$ elements to $E(O)$.

Distinct elements of $E(O)$ may differ by the global topology of $W$, or by monodromy of analytic continuation of the germ along non-contractible paths in $W$, or by which occurrence $\iota$ was chosen. They do not differ as points of $\mathrm{Obs}$. They are not extra elementary observers. They are not folded into $\sim$.

**Proposition (not a unique cosmos).** $O$ does not determine a unique $W$. Theorem B of `papers/analytic-patch-from-jet.md` determines a unique simply-connected patch $P(O)$, not a unique spacetime of arbitrary topology. Dropping simple connectedness is exactly the freedom that makes $E(O)$ larger than a singleton. Reconstructing a completed $W$ from $O$ as a unique cosmos is the 2008 reconstruction, and it is not used.

**Proposition (mapping, one direction).** Let $(W,\iota)\in E(O)$ and let $\sigma:I\to W$ be a geodesic with $\sigma(0)=\iota(p)$ and $\dot\sigma(0)=\iota_*u$. Define

$$
\pi_W(\sigma)(\tau)
\;=\;
\bigl(\text{infinite jet of }g_W\text{ at }\sigma(\tau),\;\dot\sigma(\tau)\bigr)
\in\mathrm{Obs}.
$$

Then $\pi_W(\sigma)$ is a real-analytic curve in $\mathrm{Obs}$ (Fermi coordinates along an analytic geodesic in an analytic metric). This is the mapping from a path in spacetime to a path in observer space. It is well-defined. It is many-to-one: distinct $(W,\sigma)$ may give the same $\gamma$.

**Proposition (mapping, reverse, not well-defined as a function).** A curve $\gamma:I\to\mathrm{Obs}$ does not determine a unique $(W,\sigma)$. Every pair $(W,\sigma)$ with $\pi_W(\sigma)=\gamma$ is a spacetime-path realization of $\gamma$. There may be many. The reverse mapping is therefore a *correspondence*, not a function. That is the hard distinction in operational form.

---

## 5. The hitchhiking picture, made coherent

David’s picture, written in these symbols:

- Multiplicity $N$ is not $N$ forks of one $g$ on one connected $P$. Theorem 1 kills that.
- $N$ geodesics $\sigma_1,\ldots,\sigma_N$ live in members of ensembles $E(O(\tau))$. They may lie in distinct $W$’s, distinguished mainly by topology, or in one $W$ at $M$ occurrences.
- Each $\sigma_k$ maps to a curve $\gamma_k=\pi_{W_k}(\sigma_k)$ in $\mathrm{Obs}$.
- $\sim$ compares the $\gamma_k$, not the $W_k$. Amplitude does not enter. Topology labels do not enter $\sim$.

**Where “agree up to $\tau_*$, disagree after” can live.**

*(A) In $\mathrm{Obs}$, with analytic curves.* Forbidden by Theorem 2 if $\tau_*>0$. Two analytic $\gamma_k$ that agree on a positive-length prefix are the same curve. Then $\sim$ says they are not distinct as evolutions. Distinctness, if any, is ensemble-distinctness (different $W$ or different occurrence), which is not $\sim$.

*(B) In $E(O)$, same $\gamma$, different $W$.* Allowed. Several geodesics, possibly in several topologies, can share one observer-space curve. They are many spacetime paths and one observer-space path. That is multiplicity of hitchhikers as *ensemble members*, not as distinct evolutions. $M$ counts occurrences. $N$ may count ensemble geodesics. Neither number enters $\sim$.

*(C) In $\mathrm{Obs}$, but the curves fail to be real-analytic across $\tau_*$.* Possible only with a hypothesis that has not been locked: that a curve in $\mathrm{Obs}$ need not be a real-analytic map of $\tau$, even when each $W$ is real-analytic. Concatenating two analytic pieces at $\tau_*$ is not analytic at $\tau_*$ unless all one-sided derivatives match. Theorem 2 would then not apply. This would be a property of $\Phi$, or of the mapping $\pi_W$ when $W$ is switched. $\Phi$ is not written here. This route is named as an open cost, not taken.

**EKT 1991.** Existence proof that classical geodesic evolution need not be globally unique (wormhole / CTC boundary-value problems). Picture for “doesn’t know / knows,” i.e. for $\tau_*$ as first disagreement of $P$. Not $\Phi$. Not a licence to fork one analytic $g$ on a connected patch. Not a licence to fork one analytic $\gamma$.

---

## 6. Simply connectedness: two different spaces

Simple connectedness of the *patch* $P(O)$ is locked: that is what makes $j_\infty$ determine $P$ and $P$ determine $j_\infty$.

Simple connectedness of *observer space* $\mathrm{Obs}$ is a different statement. A loop in $\mathrm{Obs}$ is a loop of germs, not a loop in some $W$. Nothing in Theorems 1–2, and nothing in the locked object, forces $\pi_1(\mathrm{Obs})=0$. David’s inclination is recorded as an inclination. It is not a theorem, and it is not used.

If $\mathrm{Obs}$ were simply connected, that would constrain loops of observers. It would not create a fork of analytic $\gamma$, and it would not kill the ensemble $E(O)$.

---

## 7. Open list

What would count as an answer is stated. Preferences are not answers.

**O1. Is $\mathrm{Obs}$ simply connected?**
What would count: a determination of $\pi_1(\mathrm{Obs})$, after a specified mathematical home for $\mathrm{Obs}$ (still open; Fréchet / inverse limit of analytic jets, and how $u$ sits in it). An inclination does not count. Simple connectedness of $P(O)$ does not count as simple connectedness of $\mathrm{Obs}$.

**O2. Properties of $E(O)$.**
What would count: a precise category of allowed $W$ (real-analytic Lorentzian 4-manifolds, possibly with stated completeness or causality conditions, or not), a precise notion of occurrence $\iota$, and a statement of when two pairs $(W,\iota)$, $(W',\iota')$ are the same element of $E(O)$. Whether $E(O)$ is a set or a proper class is part of the answer. Counting $M$ occurrences must not smuggle $|a|^2$.

**O3. Is the mapping observer-path $\leftrightarrow$ spacetime-path well-defined?**
One direction is well-defined (Proposition in §4): $\pi_W(\sigma)=\gamma$. The reverse is not a function. What would count as “well-defined both ways”: a section of $\pi$ (a rule that picks, for each $\gamma$, a unique $(W,\sigma)$). That would reconstruct a unique spacetime path from an observer path. It is not assumed. It would be a new piece of theory, and it is adjacent to the discarded unique-cosmos reconstruction. A correspondence (a relation, not a function) is the coherent default.

**O4. What would count as $\Phi$ later.**
A multi-valued map $\Phi:\mathrm{Obs}\times\mathbb{R}_{\ge 0}\to\mathcal{P}(\mathrm{Obs})$ whose solution curves from a root $O$ are the evolutions in $\mathrm{Evol}(O)$, classical in character, not unique, not Hilbert-space, not a reconstruction of $W$, gauge-agnostic on presentations of the same lump. If $\Phi$ is required to have analytic solution curves in $\mathrm{Obs}$, Theorem 2 forbids positive-length shared prefixes among distinct solutions; the tree of evolutions would then have to split at $\tau_*=0$ or not split in $\mathrm{Obs}$ at all. If $\Phi$ is allowed to produce curves that are only piecewise analytic, a split at $\tau_*>0$ in $\mathrm{Obs}$ becomes possible, at the cost of making $\Phi$ fail analytic continuation in $\tau$. That choice is not made here. $\Phi$ is not written.

**O5. Countability and the measure.**
Still conditional. Nothing in this note supplies a countable set of distinct evolutions. Ensemble cardinality is not that count. $|a|^2$ is not that count.

---

## 8. Report line

- **Coherent formulation:** yes, if path-in-$W$, path-in-$\mathrm{Obs}$, and ensemble membership stay three things. Mapping $\pi_W$ is well-defined one way and many-to-one.
- **Proved:** Theorem 1 (no fork of one analytic $g$ on a connected patch). Theorem 2 (no fork of one analytic curve in $\mathrm{Obs}$).
- **Allowed:** distinct topologies as distinct elements of $E(O)$; multiplicity $M$ of occurrences; many spacetime paths for one observer-space path.
- **Not allowed, unless a new hypothesis is locked:** two distinct $\sim$-inequivalent evolutions that are real-analytic as curves in $\mathrm{Obs}$ and share a prefix of length $\tau_*>0$.
- **Needs a hypothesis we have not locked:** if David’s “agree up to $\tau_*$, disagree after” is a statement about *curves in* $\mathrm{Obs}$, then those curves are not jointly real-analytic across $\tau_*$. If it is a statement about *geodesics in various* $W\in E(O)$ that share one $\gamma$, no new hypothesis is needed and $\sim$ does not see the split.
- **Not done:** $\Phi$; unique $W$ from $O$; folding $E(O)$ into $\sim$; Born.

---

## References

Echeverria, F., Klinkhammer, G., and Thorne, K. S. Billiard balls in wormhole spacetimes with closed timelike curves: Classical theory. *Physical Review D* 44 (1991) 1077--1099.

Krantz, S. G. and Parks, H. R. *A Primer of Real Analytic Functions.* 2nd ed. Birkhäuser, 2002.

Strayhorn, D. Observer space: jet-patch equivalence. `papers/observer-space-geometry.md`.

Strayhorn, D. Theorem: the simply-connected analytic patch from an infinite jet. `papers/analytic-patch-from-jet.md`.

Strayhorn, D. Cheat sheet: names and symbols. `papers/cheat-sheet.md`.
