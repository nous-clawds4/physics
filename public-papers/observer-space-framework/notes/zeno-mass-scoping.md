# Zeno-mass convention: scoping note (options and costs only)

**Read at:** main `e493913` (`versions/v0.9-prose.md` §8.2 item 8, §8.3, §11, C7, C8, C29, C35). **Record:** #155 toy, v0.7-outline Geometry F2/RC2, Claude v0.7 row 10, #229 N8/N22, `born-rule-readiness.md` §3 item 4, `law-of-R-scoping.md` K6. **Status:** scoping only. No reading is picked, and nothing in `versions/` is edited.

## What the Zeno mass is

- **Which histories.** *Zeno* histories: branch points accumulate at finite accumulated $\tau$ (including at a singular segment endpoint). Item 8: such a history **ends there**, outside EPP1's domain.
- **What mass.** The *Zeno mass* $z$ at a state is the per-vertex product mass of the Zeno histories through it, gate ignored (an Ionescu-Tulcea measure; finite stars). On C35's toy $z=1/2$.
- **Why it is undefined.** Hard-gate clause (2) "ranges over the histories through the state" (§8.3), and v0.9 leaves open whether that is before or after item 8's excision. Before, the gate fails at the root. After, the excised mass is either kept or renormalised away. v0.9 names (Z-i)–(Z-iii) and picks none (§11).

## Readings

$w(X)$ is the weight of arm $X$ in C35's toy. V0 is C35 with one continuing arm of two below $Y$, so the Zeno set is a single history ($z=0$). V1 is C35 with $X$ also carrying the chain, so $z=1$. Values come from `zeno.py` and are exact.

| Reading | (a) Definition | Well-defined when | $w(X)$: C35 / V0 / V1 |
|---|---|---|---|
| (Z-0) status quo | No convention; EPP1 applies only where no Zeno history passes through | wherever no Zeno history passes through the state | undefined / undefined / undefined |
| (Z-i) | Clause (2) is checked over all histories through the state, before excision | as (Z-0); the gate fails at every ancestor of any Zeno history, whatever its mass | undefined / undefined / undefined |
| (Z-ii) | Excise first; the per-vertex product mass is kept, with Zeno histories counted as ended | wherever the per-vertex product is defined (finite stars) | $1/2$ / $1/2$ / $1/2$ |
| (Z-iii) | Excise, then condition: $w(X)=(w_{\rm ii}(X)-z_X)/(1-z)$ | $z<1$ | $1$ / $1/2$ / undefined ($0/0$) |
| (Z-iv) cut limit | $\lim_{T\to1^-}$ of the weight at an accumulated-$\tau$ cut $T$, or along depth cuts. Per-vertex: the cylinder mass. Counts: the share of cut nodes | per-vertex: always, and it equals (Z-ii). Counts: iff the limit exists | per-vertex $1/2$ at every cut. Counts: $1/(1+2^k)$ for $T\in[1-2^{-k},1-2^{-k-1})$, giving $1/3, 1/5, \dots, 1/1025$ at $k=10$, with limit $0$ |
| (Z-v) $\tau$-blindness | A requirement rather than a reading: weights are unchanged when vertex times are moved monotonically, keeping the tree (e.g. $1-2^{-k}\mapsto k$) | — | Under per-vertex weights it forces $1/2$, which is (Z-ii)'s; counts along depth cuts are also unchanged by such moves and give (Z-iv)'s $0$. (Z-i) and (Z-iii) change under such moves: at $\tau=k$, $X$ has weight $1/2$ under both |

Counting (Z-iv) at $T\ge1$ meets a continuum of ended $Y$-histories (undefined; dropping them gives (Z-iii)'s 1). Its limit $0\ne1/2$, as §9's limit iff predicts for unbalanced siblings.

## (b) Pins: where it bites, recomputed

- **Only C35 changes under the readings,** with the values in the table above. C35's cell already pins three of them: undefined, $1/2$ and $1$.
- **The instance has an empty Zeno set,** so every reading agrees on all instance pins, under (a) and without it.
  - Recomputed C7: the minimum half radial period over circular radii is $111.5901853$, at $r_0=7.64575131106459=5+\sqrt7$ (`c7.py`).
  - Eccentric orbits are longer: $[7,8.3]$ gives $112.471$, $[6.5,12]$ gives $127.722$ and $[10,20]$ gives $212.567$.
- **Unchanged under every reading:** C7, C29; C16 ((H6) half periods $[200.26,225.98]$); C33, including #169's exact law ($26/3^{12}$, $9338/3^{10}$, $447373/3^{12}$; 27.68 decisions); C34, C37; C12–C15, C36 (finite trees, no accumulation). C8 is a slice fact with no $R$ or weight pinned, so no reading acts on it.

## (c) Open calls touched

| Reading | (M1)/(M2) | T1–T3 | #139 (a)–(e) | #230 F1–F12 |
|---|---|---|---|---|
| (Z-0)/(Z-i) | (M1) loses weights above any Zeno history | none | (b) | F9 (status wording of the measure) |
| (Z-ii) | (M1) weights stay functions of the current state; positive weight sits on histories that end by excision rather than by geometry | none | (b) (a named convention) | F9 |
| (Z-iii) | (M1) weights read $R$ ahead, so they are no longer depth-1 | T2 (per-step versus a distant quantity) | (b) | F9, F10 (cost lines) |
| (Z-iv), counts | This is (M2)'s cut question; the value depends on the cut family (C14, C15) | T2 | (b) | F10 |
| (Z-v) | Constrains both sides | none | (b) | F9 |

None of them touches T1, T3, #139 (a), (c)–(e), or F1–F8, F11 and F12.

## (d) Cost

- **(Z-0)/(Z-i).** No new mathematics. A per-state proof that no history ahead is Zeno is needed; on the instance C7 supplies it. A single measure-zero Zeno history is enough to make the weights undefined (V0).
- **(Z-ii).** One existence citation (Ionescu-Tulcea; Kallenberg 2021, 3rd ed., Theorem 8.24, already referenced). Item 8's "outside EPP1's domain" needs scoping: the mass is assigned before the accumulation point.
- **(Z-iii).** Each weight needs the tail mass $z$, an infinite-horizon quantity that may lack a closed form. It is undefined at $z=1$. Weights depend on $R$ beyond depth 1.
- **(Z-iv).** Under per-vertex weights it is free, because it reduces to (Z-ii) through the cut criterion. Under counts it needs a cut family and a limit-existence proof (§9's limit iff, C15), and it can fail to converge (#229 R3).
- **(Z-v).** One lemma: per-vertex weights, and counts along depth cuts, depend only on the tree. Stating it fixes a value once the weight type is fixed ($1/2$ per-vertex, $0$ for counts), which is a choice in itself.

## Questions for an outside critic

1. Is $z$, defined with the gate ignored, the right object, or does any use of the product measure beyond a failed gate already assume (Z-ii)?
2. Is (Z-iv) with counts a separate reading, or only (M2) applied to C35? Does its value 0 survive any cut family other than accumulated-$\tau$ and depth cuts?
3. Does (Z-v) beg the question, since it presupposes that weights depend on the tree and not on $\tau$?
4. Is (Z-iii)'s $z$ computable for any stated $R$ beyond toys?
5. Are there pinned rows, C8's FLRW with some $R$ or C15's schedule tree with assigned times, where a Zeno set appears that this note misses?

## Pins and scripts

`/workspace/g244/zeno.py` `40b6ce6dd8f1482c26d2ce6bcb39081566a117bc403b8ca2024855a7ca5f8db7` (exact readings, cut counts); `/workspace/g244/c7.py` `342699a7572012d6c7f3e409c96257543e54a9f7064a16c0a722ebbc1d6e0acf` (C7 recheck; imports `g154/kr.py` `0432cc20`). On the shared machine, outside the repository.
