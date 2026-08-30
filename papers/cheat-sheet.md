# Cheat sheet: names and symbols

David Strayhorn

One table for the locked objects and the maps between them. It does not change the object. It does not write $\Phi$. Companions: `papers/observer-space-geometry.md`, `papers/analytic-patch-from-jet.md`, `papers/analytic-split.md`, `papers/geodesic-lifts.md`, `papers/ensemble-labels.md`, `papers/typicality-under-the-lock.md`.

---

| Name | Symbol | What it is | What it is not |
|---|---|---|---|
| Elementary observer / germ | $O=(j_\infty,u)$ | Infinite jet of a real-analytic Lorentzian metric at a point $p$, plus a future unit timelike vector $u$ compatible with the $0$-jet | A Hilbert-space ray; a 4-velocity on a spacetime already given; a finite $k$-jet; a $C^\infty$ jet (Borel) |
| Simply-connected analytic patch | $P(j_\infty,u)$ | The unique (up to germ / maximal pointed isometry) simply-connected real-analytic Lorentzian patch realizing that jet, with time direction $u$ at the basepoint. Local continuation only | A completed four-manifold; a unique cosmos reconstructed from $O$ |
| Spacetime | $W$ | A real-analytic Lorentzian 4-manifold, any global topology, typically connected, not required to be simply connected | The elementary observer; the unique analytic continuation of $O$ |
| Observer space | $\mathrm{Obs}$ | The space of elementary observers: pairs $(j_\infty,u)$, equivalently simply-connected patches $P$ | Gielen–Wise’s 7-manifold of 4-velocities; Hilbert space; the union of ensembles |
| Ensemble of an observer | $E(O)$ | Pointed analytic occurrences of the germ $O$, modulo pointed analytic isometry. If the germ occurs $M$ times in $W$, that $W$ contributes $M$ classes | Extra elementary observers; extra points of $\mathrm{Obs}$; extra curves in $\mathrm{Obs}$; a Hilbert-space of branches |
| Hitchhiking ensemble | $E_\gamma(O)$ | Those $[W,\iota]\in E(O)$ whose geodesic lift coincides with the unique curvelet $\gamma_O$ near $\tau=0$. Persists along $\gamma_O$ in $\mathrm{int}\,P(O)$ (Thm 4) | Extra hitchhikers; extra $\sim$-classes; a continuous motion of topologies |
| Fiber ensemble | $E_{\mathrm{pt}}(O')$ | $E(O')$ as a fiber over a point of $\mathrm{Obs}$. Can jump off the curvelet | The same object as $E_\gamma(O)$ |
| Multiplicity | $M$ | Number of occurrences of the germ $O$ in a given $W$ | Born weight; $\vert a\vert^2$; a factor that enters $\sim$ |
| Geodesic in spacetime | $\sigma:I\to W$ | A causal geodesic of $W$, parameterized by proper time $\tau$. A path *through spacetime* | A path through observer space |
| Curve in observer space | $\gamma:I\to\mathrm{Obs}$ | $\tau\mapsto\bigl(j_\infty(\tau),u(\tau)\bigr)$, equivalently $\tau\mapsto P(\tau)$. A path *through observer space* | A geodesic of some $W$; a path through spacetime |
| Curvelet from $O$ | $\gamma_O$ | The unique geodesic lift of $O$ in $P(O)$ (Prop. 3.2). One $\gamma$, many $W$ in $E_\gamma(O)$ | A star of lifts from one $O$; a delayed fork |
| Mapping | $\pi_W(\sigma)=\gamma$ | Read the germ of $W$ at $\sigma(\tau)$, plus $\dot\sigma(\tau)$ as $u(\tau)$. Many-to-one | A reconstruction of a unique $W$ from $\gamma$ |
| Split time | $\tau_*$ | $\inf\{\tau:\gamma(\tau)\ne\gamma'(\tau)\}$ ($\inf\emptyset=\infty$) | A decoherence time; a Born-weighted branch time |
| Individuation cut | $\gamma\sim\gamma'$ | Elementary objects agree at every $\tau$. Topology labels and amplitude stay out | Equality of $W$’s; equality of ensemble members |

Hard distinction, one line: a path through spacetime is $\sigma$ in some $W$; a path through observer space is $\gamma$ in $\mathrm{Obs}$; the mapping $\pi_W$ goes from the first to the second and is not invertible.

Two ensembles, one line: $E_\gamma$ hitchhikes with $\gamma_O$ and stays put in $\mathrm{int}\,P(O)$; $E_{\mathrm{pt}}$ is the fiber over a moving germ and can jump off that curvelet.

---

## Theorems (pointers, not restated)

- **Thm 3.** Geodesic in real-analytic $W$ $\Rightarrow$ analytic curve in $\mathrm{Obs}$ (Fermi coordinates / inverse limit of $J^k$). Not a claim that $\mathrm{Obs}$ is an analytic manifold. `papers/geodesic-lifts.md`
- **Cor. 3.1 / Thm 2.** Analytic lifts with a positive-length prefix coincide. Delayed local “knows which path” is killed. `papers/analytic-split.md`, `papers/geodesic-lifts.md`
- **Prop. 3.2.** From one $O$, unique curvelet $\gamma_O$, not a star of geodesic lifts.
- **Thm 4.** $E_\gamma$ persists along $\gamma_O$ in $\mathrm{int}\,P(O)$; membership changes by jumps; $E_{\mathrm{pt}}$ can jump off the curvelet. `papers/ensemble-labels.md`
- **Thm 5.** No complete 4-manifold census (Markov). Compact Lorentzian $\Rightarrow\chi=0$. Countability of $E(O)$ is open.

---

## Short dictionary

- **Hitchhiking.** The elementary observer is carried along a trajectory: at each $\tau$ one reads the local germ, not a global label of $W$.
- **Same lump, two names.** $O=(j_\infty,u)$ and $P(j_\infty,u)$ are equivalent on simply-connected real-analytic patches (`papers/analytic-patch-from-jet.md`).
- **Not $W$.** Analytic continuation of the jet stops at the local patch. Completing to a unique cosmos is the 2008 reconstruction and is not used.
- **Ensemble is relative.** Extra topologies are $E(O)$, not extra points of $\mathrm{Obs}$, and they are not folded into $\sim$. $E_\gamma$ members share $\gamma_O$; they are not extra hitchhikers.
- **Analytic split.** Two distinct *analytic* curves in $\mathrm{Obs}$ cannot agree on a positive-length initial interval. See `papers/analytic-split.md`.
- **Typicality under the lock.** No remaining typicality theorem without a new hypothesis that supplies a countable set of distinct evolutions. Unique-measure stays conditional. `papers/typicality-under-the-lock.md`
