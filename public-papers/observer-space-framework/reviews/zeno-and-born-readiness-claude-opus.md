# External critique: Zeno-mass scoping note and Born-readiness v0.9 refresh
Reviewer: Claude Opus 5.5 (independent external critic)
Date: 2026-10-10
Verdict (`notes/zeno-mass-scoping.md`, #244 with #245's strings): **HOLD**
Verdict (`reviews/born-rule-readiness.md`, section "v0.9 refresh (2026-10-10)" only, #246 with #247's strings): **HOLD**

**Read at:** `main` `f920ca3`. **Reference:** `versions/v0.9-prose.md` (unchanged since `e493913`). **Targets:** `notes/zeno-mass-scoping.md` (identical at `b327a7b` and `f920ca3`) and the refresh section of `reviews/born-rule-readiness.md`. The old map above the refresh is read only where the refresh makes claims about it.

**Records read:**
- #245 (`zeno-mass-scoping-literature.md`) and #247 (`born-rule-readiness-v09-refresh-literature.md`);
- `born-rule-readiness-scan.md` (#165, with #174's classifier note);
- §4 of `v0.8.1-prose-full-claude-pressure-test.md` (#230's FOR DAVID list F1–F12);
- the App. A rows of `v0.6-prose.md` and `v0.7-outline.md` that the old map points to;
- `law-of-R-scoping.md` K6;
- `git diff b327a7b f920ca3`.

**Rules kept:**
- I pick no Zeno reading and rank none.
- I decide none of #230 F1–F12, (M1)/(M2), T1–T3, Q-D1–Q-D5 or #139 (a)–(e). Where a finding says a reading or gap *touches* a call, it states the effect on each side and takes none.
- There is no Born derivation and no squared-amplitude or $1/N$ weight, no law of $R$, and no claim about Einstein's equations.
- No existing file is edited. This PR adds this file only.

**Labels.**
- **Required:** a false statement, an unsupported claim, a wrong mapping, a missing option or gap, or a tilt toward a pick.
- **Suggested:** materially improves precision, completeness or symmetry.
- **Nit:** cosmetic or pointer-level.

**String conventions.** Each string names its file: **(note)** is `notes/zeno-mass-scoping.md`; **(brr)** is `reviews/born-rule-readiness.md`. A script checked every OLD below against the file at `f920ca3`:
- each OLD occurs exactly once in its file;
- no two OLDs overlap;
- all NEWs apply together without conflict.

Strings that share a line are written to apply together.

**How this was checked.**
1. I read both targets against v0.9 and drafted findings.
2. Two adversarial skeptics tried to refute each finding and each draft critic answer. Most findings were amended, and the strings below carry the amendments.
3. Two independent critics looked for issues outside my list. Their findings were then put through the same skeptic pass.
4. Three recomputations were run independently (§1): exact rationals for the Zeno toys; Schwarzschild numerics in mpmath at 30–80 digits; and a full rebuild of C33's $c=0.01$ orbit graph.

None of this used the pinned workspace scripts. They are not in the repository, and I did not run them.

---

## 0. Summary

**Zeno-mass note: HOLD.** Every number in the note recomputes exactly. The scoping is careful, and the note makes no pick in words. HOLD is for four reasons.
1. **The option set is incomplete.**
   - A null-set gate (clause (2) required almost surely) and arm pruning (excise, then recompute the arms in force) are statable conventions.
   - Each has a value vector no listed row has, separated by V0 and by a new toy, V2.
   - (Z1)
2. **The structure tilts toward (Z-ii), though the wording does not.**
   - The status-quo label attaches v0.9's standing to (Z-i)'s values (Z2).
   - (Z-ii)'s value appears three times in the table: as (Z-ii), as per-vertex (Z-iv), and as per-vertex (Z-v). The reason is that (Z-iv) approaches the accumulation only from below, and (Z-v) is the only requirement row.
   - The mirror requirement, and the cut at $T\ge1$ that §9 already allows, are both missing (Z3).
3. **The (c) mapping is wrong twice.** The readings touch T1 through C5's jump chains, and (Z-iii) touches T3 through §9's per-decision jump weight (Z4).
4. **Two claims need scope.**
   - "Empty Zeno set" holds under (A) only (Z5).
   - The count values hold only for one choice of $X$'s subtree, which C35 leaves open (Z6).

**Born-readiness refresh: HOLD.** All C-row figures quoted in the refresh check. Gaps 0–6 are the right gaps. HOLD is for seven items.
1. The Scope line says nothing above the section is edited, but the same merge edited l.46. Stale item 3 is out of date as a result (B1).
2. Stale item 8 says the renumbered rows "carry the same claims". Three did not: C15, C16 and C36 (B2).
3. Gap 1 says the slice is blind on flat ΛCDM. That holds only for three named scalars; C23 is the counterexample (B3).
4. Gap 3 reads C33 and C16, which are facts about one unadopted rule on one instance, as properties of realisation (a)/(b). It also drops C5's "per history" (B4).
5. The premise-status bullet says the scan "confirms ... only through tree shape". A scan cannot confirm "only" (B5).
6. Old-map lines 56 and 67 keep the wording #229 R1 corrected. They are missing from the stale list (B6).
7. Gap 4's cost cell still gives (Z-iii) and (Z-v) shorter cost lists than the other readings (B7).

The gating order is not strict, which answers the refresh's own critic question 1 (S1).

---

## 1. Recomputed (independent code; all match unless marked)

**Zeno toys** (exact Python `Fraction`s, closed forms checked by truncation).

| Quantity | Note's value | Recomputed |
|---|---|---|
| $z$ on C35 / V0 / V1 | $1/2$ / $0$ / $1$ | $1/2$ / $0$ / $1$ |
| (Z-0), (Z-i) | undefined ×3 | undefined ×3 |
| (Z-ii) | $1/2$ ×3 | $1/2$ ×3 |
| (Z-iii) | $1$ / $1/2$ / $0/0$ | $1$ / $1/2$ / $0/0$ |
| $\tau$-cut counts, C35 | $1/(1+2^k)$; $1/1025$ at $k=10$; limit $0$ | the same, for every non-Zeno $X$ subtree tried |
| depth-cut counts, C35 | $0$ (Z-v row; (d)) | $0$ only if $X$ is a single history. $1/2$ at every depth if $X$ branches in two at every vertex, and $\to1$ if in three (Z6) |
| retiming $1-2^{-k}\mapsto k$ | (Z-i), (Z-iii) $\to1/2$ | every reading $\to1/2$ on every toy. $\tau$-cut counts are *not* retiming-invariant: with $X$ a single history, $\lim_{T\to1^-}$ becomes $1/2$ |
| V0 and V1 under counting (Z-iv) | not given | $1/(k+2)\to0$ on V0; $1/2$ at every cut on V1 |
| null-set gate (new) | — | undefined / $1/2$ / undefined; V2 undefined |
| arm pruning (new) | — | $1$ / $1/2$ / undefined; V2 $1/2$, against (Z-iii)'s $2/3$ |
| C5-type vertex (3 arms, 2 jump arms, no arrival rule) | — | weight of more than $n$ consecutive jumps $=(2/3)^{n+1}$. The infinite chains are uncountably many, with total mass $0$ |

**Schwarzschild** ($M=1$, mpmath at 30–80 digits; no code shared with `kr.py`).
- **C7.** The minimum of $\pi\sqrt{r^3(r-3)/(r-6)}$ is $111.59018528548905654$, at $r=5+\sqrt7$, as the root of $r^2-10r+18=0$.
  - Eccentric half radial periods: $112.47109$ on $[7,8.3]$, $127.72176$ on $[6.5,12]$ and $212.56700$ on $[10,20]$.
  - In the Darwin form, $T(p,e)=T_0(p)+e^2T_2(p)+O(e^4)$ with $T_2(p)=3\pi p^{3/2}(2p^3-32p^2+165p-267)/\big(4(p-6)^{5/2}\sqrt{p-3}\big)>0$ for all $p>6$.
  - A 186,500-point grid and 20,000 random orbits find nothing below $111.5901853$.
  - So C7's "infimum over bound orbits" holds generally, not only on the note's three samples. The infimum is approached as $e\to0$ and never attained.
- **The orbit $[10,20]$.** $E^2=108/115$ and $L^2=400/23$ exactly, so $E=0.969087$ and $L=4.170288$.
- **Rule targets.**

| Turning point, $c$ | Edge | Target | Target orbit | (a) |
|---|---|---|---|---|
| $r=10$, $c=0.1$ | outward | $11.0813068$ | $[11.0813,39.0029]$ | fails |
| $r=10$, $c=0.1$ | inward | $8.9332073$ | $[8.93321,10.10292]$ | passes |
| $r=10$, $c=0.01$ | outward | $10.1075286$ | $[10.1075,21.3322]$ | fails |
| $r=10$, $c=0.01$ | inward | $9.8926157$ | $[9.89262,18.75044]$; radial period $400.528418$ | passes |
| $r=20$, $c=0.1$ | outward | $23.2367562$ | $[17.4250,23.2368]$ | passes |
| $r=20$, $c=0.1$ | inward | $16.7924853$ | a plunge orbit, apastron at the target | fails under any range convention |

- **C31.** Steps 1–12 pass. Step 13 goes $8.8258690\to8.7383287$, on the orbit $[8.6640074,8.7383287]$, and fails.
- **C16 (H6).** Half periods $[200.264209,225.975330]$. $a=9.8926157$, $b=10.1075286$, and the minimum derivative is $1.098432461$.
- **C37.** $705.154978$ and $69{,}303.7060$; the near-horizon windows are $r-2<1.44616\times10^{-3}$ and $r-2<1.44340\times10^{-5}$.
- **C33 census, rebuilt from the rule as stated.**
  - $c=0.01$:
    - **Orbits.** 29,119 orbits, all 116,476 targets bound. 0 of 58,238 turning points have two admissible edges. The graph is a tree, with longest chain 14.
    - **Stuck orbits.** **14,478** stuck, split 5 / 1,726 / 12,747 at depths 12 / 13 / 14.
    - **Apastra.** The maximum apastron is $25.3669$.
    - **Law.** The jump-count law is $26/3^{12}$, $9338/3^{10}$, $447373/3^{12}$, and $E[\text{decisions}]=14712160/3^{12}=27.6835$.
    - **Robustness.** These figures are identical at 30, 50 and 80 digits and under three conventions for non-bound targets (none occurs).
    - **14,477 vs 14,478.** A float64 root classifier with a $10^{-9}$ tolerance gives 14,477. It does so by mislabelling one near-circular target, $17.14796096$ from the $r=16.900001$ apastron, as a plunge. This supports old-map P4's "classifier rounding artefact".
  - $c=0.1$: 3 orbits, one jump almost surely, $E[\text{decisions}]=2$, maximum apastron $23.2368$.
- **Other checks.**
  - **Arithmetic.** $3^{-10}=1.6935\times10^{-5}$. The C33 probabilities sum to 1 ($26+9\cdot9338+447373=3^{12}$).
  - **C2, C5.** C2's ratio is $3.8147$. C5's outward chain runs $10.1075, 10.2169, 10.3283,\dots$, each target a periastron.
  - **C23, C12, P8.** C23's vertex is at $z=0.671099$. C12's arm count shares are $3/4$ and $1/4$. P8 gives $80/27$.
- **Kallenberg 2021, Theorem 8.24, second-hand.** Mathlib4's `Probability/Kernel/IonescuTulcea/Traj.lean` says "We follow the proof of Theorem 8.24 in [Kallenberg]", and its bib entry is the Third Edition, 2021. This matches #245 F4. I did not read the book.

---

## 2. Zeno-mass note: findings

### Required

**Z1. The option set is incomplete: two conventions are missing.**
- **The null-set gate.** It changes clause (2)'s quantifier ("almost every history" under the gate-ignored product), not its range.
  - Its values are undefined / $1/2$ / undefined. No listed row has that vector.
  - It is defined exactly where $z=0$, and there it equals (Z-ii) and (Z-iii). It removes (Z-i)'s own V0 cost ("A single measure-zero Zeno history is enough to make the weights undefined") and keeps (Z-i)'s undefined weights wherever $z>0$.
- **Arm pruning.** Excise, then recompute the arms in force: an arm stays iff some non-Zeno history passes through it, with equal shares over the arms that stay.
  - On C35, V0 and V1 it agrees with (Z-iii). The toy V2 separates them: (Z-iii) gives $2/3$, pruning $1/2$.
  - **Its costs go in with it.** It reads $R$ to infinite depth, and its arm set departs from $A(O^u,a)=B_R$ (§8.2 items 6–7). It also does not in general remove the Zeno mass. In a toy where every arm carries some non-Zeno history, nothing is pruned, $z=0.2097$, pruning gives $1/2$ and (Z-iii) gives $0.6327$.
- **The "After" sentence.** The note's "After, the excised mass is either kept or renormalised away" is v0.9 §8.3's own two-way framing. It should be attributed to v0.9, not read as the full list.

String Z1a (note) — OLD:
```text
| $z<1$ | $1$ / $1/2$ / undefined ($0/0$) |
```
NEW:
```text
| $z<1$ | $1$ / $1/2$ / undefined ($0/0$) |
| (Z-vi) null-set gate | A variant of (Z-i) that changes clause (2)'s quantifier, not its range: clause (2) must hold for almost every history through the state, under the gate-ignored per-vertex product | iff $z=0$ at the state, where it equals (Z-ii) and (Z-iii) | undefined / $1/2$ / undefined |
| (Z-vii) arm pruning | Excise, then recompute the arms in force: an arm stays iff some non-Zeno history passes through it; equal shares over the arms that stay | wherever some arm stays | $1$ / $1/2$ / undefined |
```

String Z1b (note) — OLD:
```text
Values come from `zeno.py` and are exact.
```
NEW:
```text
Values come from `zeno.py` and are exact. V2 has root arms $X$ (a single history) and $Y$; $Y$ has one vertex at $\tau=1/2$ with arms $Y_1$ (a single history) and $Y_2$, below which C35's chain runs at $\tau=1-2^{-k}$, $k\ge2$, so $z=1/4$. On V2, $w(X)$ is undefined under (Z-0), (Z-i) and (Z-vi), $1/2$ under (Z-ii) and (Z-vii), and $(1/2-0)/(1-1/4)=2/3$ under (Z-iii).
```

String Z1c (note) — OLD:
```text
After, the excised mass is either kept or renormalised away.
```
NEW:
```text
After, the excised mass is kept or conditioned away, the two options v0.9 names; other conventions exist (the table adds (Z-vi), which changes the quantifier, and (Z-vii), which changes the arm set).
```

String Z1d (note; it also carries Z3's cost line) — OLD:
```text
## Questions for an outside critic
```
NEW:
```text
- **(Z-vi).** The same existence citation as (Z-ii), since "almost every" needs the gate-ignored product. It is defined only where $z=0$, and there it adds no value of its own: it removes (Z-i)'s V0 cost and keeps (Z-i)'s undefined weights wherever $z>0$.
- **(Z-vii).** Whether an arm carries a non-Zeno history is a property of $R$ to infinite depth, as for (Z-iii). The arm set in force is no longer $A(O^u,a)$ (§8.2 items 6–7). It is undefined where no non-Zeno history passes. It does not in general remove the Zeno mass: if every arm carries some non-Zeno history, nothing is pruned and it equals (Z-ii) with $z>0$ (for example, $2^k$ chain arms and one escape arm at the vertex at $\tau=1-2^{-k}$ below $Y$: $z=0.2097$, (Z-vii) $1/2$, (Z-iii) $0.6327$).
- **(Z-viii).** No lemma. Like (Z-v), stating it is a choice in itself, and it does not fix a value.

## Questions for an outside critic
```

**Z2. "(Z-0) status quo" attaches v0.9's standing to (Z-i)'s values.**
- v0.9 has no status quo on this convention. §8.3 leaves open whether Zeno histories are excised before clause (2) is checked, and C35 lists three values with no default.
- (Z-0) has (Z-i)'s domain, the same three toy values, and the merged cost line "No new mathematics".
- On V0, (Z-ii) and (Z-iii) both give $1/2$. So "undefined" there is (Z-i)'s value, not something v0.9 says.

String Z2 (note) — OLD:
```text
| (Z-0) status quo | No convention; EPP1 applies only where no Zeno history passes through |
```
NEW:
```text
| (Z-0) domain restriction | EPP1 is used only where no Zeno history passes through, where (Z-i)–(Z-iii) agree. v0.9 does not adopt this: it leaves the range of clause (2) open, and C35 lists three values |
```

**Z3. The table's structure gives (Z-ii)'s value three routes and (Z-iii)'s one.**

The two causes are below. The fix names the convention behind each value and adds the mirror requirement. Each route stays a choice.

- **(Z-iv) approaches only from below.**
  - (Z-iv) is $\lim_{T\to1^-}$, which never meets the excision. Its per-vertex form therefore equals (Z-ii) by construction: per-vertex prefix weights do not depend on the cut (§9).
  - A cut past the accumulation is just as statable under §9's own conventions. With dead ends kept, per-vertex weights give $X$ $1/2$, (Z-ii)'s value. Under §9's "counting survivors only and conditioning ... on survival", they give $1$, (Z-iii)'s value on C35.
  - The note says this only for counts.
- **(Z-v) is the only requirement row.**
  - Under per-vertex weights (v0.9's working position) it lands on (Z-ii)'s values.
  - The mirror requirement, "the Zeno set carries mass $0$" (item 8 puts it outside EPP1's domain), is equally statable. It is not listed.
  - Unlike (Z-v), the mirror fixes no single value, since V2 separates (Z-iii) from (Z-vii).
- The l.24 sentence also needs §9's dead-end convention named. It needs Z6's point about $X$ too, which is why Z3a carries that part of Z6.

String Z3a (note; it also carries the l.24 part of Z6) — OLD:
```text
Counting (Z-iv) at $T\ge1$ meets a continuum of ended $Y$-histories (undefined; dropping them gives (Z-iii)'s 1). Its limit $0\ne1/2$, as §9's limit iff predicts for unbalanced siblings.
```
NEW:
```text
Per-vertex weights do not depend on the cut (§9). So at a cut $T\ge1$, past the accumulation, they give $X$ $1/2$ ((Z-ii)) under §9's dead-end convention, and $1$ ((Z-iii)'s value on C35) under §9's alternative of counting survivors only and conditioning on survival. Counting (Z-iv) at $T\ge1$ meets a continuum of ended $Y$-histories: undefined under §9's dead-end convention, while the survivors-only alternative gives (Z-iii)'s 1. Under that convention any Zeno history makes $\tau$-cuts beyond its accumulation point infinite, so $\tau$-cut counts need $T$ below every accumulation point; depth cuts are unaffected. Its limit is $0\ne1/2$. With $X$ a single history the $\tau$-cuts are depth cuts, and §9's limit iff predicts $0$ for these unbalanced siblings; the $\tau$-cut limit $0$ holds for any non-Zeno $X$ with finite stars (König, §9 *Finite cuts*), while §9's iff covers depth cuts only.
```

String Z3b (note) — OLD:
```text
at $\tau=k$, $X$ has weight $1/2$ under both |
```
NEW:
```text
at $\tau=k$, $X$ has weight $1/2$ under both |
| (Z-viii) domain fidelity | A requirement rather than a reading, mirroring (Z-v): the Zeno set carries mass $0$ (item 8 places it outside EPP1's domain) | — | Wherever $z>0$ it excludes (Z-ii), per-vertex (Z-iv) and (Z-v), and on C35 also counting (Z-iv), whose limit gives weight $1$ to $Y$, all of whose histories are Zeno. It is met by (Z-iii) and (Z-vi) where they are defined, vacuously by (Z-0)/(Z-i), and by (Z-vii) only when pruning removes every Zeno history. It fixes no single value: on V2, (Z-iii) gives $2/3$ and (Z-vii) $1/2$ |
```
(Its cost line is in Z1d.)

**Z4. (c) "None of them touches T1, T3, #139 (a)" is wrong twice.**
- **T1, through C5.**
  - The T1 row's "Drop (A)" side cites C5: "with no arrival rule jump chains pile up (C5)".
  - Without an arrival rule, C5's chains (infinitely many branch points at one value of accumulated $\tau$) are Zeno histories by item 8's first sentence ("finite in every bounded interval of accumulated proper time"). They have total mass $0$, since more than $n$ consecutive jumps has weight $(2/3)^{n+1}$ (recomputed).
  - So under (Z-0)/(Z-i), dropping (A) leaves EPP1 no domain on the instance, as v0.9 says. Under (Z-ii), (Z-iii), (Z-vi) and (Z-vii), the chains are a null set and EPP1 keeps a domain.
  - The other costs of dropping (A) are unchanged. That decides nothing on T1.
  - The link to F7 is at most indirect: F7's facts and options are the same under every reading.
- **T3 (and #139 (a) = T3), through (Z-iii) and (Z-vii).**
  - §9 derives (J1)/(J2), and C17's "$R$-independent" $(1+m)^{-n}$, from "each decision jumps with weight $m/(1+m)$ independently of the past".
  - Where $z>0$, conditioning changes that weight, in either direction. With one decision and $m=2$: Zeno mass $1/2$ below each jump arm gives the jumps $1/2$ in total, and Zeno mass $1/2$ below the continue arm gives them $4/5$ (exact). The instance's pins do not move, because $z=0$ there.
- **This string takes the new readings as added.** If Z1 and Z3 are not applied, drop the first paragraph of NEW and the (Z-vi)/(Z-vii) mentions.

String Z4 (note) — OLD:
```text
None of them touches T1, T3, #139 (a), (c)–(e), or F1–F8, F11 and F12.
```
NEW:
```text
The added rows map as follows: (Z-vi) as (Z-i) where $z>0$ and as (Z-ii) where $z=0$; (Z-vii) as (Z-iii) (it reads $R$ ahead and changes the arm set: T2, and T3 below); (Z-viii) constrains both sides, like (Z-v).

The T1–T3 column above omits two links. **T1** (and with it the proper-time part of #139 (a), which v0.9 files under T1), through C5: without an arrival rule, the instance's jump chains, infinitely many branch points at one value of accumulated $\tau$, are Zeno histories by item 8's first sentence, with total mass $0$ (more than $n$ consecutive jumps has weight $(2/3)^{n+1}$). Under (Z-0)/(Z-i), dropping (A) then leaves EPP1 no domain on the instance; under (Z-ii), (Z-iii), (Z-vi) and (Z-vii) the chains are a null set and EPP1 keeps one. The other costs of dropping (A) ((B) is law-like; (C) excludes the instance) are unchanged. **T3** (and #139 (a)), through (Z-iii) and (Z-vii): where $z>0$ they change the per-decision jump weight $m/(1+m)$ from which §9 derives (J1)/(J2) and C17's $R$-independent $(1+m)^{-n}$, in either direction (one decision with $m=2$: Zeno mass $1/2$ below each jump arm gives the jumps $1/2$ in total under (Z-iii); Zeno mass $1/2$ below the continue arm gives them $4/5$).

None of them touches #139 (c)–(e), or F1–F8, F11 and F12.
```

**Z5. (b) drops C7's qualifier "under (A)".**
- C7 reads "No Zeno on the bound Schwarzschild instance under (A)". The note's "under (a) and without it" refers to realisation (a), not to arrival rule (A).
- Without an arrival rule, the model without (a) has a non-empty Zeno set of mass $0$ (C5; see Z4). So "Only C35 changes" also holds only under (A).
- Under the (a)-restriction, chains end within 14 jumps (C33), so no Zeno set arises there even without (A).

String Z5 (note) — OLD:
```text
- **The instance has an empty Zeno set,** so every reading agrees on all instance pins, under (a) and without it.
```
NEW:
```text
- **Under (A), the instance has an empty Zeno set (C7),** so every reading agrees on all instance pins, under (a) and without it. Without an arrival rule, the model without (a) has a non-empty Zeno set of mass $0$ (C5's jump chains; see (c)), so "only C35 changes" holds under (A).
```

**Z6. The count values hold only for one $X$ subtree, which C35 leaves open.**
- C35 says only "$X$ (ordinary thereafter)". Per-vertex values do not depend on $X$'s subtree, but counts do.
- With $X$ a single history, depth-cut counts are $1/(1+2^{n-1})\to0$. If $X$ branches in two at every vertex (at $\tau=1,2,\dots$), they are exactly $1/2$ at every depth: the siblings are balanced, as §9 predicts. Ternary branching gives $\to1$.
- The $\tau$-cut counts at $T<1$ stay $1/(1+2^k)\to0$ for any non-Zeno $X$.
- So the (Z-v) cell's "give (Z-iv)'s $0$", the (d) line's "$0$ for counts", and l.24's appeal to §9's iff all hold only for the single-history $X$. The l.24 part is in Z3a.

String Z6a (note) — OLD:
```text
$w(X)$ is the weight of arm $X$ in C35's toy.
```
NEW:
```text
$w(X)$ is the weight of arm $X$ in C35's toy. C35 leaves $X$'s subtree open ("ordinary thereafter"); per-vertex values do not depend on it, but counts do, and the counts below take $X$ to be a single history with no further branch point.
```

String Z6b (note) — OLD:
```text
counts along depth cuts are also unchanged by such moves and give (Z-iv)'s $0$.
```
NEW:
```text
counts along depth cuts are also unchanged by such moves, but their value is set by $X$'s subtree, not by $\tau$-blindness: $0$ with $X$ a single history, $1/2$ at every depth if $X$ branches in two at every vertex.
```

String Z6c (note; it also carries S1's (Z-v) half) — OLD:
```text
Stating it fixes a value once the weight type is fixed ($1/2$ per-vertex, $0$ for counts), which is a choice in itself.
```
NEW:
```text
Stating it fixes a value once the weight type and, for counts, $X$'s subtree are fixed ($1/2$ per-vertex; for depth-cut counts, $0$ with $X$ a single history and $1/2$ if $X$ branches in two at every vertex), which is a choice in itself. As under (Z-ii), clause (2), which is stated in accumulated $\tau$, then changes no weight.
```

### Suggested

**S1. Cost lines are not yet symmetric.**
- (Z-iii)'s cost does not say that it gives the arms in force at one vertex unequal weights. On C35's root, $X$ gets $1$ and $Y$ gets $0$. That replaces EPP1's $1/|A|$, not only its depth-1 character.
- The mirror cost for (Z-ii) is that clause (2) and item 8 then change no weight. (Z-v)'s half of this is in Z6c.

String S1a (note) — OLD:
```text
Weights depend on $R$ beyond depth 1.
```
NEW:
```text
Weights depend on $R$ beyond depth 1, and the arms in force at one vertex get unequal weights (C35's root: $X$ $1$, $Y$ $0$), so EPP1's equal share $1/|A|$ is replaced, not only re-scoped.
```

String S1b (note) — OLD:
```text
Item 8's "outside EPP1's domain" needs scoping: the mass is assigned before the accumulation point.
```
NEW:
```text
Item 8's "outside EPP1's domain" needs scoping: the mass is assigned before the accumulation point. Clause (2) and item 8 then label histories as ended but change no weight.
```

**S2. "through the cut criterion" is the wrong reason.**
- In this repository, "cut criterion" means C13: per-vertex weights and counts agree on a cut iff $D$ is constant on it.
- Per-vertex (Z-iv) reduces to (Z-ii) because prefix weights are cut-independent (§9: "the per-vertex value does not").

String S2 (note) — OLD:
```text
Under per-vertex weights it is free, because it reduces to (Z-ii) through the cut criterion.
```
NEW:
```text
Under per-vertex weights it is free: per-vertex prefix weights do not depend on the cut (§9), so its limit is the cylinder mass, (Z-ii).
```

**S3. The (Z-iv) cell gives C35 only, although the column header promises C35 / V0 / V1.**
- The V0 and V1 values matter for critic question 2.
- On V0, counting (Z-iv) gives $0$ although $z=0$.
- On V1, it gives $1/2$ where (Z-i) and (Z-iii) are undefined.

String S3 (note) — OLD:
```text
per-vertex $1/2$ at every cut. Counts: $1/(1+2^k)$ for $T\in[1-2^{-k},1-2^{-k-1})$, giving $1/3, 1/5, \dots, 1/1025$ at $k=10$, with limit $0$
```
NEW:
```text
C35: per-vertex $1/2$ at every cut. Counts: $1/(1+2^k)$ for $T\in[1-2^{-k},1-2^{-k-1})$, giving $1/3, 1/5, \dots, 1/1025$ at $k=10$, with limit $0$. V0 ($z=0$): per-vertex $1/2$; counts at the same cuts $1/(k+2)$, with limit $0$. V1: per-vertex $1/2$; counts $1/2$ at every cut
```

**S4. "C12–C15, C36 (finite trees, no accumulation)" is not accurate for C15 and C36.**
- C15's tree is infinite: its shares are pinned at $n=120,121$.
- C36 counts walks on $P_4$ and $K_{2,3}$.
- Neither assigns proper times, so no Zeno set is defined on them. The conclusion "unchanged" stands.

String S4 (note) — OLD:
```text
C12–C15, C36 (finite trees, no accumulation).
```
NEW:
```text
C12–C14 (finite trees or finite cuts, no accumulation); C15 and C36 (an infinite tree and walks on finite graphs, with no proper times assigned, so no Zeno set is defined).
```

### Nit

**N1. $z_X$ is used in the (Z-iii) formula but never defined.**
- Read as the Zeno mass measured from $X$, the formula would give $-1$ for $Y$ on C35. It needs the root-measure mass.
- The note's numbers for $X$ are unaffected.

String N1 (note) — OLD:
```text
Excise, then condition: $w(X)=(w_{\rm ii}(X)-z_X)/(1-z)$
```
NEW:
```text
Excise, then condition: $w(X)=(w_{\rm ii}(X)-z_X)/(1-z)$, with $z_X=w_{\rm ii}(X)\,z(X)$ the root-measure mass of the Zeno histories through $X$ and $z=\sum_X z_X$
```

**N2. "end by excision rather than by geometry" holds only for regular accumulation.**
- Item 8 includes accumulation "at a singular endpoint of one segment" (C8). There a Zeno history ends where the geometry ends too.
- Stated without comment, this narrows a (Z-ii) cost to the regular case.

String N2 (note) — OLD:
```text
positive weight sits on histories that end by excision rather than by geometry
```
NEW:
```text
positive weight sits on histories that item 8 ends (at a regular accumulation, by excision alone; at a singular endpoint, as in C8, the geometry ends there too)
```

---

## 3. Zeno-mass note: answers to its critic questions

1. **Is $z$, defined with the gate ignored, the right object, or does using the product measure already assume (Z-ii)?**
   - $z$ is the mass of the Zeno set under the gate-ignored product measure. That measure exists from the kernels $1/|A|$ alone, whether or not the gate holds (Ionescu-Tulcea), so using it does not assume (Z-ii) *as the weight*.
   - (Z-ii) takes this measure as the weight, (Z-iii) conditions it, and the null-set gate (Z-vi) uses its null sets. (Z-0)/(Z-i), pruning (Z-vii) and the count readings do not use it.
   - Each Zeno history has mass $0$, since it passes infinitely many branch points with at least 2 arms each. So a countable Zeno set gives $z=0$, and mass-based readings can differ only where an uncountable Zeno set passes through the state.
   - On every pinned or stated case, $z\in\{0,1\}$:
     - C7: the Zeno set is empty.
     - C5 without (A): uncountable but null.
     - C8 under the hypothetical rule of question 5: $z=1$.

     Intermediate $z$ occurs only in hand-built toys (C35, V2). So on the record the mass-based readings differ only on such toys: (Z-iii) either equals (Z-ii) or is undefined, and (Z-0)/(Z-i) differ from both only where a Zeno set exists (C5 without (A)).
2. **Is counting (Z-iv) a separate reading or (M2) applied to C35? Does 0 survive other cut families?**
   - It is (M2) at $\tau$-cuts approaching the accumulation from below. The note's own (c) row says so.
   - Its $0$ at $\tau$-cuts holds for any non-Zeno $X$ with finite stars: $X$ has finitely many nodes before $\tau=1$ (König), while $Y$'s grow like $2^k$.
   - Under other families: with $X$ a single history, every family that cuts each $Y$-history ever deeper gives $0$. With $X$ branching, the limit is set by how the $X$- and $Y$-parts of the cuts grow. It is $1/2$ along depth cuts for binary $X$ and $\to1$ for ternary $X$, and it can fail to exist. So $0$ does not survive other families in general (Z6).
   - It also departs from the per-vertex value regardless of $z$: $0$ on V0, where $z=0$, and $1/2$ on V1, where $z=1$ (S3).
3. **Does (Z-v) beg the question?**
   - Structurally: under per-vertex weights, (Z-v) is equivalent to "the Zeno set changes no weight". That is (Z-ii)'s values, so (Z-v) adds no independent support to them.
   - Under counts it selects depth cuts over $\tau$-cuts, which is (M2)'s cut question. $\tau$-cut counts are not retiming-invariant: with $X$ a single history, the $T\to1^-$ limit moves from $0$ to $1/2$.
   - (Z-v) is compatible with clause (2), which is stated in accumulated $\tau$, only if clause (2) changes no weight.
   - Whether this amounts to begging the question is the author's call. The mirror requirement (Z-viii) is offered so that each side has one.
4. **Is (Z-iii)'s $z$ computable for any stated $R$ beyond toys?**
   - In every pinned or stated case, yes, and trivially:
     - $z=0$ on the instance under (A). C7, recomputed: no stable bound orbit has a half radial period below $111.5901853$, so the Zeno set is empty.
     - $z=0$ without an arrival rule (C5's chains, $(2/3)^{n+1}$).
     - $z=1$ on C8's lump for any hypothetical (a)-admissible $R$ with a non-empty star at every $K$-vertex. $K=K(t)$, so every history from a state at $t_0$ meets the infinitely many critical times before $t=1$ within accumulated $\tau<1-t_0$; (a)-targets lie in the future.
   - In general, $z$ is the probability of an explosion-type tail event of the EPP1 chain on $(O^u,a)$, so it is a function of the state. Conditioning on non-explosion is then a Doob $h$-transform with $h=1-z$. This is a standard identification, not checked against a source.
   - A positive lower bound on segment proper time between decisions makes the Zeno set empty. No closed form beyond these is claimed.
5. **Are there pinned rows where a Zeno set appears that the note misses?**
   - **C5: yes.** Without an arrival rule it is an uncountable, null Zeno set at the instance's periastron (Z4, Z5).
   - **C8.** Under the worked rule there are no branch points: §7 defines no target where $\nabla K=0$, which is every $K$-vertex of an FLRW lump. Under a hypothetical (a)-model with non-empty stars at every $K$-vertex (not pinned), $z=1$ at every state. That is a V1-type case:
     - (Z-ii), per-vertex (Z-iv) and (Z-v) give weights;
     - counts give weights where their cuts are finite and the limit exists;
     - (Z-0)/(Z-i), (Z-iii), (Z-vi) and (Z-vii) give none.
   - **C15 and C36** assign no times.
   - **C14's** times are finitely many before its cut.

---

## 4. Born-readiness v0.9 refresh: findings

### Required

**B1. "Nothing above this section is edited" is false at `main`, and stale item 3 is out of date.**
- `git diff b327a7b f920ca3` shows that #246's merge changed l.46 in place. "(§6 is a cartoon; matter open)" became "(v0.6 §6 is an informal picture, not ontology; matter open)". This is #247's F-string A, which #247 called a separate edit.
- At `main`, stale item 3's second sentence is therefore false: no forbidden word remains. The row also now says "v0.6 §6" itself.
- Line numbering is unchanged, so the other pointers still land.

String B1a (brr) — OLD:
```text
the old map above is re-mapped against v0.9, and nothing above this section is edited.
```
NEW:
```text
the old map above is re-mapped against v0.9. One line above this section changed in the same merge: l.46's "(§6 is a cartoon; matter open)" became "(v0.6 §6 is an informal picture, not ontology; matter open)" (#247's F-string A). Nothing else above is edited.
```

String B1b (brr) — OLD:
```text
The row also uses a word on Literature's forbidden list.
```
NEW:
```text
At `b327a7b` the row also used a word on Literature's forbidden list; #246's merge replaced it, and the row now says "v0.6 §6" itself, so only the pointer to v0.9 §4 remains live.
```

**B2. Stale item 8: "The same numbers carry the same claims" is false for three of the six rows.**
- **C15.** v0.6's "cofinal constancy sufficient" became constancy of $D$ at every depth from some depth on. That is #229 R3; cofinal constancy is false as a sufficient condition.
- **C16.** v0.6's "(numerical evidence, not a proof)" is now "(**proof**, model without (a))", with a new checked instance.
- **C36.** v0.7-outline's "matches MERW only in the long-path limit" became "in general only" (#229 R2).
- C9 and C24 are unchanged apart from section numbers. C33's claim text is unchanged; its stuck count is item 5's business.

String B2 (brr) — OLD:
```text
The same numbers carry the same claims: C9, C15, C16, C24, C33, C36.
```
NEW:
```text
The numbers carry over. C9, C24 and C33 keep their claims (C33's stuck count is item 5). Three claims changed: C15 (v0.6's "cofinal constancy sufficient" is now constancy of $D$ at every depth from some depth on, #229 R3), C16 (v0.6's "numerical evidence, not a proof" is now a proof) and C36 (v0.7-outline's "only in the long-path limit" is now "in general only", #229 R2).
```

**B3. Gap 1: "the slice is blind ... on flat ΛCDM (C18)" holds only for three scalars.**
- C18 covers $K$, $g^{ab}R_{ab}$ and $R_{ab}R^{ab}$.
- C23 puts a $(R_{ab}u^au^b)^2$ vertex at $z=0.671$ (recomputed: $0.671099$).
- The scalar is open (§6.1, §11). The NEW uses v0.9's neutral "the choice matters".

String B3 (brr) — OLD:
```text
the slice is blind on Minkowski/dS/ESU (C19) and on flat ΛCDM (C18)
```
NEW:
```text
the slice is blind on Minkowski/dS/ESU for every lock-side scalar (C19), and on flat ΛCDM for $K$, $g^{ab}R_{ab}$ and $R_{ab}R^{ab}$ (C18); there the choice of scalar matters (C23)
```

**B4. Facts about one unadopted rule on one instance are stated as properties of (a)/(b), and C5 loses "per history".**
- C33 is about "The (a)-restriction of the Kretschmann rule". C16 is about "the worked model without (a)", in fact its sub-rule "jump toward 10".
- v0.9 §2 says '"(a) has a model" does not mean "(a) has an ongoing branching model"'. C4 and §8.2 say that (a) "selects no countable star".
- As worded, the Cost cell's unscoped "under (a) branching is transient" is the only realisation-side cost, so it tilts against (a).
- C5 says clause (2) fails *per history*. Whether that removes EPP1's domain depends on the Zeno-mass convention (Zeno-note Z4).
- Gap 4's "Exact (a) law" is the same overreach.

String B4a (brr) — OLD:
```text
Without an arrival rule clause (2) fails (C5).
```
NEW:
```text
Without an arrival rule clause (2) fails per history (C5); whether that leaves EPP1 without a domain depends on the Zeno-mass convention (gap 4).
```

String B4b (brr) — OLD:
```text
Completed histories are countable under (a) (C33: 29,119 orbits, 14,478 stuck) and a continuum without it (C16).
```
NEW:
```text
For the worked rule on the instance, completed histories are countable under its (a)-restriction (C33: 29,119 orbits, 14,478 stuck) and a continuum in the model without (a) (C16); (a) itself selects no countable star (§8.2, C4).
```

String B4c (brr) — OLD:
```text
under (a) branching is transient |
```
NEW:
```text
under the worked rule's (a)-restriction, branching on the instance is transient (C33), which v0.9 keeps apart from (a) in general (§2) |
```

String B4d (brr) — OLD:
```text
Exact (a) law $26/3^{12}$
```
NEW:
```text
Exact law of the worked rule's (a)-restriction on the instance at $c=0.01$: $26/3^{12}$
```

**B5. "It confirms that a germ parameter can enter only through tree shape" claims what a scan cannot show.**
- The old map's PASS clause is sufficiency: a germ parameter "can enter through tree shape alone".
- Exclusivity is the old map's structural point (§1.2: "Every computable weight is a combinatorial function of a tree"). It is not a result.
- The scan's own "only" (§5) is scoped to its instance.

String B5 (brr) — OLD:
```text
It confirms that a germ parameter can enter only through tree shape, as step functions at finite $n$.
```
NEW:
```text
On that instance (unadopted rule, $c=0.1$, one orbit family) a germ parameter enters the weights through tree shape alone ($|A|=3$ at every decision; only the kinds of jump targets change), as step functions at finite $n$ (scan §5). That weights can depend on nothing but the tree is §1.2's structural point, not a scan result.
```

**B6. The stale list misses the wording that #229 R1 corrected.**
- Old-map l.56 reads "under (a) no uniform countably additive measure exists", and l.67 reads "(M2) has no uniform countably additive measure".
- Counting measure is uniform and countably additive. What fails is a countably additive *probability* measure that gives each point the same positive weight (#230 R1; v0.9 §11; Paper 1 §6).
- The NEW's item 12 is a **nit** and can be dropped. It covers l.66 and l.67's "in expectation" wording, which v0.9 replaced with ratios of expectations and pooled shares. The difference is real: under (a) at $c=0.1$ the pooled share is $1/2$ but $E[J/D]=\ln2$.

String B6 (brr) — OLD:
```text
### Critic questions
```
NEW:
```text
11. **l.56, l.67:** "(M2) ... under (a) no uniform countably additive measure exists" and "(M2) has no uniform countably additive measure" keep the wording that #229 R1 corrected. Counting measure is uniform and countably additive; what fails, in v0.9 §11's words after Paper 1 §6, is that "a countably infinite set carries no countably additive probability measure that gives each point the same positive weight". "Under (a)" is also C33's (a)-restriction on the instance.
12. **l.66, l.67:** "the jump share is $2/3$ in expectation" and "the jump share is 1/2 while branching lasts" are v0.7 wording. v0.9 states $2/3$ and $1/2$ as ratios of expectations (Wald's identity), gives 0.6672, 0.5015 and 0.4999 as pooled shares, and says a single history's jump share differs (§9, C33, C34).

### Critic questions
```

**B7. Gap 4's cost cell is still one-sided.**
- It claims to give "the note's (d) cost for each reading". Since #247 string 1 it costs (Z-0)/(Z-i) and (Z-ii) in full.
- It keeps only one of (Z-iii)'s three costs, and drops (Z-v)'s "One lemma" and "a choice in itself".
- (Z-v)'s surviving clause can then read as a benefit. This is the defect #247 F5 marked required, in the readings its string left short.
- The NEW restores the note's wording, with the mitigations on both sides. If the note adopts Z1/Z3, add the costs of (Z-vi)–(Z-viii) here too.

String B7 (brr) — OLD:
```text
(Z-0)/(Z-i) need a per-state no-Zeno proof, and one measure-zero Zeno history leaves weights undefined; (Z-ii) needs an existence citation and a scoped item 8; (Z-iii) reads $R$ ahead; counting (Z-iv) needs a cut family and a proof that the limit exists; (Z-v) fixes a value once the weight type is fixed
```
NEW:
```text
(Z-0)/(Z-i) need a per-state no-Zeno proof (C7 supplies it on the instance), and one measure-zero Zeno history leaves weights undefined; (Z-ii) needs an existence citation (already referenced) and a scoped item 8; (Z-iii) needs the tail mass $z$, an infinite-horizon quantity that may lack a closed form, is undefined at $z=1$, and reads $R$ ahead; counting (Z-iv) needs a cut family and a proof that the limit exists, and can fail to converge; (Z-v) needs one lemma, and stating it fixes a value once the weight type is fixed, which is a choice in itself
```

### Suggested

**S1. The gating order is not strict. This answers critic question 1.**
- Gap 4's §9 proofs need no $R$.
- Gaps 3 and 4 depend on each other, which makes a cycle:
  - The Zeno convention decides whether C5's per-history failure removes EPP1's domain from a model with no arrival rule.
  - C33's countability changes the (M1) and (M2) costs.
- Gap 2's figures are EPP1 quantities (C17, C34).

String S1 (brr) — OLD:
```text
The gaps follow the old gating order (§3 above, gates 0–6).
```
NEW:
```text
The gaps follow the old gating order (§3 above, gates 0–6). The order is not strict. Gap 4's §9 proofs (C13, C15, C36) need no $R$. Gaps 3 and 4 depend on each other: C5's per-history failure leaves a model with no arrival rule without an EPP1 domain under (Z-0)/(Z-i), but not under (Z-ii)/(Z-iii), where C5's chains are a Zeno set of mass $0$; and C33's countability changes the costs of (M1) and (M2). Gap 2's figures are EPP1 quantities (C17, C34).
```

**S2. Gap 5 omits the one v0.9 constraint on laboratories, two couplings, and the link from weights to frequencies.**
- **C38 (§6.1).** Under the example slice, a freely falling laboratory's branch opportunities are its radial turning points.
- **Two couplings.**
  - The "Which Bell premise" call turns on "if co-existing arms count as outcomes", a labelling question.
  - (a) forbids the cross-continuation jumps "a measurement picture would want" (§8.2).

  Both are couplings, not calls that gap 5 waits on, so "No listed call" stands.
- **Weights to frequencies.** §8.4 names "a typicality rule" as part of its later bar. A frequency comparison needs some link from weights to frequencies under either reading of the weight. The NEW does not scope it to one reading.

String S2a (brr) — OLD:
```text
| 5. Measurement model, matter | None. §4 "Measurement, informally (not ontology)": no picture is used, and matter is open |
```
NEW:
```text
| 5. Measurement model, matter | No measurement model. §4 "Measurement, informally (not ontology)": no picture is used, and matter is open. One named constraint bears on any later model: under the example slice, a freely falling near-flat laboratory in a Schwarzschild exterior has its $K$-vertices exactly at its radial turning points, so its branch opportunities are fixed by its own free fall, not by anything an experiment does; a supported laboratory lies outside the model while matter is open (§6.1, C38) |
```

String S2b (brr) — OLD:
```text
No §8 item; §4, §11 (matter) |
```
NEW:
```text
No §8 item; §4, §11 (matter). Coupled to the mapping choice inside §11's "Which Bell premise" call ("if co-existing arms count as outcomes"), and to (a) versus (b): (a) forbids the cross-continuation jumps, "the ones a measurement picture would want" (§8.2) |
```

String S2c (brr) — OLD:
```text
| An outcome labelling ("same outcome") and matter fields, beyond the lock |
```
NEW:
```text
| An outcome labelling ("same outcome") and matter fields, beyond the lock; for any frequency comparison, also a stated link from weights to frequencies (§8.4 lists "a typicality rule", with "a law of $R$" and "work on circularity", for its later bar) |
```

**S3. Gap 1 omits hard-gate clause (1).**
- A law must give finite stars, or countable ones with a named exhaustion.
- This does not depend on the realisation: lock-side candidates give trivial maps or a continuum (§8.5), and even (a) selects no countable star.

String S3 (brr) — OLD:
```text
The §8.4 motivation clause is unmet (Bertrand over (slice, rule) pairs)
```
NEW:
```text
The §8.4 motivation clause is unmet (Bertrand over (slice, rule) pairs). Hard-gate clause (1): a law must give finite stars, or countable ones with a named exhaustion (§8.3; §9 *Exhaustion*; §11); lock-side candidates give trivial maps or a continuum of successors (§8.5), and (a) selects no countable star (§8.2, C4)
```

**S4. F11 is filed under gap 1, but it concerns C33's $m\le1$, which gap 3 uses. F7 is narrower in the table than in #230.**
- #230 F11: "It would make C33's $m\le1$ a theorem. It adds a physics claim about the unadopted example." Both clauses are carried, so the move leans toward neither of F11's options.
- F7 also covers the labelling of (A).

String S4a (brr) — OLD:
```text
T3 / #139 (a); F11 (the #203 lemma bears only on the worked rule)
```
NEW:
```text
T3 / #139 (a)
```

String S4b (brr) — OLD:
```text
T1; F7 ((B) scope); #139 (a) for the proper-time part
```
NEW:
```text
T1; F7 ((B) scope; labelling of (A)); F11 (the #203 lemma would make C33's $m\le1$ a theorem and adds a physics claim about the unadopted example); #139 (a) for the proper-time part
```

**S5. Gap 4's Open and Waits-on cells need three fixes.**
- **"§8.2 item 8's range" names the wrong clause.** The range belongs to clause (2), which §8.3 states. Its open part is already the Zeno-mass convention, so the cell counts one item twice.
- **"(Z-0)–(Z-v)" breaks the table's own rule** ('"Waits on" lists only the named open calls'). They are a note's options; (Z-0), (Z-iv) and (Z-v) are not in v0.9 at all.
- **#230 F6 is missing.** It "touches a cost line of (M2)", which gap 4 incorporates. It is glossed here as attribution only, with both options named.

String S5a (brr) — OLD:
```text
§8.3 Zeno-mass convention; §8.2 item 8's range;
```
NEW:
```text
§8.3 Zeno-mass convention (which includes clause (2)'s range, before or after item 8's excision, and, after it, whether the excised mass is kept or conditioned away; options in `notes/zeno-mass-scoping.md`);
```

String S5b (brr) — OLD:
```text
F5 (MERW-hazard wording); (Z-0)–(Z-v) |
```
NEW:
```text
F5 (MERW-hazard wording); F6 (who is credited for §11's (M2) cut objection, Wallace 2007 or SHPMP 2008) |
```

**S6. "The DW, Zurek, Saunders and Vaidman rows are unchanged" carries forward one error and misses one v0.9 note.**
- **The DW (a) row.** Its "EPP1 and (M2) already weight all arms equally" is wrong for (M2), which weights the evolutions at its cut equally, not the arms. C12's count gives $3/4$ and $1/4$. Arms swapped by an automorphism still get equal counts at a cut it preserves, so the row's "idle" needs rewording, not reversal.
- **The Zurek row.** Its locality half now meets v0.9 §10's statement that the flag is not lock-side, together with open call T1. Its $E_W$ is v0.9's $E_{\mathcal W}$.

String S6 (brr) — OLD:
```text
- **The DW, Zurek, Saunders and Vaidman rows are unchanged.**
```
NEW:
```text
- **The DW, Zurek, Saunders and Vaidman rows are unchanged in status,** with three notes. The DW (a) row's "EPP1 and (M2) already weight all arms equally" is wrong for (M2), which weights the evolutions at its cut equally, not the arms (C12's depth-2 count gives arm $A$ $3/4$ and arm $B$ $1/4$); arms swapped by an automorphism still get equal counts at any cut the automorphism preserves, so "idle" needs rewording, not reversal. The Zurek row's locality half is met as Obs-locality on $(O^u,a)$; v0.9 §10 adds that the flag is not lock-side, that it bears only on whether EPP1 applies, not on the weights it gives, and that how to resolve this is open call T1. The Zurek row's $E_W$ is v0.9's $E_{\mathcal W}$ (#229 N22).
```

### Nit

**N1.** P3's "longest chain 1" at $c=0.1$ is C33's "no post-jump orbit has an (a)-admissible edge". Only P3's orbit count (3) lacks a row.

String N1 (brr) — OLD:
```text
P3, P7 and P8 have no v0.9 row.
```
NEW:
```text
P3's "longest chain 1" at $c=0.1$ is C33's "no post-jump orbit has an (a)-admissible edge: one jump a.s."; P3's orbit count (3), P7 and P8 have no v0.9 row.
```

**N2.** In gap 1's Settled cell, $R\subseteq V^\tau\times V$ appears without the status v0.9 gives it.

String N2 (brr) — OLD:
```text
| 1. Law of $R$, slice, motivation | $R\subseteq V^\tau\times V$;
```
NEW:
```text
| 1. Law of $R$, slice, motivation | $R\subseteq V^\tau\times V$, a declared constraint on sources with named-extra status (§8.2 item 1);
```

**N3.** l.127's "`versions/v0.6-prose.md` §§7–9" is stale too. Items 1, 4 and 6 renumber the same sections elsewhere.

String N3 (brr) — OLD:
```text
the v0.6-prose / v0.7-outline App. A pointers are now v0.9 App. A.
```
NEW:
```text
the v0.6-prose §§7–9 pointers are now v0.9 §§9–11, and the v0.6-prose / v0.7-outline App. A pointers are now v0.9 App. A.
```

**N4.** l.97's "the weight's reading: per-vertex shares or counts" can be read as restating (M1)/(M2). Gap 4 uses the v0.9 sense, which is also the v0.6 sense.

String N4 (brr) — OLD:
```text
now has the options (Z-0)–(Z-v) of `notes/zeno-mass-scoping.md`.
```
NEW:
```text
now has the options (Z-0)–(Z-v) of `notes/zeno-mass-scoping.md`. The same item's "the weight's reading: per-vertex shares or counts" can be read as restating (M1)/(M2); in v0.9 §§9, 11 (as in v0.6 §9) the reading of the weight is co-existence (working Postulate, revisable) versus chance (defined), the sense gap 4 uses.
```

**N5.** "(below)" points to stale item 7.

String N5 (brr) — OLD:
```text
has been run (below).
```
NEW:
```text
has been run (stale item 7).
```

---

## 5. Born-readiness refresh: answers to its critic questions

1. **Is the gating order still strict?**
   - No. Gap 4's R-free §9 proofs (C13, C15, C36) are a parallel track.
   - Gaps 3 and 4 depend on each other: through item 8 and C5 under the Zeno convention, and through C33's countability, which changes the costs of (M1) and (M2). That is a cycle, so the relation is a partial order only if gaps 3 and 4 are merged.
   - Gap 2's figures are EPP1 quantities, a back-edge to gap 4's working postulate.
   - Gap 5's dependence on gap 3 is consistent with the old order. See S1.
2. **Does the (a)-restriction's countability (C33) move any premise to "statable"?**
   - No. The DW (a), Saunders, Zurek-swap and post-branching self-location rows lack amplitude-like structure, a norm, a factorisation or a lock-compatible uncertainty, and countability supplies none of these. DW (b)'s same-vertex half still lacks a labelling. The measure-problem row was already "Yes, fully".
   - Countability sharpens (M1)'s refusal-case cost and leaves (M2)'s "needs a cut or grain" cost in place. v0.9 §11 says both. The question's "only (M1)" framing omits the (M2) half.
   - Where the whole history set, Zeno histories included, is countable, $z=0$, so (Z-ii) and (Z-iii) coincide. (Z-0)/(Z-i) still fail wherever any Zeno history passes. On C33 itself the Zeno set is empty (C7), so all readings agree there.
3. **Are gaps 5 and 6 independent?**
   - Not shown either way. Lock-side invariants can tell arms apart without amplitude-like structure: the old map's retired toy has $K=0$ against $80/27$ (P8, recomputed). But that toy's edge is cross-continuation, which is forbidden under (a), and telling arms apart is not grouping them as "the same outcome".
   - v0.9 uses no measurement picture (§4) and does not address whether a labelling needs amplitude-like structure, or the converse.
   - A Born-type comparison needs both.
4. **Is any C-row used beyond its instance?**
   - Yes:
     - C18 in gap 1 is used beyond its three scalars (B3).
     - C33 and C16 in gap 3's Settled and Cost cells, and in gap 4's "Exact (a) law", are used beyond the worked rule on the instance (B4).
     - C5 loses "per history" in gap 3 (B4a).
   - C7 and C29 are correctly scoped "on the instance".
5. **Does the #174 relabelling put the $n\ge6$ figures under the degenerate-target caveat?**
   - Partly.
   - Apart from the 10.85 target (a 2-ulp flip, from $n\ge7$), the relabelled targets are not under the degenerate targets' "resolution of the arithmetic" caveat. The scan says each of the 77 lies closer to its root than 1% of the smallest root gap.
   - Unlike the five degenerate targets, though, they were not given an exact 60-digit parent-state recomputation. Their labels, and so the $n\ge6$ values at the 31 changed germs, rest on the hardened classifier, which uses 40-digit roots only near root coincidence.
   - The read at $n=4$ does not depend on them. I could not re-run the scan; see §7.

---

## 6. Notes on the record (no string)

- **#247 F2 is wrong in one aside, harmlessly.** It says '"Bertrand" ... does not appear in v0.9'. It does, in §4 ("Bertrand’s problem (on a continuum ...)") and §8.4 ("ends at Bertrand’s problem over admissible (slice, rule) pairs"). The refresh's use is supported.
- **#245 F2's "I integrated the eccentric half-periods independently" is confirmed here.** The match is to 5 or more digits, and the general infimum claim also holds (§1).
- **The C33 census in §1 reproduces every C33 figure at $c=0.01$ from the rule as stated.** It also locates the 14,477/14,478 classifier difference in one near-circular target. This independently supports the old map's P4 note and the refresh's stale item 5.
- **Z4 and S1 rest on reading item 8's first sentence literally.** That sentence is "finite in every bounded interval of accumulated proper time", and read literally it covers infinitely many branch points at one $\tau$ (C5's chains). v0.9 §8.3 also says clause (2) "is supplied by strict alternation plus the no-Zeno clause". If the author intends strict alternation *alone* to cover the single-$\tau$ case, a sentence in §8.2 item 8 saying so would remove the T1 link. That would itself be a convention choice touching T1, and it is left to the author.

---

## 7. Unchecked

- **Pinned workspace scripts were not run.** None is in the repository: `zeno.py`, `c7.py`, `brr_check.py`, `kr.py`, `sim.py`, `agraph.py`, `along.py`, `c33r.py`, `scan.py`, `scan_robust.py`. Their SHA-256 pins are unverified. Every figure in §1 comes from independent code.
- **Sampled figures were not recomputed:** C34 (0.6672, 0.0658, 5.90; 0.6669, 99.94%) and C33's sampled 0.5015, 0.4999, 3,169 / 16,831.
- **The scan.** Its $n\ge6$ values and the hardened-classifier relabelling of 77 targets were not checked (critic question 5).
- **C8's counts** of 7, 64 and 637 critical points were not recomputed. The C8 statements in §3 use only its stated form, $K=K(t)$ with $dK/dt$ oscillating before $t=1$.
- **C13–C15 and C36's values** were not recomputed here, beyond the toy and $P_4$ facts that #245 and #247 cover.
- **Kallenberg 2021, Theorem 8.24** was checked only second-hand, through Mathlib4's source and bib entry. I did not read the book.
- **Records not re-read in full:** #155, #169, #173, #174, #229's N8 and N22, Geometry's v0.7-outline F2/RC2, and Claude's v0.7 row 10. I relied on the targets' and #245's descriptions of them. I checked `law-of-R-scoping.md` K6 (one row).
- **The PR bodies of #244 and #246** were not read. The #246 squash message was seen in `git log`.
- **The old map's literature references** (§1.1, Deutsch through Zurek) were not checked. They are outside the refresh.
- **Whether item 8 is meant to cover accumulation at a single value of $\tau$** is a reading of the text (§6, last bullet). Z4, Z5, B4a and S1 depend on it.

---

## 8. Provenance

- **Reviewer:** Claude Opus 5.5, an Anthropic model, acting as an independent external critic in a Claude Code session. The serving model was confirmed from session metadata.
- **Date:** 2026-10-10.
- **Process:** one author pass, then a multi-agent workflow:
  - two adversarial skeptic passes over every draft finding and critic answer;
  - two independent completeness critics, whose new findings were put through a further skeptic pass;
  - three recomputation agents.

  I merged the results and checked the strings mechanically.
- **Tools:** Python 3.13 with `fractions`, mpmath 1.3, sympy 1.14, numpy and scipy, in a scratch virtual environment outside the repository. The scratch scripts are not part of this PR.
- **Repository changes:** this file only. No existing file was edited.
