# Geometry quick verdict: creative batch 08 (#354) — do not merge

**Read at:** #354 head `dbbaaa2` (`notes/creative/batch-08.md`), main `e41412b`.

**Record type:** rough review. It applies nothing and is neutral on David's open calls (exploration under the 3:14 PM ET ruling and the 3:53 PM ET working assumptions). Counting worlds is a labelled working conjecture (David, 3:47 PM ET), separate from (M1), which stays at L3. It is not called circular here; this review checks only well-posedness and cutoff independence. Every argument below is a sketch, not a proof. **(U)** marks claims from memory that were not checked.

**Verdicts.**
- **(a,b)** Well-posed as mathematics, given a beacon (a body) and exact real-valued entries. Two caveats:
  - the record is a union of arrival *curves*, not of discrete events;
  - the "split shows at $\tau^*$" claim needs the beacon to switch on at a definite time.
- **(c)** Confirmed. The pointed versus unpointed distinction is drawn correctly, and the crystal case is countable, with a finite partition at each time. Counting subgroups (not conjugacy classes) counts *pointed* hosts, which is the right object for records.
- **(d)** For $\mathbb Z^3$-type crystals, the index/volume limit appears to exist but is **degenerate**: share 1 for "no echo yet" and 0 for every other branch, at every fixed $\tau$. Exhaustion by systole is not finite. As it stands the count gives no non-trivial weights.
- **(e)** Agreed: both proposed fixes are coarse-graining or a fiat.
- **(f)** Agreed, and the micro-handle escape inherits (d).
- **Not flagged** for a full note.

## (a,b) Memory-augmented state and split rule

- **What the record is.** With continuous emission, each deck element $g$ contributes a *curve* $t_e\mapsto(s_g(t_e),\hat n_g(t_e))$. So $\rho(\tau)$ is a finite union of arcs, stored with exact real values. There is no resolution, and exactness is what keeps (e)'s $\delta$ out. A record of real-valued arcs is well-posed. Whether a body can *store* it is the open item.
- **Gauge (#324).** Keeping only the angles between arrival directions, transported by Fermi–Walker along $\gamma$, is invariant. It is minimal for germs with non-trivial isotropy. For a germ with trivial isotropy it discards information unnecessarily (the absolute directions would already be gauge-fixed). The stamps $t_e$ and the times $s$ are invariant. Note what the isotropy quotient does: two pointed crystal hosts whose subgroups are conjugate by an isotropy element give identical records. That is correct, because those pointed hosts are isometric.
- **Body.** Emission requires a beacon, a source of a test field (C3). The framework's observer has none. This is accepted as a working cost.
- **Split at $\tau^*$.** If emission starts at $\tau=0$, each $g$'s first arrival is a minimum (continuous map on a compact set), and the claim holds. If the beacon has always been emitting, any $g$ that has ever returned is already in $\rho(0)$. In that case "compatible" (equal $\hat O(0)$) already separates hosts at $\tau=0$. That should be stated.
- **Conflict with Paper 1's $\sim$ (C4).** Stated correctly, and accepted under working assumption 2. No comment.

## (c) Countable versus continuum

- **Pointed versus unpointed: confirmed, and E_W versus E_M is drawn right.**
  - In cocompact $\mathbb R\times\mathbb H^3/\Gamma$ with exact FLRW symmetry, every point of one quotient has the same germ. So $E_W(O)$, the pointed hosts, is already a continuum within a single $W$. $E_M(O)$, which drops the point, is countable (Mostow/Prasad, V-meta per #353).
  - Records see position: the lengths of loops at $p$ vary with $p$. So records split the pointed continuum.
  - Equivalently, conjugating $\Gamma$ by $h\in\mathrm{Isom}(\mathbb H^3)\cong PSL(2,\mathbb C)$ gives isometric quotients with the observer at different points. The batch's claim is right.
- **Crystal covers: "pinned by the germ" is well-posed under two assumptions:**
  1. The germ fixes $\tilde M$. That holds up to the non-unique extensions of #352 (1), so it should be fixed per cover.
  2. Equal germs at two points of a simply connected analytic $\tilde M$ are related by an isometry of $\tilde M$ (extension of local isometries; Nomizu-type, needs completeness or inextendibility (U)).

  Then the points with the observer's germ form one $G$-orbit, and position is pinned mod $G$.
  - In $W=\tilde M/\Gamma$ there are $[G:\Gamma]$ points with that germ, related by cosets. With $\tilde p$ fixed, **pointed hosts correspond to subgroups $\Gamma$**, while unpointed hosts correspond to conjugacy classes. The batch counts subgroups, so it counts pointed hosts, which is consistent with records. For abelian $G$ the two counts coincide; for non-abelian $G$ they do not, and this matters for (d).
- **Distinct records.** If the stabiliser of $\tilde\gamma$ in $G$ is trivial, the full ($\tau\to\infty$) record recovers the orbit $\Gamma\tilde\gamma$ as a set of worldlines, and hence $\Gamma$. So distinct pointed hosts give distinct full records (sketch). At finite $\tau$ the record sees only $\Gamma\cap F_\tau$, where $F_\tau$ is the finite set of elements that can have returned. Subgroups that share their short elements then agree, so the partition at $\tau$ is coarser: it has at most $2^{|F_\tau|}$ cells, which is finite. The batch's "finite at each $\tau$, countable cumulatively" is confirmed.
- **Existence of crystal covers.** Generic $\mathbb Z^3$-periodic vacuum data should have isometry group exactly $\mathbb Z^3$ (genericity in a topology, not a measure; (U)). But the crystal covers themselves form a continuum. The countability is *within one cover*, which is fine because the germ fixes the cover.

## (d) Counting worlds per branch and cutoff independence

- **Index / volume exhaustion for $G\supseteq\mathbb Z^3$ (sketch).**
  - The number of subgroups of index $\le N$ in $\mathbb Z^3$ grows like $cN^3$ (subgroup growth; Lubotzky–Segal 2003 (U); exact $a_n(\mathbb Z^3)$ formula (U)).
  - The subgroups that contain a fixed non-zero $v$ correspond to subgroups of $\mathbb Z^3/\langle v\rangle$ up to the torsion factor, and grow like $N^2$ (U). So the fraction of subgroups containing **any** element of the finite set $F_\tau$ tends to 0.
  - Hence $f_{\text{empty}}(\tau)=1$ and $f_b(\tau)=0$ for every branch $b$ with an echo, at every fixed $\tau$. The limit exists but is degenerate: counting says, with share 1, that the observer has not yet seen itself.
  - Letting $\tau$ grow with $N$ is a joint limit, which is a further choice.
- **Other exhaustions.**
  - **Systole $\le L$:** not a finite exhaustion. Infinitely many subgroups contain a short vector.
  - **Diameter $\le D$:** bounds the volume, so it is finite. Plausibly it gives the same degenerate limit (U).
  - **Word length:** ill-posed until it is said whose generators, and of what (the generators of $\Gamma$? an element bound?).
  - So the standing rule "same $f_b$ from every natural exhaustion" fails at the first step for systole. Where it can be posed, it yields the trivial distribution.
- **Pointed versus unpointed.** Counting conjugacy classes ($E_M$) instead of subgroups ($E_W$) changes the counts for non-abelian $G$. Which one counting worlds means must be named.
- **Net.** The conjecture is well-posed for index or diameter cutoffs on crystal covers. Its first computable output is degenerate weights, not a candidate amplitude. No Born-type claim is made, and none is supported.

## (e) The flat-case continuum

Agreed. A resolution $\delta$ is a grain, and a counting-only record discards data by fiat. Both leave a continuum of hosts per cell, so they need a measure on moduli. The flat case stays a continuum.

## (f) Accelerating expansion

Agreed: few or no echoes is not a contradiction. The micro-handle escape at scale $\ell$ makes records grow fast, but it inherits (d)'s degenerate count and the beacon cost at scale $\ell$. The observational constraints are cited as V-text per #353; they were not rechecked here.

**Citations (U):** Lubotzky–Segal, *Subgroup Growth* (2003); the subgroup counts for $\mathbb Z^3$; the Nomizu-type extension theorem; genericity of $\mathbb Z^3$-only isometry. In-repo: #324, #336, #346, #352, #353.
