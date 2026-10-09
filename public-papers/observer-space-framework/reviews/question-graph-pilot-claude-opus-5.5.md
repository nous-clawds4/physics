# Exploratory critique: question-graph pilot (framework v0.3 to v0.7.1)

Verdict: none (exploratory critique)

Reviewer: Claude Opus 5.5 (external critic)
Date: 2026-10-08

**Target:** `public-papers/observer-space-framework/question-graph/` on `main` at `21e2f09`: merged via #199 as `33c06d2`, with the wording follow-up #206 (`83ff2d6`). That is 30 nodes, `graph.yaml`, `index.md` and `versions/v0.3.yaml` to `v0.7.1.yaml`.
- **Brief:** `reviews/question-graph-pilot-claude-cover.md` (#218), read first, and the queue prompt `ops/claude-queue/008-question-graph-pilot.txt`. Questions 1–4 are answered in order below. Findings outside them are kept apart in the separate part.
- **Sources read:**
  - every node file, `index.md`, `graph.yaml` and the six version files;
  - `versions/v0.3-prose.md`, `v0.4-prose.md` and `v0.5-prose.md` in full; `v0.6-prose.md`, `v0.7-prose.md` and `v0.7.1-prose.md` by section (header and changelogs, §§1–5, 7, 9, 10, and the Appendix A rows the nodes cite); the v0.4 to v0.7 outlines where nodes cite them; `v0.8-prose.md` and `v0.8.1-prose.md` (header, §§2, 4, 7, 9, 10, Appendix B);
  - the reviews the nodes cite: #105, #117 and its cover, #118, #128, #129, #154, #155, #158, #162, #168, #169, the v0.5 outline Geometry panel (#120), the v0.6 outline Ontology review (#133), and the v0.2.1 Claude review and Geometry motion recommendation;
  - Paper 1, `papers/obs-as-a-space.md`, `papers/type-ii-adopted.md`, `papers/piecewise-geodesic-Ck-graph.md` and its Ontology note, `papers/Vstar-extend-vs-not.md`, `mathematical-framework.md`, `docs/scratch/path-of-42.md`, *Statement of the Problem* v0.1 note 1, and *Mathematical Foundations* v0.3 T2;
  - with `gh`: the bodies of #102, #103, #104, #130, #134, #199, #206 and #213, and the infinite-harness `docs/path-of-42.md` at `6f02238`;
  - the in-house checks #200 and #202, the cover's claim check #219, and `reviews/law-of-R-scoping.md` (as edited by #187 and #204) with #182 and #185.

**Stance.** I am independent of Ontology, Geometry and Literature. I keep Postulate, Hope, Open and Firewall apart. I neither pick nor rank (M1)/(M2), propose no law of $R$, and decide none of T1–T3, Q-D1–Q-D5 or #139 (a)–(e). I propose no rating values or hold levels, and I do not decide the two items the cover reserves for David. Where a finding touches one of these, it records what the text says and stops.

**Conventions.** Labels are the cover's: **Substantive** (it changes what a reader would take the record to say), **Clarification**, **Nit**. OLD strings are quoted as folded YAML text: a line break inside a `>-` block reads as a space. Each OLD was checked by script to occur exactly once in its file after whitespace normalisation. NEW strings are proposals for Ontology. None changes a status, rating, hold, parent or selection. Where a finding raises a status, parent or selection question, it gives the options without choosing. "v0.N §k" is the prose file. "#N" is the PR, read through the file it merged where there is one.

**What checks out.**
- **Arithmetic.** I recomputed h at all 30 nodes from the YAML (weakest parent; a question carries its parent's h). Every `# h` comment and every value in the index table matches, and IH §2's hold cap holds at every edge.
- **Statuses.** Every answer's status matches the record at v0.7.1, with one placement question (3.4).
- **Guardrails.** (M1) and (M2) share their a, as do (a) and (b). No accepted node is a law of $R$. T1–T3, Q-D1–Q-D5 and #139 (a)–(e) are named as open. None of the house-excluded terms occurs.
- **Earlier checks.** All of #200's and #202's fixes are present, and #206 matches its PR body.
- **The two items for David** are stated as pending and attributed correctly. One adjacent observation (3.15) decides neither.

---

## Summary

- **Q1, faithfulness.** Most sentences follow their sources. Four do not, in ways a reader would carry away:
  - `a-option-e` and the index place the arm-set change at v0.6. In fact $B_R$ held the continue arm from v0.4; v0.6 changed only the wording "arms are the graph out-star".
  - `q-measure` calls the measure "undecided in every version". That is false for v0.3 and v0.4, and it sits in tension with `versions/v0.4.yaml`.
  - `a-option-f`'s reopen condition is labelled as #118's wording. #118 gives no reopen condition, and its own argument rules out the one stated.
  - `a-anchored-count`'s reopen condition turns the record's necessary condition into a sufficient one.
  
  Among the clarifications, `a-jump-bound`'s reopen condition omits a record fact that bears on it (the (a)-restriction's finite chains, C33), reported here without a judgement. Several datings are off by about one version: the isotropy clause, the existence clause for $R$, $V^\tau$, the decoherence-branch firewall, and the Kretschmann rule.
- **Q2, selections.** The `selects` lists are defensible, but two synopses misdescribe what changed. v0.6 ("the rest changed in open and rejected nodes") and v0.7 ("changes in open nodes only") both changed accepted nodes. As clarifications:
  - v0.4 and v0.5 rest on a composition (plain alternation) that has no node, so they select nothing for `q-composition`; the index should disclose this without filing it as rejected, since that would touch T1;
  - two nodes selected in v0.4–v0.5 carry content those versions lack, while `a-alternation` was deselected for that reason.
- **Q3, structure.**
  - A fork David asked for by name is missing: "which objects can be observers?", with no privileged matter accepted and privileged (conscious) matter rejected. The pilot folds the accepted answer into the root.
  - As clarifications:
    - the join layer's rejected options are understated (Option D);
    - `q-law-of-r`'s second parent, `a-vtau`, is younger than the question and sets h for the whole subtree;
    - `a-kretschmann`'s "open" does not fit the index's own gloss;
    - several merged nodes and smaller missing decisions.
- **Q4, neutrality.**
  - (M1)/(M2) is balanced in substance, with two small asymmetries.
  - (a)/(b) is not quite balanced. `a-real-a` omits the (a)-restriction's (J1)/(J2) record and the point that "not fatal" does not depend on dropping (a). It also files the cost the record itself names for (a) outside its cost list.
  - Three open items read slightly as results: `a-type-ii`'s hard Prop. 13, `q-law-of-r`'s dilemma without "not a no-go theorem", and `a-vtau`'s discreteness.
  - The index's open-node rule should say that two accepted nodes are each one side of an open call (Q-D1; T1).
- **Separate part.** Fourteen items an extension to v0.8, v0.8.1 and the scoping note would need, then three other findings.

---

## Question 1: faithfulness

### Substantive

**1.1. `a-option-e` and `index.md` (Unclear record): the arm-set change is put in the wrong place.** The node says "the v0.4 cover says the arms are the out-star; v0.6 on counts the continue arm too". The index says "out-star only in the v0.4 cover, continue arm included from v0.6". Both halves are wrong.
- The continue arm was in $B_R$ from v0.4 on. v0.4 §4.2 item 4 defines $B_R(O^u):=\{[\gamma_{O^u}]\}\cup\mathrm{succ}_R(O^u)$ (`v0.4-prose.md:88`), and v0.5 has the same formula, with "When a continue segment exists, $|B_R|=1+|\mathrm{succ}_R|$" (`v0.5-prose.md:19, 90`).
- "Arms are the graph out-star" is in v0.4 prose (`v0.4-prose.md:79`) and in v0.5 prose §1 and §4.2 (`v0.5-prose.md:17, 79`), not only in the cover.
- Claude #117 §2.4 flagged the mismatch ("Two numbers disagree", `reviews/v0.4-prose-claude-fable-5.1.md:73`). #128 row 4 asked for "arms are the elements of $B_R$" (`reviews/v0.5-prose-claude-opus-5.5.md:142`). v0.6 dropped the out-star sentence ("Dropped from v0.5 …: 'arms are the graph out-star' (replaced)", `v0.6-outline.md:17`; `v0.6-prose.md:186`).

What changed at v0.6 is the arms wording, not the arm set. Literature #202 marked this node OK.

OLD (`a-option-e.yaml`):
```text
(the v0.4 cover says the arms are the out-star; v0.6 on counts the continue arm too, after #128).
```
NEW:
```text
(v0.4 prose §4.2, v0.5 prose §1 and §4.2 and the v0.4 cover say "arms are the graph out-star", while their B_R = {[γ]} ∪ succ_R already counts the continue arm, a mismatch Claude #117 §2.4 flagged; from v0.6 on, the arms are "the elements of B_R", after #128 row 4).
```
OLD (`index.md`):
```text
The arm set changed across versions: out-star only in the v0.4 cover, continue arm included from v0.6 (`a-option-e`).
```
NEW:
```text
The arms wording changed, not B_R: v0.4 and v0.5 prose (like the v0.4 cover) say "arms are the graph out-star" while their B_R already counts the continue arm; from v0.6 the arms are the elements of B_R, after #128 row 4 (`a-option-e`).
```

**1.2. `q-measure`: "Undecided in every version" is wrong for v0.3 and v0.4.**
- v0.3 runs EPP1 as a "working postulate for narrative" (`v0.3-prose.md:139`), and v0.4 as a "named postulate" (`v0.4-prose.md:147`). Neither version's Open list names a count alternative.
- v0.5 §9 first lists "Path-count alternative to per-vertex EPP1" (`v0.5-prose.md:175`).
- The quoted sentence first appears in v0.6, as the owner's §9 edit (`v0.6-prose.md:62`: "keeps the owner's §9 edit (`badc85e`: 'This paper does not choose between them.')"). v0.8 B.2a logs "EPP1 versus Paper 1's count **moved to open call**".

The node's own first sentence ("Framed as (M1)/(M2) in v0.6") and `versions/v0.4.yaml` ("framed as an undecided call only from v0.6") already say so; the node sits in tension with both. EPP1's adoption as a named postulate continues through v0.7.1 §7 (`v0.7.1-prose.md:317`). What changes is that an alternative is named (v0.5) and the call is then framed as undecided (v0.6). The correction does not touch the open status: the call is undecided now.

OLD (`q-measure.yaml`):
```text
Undecided in every version ("This paper does not choose between them").
```
NEW:
```text
Undecided from v0.6 on ("This paper does not choose between them", added to §9 in v0.6). In v0.3 and v0.4 EPP1 is the version's postulate ("working postulate for narrative"; "named postulate") and no alternative is named; v0.5 §9 first lists a "Path-count alternative to per-vertex EPP1" as open (v0.8 B.2a: "EPP1 versus Paper 1's count moved to open call").
```

**1.3. `a-option-f` reopen_if: it claims record backing it does not have.** It opens "Mapper's wording of #118's QUALIFY". Under `index.md`'s own convention, any reopen condition not marked "Mapper's proposal" paraphrases the record (`index.md:109`). But #118's QUALIFY states no reopen condition:
- it is headed "QUALIFY (narrow — does not save F as branching mechanism)" (`reviews/v0.4-claude-117-geometry.md:34`);
- it keeps truncated-jet language only as housekeeping: automatic on the continue arm, and an optional bare-$u$-jump exclusion stated as "a selection rule on $R$, not finite-$k$ magic" (`:36–40`).

#118's argument also rules out the condition as stated: "Across distinct lumps there is no canonical tangent-space ID", and at $k\ge2$, "Matching $j^kg$ across distinct lumps forces equal curvature (under any identification that makes the comparison defined)" (`:28–30`). The condition also omits the half of Claim A that removed F's rationale: the CWS singleton never rested on the order of matching (`:14`, `:25`).

OLD (`a-option-f.yaml`):
```text
Mapper's wording of #118's QUALIFY (truncated-jet language may stay as continue-arm housekeeping): only if a canonical comparison of jets across distinct lumps were found under which finite-k agreement is neither vacuous (k = 1) nor forbids curvature change (k of 2 or more).
```
NEW:
```text
Mapper's proposal; the record gives no reopen condition. #118's QUALIFY keeps truncated-jet language only as housekeeping (automatic on the continue arm; an exclusion of bare u-jumps, if kept, is a selection rule on R) and "does not save F as branching mechanism". Only if finite-k matching were shown to create a branching edge, or the CWS singleton were shown to depend on the order of matching after all (#117 §2.1; #118 Claim A: it rests on the shared oriented germ and geodesic uniqueness). A comparison of jets across distinct lumps would not do it: #118 finds no canonical identification there, and at k of 2 or more matching forces equal curvature "under any identification that makes the comparison defined".
```

**1.4. `a-anchored-count` reopen_if: a necessary condition is read as sufficient.**
- The record: the two properties "hold together only where the tree's shape allows it ($D$-constancy on the cut, C13, or a finite tree counted to its completed histories)" (`v0.7.1-prose.md:394`).
- The node: "If the relevant R were shown to give only such trees, the v0.7 sentence would hold there."
- The record's own C13 tree breaks that. It is $D$-constant at depth 3 (1/12 each), yet the count re-anchored two steps ahead gives 1/10 and 1/15 (Appendix A, C13).
- The other half of the v0.7 sentence ("The depth-1 anchor is the only cut whose weights are functions of the current state", `v0.7-prose.md:366`) is false on every tree. #169: the re-anchored weight "is determined by $v$ (given $R$) for every $k$, not only for $k=1$" (`reviews/v0.7-prose-claude-pressure-test.md:22`).
- #169 adds that the finite-tree case does not help under the (a)-restriction (`:50`).

The second sentence is the mapper's inference, but it carries no "Mapper's proposal" label.

Smaller, same node:
- The title's "at no cost (v0.7 wording)" is not a v0.7 phrase. The title also omits the exclusivity claim, which the synopsis and rationale treat as half of what was rejected.
- The rationale drops "and needs no named depth" from #169's statement of what is particular to depth 1 (`:32`; P1 at `v0.7.1-prose.md:15`).
- It gives only #169's re-anchored reading. #169 also refutes a cut anchored once, whose implied weights "depend on the remaining depth", so "note 6's cost is not escaped either way" (`:41–44`).

OLD (`a-anchored-count.yaml`):
```text
If the relevant R were shown to give only such trees, the v0.7 sentence would hold there.
```
NEW:
```text
The record gives these as necessary conditions ("only where the tree's shape allows it", v0.7.1 §9), not as cases where an anchored count keeps equal weight: C13's own tree is D-constant at depth 3, yet the count re-anchored two steps ahead gives 1/10 and 1/15; and the claim that depth 1 is the only cut with state-function weights is false on every tree (#169). Mapper's proposal: reopen only if the relevant R were shown to give only trees on which a named anchored count keeps equal weight at the fixed cut.
```
OLD (`a-anchored-count.yaml`):
```text
title: "Anchoring the count removes (M2)'s cut dependence at no cost (v0.7 wording)"
```
NEW:
```text
title: "Only the depth-1 anchor gives state-function weights, and anchoring frees the count of its note-6 cost (v0.7 §9 claims)"
```

### Clarification

**1.5. `a-jump-bound`: a record fact that bears on its own reopen condition is missing.**
- The rationale copies v0.7.1's own (B) bullet, "On the instance, chains of edges are infinite" (`v0.7.1-prose.md:208`), which states no qualifier. The qualifier is elsewhere in the record. The infinite chain (C5) is built from outward edges of the model without (a): "(model without (a); these edges fail (a), C30)" (`:492`; `reviews/v0.5-claude-128-geometry.md:93–100`). #129's rejection also predates the lock-side (a) test, which arrived with Geometry #131 R1 in the v0.6 outline r2.
- The reopen condition's first half reads "an R whose edge chains are finite, so that a bound is not law-like". From v0.7 the record contains a stated, uniform, lock-side rule whose edge chains are finite on the instance: the (a)-restricted Kretschmann model. C33 gives "$m\le1$ at every turning point, no cycle, longest jump chain 14" (`:520`), and "At $c=0.1$ … a history jumps once, almost surely" (`:230`).
- v0.7.1 §9 still lists "(B) and (C) are rejected" (`:384`), and v0.8.1 repeats (B)'s reason word for word. Neither says whether C33 bears on it.

I report the record fact only. Whether it meets the condition is not judged here: the record may intend an adopted $R$, or chains finite beyond the instance. (B) is also the replacement named under T1's "Drop (A)", which stays open.

OLD (`a-jump-bound.yaml`):
```text
on the instance, chains of edges are infinite,
```
NEW:
```text
on the instance as stated (the model without (a), C5), chains of edges are infinite,
```
OLD (`a-jump-bound.yaml`):
```text
or a way to make the bound a property of R that does not restart the leftover inventory.
```
NEW:
```text
or a way to make the bound a property of R that does not restart the leftover inventory. Record note: from v0.7 the (a)-restricted model, a stated and uniform rule, has finite edge chains on the instance (no cycle, longest jump chain 14; C33); v0.7.1 §9 keeps (B) rejected and does not say whether C33 bears on it. Not judged here.
```

**1.6. `a-type-ii`: Prop. 13 is given in its strong form only.** "Not derivable from locked data (Prop. 13, papers/type-ii-adopted.md)" repeats the form that Claude #105 §3.4 found "stronger than the author's theorem" (`reviews/v0.3-prose-claude-fable-5.1.md:82`). From v0.4 on, the paper carries a softened Prop. 13: "It is wrong to claim that locked data can never determine any off-curvelet edge" (`v0.4-prose.md:100`). v0.7.1 has both forms:
- §4.2, strong: "Locked data determine no type-(ii) edge (Prop. 13)" (`:189`);
- §4.3, "**Soft Prop. 13.**": "Locked data *can* determine off-curvelet stars … But **kinematics does not single out a dynamics**" (`:238`).

v0.8 B.2b logs Prop. 13 as "**restated**; one clause **dropped**". `q-law-of-r` follows the §4.3 form and `a-type-ii` the §4.2 form. Each node follows its passage faithfully; the graph passes on the paper's own unreconciled pair, which is a note on the paper (B.2 below). The soft form alone is in v0.4 (`:100`) and v0.5 (`:105`). The strong-plus-soft pair runs from v0.6 (`v0.6-prose.md:191, 233`) through v0.8.1.

OLD (`a-type-ii.yaml`):
```text
Not derivable from locked data (Prop. 13, papers/type-ii-adopted.md).
```
NEW:
```text
Not derivable from locked data (v0.7.1 §4.2, citing Prop. 13 of papers/type-ii-adopted.md). From v0.4 the paper also carries a soft Prop. 13 (v0.7.1 §4.3): locked data "can determine off-curvelet stars", but "kinematics does not single out a dynamics", so which readout is a new physical choice; v0.8 B.2b logs Prop. 13 as "restated; one clause dropped".
```

**1.7. `a-type-ii`: four datings and attributions.**
- (a) **"Every later header says so"** (the HOLE relocated, not cleared). This is false for v0.4, whose Status reads "relocation completed here by writing Option F composition" (`v0.4-prose.md:5`), a claim Claude #117 disputed. "Still relocated as a problem" appears from v0.5 on (`v0.5-prose.md:5`), and the three-part address from v0.6.
- (b) **The existence clause has a history.** v0.3 §4.2 adopts it: "**Adopted (working, abandonable).** Existence of type-(ii) edges" (`v0.3-prose.md:93`). v0.4 and v0.5 call type (ii) "the working branching pad" with no existence clause (`v0.4-prose.md:17, 75`; `v0.5-prose.md:17`). #128 found "the pad as written admits $R=\emptyset$, which is CWS" and asked for "$R\ne\emptyset$" to be filed "as a working Postulate or as Open" (`reviews/v0.5-prose-claude-opus-5.5.md:252`). v0.6 makes it "an existential working Postulate" (`v0.6-prose.md:24, 190`). So v0.4 and v0.5 select a node whose title clause "with R nonempty" they lack (see 2.4).
- (c) **No adopter is named.** `papers/type-ii-adopted.md:5`, a note with David's byline, records "David adopted type-(ii) links as the working across-worlds motion" (commit `9c22d9f`, 2026-08-30, a week before v0.3), with no PR or sign-off cited. The index tracks David's adoption of Option F, so it should track this one the same way, stated as the note states it.
- (d) **The type-(i)/(ii) split changed.** v0.3 Definition 7 sorts edges by underlying lumps (`v0.3-prose.md:89`). Under that, #105 §3.3 found that bare orientation changes are type (ii) only for germs whose invariants vary. v0.4 §3 "replaces the v0.3 wording that sorted edges by bare lumps alone" (`v0.4-prose.md:55`), which makes them type (ii) in every case. v0.6 makes them "ordinary type-(ii) candidates with no separate selection rule" (`v0.7.1-prose.md:148`).

OLD (`a-type-ii.yaml`):
```text
and every later header says so.
```
NEW:
```text
and the headers from v0.5 on say so (v0.4's Status had said "relocation completed here by writing Option F composition", which Claude #117 disputed). The existence clause has its own history: v0.3 §4.2 adopts "Existence of type-(ii) edges"; v0.4 and v0.5 state none, and #128 found "the pad as written admits R=∅"; v0.6 makes R ≠ ∅ an existential working Postulate. In-house, papers/type-ii-adopted.md records "David adopted type-(ii) links as the working across-worlds motion" before v0.3 (no signature cited). v0.3 sorts edges by bare lumps; v0.4's oriented split makes bare orientation changes type (ii), and from v0.6 they are "ordinary type-(ii) candidates".
```

**1.8. `a-type-ii`: the cost of abandonment drops the record's condition.** The node says "abandoning type (ii) makes Paper 1's 'the evolution is not unique' false". v0.7.1 §10 says it is false "under the CWS singleton, with the convention of §5.2 that ending and continuing count as one evolution" (`v0.7.1-prose.md:456`). That convention rests on "dying is not an arm", which has no node (3.12).

OLD (`a-type-ii.yaml`):
```text
abandoning type (ii) makes Paper 1's "the evolution is not unique" false.
```
NEW:
```text
abandoning type (ii) makes Paper 1's "the evolution is not unique" false under the CWS singleton, with the §5.2 convention that a history that ends and one that continues count as one evolution (v0.7.1 §10).
```

**1.9. `a-jet-direction` and `index.md` (isotropy): "kept in every version" merges two B.2a rows.** v0.8 B.2a logs "Object: analytic jet plus future time direction | **kept**", but "Oriented observer $O^u$; null observers excluded | **restated**" (`v0.8-prose.md:497–498`). Two parts of the synopsis date from v0.6:
- v0.3 to v0.5 add the direction only "when branching is discussed" (`v0.3-prose.md:15`; `v0.4-prose.md:15`; `v0.5-prose.md:15`), and v0.3 and v0.4 say "Bare $O$ is used when orientation is not yet chosen" (`:37`).
- v0.3 and v0.4 state the isotropy only as a qualifier ("up to the isotropy of the germ"). Claude #105 noted that this "qualifies 'prefers' rather than defining the class" (`reviews/v0.3-prose-claude-fable-5.1.md:129`). The v0.4 and v0.5 outlines name "$u$ modulo germ isotropy". v0.5 prose drops the sentence. v0.6 first defines $O^u$ as the quotient class, and calls the quotient "not optional" (`v0.6-prose.md:128`; C9).

v0.5 also never defines $V$ (#128, `:144`). "$V$ is Paper 1's observer space" is a "reading, stated as such", from v0.6 (`v0.6-prose.md:130`; `v0.7.1-prose.md:128`).

Two small items. The T1-row quote "cannot [be taken] without the lock being changed" alters the source ("which this paper cannot take without the lock being changed", `:407`). And #183 (v0.8 B.2a/B.2b) is quoted but not listed among the sources.

OLD (`a-jet-direction.yaml`):
```text
The isotropy quotient was lost silently in v0.5 prose and restored in v0.6, after Claude Opus 5.5's HOLD on v0.5 (#128) and Geometry's ACCEPT of that item (#129).
```
NEW:
```text
v0.8 B.2a logs the object as "kept" and the oriented observer O^u as "restated". Two parts of the synopsis date from v0.6: v0.3 to v0.5 add the direction only "when branching is discussed", and v0.3 and v0.4 state the isotropy only as a qualifier ("up to the isotropy of the germ"), which Claude #105 noted does not define the class; the v0.4 and v0.5 outlines name the quotient, v0.5 prose drops the sentence silently, and v0.6 first defines O^u as the quotient class ("not optional"), after #128 and Geometry's ACCEPT (#129). "V is Paper 1's observer space" is v0.7.1's "reading, stated as such" (§2).
```
OLD (`a-jet-direction.yaml`):
```text
"cannot [be taken] without the lock being changed"
```
NEW:
```text
is one "which this paper cannot take without the lock being changed"
```
OLD (`index.md`):
```text
The isotropy quotient was lost silently in v0.5 prose and restored in v0.6 (`a-jet-direction`).
```
NEW:
```text
The isotropy clause: v0.3 and v0.4 prose give it only as a qualifier ("up to the isotropy of the germ"; Claude #105: it qualifies "prefers" rather than defining the class), the v0.4 and v0.5 outlines name "u modulo germ isotropy", v0.5 prose drops it silently (#128), and v0.6 first defines O^u as the quotient class (`a-jet-direction`).
```

**1.10. `a-everett-worlds` and `index.md` (Everett line): the firewall's first appearance can be traced, and it is earlier.**
- The object-level firewall enters the framework paper's v0.1.1 outline (as a "Literature firewall thickener", `v0.1.1-outline.md:7, 141`). It is carried through v0.2 and v0.2.1 prose into v0.3 §10, inside the mapped range: objects are "analytic jets / oriented observers as named — not decoherence branches …" (`v0.2.1-prose.md:186`; `v0.3-prose.md:196`). v0.3 is its last carrier.
- v0.4 keeps an arm-level form in §7 ("decision weights on decoherence branches; arms here are Option F out-stars", `v0.4-prose.md:147`) and a Deutsch–Wallace row ("not a decision-theoretic derivation on decoherence branches", `:189`). v0.5 keeps only the row (`v0.5-prose.md:188`).
- The AFLB 2008 clause enters with the v0.6 outline, from Literature #132 finding 2 (`v0.6-outline.md:25`). The words "world-counting slot" first appear in v0.6 prose (`v0.6-prose.md:309`).

So the index's "a first-appearance commit was not traced" can now be filled in. #202's "first appearance … absent from v0.5" holds only for the world-counting wording.

OLD (`index.md`):
```text
The Everett world-counting firewall is found in the paper from v0.6. Its earlier source is Paper 1, and a first-appearance commit was not traced (`a-everett-worlds`).
```
NEW:
```text
The Everett world-counting firewall (AFLB 2008 outcome counting) enters the paper with the v0.6 outline (#130), from Literature #132 finding 2. A narrower firewall, that the objects are "not decoherence branches", is already in v0.3 §10 (carried from the v0.1.1 outline through v0.2.1); v0.4 keeps an arm-level line in §7 and a Deutsch–Wallace row, and v0.5 the row only. The source of both is Paper 1 (`a-everett-worlds`).
```

**1.11. `a-gielen-wise`: the record treats Gielen–Wise as a homonym, not as a weighed option, and dates the disambiguation earlier than v0.3.**
- Paper 1 calls theirs "a different use of the same English words" and its distinction "courtesy, not … a complaint" (`papers/observer-space-ontology.md:57, 179`).
- The framework carries "phrase collision only" from its v0.1.1 outline (`v0.1.1-outline.md:34`) through v0.2/v0.2.1 §2 (the sentence v0.3 repeats) to v0.7.1 §10 ("Phrase collision only").
- The only considered-and-killed move is in-house. Its note's opening brief had already said "Do not identify $\mathrm{Obs}$ with Gielen–Wise", and its Status keeps "Gauge as a named home (Gielen–Wise, …)" open (`papers/obs-as-a-space.md:5, 9, 69, 81`).
- Paper 1 §9 still gives the "given metric" reason, which #158 flagged as true of the induced case only and left to David (`reviews/v0.7-outline-literature.md:110`). Paper 1 is not among the sources.
- Nit: the node gives "phrase collision only" as "v0.7.1 §2, §10". The phrase is only in §10 (`v0.7.1-prose.md:471`).

"Rejected" is still a usable status for a kept-apart reading. The rationale should say that it is a disambiguation.

OLD (`a-gielen-wise.yaml`):
```text
Rejected as the meaning of this programme's observer space, from v0.3 on (§2).
```
NEW:
```text
Rejected as the meaning of this programme's observer space. The record treats it as a homonym rather than a weighed option: Paper 1 calls it "a different use of the same English words", and the framework paper carries "phrase collision only" from its v0.1.1 outline through v0.2.1 into v0.3 §2 and on; the only considered-and-killed move is in-house (below).
```

**1.12. `a-cws-branching`: four points.**
- (a) **The title** names CWS by the class v0.3 gave it while rejecting it. While live, CWS was "a working type-(ii) motion law on observer space" (`v0.2.1-prose.md:17`), and the living notes called it "a type-(ii) framework" (`mathematical-framework.md:29`). Claude's v0.2.1 HOLD and Geometry's motion recommendation recast it as type (i) (`reviews/v0.2.1-motion-recommendation-geometry.md:28`), and v0.3 calls it "a coherent type-(i) package" (`v0.3-prose.md:79`).
- (b) **The first disjunct of the reopen condition** ("a path-germ equivalence other than (E1)/(E2)") cannot do the work alone. Sketch step 3 shows all allowed paths agree on an initial interval (`v0.7.1-prose.md:176`), so they are one germ under any equivalence on path germs. The record lists escapes that fail: Geometry's v0.2.1 motion recommendation, citing Claude's v0.2.1 HOLD §1.3 (`:26, 30`).
- (c) Nit: the banner's words are CWS "is no longer favoured" (`mathematical-framework.md:1`). "Not favoured" is the PR title.
- (d) **#105's verdict** is quoted as "cleared as an error" without the rest of the same line: "v0.2.1 HOLE: cleared as an error, relocated honestly to the law of $R$, not fatal" (`reviews/v0.3-prose-claude-fable-5.1.md:182`; PR title "HOLE relocated, not cleared"). See 4.5.

OLD (`a-cws-branching.yaml`):
```text
Rejected as the branching law in v0.3 ("CWS demoted", #98).
```
NEW:
```text
Proposed in v0.2.1 as "a working type-(ii) motion law on observer space"; recast as type (i) by Claude's v0.2.1 HOLD and Geometry's motion recommendation, and rejected as the branching law in v0.3 ("CWS demoted", #98), which keeps it as "a coherent type-(i) package" (v0.3 §4.1): switching worlds leaves the path in Obs unchanged.
```
OLD (`a-cws-branching.yaml`):
```text
Mapper's proposal, from the proposition's hypotheses: a path-germ equivalence other than (E1)/(E2) that a referee accepts, or a flaw in the CWS-singleton sketch, under which type-(i) motion gives two or more arms.
```
NEW:
```text
Mapper's proposal, from the proposition's sketch: a flaw in sketch steps 1–2, or an escape not among those the record lists as failing (Geometry's v0.2.1 motion recommendation, citing Claude's v0.2.1 HOLD §1.3), under which CWS gives two or more arms. A different equivalence on path germs cannot do it alone: by step 3 all allowed paths agree on an initial interval.
```

**1.13. `a-option-f` rationale: who proposed F, and the half of Claim A that is missing.**
- (a) "Ontology's proposal (#103)" omits that Option F was defined in Geometry's join menu (#102) as the "Hybrid default candidate (for Ontology to accept or reject)", with "Geometry's non-binding lean: **F**" (`papers/piecewise-geodesic-Ck-graph.md:77, 136`).
- (b) The "why" gives the inert/prohibitive half of Claim A. It quotes #134's "finite k is not the HOLE escape", but not #117/#118's reason for it: "CWS HOLE misattributed to matching order" (`reviews/v0.4-claude-117-geometry.md:14`). The singleton rests on the shared oriented germ, geodesic uniqueness and equivalence at the start. That reason removed F's founding rationale; F's table had listed "Escape CWS HOLE" (`papers/piecewise-geodesic-Ck-graph-ontology.md:61–63`).
- (c) "Cannot create a branching edge" is #128 row 1's later wording, repeated in #134's banner (`reviews/v0.5-prose-claude-opus-5.5.md:100`). It is not #117's or #118's.
- Nit: "the demotion found here was recommended" reads as a leftover of the #202 fix ("found here" adds nothing).

OLD (`a-option-f.yaml`):
```text
Ontology's proposal (#103), adopted by David
```
NEW:
```text
Defined in Geometry's join menu as the "Hybrid default candidate", with Geometry's non-binding lean (#102); recommended by Ontology (#103); adopted by David
```
OLD (`a-option-f.yaml`):
```text
and cannot create a branching edge; F is demoted to E.
```
NEW:
```text
so it does no work for branching edges ("cannot create a branching edge" is #128 row 1's later wording); and the CWS singleton never depended on the order of matching (#117 §2.1, Claim A), so dropping infinite-order matching was not the escape. F is demoted to E.
```

**1.14. `a-option-e`: the "cleared as a definition" quote.** It is #117's verdict on v0.4's composition under Option F, which #118 told the paper to keep ("Composition $B_R$: Keep (cleared #105 as definition)", `reviews/v0.4-claude-117-geometry.md:110`). It is not something the Option E residue achieved. The node quotes only the first clause of the v0.5 header line, which goes on "still relocated as a problem (law of $R$, costs)" (`v0.5-prose.md:5`).

OLD (`a-option-e.yaml`):
```text
v0.5's header: the relocated HOLE is "cleared as a definition (B_R given R)".
```
NEW:
```text
v0.5's header, carrying #117's verdict on v0.4's composition (kept by #118): the relocated HOLE is "cleared as a definition (B_R given R); still relocated as a problem (law of R, costs)".
```

**1.15. `a-vstar`: the reopen condition, and the date of supersession.**
- (a) **The reopen condition** says it follows "the record's own escape clause (v0.7.1 §5.1)", but changes it in three ways:
  - it adds "motivated", which §5.1 does not say ("an explicitly chosen discrete sub-ensemble, which is a grain on $E_W$", `v0.7.1-prose.md:250`);
  - it adds a second route, an ensemble restriction that makes ending times discrete, which #118's Claim B table classes as the same kind of grain (`reviews/v0.4-claude-117-geometry.md:69`);
  - it omits the record's second objection, which the node's own rationale gives: ensemble timing "is E-smuggling. It is not used" (`v0.7.1-prose.md:134`).
- (b) **The date.** "Superseded by V^τ (#134 banner, after Claude #128)" dates the supersession to the 2026-09-27 banner. The v0.5 outline (#119, changelog (2)) had already dropped ensemble-timed $V^*$ as the public engine, and the v0.5 outline panel confirmed it ("Ensemble-timed $V^*$ demoted | **Holds**", `reviews/v0.5-outline-geometry.md:26`). #119 is not among the sources.

OLD (`a-vstar.yaml`):
```text
From the record's own escape clause (v0.7.1 §5.1): an explicitly chosen, motivated discrete sub-ensemble of E_W (a grain on E_W), or an ensemble restriction that makes ending times discrete, which inextendibility alone does not do (C25).
```
NEW:
```text
From the record's own escape clause (v0.7.1 §5.1): an explicitly chosen discrete sub-ensemble of E_W, which the record calls a grain on E_W (an ensemble restriction that made ending times discrete is the same kind of grain, #118 Claim B; inextendibility alone does not do it, C25). Mapper's addition: the timing-vote objection would also need an answer, since v0.7.1 §2 calls choosing vertex times by which members die E-smuggling and says "It is not used".
```
OLD (`a-vstar.yaml`):
```text
Superseded by V^τ (#134 banner, after Claude #128);
```
NEW:
```text
Replaced by V^τ as the public vertex engine in the v0.5 outline (#119, changelog (2)), confirmed by its Geometry panel (#120); banner on the in-house note in #134, after Claude #128 row 3;
```

**1.16. `a-vtau`: where it came from.** "Introduced in v0.5" omits three earlier steps:
- Claude #105 §3.1 proposed the engine: level sets or critical points of a curvature scalar, discrete by one-variable analyticity, with "the choice of scalar and level" as the extra (`reviews/v0.3-prose-claude-fable-5.1.md:72`).
- The v0.4 outline (`v0.4-outline.md:105`) and v0.4 §5.3 name it as a lock-side candidate for hard-gate clause (2) (`v0.4-prose.md:127`), with $V^*$ in §5.1. #117 calls the two "competing" (`reviews/v0.4-prose-claude-fable-5.1.md:73`).
- #118 preferred it to naming a sub-ensemble (`reviews/v0.4-claude-117-geometry.md:70`).

The v0.5 outline (#119) then made it the public engine, and v0.5 prose named it $V^\tau$ (`v0.5-prose.md:7`). Nit: "empty on … every locally symmetric lump" came from Geometry #131 on the v0.6 outline (`v0.6-outline.md:23`), not from #128 row 2 or #129 item 5. Those listed named backgrounds, and #129 item 5's QUALIFY was about radial infall (`reviews/v0.5-claude-128-geometry.md:21`).

OLD (`a-vtau.yaml`):
```text
Introduced in v0.5 (#119, #123), then costed
```
NEW:
```text
Proposed by Claude #105 §3.1 and named in v0.4 §5.3 as a lock-side candidate for the hard gate's clause (2), while V* (§5.1) was the offered rule; made the public τ-slice in the v0.5 outline (#119, after #118; written V^τ in #123), then costed
```

**1.17. `q-vertex-times` and `q-join-law`: order of events.**
- (a) **The vertex question** was first posed in-house as the "law of $V^*$" (#102 §5 item 2, `papers/piecewise-geodesic-Ck-graph.md:137`; #103 §2.1). Both merged before #105, which ties $V^*$ to its §3.1 (`reviews/v0.3-prose-claude-fable-5.1.md:49`).
- (b) **`q-join-law`'s "Claude #105 had said"** puts #105 before #102. #105 was written after #102–#104 and read Option F as its own composition reading (C), "written out" (`reviews/v0.3-prose-claude-fable-5.1.md:6, 48`).
- (c) Nit: the synopsis reduces #102's six-option menu (A Obs-path, B $u$ only, C metric jets, D spacetime chart, E graph-native, F hybrid) to a two-way choice. See 3.2.

OLD (`q-vertex-times.yaml`):
```text
was added in v0.4 after Claude #105 §3.1.
```
NEW:
```text
was added in v0.4 after Claude #105 §3.1. The vertex question itself was first posed in-house as the "law of V*" (#102 §5 item 2; #103 §2.1), which #105 tied to §3.1's missing τ-slice.
```
OLD (`q-join-law.yaml`):
```text
Claude #105 had said v0.3
```
NEW:
```text
Claude #105, written after #102 to #104 and reading Option F as its composition reading (C) written out, said v0.3
```

**1.18. `a-alternation`, and the v0.4/v0.5 synopses: "made strict in v0.6".** These read as if the record found v0.4's composition non-strict: the node's "made strict", `versions/v0.4.yaml`'s and the index's "with neither strictness nor the arrival flag", and `v0.5.yaml`'s "plain alternation". The wording follows #200 ("no strictness clause", `reviews/question-graph-pilot-geometry.md:69`). The record did not find that:
- Claude #117 §2.4 read v0.4's "alternates" as strict alternation that "forbids two consecutive jumps", and asked to "allow consecutive jumps or say why not" (`reviews/v0.4-prose-claude-fable-5.1.md:73`).
- #128 says "alternates" "suggests" strictness, and that the draft never answered #117 (`reviews/v0.5-prose-claude-opus-5.5.md:108, 111`).

What v0.4 and v0.5 lack is a written positive-length clause, a ruling on consecutive jumps, and the arrival flag. Leaving `a-alternation` unselected there is still justified by the flag alone. Nit: "Claude #105's reading C" collides with the graph's own letters, where (C) is target avoidance. #105's (A)–(C) are different objects (`reviews/v0.3-prose-claude-fable-5.1.md:58`).

OLD (`a-alternation.yaml`):
```text
made strict in v0.6 (#130) after #128 row 2.
```
NEW:
```text
made explicitly strict in v0.6 (#130) after #128 row 2 (Claude #117 had read v0.4's "alternates" as already forbidding consecutive jumps and asked to "allow consecutive jumps or say why not"; v0.6 writes the positive-length clause and adds the flag). Claude #105's reading letters are not #128's.
```

**1.19. `q-composition`: the wrong reason for #128's finding.** The node says clause (2) held per segment "because every Kretschmann target is itself a vertex". #128 says it says nothing about histories "because jumps carry no proper time" (`reviews/v0.5-prose-claude-opus-5.5.md:106`). The vertex status of the targets is #128's evidence that the gap is live on the worked rule (`:108`). The node follows #129's compressed restatement (`reviews/v0.5-claude-128-geometry.md:18`).

OLD (`q-composition.yaml`):
```text
because every Kretschmann target is itself a vertex,
```
NEW:
```text
since jumps carry no proper time (live on the worked rule, where every Kretschmann target is itself a vertex),
```

**1.20. `a-kretschmann`: three points.**
- (a) **"First used by Claude in #117; carried into the public paper from v0.6 via #128 and #129 (orbit [10, 20])".** #117 already applied the rule to the [10, 20] orbit, with $|B_R|=3$ (`reviews/v0.4-prose-claude-fable-5.1.md:85`). The rule first appears in a public version file in the v0.5 outline (#119), as an arbitrary rule showing that "stated" alone is not enough (`v0.5-outline.md:116`). It was dropped from v0.5 prose (#128, `:205`) and restored in v0.6 ("Restored from v0.5 outline", `v0.6-outline.md:18`).
- (b) **The colon in "As stated it models the schema without (a): typical histories are jump-dominated …"** presents jump dominance as what "without (a)" means. In the record, "without (a)" means one of its edges fails (a) at each turning point, so it is a (b) model (`v0.7.1-prose.md:294, 296`). Jump dominance is a separate fact (`:342`).
- (c) **"It adopts no R"** closes the paragraph on the (a)-restriction (`:234`). The Firewall's "neither is an adopted $R$" (`:86`) covers both models.

OLD (`a-kretschmann.yaml`):
```text
First used by Claude in #117; carried into the public paper from v0.6 via #128 and #129 (orbit [10, 20]).
```
NEW:
```text
First used by Claude in #117, on the orbit [10, 20] with |B_R| = 3; named in the v0.5 outline (#119) as an arbitrary rule showing that "stated" alone is not enough, dropped from v0.5 prose (#128), and restored in v0.6 (#130) as the consistency witness after #128 and #129.
```
OLD (`a-kretschmann.yaml`):
```text
As stated it models the schema without (a): typical histories are jump-dominated
```
NEW:
```text
As stated it models the schema without (a), since at each turning point of the instance one of its edges fails (a) (v0.7.1 §5.4). Separately, under the rule as stated typical histories are jump-dominated
```

**1.21. `a-target-avoid`: one of #129's two costs is missing.** #129 says (C) "excludes the only worked instance … and it adds a clause on $R$'s target set". It conditions its verdict: "not recommended while the Kretschmann rule is the draft's consistency witness" (`reviews/v0.5-claude-128-geometry.md:130`). The v0.6 outline records it as "Rejected alternatives [Geometry over #128]" (`v0.6-outline.md:142`), and it and v0.7.1 carry only the first cost. That matters for the reopen condition: a worked instance with off-slice targets would remove only one of the two.

OLD (`a-target-avoid.yaml`):
```text
Rejected because it excludes the only worked instance,
```
NEW:
```text
#129 also names a second cost, not carried into the v0.6 outline or v0.7.1: it "adds a clause on R's target set". Rejected because it excludes the only worked instance,
```

**1.22. `q-law-of-r`: four points.**
- (a) **"The singleton-or-continuum dilemma lives here (soft Prop. 13)"** drops the record's "In the target direction" and its guard: "It is escaped only by leaving $R$ unspecified or by adding selection extras. That is a motivation problem, not a no-go theorem" (`v0.7.1-prose.md:240`; see 4.5). The dilemma has its own paragraph, after Soft Prop. 13.
- (b) **The synopsis** calls the law of $R$ "the relocated HOLE's final address". The header's address has three parts: "the law of $R$, its motivation, and the choice of $\tau$-slice" (`:9`). The rationale has it right.
- (c) Nit: the quote "No law of R is written" is attached to "every version". Those words start in v0.5; v0.3 has "No law of $R$." and v0.4 "No law of $R$ or $E^*$ is written."
- (d) Nit: #204 (2026-09-30, after the pilot merged) also edited the scoping note.

OLD (`q-law-of-r.yaml`):
```text
The singleton-or-continuum dilemma lives here (soft Prop. 13): kinematics does not single out a dynamics, so a countable star is a new physical choice.
```
NEW:
```text
In the target direction the singleton-or-continuum dilemma lives here (v0.7.1 §4.3, after soft Prop. 13: kinematics does not single out a dynamics, so a countable star is a new physical choice). It "is escaped only by leaving R unspecified or by adding selection extras. That is a motivation problem, not a no-go theorem."
```
OLD (`q-law-of-r.yaml`):
```text
This is the relocated HOLE's final address.
```
NEW:
```text
With its motivation and the choice of τ-slice, it is the relocated HOLE's final address (v0.7.1 header).
```

**1.23. `q-measure`: framing attribution and a stitched quote.**
- "Framed as (M1)/(M2) in v0.6 after Claude #128 row 5 and Geometry #129 claim 4 (Paper 1 measure honesty)" glosses both citations as measure honesty. The honesty point (the uniqueness thesis lapsing silently) is #128's, in row 5, §4.1 and change 4. #129 claim 4 is its "Measure" section, whose named-cut criterion ("'Rules agree only on generation-regular trees' is false at a fixed cut", `reviews/v0.5-claude-128-geometry.md:20`) is where (M2)'s "at a named cut" comes from.
- The labels (M1)/(M2) were introduced in v0.6 outline r2 to rename what Literature #132 called "option (C)" (`v0.6-outline.md:27`).
- The quoted "(b) = T2 and (M1)/(M2)" does not occur in v0.7.1, and header item 2 does not map (b). The header gives "Q-D3 = T2" (`:73`); the §9 row (b) cells read "= T2 and (M1)/(M2)." (`v0.7.1-prose.md:413`). The index repeats the stitched form.

OLD (`q-measure.yaml`):
```text
Framed as (M1)/(M2) in v0.6 after Claude #128 row 5 and Geometry #129 claim 4 (Paper 1 measure honesty);
```
NEW:
```text
Made a live open alternative in v0.6 after Claude #128 row 5 and §4.1 (Paper 1 measure honesty), with Geometry #129 claim 4's named-cut criterion; labelled (M1)/(M2) in the v0.6 outline r2, renaming what Literature #132 called "option (C)";
```
OLD (`q-measure.yaml`):
```text
(v0.7.1 header item 2 and §9 table: "(b) = T2 and (M1)/(M2)").
```
NEW:
```text
(v0.7.1 header item 2 for Q-D3 = T2; §9 table, row (b): "= T2 and (M1)/(M2).").
```

**1.24. `a-m1`: three points.**
- (a) **The pedigree** sits inside "from v0.3 on", but it changed. v0.3 gives none ("chosen for story", `v0.3-prose.md:139`). v0.4 says "the author's 2005 pedigree" (`v0.4-prose.md:147`), and v0.5 "(2005 pedigree)" (`v0.5-prose.md:150`). MMWI's applied per-split rule came in the v0.6 outline after Literature #132 finding 1 (`v0.6-outline.md:24`). SHPMP 2008 Definition 3 came in v0.6 prose r2, after Literature #136 R1 (`v0.6-prose.md:64`).
- (b) **"Did not adopt its framing of (M1) as 'overstated'"** can be read as #154 calling (M1) overstated, which would be a lean against (M1). In fact #154 R7 called one (M1) cost line overstated (`reviews/v0.6-prose-claude-opus-5.5.md:221`). #155 said that framing "leans toward (M1)" and replaced it with "R-dependent" (`reviews/v0.6-claude-154-geometry.md:193`; `v0.7-outline.md:93, 111`). Read the first way, the node reverses the direction of the lean that was neutralised.
- (c) Nit: "runs with EPP1 … from v0.3 on …, but records the choice as undecided" runs two timelines together. The choice is undecided only from v0.6 (1.2).

OLD (`a-m1.yaml`):
```text
(M1) as "overstated" (v0.7 outline, a lean neutralised).
```
NEW:
```text
(M1)'s §9 cost line as "overstated", which #155 said leans toward (M1) and replaced by "R-dependent" (v0.7 outline, a lean neutralised).
```
OLD (`a-m1.yaml`):
```text
(pedigree: the per-split rule applied in MMWI 2006 and stated as SHPMP 2008 Definition 3)
```
NEW:
```text
(pedigree as stated from v0.6, after Literature #132 finding 1 and #136 R1: the per-split rule applied in MMWI 2006 and stated as SHPMP 2008 Definition 3; v0.4 and v0.5 said "2005 pedigree")
```

**1.25. `q-realisation`: the source of the lock-side form.** "Made lock-side in v0.6 after Claude #128 row 7 (Geometry #129 claim 1 ACCEPT …)" is incomplete. #129 left the arrival convention open (`reviews/v0.5-claude-128-geometry.md:70`). The v0.6 outline r1 (#130) adopted "arrival tangent $=u'$". Geometry #131 R1 then drew the consequence: (a) is lock-side, with the test $O'^{u'}\in F(O)\setminus\gamma_{O^u}$; the outward Kretschmann edges fail; and (b) is re-glossed "no realisation required" (`reviews/v0.6-outline-geometry.md:20`; `v0.6-outline.md:21`, r2). No node cites #131.

OLD (`q-realisation.yaml`):
```text
saying (a) forbids curvature-changing jumps was false).
```
NEW:
```text
saying (a) forbids curvature-changing jumps was false); given the outline's arrival-tangent convention, Geometry #131 R1 showed (a) is lock-side (target in F(O), off the source's curvelet) and re-glossed (b) as "no realisation required" (v0.6 outline r2).
```

**1.26. `a-root`: "states the same object".** The v0.7.1 §1 sentence the node quotes continues: "the infinite jet of a real-analytic Lorentzian metric at a point, together with a future time direction" (`v0.7.1-prose.md:102`). That is `a-jet-direction`'s answer, which the root leaves open, as *Statement of the Problem* note 1 does ("*Does not commit to* what that thing is", `public-essays/statement-of-the-problem/versions/v0.1.md:29`). The larger `a-root` point is structural (3.1).

OLD (`a-root.yaml`):
```text
The framework paper states the same object:
```
NEW:
```text
The framework paper opens with the same phrase, then names a particular object (the analytic jet with a time direction, a-jet-direction's answer), which the root leaves open:
```

### Nits (Question 1)

| # | Node | Finding | OLD → NEW |
|---|---|---|---|
| 1.27 | `a-world-analytic` | Both v0.3 clauses are already absent from v0.4 §2, so they were dropped in v0.4, not "later" (`v0.4-prose.md:41, 43`). Both quoted phrases are v0.8 B.2b's excerpts. v0.3 reads "Topology (for example $\pi_1$) may vary across the ensemble" and "The intersection of distinct *world* ensembles is empty" (`v0.3-prose.md:47, 59`). | "were later dropped," → "were dropped in v0.4 (absent from its §2; the phrases are v0.8 B.2b's excerpts of v0.3 §2)," |
| 1.28 | `a-real-a` | "12 to 14 at c = 0.01 … (C33, v0.7 on)" gives v0.7.1's P6–P8 figure to v0.7, which said "13 or 14" (`v0.7-prose.md:202`; `v0.7.1-prose.md:20`). | "(C33, v0.7 on)" → "(C33, v0.7 on; "12 to 14" is v0.7.1's exact law, P6–P8, where v0.7 had "13 or 14")" |
| 1.29 | `a-real-a` | "declined as not borne out by the census (#169)" follows v0.7.1's changelog (`:38`) but drops #169's "The narrowing is real". #169 declined the clause because its threshold ("until ε exceeds the orbit's width") is unpinned (`reviews/v0.7-prose-claude-pressure-test.md:200`). | "not borne out by the census (#169)." → "unpinned: the narrowing is real, but the census does not show that branching stops once the jump length exceeds the orbit's width (#169)." |
| 1.30 | `a-real-b` | (J1) and (J2) are conditions on a rule. The record says "The Kretschmann rule as stated fails both (C17)", and cites jump dominance as "(C17, C34)" (`v0.7.1-prose.md:348, 420`). | "jump-dominated and fail both (J1) and (J2) (C17)." → "jump-dominated (C17, C34), and the rule as stated fails both (J1) and (J2) (C17)." |
| 1.31 | `a-m2` | It drops "implied" from v0.7.1's "its implied next-step weights", and turns "It would carry the uniqueness thesis" into "it carries". | "its next-step weights depend" → "its implied next-step weights depend"; "For: it carries" → "For: it would carry" |
| 1.32 | `q-observer-object` | Every version states the object first in §1 (v0.3's abstract; "What this paper is" from v0.4) and defines it in §2. | "answers it first, in §2." → "answers it first: stated in §1, defined in §2." |
| 1.33 | `a-option-e` | "Abandonable" is v0.7.1 §1 and the §10 table; §4.2 says "working branching pad" (`v0.7.1-prose.md:106, 182, 447`). The term "Option E residue" is #117's, which is not cited. | "through v0.7.1 (§4.2)." → "through v0.7.1 (§1, §4.2)." |
| 1.34 | `a-hand-listed` | "The losing side of … #105" suggests that someone argued for a hand-listed digraph as the controlled example. No one did: it was the loophole #105 named in v0.3's exit gate. The in-house toy (#107) showed one only "in form". | "The losing side of Claude Fable 5.1's HOLD on v0.3 (#105):" → "The loophole in v0.3's exit gate that Claude Fable 5.1's HOLD on v0.3 (#105) named:" |
| 1.35 | `a-vstar` | The synopsis gives half of the rule: v0.4 and #106 need the hitchhiking ensemble to split, with some members extending and some ending (`v0.4-prose.md:112`). | "where members of the world ensemble stop being extendible," → "where the hitchhiking ensemble splits: some members extend analytically through that time and some end there (v0.4 §5.1)," |

---

## Question 2: selections

I agree with #200's corrected lists: v0.3 four nodes; v0.4 adds F and $V^*$; v0.5 replaces them with E and $V^\tau$; v0.6 to v0.7.1 add (A). The findings below are about what the synopses say, and about two convention gaps.

### Substantive

**2.1. `versions/v0.6.yaml` (and the index's v0.6 bullet): "The rest changed in open and rejected nodes" is false.** v0.6 also revised three accepted nodes it selects:
- `a-jet-direction`: "$u$ modulo germ isotropy restored", and "when branching is discussed" deleted (`v0.6-prose.md:20, 104, 128`; `v0.6-outline.md:10`);
- `a-type-ii`: $R\ne\emptyset$ filed as an existential working Postulate, as #128 asked, with three clauses from Geometry #131 R2 (`v0.6-prose.md:24, 190`; `v0.6-outline.md:22`);
- `a-vtau`: v0.5's engine giving a "discrete set" becomes "A candidate lock-side slice", costed as codimension one and blind on locally symmetric lumps, with no time tags (`v0.6-prose.md:243–257`; `v0.6-outline.md:17, 23`).

It also reworded `a-option-e`'s arms ("the elements of $B_R$"), which is a wording fix (1.1). #200 fix S5 rephrased Ontology's original "What changed sits in open and rejected nodes" and kept the claim. I disagree with both.

OLD (`versions/v0.6.yaml`):
```text
The rest changed in open and rejected nodes:
```
NEW:
```text
Accepted nodes also changed: u is again taken modulo germ isotropy and the direction is always part of the object (a-jet-direction); R ≠ ∅ is filed as an existential working Postulate with three clauses (a-type-ii, after #128 and Geometry #131); V^τ becomes a "candidate" slice, costed (a-vtau); the arms wording becomes "the elements of B_R" (a-option-e). In open and rejected nodes:
```
(Mirror it in `index.md`'s v0.6 bullet.)

**2.2. `versions/v0.7.yaml` (and the index's v0.7 bullet): "Changes in open nodes only" does not match v0.7's changelog.**
- (A) is relabelled from "Arrival semantics: (A) is adopted" (`v0.6-prose.md:368`) to "working Postulate, revisable" (`v0.7-prose.md:356`). $R\ne\emptyset$, already a working Postulate in v0.6, gains "revisable" (`:361`).
- v0.7 is also where the sentences of `a-anchored-count`, now a rejected node, first appear (`v0.7-prose.md:366`).
- $R\ne\emptyset$'s existence clause is reworded to "does not by itself give EPP1 a domain" (`v0.7-prose.md:162`, against `v0.6-prose.md:192`).
- The arrival flag is disclosed as history data outside §2's lock-side definition, and T1 lists "Drop (A)". This bears on `a-alternation`.
- A freely-falling-laboratory cost is added to $V^\tau$ (C38).
- A rejected node, `a-gielen-wise`, is corrected per Literature #158; that node records the correction itself.
- T1–T3 and Q-D1–Q-D5 are not nodes, so "open nodes only" does not cover them. v0.7's calls table also carries #139 (a)–(e) (`v0.7-prose.md:374, 385–388`).

OLD (`versions/v0.7.yaml`):
```text
Changes in open nodes only:
```
NEW:
```text
Accepted nodes also changed: (A) is relabelled a working Postulate, revisable (v0.6 had "(A) is adopted"), and R ≠ ∅ gains "revisable" and "does not by itself give EPP1 a domain" (a-type-ii); the arrival flag is disclosed as history data outside §2's lock-side definition, and open call T1 lists "Drop (A)" (a-alternation); V^τ gains a freely-falling-laboratory cost (C38). The rejected a-gielen-wise is corrected after Literature #158, and the sentences later rejected as a-anchored-count first appear. In open nodes and open calls:
```
(Mirror it in `index.md`'s v0.7 bullet, and add "#139 (a)–(e)" after "Q-D1-Q-D5".)

### Clarification

**2.3. `index.md` (Method), with `versions/v0.4.yaml` and `v0.5.yaml`: v0.4 and v0.5 select nothing for a question they answer.** Both versions rest on a composition, "A **history** alternates type-(i) curvelet segments and type-(ii) jumps" (`v0.4-prose.md:84`; `v0.5-prose.md:86`). That is plain alternation, with no arrival rule. No node represents it, so neither version selects an answer to `q-composition`. The yaml synopses and `a-alternation`'s rationale say so. But the Method line (`index.md:12`) restates IH §4's "one accepted answer for each question it depends on", and the exception at `index.md:70` covers open calls only, not this case. It differs from the Option F / $V^*$ convention too, since those two were explicitly demoted and this composition was replaced without being called rejected.

The disclosure should not file the plain composition under "Rejected options by layer". The record rejects only (B) and (C) ("Two alternatives to strict alternation are rejected", `v0.7.1-prose.md:207–210`). Having no arrival rule appears as a cost on the open T1 call's "Drop (A)" side ("with no arrival rule jump chains pile up (C5)", `:407`). Giving it a rejected status would treat part of T1 as decided.

OLD (`index.md`):
```text
parallel branches are allowed (IH §4).
```
NEW:
```text
parallel branches are allowed (IH §4). Departure (disclosed): a question with no accepted answer at a version gets no selection — `q-realisation` and `q-law-of-r` throughout, `q-measure` (an open call from v0.6; EPP1 unselected in v0.3–v0.5 for the reason the version files give), and `q-composition` in v0.4 and v0.5, whose plain alternation has no node; that composition is not filed as rejected, since its replacement bears on open call T1.
```

**2.4. The selection convention is applied unevenly.** `a-alternation` was taken out of v0.4 and v0.5 because its defining clauses arrived in v0.6. Two other selected nodes also carry content those versions lack:
- `a-jet-direction`: the isotropy sentence is missing in v0.5 (v0.4 had it, as a qualifier), and $V$ is defined in neither (1.9);
- `a-type-ii`: "with R nonempty". v0.3 prose had an existence clause, and so did the v0.5 outline ("existence of type-(ii) edges", `v0.5-outline.md:68`); v0.4 and v0.5 prose did not (1.7b).

(`a-option-e`, selected only in v0.5, matches v0.5's $B_R$; only a leftover sentence there says "out-star", see 1.1.) Selecting each node's core decision is defensible. The isotropy loss and the arm wording are disclosed in the index, the second inaccurately (1.1); the existence clause is not. A one-line note in v0.4.yaml and v0.5.yaml would make the convention visible.

**2.5. EPP1 and `a-m1` across all six files.**
- #200's narrative says its fixes disclose that leaving `a-m1` unselected departs from the Option F / $V^*$ convention ("status is current and the selection historical"; "fixes S2, S4, S7 and S8 say so", `reviews/question-graph-pilot-geometry.md:75`). The NEW text #200 supplied, applied verbatim, gives a reason ("framed as an undecided call only from v0.6") but never states the departure. The gap is inside #200, not in its application.
- `v0.3.yaml` gives no reason; #200's fixes cover only v0.4 and v0.5. Its "the measure is run as EPP1 on discrete arms" omits v0.3's empty domain ("Empty domain until a discrete controlled example exists", `v0.3-prose.md:139`). It also omits that EPP2 sat beside it: "EPP2 remains schematic hope" (`:141`), which #105 calls "co-equal with EPP1" (`:89`). EPP2 is a foil only from v0.4.
- The v0.6, v0.7 and v0.7.1 files drop the disclosure, although those versions still call (M1) "the working postulate here" and EPP1 "the working position" (`v0.6-prose.md:106, 362`; `v0.7.1-prose.md:104, 378`).

These are disclosures only: `a-m1` stays open and unselected.

OLD (`versions/v0.3.yaml`):
```text
the measure is run as EPP1 on discrete arms.
```
NEW:
```text
the measure is EPP1 on discrete arms, a "working postulate for narrative" with empty domain, beside EPP2 as a "schematic hope" (a foil from v0.4); a-m1 is not selected, as in v0.4.
```
OLD (`versions/v0.4.yaml`):
```text
(M1)/(M2) is framed as an undecided call only from v0.6 and stays open.
```
NEW:
```text
(M1)/(M2) is framed as an undecided call only from v0.6 and stays open. This departs from the Option F / V* convention above: EPP1 was this version's named postulate, and a-m1 is left unselected so that the viewer shows no lean on a call that is open now.
```
OLD (`versions/v0.6.yaml`):
```text
(M1)/(M2) framed as an undecided call;
```
NEW:
```text
(M1)/(M2) framed as an undecided call, with EPP1 kept as the named working postulate inside it (§1 "This is the working position"), so a-m1 is not selected because the call is open;
```

**2.6. The index's v0.4 and v0.5 bullets disagree with their yaml.** The v0.3 and v0.6 to v0.7.1 bullets match their files; these two do not.
- v0.5's "Composition and EPP1 as in v0.4" is right for the composition but not for EPP1. v0.5 first labels per-vertex EPP1 as departing from Paper 1's count (§7, the uneven tree, `v0.5-prose.md:152`). It lists the path-count alternative as open (`:175`). And it requires finite stars, or "a **named exhaustion**" for countable ones (`:129`, against v0.4's "finite or countable", `v0.4-prose.md:124`). The yaml has the path-count item.
- v0.4's bullet drops "with empty domain", which the yaml has (#200 S2 had it; its index mirror S7 dropped it).

OLD (`index.md`):
```text
Composition and EPP1 as in v0.4, so neither `a-alternation` nor `a-m1` is selected.
```
NEW:
```text
The composition is still plain alternation with no arrival flag, so `a-alternation` is not selected (Claude #128 row 2). EPP1 is a named postulate with empty domain, now labelled as departing from Paper 1's count (§7), with a path-count alternative listed as open (§9); `a-m1` is not selected ((M1)/(M2) is framed only from v0.6).
```
OLD (`index.md`):
```text
EPP1 is a named postulate; `a-m1` is not selected
```
NEW:
```text
EPP1 is a named postulate with empty domain; `a-m1` is not selected
```

**2.7. `versions/v0.4.yaml`: $V^*$ was not v0.4's only vertex answer on the table.** I agree with #200 that $V^*$ counts as accepted at the time ("may be selected", `v0.4-prose.md:21`; #106 "adopt $V^*$ with caveats"). But:
- v0.4's §9 lists the τ-slice for clause (2) as open (`:168`);
- §5.3 names curvature-scalar critical points as a lock-side candidate (`:127`), the seed of $V^\tau$;
- #117 calls the two "competing".

The synopsis is silent, so a reader would think $V^\tau$ first appears in v0.5 (1.16).

**2.8. "Neither strictness nor the arrival flag" in v0.4.yaml, v0.5.yaml and the index** should read "without a written positive-length clause or the arrival flag", for the reason in 1.18. The selection does not change.

**2.9. Further omissions in three synopses.**
- (a) **`v0.7.yaml`** does not mention `a-anchored-count`, although v0.7 is where its sentences first appear (`v0.7-prose.md:366`). Leaving it unselected may be right, since v0.7 states it inside the undecided call ("Neither fact is used to decide"). Unlike F and $V^*$ in v0.4, though, no reason is given.
- (b) **`v0.7.1.yaml`** names only the anchoring rejection (which, through `a-anchored-count`, covers P1's depth-1 correction). It omits:
  - P6–P8, the exact jump law at $c=0.01$, which `a-real-a` carries (dated "v0.7 on", 1.28);
  - two Literature #161 nits, which relabel T1 and put #139 (a)'s proper-time part under T1. `a-alternation` cites the second.
- (c) Nit: **`v0.5.yaml`** says "replace" but has no "Rejected at this version:" label, unlike v0.3 and v0.4.

**2.10. `q-law-of-r` in v0.3 and v0.4.** v0.3 ("Open: the law of R") and v0.4 (which rejects `a-hand-listed`, a child of `q-law-of-r`) pose the question without its second parent, `a-vtau`, in their selections. That parent exists only from v0.5. This is the selection side of 3.3.

---

## Question 3: structure

### Substantive

**3.1. A fork David asked for by name is missing, and the root absorbs its accepted answer.** David's notes:

> "One decision-making fork we need to add in the graph: triggered by a question. Are there physical objects that can be on observer and objects that cannot? … A rejected child node for privileged pieces of conscious matter. Accepted node will be: no privileged pieces of matter."
>
> (`docs/scratch/path-of-42.md:1`, #194)

The IH seed (§7, `docs/path-of-42.md` at `6f02238`) writes the same thing as root → question ("Which physical objects can and cannot be observers? Is there a privileged class?") → rejected "privileged (for example, conscious) matter", with why and reopen-if → accepted "no privileged matter", tag `method`.

The pilot puts "with no privileged observer matter" into `a-root`'s synopsis, and cites David's notes for it as root wording. It maps neither the question nor the rejected sibling, and does not list them under "not mapped". (`index.md:7` says the IH doc was used for "§§1–5, 8 and 9", which leaves out §7, yet `a-root` cites §7 for the root.) Folding the answer into the root puts "no privileged matter" at L0, as part of the goal, where both sources make it a method answer below the root. The fork is not a decision of v0.3–v0.7.1. It is the one decision David's method note asks the graph to contain, and the companion document of rejected options is incomplete without it.

There are two options: add the question and both answers (they would sit above `q-observer-object`), or list them as not mapped and take the clause out of the root. Hold levels for such nodes are David's call.

OLD (`a-root.yaml`):
```text
and David's notes (docs/scratch/path-of-42.md: no privileged pieces of matter).
```
NEW:
```text
and David's notes (docs/scratch/path-of-42.md). In both, "no privileged (pieces of) matter" is not the root but the accepted answer to a question under it ("Which physical objects can and cannot be observers?", IH §7), beside a rejected sibling, privileged (for example conscious) matter, which David asked the graph to keep. This pilot does not yet map that fork.
```

### Clarification

**3.2. The join layer's rejected options are understated.** The layer has nodes only for F and E. v0.4 §4.2 rejects Option D, "Glueing a $C^k$ spacetime metric in a single world (Option D) is rejected as primary: it clashes with locked analytic worlds or collapses into Direction Switching" (`v0.4-prose.md:77`; outline `:64`; cover `:22`), following #102 and #103. #104's adoption stamp on Geometry's note records the menu verdicts: "Reject D as primary; A parked until gauge-as-space; B only inside C" (`papers/piecewise-geodesic-Ck-graph.md:15`). So the D verdict carries David's adoption, and A was parked, not rejected.

Neither has a node or a not-mapped entry, so the "Rejected options by layer" entry for `q-join-law` (F only) understates what the record rejected at the join. #103's "E alone — too thin" was reversed by the accepted residue; it belongs with `a-option-e` (3.15), not here. v0.4 §4.2 also rejects infinite-order matching at joins, "that was the HOLE under CWS", a reason #117/#118 later corrected. It sits loosely beside `a-cws-branching`.

OLD (`index.md`):
```text
v0.3's rejected primaries (Direction Switching; instantaneous u-jumps), which were ruled before v0.3;
```
NEW:
```text
v0.3's rejected primaries (Direction Switching; instantaneous u-jumps), not recommended before v0.3 and rejected as primary in v0.3 §4.1 (u-jumps were later restated as ordinary type-(ii) candidates, v0.8.1 B.2b; Direction Switching drops out from v0.5); the other options of Geometry's join menu (#102): Option D, a C^k metric glued in one world, rejected as primary in v0.4 §4.2 (#104's stamp: "Reject D as primary; A parked until gauge-as-space; B only inside C");
```

**3.3. `q-law-of-r`'s second parent is younger than the question, and it sets h for the whole subtree.**
- The node: "Composition item 1 puts R's source set inside V^τ, hence the second parent". The edge has a record basis from v0.5: #128 classes item 1 as "the 'when' half of any star law, never the targets" (`reviews/v0.5-prose-claude-opus-5.5.md:209`).
- That constraint is conditional in v0.5 ("Require $R\subseteq V^\tau\times V$ when $V^\tau$ enforces clause (2)", `v0.5-prose.md:85`) and unconditional from v0.6 (`v0.6-prose.md:198`). v0.4 had none (#117: "there is no '$R\subseteq V^*\times V$'").
- The question itself is open from v0.3 ("The law of which edges exist is extra", `v0.3-prose.md:95`; §9 "Law of $R$", `:173`), and v0.4 rejects `a-hand-listed` under it (2.10).
- The record lists the slice choice beside the law of $R$: the header's three-part address (`v0.7.1-prose.md:9`), the §9 Open list (`:375–376`), and §5.4's "(slice, rule) pairs" (`:303`).

Structural effect: this edge puts the question at h = 0.5213 rather than 0.6859, and `a-hand-listed` and `a-kretschmann` at 0.2476 rather than 0.3258. What a reader may misread is the question's age, and its independence from the slice choice.

Options: keep the edge and disclose its date; or hang the question from `a-type-ii` only and record the source constraint in the rationale. I propose no values.

**3.4. `a-kretschmann`'s status does not fit the index's own gloss.** The index's scale reads open-plus-low-a as "one side of an undecided call" (`index.md:21`). The record poses no such call for this rule:
- "neither is an adopted $R$" (Firewall, `v0.7.1-prose.md:86`);
- it "fails the motivated gate";
- it is "a consistency witness for the schema **without (a)**" (`:296`).

The node's title ("unadopted worked model") and its rationale ("not as a candidate law") say so, and the viewer's side panel shows both. So a careful reader is told. What remains is that the status merges two roles, a would-be law that fails the gate and a model used as evidence, and that "open" means something different here than at (M1)/(M2) and (a)/(b).

Options include a line in the index's scale ("open: never adopted and never rejected; for `a-kretschmann`, not one side of a call"); a different parent (for example under `q-realisation`, where it is the (b) witness); or a non-IH marker such as "example". The choice, and any rating effect, is not mine. Related: 4.6.

**3.5. `a-option-e` merges three decisions.**
- the join law (Option E residue), public from v0.5;
- the branch-set definition $B_R$ under first-edge equivalence, written in v0.4 under Option F and kept when F was dropped. The record credits it with clearing the HOLE "as a definition" (1.14);
- the arm set, arms as elements of $B_R$, from v0.6 (1.1).

Because $B_R$ lives only inside the E node, v0.4's $B_R$ has no node, and it seems to come and go with the join law.

**3.6. `a-type-ii` merges v0.3's decision with v0.6's.** v0.3's decision is to add a type-(ii) pad; v0.6's is to assert existence as a working Postulate. The existence clause is also one side of an open call: Q-D1's "Existence (this paper's reading, via $R\ne\emptyset$)" (`v0.7.1-prose.md:410`). Because of the merge, a ruling on Q-D1 would rewrite an accepted node rather than choose between nodes (see 1.7b, 4.2).

**3.7. `a-everett-worlds` merges two firewalls.**
- Paper 1's firewall is on what a world is ("they are not Everett worlds", `papers/observer-space-ontology.md:189`). It belongs under `q-what-is-a-world`.
- The v0.6+ firewall is on what the weighted arms are. It sits in §7, under the reading of the weight: arms are "oriented observers joined by $R$, not decoherence branches", "not the Everett world-counting slot" (`v0.7.1-prose.md:323`). It bears on `q-measure`.

`q-what-is-a-world`'s synopsis ("what is counted when the paper speaks of alternatives") is answered in the record by the arms, not by worlds, which are "not extra vertices" (`:134`).

**3.8. `a-vtau` merges the accepted decision with an open call.** The decision is that vertex times come from a lock-side slice. The open call, "The slice: which scalar in the class of §5.1, and critical point versus level", is its own §9 Open item (`v0.7.1-prose.md:376`) and part of the HOLE's address. It has no open node. A rejected answer is also missing: v0.5's fallback of "(lump, τ) tags on homogeneous curvelets" (`v0.5-prose.md:117`), dropped in v0.6 as not lock-side ("τ needs an origin, which is history data", `v0.7.1-prose.md:262`).

**3.9. `a-jet-direction` answers both halves of `q-observer-object`.** It joins Paper 1's object (jet plus future time direction) with two framework-level items: the isotropy quotient, an outline commitment not in Paper 1, and the reading "observer space = $V$", "a reading, stated as such". The node's reason for L1 (Paper 1's object is a lock) covers the first part only. This is an observation about scope. Raising `q-observer-object` to L1 is David's call, and I say nothing about it.

**3.10. The accepted type-(i) layer has no node.** That layer is geodesic segments along the curvelet, with CWS "kept only as a null baseline" and "a coherent type-(i) package" in v0.3 (`v0.3-prose.md:17, 79`), and from v0.4 a singleton whose "null result is accepted" (`v0.4-prose.md:17`; `v0.7.1-prose.md:106`). Every version rests on it, and `q-join-law`, `q-vertex-times`, `a-option-e` and (a)'s $F(O)$ presuppose it. The v0.3 synopsis mentions it ("CWS demoted to the type-(i) null baseline"). But no node carries it, and only `a-cws-branching`'s rationale says it stays accepted, so a viewer user sees CWS only greyed out. It is not on the not-mapped list.

**3.11. The public controlled-example gate has no node, and it changed four times.**
- v0.3: "a controlled example … under an explicit $R$" (`v0.3-prose.md:115`). #105 §3.2 called it vacuous.
- v0.4: a stated rule; a hand-listed digraph does not qualify (`v0.4-prose.md:133`).
- v0.5: stated, uniform, and "carries a **named motivation** (symmetry, naturality, variational, or empirical — a menu, not a blank cheque)" (`v0.5-prose.md:136`). Under this, #128 row 6 found that the gate "returns no verdict" on the Kretschmann rule (`reviews/v0.5-prose-claude-opus-5.5.md:169`).
- v0.6: a motivation test, under which covariance, naturality and isometry-equivariance "hold for *every* rule defined on lumps … So they do not count as motivation" (`v0.7.1-prose.md:291`).

`a-hand-listed` is the gate's rejected side, and its rationale traces the v0.4 firewall, the v0.5 gate and the v0.7.1 bar in force. The gate's firewall half falls under the not-mapped "version firewalls". The v0.6 motivation test appears nowhere in the graph. Yet `a-kretschmann`'s "fails the motivated gate" depends on it (C26).

**3.12. Arm individuation has no node.** This covers "dying is not an arm" (from v0.4 §5.2: "**Die** is ensemble dropout, not a second Obs arm, unless an explicit terminal sink vertex is added and named", `v0.4-prose.md:118`) and its convention that ending and continuing count as one evolution (`v0.7.1-prose.md:268`). It also covers first-edge equivalence (v0.4 on; C11 records that an earlier literal wording gave 5 classes, not 3, `v0.6-prose.md:202`). None of these is on the not-mapped list, though 1.8 shows `a-type-ii`'s cost depends on them.

**3.13. Two older decisions sit inside `a-alternation`.**
- (a) **Proper time on segments only.** v0.4's composition already carries proper time only on type-(i) segments (§4.2 item 2; §10 Paper 1 row, `v0.4-prose.md:84, 202`). v0.4 and v0.5 rest on it but do not select this node.
- (b) **Direction versus walk semantics.** This was a named open one-liner in v0.4 and v0.5 ("**Direction (open).**", `v0.4-prose.md:94`; `v0.5-prose.md:94, 170`), settled in v0.6 as per-visit under (A) (`v0.6-outline.md:17`). The other side, a direction hypothesis on $R$, is "not needed", and none "could make histories acyclic here anyway, since successive periastra of a bound Schwarzschild orbit are one oriented germ" (`v0.7.1-prose.md:211`). It appears only as "Walk semantics follows" and is not on the not-mapped list.

**3.14. "v0.3's rejected primaries … ruled before v0.3".**
- "Ruled before v0.3" has support. v0.2/v0.2.1 call Direction Switching "Alternative (not current)" (`v0.2.1-prose.md:84`). Geometry's v0.2.1 motion recommendation advised against both as primary (`reviews/v0.2.1-motion-recommendation-geometry.md:102`). The v0.3 outline names them "only as rejected primary options" (`v0.3-outline.md:63`).
- But the rejection is also stated in v0.3 §4.1 and v0.4 §4.1 (`v0.3-prose.md:85`; `v0.4-prose.md:73`), inside the range. And their statuses later split. v0.4's oriented split makes bare orientation jumps type (ii). v0.5 floats an optional selection rule (`v0.5-prose.md:81`). v0.6 deletes it ("bare $u$-jumps are ordinary type-(ii) candidates", `v0.6-outline.md:17`). Direction Switching drops out silently: no mention from v0.5 to v0.7.1. v0.8.1 B.2b (P10) logs the $u$-jumps as "**restated** (ordinary type-(ii) candidates)" and Direction Switching as "**dropped**" (`v0.8.1-prose.md:535`); v0.8 had logged the joint row only as "restated".

The grouping hides that change. (A.5 below lists it for an extension.)

**3.15. #103's "Option E alone — too thin" verdict is reversed by v0.5, and the index does not say so.** The note David adopted in #104 judged "Option E alone — too thin" (`papers/piecewise-geodesic-Ck-graph-ontology.md:34`). The Option E residue made public in v0.5 is graph incidence plus jumps, without F's matching clause. #128 row 3 noted the piecewise notes "still call … Option E 'too thin'" (`reviews/v0.5-prose-claude-opus-5.5.md:129`), and #134's banner says the residue is not "too thin". #104 put two stamps in. The one on the Ontology note covers "Option F (and the §2 answers)" (`:17`). The one on Geometry's note records the D, A and B verdicts (3.2). Neither names "E alone — too thin" (or "C alone — incomplete"). I record this next to the Option F item in "Unclear record". I do not rule on it, and it is not one of the two items the cover reserves for David.

### Nit

**3.16. Further v0.3–v0.7.1 items that are neither mapped nor named in the not-mapped list.**
- **Matter fields.** These were lost silently, with the physical cost of analyticity, in v0.5 prose, and restored in v0.6 (`v0.6-outline.md:13, 18`). They are on the v0.7.1 §9 Open list.
- **The measure on completed histories versus at a cut** (§9 Open, `v0.7.1-prose.md:382`).
- **The withdrawal of the no-no-go sketch** from the title. It is in the v0.3–v0.5 titles, and v0.6 drops it (`v0.6-outline.md:12`). The Obs-local Hope it became is already named.
- **The dead-end convention** for comparing per-vertex weights with the count at a cut (v0.6 §7, from #129; `v0.7.1-prose.md:332`).
- **The lock-side definition itself** (v0.6 §2, `v0.7.1-prose.md:136`). It is cited in `a-alternation` and used in `a-vtau`, `a-real-a` and `q-law-of-r`, but has no node.
- **The 2007 tree** "not restored" (`v0.3-prose.md:69`; `v0.7.1-prose.md:150`).
- **v0.3 items B.2b logs as dropped:** Definition 8 (delayed fork), the §6 distinct-topology stipulation, and the v0.3 Open items gauge-as-space, tangent and path-space options, and analytic germ versus small-ball. The last is an alternative observer object, and it bears on `q-observer-object`.

Not every pre-v0.8 drop was unlogged. Among v0.3's items, v0.4 §4.3 drops Prop. 13's "waits on $\mathrm{Obs}$ as a space" clause with a reason (`v0.4-prose.md:102`). The v0.6 outline's "Dropped from v0.5" list logs its drops with reasons (`v0.6-outline.md:17`).

---

## Question 4: neutrality

The (M1)/(M2) pair holds up in substance. Both have the same a, `a-m2`'s cost line is item-for-item faithful to v0.7.1 §9 (apart from 1.31), and `a-anchored-count` corrects a claim about both. The findings are below.

### Substantive

**4.1. `a-real-a` against `a-real-b`: the mapping leaves out facts on both sides of (a).**
- `a-real-b` charges the model without (a) with jump dominance and failing (J1) and (J2). `a-real-a` says nothing of how the (a)-restricted model fares on them, though the record states it: "The (a)-restriction meets it over late windows … and fails it over early ones: the jump share is 1/2 over the decisions that occur … It fails (J2): one jump changes the orbit by $O(1)$" (`v0.7.1-prose.md:348`; T3 row, `:409`).
- `a-real-a` also omits the record's point in favour of (a). The restricted rule "is stated, uniform and lock-side", with "$|B_R|=2$ at both turning points", "So 'not fatal' does not depend on dropping (a)" (`:229`).
- The record's §4.2 bullet on (a) forbidding every edge off $F(O)$, including the cross-continuation jumps "a measurement picture would want", closes with "The cost of (a) is real, but it is not 'no curvature change'" (`:223`). `a-real-a` lists the same-class half of that cost (the lost Kretschmann edge) under "Costs recorded". It files the cross-continuation half under "What the record gives for (a)". `a-real-b` quotes the measurement-picture phrase as a point for (b).

A reader comparing the two nodes would conclude that only (b) has a (J1)/(J2) problem, and would miss both the strongest point and the named cost for (a).

OLD (`a-real-a.yaml`):
```text
Costs recorded: the worked Kretschmann rule loses one edge at each turning point of the instance
```
NEW:
```text
Costs recorded: the forbidding above is itself the cost the record names ("the ones a measurement picture would want"; "The cost of (a) is real, but it is not 'no curvature change'", v0.7.1 §4.2); the worked Kretschmann rule loses one edge at each turning point of the instance
```
OLD (`a-real-a.yaml`):
```text
with countably many completed histories (C33, v0.7 on);
```
NEW:
```text
with countably many completed histories (C33, v0.7 on); the record also gives that this restricted rule is stated, uniform and lock-side, with |B_R| = 2 at both turning points, so "not fatal" does not depend on dropping (a), and that it meets (J1) over late windows only and fails (J2), one jump changing the orbit by O(1), with a jump share of 1/2 over the decisions that occur (v0.7.1 §4.2, §7, §9 T3 row);
```

### Clarification

**4.2. `index.md`, Open-node rule.** "No accepted node stands for (M1)/(M2), T1–T3, Q-D1–Q-D5, #139 (a)–(e) or the law of R" is literally true. But two accepted nodes are each one side of an open call, as the record's own working position:
- `a-type-ii`'s $R\ne\emptyset$ is Q-D1's "Existence (this paper's reading, via $R\ne\emptyset$)" (`v0.7.1-prose.md:410`), and T3's "Rule jumps out" would give it up (`:409`);
- `a-alternation` is kept by two of T1's three options and given up by the third, "Drop (A)" (`:407`).

So a ruling on Q-D1, T1 or T3 could change or remove an accepted node. Both nodes disclose this locally. The index's gap list says T3 "Bears on `q-branching` and `a-type-ii`" and T1 is "Carried in `a-alternation`" (`index.md:95–96`). What it lacks is Q-D1's bearing on `a-type-ii` (`:97` lists Q-D1 with no node), and the consequence. The asymmetry is the record's: it adopts both items as working Postulates and calls only the measure "undecided" (`v0.7.1-prose.md:377`). The index rule should still say so. Saying it decides nothing. On this I disagree in part with #202's guardrail item 10.

OLD (`index.md`):
```text
No accepted node stands for (M1)/(M2), T1–T3, Q-D1–Q-D5, #139 (a)–(e) or the law of R.
```
NEW:
```text
No accepted node stands for (M1)/(M2), T1–T3, Q-D1–Q-D5, #139 (a)–(e) or the law of R. Two accepted nodes do hold one side of an open call, as the record's working position: `a-type-ii`'s R ≠ ∅ is the existence side of Q-D1 ("this paper's reading", v0.7.1 §9) and is given up by T3's "Rule jumps out"; `a-alternation` is kept by two of T1's options and given up by "Drop (A)". A ruling on Q-D1, T1 or T3 could therefore change or remove an accepted node; none is decided here.
```

**4.3. `a-m1` against `a-m2`: two small asymmetries from the mapping, and one from the record.**
- (a) **Pedigree.** `a-m1` gives (M1) a pedigree (MMWI 2006 per-split rule; SHPMP 2008 Definition 3). `a-m2` names Paper 1 as its source, but cites the earlier corpus (SHPMP 2008) only as a cost. Yet v0.7.1 §3 gives the count its own pedigree in that corpus too:
  - MMWI "**states** the count";
  - `Strayhorn3` "states path counting", "the form of Paper 1's count";
  - SHPMP kept a count on a refined sub-branch tree (Definition 4), tied to Definition 3 by Axiom 2 (`v0.7.1-prose.md:153, 155, 157, 159`).

  Either drop the pre-Paper-1 pedigree from both nodes or give one to each.
- (b) **The neutralised lean.** `a-m1` records "a lean neutralised" without saying which way it went. It went toward (M1) (1.24b).
- (c) **Referee hazards (the record's asymmetry).** The §9 cost lines carry a referee hazard for (M2), the maximal-entropy random walk, and none for (M1). §7 says the first SHPMP referee's hidden-variable reading of equal-share weights on an added transition layer "stays attached" (`v0.7.1-prose.md:317`; also §4.3, `:242`), and `a-m1` follows §9 only. Since this asymmetry is in the record, a pointer to `a-type-ii`, which carries the smell for $R$, is enough.

**4.4. `q-vertex-times`: the synopsis presupposes (M1).** "The per-vertex weight needs discrete branch points along each segment" grounds the question in (M1), an open answer under a sibling question. The record's reasons are wider:
- #105 §3.1 shows that both readings of the weight fail on a continuum of branch points (`reviews/v0.3-prose-claude-fable-5.1.md:72`);
- once clause (2) holds per history, "every proper-time cut [is] a finite tree when stars are finite", so a count at a named cut can be compared at all (C29, `v0.7.1-prose.md:334`);
- from v0.5, $R$'s source set would otherwise be a continuum (`:196`).

OLD (`q-vertex-times.yaml`):
```text
The per-vertex weight needs discrete branch points along each segment.
```
NEW:
```text
Any weight on the arms, under either reading, needs discrete branch points along each segment (#105 §3.1), as does any count at a named proper-time cut (C29); from v0.5, R's sources are also restricted to them (§4.2 item 1).
```

**4.5. Open or relocated items that read as results.**
- `a-type-ii`'s strong Prop. 13 (1.6).
- `q-law-of-r`'s dilemma without "a motivation problem, not a no-go theorem" (1.22a).
- `a-vtau`'s synopsis, "One-variable analyticity makes them discrete per curvelet", without the record's "in its open maximal domain" and its caveat that accumulation at a singular endpoint is possible (C8) and is handled by no-Zeno, "not $V^\tau$" (`v0.7.1-prose.md:252`).
- `a-option-e`'s "cleared as a definition" without "still relocated as a problem" (1.14).
- `a-cws-branching`'s "cleared as an error" without "relocated honestly to the law of $R$" (1.12d).

Each is one clause.

OLD (`a-vtau.yaml`):
```text
One-variable analyticity makes them discrete per curvelet.
```
NEW:
```text
One-variable analyticity makes them discrete per curvelet, in its open maximal domain; accumulation at a singular endpoint remains possible (C8) and is handled by the no-Zeno clause, not by V^τ.
```
OLD (`a-cws-branching.yaml`):
```text
Claude #105 judged the HOLE "cleared as an error" by this move.
```
NEW:
```text
Claude #105 judged the HOLE "cleared as an error, relocated honestly to the law of R, not fatal" by this move.
```

**4.6. `a-kretschmann`: "meets the bar in force" and "evidence for 'not fatal'" are not paired with the Firewall.** The Firewall says of the rule and its restriction alike: "Neither is a controlled public example, and neither is an adopted $R$" (`v0.7.1-prose.md:86`). The node also omits why the bar in force is "uniform, not a hand list": "No rule meets the motivation clause" (`:303`). This is the neutrality side of 3.4.

OLD (`a-kretschmann.yaml`):
```text
The paper uses it as evidence for "not fatal", not as a candidate law.
```
NEW:
```text
The paper uses it as evidence for "not fatal" (a consistency witness for the schema without (a), §5.4), not as a candidate law; the Firewall says of it and its (a)-restriction "Neither is a controlled public example, and neither is an adopted R". The bar in force is "uniform, not a hand list" only because no rule meets the motivation clause (§5.4).
```

**4.7. `a-world-analytic`: the record's open item and status wording are missing.** The open item is "Whether $E_W$ should be restricted to inextendible or maximal members is open" (`v0.7.1-prose.md:134`; §9 "Ensemble hygiene and inextendibility, if $E_W$ becomes load-bearing", `:388`). The status wording is "The definitions in this section are the working ones for review" (`:120`). I make no proposal about values.

OLD (`a-world-analytic.yaml`):
```text
Record note: v0.3's "topology may vary"
```
NEW:
```text
Open in the record: whether E_W should be restricted to inextendible or maximal members (v0.7.1 §2; §9 "Ensemble hygiene and inextendibility, if E_W becomes load-bearing"); §2's definitions are "the working ones for review". Record note: v0.3's "topology may vary"
```

### Nits (Question 4)

| # | Node | Finding |
|---|---|---|
| 4.8 | `a-alternation`, `a-option-e`, `a-vtau` (titles; index table) | Of the seven accepted nodes, only `a-type-ii`'s title gives the record's status ("working, abandonable"). The record calls (A) a "working Postulate, revisable" (`v0.7.1-prose.md:384`), the residue a "working, abandonable pad" (`:106`) and $V^\tau$ "A candidate lock-side slice" (`:248`). The index table shows status and q/a (a = medium is glossed "working, abandonable, or with a named cost"), but not the record's own words, which sit only in each rationale. Suggested suffixes: "(working Postulate, revisable)", "(working, abandonable)", "(candidate)". |
| 4.9 | `a-target-avoid` | `a-jump-bound` says T1's "drop (A)" column lists it. `a-target-avoid` does not say that T1 names (C) too ("or kill the worked instance (target avoidance)", `:407`). |
| 4.10 | `a-m1` | "runs with EPP1 … from v0.3 on …, but records the choice as undecided": the first half is the record's own working position (§1 "This is the working position"), not a lean added by the mapper. The second half dates from v0.6 (1.2). |

---

## Separate part

### A. What an extension to v0.8, v0.8.1 and the scoping note would need (list only)

The status of each item is the record's. The scoping note is "**SCOPING ONLY, NOT A CLAIM**", and an extension must not turn it into accepted nodes. To avoid a clash of labels, "ruling F*n*" means the Lead's v0.8 rulings and "family F*n*" means the scoping note's families.

1. **New version files `v0.8` and `v0.8.1`, selecting the same seven accepted answers.** v0.8 is "Presentation and hygiene only. … No physics claim, pin or number is added, and no (M1)/(M2) choice is made" (`v0.8.1-prose.md`, B.1). v0.8.1 is "Patch only" (header). v0.8 was never made current: "`v0.7.1-prose.md` stays the current draft until this file is adopted" (`v0.8-prose.md:5`). v0.8.1 is current by the Lead's status edit (#213). The pair has a precedent in v0.7/v0.7.1. Changes needed: `graph.yaml`'s title range, and `index.md`'s "v0.8 are outside the range".
2. **Changed source labels.** 22 node files label their pinned v0.7.1 source "(current draft)". Since #213, v0.7.1 is "the prior prose" (`v0.8.1-prose.md:5`). The pinned `5acf9d3` URLs remain correct historical pins.
3. **`a-real-a` and `a-real-b`: changed sources.** P1–P9 (#201 R1 as extended by #203, applied in #205) scope the Kretschmann (a) results to the instance. #206 copied the scoped wording into both nodes but added no source. They still cite only v0.7.1, whose §4.2, §5.4 (third bullet) and §9 still say "outward edges" (for example "loses its outward edges", `v0.7.1-prose.md:385`); only §5.4's first bullet and the (a)-restriction paragraph support the per-turning-point wording. Add #201, #203, #205 and v0.8.1 §4.2, §5.4 and §9.
4. **Record note only.** #203's turning-type lemma: at every turning point of every bound orbit, the edge into the orbit's radial range fails (a). #211 suggested carrying it in the next full version, "a suggestion, not a gate". It is not in v0.8.1. At most it is a note on `a-real-a` and `a-kretschmann`, cited to #203 and #211, not to the paper.
5. **P10 (#201 R2, #203).** B.2b splits v0.3's "Rejected as primary" row: the $u$-jumps are "**restated** (ordinary type-(ii) candidates)" and Direction Switching is "**dropped**". The index's not-mapped entry changes (3.14). If they are mapped, Direction Switching would be a new answer under `q-branching` (rejected in v0.3, dropped later), and `a-type-ii`'s synopsis would change to cover bare orientation changes.
6. **Further v0.3 drops that B.2 logs.** These are Definition 8; one clause of Prop. 13; Compatibility's mutual relation; the §6 distinct-topology stipulation and particle picture; and the v0.3 Open items gauge-as-space, tangent and path-space options, and analytic germ versus small-ball. They would be record notes on `a-type-ii`, `q-realisation`, `q-observer-object` and `q-law-of-r`. The index's "Unclear record" line, which names two drops, would change. The status is "dropped": "drops before v0.8 were unlogged, and nothing dropped is reinstated (F7)" (ruling F7).
7. **`a-gielen-wise`'s reopen condition.** It rests on the named-home question for gauge, which `obs-as-a-space.md` keeps open in-house. The public paper logs v0.3's gauge-as-space Open item as dropped, and §2 now says "Gauge is this identity". This is a changed note: the condition is in-house only.
8. **`a-world-analytic`'s synopsis.** v0.8 defines $E_W(O)$ by occurrences of the germ (I2), with #179's disclosure that indexing by $O^u$ gives the same pointed worlds (ruling F4). Wording only; the status is unchanged.
9. **The EPP2 foil.** v0.8 restores the arm-to-ensemble caveat (ruling F6) and adds the $E_M$ multiplicity disclosure (ruling F5). This changes `q-measure`'s EPP2 mention and the not-mapped entry. No node is needed unless EPP2 is mapped.
10. **`a-m1` and `a-m2`: both or neither.** v0.8 adds paired clauses in §9's "Both rules as counts at a cut" (ruling F10, "both or neither"): EPP1's unequal weights wherever branching differs (C12, C13, C33), and the count's next-step weights depending on where the cut sits, through recurrence along a bound orbit. An extension that re-sources one node must re-source the other.
11. **Three new firewall rows: EKT 1991, Israel's junction conditions, and SSA.** Each says "Not used". Ruling F2 keeps Paper 1's EKT existence-proof clause out, and P11 and P12 reword the SSA and EKT rows. The rows bear on `q-branching`, `q-join-law` ("not a spacetime metric glued across a surface"; "Matching jets to a finite order at a join cannot create a branching edge") and `q-measure`/`q-what-is-a-world`. The pilot maps two firewalls as rejected answers but lists "the version firewalls" as not mapped. These rows need a decision either way: nodes, or not-mapped entries. They are firewall rows, not rejections.
12. **Presentation only; no node.** The §6 locality slogan is deleted (ruling F3), Kent is cut as an attribution change (ruling F11), and Paper 1 §8's sentence is quoted at the §8 circularity wall. At most the circularity entry cites v0.8.1 §8.
13. **The Q-D labels.** v0.8 moves v0.7.1's header changelogs into pointers in B.1 (ruling F8, option B1). Neither v0.8 nor v0.8.1 contains "Q-D". The Q-D map that the index and `q-measure`, `q-branching`, `q-composition`, `a-type-ii` and `a-alternation` anchor to "the v0.7.1 header" would rest on B.1's pointer. Their sources or wording would change if re-sourced.
14. **The law-of-R scoping note (#178; v2 #187; #204; reviews #182, #185, #189). Scoping only.**
    - (a) `q-law-of-r` should add #204 to its list. v2, after #185 ruling 1.1, narrows the singleton-or-continuum result to "the named lock-side selection devices"; it "is not a blanket 'no map'", and "An explicit lock-side map on a slice can give finite stars without a grain (F1)" (`law-of-R-scoping.md:19, 78`). The rationale would carry that narrower scope.
    - (b) **Families F0–F11.** Added under `q-law-of-r`, they would be new nodes, and no IH status fits them. "Surviving is not adoption or ranking; no family is endorsed" (`:122`). F1's exclusion is "conditional on that aim" (I13), so no family can be accepted, and marking family F1 rejected would overstate the record. An extension needs a convention for scoping-only nodes, or should leave them out.
    - (c) **`a-kretschmann`.** The note treats the rule as stated (F1), its (a)-restriction (F2) and the short-jump reading (F3) as separate families with different constraint profiles. A split would rest on the scoping note alone: v0.8.1 still carries them as one unadopted example.
    - (d) **`a-vstar`.** Its reopen route, a chosen discrete sub-ensemble, is family F10, which #185 ruled "fails a convention in force" (E-smuggling). This changes the note on its reopen condition.
    - (e) **Overlaps.** F9 is arrival option (C), already `a-target-avoid`. F0 (empty $R$) overlaps `a-cws-branching` and "whether to abandon type (ii)". Mapping either under `q-law-of-r` would duplicate nodes; a second parent for `a-target-avoid` would be the alternative.
    - (f) **T3 (a gap node, if one is added).** The preregistered Q4 readout (specified in #182, run in #185) reads "**SEPARATES**". It "does not establish that F3 meets (J2)", and "Windowed (J1) is not met" (`:195, 209`). It is a scoping-only data point, and it must not edit the paper's T3 cells.

### B. Other findings (not questions 1–4)

- **B.1. Where the rejected "unless anchored" clause came from (`a-anchored-count`).** It did not start in v0.7. It is *Mathematical Foundations*' T2 wording, "unless the cut is anchored at the current observer" (`public-essays/mathematical-foundations/versions/v0.3.md:183`, the same in v0.2), and #142's note-6 bullet. v0.7 reproduced it (#168 §4.4). The essay still carries it, and `q-measure` identifies that essay's T2 as the same call. This is flagged only: essay edits are out of bounds, and nothing here bears on T2's resolution.
- **B.2. The paper's own Prop. 13 pair.** From v0.6 through v0.8.1, §4.2 says "Locked data determine no type-(ii) edge (Prop. 13)" and §4.3 says "Locked data *can* determine off-curvelet stars". Claude #105 had called "determine" the wrong verb (`reviews/v0.3-prose-claude-fable-5.1.md:84`). This is a note on the paper, not on the folder; paper edits are out of bounds. `a-type-ii` inherits it (1.6).
- **B.3. "Rejected options by layer" lists `a-anchored-count`** as a rejected option for "How are the arms weighted?". It is a rejected claim about the options, as #200 §2 noted. Read as David's companion document, the layer then shows a corrected sentence as if it were a weighing rule. A one-line gloss in the index would prevent that.

---

## Unchecked

- **The viewer build** (`build/build.mjs`, path-of-42-viewer) was not run. h and the hold cap were recomputed independently. The "2 warnings, 0 errors" result is taken from the index and #200.
- **infinite-harness `docs/hold-axis.md` §3 and the viewer README** were not read. Hold levels and the format are taken as given; ruling on them is out of bounds.
- **Primary manuscripts** (MMWI 2006, SHPMP 2008, AFLB 2008, `Strayhorn3`) were not opened. Pedigree statements were checked only against v0.7.1 §3 and the earlier version texts. The Gielen–Wise external record was not re-checked (I relied on #158 and #202).
- **Numbers.** None of the paper's numbers was recomputed: C2's factor 3.8, C13's 1/10 and 1/15 (checked by hand only), C33's census and exact law, C34's 2/3, and #203's lemma.
- **Reviews read only in part or through quotation:** Geometry #131, Literature #132, #136 and #161 (through the v0.6, v0.7 and v0.7.1 changelogs); the v0.4 outline and prose panels (#109–#111, #113–#115); the v0.5 outline Literature and Ontology panels (#121, #122). #129 and #118 were read for the sections the nodes cite.
- **PR bodies** other than those listed under Sources were not read.
- **v0.6 and v0.7 prose** were read by section and grep, not line by line.
- **A David signature** for the Option F demotion, the CWS demotion or the type-(ii) adoption was not searched for beyond the PR bodies and status lines read. None of these is decided here.
- **The pinned blob URLs** (`5acf9d3`) were not fetched over HTTP. `git log 5acf9d3..21e2f09` shows that no version or `papers/` file in range has changed since then.

## Provenance

- **Model:** Claude Opus 5.5 (`claude-opus-5-5`).
- **Run:** manually, at the requester's prompt, from the Claude desktop app (Code tab), on a local checkout of `main` at `21e2f09` with read-only `gh` access. It was not run by the queue automation.
- **Workflow:** two background workflow runs of read-only subagents, all Claude Opus 5.5:
  - 10 readers, one per checklist slice (Q1 in four node groups, Q2 in two version groups, Q3 in two, Q4, and the separate part), returned 169 candidate findings;
  - 8 adversarial verifiers then tried to refute the 50 findings consolidated from them.
  
  The verifiers confirmed 24 findings and qualified 26 (PARTLY); none was refuted outright. I applied their corrections, which moved several findings from Substantive to Clarification and reworded two to stay out of open calls (1.5 on T1, 2.3 on T1). I re-checked the substantive findings against the files myself, merged duplicates, and dropped one candidate of my own that did not survive: a supposed mislabel of #128's row in #134's banners (#128 row 3's residual is where those banners were requested). Then I wrote this file.
- **Recomputation:** h and the hold cap, by a short Python script (not committed). The OLD-string uniqueness check was also scripted.
- **Filing:** the `gh` account available here (`ark-clawds4`) has read-only permission on `nous-clawds4/physics`. At the requester's direction, the pull request was therefore opened from the fork `ark-clawds4/physics`. The commit carries the local git identity (`nous-clawds4`).
