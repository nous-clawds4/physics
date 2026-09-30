# Question graph (Path of 42 pilot): observer-space framework v0.3 to v0.7.1

**Status: pilot, do not merge without the checks below.** This folder retro-maps the decisions behind the framework paper's versions v0.3 to v0.7.1 (`../versions/`) onto a question graph. It records; it does not decide. **Every rating (q, a) and every hold level above "weakly held" is a proposal, pending David's signature.** No paper text, essay or version file is edited; only this folder is new.

## Method (brief)

Sources used: David's notes, [`docs/scratch/path-of-42.md`](../../../docs/scratch/path-of-42.md) (physics#194; the same text as the paragraph beginning "Probably move the following paragraph elsewhere" in `wds4/physics`, *Statement of the Problem* v0.5 at `047ba16`; removed there at `69f4042`); the Chief of Staff's IH method doc, [infinite-harness `docs/path-of-42.md`](https://github.com/nous-clawds4/infinite-harness/blob/6f02238c3aab7f9bcc8cf83abcebc6c98dc6d094/docs/path-of-42.md) (infinite-harness#7, commit `6f02238`), §§1–5, 8 and 9, with levels from [`docs/hold-axis.md`](https://github.com/nous-clawds4/infinite-harness/blob/main/docs/hold-axis.md) §3; and the viewer's data format, [path-of-42-viewer README](https://github.com/nous-clawds4/path-of-42-viewer#data-format).

- Research is a directed acyclic graph of **question** and **answer** nodes (IH §1). Answers are **accepted**, **rejected** or **open**, and carry one tag: definition, math-tool, method or physical-hypothesis.
- **Rejected answers are kept**, with why and a reopen-if condition (IH §3). Read together, the rejected answers are the companion document of rejected options for each layer (David's earlier idea); see "Rejected options by layer" below.
- **A child is never held more strongly than its weakest parent** (IH §2).
- **A paper version is a consistent selection** of accepted answers, one per question it depends on; parallel branches are allowed (IH §4).
- **Hold number** (IH §9, proposal): h(root) = 1; for an answer, h = h(parent) × q × a; a question carries its parent's h; with several parents the weakest is used (viewer README).

## Rating scale (proposal, pending David's signature)

| Level | Value | q: is the question worth asking? | a: is this the best answer? |
|---|---|---|---|
| high | 0.95 | clearly needed by the parent | the record runs with it and has not found a rival |
| medium | 0.8 | needed, but the record reframed it | working, abandonable, or with a named cost |
| low | 0.5 | — (not used for q here) | rejected, or one side of an undecided call |

The mapping is IH §9's example, not a fixed one. q belongs to the question but is stored on each answer (viewer format), so siblings share it. Both sides of every open call get the same a, so the numbers do not lean. Holds: the root is L0; Paper 1's object (`a-jet-direction`) and the question it answers (`q-observer-object`) are L1, since a child is never held more strongly than its parent (IH §2) (all proposals, pending David's signature); every other node is L3, weakly held (disclosed).

**Do the numbers feel right? Two things to look at, recorded, not ruled on.** (1) With three levels, rejected and open answers get the same a, so `a-vstar` (rejected) and `a-m1` (open) both sit at h = 0.3258. (2) A rejected option high in the graph outranks accepted options lower down: `a-gielen-wise` (rejected) has h = 0.4750, above `a-option-e` (accepted, 0.4390). Either may call for a lower value for rejected answers, or for not showing h on them. That is David's call.

## Nodes

9 questions and 21 answers: 7 accepted, 9 rejected, 5 open (30 nodes). The q / a column is proposal, pending David's signature; h is recomputed from it.

| id | type | status | tag | title | parents | q / a | h |
|---|---|---|---|---|---|---|---|
| [`a-root`](a-root.yaml) | answer | accepted | method | Root: the observer is a physical object inside the theory | (root) | — | 1.0000 |
| [`q-observer-object`](q-observer-object.yaml) | question | — | — | What physical object is an observer, and what is observer space? | `a-root` | — | 1.0000 |
| [`a-jet-direction`](a-jet-direction.yaml) | answer | accepted | definition | An analytic metric germ with a future time direction (V = oriented observers) | `q-observer-object` | high / high | 0.9025 |
| [`a-gielen-wise`](a-gielen-wise.yaml) | answer | rejected | definition | Observer space as Gielen–Wise's space of observer 4-velocities | `q-observer-object` | high / low | 0.4750 |
| [`q-what-is-a-world`](q-what-is-a-world.yaml) | question | — | — | What is a world, relative to an observer? | `a-jet-direction` | — | 0.9025 |
| [`a-world-analytic`](a-world-analytic.yaml) | answer | accepted | definition | A world is a pointed analytic spacetime W = (M, p) | `q-what-is-a-world` | high / high | 0.8145 |
| [`a-everett-worlds`](a-everett-worlds.yaml) | answer | rejected | definition | Worlds as Everett worlds (branches of a quantum state), counted as outcomes | `q-what-is-a-world` | high / low | 0.4287 |
| [`q-branching`](q-branching.yaml) | question | — | — | How can one observer have more than one future? | `a-jet-direction` | — | 0.9025 |
| [`a-cws-branching`](a-cws-branching.yaml) | answer | rejected | math-tool | Continuous World Switching (type-(i) hitchhiking) as the branching law | `q-branching` | high / low | 0.4287 |
| [`a-type-ii`](a-type-ii.yaml) | answer | accepted | math-tool | Type-(ii) edges: a transition relation R on V, with R nonempty (working, abandonable) | `q-branching` | high / medium | 0.6859 |
| [`q-join-law`](q-join-law.yaml) | question | — | — | What joins a geodesic segment to a type-(ii) edge (the join law)? | `a-type-ii` | — | 0.6859 |
| [`a-option-f`](a-option-f.yaml) | answer | rejected | math-tool | Option F: finite-k truncated-jet matching at joins, plus graph incidence | `q-join-law` | medium / low | 0.2744 |
| [`a-option-e`](a-option-e.yaml) | answer | accepted | math-tool | Option E residue: graph joins with discontinuous type-(ii) jumps | `q-join-law` | medium / medium | 0.4390 |
| [`q-vertex-times`](q-vertex-times.yaml) | question | — | — | When may a history branch (which germs are vertices)? | `a-type-ii` | — | 0.6859 |
| [`a-vstar`](a-vstar.yaml) | answer | rejected | math-tool | V*: vertex times where some compatible world ends (extend-versus-not) | `q-vertex-times` | high / low | 0.3258 |
| [`a-vtau`](a-vtau.yaml) | answer | accepted | math-tool | V^τ: a lock-side slice along each curvelet | `q-vertex-times` | high / medium | 0.5213 |
| [`q-composition`](q-composition.yaml) | question | — | — | How do segments and jumps compose along a history? | `a-type-ii` | — | 0.6859 |
| [`a-alternation`](a-alternation.yaml) | answer | accepted | definition | (A) Strict alternation, with an arrival flag | `q-composition` | high / medium | 0.5213 |
| [`a-jump-bound`](a-jump-bound.yaml) | answer | rejected | definition | (B) Consecutive jumps, counted under a bound N | `q-composition` | high / low | 0.3258 |
| [`a-target-avoid`](a-target-avoid.yaml) | answer | rejected | definition | (C) Target avoidance: no jump lands on a vertex | `q-composition` | high / low | 0.3258 |
| [`q-realisation`](q-realisation.yaml) | question | — | — | Must each type-(ii) edge be realised in some spacetime? ((a)/(b)) | `a-type-ii` | — | 0.6859 |
| [`a-real-a`](a-real-a.yaml) | answer | open | definition | (a) Realised edges | `q-realisation` | high / low | 0.3258 |
| [`a-real-b`](a-real-b.yaml) | answer | open | definition | (b) No realisation required | `q-realisation` | high / low | 0.3258 |
| [`q-measure`](q-measure.yaml) | question | — | — | How are the arms weighted? ((M1)/(M2); also T2 = Q-D3 = #139 (b)) | `a-type-ii` | — | 0.6859 |
| [`a-m1`](a-m1.yaml) | answer | open | method | (M1) Per-vertex equal weight (EPP1) | `q-measure` | high / low | 0.3258 |
| [`a-m2`](a-m2.yaml) | answer | open | method | (M2) Paper 1's count of distinct evolutions at a named cut | `q-measure` | high / low | 0.3258 |
| [`a-anchored-count`](a-anchored-count.yaml) | answer | rejected | method | Anchoring the count removes (M2)'s cut dependence at no cost (v0.7 wording) | `q-measure` | high / low | 0.3258 |
| [`q-law-of-r`](q-law-of-r.yaml) | question | — | — | What is the law of R? | `a-type-ii`, `a-vtau` | — | 0.5213 |
| [`a-hand-listed`](a-hand-listed.yaml) | answer | rejected | method | A hand-listed digraph as the controlled example | `q-law-of-r` | high / low | 0.2476 |
| [`a-kretschmann`](a-kretschmann.yaml) | answer | open | math-tool | The Kretschmann rule on a bound Schwarzschild orbit (unadopted worked model) | `q-law-of-r` | high / low | 0.2476 |

**Monotonicity:** checked with the viewer build (`build/build.mjs`) and a separate script: no node's h exceeds its weakest parent's. Violations: none. Hold levels obey the same cap (IH §2): no node's L-level is stronger than any parent's. `q-law-of-r` has two parents (`a-type-ii`, 0.6859; `a-vtau`, 0.5213) and takes the weaker.

**Open-node rule.** No accepted node stands for (M1)/(M2), T1–T3, Q-D1–Q-D5, #139 (a)–(e) or the law of R. (M1) and (M2) are open answers; the law of R is a question with only open or rejected answers; the others are named inside nodes and in the gaps and are marked open there. Where to find them: T1–T3 in *Mathematical Foundations* v0.3 (physics#149) and the v0.7.1 §9 calls table; Q-D1–Q-D5 in `public-essays/mathematical-foundations/reviews/v0.1-ontology.md` (physics#142); #139 (a)–(e) in the body of physics#139; the v0.7.1 header and §9 calls table map them (Q-D3 = T2, Q-D5 = T1, (a) = T3 with its proper-time part under T1, (b) = T2 and (M1)/(M2)).

## Paper versions (selections)

Each file in `versions/` lists the accepted answers the version rests on. Open calls have no selected answer, so they do not appear in `selects`; each file's synopsis says what changed in open and rejected nodes.

- **v0.3** (`versions/v0.3-prose.md`, physics#98): `a-root`, `a-jet-direction`, `a-world-analytic`, `a-type-ii`. Type-(ii) R introduced; CWS demoted to the type-(i) null baseline. No join law, vertex engine or composition is stated yet (Claude #105). Open: the law of R. Realisation of edges is not yet posed as a question (v0.3 has a compatibility relation, later identified with (a)); the measure is run as EPP1 on discrete arms. Rejected at this version: CWS as the branching law.
- **v0.4** (`versions/v0.4-prose.md`, physics#112): `a-root`, `a-jet-direction`, `a-world-analytic`, `a-type-ii`, `a-option-f`, `a-vstar`. Selects Option F and V*, both accepted at the time and rejected since (#118, #134), so the viewer flags these two selections; that flag is expected in a retro-map, where status is current and the selection historical. The composition is written here as plain alternation, with neither strictness nor the arrival flag, so `a-alternation` ((A), made strict in v0.6) is not selected (Claude #128 row 2). EPP1 is a named postulate; `a-m1` is not selected, since (M1)/(M2) is framed as an undecided call only from v0.6 and stays open. Realisation of edges named as an open one-liner. Rejected at this version: a hand-listed digraph as the controlled example (#105).
- **v0.5** (`versions/v0.5-prose.md`, physics#123): `a-root`, `a-jet-direction`, `a-world-analytic`, `a-type-ii`, `a-option-e`, `a-vtau`. Option E residue and V^τ replace Option F and V* (#117, #118). (a)/(b) gets a cost table, later corrected (#128, #129). Composition and EPP1 as in v0.4, so neither `a-alternation` nor `a-m1` is selected.
- **v0.6** (`versions/v0.6-prose.md`, physics#135): `a-root`, `a-jet-direction`, `a-world-analytic`, `a-type-ii`, `a-option-e`, `a-vtau`, `a-alternation`. Adds `a-alternation` to v0.5's selection: strict alternation with the arrival flag (#130). The rest changed in open and rejected nodes: (B) and (C) rejected; (a)/(b) re-costed and lock-side; (M1)/(M2) framed as an undecided call; the Kretschmann model carried as an unadopted example (#128, #129, #130).
- **v0.7** (`versions/v0.7-prose.md`, physics#160): `a-root`, `a-jet-direction`, `a-world-analytic`, `a-type-ii`, `a-option-e`, `a-vtau`, `a-alternation`. Same accepted selection. Changes in open nodes only: the (a)-restriction's transient branching (C33), the (M1)/(M2) cost lines made symmetric, T1-T3 and Q-D1-Q-D5 carried as open calls (#156).
- **v0.7.1** (`versions/v0.7.1-prose.md`, physics#170): `a-root`, `a-jet-direction`, `a-world-analytic`, `a-type-ii`, `a-option-e`, `a-vtau`, `a-alternation`. Same accepted selection. Patch after Claude #168 and Geometry #169: the v0.7 claim that anchoring removes cut dependence at no cost is rejected (a-anchored-count).

Skipped: none of the six requested versions is missing (v0.7 and v0.7.1 both exist). The mapped file is the prose for each version. v0.3, v0.4, v0.5, v0.6 and v0.7 also have outlines, which are not mapped separately. v0.1 to v0.2.1 and v0.8 are outside the range.

## Rejected options by layer (the companion document)

- **What physical object is an observer, and what is observer space?** (`q-observer-object`): `a-gielen-wise` (Observer space as Gielen–Wise's space of observer 4-velocities).
- **What is a world, relative to an observer?** (`q-what-is-a-world`): `a-everett-worlds` (Worlds as Everett worlds (branches of a quantum state), counted as outcomes).
- **How can one observer have more than one future?** (`q-branching`): `a-cws-branching` (Continuous World Switching (type-(i) hitchhiking) as the branching law).
- **What joins a geodesic segment to a type-(ii) edge (the join law)?** (`q-join-law`): `a-option-f` (Option F: finite-k truncated-jet matching at joins, plus graph incidence).
- **When may a history branch (which germs are vertices)?** (`q-vertex-times`): `a-vstar` (V*: vertex times where some compatible world ends (extend-versus-not)).
- **How do segments and jumps compose along a history?** (`q-composition`): `a-jump-bound` ((B) Consecutive jumps, counted under a bound N); `a-target-avoid` ((C) Target avoidance: no jump lands on a vertex).
- **How are the arms weighted? ((M1)/(M2); also T2 = Q-D3 = #139 (b))** (`q-measure`): `a-anchored-count` (Anchoring the count removes (M2)'s cut dependence at no cost (v0.7 wording)).
- **What is the law of R?** (`q-law-of-r`): `a-hand-listed` (A hand-listed digraph as the controlled example).

## Gaps and unclear record

**Open calls not given their own node (all open; none decided here).**
- **T3 = #139 (a):** the essay's no-teleport intuition versus this paper's jumps. Bears on `q-branching` and `a-type-ii`. v0.7.1 §9 carries it with costs on both sides, plus the note on how the (a) transient bears on it (not resolved).
- **T1 = Q-D5:** the arrival flag versus observer-only locality. Carried in `a-alternation` and `q-composition`, not as its own node.
- **Q-D1** (existence or permission), **Q-D2** ("next": discrete or continuous), **Q-D4** (which Bell premise), **#139 (c)** (complete representation versus Paper 1's no-reconstruction lock) and **#139 (d)** (the essay's "almost trivially" versus the paper's Hope). Each has two sides with costs in the v0.7.1 §9 table.
- **#139 (e):** the essay's two long-range derivation goals (a probability rule for detector outcomes, and the gravitational field equations), kept as goals, not claims. Described neutrally here because the record's own words for them are not used in this graph.

**Parts of the record not mapped (kept out to stay within 20–30 nodes).** EPP2 as a foil and the product-ansatz Hope; the circularity wall (v0.7.1 §8: a tree drawn by hand on (V, R) to match a target weight is Paper 1's trivial scheme, and "weights forced, not assumed" would need a law of R, a typicality rule and work on circularity); the co-existence reading of the weight (working postulate) versus the chance reading (defined only); the hard gate, the no-Zeno clause and the open Zeno-mass convention; (J1)/(J2); the throat convention; backward-only pairs; exhaustion for countable stars; ensemble hygiene; the Obs-local Bell-compatibility Hope; the version firewalls; the maximal-entropy random walk hazard for (M2) (described neutrally in `a-m2`, since the record's name for it uses a word this graph avoids); v0.3's rejected primaries (Direction Switching; instantaneous u-jumps), which were ruled before v0.3; v0.8 and the law-of-R scoping work (#177–#189), which come after v0.7.1.

**Unclear record.**
- Option F was adopted by David (#104). Its demotion was recommended by Geometry (#118), made in the v0.5 outline (#119) and passed by its panels (#120 to #122); no separate signature from David was found (`a-option-f`).
- v0.8 Appendix B.2 says drops before v0.8 were unlogged. The reasons for dropping v0.3's "topology may vary" and "distinct world ensembles do not intersect" are therefore not in the record (`a-world-analytic`).
- The isotropy quotient was lost silently in v0.5 prose and restored in v0.6 (`a-jet-direction`).
- Gielen–Wise: the in-house reason (their space needs a world first) is weaker against the abstract form Literature #158 cites. The public reason (points are 4-velocities, not germs) is the one carried (`a-gielen-wise`).
- The Everett world-counting firewall is found in the paper from v0.6. Its earlier source is Paper 1, and a first-appearance commit was not traced (`a-everett-worlds`).
- The arm set changed across versions: out-star only in the v0.4 cover, continue arm included from v0.6 (`a-option-e`).
- Reopen-if conditions marked "Mapper's proposal" are not in the record. The others paraphrase the record's own reasons or escape clauses.
- Tags, the root's wording and all ratings are the mapper's.

## Viewer format notes (README followed where it differs from the brief)

1. `reopen_if` (README), not `reopen-if`.
2. `q` and `a` are numbers (README). The level (high / medium / low) is given in a comment.
3. `h` is computed by the viewer, not stored as a field. It is shown in a comment in each file and in the table above.
4. `status` and `tag` are for answers only (README). Question nodes carry neither.
5. `hold` (L0–L4) is a README field that the brief does not list. It is included.
6. `sources` uses the README's `label` / `url` form.
7. This `index.md` has no frontmatter, so the viewer ignores it. `graph.yaml` is the optional metadata file.
8. The viewer warns when a version selects a non-accepted node. `versions/v0.4.yaml` selects Option F and V*, accepted then and rejected now, so the build gives 2 warnings and 0 errors. That is expected in a retro-map.

Build check: `node build/build.mjs --in <this folder> --out graph.json` gives 30 nodes, 6 versions, 2 warnings (above) and 0 errors.

## Review

Geometry checks the math and the version selections. Literature checks citations and attributions. Physics Lead merges.
