# Creative batch 08: L28 toward rigour (Creative Lead; proposal, do not merge)

**Status.** Exploration only, under David's 3:14 PM ET ruling and his 3:53 PM ET **working assumptions** (ledger; relayed, not signed): memory of received signals is allowed, and splitting with identical patches is allowed. These are not changes to the paper; nothing goes into `versions/` or `papers/`. Lead set: L28 (batch 07 Set 2). Citations are **unchecked** unless marked V-text/V-meta per #353. Every result here is a **proof sketch**, not a proof, unless it says otherwise.

## For David (one minute)

The observer keeps a diary of its own light coming back to it around the universe's handles: when each echo arrives, from which direction, and when it was sent. Free fall is perfectly predictable in each possible world, so each world writes exactly one diary. Two worlds are on different branches the moment their diaries differ. That is the whole split rule: branch A is "the diary world A writes". In a universe whose unrolled shape has a rigid repeating pattern (a "crystal" universe), only finitely many diaries are possible at any moment, and countably many over all time. So we can try counting worlds per branch, as a labelled conjecture. The count is infinite as it stands, though. It only becomes finite if worlds are listed by size, and the conjecture is that the share of each branch settles to a fixed fraction however the list is cut. Two honest problems remain. Perfectly smooth, uniform universes give a continuum of diaries, and rounding the diary off would just be coarse-graining in disguise. Accelerating universes may send back few or no echoes, so they branch little or not at all. That isn't a contradiction, but it means this mechanism works best for small (microscopic) handles.

---

## (a) The memory-augmented state

- **Germ part.** $O(\tau)=(j_\infty(\tau),u(\tau))$ modulo isotropy (v0.10.1 §4; #324), as before.
- **Emission.** The observer carries a test beacon (a body; cost C3 below). It emits continuously in all directions, and each signal is stamped with its emission proper time $t_e$. The signals are a test field and do not change $g$.
- **Record.** $\rho(\tau)$ is the set of received self-signal events $r=(s,t_e,\hat n)$:
  - $s\le\tau$ is the arrival proper time;
  - $t_e<s$ is the emission stamp, which is what identifies the signal as the observer's own;
  - $\hat n$ is the arrival direction.
- **Gauge (#324).** A direction needs a frame, and the frame is defined only up to the isotropy of the germ. So the record keeps $\hat n$ only through **isotropy invariants**: the angles between pairs of recorded arrival directions, all transported to a common time by Fermi–Walker transport along $\gamma$. The first recorded direction carries no information on its own. This is the minimal choice that is invariant under #324 (sketch).
- **State.** $\hat O(\tau)=(O(\tau),\rho(\tau))$.
- **Update.** $\rho$ only grows: $\rho(\tau')=\rho(\tau)\cup\{r: \tau<s\le\tau'\}$. Nothing is forgotten (working assumption 1).
- **When signals arrive.** In a host $W=\tilde M/\Gamma$ ($\tilde M$ is its own universal cover; #352), a self-signal emitted at $t_e$ arrives at $s$ exactly when, for some deck element $g\ne1$, a future null geodesic in $\tilde M$ runs from $g\tilde\gamma(t_e)$ to $\tilde\gamma(s)$. Each such $g$ gives an arrival map $t_e\mapsto s_g(t_e)$.
- **Determinism.** Given $W$, the record history is unique, because free fall is unique (Prop 3.2) and null geodesics are unique given their data.
- **Open item (ledger).** How the memory is stored, and whether it is part of the state itself, is open (David, 3:53 PM).

## (b) Split rule

- **Rule.** Compatible hosts $W_1,W_2$ (sharing $\hat O(0)$) are on the **same branch at $\tau$** iff $\rho_1(\tau')=\rho_2(\tau')$ for all $\tau'\le\tau$. Since records only grow, this is just $\rho_1(\tau)=\rho_2(\tau)$. A branch at $\tau$ is an equivalence class of hosts under this relation.
- **Split time.** $\tau^*=\inf\{\tau:\rho_1(\tau)\ne\rho_2(\tau)\}$.
- **The disagreement shows at $\tau^*$ itself.** The record is closed under arrival at time $s$, so if one host has an arrival at $\tau^*$ that the other lacks, the states differ *at* $\tau^*$. Compare #346 (c), where germs agree at $\tau^*$.
- **Reconciliation with Paper 1.** Paper 1's distinctness relation $\sim$ "compares the $\gamma_k$, not the $W_k$", and "Topology labels do not enter $\sim$" (`papers/analytic-split.md`). This rule extends $\mathrm{Obs}$ to $\mathrm{Obs}\times\mathrm{Rec}$ and compares the curves $\hat\gamma=(\gamma,\rho)$. It **reduces to Paper 1's rule when all records are empty**, e.g. in simply connected hosts.
- **Conflict, stated plainly.** Two hosts with identical $\gamma$ but different $\rho$ are *distinct* here and *not distinct* in Paper 1. A record is an observed event rather than a topology label, but it is host data that is not in the germ. This conflict is accepted under David's working assumption 2; it is not resolved.
- **Nested prefix (#345 caveat).** A host whose geodesic ends early is a *prefix*, as before. Splits by record are not prefixes, because both hosts continue (#352).

## (c) What makes the partition countable or finite

- **Per host.** Γ is a discrete subgroup of a Lie group, so it is countable. Proper discontinuity means only finitely many translates $g\tilde\gamma$ meet the compact past region $J^-(\tilde\gamma(\tau))\cap\{\text{emission times}\in[0,\tau]\}$. So each host has **finitely many arrival branches $g$ by any finite $\tau$** (sketch; it needs that compact region and global hyperbolicity of $\tilde M$).
- **Across hosts: the pointed problem.** In a cover with a continuous isometry group, conjugating Γ by an isometry moves the observer within the quotient. Pointed hosts $(W,p,u)$ then form a **continuum**, even when the unpointed ones are countable. This is the case for cocompact hyperbolic $\mathbb R\times\mathbb H^3/\Gamma$ with exact FLRW symmetry; Mostow/Prasad (V-meta per #353) counts unpointed $W$ only. So #352's countable case is countable **only after the observer's position is forgotten**, which the record does not do.
- **Countable host class (proposed): crystal covers.**
  - $\tilde M$ has a **discrete**, cocompact isometry group $G$: periodic but inhomogeneous, so the germ pins the observer's position relative to the pattern.
  - Γ ranges over finite-index, torsion-free subgroups of $G$ with no element mapping a point into its own chronological future (#352).
  - Finite-index subgroups of a finitely generated group are countable (standard, unchecked).
- **Result for crystal covers (sketch).**
  - At each finite $\tau$, the realised records come from finitely many deck elements, giving a **finite partition at each $\tau$**.
  - Over all time the partition is **countable cumulatively**.
  - Distinct Γ should eventually give distinct records, since the arrival set encodes Γ's orbit of the worldline. This is unchecked when there are coincident arrival maps.
- **Other classes.**
  - Flat, infinite-volume hyperbolic, 2+1 Teichmüller and AdS₃/BTZ quotients are continua (#352). dS is unchecked.
  - Exactly homogeneous covers give pointed continua (above).

## (d) Counting worlds per branch (labelled conjecture)

**Label: conjecture: count gives Born (to be derived, not assumed).** This is kept separate from (M1), which is unchanged at L3. Under (M1), each record-class at a split would get an equal share however many hosts it holds.

- **The raw count is infinite.** For a crystal cover, any finite record is consistent with **infinitely many** finite-index Γ: their short elements match the record, and their long elements are unconstrained. So the naive $N_b(\tau)$ is infinite for every branch.
- **How the worlds become countable *and* finitely counted.**
  - Order hosts by index $[G:\Gamma]$, which is proportional to spatial volume: a geometric quantity, not a free label.
  - Count $N_b(\tau;n)=\#\{\Gamma:[G:\Gamma]\le n,\ \rho_\Gamma(\tau)=\rho_b\}$, which is finite for each $n$.
  - Take the branch share $f_b(\tau)=\lim_{n\to\infty}N_b(\tau;n)/\sum_{b'}N_{b'}(\tau;n)$, if it exists. That subgroups of finite index are finitely many for each $n$ is standard subgroup-growth theory (Lubotzky–Segal, unchecked).
- **What would make the count inevitable (standing rule).** The same $f_b$ must come out of *every* natural exhaustion: by index, by volume, by systole, by word length. If it does, ordering by volume is not a choice. If the limits differ, the ordering is a measure by fiat, and that is the L23 hazard.
- **No result claimed.** No weights are computed, and no Born or $|a|^2$ claim is made. Whether $f_b$ has anything to do with quantum weights is the conjecture, and nothing here supports it yet.

## (e) The flat-case continuum of return times

- **Finite resolution.** Record arrival times only to resolution $\delta$. The partition becomes countable, but $\delta$ is a grain. The hosts in each cell are still a continuum (lattice moduli), so counting worlds per cell needs a measure on moduli. **This is a disguised coarse-graining**: it fails both the no-measure and the no-fiat rule.
- **Discrete-event record.** Record only the integer number of returns so far (no times, no directions). This needs no $\delta$ and gives a countable partition of *records*. But each branch still holds a continuum of hosts, so counting fails, and discarding data the observer receives is a choice of what memory stores. That ties to the open item. It would be honest **only if** a physical account of storage (the open item) showed the record cannot hold more. Otherwise it is coarse-graining.
- **Verdict.** Neither approach makes the flat case countable in *worlds* without a measure or a fiat. The flat case stays a continuum, and the countable story is restricted to crystal covers (c).

## (f) Accelerating expansion and no return

- **What happens.** In a host with accelerated expansion (dS-like at late times), the observer has an event horizon. Self-signals return only around loops shorter than the horizon scale, so the cumulative record is **finite, possibly empty** (sketch; unchecked for specific models).
- **Reading.** It is a host with few or no splits: the compatible set stops splitting, and nothing contradicts the framework, since branching was never guaranteed. It does **not** restrict the theory to non-accelerating hosts.
- **Cost, stated honestly.** Our universe appears to accelerate, and large-scale topology is observationally constrained (Planck 2015 XVIII, V-text per #353; Cornish–Spergel–Starkman 1998, V-text per #353). So for *cosmic* handles this mechanism may be empty in practice. It is live mainly for the charter's **microscopic** handles at scale $\ell$, where returns take time of order $\ell$ and repeat many times even under acceleration. That pushes the story toward the micro-topology picture, with costs not yet assessed: a test beacon at scale $\ell$, and records of very frequent events.

## Costs (carried)

- C1: the state is non-local, which breaks the germ-only definition (#352). This is a working assumption, not a change to the paper.
- C2: #324's gauge quotient must act on records (handled minimally in (a), sketch).
- C3: emission needs a body or beacon; the framework's observer is a germ.
- C4: the split rule conflicts with Paper 1's $\sim$ (b).

## Weak points

1. The countable case needs crystal covers: an inhomogeneous, exactly periodic universe.
2. The count needs an exhaustion, and inevitability means exhaustion-independence, which is unproved.
3. Distinct Γ are assumed to give distinct records, which is unchecked.
4. Flat covers stay a continuum.
5. In accelerating hosts the mechanism is empty at cosmic scale and untested at micro scale.
6. Everything is a sketch.
