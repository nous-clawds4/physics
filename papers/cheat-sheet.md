# Cheat sheet: names and symbols

David Strayhorn

One table for the locked objects and the maps between them. It does not change the object. It does not write $\Phi$. Companions: `papers/observer-space-geometry.md`, `papers/analytic-patch-from-jet.md`, `papers/analytic-split.md`, `papers/geodesic-lifts.md`, `papers/ensemble-labels.md`, `papers/typicality-under-the-lock.md`, `papers/patch-edge.md`, `papers/phi-straits.md`, `papers/obs-as-a-set.md`, `papers/tree-as-structure.md`, `papers/type-ii-adopted.md`, `papers/law-of-r.md`, `papers/fusion-and-path-counting.md`.

---

| Name | Symbol | What it is | What it is not |
|---|---|---|---|
| Elementary observer / germ | $O=(j_\infty,u)$ | Infinite jet of a real-analytic Lorentzian metric at a point $p$, plus a future unit timelike vector $u$ compatible with the $0$-jet | A Hilbert-space ray; a 4-velocity on a spacetime already given; a finite $k$-jet; a $C^\infty$ jet (Borel) |
| Simply-connected analytic patch | $P(j_\infty,u)$ | The unique (up to germ / maximal pointed isometry) simply-connected real-analytic Lorentzian patch realizing that jet, with time direction $u$ at the basepoint. Local continuation only | A completed four-manifold; a unique cosmos reconstructed from $O$ |
| Spacetime | $W$ | A real-analytic Lorentzian 4-manifold, any global topology, typically connected, not required to be simply connected | The elementary observer; the unique analytic continuation of $O$ |
| Observer space (as a set) | $\mathrm{Obs}=\mathcal{P}/{\sim_L}$ | Set of lumps: coordinate presentations at $0\in\mathbb{R}^4$ modulo pointed germ equivalence (Thm 10). $\sim$ and typicality of many $O$ range over this set | Raw coordinate jets; $\mathrm{Met}(M)/\mathrm{Diff}(M)$; Gielen–Wise’s 7-manifold; Hilbert space; $E(O)$; a manifold structure on $\mathrm{Obs}$ |
| Ensemble of an observer | $E(O)$ | Pointed analytic occurrences of the germ $O$, modulo pointed analytic isometry. If the germ occurs $M$ times in $W$, that $W$ contributes $M$ classes | Extra elementary observers; extra points of $\mathrm{Obs}$; extra curves in $\mathrm{Obs}$; a Hilbert-space of branches |
| Hitchhiking ensemble | $E_\gamma(O)$ | Those $[W,\iota]\in E(O)$ whose geodesic lift coincides with the unique curvelet $\gamma_O$ near $\tau=0$. Persists along $\gamma_O$ in $\mathrm{int}\,P(O)$ (Thm 4) | Extra hitchhikers; extra $\sim$-classes; a continuous motion of topologies |
| Fiber ensemble | $E_{\mathrm{pt}}(O')$ | $E(O')$ as a fiber over a point of $\mathrm{Obs}$. Can jump off the curvelet | The same object as $E_\gamma(O)$ |
| Multiplicity | $M$ | Number of occurrences of the germ $O$ in a given $W$ | Born weight; $\vert a\vert^2$; a factor that enters $\sim$ |
| Geodesic in spacetime | $\sigma:I\to W$ | A causal geodesic of $W$, parameterized by proper time $\tau$. A path *through spacetime* | A path through observer space |
| Curve in observer space | $\gamma:I\to\mathrm{Obs}$ | $\tau\mapsto\bigl(j_\infty(\tau),u(\tau)\bigr)$, equivalently $\tau\mapsto P(\tau)$. A path *through observer space* | A geodesic of some $W$; a path through spacetime |
| Curvelet from $O$ | $\gamma_O$ | The unique geodesic lift of $O$ in $P(O)$ (Prop. 3.2). One $\gamma$, many $W$ in $E_\gamma(O)$ | A star of lifts from one $O$; a delayed fork |
| Mapping | $\pi_W(\sigma)=\gamma$ | Read the germ of $W$ at $\sigma(\tau)$, plus $\dot\sigma(\tau)$ as $u(\tau)$. Many-to-one | A reconstruction of a unique $W$ from $\gamma$ |
| Split time | $\tau_*$ | $\inf\{\tau:\gamma(\tau)\ne\gamma'(\tau)\}$ ($\inf\emptyset=\infty$) | A decoherence time; a Born-weighted branch time |
| Patch lifetime | $\tau_\partial$ | $\sup\{\tau\ge 0:\ \sigma_O\text{ is defined in }P(O)\text{ on }[0,\tau]\}$. May be finite or infinite (Thm 6) | A decoherence time; a guaranteed last time for every germ |
| Lump equivalence | $\sim_L$ | Germ equivalence of Theorem A: pointed analytic diffeomorphism sending $(p,u)$ to $(p',u')$ and pulling metrics. Two presentations of the same lump | Unpointed $\mathrm{Diff}(M)$; the individuation cut $\sim$ on curves; ensemble labels |
| Individuation cut | $\gamma\sim\gamma'$ | Elementary objects agree at every $\tau$. Topology labels and amplitude stay out | Equality of $W$’s; equality of ensemble members; $\sim_L$ on presentations |
| Type-(ii) transition | $R$ | Working across-worlds stand-in: extra edges of a transition structure that are not geodesic lifts. Abandonable. Delayed forks allowed as graph-paths | The 2007 geodesic-generated tree; $1/N$; a locked grain; $\Phi$; a theorem of hitchhiking |

Hard distinction, one line: a path through spacetime is $\sigma$ in some $W$; a path through observer space is $\gamma$ in $\mathrm{Obs}$; the mapping $\pi_W$ goes from the first to the second and is not invertible.

Two ensembles, one line: $E_\gamma$ hitchhikes with $\gamma_O$ and stays put in $\mathrm{int}\,P(O)$; $E_{\mathrm{pt}}$ is the fiber over a moving germ and can jump off that curvelet.

---

## Theorems (pointers, not restated)

- **Thm 3.** Geodesic in real-analytic $W$ $\Rightarrow$ analytic curve in $\mathrm{Obs}$ (Fermi coordinates / inverse limit of $J^k$). Not a claim that $\mathrm{Obs}$ is an analytic manifold. `papers/geodesic-lifts.md`
- **Cor. 3.1 / Thm 2.** Analytic lifts with a positive-length prefix coincide. Delayed local “knows which path” is killed. `papers/analytic-split.md`, `papers/geodesic-lifts.md`
- **Prop. 3.2.** From one $O$, unique curvelet $\gamma_O$, not a star of geodesic lifts.
- **Thm 4.** $E_\gamma$ persists along $\gamma_O$ in $\mathrm{int}\,P(O)$; membership changes by jumps; $E_{\mathrm{pt}}$ can jump off the curvelet. `papers/ensemble-labels.md`
- **Thm 5.** No complete 4-manifold census (Markov). Compact Lorentzian $\Rightarrow\chi=0$. Countability of $E(O)$ is open.
- **Thm 6.** Lifetime $\tau_\partial$ in $P(O)$ may be finite or infinite; both occur. `papers/patch-edge.md`
- **Thm 7.** No $\sim$-split of next germs among $E_\gamma$ members at $\partial P$. Hitchhiker story dead at the boundary too. `papers/patch-edge.md`
- **Thm 8.** Under hitchhiking, typicality of branches from one $O$ is empty. `papers/phi-straits.md`
- **Thm 9.** Any $\Phi$ with real-analytic solution curves $I\to\mathrm{Obs}$ cannot delayed-fork. Analytic $W$+geodesics is one such. Concatenating disagreeing pieces at $\tau_\partial$ is not. $\Phi$ itself is not written. `papers/phi-straits.md`
- **Thm 10.** $\mathrm{Obs}=\mathcal{P}/{\sim_L}$ is a set of lumps. Not raw jets, not $\mathrm{Met}/\mathrm{Diff}$, not $E(O)$. Not a space. `papers/obs-as-a-set.md`
- **Thm 11.** 2007 across-worlds tree is not a theorem of the geodesic-analytic layer. `papers/original-two-layer.md`
- **Prop. 13.** Locked data at $O$ do not determine type-(ii) edges. Neighborhood-law for $R$ needs $\mathrm{Obs}$ as a space. `papers/type-ii-adopted.md`
- **Thm 16.** Fermi-slice topology (Fermi coordinates modulo $O(3)$) descends to a Hausdorff topology on $\mathrm{Obs}$. Formal-Fréchet on all presentations does not. `papers/obs-as-a-space.md`
- **Thm 17.** Open balls minus $\gamma_O$ are uncountable. Neighborhoods do not give countable type-(ii) successors. `papers/neighborhood-uncountable.md`
- **Thm 18.** Finitely many continuous functions on a connected open in $\mathrm{Obs}$ yield one class or a continuum. Grain is extra. `papers/grain-not-from-invariants.md`
- **Thm 19.** Named lock-side functors (data at $O$, open neighborhoods, continuous $f:\mathrm{Obs}\to\mathbb{R}^n$) do not supply a nonempty countable typicality set of delayed forks. Law of $R$ extra relative to those. Not a blanket “no map.” `papers/law-of-r.md`
- **Thm 20.** Walk-count is infinite if a cycle can be pumped. Strayhorn3 both-ways, as walks, is ill-defined. `papers/fusion-and-path-counting.md`
- **Thm 21.** On a DAG with finitely many walks $p\to q$, $N(p,q)$ is well-defined; fusion adds walks. Unique-tree extra. `papers/fusion-and-path-counting.md`
- **Thm 22.** Named non-slices (hitchhiker $\tau$, Fermi balls, continuous $f$, grain) fail to make $N(p,\cdot)$ a probability of type-(ii) targets. Not a closed “nothing supplies.” `papers/counting-needs-a-slice.md`
- **Thm 23.** Hitchhiker $\tau$ does not timestamp type (ii). Extra $W$ from $E(O)$ is $E$-smuggling. In-patch Lorentzian distance (sup) is lock-side, unique given a fixed $q$; leftover non-uniqueness is only multiple occurrence; not a general type-(ii) clock. `papers/type-ii-clock.md`
- **Thm 24.** Fermi-slice distance is a continuous scale, not a finite slice or generation. Rounding is a grain. `papers/fermi-distance.md`
- **Thm 25.** Continuous $y$ on a connected open does not finite-support $R$. Integer $y\in[0,Y]$ is a grain. Least-action-on-support named, not adopted. `papers/least-action-support.md`
- **Thm 26.** Combinatorial $y$ (edge count, Euler, out-degree) does not finite-support $R$ without a grain or a law of $R$ plus a slice. Compact Lorentzian $\chi=0$ (Poincaré–Hopf) does not select type-(ii) edges. `papers/combinatorial-y.md`
- **Thm 27.** $\mathrm{Occ}(O)\setminus\gamma_O$ is lock-side. Nonconstant curvature (or jet coefficient) $\Rightarrow$ continuum of lumps; local homogeneity $\Rightarrow$ Occ may collapse and $S$ may be empty. Restricting type-(ii) targets to it is not $E$-smuggling and does not grain. Named, not adopted. `papers/in-patch-support.md`
- **Thm 28.** Named lock-side subsets of $S(O)=\mathrm{Occ}(O)\setminus\gamma_O$ (Fermi spatial slice at one $\tau$, Cauchy surface in $P(O)$, integer curvature bins) are one class or a continuum, or smuggle a grain. Not a closed “no countable subset.” `papers/countable-in-patch.md`
- **Thm 29.** Morse of a curvature scalar is extra. Conjugate locus and cut locus of $p$ are typically continua after $q\mapsto O_q$. Lorentzian cut: geodesic ceases to *maximize* $\tau(p,q)$ (sup). Isolated conjugates along $\sigma_O$ are type (i). `papers/critical-points-in-patch.md`
- **Thm 30.** Chronological future in $P(O)$, Einstein/vacuum, and energy conditions do not finite-support $R$ without a grain. Named remainder: that well is dry as of this inventory. Not a closed “no constraint exists.” `papers/support-without-grain.md`
- **Def. 9.** Transition structure on lumps: $(V,R)$ with $V\subseteq\mathrm{Obs}$. A matrix only if $V$ is discrete. Not adopted. `papers/transition-matrix-on-lumps.md`

---

## Short dictionary

- **Hitchhiking.** The elementary observer is carried along a trajectory: at each $\tau$ one reads the local germ, not a global label of $W$.
- **Same lump, two names.** $O=(j_\infty,u)$ and $P(j_\infty,u)$ are equivalent on simply-connected real-analytic patches (`papers/analytic-patch-from-jet.md`).
- **Not $W$.** Analytic continuation of the jet stops at the local patch. Completing to a unique cosmos is the 2008 reconstruction and is not used.
- **Ensemble is relative.** Extra topologies are $E(O)$, not extra points of $\mathrm{Obs}$, and they are not folded into $\sim$. $E_\gamma$ members share $\gamma_O$; they are not extra hitchhikers.
- **Analytic split.** Two distinct *analytic* curves in $\mathrm{Obs}$ cannot agree on a positive-length initial interval. See `papers/analytic-split.md`.
- **Typicality under the lock.** No remaining typicality theorem without a new hypothesis that supplies a countable set of distinct evolutions. Unique-measure stays conditional. `papers/typicality-under-the-lock.md`
- **Straitjacket.** Analytic-curve $\Phi$ cannot delayed-fork. Gauge stays open; no measure on $\mathrm{Obs}$. `papers/phi-straits.md`
- **Type (ii).** Working across-worlds stand-in: extra links on lumps (2005 / Strayhorn3), abandonable. Not the 2007 geodesic-generated tree. Law of $R$ extra structure (Thm 19). `papers/type-ii-adopted.md`, `papers/law-of-r.md`
- **Obs as a set.** Lumps, not presentations and not occurrences. Gauge as a *space* stays open. No measure. `papers/obs-as-a-set.md`
