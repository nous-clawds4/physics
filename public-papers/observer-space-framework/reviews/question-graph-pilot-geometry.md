# Question-graph pilot (#199): Geometry math and selection check

Author: Geometry. Review record for physics#199 (Ontology, "Question-graph pilot (Path of 42)"). It records; it rules on nothing in the graph and chooses no law.

**Commit read:** `4e6d0783afbd06ae375ca4f638f810b21b4246b4` (branch `question-graph-pilot`, base `main` at `747f81c`). Sources: the 30 node files, `index.md`, `graph.yaml` and `versions/*.yaml` at that commit; `versions/v0.3-prose.md` to `v0.8-prose.md` on main; the Claude and Geometry reviews (#105, #117, #118, #128, #129, #168, #169); the viewer README and `build/build.mjs` (path-of-42-viewer `ed86851`); IH `docs/path-of-42.md` at `6f02238` (§§2, 4, 9).

## Verdict: PASS with fixes

The h arithmetic is right at every node. Every answer's status matches the record, (M1)/(M2) and the law of R are open, nothing is rated as adopted that was not, and no forbidden term appears. Three things need fixing:
- **Selections:** v0.4 and v0.5 select `a-alternation`, which they did not have.
- **Hold cap:** one violation of the hold-level cap.
- **Gap:** one missing gap entry.

There are 13 OLD/NEW fixes: 9 on selections (5 in version files, 4 mirrored in `index.md`), 3 on the hold cap and 1 on gaps. None changes any h. Rerunning the viewer build on the fixed copy gives the same 30 nodes and 6 versions, with the same 2 expected warnings and 0 errors.

## 1. Status against the record

All 21 answers agree with what each version did.
- **Accepted:** root, jet with time direction, world W = (M, p), type (ii) (all from v0.3, §2 and Definition 7), Option E residue and V^τ (from v0.5), and (A) (from v0.6, §4.2 items 2 and 7).
- **Rejected:**
  - Gielen–Wise, from v0.3 §2 ("not Gielen and Wise's 7-manifold").
  - CWS as the branching law, from v0.3.
  - Everett worlds, per Paper 1.
  - The hand-listed digraph, from v0.4's firewall.
  - Option F and V*, from v0.5: "Not Option F as a branching mechanism", and extend-versus-not listed under does-not-claim.
  - (B) and (C), from v0.6.
  - The anchoring sentence, from v0.7.1 (P1–P5).
- **Open:** (a) and (b), (M1) and (M2) (v0.7.1 §9: "This paper does not choose between them"), and the Kretschmann rule ("It adopts no R").

Two notes, neither needing a fix:
- v0.7.1 §5.1 calls V^τ a "candidate engine". "Accepted" still holds, because composition item 1 declares $R\subseteq V^\tau\times V$ and the node says "candidate, not a theorem".
- v0.4 offers V* with "may be selected". "Accepted at the time" matches #106's "adopt V* with caveats".

## 2. q and a ratings

There are no clear misratings. The ratings apply the index's three-level scale consistently:
- Siblings share q (0.8 under `q-join-law`, 0.95 elsewhere).
- Both sides of each open call get a = 0.5.
- The working, abandonable nodes get a = 0.8: type (ii), Option E, V^τ and (A).
- Only the object and the world get a = 0.95.

Two placement notes, not ratings:
- `a-anchored-count` is a rejected claim about (M2), not an answer to "How are the arms weighted?".
- `a-hand-listed` answers "what meets the exit gate", not "What is the law of R?".

Either could make way for a node from §5.

## 3. h = h(weakest parent) · q · a

`hcheck.py` (sha256 `a82875dbd73f632175506a8c7d653c892f42ff0bdaa57c5049d7502085dd6b0a`) recomputes h from the YAML:
- **Rules:** a root has h = 1 and no q or a; an answer has h = min over parents of h, times q·a; a question has h = min over parents of h.
- **Checks against the files:**
  - It compares exact h with the chain rounded at every node to 4 dp.
  - It compares both with each file's `# h` comment and with the `index.md` table.
  - It checks that each comment names the weakest parent.

Results:
- **0 mismatches in 30 nodes.** Exact and rounded chains agree to 4 dp everywhere; for example, `a-hand-listed` is 0.247610 exact, 0.2476 rounded.
- **One node has two parents:** `q-law-of-r` (`a-type-ii` 0.6859, `a-vtau` 0.5213) correctly takes 0.5213.
- **Monotone:** no child has a higher h than any of its parents.
- **Viewer agrees:** `build.mjs` gives the same h at all 30 nodes.
- **Hold levels:** `hcheck.py` also checks IH §2's cap on L-levels, which the build does not. It found one violation: `a-jet-direction` (L1) sits under `q-observer-object` (L3). Fixes H1–H3 raise the question to L1 as a proposal pending David's signature. The other way to clear it is to lower `a-jet-direction` to L3, but that would contradict v0.7.1 treating the object as a lock.

## 4. `selects` lists

v0.3, v0.7 and v0.7.1 are right. v0.4's Option F and V* are right, with the 2 warnings the index expects.

**`a-alternation` in v0.4 and v0.5 is wrong.** The node is "(A) Strict alternation, with an arrival flag": a positive-length segment after every jump, and the state (O^u, a). Neither version had it:
- v0.4 §4.2 item 2 and v0.5 §4.2 item 2 say only "A history alternates type-(i) curvelet segments and type-(ii) jumps". They have no strictness clause and no arrival flag.
- Claude #128 row 2 held v0.5 because clause (2) held "per segment, not per history". It noted that if strict alternation were meant, $B_R$ at a jump target would count arms the history cannot take.
- Strict alternation (item 2) and the arrival flag (item 7) first appear in v0.6.

So v0.6 adds a node to the selection; its synopsis's "Same accepted selection as v0.5" is wrong. Fixes S1–S9 correct this. **Ontology may wish to update the PR body's "these four selections are identical" line** (it is not a file, so no OLD/NEW is given).

**EPP1 in v0.3 to v0.5 (disclosure only).** v0.4 and v0.5 adopt EPP1 as a "named postulate", and v0.3 as a "working postulate for narrative". Not selecting `a-m1` there keeps (M1)/(M2) open and puts no lean in the viewer, which is right. It differs from the v0.4 Option F / V* convention, though, so fixes S2, S4, S7 and S8 say so. `a-m1` stays open and unselected everywhere.

## 5. Coverage

**Present:**
- Gielen–Wise (rejected).
- V* versus Option F (both rejected, on separate questions).
- (a)/(b) (open).
- Jump/segment alternation ((A) accepted; (B) and (C) rejected).
- Every Claude HOLD in range: v0.2.1, #105, #117, #128 and #168 (v0.6 #154 and v0.7.1 were PASS).
- (M1)/(M2), **open**.
- The law of R, **open**: a question with only open or rejected answers.

**Named in gaps, not mapped:** EPP2 and (J1)/(J2).

**Missing:** circularity. The v0.7.1 §8 circularity wall is not mentioned anywhere; `a-real-a`'s "circularisation" is a different thing. Fix G1 adds it to the gaps.

**Optional, for a later round (not required for PASS):** within 30 nodes, `a-epp2` (rejected foil under `q-measure`) could replace `a-anchored-count`, whose content is already in `a-m2` and the v0.7.1 synopsis. A (J1)/(J2) question under `q-law-of-r` could replace `a-hand-listed`.

**Standing constraints:**
- No node or file uses the Born rule, $|a|^2$ or $1/N$.
- No T1–T3, Q-D or #139 (a)–(e) call is decided.
- No law is chosen.

## 6. Fixes (OLD occurs once in its file at `4e6d078`; apply in order)

**S1** (selection): `question-graph/versions/v0.4.yaml`

```text
OLD:
selects: [a-root, a-jet-direction, a-world-analytic, a-type-ii, a-option-f, a-vstar, a-alternation]

NEW:
selects: [a-root, a-jet-direction, a-world-analytic, a-type-ii, a-option-f, a-vstar]
```

**S2** (selection): `question-graph/versions/v0.4.yaml`

```text
OLD:
status is current and the selection historical. The composition (alternation) is
  written here, without the arrival flag. Realisation

NEW:
status is current and the selection historical. The composition is written here as
  plain alternation ("a history alternates"), with neither strictness nor the arrival
  flag, so a-alternation, which is (A) as made strict in v0.6, is not selected (Claude
  #128 row 2). EPP1 is a named postulate with empty domain; a-m1 is not selected, since
  (M1)/(M2) is framed as an undecided call only from v0.6 and stays open. Realisation
```

**S3** (selection): `question-graph/versions/v0.5.yaml`

```text
OLD:
selects: [a-root, a-jet-direction, a-world-analytic, a-type-ii, a-option-e, a-vtau, a-alternation]

NEW:
selects: [a-root, a-jet-direction, a-world-analytic, a-type-ii, a-option-e, a-vtau]
```

**S4** (selection): `question-graph/versions/v0.5.yaml`

```text
OLD:
table, later corrected (#128, #129). Source:

NEW:
table, later corrected (#128, #129). The composition is still plain alternation with
  no arrival flag, so a-alternation is not selected: Claude #128 row 2 found clause (2)
  held per segment, not per history. EPP1 is a named postulate with empty domain and a
  path-count alternative listed as open; a-m1 is not selected ((M1)/(M2) is framed only
  from v0.6 and stays open). Source:
```

**S5** (selection): `question-graph/versions/v0.6.yaml`

```text
OLD:
Same accepted selection as v0.5. What changed sits in open and rejected nodes: strict
  alternation with the arrival flag, (B) and (C) rejected;

NEW:
Adds a-alternation to v0.5's selection: strict alternation with the arrival flag
  (#130). The rest changed in open and rejected nodes: (B) and (C) rejected;
```

**S6** (selection (index mirror)): `question-graph/index.md`

```text
OLD:
`a-option-f`, `a-vstar`, `a-alternation`. Selects Option F and V*

NEW:
`a-option-f`, `a-vstar`. Selects Option F and V*
```

**S7** (selection (index mirror)): `question-graph/index.md`

```text
OLD:
The composition (alternation) is written here, without the arrival flag.

NEW:
The composition is written here as plain alternation, with neither strictness nor the arrival flag, so `a-alternation` ((A), made strict in v0.6) is not selected (Claude #128 row 2). EPP1 is a named postulate; `a-m1` is not selected, since (M1)/(M2) is framed as an undecided call only from v0.6 and stays open.
```

**S8** (selection (index mirror)): `question-graph/index.md`

```text
OLD:
`a-option-e`, `a-vtau`, `a-alternation`. Option E residue and V^τ replace Option F and V* (#117, #118). (a)/(b) gets a cost table, later corrected (#128, #129).

NEW:
`a-option-e`, `a-vtau`. Option E residue and V^τ replace Option F and V* (#117, #118). (a)/(b) gets a cost table, later corrected (#128, #129). Composition and EPP1 as in v0.4, so neither `a-alternation` nor `a-m1` is selected.
```

**S9** (selection (index mirror)): `question-graph/index.md`

```text
OLD:
Same accepted selection as v0.5. What changed sits in open and rejected nodes: strict alternation with the arrival flag, (B) and (C) rejected;

NEW:
Adds `a-alternation` to v0.5's selection: strict alternation with the arrival flag (#130). The rest changed in open and rejected nodes: (B) and (C) rejected;
```

**H1** (hold cap): `question-graph/q-observer-object.yaml`

```text
OLD:
hold: L3   # weakly held (disclosed)

NEW:
hold: L1   # proposal, pending David's signature (not weaker than its child a-jet-direction, L1; IH §2)
```

**H2** (hold cap (index mirror)): `question-graph/index.md`

```text
OLD:
Holds: the root is L0 and Paper 1's object is L1 (both proposals, pending David's signature);

NEW:
Holds: the root is L0; Paper 1's object (`a-jet-direction`) and the question it answers (`q-observer-object`) are L1, since a child is never held more strongly than its parent (IH §2) (all proposals, pending David's signature);
```

**H3** (hold cap (index mirror)): `question-graph/index.md`

```text
OLD:
no node's h exceeds its weakest parent's. Violations: none.

NEW:
no node's h exceeds its weakest parent's. Violations: none. Hold levels obey the same cap (IH §2): no node's L-level is stronger than any parent's.
```

**G1** (gap): `question-graph/index.md`

```text
OLD:
EPP2 as a foil and the product-ansatz Hope;

NEW:
EPP2 as a foil and the product-ansatz Hope; the circularity wall (v0.7.1 §8: a tree drawn by hand on (V, R) to match a target weight is Paper 1's trivial scheme, and "weights forced, not assumed" would need a law of R, a typicality rule and work on circularity);
```

## Pins

- `/workspace/g199/hcheck.py`: `a82875dbd73f632175506a8c7d653c892f42ff0bdaa57c5049d7502085dd6b0a` (h, hold cap, selections).
- `/workspace/g199/fixes.py`: `f7055411ac9486dcd330343a13677196c858166fd0faa5cd5380ded22307a498`. Applies S1–G1 to a copy and asserts each OLD occurs once.
- Viewer build after the fixes: 30 nodes, 6 versions, 2 warnings (v0.4's F and V*), 0 errors. h is unchanged at all 30 nodes.
