# Cheat sheet: names and symbols

David Strayhorn

One table for the locked objects and the maps between them. It does not change the object. It does not write $\Phi$. Companion: `papers/observer-space-geometry.md`, `papers/analytic-patch-from-jet.md`, `papers/analytic-split.md`.

---

| Name | Symbol | What it is | What it is not |
|---|---|---|---|
| Elementary observer / germ | $O=(j_\infty,u)$ | Infinite jet of a real-analytic Lorentzian metric at a point $p$, plus a future unit timelike vector $u$ compatible with the $0$-jet | A Hilbert-space ray; a 4-velocity on a spacetime already given; a finite $k$-jet; a $C^\infty$ jet (Borel) |
| Simply-connected analytic patch | $P(j_\infty,u)$ | The unique (up to germ / maximal pointed isometry) simply-connected real-analytic Lorentzian patch realizing that jet, with time direction $u$ at the basepoint. Local continuation only | A completed four-manifold; a unique cosmos reconstructed from $O$ |
| Spacetime | $W$ | A real-analytic Lorentzian 4-manifold, any global topology, typically connected, not required to be simply connected | The elementary observer; the unique analytic continuation of $O$ |
| Observer space | $\mathrm{Obs}$ | The space of elementary observers: pairs $(j_\infty,u)$, equivalently simply-connected patches $P$ | Gielen–Wise’s 7-manifold of 4-velocities; Hilbert space; the union of ensembles |
| Ensemble of an observer | $E(O)$ | Pointed spacetimes that contain the germ $O$. If the germ occurs $M$ times in $W$, then $W$ appears in $E(O)$ $M$ times. Distinct $W$ may differ mainly by topology / monodromy | Extra elementary observers; extra points of $\mathrm{Obs}$; a Hilbert space of branches |
| Multiplicity | $M$ | Number of occurrences of the germ $O$ in a given $W$. That $W$ is counted $M$ times in $E(O)$ | Born weight; $\vert a\vert^2$; a factor that enters $\sim$ |
| Geodesic in spacetime | $\sigma:I\to W$ | A causal geodesic of $W$, parameterized by proper time $\tau$. A path *through spacetime* | A path through observer space |
| Curve in observer space | $\gamma:I\to\mathrm{Obs}$ | $\tau\mapsto\bigl(j_\infty(\tau),u(\tau)\bigr)$, equivalently $\tau\mapsto P(\tau)$. A path *through observer space* | A geodesic of some $W$; a path through spacetime |
| Mapping | $\pi_W(\sigma)=\gamma$ | Read the germ of $W$ at $\sigma(\tau)$, plus $\dot\sigma(\tau)$ as $u(\tau)$. Sends a spacetime path to an observer-space path. Many-to-one: many $(W,\sigma)$ can give the same $\gamma$ | A reconstruction of a unique $W$ from $\gamma$; an identification of the two kinds of path |
| Split time | $\tau_*$ | For two curves $\gamma,\gamma'$ in $\mathrm{Obs}$, $\tau_*=\inf\{\tau:\gamma(\tau)\ne\gamma'(\tau)\}$ (with $\inf\emptyset=\infty$) | A decoherence time; a Born-weighted branch time |
| Individuation cut | $\gamma\sim\gamma'$ | $\gamma(\tau)=\gamma'(\tau)$ as elementary objects for every $\tau$ (jets and $u$ agree, equivalently the simply-connected patches agree). Distinct iff $\tau_*<\infty$. Topology labels and amplitude stay out | Equality of $W$’s; equality of ensemble members; a decoherence-branch label |

Hard distinction, one line: a path through spacetime is $\sigma$ in some $W$; a path through observer space is $\gamma$ in $\mathrm{Obs}$; the mapping $\pi_W$ goes from the first to the second and is not invertible.

---

## Short dictionary

- **Hitchhiking.** The elementary observer is carried along a trajectory: at each $\tau$ one reads the local germ, not a global label of $W$.
- **Same lump, two names.** $O=(j_\infty,u)$ and $P(j_\infty,u)$ are equivalent on simply-connected real-analytic patches (`papers/analytic-patch-from-jet.md`).
- **Not $W$.** Analytic continuation of the jet stops at the local patch. Completing to a unique cosmos is the 2008 reconstruction and is not used.
- **Ensemble is relative.** Drop simple connectedness and one jet can determine several patches, one per topology / monodromy. Those are $E(O)$, not extra points of $\mathrm{Obs}$, and they are not folded into $\sim$.
- **Analytic split.** Two distinct *analytic* curves in $\mathrm{Obs}$ cannot agree on a positive-length initial interval. Identity theorem on a connected *patch* forbids a fork of one metric $g$. Identity theorem in one real variable forbids a fork of one analytic $\gamma$. See `papers/analytic-split.md`.

