# Neutrality and record check: topology decision brief (#301)

**Verdict: HOLD (narrow).** The brief is well sourced, and most of it is neutral. It makes no pick, adopts nothing, gives no recommendation and explains its ordering. Seven strings are needed before it goes to David (R1–R7). They are the same kinds of fix as my #268 review of #266:

- a dropped hedge (R3);
- one overclaim about the record (R4);
- (M1) without its ruling tag (R5);
- unflagged omissions (R6);
- asymmetric (T0) and (T3) entries (R1, R2, R7).

Two optional strings follow.

**Heads read (re-checked before filing).**

- #301 head is `2134523`, one commit on main `f7acfac`. Main is unchanged.
- The diff is exactly one added file, `notes/topology-decision-brief.md`: 1,100 words by `str.split`, no table.
- Paper 1, v0.9.1 and `papers/` are untouched.
- This file is a one-file PR from `f7acfac`. I merged nothing and messaged no one.

**#299's final state.** #299 merged at `f7acfac` (head `26147c4`), with #300's R1, R2 and R3 (R3 slightly reworded) and N1–N4 applied. #300 itself is still open. The brief reflects #299's final text: "Theorem 16 is stated for $\mathrm{Obs}$ and is read here on $V$", and (Z-ix) "relayed, not signed". Its pins (`zwp.py` `1777f0be425d`) are unchanged by #299's fix commit. Every number used is a #299 pin:

- $r^*=2.00036101764$;
- $2\times10^{-11}$ after 20,000 jumps;
- $v=0.3849001795$.

## 1. Neutrality

- **Ordering and stance.** The status line says: "Options are listed in the order the Physics Lead gave them; the order implies no ranking." It says "no pick, no lean, no recommendation" and "the call is David's".
  - Nothing presents an option as adopted.
  - There is no Lead or agent recommendation. A scan for recommend, prefer, should, best, natural and obvious finds only "should" inside an open question (§4.3).
- **(T3) "Case for identifying" is an accurate record statement.**
  - v0.9.1 §4: $O^u$ "is the class of triples (presentation, $p$, $u$) … under pointed analytic diffeomorphisms that carry $u$".
  - v0.9.1 §7: "'Which exterior' is not a property of the target, since $V$ consists of germs modulo pointed diffeomorphism."
  - The record basis is therefore real. But the other side gets less. Its case cites no record ("a distinction a completed spacetime draws"), although the record does state that reading: #297 §3, row "Gauge: 'which exterior' kept | It still exists, as a distinct element", and `obs-as-a-space.md`'s "Gauge as a named home … stays open".
  - The shared *Cost* line names a cost only for keeping labels ("needs a $V$ finer than §4's"). It names none for identifying, which merges two states that a completed spacetime separates.
  - Read together, the entry leans toward identifying. **R7** balances it.
- **(T0) is thinner than (T1)/(T2).** It has 99 words, against 258, 157 and 159 for (T1), (T2) and (T3).
  - Its *Case* omits the mirror image of (T1)'s costs: no owed proofs, and nothing adopted that the record left unadopted (**R2**).
  - Its *Cost* says the example ends "even though its radius visibly converges to a regular germ". That presupposes the very limit notion (T0) declines to define. Convergence holds for $r_n$ in the $(r,u^r,v)$ parameters, while convergence of germs is what a topology would decide (**R1**).
- **A hedge is dropped in (T1).** #299 §1 says the $(r,u^r,v)$ chart and the Fermi coefficients "agree there; they differ as $r\to\infty$". The brief keeps "inside $r>2$ it agrees with the $(r,u^r,v)$ parameters" and drops the second half (**R3**). That half is the outward-chain case, where (T1) gives a flat limit and the chart gives none.
- **Pedigrees.** (T0) cites v0.9.1 §8.2 item 8, and (T1)/(T2) cite `obs-as-a-space.md` Theorem 16 and `fermi-distance.md`. Both sides are given.

## 2. (T2) as a metrization of (T1)

- **What `fermi-distance.md` §0 says.** "The inverse-limit topology on $J^\infty$ is metrizable. Compact $O(3)$ acts continuously on the Fermi slice $\mathcal P_F$. A quotient metric $d([x],[y])=\inf_{g\in O(3)}d_{\mathcal P_F}(x,g\cdot y)$ is then a candidate *Fermi-slice distance* on $\mathrm{Obs}$. Any metric generating the same topology … is the same kind of scale. Extra packaging of Theorem 16, not a new lock-side functor."
- **Which variant.** It is built on the inverse-limit variant specifically. The brief is right that the record gives no metric for the inductive-limit variant.
- **The overclaim.** The record calls the quotient metric "a candidate". It does not prove that this metric generates Theorem 16's quotient topology. That is a standard fact if $d_{\mathcal P_F}$ is $O(3)$-invariant, which the paper does not state.
- So the brief's "So it is a metrization of (T1)'s inverse-limit variant and has the same limits" states as settled what the record leaves owed (**R4**). The citation "(#300 N1)" points to an open review PR. The text it supports is now in #299 §1, which has merged.
- **This affects my own wording too.** #300 N1's phrase "it gives the same limits", applied in #299 §1, carries the same unproved step. #299 should be corrected along the lines of R4 in a later pass. I do not give a string for #299 here.

## 3. Formal-jet limits and owed proofs

- **"A limit can be a formal jet that is not a germ at all (Prop. 14 there)".** This is accurate. `obs-as-a-space.md` Proposition 14: "Polynomial (hence analytic) jets are dense in $J^\infty$. The subset of convergent Lorentzian jets is therefore not closed in the inverse-limit topology."
  - Strictly, the formal limit lies in the ambient $J^\infty$. In the subspace topology on $V$, such a sequence has no limit.
  - The brief flags that point as unclear (§4.2). Optional N2 tightens the wording.
- **"Inductive-limit … keeps limits analytic but owes proofs, including the outward chain's flat limit (#299)".** This matches #299's own disclosure: "For the inductive-limit variant I have not proved that the radii of convergence stay bounded below."
- **"Shown for the inverse-limit variant in #299; owed for the inductive-limit one".** This is fair for $r^*$. Inside $r>2$ the coefficients are analytic in $(r,u^r,v)$, so chart convergence gives inverse-limit convergence. #299 did not treat either variant separately at $r^*$, so "owed" is the honest word.

## 4. Record tags, pointers, terms, omissions

- **Tags.**
  - (Z-ix) is tagged "relayed, not signed; `notes/zeno-mass-scoping.md`".
  - (M1) appears only as "(M1), which is ruled". The record form is "ruled by David at L3, 2026-10-10; relayed, not signed" (**R5**).
- **Pointers.** All resolve:
  - §8.2 item 8, §4, §7, C5, C7, C8, C37;
  - the Zeno note's N-b; plan items 2 and 12;
  - #292 (merged) D1/D2: "A Zeno history is one completed history, ended by item 8";
  - #297 (merged); #299 (merged) and its second critic question;
  - Proposition 14 and Theorem 16 of `obs-as-a-space.md`, and Theorem 24 of `fermi-distance.md` ("Rounding it is a grain").
  - The exception is "(#300 N1)" (R4).
  - The brief never states that bare § and C pointers are to v0.9.1 (N1).
- **Terms.** These are defined or glossed at first use: $V$, topology, Fermi coordinates, the two variants, $r^*$ and the example. D1/D2, N-a, N-b and (A) are used through pointers, which is acceptable for a brief that cites by path.
- **Omissions** (**R6**). The options are not exhaustive, and the brief does not say so. Missing:
  - deferring the choice until (Z-ix) is adopted. This leaves "exists" undefined, as (T0) does, without ruling a topology out;
  - any topology or metric not on record, which #299 §1 says "would be new".
  - The $(r,u^r,v)$ chart is a parametrisation of one family, not a topology on $V$ (#299). Saying so heads off a likely question.
- **"Not being decided".** The list is right (Zeno reading, throat convention, gauge, grain, F11, law of $R$, (M1)). "Choosing (T1) or (T2) defines 'exists' … does not adopt (Z-ix)" is accurate.

## 5. Guardrails

- χ, `\chi`, egalit, cartoon, GRW, 4-geon, spin-foam, Everett, Deutsch, Wallace and Born: 0.
- No $|a|^2$ or 1/N; no law of $R$; nothing recorded as signed.
- Paper 1 and v0.9.1 are untouched, and the diff is only this file.

## Exact strings (file `notes/topology-decision-brief.md`; each OLD occurs once at `2134523`)

**R1 (required: (T0) cost presupposes a limit).**
OLD: `The example ends even though its radius visibly converges to a regular germ.`
NEW: `The example ends even though its radius converges ($r_n\to r^*$ in the $(r,u^r,v)$ parameters); whether the germs converge is what a topology would decide.`

**R2 (required: (T0) case, the mirror of (T1)'s costs).**
OLD: `- *Case.* No new structure. Item 8 is a stated clause; every Zeno-mass reading (Z-0)–(Z-viii) is defined without a topology.`
NEW: `- *Case.* No new structure and no owed proofs. Item 8 is a stated clause; every Zeno-mass reading (Z-0)–(Z-viii) is defined without a topology, and v0.9.1 and #292 stand as written.`

**R3 (required: restore #299's hedge).**
OLD: `and inside $r>2$ it agrees with the $(r,u^r,v)$ parameters the numerics use.`
NEW: `and inside $r>2$ it agrees with the $(r,u^r,v)$ parameters the numerics use; the two differ as $r\to\infty$ (#299).`

**R4 (required: the metric is a candidate; cite the merged text).**
OLD: `So it is a metrization of (T1)'s inverse-limit variant and has the same limits (#300 N1).`
NEW: `The record calls it "a candidate" and does not prove that it generates (T1)'s inverse-limit topology (a standard fact if the slice metric is $O(3)$-invariant). If it does, it is a metrization of that variant and has the same limits (#299 §1).`

**R5 (required: (M1) ruling tag).**
OLD: `(M1), which is ruled.`
NEW: `(M1), which David ruled at L3 on 2026-10-10 (relayed, not signed).`

**R6 (required: flag the omissions).**
OLD: `This brief sets out the options the record supports.`
NEW: `This brief sets out the options the record supports. Two further courses are not listed. One is deferring the choice until (Z-ix) is adopted, which leaves "exists" undefined as (T0) does but does not rule a topology out. The other is any topology or metric not on record, which #299 §1 says "would be new". The $(r,u^r,v)$ chart is a parametrisation of one family, not a topology on $V$ (#299).`

**R7 (required: (T3) record basis and costs on both sides).** Two strings.

OLD: `- *Case for keeping the label.* It keeps a distinction a completed spacetime draws (regions I and III) and leaves gauge fully open.`
NEW: `- *Case for keeping the label.* It keeps a distinction a completed spacetime draws (regions I and III) and leaves gauge fully open. The record states this reading as a gauge option (#297 §3, row "Gauge: 'which exterior' kept"), and gauge as a named home is open (`papers/obs-as-a-space.md`).`

OLD: ``- *Cost.* Either way it touches the open gauge question (`papers/obs-as-a-space.md`: gauge as a named home stays open); keeping labels also needs a $V$ finer than §4's.``
NEW: ``- *Cost.* Identifying merges two states that a completed spacetime separates (regions I and III); keeping labels needs a $V$ finer than §4's. Either way it touches the open gauge question (`papers/obs-as-a-space.md`: gauge as a named home stays open).``

**N1 (optional: pointer convention).**
OLD: ``nothing in `versions/` or `papers/` is edited.``
NEW: ``nothing in `versions/` or `papers/` is edited. Bare § and C pointers are to v0.9.1.``

**N2 (optional: where a formal limit lives).**
OLD: `where a limit can be a formal jet that is not a germ at all (Prop. 14 there), so membership in $V$ is checked separately`
NEW: `where the limit in the ambient jet space can be a formal jet that is not a germ (Prop. 14 there: analytic jets are not closed), so membership in $V$ is checked separately`

## Addendum: diff check of #301 `2134523` → `110a4c7`

**Heads read (re-checked before filing):** #301 head `110a4c7` (commits `2134523`, `110a4c7`; open, not merged); main `f7acfac`; this PR (#302) was at `5cd062a` before this commit. **Verdict:** PASS with notes. The brief: PASS, and **yes, it is neutral enough to go to David.** The `zeno-well-posedness.md` §1 edit: accurate, with one recommended disclosure (D1).

**Scope.** `git diff --stat 2134523 110a4c7` touches two files only: `notes/topology-decision-brief.md` (12 lines) and `notes/zeno-well-posedness.md` (1 line, §1). Against main, the PR touches only those two files. Paper 1, `versions/` and `papers/` are untouched.

**Strings.** R1–R7 and N1–N2 each appear exactly as their NEW text in this review, and no OLD survives. "No amendments" holds for the strings themselves. The only text outside the strings is the T0 balance text below, which Geometry declared.

**T0 additions (not strings), checked against the record:**
- "Item 8's 'ends there' stays unconditional": this is v0.9.1 §8.2 item 8's own clause. Accurate.
- "whether germs are identified across exteriors does not arise … no gauge reading is needed" and "(T3)'s question does not arise": these follow because T0 asks for no limit. Accurate.
- "Plan item 2's ILL flag on (Z-ix) stays … takes its partner's value": this matches the brief's own Settles line ("(Z-ix) reduces to its partner (Zeno note N-b)") and plan item 2. Accurate.
- "C37 and plan item 12 are unaffected, as under every option": accurate, and phrased symmetrically.
- The weight claim, "C5's chains have mass 0 (#299), so under (Z-ii), (Z-iii), (Z-vi) and (Z-vii) no weight above it moves", is accurate. #299 has the same claim, scoped to C5 by my #300 R3. Here is why the other two readings are left out. `notes/zeno-mass-scoping.md` (main `f7acfac`), line 72: "| (Z-0)/(Z-i) | (M1) loses weights above any Zeno history |". The same note says one measure-zero Zeno history is enough to leave the weights undefined (V0, #270), and that clause (2) still fails on a continued history. So under (Z-0)/(Z-i) the weights stay undefined whatever topology is chosen, and none "moves". For the other four: (Z-ii) drops measure-zero histories; line 77 reads "| (Z-vi) | As (Z-i) where $z>0$, as (Z-ii) where $z=0$ |", and C5 has $z=0$; and (Z-iii)/(Z-vii) act only where $z>0$ (#274 Z3/Z4 wording). So with $z=0$, all four keep (M1)'s weights. The limit to C5 matters: #270's toys with $z>0$ are where a stipulated limit can move weights, and the brief does not generalise beyond C5.
- On lean: the weight fact holds under every option, not only T0, because #299 says no notion of limit moves a C5 weight. Placed only under T0's *Example*, a reader could take it as a T0 advantage. This is optional (N3).

**Option word counts** (str.split, from each bold label to the next): T0 222, T1 273, T2 184, T3 197, which matches Geometry. Brief 1,375 and Zeno note 1,363 also match. T0 is no longer the thinnest option. T1 is longest because it carries its two variants and the owed proofs. T2 is shortest because it is framed as part of T1. Neither difference is a lean. T0 now has a Case, a Cost (David's reading cannot act, and the ILL flag stays), an Example and Settles, in parallel with the others.

**Neutrality: yes.** The reasons:
- Every option has a record basis, its cost and its hedges. T1's "can be a formal jet … analytic jets are not closed" and T2's "does not prove … owed" are both kept.
- T3 now gives both sides a record basis: #297 §3's gauge row for keeping labels, and v0.9.1 §4/§7 for identifying.
- The omitted courses (defer; a topology not on record) are flagged.
- (M1) is tagged "ruled at L3 on 2026-10-10 (relayed, not signed)", and (Z-ix) carries its relay tag.
- No option is presented as adopted, and there is no Lead or agent recommendation.

**`zeno-well-posedness.md` §1 edit.** It is consistent with `papers/fermi-distance.md`:
- line 17: "The inverse-limit topology on $J^\infty$ is metrizable … A quotient metric";
- line 21: "is then a candidate *Fermi-slice distance*" and "Extra packaging of Theorem 16".

Nothing in that file proves that the quotient metric generates the Theorem 16 topology. The parenthetical fact (a quotient of a metric by a compact group acting by isometries generates the quotient topology) is standard, and it is correctly stated as conditional on the slice metric being $O(3)$-invariant. One nuance: fermi-distance.md line 37 uses "a compatible metric is extra packaging" in a conditional sense, so changing "compatible" to "candidate" is a tightening, not a contradiction. Nothing else in the note changed (a 1-line diff).

Repo norm: notes edited after merge record it in their header. For example, `zeno-mass-scoping.md` line 5 says "**Revised** against main `56ad9b7` …" and "**Revised** again against main `af55f77` …". This note's header still says only "Written at main `af75d21`". Recommended (D1):

- **D1** (`notes/zeno-well-posedness.md`; OLD occurs once at `110a4c7`)
  OLD: `Written at main `af75d21`; v0.9.1 unedited.`
  NEW: `Written at main `af75d21`; §1's metric sentence revised in #301 (the record calls the fermi-distance metric a candidate; that it generates the Fermi-slice topology is owed, not proved); v0.9.1 unedited.`

- **N3** (optional, brief; OLD occurs once at `110a4c7`)
  OLD: `no weight above it moves.`
  NEW: `no weight above it moves, as under every option (#299).`

**PR body.** The T2 bullet now reads "a candidate metric on (T1)'s inverse-limit variant; that it generates that topology is owed, not proved". That matches the file.

**Guardrails.** The added lines contain zero χ/\chi and zero forbidden words. There is no Born, $|a|^2$ or 1/N result; no Everett-vs-DW framing; no law of $R$. Paper 1 and v0.9.1 are untouched, and nothing is recorded as signed.
