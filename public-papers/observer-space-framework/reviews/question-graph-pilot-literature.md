# Literature: citation and attribution check of the question-graph pilot (Path of 42), physics#199

Reviewer: Literature
Date: 2026-09-30
**Read:** #199 at **`4e6d0783afbd06ae375ca4f638f810b21b4246b4`** (branch `question-graph-pilot`), confirmed unchanged before filing. Baseline: `main` at `5acf9d3`, the SHA every node's blob links pin to.
**Scope:** all 30 nodes (9 `q-*`, 21 `a-*`), plus `index.md`, `graph.yaml` and `versions/*.yaml` where they make source claims. Math and version selections are Geometry's; not re-derived here.
**Verdict: HOLD (narrow).** Every cited PR, commit, file and version exists. The external work (Gielen–Wise) is verified. The forbidden-word scan and every guardrail are clean, and Paper 1 is untouched. The HOLD is for citation and attribution errors that point readers to the wrong source or the wrong decider:
- five nodes cite the wrong "#128 row";
- one correction is credited to Geometry when it was Claude's;
- the Option F demotion is said to have been "ruled" by Geometry, which only recommended it;
- one node calls two merged PRs "open".

There are 14 required fixes and 4 optional ones, all exact strings (below).

**Method.**
- PR metadata: one GraphQL batch for all 37 PRs cited (#98–#199, plus infinite-harness#7).
- Every quoted string was grepped in its source file at `5acf9d3`.
- Crossref: one query (Gielen–Wise).
- `wds4/physics`: file history read via the GitHub API.
- Items verified in earlier Literature reviews (#158 Gielen–Wise wording; #186 SHPMP 2008, MMWI and Strayhorn3 records) were not re-derived.

---

## Per-node table

| Node | Sources checked | Result |
|---|---|---|
| `a-root` | IH `docs/path-of-42.md` at `6f02238` (§2 root L0, §7 physics seed); `docs/scratch/path-of-42.md` (#194, commit authored by David Strayhorn: "Accepted node will be: no privileged pieces of matter"); v0.7.1 §1 | OK |
| `q-observer-object` | #98; v0.7.1 §2 | OK |
| `a-jet-direction` | #98 (v0.3 changelog: vertices are oriented observers); #128 §4.1 (isotropy dropped); #129 claim 3 ACCEPT; #130 ("restored … after silent loss in v0.5 prose"); v0.7.1 §9 T1 row; v0.8 B.2a/B.2b; Paper 1 | OK |
| `a-gielen-wise` | v0.3 §2 (not Gielen–Wise's 7-manifold); `papers/obs-as-a-space.md` (Killed list; "needs a $W$ first"); #158 L1 via v0.7 outline item 18; v0.7.1 §10 "Phrase collision only"; Crossref: Gielen & Wise, *J. Math. Phys.* 54 (2013), doi:10.1063/1.4802878 | OK |
| `q-what-is-a-world` | #98 §2; v0.7.1 §2 | OK |
| `a-world-analytic` | v0.3 §2; v0.7.1 §2 ("not extra vertices, and not a second observer"); v0.8 B.2b rows (#183) | OK |
| `a-everett-worlds` | Paper 1 §9 ("they are not Everett worlds") and Abstract ("not Everettian quantum mechanics"); v0.6 prose l. 309 (first appearance of the firewall; absent from v0.5); v0.7.1 §3, §7, §10 | OK |
| `q-branching` | `reviews/v0.2.1-prose-claude-fable-5.1.md` (HOLD, one HOLE); Geometry confirmation in `reviews/v0.2.1-motion-recommendation-geometry.md` ("Verdict on HOLE: CONFIRM"); v0.3 Status line; #98; Q-D file | OK (the Geometry confirmation file is not listed as a source; optional) |
| `a-cws-branching` | #98; #105 ("As an error the HOLE is cleared"); #117 Claim A; #118; #134 banners; v0.7.1 §4.1 (E1)/(E2) | **Issue:** credits Geometry #118 with correcting the singleton's attribution. The correction is Claude's #117 Claim A ("CWS HOLE misattributed to matching order"). #118 ACCEPTs it: "Claude is right that #92 Step 1 is shared oriented germ + geodesic uniqueness". Fix 1 |
| `a-type-ii` | #98 (Def. 7); `papers/type-ii-adopted.md` Prop. 13; #105; v0.7.1 §4.2, §4.3, §9 | OK |
| `q-join-law` | #102 (join menu; Geometry note per #104's body); #105 §2 | OK |
| `a-option-f` | #103; #104 (body: "David (2026-09-07) adopted Ontology Option F…"; the note's stamp "Adopted (working, abandonable) — David 2026-09-07"); #108; #112; #117; #118; #134; `papers/piecewise-geodesic-Ck-graph-ontology.md` | **Issue:** "the demotion … was ruled by Geometry (#118)". #118 accepts Claim A and *recommends* the demotion ("Recommend demote F→E in v0.5"; "For public v0.5: demote F → E residue"). The demotion was made in the v0.5 outline (#119) and passed by its panels (#120 to #122). The node's handling of David is right: #104 is a record of David adopting F, and no record of David signing the demotion exists (commit log and #118/#119/#134 bodies searched). Fix 2 |
| `a-option-e` | #118 §3 ("does not buy branching power"); #119; #123; v0.5 Status ("cleared as a definition"); `reviews/v0.4-prose-claude-cover.md` (arms = out-star); #130 (out-star replaced) | OK |
| `q-vertex-times` | #105 §3.1; #112 (hard gate, clause (2)) | OK |
| `a-vstar` | #106 ("adopt $V^*$ with caveats", quoted in #134); #107; #112; #117 Claim B; #118 ACCEPT; #134; `papers/Vstar-extend-vs-not.md`; v0.7.1 C24, C25, §5.1 | OK |
| `a-vtau` | #119; #123; #129 claim 5 QUALIFY; v0.7.1 §5.1, §9 | **Issue:** "Claude #128 row 5". #128's row 5 is "per-vertex ≠ Paper 1 count"; the $V^\tau$ residuals are under #128's **row 2** (l. 119–120). Fixes 3–4 |
| `q-composition` | #105 §2; #112; #128 row 2; #129 claim 2 and Option (C); Q-D file | OK (T1 = Q-D5 and Q-D2 = "Next" match logged difference 2) |
| `a-alternation` | #112; #105 reading (C); #128 row 2; #129 claim 2 QUALIFY (quoted accurately); #130 ("Geometry's option (A) adopted"); v0.7.1 §9 | OK |
| `a-jump-bound` | #128 row 2; #129 ("Not recommended"); #130 ("Rejected alternatives [Geometry over #128]"); v0.7.1 §9 T1 row | OK (the attribution follows the record's own tag) |
| `a-target-avoid` | #129 ("Option (C), not in #128"); #130; #133 (label collision "Fixed in #130 before filing"); v0.7.1 §4.2 | OK |
| `q-realisation` | #112 (open one-liner); #123; #128; #129 claim 1 ACCEPT; #130; v0.8 B.2b ("(a) versus (b) moved to open call"); v0.7.1 §4.2 | **Issue:** "#128 row 1". #128's row 1 is Option F; the (a) cost row is #128's **row 7** ("HOLD: the cost row is false"). "#129 row 1" is #129's claim 1. Fixes 5–7 |
| `a-real-a` | #128 row 7; #129 claim 1; #130; #156; #169 (declined clause); v0.7.1 C2, C4, C33 | **Issue:** the same row labels (Fixes 8–9). Optional: #169 declines the circularisation clause because the census contradicts its mechanism, not because it is "unpinned" (Fix 15) |
| `a-real-b` | #128; #130; #156; v0.7.1 §4.2 ("a measurement picture would want"), C16, C17; Paper 1 §6 ("a failure of the program") | OK |
| `q-measure` | #128; #129 claim 4; #130; #149; #156; #139 body (a)–(e); Q-D file; v0.7.1 §9 row (b) "= T2 and (M1)/(M2)" | **Issue:** "#128 row 4". #128's row 4 is graph hygiene; the measure claim is #128's **row 5** (#129 claim 4). Fixes 10–11 |
| `a-m1` | #98; #128; #154 R7; #155 R7 QUALIFY; #156 ("Not adopted from #154: … R7's framing of the (M1) line as 'overstated'"); v0.7.1 §3, §9, C12, C16, C33 | **Issue:** label "(row 4)" (Fix 12). Optional: the non-adoption of R7's framing is recorded by the v0.7 outline, after Geometry's QUALIFY (Fix 16) |
| `a-m2` | Paper 1 §6 ("countable at a grain"); #130; #156; #168; #169; v0.7.1 §3, §9 | OK |
| `a-anchored-count` | #160 (v0.7 §9, "unless it is anchored", l. 366); #162; #168; #169 ("I withdraw that part of #162"; C13 1/10, 1/15 against 1/12); #170 (P1–P5 are the §9 / table / C13 items; P6–P8 are the C33 items) | OK |
| `q-law-of-r` | #105; #178; v0.7.1 header, §4.2 soft Prop. 13 ("No law of $R$ is written") | **Issue:** "the open #185 and #187". Both were merged, at 6:19 and 6:20 PM ET on 30 Sep, three minutes before the pilot commit. Fix 13 |
| `a-hand-listed` | #105 (verbatim: "is met by a hand-drawn two-vertex graph, so it is not a test"); #107 (retired-as-demo banner); #112 firewall; v0.5 gate (per #128 row 6); v0.7.1 §5.4 ("uniform, not a hand list") | OK |
| `a-kretschmann` | #117 (the rule is "#117's Kretschmann rule" in #128); #128; #129 (orbit $[10,20]$); #130; v0.7.1 §4.2 ("It adopts no $R$"), C17, C33, C34 (2/3 in expectation) | OK |

**`index.md`:**
- The "ruled by Geometry" line under Unclear record repeats the `a-option-f` issue (Fix 14).
- The `wds4/physics` sentence is true only historically. The paragraph is in `wds4/physics` v0.5 at `047ba16` (identical to `docs/scratch/path-of-42.md` up to one line break), and it was removed there at `69f4042` (29 Sep, 7:34 PM ET) (Fix 17).
- "The v0.7.1 header maps them … (b) = T2 and (M1)/(M2)": (b) is mapped in the §9 calls table, not the header (Fix 18).
- Q-D1–Q-D5 "(physics#142)": the PR is closed, not merged, but the file landed on `main` as `88cfdf5` "(#142)", so the citation stands.

**`graph.yaml`:** `source_base_url` points at the `question-graph-pilot` branch, which will go stale if the branch is deleted after merge. This is a note for the Lead; it gets no fix here.

**`versions/*.yaml`:** each source PR is the right prose PR (#98, #112, #123, #135, #160, #170). The "rejected at this version" and changed-node summaries match the per-node findings.

## Findings

1. **Sources exist.** All 36 physics PRs cited exist; 35 are merged, and #142 landed on `main` by commit. infinite-harness#7 is merged, and `6f02238` holds `docs/path-of-42.md`. Every blob link resolves at `5acf9d3`.
2. **Row-number misreads (five nodes).** The "#128 row N" citations in `q-realisation`, `a-real-a`, `q-measure`, `a-m1` and `a-vtau` follow the numbering of #129's claim table ("# | Claim in #128"), not #128's own rows. In #128 itself, row 1 is Option F, row 2 is $V^\tau$ and clause (2), row 4 is graph hygiene, row 5 is per-vertex against count, and row 7 is realisation (a). `q-composition` and `a-jump-bound` (row 2) happen to match both schemes.
3. **Misattribution in `a-cws-branching`.** The node credits Geometry with a correction that Claude #117 made (Claim A); Geometry #118 accepted it.
4. **Overstated ruling in `a-option-f` and `index.md`.** Geometry #118 recommended the F → E demotion. The v0.5 outline (#119) made it, and the v0.5 panels (#120 to #122) passed it. The pilot's David check is sound: #104 records David adopting F, and no David signature on the demotion was found. The flag stays; only the decider is corrected.
5. **Other David attributions: all backed by a record.** `a-root` rests on `docs/scratch/path-of-42.md`, committed by David in #194. `a-option-f` rests on #104's adoption record. No node says David rejected, accepted or demoted anything else.
6. **Other rulings: attributed as the record states.** Examples: (B)'s rejection "[Geometry over #128]" (#130), #129's QUALIFY on (A), #169's withdrawal of part of #162, and Claude #105's "cleared as an error". The optional Fixes 15–16 tighten two paraphrases.
7. **Stale status in `q-law-of-r`.** It calls #185 and #187 "open"; both are merged.
8. **External source.** Gielen–Wise, "Lifting general relativity to observer space", *J. Math. Phys.* 54 (2013), doi:10.1063/1.4802878 (Crossref). The 7-dimensional space and the abstract Cartan form match the node and v0.7.1 §10. CWS is an in-house term (v0.2.1 prose), not an external paper. `/workspace/old-ms` was not needed: no node cites a manuscript claim beyond what v0.7.1 carries, and #186 already checked those records.
9. **Forbidden words: clean.** None of the house-excluded terms listed in the brief (the six words and symbols, including the Ghirardi–Rimini–Weber acronym) occurs in any of the 38 files; the index even avoids the record's name for the maximal-entropy random walk.
10. **Guardrails: clean.**
    - No law of R is adopted. `a-kretschmann` is open and "unadopted", and `q-law-of-r` has only open or rejected answers.
    - Born, |a|² and 1/N appear nowhere as a result.
    - (M1) and (M2) are both open, with the same a. T1–T3, Q-D1–Q-D5 and #139 (a)–(e) are named as open, with no accepted node.
    - There is no framing of Everett against Deutsch–Wallace. `a-everett-worlds` records Paper 1's firewall only.
    - Bell appears only as "which Bell premise" and is never called refuted.
    - Paper 1 is untouched: #199 changes only files under `question-graph/`.

## Fixes (OLD → NEW; each OLD occurs exactly once in the named file)

Required (1–14):

**Fix 1, `a-cws-branching.yaml`.** OLD:
```text
Claude #117, Claim A) corrected the attribution:
```
NEW:
```text
Claude #117, Claim A) accepted Claude's correction of the attribution:
```

**Fix 2, `a-option-f.yaml`.** OLD:
```text
here was ruled by Geometry (#118) and carried through the v0.5 panel
```
NEW:
```text
here was recommended by Geometry (#118), made in the v0.5 outline (#119) and passed by its panels (#120 to #122)
```

**Fix 3, `a-vtau.yaml`.** OLD:
```text
costed after Claude #128 row 5 and Geometry #129
```
NEW:
```text
costed after Claude #128 row 2 and Geometry #129
```

**Fix 4, `a-vtau.yaml`.** OLD:
```text
"physics#128: Claude HOLD on v0.5 prose (row 5)"
```
NEW:
```text
"physics#128: Claude HOLD on v0.5 prose (row 2)"
```

**Fix 5, `q-realisation.yaml`.** OLD:
```text
after Claude #128 row 1 (Geometry #129 ACCEPT:
```
NEW:
```text
after Claude #128 row 7 (Geometry #129 claim 1 ACCEPT:
```

**Fix 6, `q-realisation.yaml`.** OLD:
```text
"physics#128: Claude HOLD on v0.5 prose (row 1)"
```
NEW:
```text
"physics#128: Claude HOLD on v0.5 prose (row 7)"
```

**Fix 7, `q-realisation.yaml`.** OLD:
```text
"physics#129: Geometry: row 1 ACCEPT"
```
NEW:
```text
"physics#129: Geometry: claim 1 ACCEPT"
```

**Fix 8, `a-real-a.yaml`.** OLD:
```text
"physics#128: Claude HOLD on v0.5 prose (row 1)"
```
NEW:
```text
"physics#128: Claude HOLD on v0.5 prose (row 7)"
```

**Fix 9, `a-real-a.yaml`.** OLD:
```text
"physics#129: Geometry: row 1 ACCEPT"
```
NEW:
```text
"physics#129: Geometry: claim 1 ACCEPT"
```

**Fix 10, `q-measure.yaml`.** OLD:
```text
after Claude #128 row 4 and Geometry #129
```
NEW:
```text
after Claude #128 row 5 and Geometry #129 claim 4
```

**Fix 11, `q-measure.yaml`.** OLD:
```text
"physics#128: Claude HOLD on v0.5 prose (row 4)"
```
NEW:
```text
"physics#128: Claude HOLD on v0.5 prose (row 5)"
```

**Fix 12, `a-m1.yaml`.** OLD:
```text
"physics#128: Claude HOLD on v0.5 prose (row 4)"
```
NEW:
```text
"physics#128: Claude HOLD on v0.5 prose (row 5)"
```

**Fix 13, `q-law-of-r.yaml`.** OLD:
```text
(#178, #182, and the open #185 and #187)
```
NEW:
```text
(#178, #182, #185 and #187, all merged)
```

**Fix 14, `index.md`.** OLD:
```text
Its demotion was ruled by Geometry (#118) and carried by the v0.5 panel
```
NEW:
```text
Its demotion was recommended by Geometry (#118), made in the v0.5 outline (#119) and passed by its panels (#120 to #122)
```

Optional (15–18):

**Fix 15, `a-real-a.yaml`.** OLD:
```text
unpinned (#169).
```
NEW:
```text
not borne out by the census (#169).
```

**Fix 16, `a-m1.yaml`.** OLD:
```text
Geometry did not adopt Claude #154's R7 framing of
```
NEW:
```text
Geometry qualified Claude #154's R7 (#155), and the v0.7 outline did not adopt its framing of
```

**Fix 17, `index.md`.** OLD:
```text
in `wds4/physics`, *Statement of the Problem* v0.5)
```
NEW:
```text
in `wds4/physics`, *Statement of the Problem* v0.5 at `047ba16`; removed there at `69f4042`)
```

**Fix 18, `index.md`.** OLD:
```text
the v0.7.1 header maps them (
```
NEW:
```text
the v0.7.1 header and §9 calls table map them (
```

## Report line

Literature: **HOLD (narrow)** on the question-graph pilot, #199 at `4e6d078`.
- All sources exist; Gielen–Wise is verified by Crossref; the forbidden-word scan and guardrails are clean; Paper 1 is untouched.
- Required: 14 exact fixes.
  - Five nodes cite "#128 row N" by #129's claim numbering (realisation is #128 row 7, measure row 5, $V^\tau$ row 2).
  - `a-cws-branching` credits Geometry with Claude #117's correction.
  - `a-option-f` and `index.md` call Geometry's recommendation a ruling; the demotion was made in the v0.5 outline (#119) and panel-passed.
  - `q-law-of-r` calls the merged #185 and #187 "open".
- The David check is sound: #104 and #194 are records of David; no David signature on the Option F demotion exists, and the pilot says so.
- Optional: 4 fixes.
