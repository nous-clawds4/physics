# Zeno-mass convention: scoping note (options and costs only)

**Read at:** main `e493913` (`versions/v0.9-prose.md` §8.2 item 8, §8.3, §11, C7, C8, C29, C35). **Record:** #155 toy, v0.7-outline Geometry F2/RC2, Claude v0.7 row 10, #229 N8/N22, `born-rule-readiness.md` §3 item 4, `law-of-R-scoping.md` K6. **Revised** against main `56ad9b7` with the items of #258 confirmed or qualified in `reviews/zeno-and-born-readiness-pressure-test.md`. **Status:** scoping only. No reading is picked, and nothing in `versions/` is edited.

## What the Zeno mass is

- **Which histories.** *Zeno* histories: branch points accumulate at finite accumulated $\tau$ (including at a singular segment endpoint). Item 8: such a history **ends there**, outside EPP1's domain.
- **What mass.** The *Zeno mass* $z$ at a state is the per-vertex product mass of the Zeno histories through it, gate ignored (an Ionescu-Tulcea measure; finite stars). On C35's toy $z=1/2$.
- **Why it is undefined.** Hard-gate clause (2) "ranges over the histories through the state" (§8.3), and v0.9 leaves open whether that is before or after item 8's excision. Before, the gate fails at the root. After, the excised mass is kept or conditioned away, the two options v0.9 names; other conventions exist (the table adds (Z-vi), which changes the quantifier, and (Z-vii), which changes the arm set). v0.9 names (Z-i)–(Z-iii) and picks none (§11).

## Readings

$w(X)$ is the weight of arm $X$ in C35's toy. C35 leaves $X$'s subtree open ("ordinary thereafter"); per-vertex values do not depend on it, but counts do, and the counts below take $X$ to be a single history with no further branch point. V0 is C35 with one continuing arm of two below $Y$, so the Zeno set is a single history ($z=0$). V1 is C35 with $X$ also carrying the chain, so $z=1$. Values come from `zeno.py` and are exact. V2 has root arms $X$ (a single history) and $Y$; $Y$ has one vertex at $\tau=1/2$ with arms $Y_1$ (a single history) and $Y_2$, below which C35's chain runs at $\tau=1-2^{-k}$, $k\ge2$, so $z=1/4$. On V2, $w(X)$ is undefined under (Z-0), (Z-i) and (Z-vi), $1/2$ under (Z-ii) and (Z-vii), and $(1/2-0)/(1-1/4)=2/3$ under (Z-iii) (`zeno2.py`).

| Reading | (a) Definition | Well-defined when | $w(X)$: C35 / V0 / V1 |
|---|---|---|---|
| (Z-0) domain restriction | EPP1 is used only where no Zeno history passes through, where (Z-i)–(Z-iii) agree. v0.9 does not adopt this: it leaves the range of clause (2) open, and C35 lists three values | wherever no Zeno history passes through the state | undefined / undefined / undefined |
| (Z-i) | Clause (2) is checked over all histories through the state, before excision | as (Z-0); the gate fails at every ancestor of any Zeno history, whatever its mass | undefined / undefined / undefined |
| (Z-ii) | Excise first; the per-vertex product mass is kept, with Zeno histories counted as ended | wherever the per-vertex product is defined (finite stars) | $1/2$ / $1/2$ / $1/2$ |
| (Z-iii) | Excise, then condition: $w(X)=(w_{\rm ii}(X)-z_X)/(1-z)$, with $z_X=w_{\rm ii}(X)\,z(X)$ the root-measure mass of the Zeno histories through $X$ and $z=\sum_X z_X$ | $z<1$ | $1$ / $1/2$ / undefined ($0/0$) |
| (Z-vi) null-set gate | A variant of (Z-i) that changes clause (2)'s quantifier, not its range: clause (2) must hold for almost every history through the state, under the gate-ignored per-vertex product | iff $z=0$ at the state, where it equals (Z-ii) and (Z-iii) | undefined / $1/2$ / undefined |
| (Z-vii) arm pruning | Excise, then recompute the arms in force: an arm stays iff some non-Zeno history passes through it; equal shares over the arms that stay | wherever some arm stays | $1$ / $1/2$ / undefined |
| (Z-iv) cut limit | $\lim_{T\to1^-}$ of the weight at an accumulated-$\tau$ cut $T$, or along depth cuts. Per-vertex: the cylinder mass. Counts: the share of cut nodes | per-vertex: always, and it equals (Z-ii). Counts: iff the limit exists | C35: per-vertex $1/2$ at every cut. Counts: $1/(1+2^k)$ for $T\in[1-2^{-k},1-2^{-k-1})$, giving $1/3, 1/5, \dots, 1/1025$ at $k=10$, with limit $0$. V0 ($z=0$): per-vertex $1/2$; counts at the same cuts $1/(k+2)$, with limit $0$. V1: per-vertex $1/2$; counts $1/2$ at every cut |
| (Z-v) $\tau$-blindness | A requirement rather than a reading: weights are unchanged when vertex times are moved monotonically, keeping the tree (e.g. $1-2^{-k}\mapsto k$) | — | Under per-vertex weights it forces $1/2$, which is (Z-ii)'s; counts along depth cuts are also unchanged by such moves, but their value is set by $X$'s subtree, not by $\tau$-blindness: $0$ with $X$ a single history, $1/2$ at every depth if $X$ branches in two at every vertex. (Z-i) and (Z-iii) change under such moves: at $\tau=k$, $X$ has weight $1/2$ under both |
| (Z-viii) domain fidelity | A requirement rather than a reading, mirroring (Z-v): the Zeno set carries mass $0$ (item 8 places it outside EPP1's domain) | — | Wherever $z>0$ it excludes (Z-ii), per-vertex (Z-iv) and (Z-v), and on C35 also counting (Z-iv), whose limit gives weight $1$ to $Y$, all of whose histories are Zeno. It is met by (Z-iii) and (Z-vi) where they are defined, vacuously by (Z-0)/(Z-i), and by (Z-vii) only when pruning removes every Zeno history. It fixes no single value: on V2, (Z-iii) gives $2/3$ and (Z-vii) $1/2$ |

Per-vertex weights do not depend on the cut (§9). So at a cut $T\ge1$, past the accumulation, they give $X$ $1/2$ ((Z-ii)) under §9's dead-end convention. Under §9's alternative, counting survivors only and conditioning per vertex on survival, they give (Z-vii)'s value: $1$ on C35, equal there to (Z-iii)'s, and $1/2$ on V2, where (Z-iii) gives $2/3$. Counting (Z-iv) at $T\ge1$ meets a continuum of ended $Y$-histories: undefined under §9's dead-end convention, while the survivors-only alternative gives $1$ on C35. Under that convention any Zeno history makes $\tau$-cuts beyond its accumulation point infinite, so $\tau$-cut counts need $T$ below every accumulation point; depth cuts are unaffected. Its limit is $0\ne1/2$. With $X$ a single history the $\tau$-cuts are depth cuts, and §9's limit iff predicts $0$ for these unbalanced siblings; the $\tau$-cut limit $0$ holds for any non-Zeno $X$ with finite stars (König, §9 *Finite cuts*), while §9's iff covers depth cuts only.

## (b) Pins: where it bites, recomputed

- **Only C35 changes under the readings,** with the values in the table above. C35's cell already pins three of them: undefined, $1/2$ and $1$.
- **Under (A), the instance has an empty Zeno set (C7),** so every reading agrees on all instance pins, under (a) and without it. Without an arrival rule, the model without (a) has a non-empty Zeno set of mass $0$ (C5's jump chains; see (c)), so "only C35 changes" holds under (A).
  - Recomputed C7: the minimum half radial period over circular radii is $111.5901853$, at $r_0=7.64575131106459=5+\sqrt7$ (`c7.py`).
  - Eccentric orbits are longer: $[7,8.3]$ gives $112.471$, $[6.5,12]$ gives $127.722$ and $[10,20]$ gives $212.567$.
- **Unchanged under every reading:** C7, C29; C16 ((H6) half periods $[200.26,225.98]$); C33, including #169's exact law ($26/3^{12}$, $9338/3^{10}$, $447373/3^{12}$; 27.68 decisions); C34, C37; C12–C14 (finite trees or finite cuts, no accumulation); C15 and C36 (an infinite tree and walks on finite graphs, with no proper times assigned, so no Zeno set is defined). C8 is a slice fact with no $R$ or weight pinned, so no reading acts on it.

## (c) Open calls touched

| Reading | (M1)/(M2) | T1–T3 | #139 (a)–(e) | #230 F1–F12 |
|---|---|---|---|---|
| (Z-0)/(Z-i) | (M1) loses weights above any Zeno history | T1 (below) | (b) | F9 (status wording of the measure) |
| (Z-ii) | (M1) weights stay functions of the current state; positive weight sits on histories that item 8 ends (at a regular accumulation, by excision alone; at a singular endpoint, as in C8, the geometry ends there too) | T1 (below) | (b) (a named convention) | F9 |
| (Z-iii) | (M1) weights read $R$ ahead, so they are no longer depth-1 | T2 (per-step versus a distant quantity); T1, T3 (below) | (b) | F9, F10 (cost lines) |
| (Z-iv), counts | This is (M2)'s cut question; the value depends on the cut family (C14, C15) | T2 | (b) | F10 |
| (Z-v) | Constrains both sides | none | (b) | F9 |
| (Z-vi) | As (Z-i) where $z>0$, as (Z-ii) where $z=0$ | T1 (below) | (b) | F9 |
| (Z-vii) | (M1) weights read $R$ ahead, and the arm set in force departs from $A(O^u,a)$ (§8.2 items 6–7) | T2; T1, T3 (below) | (b) | F9, F10 |
| (Z-viii) | Constrains both sides | none | (b) | F9 |

Two links in the T1–T3 column. **T1** (and with it the proper-time part of #139 (a), which v0.9 files under T1), through C5: without an arrival rule, the instance's jump chains, infinitely many branch points at one value of accumulated $\tau$, are Zeno histories by item 8's first sentence, with total mass $0$ (more than $n$ consecutive jumps has weight $(2/3)^{n+1}$). Under (Z-0)/(Z-i), dropping (A) then leaves EPP1 no domain on the instance; under (Z-ii), (Z-iii), (Z-vi) and (Z-vii) the chains are a null set and EPP1 keeps one. The other costs of dropping (A) ((B) is law-like; (C) excludes the instance) are unchanged. **T3** (and #139 (a)), through (Z-iii) and (Z-vii): where $z>0$ they change the per-decision jump weight $m/(1+m)$ from which §9 derives (J1)/(J2) and C17's $R$-independent $(1+m)^{-n}$, in either direction (one decision with $m=2$: Zeno mass $1/2$ below each jump arm gives the jumps $1/2$ in total under (Z-iii); Zeno mass $1/2$ below the continue arm gives them $4/5$).

None of them touches #139 (c)–(e), or F1–F8, F11 and F12.

## (d) Cost

- **(Z-0)/(Z-i).** No new mathematics. A per-state proof that no history ahead is Zeno is needed; on the instance C7 supplies it. A single measure-zero Zeno history is enough to make the weights undefined (V0).
- **(Z-ii).** One existence citation (Ionescu-Tulcea; Kallenberg 2021, 3rd ed., Theorem 8.24, already referenced). Item 8's "outside EPP1's domain" needs scoping: the mass is assigned before the accumulation point. Clause (2) and item 8 then label histories as ended but change no weight.
- **(Z-iii).** Each weight needs the tail mass $z$, an infinite-horizon quantity that may lack a closed form. It is undefined at $z=1$. Weights depend on $R$ beyond depth 1, and the arms in force at one vertex get unequal weights (C35's root: $X$ $1$, $Y$ $0$), so EPP1's equal share $1/|A|$ is replaced, not only re-scoped.
- **(Z-iv).** Under per-vertex weights it is free: per-vertex prefix weights do not depend on the cut (§9), so its limit is the cylinder mass, (Z-ii). Under counts it needs a cut family and a limit-existence proof (§9's limit iff, C15), and it can fail to converge (#229 R3).
- **(Z-v).** One lemma: per-vertex weights, and counts along depth cuts, depend only on the tree. Stating it fixes a value once the weight type and, for counts, $X$'s subtree are fixed ($1/2$ per-vertex; for depth-cut counts, $0$ with $X$ a single history and $1/2$ if $X$ branches in two at every vertex), which is a choice in itself. As under (Z-ii), clause (2), which is stated in accumulated $\tau$, then changes no weight.

- **(Z-vi).** The same existence citation as (Z-ii), since "almost every" needs the gate-ignored product. It is defined only where $z=0$, and there it adds no value of its own: it removes (Z-i)'s V0 cost and keeps (Z-i)'s undefined weights wherever $z>0$.
- **(Z-vii).** Whether an arm carries a non-Zeno history is a property of $R$ to infinite depth, as for (Z-iii). The arm set in force is no longer $A(O^u,a)$ (§8.2 items 6–7). It is undefined where no non-Zeno history passes. It does not in general remove the Zeno mass: if every arm carries some non-Zeno history, nothing is pruned and it equals (Z-ii) with $z>0$ (for example, $2^k$ chain arms and one escape arm at the vertex at $\tau=1-2^{-k}$ below $Y$: $z=0.2097$, (Z-vii) $1/2$, (Z-iii) $0.6327$).
- **(Z-viii).** No lemma. Like (Z-v), stating it is a choice in itself, and it does not fix a value.

## Questions for an outside critic

1. The gate-ignored product exists from the kernels alone (#258 §3). Is (Z-vi), which uses only its null sets, then a reading in its own right or a restatement of (Z-i) restricted to $z=0$?
2. Counting values depend on $X$'s subtree, which C35 leaves open (Z6). Is there any non-arbitrary way to fix that subtree, or should every counting row be stated as a function of it?
3. (Z-v) and (Z-viii) are the two requirement rows. Does either beg the question, and is either compatible with clause (2), which is stated in accumulated $\tau$, other than by clause (2) changing no weight?
4. Are (Z-iii)'s $z$ and (Z-vii)'s pruned arm set computable for any stated $R$ beyond toys and the cases with $z\in\{0,1\}$?
5. C5 without (A) gives a null Zeno set, and C8 under a hypothetical rule gives $z=1$ (#258 §3). Is there any pinned or stated rule with $0<z<1$, where the mass-based readings come apart?

## Pins and scripts

`/workspace/g244/zeno.py` `40b6ce6dd8f1482c26d2ce6bcb39081566a117bc403b8ca2024855a7ca5f8db7` (exact readings, cut counts); `/workspace/g244/c7.py` `342699a7572012d6c7f3e409c96257543e54a9f7064a16c0a722ebbc1d6e0acf` (C7 recheck; imports `g154/kr.py` `0432cc20`). `/workspace/g258/zeno2.py` `ce3d90881cc64acb705af77d3c6db61dc6035d309925ff4463378ddad60a2096` (V2, V3, (Z-vi)–(Z-viii), counts by $X$ subtree, the T3 example); `/workspace/g258/c5chain.py` `f6e912ebf6c3fb691530e4c94ce59110d70f282051cb980f82db4b630c877929` (C5's jump chains without an arrival rule; imports `g154/kr.py`). On the shared machine, outside the repository.
