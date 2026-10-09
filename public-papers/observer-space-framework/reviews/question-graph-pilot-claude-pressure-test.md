# Pressure test: Claude's exploratory critique of the question-graph pilot (#224)

**Reviewer:** Geometry. **Record reviewed:** `reviews/question-graph-pilot-claude-opus-5.5.md` (#224, `332f7c5`), no verdict. **Read against:** `main` at `332f7c5`; the `question-graph/` folder; the version files (v0.1 outline to v0.8.1); reviews #105, #117, #118, #128, #129, #131, #168, #169, #200, #202; `papers/` notes cited by the nodes. **Scope:** every finding in Q1–Q4 is ruled, except those marked FOR DAVID. Separate part A is checked for factual errors only; part B is not ruled. Record only: this review adopts nothing, rates nothing as adopted that was not, and decides no open call. (M1)/(M2), the law of R, T1–T3 and Q-D1–Q-D5 stay open.

## 0. State of the folder on main

- The graph files last changed in #199 (`33c06d2`, head `084809e`) and #206 (`83ff2d6`, a-real-a/a-real-b instance scoping). Nothing later touches `question-graph/`.
- **#200 (Geometry): 13 of 13 fixes landed** (S1–S9, H1–H3, G1), checked string by string by script.
- **#202 (Literature): 18 of 18 fixes landed**, checked the same way.
- On `main` the viewer (path-of-42-viewer `82fd625`, `node build/build.mjs`) gives 30 nodes, 6 versions, 2 warnings (v0.4 selects `a-option-f` and `a-vstar`, expected), 0 errors. An independent h script gives 0 mismatches.
- Two of Claude's findings fall on my own #200 text: S5 (2.1, "the rest changed in open and rejected nodes" is wrong) and S7 (2.6, the index mirror dropped "with empty domain"). I confirm both below.

## 1. Rule for FOR DAVID

A finding is marked FOR DAVID, with no ruling and no APPLY, if it is 3.1, one of 3.3–3.9, or 3.15. It is also FOR DAVID if its OLD or NEW adds, removes or rewords what the graph says about any of these:
- a side, cost, framing or history of (M1)/(M2): `q-measure`, `a-m1`, `a-m2`, or the standing of EPP1;
- T1: (A), "Drop (A)", or the arrival flag as history data;
- Q-D1: R ≠ ∅ as existence or permission;
- a hold level.

A mathematical correction that applies equally to both measures (1.4) is ruled. Where only part of a finding touches these, that part is FOR DAVID and the rest is ruled.

## 2. Priority items

**1.1 (`a-option-e`, index): CONFIRM, APPLY-AMENDED.**
- The record keeps B_R = {[γ]} ∪ succ_R from v0.4 on: v0.4 :79, :88; v0.5 :17, :19, :79, :90.
- What changed is the arms wording, "arms are the graph out-star" (v0.4 cover :17; v0.4 §4.2; v0.5 §1 and §4.2), flagged by #117 :73 and fixed by #128 row 4 (:142), giving v0.6's "the elements of B_R" (v0.6 :186).
- Claude's node NEW replaces only the parenthesis, which would leave "the arm set changed across versions" standing in front of it. The amended OLD therefore takes the whole record note and says "the arms wording changed across versions, not B_R".
- The index string is APPLY as given.

**1.2 (`q-measure`, "Undecided in every version"): FOR DAVID** ((M1)/(M2) framing). See §4.

**1.3 (`a-option-f` reopen_if): CONFIRM, APPLY-AMENDED.**
- #118's QUALIFY (:34–40) keeps truncated-jet language as housekeeping and states no reopen condition, so "Mapper's wording of #118's QUALIFY" claims a backing the record does not give.
- The node's condition cannot be met. At k = 1 matching between distinct lumps is vacuous, and at k ≥ 2 #118 has it force equal curvature "under any identification that makes the comparison defined". So no canonical comparison of either kind is available.
- Claude's NEW drops the k = 1 half and credits Claim A to #118 alone. The amendment restores the k = 1 half and attributes Claim A as "#117 §2.1, Claim A, accepted by #118".

**1.4 (`a-anchored-count`): QUALIFY, APPLY-AMENDED (reopen_if, index mirrors), APPLY (title).** Computed on C13's tree:
- **The tree.** The root has children A and B. A has A1–A3 with 2 leaves each; B has B1 and B2 with 3 leaves each, for 12 leaves.
- **Fixed cut, depth 3.** The tree is D-constant there. EPP1 and the count both give 1/12 per leaf, and so does the depth-1 anchor.
- **Count re-anchored at each state, two steps ahead.** At the root, A has 3 grandchildren and B has 2, so A gets 3/5 and B 2/5. Under A each A_i gets 1/3; under B each B_j gets 1/2. An A-leaf gets 3/5 · 1/3 · 1/2 = 1/10, and a B-leaf gets 2/5 · 1/2 · 1/3 = 1/15. Check: 6 · 1/10 + 6 · 1/15 = 1.
- So D-constancy is necessary, not sufficient: on C13's own D-constant tree one anchored count keeps equal weight and another does not. The exclusivity claim is false on every tree, because anchored counts are state functions for every k (#169).
- Claude's NEW says the named cases are "not … cases where an anchored count keeps equal weight". That goes too far, since the depth-1 anchor does keep it there. The amendment says "not as trees on which any anchored count keeps equal weight" and gives the 1/12 agreement.
- Claude's title is APPLY. It is mirrored in index lines 59 and 89 (APPLY-AMENDED, the same title). `v0.7.1.yaml` and index :77 paraphrase the claim ("at no cost") and stay as they are.
- No q, a, h or parent changes.

**2.1 (`v0.6.yaml`, index): CONFIRM, APPLY-AMENDED.**
- v0.6 revised three accepted nodes that it selects:
  - `a-jet-direction`: v0.6 :20, :104, :128 and outline :10;
  - `a-type-ii`: v0.6 :24, :190 and outline :22;
  - `a-vtau`: v0.6 :243–257 and outline :17, :23.
- It also reworded `a-option-e`'s arms.
- My #200 S5 was wrong.
- The amended NEW names the changed accepted nodes as pointers. For `a-type-ii` it gives only "rewritten after #128 and Geometry #131 R2", because the content of the change (R ≠ ∅ as an existential working Postulate) is Q-D1 and goes FOR DAVID.
- It is mirrored in the index v0.6 bullet. The index's "each file's synopsis says what changed in open and rejected nodes" becomes "what else changed".

**2.2 (`v0.7.yaml`, index): CONFIRM, APPLY-AMENDED.**
- (A) went from "(A) is adopted" (v0.6 :368) to "working Postulate, revisable" (v0.7 :356). R ≠ ∅ gains "revisable" (:361) and the EPP1-domain sentence (:162).
- C38 is new in v0.7. The `a-anchored-count` sentences first appear at :366. #139 (a)–(e) are in v0.7's calls table (:374, :385–388).
- The amended NEW records that the status wording for (A) and for R ≠ ∅ changed, pointing to v0.7 §9 and §4.2, without restating it. It adds C38, the `a-gielen-wise` correction and the first appearance of the `a-anchored-count` sentences, and adds "#139 (a)-(e)" to the open-calls list.
- The content clauses of Claude's NEW go FOR DAVID: the arrival flag as history data, T1's "Drop (A)", and R ≠ ∅'s EPP1-domain clause. These are T1 and Q-D1.
- The NEW is mirrored in the index v0.7 bullet.

**4.1 (`a-real-a`): CONFIRM, APPLY (first string), APPLY-AMENDED (second, merged with 1.28).**
- The record gives the (a)-restricted rule's (J1)/(J2) standing (v0.7.1 :348, T3 row :409), its point in favour (:229) and the named cost (:223).
- The second string carries Claude's facts with the record's instance scope (#206): "|B_R| = 2 at both turning points of the orbit [10, 20] for c = 0.1 and 0.01".
- It is re-ordered so that (J1)'s two halves sit together.
- It also carries 1.28: "12 to 14" is v0.7.1's P6–P8 law; v0.7 said "13 or 14" (v0.7 :202).
- Neither side is given more weight than the record gives it. `a-real-a` and `a-real-b` both stay open.

## 3. Rulings, all items

C = CONFIRM, Q = QUALIFY, R = REJECT, FD = FOR DAVID. String rulings: A = APPLY, AA = APPLY-AMENDED, D = DECLINE. "—" means no string was offered.

| # | Ruling | Strings | Basis (record) |
|---|---|---|---|
| 1.1 | C | AA, A | see §2 |
| 1.2 | FD | — | (M1)/(M2) framing; §4 |
| 1.3 | C | AA | see §2 |
| 1.4 | Q | AA, A, AA×2 (index mirrors) | see §2 |
| 1.5 | FD | — | T1 ((B) is "Drop (A)"'s replacement); §4 |
| 1.6 | C | A | strong form v0.6 :191 / v0.7.1 :189; soft form from v0.4 :100, v0.7.1 :238; v0.8 B.2b :510 "restated; one clause dropped" |
| 1.7 | Q | AA; (b) FD | (a) v0.4 :5 "relocation completed here…", #117 disputed; (c) `papers/type-ii-adopted.md:5`, added `9c22d9f` 2026-08-30; (d) v0.4 :55, v0.7.1 :148. The amended NEW omits (b), the existence-clause history (Q-D1) |
| 1.8 | C | A | v0.7.1 :456; §5.2 :268 |
| 1.9 | Q | AA, A; T1-quote string FD | Claude's node NEW repeats B.2a's "kept", which the rationale already gives, so the amendment drops it; v0.4/v0.5 outlines :31 "u modulo germ isotropy (named)". The quote fix sits in the hold-L1 justification and the T1 row, so FD |
| 1.10 | C | A | v0.1.1 outline :7; v0.3 :196 (§10); v0.6 outline :24–25 (#132 finding 2) |
| 1.11 | Q | AA | Homonym reading confirmed (Paper 1 :57). Claude's dating is wrong in one place: v0.3 §2 says "same English phrase, different object" (:45), not "phrase collision only". That phrase is in the v0.1.1 outline (:34, :142), v0.2/v0.2.1 :187 (§10) and the firewall table from v0.4 (:194; v0.7.1 :471). The amendment also fixes "(v0.7.1 §2, §10)" to §10 |
| 1.12 | Q | AA, A; 4.5's string A | CWS as a type-(ii) motion law dates from the v0.1 outline (:14), not v0.2.1. Sketch step 3 holds ("World switching changes lifetime, not path") |
| 1.13 | Q | A, AA | #102 :77 "Hybrid default candidate", :136 lean. Claude's NEW brings back "does no work for branching edges", which #128 row 1 found inaccurate; the amendment keeps "cannot create a branching edge" |
| 1.14 | C | A | v0.5 header; #117 verdict kept by #118 |
| 1.15 | C | A, A | §5.1 :250 has no "motivated"; §2 :134 E-smuggling; v0.5 outline changelog (2); #120 |
| 1.16 | C | A | v0.4 §5.3 :127; #118 :70. Nit: "every locally symmetric lump" is #131's (v0.6 outline :23), not #129's |
| 1.17 | C | A, AA | #102–#104 merged 2026-09-07, #105 2026-09-08. The amendment marks #105's "(C)" as #105's own lettering, not the graph's (A)–(C) |
| 1.18 | C | AA | #117 read v0.4's "alternates" as strict. Last sentence reworded to avoid the letter clash |
| 1.19 | C | A | #128 :106 "jumps carry no proper time" |
| 1.20 | C | A, AA | #117 :85; v0.5 outline :116; v0.5 prose 0 hits; v0.6 outline :18. The amendment cites "§5.4, first bullet", since the third bullet is about outward edges |
| 1.21 | C | AA | #129's second cost and its conditional verdict; placed after the first cost |
| 1.22 | C | A, A | v0.7.1 :240; header :9 |
| 1.23 | FD | — | (M1)/(M2) framing history; §4 |
| 1.24 | FD | — | `a-m1` lean and pedigree; §4 |
| 1.25 | C | A | #131 R1 via v0.6 outline r2 |
| 1.26 | C | AA | v0.7.1 §1 sentence continues with the jet. Claude's colon would make the parenthetical the quoted object; the amendment ends "The phrase:" |
| 1.27 | C | A | v0.4 §2 has neither clause; v0.8 B.2b :520, :523 |
| 1.28 | C | AA (merged with 4.1) | v0.7 :202 "13 or 14"; v0.7.1 P6–P8 |
| 1.29 | C | A | v0.7.1 :38; #169 :200 |
| 1.30 | C | AA | "the rule fails" (conditions are on the rule); C34 added |
| 1.31 | FD | — | `a-m2` For/Against wording; §4 |
| 1.32 | C | A | every version states the object in §1 |
| 1.33 | C | A | v0.7.1 :106, :182, :447 |
| 1.34 | C | A | no one argued for a hand list; #105 named the loophole |
| 1.35 | C | A | v0.4 :112 |
| 2.1 | C | AA×3; content FD | see §2 |
| 2.2 | C | AA×4; content FD | see §2 |
| 2.3 | FD | — | T1 (plain composition's status); §4 |
| 2.4 | FD | — | selection convention for R ≠ ∅ (Q-D1); §4 |
| 2.5 | FD | — | EPP1/`a-m1` disclosures; §4 |
| 2.6 | FD | — | EPP1 in index bullets; §4 |
| 2.7 | C | — | v0.4 :168, :127; #117 "competing". 1.16's string covers the node |
| 2.8 | Q | AA×2 (supplied) | Correct for `v0.4.yaml` and the index. `v0.5.yaml` has no "strictness" phrase |
| 2.9 | C | — | (a) v0.7 :366; (b) P6–P8 and #161 nits omitted; (c) nit holds |
| 2.10 | FD | — | selection side of 3.3; §4 |
| 3.1 | FD | — | §4 |
| 3.2 | C | AA | v0.4 §4.2 :77; #104 stamp `piecewise-geodesic-Ck-graph.md:15`. The amendment states the u-jump / Direction Switching split as v0.8.1 B.2b logs it, and marks #104's letters as the join menu's |
| 3.3–3.9 | FD | — | §4 |
| 3.10 | C | — | v0.3 :17, :79; v0.4 :17; not on the not-mapped list |
| 3.11 | C | — | v0.3 :115, v0.4 :133, v0.5 :136, v0.7.1 :291 |
| 3.12 | C | — | v0.4 :118; v0.7.1 :268; v0.6 :202 (C11) |
| 3.13 | FD | — | (a) proper time on segments sits under T1 (#161); §4 |
| 3.14 | C | — (covered by 3.2's string) | v0.2.1 :84; v0.3 outline :63; v0.8.1 :535 |
| 3.15 | FD | — | §4 |
| 3.16 | C | — | v0.6 outline :12, :13, :18; v0.7.1 :136, :150, :332, :382 |
| 4.1 | C | A, AA | see §2 |
| 4.2 | FD | — | Q-D1, T1, T3; §4 |
| 4.3 | FD | — | (M1)/(M2) pedigree and hazards; §4 |
| 4.4 | FD | — | grounds a question in (M1); §4 |
| 4.5 | C | A, A (+1.6, 1.14, 1.22) | v0.7.1 :252; #105 verdict |
| 4.6 | C | A | v0.7.1 :86 (Firewall), :296, :303 |
| 4.7 | C | A | v0.7.1 §2, §9 |
| 4.8 | FD | — | status suffixes in titles, including (A)'s (T1) |
| 4.9 | FD | — | T1's naming of (C); §4 |
| 4.10 | FD | — | `a-m1` lean dating; §4 |

Minor line reference in Claude's text: the "Escape CWS HOLE" table is at `papers/piecewise-geodesic-Ck-graph-ontology.md:20`, not :61–63. Of 257 citations checked by script, the others resolve or are off by a line or two.

## 4. FOR DAVID (options stated neutrally; no ruling)

- **1.2 `q-measure`, "Undecided in every version".** Record:
  - v0.3 :139 "working postulate for narrative";
  - v0.4 :147 "named postulate";
  - v0.5 :175 first lists a "Path-count alternative";
  - "This paper does not choose between them" was added in v0.6 (:62, `badc85e`).

  So the sentence is false for v0.3–v0.5. Options: Claude's NEW; a minimal date fix ("from v0.6 on"); leave it.
- **1.5 `a-jump-bound`.** Facts check: C5 is on the model without (a); C33 gives the restricted model finite chains (longest 14); v0.7.1 §9 :384 keeps (B) rejected and does not link the two. Options: Claude's two strings; the first only; neither.
- **1.7(b) `a-type-ii`, existence-clause history.** Record:
  - v0.3 §4.2 "Existence of type-(ii) edges";
  - none in v0.4 or v0.5 prose ("the pad as written admits R=∅", #128);
  - v0.5 outline :68 has it;
  - existential working Postulate from v0.6.

  Options: add the history to `a-type-ii`; leave it to a Q-D1 node if one is made.
- **1.9 T1-row quote in `a-jet-direction`'s hold-L1 sentence.** The record's words are "which this paper cannot take without the lock being changed". Options: Claude's exact quote; keep the bracketed paraphrase.
- **1.23, 1.24, 1.31 (`q-measure`, `a-m1`, `a-m2` wording).** Facts as Claude gives them check against #128 row 5 and §4.1, #129 claim 4, #132, #155, and v0.7.1 §9 ("implied", "would carry"). Options: apply all three as a set; apply none. Applying one side's wording alone would make (M1) and (M2) asymmetric.
- **2.3 `q-composition` in v0.4/v0.5.** The plain composition (v0.4 :84, v0.5 :86) has no node. The record rejects only (B) and (C) (v0.7.1 :207–210), and "Drop (A)" is a T1 option. Options: Claude's disclosure line; a not-mapped entry; leave it.
- **2.4 selection convention.** v0.4 and v0.5 prose state no R ≠ ∅ clause; the isotropy sentence is missing from v0.5 prose. Options: a one-line note in `v0.4.yaml` and `v0.5.yaml`; leave it.
- **2.5, 2.6 EPP1 disclosures.** Record:
  - v0.3 :139 (empty domain), :141 (EPP2 "schematic hope");
  - v0.6 :106, :362 and v0.7.1 :104, :378 ("working position");
  - v0.5 :152, :175, :129 (named exhaustion).

  #200 S7 dropped "with empty domain" from the index mirror; that is my error. Options: Claude's five strings; only the factual parts (empty domain in v0.3 and the index); leave them.
- **2.10 / 3.3 `q-law-of-r`'s second parent.**
  - v0.4 has no R ⊆ V*×V (#117).
  - v0.5 :85 makes R ⊆ V^τ × V conditional; v0.6 :198 makes it unconditional.
  - The edge sets h(`q-law-of-r`) = 0.5213, not 0.6859, and `a-hand-listed` and `a-kretschmann` = 0.2476, not 0.3258.

  Options: keep the edge and date it; keep `a-type-ii` as the only parent and move the constraint into the rationale. The second option changes three h values, which I would compute if chosen.
- **3.1 the "which objects can be observers?" fork.** David's notes (`docs/scratch/path-of-42.md:1`, #194) and IH §7 put "no privileged matter" as the accepted answer to a question under the root, with a rejected sibling. The pilot folds it into `a-root` (L0). Options: add the question and both answers above `q-observer-object`, with hold levels David's to set; list the fork as not mapped and take the clause out of the root; leave it.
- **3.4 `a-kretschmann` status.** Record: "neither is an adopted R" (:86); a "consistency witness for the schema without (a)" (:296). Options: an index gloss; a different parent (`q-realisation`); a non-IH marker.
- **3.5–3.9 merges** (`a-option-e`, `a-type-ii`, `a-everett-worlds`, `a-vtau`, `a-jet-direction`). Claude's facts check. Options for each: split into separate nodes; disclose the merge in the rationale; leave it. 3.6 and 3.9 bear on Q-D1 and a hold level.
- **3.13 decisions inside `a-alternation`.** v0.4 :84, :202 (proper time on segments; T1 per #161); v0.4 :94, v0.5 :94, :170 (direction, an open one-liner); v0.7.1 :211. Options: separate nodes; not-mapped entries; leave it.
- **3.15 #103's "Option E alone — too thin".** `papers/piecewise-geodesic-Ck-graph-ontology.md:34`; #128 :129; #134 banner. Neither #104 stamp names it. Options: an "Unclear record" line beside Option F; leave it.
- **4.2 open-node rule.**
  - Q-D1's existence side is `a-type-ii`'s R ≠ ∅ (v0.7.1 :410), and T3's "Rule jumps out" gives it up (:409).
  - T1's "Drop (A)" gives up `a-alternation` (:407).

  Options: Claude's sentence; a shorter pointer to the two nodes; leave it.
- **4.3 `a-m1`/`a-m2` pedigree and hazards.** v0.7.1 :153–159 (count pedigree); :317, :242 (referee hazard). Options: pedigree for both or for neither; add the hazard pointer; leave it.
- **4.4 `q-vertex-times` grounded in (M1).** #105 :72; C29 (:334); :196. Options: Claude's string; leave it.
- **4.8** status suffixes in titles. **4.9** T1 also names (C) (:407). **4.10** `a-m1`'s working-position half and its dating (1.2). Options: apply or leave, for each.

## 5. Separate part A: factual notes

- **A.4:** the lemma is stated "short of the throat" (#203; #209 :38, :44), and A.4 drops that proviso.
- Otherwise the checked facts hold:
  - 22 node files label v0.7.1 "(current draft)";
  - v0.8.1 :5 has "the prior prose";
  - v0.7.1 :385 has "loses its outward edges";
  - neither v0.8 nor v0.8.1 contains "Q-D";
  - #185's "fails a convention in force" (A.14(d)).
- Claude's "Unchecked" list says the viewer was not run. It has now been run, on `main` and on the patched folder (§6).

## 6. Verification of the APPLY list

- **Uniqueness.** `fixes224.py` (not committed) locates each OLD in its file on `main` at `332f7c5`. Each raw OLD below occurs exactly once.
- **Application.** All 56 were applied in order to a copy of `question-graph/`. They do not overlap, and each NEW then occurs once. Every yaml file parses.
- **Checks on the patched copy.**
  - The h script reports 0 mismatches.
  - The viewer reports 30 nodes, 6 versions, 2 warnings (the expected v0.4 pair) and 0 errors.
  - id, q, a, h, parents and status are identical before and after for all 30 nodes.
- **No downstream recomputation.** No string changes q, a, h, a parent or a hold level.
- **Line breaks.** Many OLDs span line breaks inside folded (`>-`) scalars. The raw OLD below keeps the file's newlines and two-space indentation. Each NEW is one line, which a folded scalar reads the same way.


## 7. APPLY list (for Ontology to apply mechanically)

Paths are relative to `public-papers/observer-space-framework/question-graph/`. Apply in the order given: replace the OLD between the `~~~~` fences, byte for byte, with the NEW. Each OLD occurs exactly once on `main` at `332f7c5`. Fence lines are not part of either string.

<!-- BEGIN APPLY LIST -->

### APPLY-01 · item 1.1 · APPLY-AMENDED · `a-option-e.yaml`

OLD:
~~~~text
Record note: the arm set changed across versions (the v0.4 cover says
  the arms are the out-star; v0.6 on counts the continue arm too, after #128).
~~~~

NEW:
~~~~text
Record note: the arms wording changed across versions, not B_R (v0.4 prose §4.2, v0.5 prose §1 and §4.2 and the v0.4 cover say "arms are the graph out-star", while their B_R = {[γ]} ∪ succ_R already counts the continue arm, a mismatch Claude #117 §2.4 flagged; from v0.6 on, the arms are "the elements of B_R", after #128 row 4).
~~~~

### APPLY-02 · item 1.1 · APPLY · `index.md`

OLD:
~~~~text
The arm set changed across versions: out-star only in the v0.4 cover, continue arm included from v0.6 (`a-option-e`).
~~~~

NEW:
~~~~text
The arms wording changed, not B_R: v0.4 and v0.5 prose (like the v0.4 cover) say "arms are the graph out-star" while their B_R already counts the continue arm; from v0.6 the arms are the elements of B_R, after #128 row 4 (`a-option-e`).
~~~~

### APPLY-03 · item 1.3 · APPLY-AMENDED · `a-option-f.yaml`

OLD:
~~~~text
Mapper's wording of #118's QUALIFY (truncated-jet language may stay as continue-arm
  housekeeping): only if a canonical comparison of jets across distinct lumps were found
  under which finite-k agreement is neither vacuous (k = 1) nor forbids curvature change
  (k of 2 or more).
~~~~

NEW:
~~~~text
Mapper's proposal; the record gives no reopen condition. #118's QUALIFY keeps truncated-jet language only as housekeeping (automatic on the continue arm; an exclusion of bare u-jumps, if kept, is a selection rule on R) and "does not save F as branching mechanism". Only if finite-k matching were shown to create a branching edge, or the CWS singleton were shown to depend on the order of matching after all (#117 §2.1, Claim A, accepted by #118: it rests on the shared oriented germ and geodesic uniqueness). A comparison of jets across distinct lumps would not do it: #118 finds no canonical identification there; at k = 1 matching is vacuous, and at k of 2 or more matching forces equal curvature "under any identification that makes the comparison defined".
~~~~

### APPLY-04 · item 1.4 · APPLY-AMENDED · `a-anchored-count.yaml`

OLD:
~~~~text
If the relevant R were shown to give only such trees, the v0.7
  sentence would hold there.
~~~~

NEW:
~~~~text
The record gives these as necessary conditions ("only where the tree's shape allows it", v0.7.1 §9), not as trees on which any anchored count keeps equal weight: on C13's tree, D-constant at depth 3, the fixed cut and the depth-1 anchor agree (1/12 each), but the count re-anchored two steps ahead gives 1/10 and 1/15; and the claim that depth 1 is the only cut with state-function weights is false on every tree (#169). Mapper's proposal: the exclusivity claim does not reopen; the "unless anchored" claim would hold only for an R whose trees make the named anchored count agree with the fixed-cut count.
~~~~

### APPLY-05 · item 1.4 · APPLY · `a-anchored-count.yaml`

OLD:
~~~~text
title: "Anchoring the count removes (M2)'s cut dependence at no cost (v0.7 wording)"
~~~~

NEW:
~~~~text
title: "Only the depth-1 anchor gives state-function weights, and anchoring frees the count of its note-6 cost (v0.7 §9 claims)"
~~~~

### APPLY-06 · item 1.4 · APPLY-AMENDED · `index.md`

OLD:
~~~~text
| rejected | method | Anchoring the count removes (M2)'s cut dependence at no cost (v0.7 wording) |
~~~~

NEW:
~~~~text
| rejected | method | Only the depth-1 anchor gives state-function weights, and anchoring frees the count of its note-6 cost (v0.7 §9 claims) |
~~~~

### APPLY-07 · item 1.4 · APPLY-AMENDED · `index.md`

OLD:
~~~~text
`a-anchored-count` (Anchoring the count removes (M2)'s cut dependence at no cost (v0.7 wording))
~~~~

NEW:
~~~~text
`a-anchored-count` (Only the depth-1 anchor gives state-function weights, and anchoring frees the count of its note-6 cost (v0.7 §9 claims))
~~~~

### APPLY-08 · item 1.6 · APPLY · `a-type-ii.yaml`

OLD:
~~~~text
Not derivable from locked data (Prop. 13,
  papers/type-ii-adopted.md).
~~~~

NEW:
~~~~text
Not derivable from locked data (v0.7.1 §4.2, citing Prop. 13 of papers/type-ii-adopted.md). From v0.4 the paper also carries a soft Prop. 13 (v0.7.1 §4.3): locked data "can determine off-curvelet stars", but "kinematics does not single out a dynamics", so which readout is a new physical choice; v0.8 B.2b logs Prop. 13 as "restated; one clause dropped".
~~~~

### APPLY-09 · item 1.7 · APPLY-AMENDED · `a-type-ii.yaml`

OLD:
~~~~text
and
  every later header says so.
~~~~

NEW:
~~~~text
and the headers from v0.5 on say so (v0.4's Status had said "relocation completed here by writing Option F composition", which Claude #117 disputed). In-house, papers/type-ii-adopted.md records "David adopted type-(ii) links as the working across-worlds motion" (added 2026-08-30, before v0.3; no signature cited). v0.3 sorts edges by bare lumps; v0.4's oriented split makes bare orientation changes type (ii), and from v0.6 they are "ordinary type-(ii) candidates".
~~~~

### APPLY-10 · item 1.8 · APPLY · `a-type-ii.yaml`

OLD:
~~~~text
abandoning type (ii) makes Paper 1's "the evolution is not unique" false.
~~~~

NEW:
~~~~text
abandoning type (ii) makes Paper 1's "the evolution is not unique" false under the CWS singleton, with the §5.2 convention that a history that ends and one that continues count as one evolution (v0.7.1 §10).
~~~~

### APPLY-11 · item 1.9 · APPLY-AMENDED · `a-jet-direction.yaml`

OLD:
~~~~text
The isotropy quotient was lost silently in v0.5 prose and
  restored in v0.6, after Claude Opus 5.5's HOLD on v0.5 (#128) and Geometry's ACCEPT of
  that item (#129).
~~~~

NEW:
~~~~text
v0.8 B.2a logs the oriented observer O^u as "restated". Two parts of the synopsis date from v0.6: v0.3 to v0.5 add the direction only "when branching is discussed", and v0.3 and v0.4 state the isotropy only as a qualifier ("up to the isotropy of the germ"), which Claude #105 noted does not define the class; the v0.4 and v0.5 outlines name the quotient, v0.5 prose drops the sentence silently, and v0.6 first defines O^u as the quotient class ("not optional"), after #128 and Geometry's ACCEPT (#129). "V is Paper 1's observer space" is v0.7.1's "reading, stated as such" (§2).
~~~~

### APPLY-12 · item 1.9 · APPLY · `index.md`

OLD:
~~~~text
The isotropy quotient was lost silently in v0.5 prose and restored in v0.6 (`a-jet-direction`).
~~~~

NEW:
~~~~text
The isotropy clause: v0.3 and v0.4 prose give it only as a qualifier ("up to the isotropy of the germ"; Claude #105: it qualifies "prefers" rather than defining the class), the v0.4 and v0.5 outlines name "u modulo germ isotropy", v0.5 prose drops it silently (#128), and v0.6 first defines O^u as the quotient class (`a-jet-direction`).
~~~~

### APPLY-13 · item 1.10 · APPLY · `index.md`

OLD:
~~~~text
The Everett world-counting firewall is found in the paper from v0.6. Its earlier source is Paper 1, and a first-appearance commit was not traced (`a-everett-worlds`).
~~~~

NEW:
~~~~text
The Everett world-counting firewall (AFLB 2008 outcome counting) enters the paper with the v0.6 outline (#130), from Literature #132 finding 2. A narrower firewall, that the objects are "not decoherence branches", is already in v0.3 §10 (carried from the v0.1.1 outline through v0.2.1); v0.4 keeps an arm-level line in §7 and a Deutsch–Wallace row, and v0.5 the row only. The source of both is Paper 1 (`a-everett-worlds`).
~~~~

### APPLY-14 · item 1.11 · APPLY-AMENDED · `a-gielen-wise.yaml`

OLD:
~~~~text
Rejected as the meaning of this programme's observer space, from v0.3 on (§2). Its
  points are 4-velocities, not analytic germs, and V is not their 7-manifold: "phrase
  collision only" (v0.7.1 §2, §10).
~~~~

NEW:
~~~~text
Rejected as the meaning of this programme's observer space. The record treats it as a homonym rather than a weighed option: Paper 1 calls it "a different use of the same English words"; the framework paper has "phrase collision only" in its v0.1.1 outline and in v0.2 and v0.2.1 §10, "same English phrase, different object" in §2 of v0.2 to v0.3, and "Phrase collision only" in its firewall table from v0.4; the only considered-and-killed move is in-house (below). Its points are 4-velocities, not analytic germs, and V is not their 7-manifold: "phrase collision only" (v0.7.1 §10).
~~~~

### APPLY-15 · item 1.12 · APPLY-AMENDED · `a-cws-branching.yaml`

OLD:
~~~~text
Rejected as the branching law in v0.3 ("CWS demoted", #98).
~~~~

NEW:
~~~~text
Proposed from the v0.1 outline through v0.2.1 prose as "a working type-(ii) motion law on observer space"; recast as type (i) by Claude's v0.2.1 HOLD and Geometry's motion recommendation, and rejected as the branching law in v0.3 ("CWS demoted", #98), which keeps it as "a coherent type-(i) package" (v0.3 §4.1): switching worlds leaves the path in Obs unchanged.
~~~~

### APPLY-16 · item 1.12 · APPLY · `a-cws-branching.yaml`

OLD:
~~~~text
Mapper's proposal, from the proposition's hypotheses: a path-germ equivalence other
  than (E1)/(E2) that a referee accepts, or a flaw in the CWS-singleton sketch, under
  which type-(i) motion gives two or more arms.
~~~~

NEW:
~~~~text
Mapper's proposal, from the proposition's sketch: a flaw in sketch steps 1–2, or an escape not among those the record lists as failing (Geometry's v0.2.1 motion recommendation, citing Claude's v0.2.1 HOLD §1.3), under which CWS gives two or more arms. A different equivalence on path germs cannot do it alone: by step 3 all allowed paths agree on an initial interval.
~~~~

### APPLY-17 · item 1.13 · APPLY · `a-option-f.yaml`

OLD:
~~~~text
Ontology's proposal (#103), adopted by David
~~~~

NEW:
~~~~text
Defined in Geometry's join menu as the "Hybrid default candidate", with Geometry's non-binding lean (#102); recommended by Ontology (#103); adopted by David
~~~~

### APPLY-18 · item 1.13 · APPLY-AMENDED · `a-option-f.yaml`

OLD:
~~~~text
and cannot create a branching edge; F is demoted to E.
~~~~

NEW:
~~~~text
and cannot create a branching edge (#128 row 1's wording, after #118); and the CWS singleton never rested on the order of matching (#117 §2.1, Claim A), so finite-k matching was not the HOLE escape. F is demoted to E.
~~~~

### APPLY-19 · item 1.14 · APPLY · `a-option-e.yaml`

OLD:
~~~~text
v0.5's header: the relocated HOLE is "cleared as a definition
  (B_R given R)".
~~~~

NEW:
~~~~text
v0.5's header, carrying #117's verdict on v0.4's composition (kept by #118): the relocated HOLE is "cleared as a definition (B_R given R); still relocated as a problem (law of R, costs)".
~~~~

### APPLY-20 · item 1.15 · APPLY · `a-vstar.yaml`

OLD:
~~~~text
From the record's own escape clause (v0.7.1 §5.1): an explicitly chosen, motivated
  discrete sub-ensemble of E_W (a grain on E_W), or an ensemble restriction that makes
  ending times discrete, which inextendibility alone does not do (C25).
~~~~

NEW:
~~~~text
From the record's own escape clause (v0.7.1 §5.1): an explicitly chosen discrete sub-ensemble of E_W, which the record calls a grain on E_W (an ensemble restriction that made ending times discrete is the same kind of grain, #118 Claim B; inextendibility alone does not do it, C25). Mapper's addition: the timing-vote objection would also need an answer, since v0.7.1 §2 calls choosing vertex times by which members die E-smuggling and says "It is not used".
~~~~

### APPLY-21 · item 1.15 · APPLY · `a-vstar.yaml`

OLD:
~~~~text
Superseded by V^τ (#134 banner, after Claude #128);
~~~~

NEW:
~~~~text
Replaced by V^τ as the public vertex engine in the v0.5 outline (#119, changelog (2)), confirmed by its Geometry panel (#120); banner on the in-house note in #134, after Claude #128 row 3;
~~~~

### APPLY-22 · item 1.16 · APPLY · `a-vtau.yaml`

OLD:
~~~~text
Introduced in v0.5 (#119, #123), then costed
~~~~

NEW:
~~~~text
Proposed by Claude #105 §3.1 and named in v0.4 §5.3 as a lock-side candidate for the hard gate's clause (2), while V* (§5.1) was the offered rule; made the public τ-slice in the v0.5 outline (#119, after #118; written V^τ in #123), then costed
~~~~

### APPLY-23 · item 1.17 · APPLY · `q-vertex-times.yaml`

OLD:
~~~~text
was added in v0.4 after Claude #105 §3.1.
~~~~

NEW:
~~~~text
was added in v0.4 after Claude #105 §3.1. The vertex question itself was first posed in-house as the "law of V*" (#102 §5 item 2; #103 §2.1), which #105 tied to §3.1's missing τ-slice.
~~~~

### APPLY-24 · item 1.17 · APPLY-AMENDED · `q-join-law.yaml`

OLD:
~~~~text
Claude #105 had said v0.3
~~~~

NEW:
~~~~text
Claude #105, written after #102 to #104 and reading Option F as its own §2 composition reading (C) written out (#105's lettering, not this graph's (A)–(C)), said v0.3
~~~~

### APPLY-25 · item 1.18 · APPLY-AMENDED · `a-alternation.yaml`

OLD:
~~~~text
made strict in v0.6
  (#130) after #128 row 2.
~~~~

NEW:
~~~~text
made explicitly strict in v0.6 (#130) after #128 row 2 (Claude #117 had read v0.4's "alternates" as already forbidding consecutive jumps and asked to "allow consecutive jumps or say why not"; v0.6 writes the positive-length clause and adds the flag). Claude #105's reading letters are its own, not this graph's (A)–(C).
~~~~

### APPLY-26 · item 1.19 · APPLY · `q-composition.yaml`

OLD:
~~~~text
because every
  Kretschmann target is itself a vertex,
~~~~

NEW:
~~~~text
since jumps carry no proper time (live on the worked rule, where every Kretschmann target is itself a vertex),
~~~~

### APPLY-27 · item 1.20 · APPLY · `a-kretschmann.yaml`

OLD:
~~~~text
First used by Claude in
  #117; carried into the public paper from v0.6 via #128 and #129 (orbit [10, 20]).
~~~~

NEW:
~~~~text
First used by Claude in #117, on the orbit [10, 20] with |B_R| = 3; named in the v0.5 outline (#119) as an arbitrary rule showing that "stated" alone is not enough, dropped from v0.5 prose (#128), and restored in v0.6 (#130) as the consistency witness after #128 and #129.
~~~~

### APPLY-28 · item 1.20 · APPLY-AMENDED · `a-kretschmann.yaml`

OLD:
~~~~text
As stated it
  models the schema without (a): typical histories are jump-dominated
~~~~

NEW:
~~~~text
As stated it models the schema without (a), since at each turning point of the instance one of its edges fails (a) (v0.7.1 §5.4, first bullet). Separately, under the rule as stated typical histories are jump-dominated
~~~~

### APPLY-29 · item 1.21 · APPLY-AMENDED · `a-target-avoid.yaml`

OLD:
~~~~text
jump targets are all turning points and hence vertices (v0.7.1 §4.2).
~~~~

NEW:
~~~~text
jump targets are all turning points and hence vertices (v0.7.1 §4.2). #129 names a second cost, not carried into the v0.6 outline or v0.7.1: it "adds a clause on R's target set"; and it conditions its verdict, "not recommended while the Kretschmann rule is the draft's consistency witness".
~~~~

### APPLY-30 · item 1.22 · APPLY · `q-law-of-r.yaml`

OLD:
~~~~text
The
  singleton-or-continuum dilemma lives here (soft Prop. 13): kinematics does not single
  out a dynamics, so a countable star is a new physical choice.
~~~~

NEW:
~~~~text
In the target direction the singleton-or-continuum dilemma lives here (v0.7.1 §4.3, after soft Prop. 13: kinematics does not single out a dynamics, so a countable star is a new physical choice). It "is escaped only by leaving R unspecified or by adding selection extras. That is a motivation problem, not a no-go theorem."
~~~~

### APPLY-31 · item 1.22 · APPLY · `q-law-of-r.yaml`

OLD:
~~~~text
This is the relocated HOLE's final address.
~~~~

NEW:
~~~~text
With its motivation and the choice of τ-slice, it is the relocated HOLE's final address (v0.7.1 header).
~~~~

### APPLY-32 · item 1.25 · APPLY · `q-realisation.yaml`

OLD:
~~~~text
saying (a) forbids curvature-changing jumps was false).
~~~~

NEW:
~~~~text
saying (a) forbids curvature-changing jumps was false); given the outline's arrival-tangent convention, Geometry #131 R1 showed (a) is lock-side (target in F(O), off the source's curvelet) and re-glossed (b) as "no realisation required" (v0.6 outline r2).
~~~~

### APPLY-33 · item 1.26 · APPLY-AMENDED · `a-root.yaml`

OLD:
~~~~text
The framework
  paper states the same object:
~~~~

NEW:
~~~~text
The framework paper opens with the same phrase, then names a particular object, the analytic jet with a time direction (a-jet-direction's answer, which the root leaves open). The phrase:
~~~~

### APPLY-34 · item 1.27 · APPLY · `a-world-analytic.yaml`

OLD:
~~~~text
were later
  dropped,
~~~~

NEW:
~~~~text
were dropped in v0.4 (absent from its §2; the phrases are v0.8 B.2b's excerpts of v0.3 §2),
~~~~

### APPLY-35 · item 4.1 · APPLY · `a-real-a.yaml`

OLD:
~~~~text
Costs recorded: the worked Kretschmann rule loses one edge at each
  turning point of the instance
~~~~

NEW:
~~~~text
Costs recorded: the forbidding above is itself the cost the record names ("the ones a measurement picture would want"; "The cost of (a) is real, but it is not 'no curvature change'", v0.7.1 §4.2); the worked Kretschmann rule loses one edge at each turning point of the instance
~~~~

### APPLY-36 · item 1.28+4.1 · APPLY-AMENDED · `a-real-a.yaml`

OLD:
~~~~text
with countably many completed histories (C33, v0.7 on);
~~~~

NEW:
~~~~text
with countably many completed histories (C33, v0.7 on; "12 to 14" is v0.7.1's exact law, P6–P8, where v0.7 had "13 or 14"); the record also gives that this restricted rule is stated, uniform and lock-side, with |B_R| = 2 at both turning points of the orbit [10, 20] for c = 0.1 and 0.01, so "not fatal" does not depend on dropping (a); it meets (J1) over late windows and fails it over early ones (jump share 1/2 over the decisions that occur), and fails (J2): one jump changes the orbit by O(1) (v0.7.1 §4.2, §7, §9 T3 row);
~~~~

### APPLY-37 · item 1.29 · APPLY · `a-real-a.yaml`

OLD:
~~~~text
not borne out by the census (#169).
~~~~

NEW:
~~~~text
unpinned: the narrowing is real, but the census does not show that branching stops once the jump length exceeds the orbit's width (#169).
~~~~

### APPLY-38 · item 1.30 · APPLY-AMENDED · `a-real-b.yaml`

OLD:
~~~~text
jump-dominated and fail both (J1) and (J2) (C17).
~~~~

NEW:
~~~~text
jump-dominated (C17, C34), and the rule fails both (J1) and (J2) (C17).
~~~~

### APPLY-39 · item 1.32 · APPLY · `q-observer-object.yaml`

OLD:
~~~~text
answers it first,
  in §2.
~~~~

NEW:
~~~~text
answers it first: stated in §1, defined in §2.
~~~~

### APPLY-40 · item 1.33 · APPLY · `a-option-e.yaml`

OLD:
~~~~text
through v0.7.1 (§4.2).
~~~~

NEW:
~~~~text
through v0.7.1 (§1, §4.2).
~~~~

### APPLY-41 · item 1.34 · APPLY · `a-hand-listed.yaml`

OLD:
~~~~text
The losing side of Claude Fable 5.1's HOLD on v0.3 (#105):
~~~~

NEW:
~~~~text
The loophole in v0.3's exit gate that Claude Fable 5.1's HOLD on v0.3 (#105) named:
~~~~

### APPLY-42 · item 1.35 · APPLY · `a-vstar.yaml`

OLD:
~~~~text
where members of the world ensemble stop being
  extendible,
~~~~

NEW:
~~~~text
where the hitchhiking ensemble splits: some members extend analytically through that time and some end there (v0.4 §5.1),
~~~~

### APPLY-43 · item 2.1 · APPLY-AMENDED · `versions/v0.6.yaml`

OLD:
~~~~text
The rest changed in open and rejected nodes:
~~~~

NEW:
~~~~text
Accepted nodes also changed: a-jet-direction (u again taken modulo germ isotropy; the direction always part of the object), a-type-ii (rewritten after #128 and Geometry #131 R2), a-vtau (a "candidate" slice, costed) and the arms wording of a-option-e ("the elements of B_R"). In open and rejected nodes:
~~~~

### APPLY-44 · item 2.1 · APPLY-AMENDED · `index.md`

OLD:
~~~~text
(#130). The rest changed in open and rejected nodes:
~~~~

NEW:
~~~~text
(#130). Accepted nodes also changed: a-jet-direction (u again taken modulo germ isotropy; the direction always part of the object), a-type-ii (rewritten after #128 and Geometry #131 R2), a-vtau (a "candidate" slice, costed) and the arms wording of a-option-e ("the elements of B_R"). In open and rejected nodes:
~~~~

### APPLY-45 · item 2.1 · APPLY-AMENDED · `index.md`

OLD:
~~~~text
each file's synopsis says what changed in open and rejected nodes.
~~~~

NEW:
~~~~text
each file's synopsis says what else changed.
~~~~

### APPLY-46 · item 2.2 · APPLY-AMENDED · `versions/v0.7.yaml`

OLD:
~~~~text
Changes in open nodes only:
~~~~

NEW:
~~~~text
Accepted nodes also changed: the record's status wording for (A) and for R ≠ ∅ (a-alternation, a-type-ii; see v0.7 §9 and §4.2), and a cost added to V^τ (C38; a-vtau). The rejected a-gielen-wise is corrected after Literature #158, and the sentences later rejected as a-anchored-count first appear (§9). In open nodes and open calls:
~~~~

### APPLY-47 · item 2.2 · APPLY-AMENDED · `versions/v0.7.yaml`

OLD:
~~~~text
T1-T3 and Q-D1-Q-D5 carried
  as open calls (#156).
~~~~

NEW:
~~~~text
T1-T3, Q-D1-Q-D5 and #139 (a)-(e) carried as open calls (#156).
~~~~

### APPLY-48 · item 2.2 · APPLY-AMENDED · `index.md`

OLD:
~~~~text
Same accepted selection. Changes in open nodes only:
~~~~

NEW:
~~~~text
Same accepted selection. Accepted nodes also changed: the record's status wording for (A) and for R ≠ ∅ (a-alternation, a-type-ii; see v0.7 §9 and §4.2), and a cost added to V^τ (C38; a-vtau). The rejected a-gielen-wise is corrected after Literature #158, and the sentences later rejected as a-anchored-count first appear (§9). In open nodes and open calls:
~~~~

### APPLY-49 · item 2.2 · APPLY-AMENDED · `index.md`

OLD:
~~~~text
T1-T3 and Q-D1-Q-D5 carried as open calls (#156).
~~~~

NEW:
~~~~text
T1-T3, Q-D1-Q-D5 and #139 (a)-(e) carried as open calls (#156).
~~~~

### APPLY-50 · item 2.8 · APPLY-AMENDED · `versions/v0.4.yaml`

OLD:
~~~~text
with neither strictness nor the arrival
  flag
~~~~

NEW:
~~~~text
without a written positive-length clause or the arrival flag
~~~~

### APPLY-51 · item 2.8 · APPLY-AMENDED · `index.md`

OLD:
~~~~text
with neither strictness nor the arrival flag
~~~~

NEW:
~~~~text
without a written positive-length clause or the arrival flag
~~~~

### APPLY-52 · item 3.2 · APPLY-AMENDED · `index.md`

OLD:
~~~~text
v0.3's rejected primaries (Direction Switching; instantaneous u-jumps), which were ruled before v0.3;
~~~~

NEW:
~~~~text
v0.3's rejected primaries (Direction Switching; instantaneous u-jumps), not recommended before v0.3 and rejected as primary in v0.3 §4.1 (u-jumps are ordinary type-(ii) candidates from v0.6; Direction Switching is not mentioned from v0.5; v0.8.1 B.2b logs the u-jumps as restated and Direction Switching as dropped); the other options of Geometry's join menu (#102): Option D, a C^k metric glued in one world, rejected as primary in v0.4 §4.2 (#104's stamp, in the join menu's letters: "Reject D as primary; A parked until gauge-as-space; B only inside C");
~~~~

### APPLY-53 · item 4.5 · APPLY · `a-vtau.yaml`

OLD:
~~~~text
One-variable analyticity makes them discrete per curvelet.
~~~~

NEW:
~~~~text
One-variable analyticity makes them discrete per curvelet, in its open maximal domain; accumulation at a singular endpoint remains possible (C8) and is handled by the no-Zeno clause, not by V^τ.
~~~~

### APPLY-54 · item 4.5 · APPLY · `a-cws-branching.yaml`

OLD:
~~~~text
Claude #105 judged the HOLE "cleared as an error" by this move.
~~~~

NEW:
~~~~text
Claude #105 judged the HOLE "cleared as an error, relocated honestly to the law of R, not fatal" by this move.
~~~~

### APPLY-55 · item 4.6 · APPLY · `a-kretschmann.yaml`

OLD:
~~~~text
The paper uses it as evidence for
  "not fatal", not as a candidate law.
~~~~

NEW:
~~~~text
The paper uses it as evidence for "not fatal" (a consistency witness for the schema without (a), §5.4), not as a candidate law; the Firewall says of it and its (a)-restriction "Neither is a controlled public example, and neither is an adopted R". The bar in force is "uniform, not a hand list" only because no rule meets the motivation clause (§5.4).
~~~~

### APPLY-56 · item 4.7 · APPLY · `a-world-analytic.yaml`

OLD:
~~~~text
Record note:
  v0.3's "topology may vary"
~~~~

NEW:
~~~~text
Open in the record: whether E_W should be restricted to inextendible or maximal members (v0.7.1 §2; §9 "Ensemble hygiene and inextendibility, if E_W becomes load-bearing"); §2's definitions are "the working ones for review". Record note: v0.3's "topology may vary"
~~~~

<!-- END APPLY LIST -->

## 8. Tallies

- **Findings (71: 1.1–1.35, 2.1–2.10, 3.1–3.16, 4.1–4.10):** CONFIRM 38, QUALIFY 7, REJECT 0, FOR DAVID 26 (whole items). Four ruled items also have a FOR DAVID part: 1.7(b), 1.9 (T1-quote string), 2.1 and 2.2 (content clauses).
- **Strings:** 56 in the APPLY list: APPLY 29, APPLY-AMENDED 27, DECLINE 0. Of Claude's 67 OLD/NEW pairs, 19 sit in FOR DAVID items and are not ruled. 1.28 and 4.1's second string are merged into one entry. The list also adds 9 mirror or supplied strings: 1.4 index ×2, 2.1 index ×2, 2.2 ×3, and 2.8 ×2.
- **APPLY strings by file:** `index.md` 11; `a-cws-branching.yaml` 3; `a-kretschmann.yaml` 3; `a-option-e.yaml` 3; `a-option-f.yaml` 3; `a-real-a.yaml` 3; `a-type-ii.yaml` 3; `a-vstar.yaml` 3; `a-anchored-count.yaml` 2; `a-vtau.yaml` 2; `a-world-analytic.yaml` 2; `q-law-of-r.yaml` 2; `versions/v0.7.yaml` 2; `a-alternation.yaml` 1; `a-gielen-wise.yaml` 1; `a-hand-listed.yaml` 1; `a-jet-direction.yaml` 1; `a-real-b.yaml` 1; `a-root.yaml` 1; `a-target-avoid.yaml` 1; `q-composition.yaml` 1; `q-join-law.yaml` 1; `q-observer-object.yaml` 1; `q-realisation.yaml` 1; `q-vertex-times.yaml` 1; `versions/v0.4.yaml` 1; `versions/v0.6.yaml` 1.
- **h:** unchanged everywhere. No downstream recomputation was needed.
