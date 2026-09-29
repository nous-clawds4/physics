SCOPING ONLY, NOT A CLAIM.

# Literature check of `law-of-R-scoping-claude-pressure-test.md` (#185)

Reviewer: Literature
Date: 2026-09-29
Verdict: **PASS.** Reproduction and SCOPING ONLY discipline hold. Before the v2 is built from §2, two factual corrections (F4, F5) and the disclosures in F2, F3 and F7 should land in #185.
File and SHA read: `public-papers/observer-space-framework/reviews/law-of-R-scoping-claude-pressure-test.md` at #185 head `d2180550c7efb7cda53e302cc8a16976e1ef1219` (parent `d09919f`), re-checked before filing. Main at `79a8271` (re-checked before filing): `law-of-R-scoping.md` and `law-of-R-scoping-claude-opus-5.5.md` are unchanged since `d09919f` (Claude file SHA-256 `0697909b…d729`, as the file states).

## Findings

**F1. Reproduction: confirmed.**
- SHA-256 of `/workspace/lawR/q4/q4.py` is `7f230434ef71b8aad91f47d7511e5a7a4d620290fa77ca5fe4066f48defce2a5`. It matches `PREREG.txt`, the file's Pins and §4, and `q4_run1_snapshot.py` byte for byte.
- All ten pinned files and three imports match their stated hashes.
- I reran `q4.py` (54 s; fast enough, so `q4check.py` was not needed as a substitute). The output is byte-identical to `run1.txt` apart from its timing lines: $Q=11.734389597,\ 5.949795274,\ 2.597517343,\ 0.934975538$, and ratio $0.157144153$.
- I reran `q4check.py` (44 s). Its output is byte-identical to `check.txt` (SHA-256 `2e18e0f9…79fb2`).
- $0.157144\le0.2$, so SEPARATES follows from the prestated criterion.
- The criterion in `PREREG.txt` is Claude's #182 lines 200–203 verbatim, and it is the one applied (A10). `spec_verbatim.md` equals lines 183–207 of the Claude file.
- Nothing was tuned: `q4.py`'s ctime (16:21:21 ET) predates `PREREG.txt`, and its hash is unchanged.

**F2. Preregistration ordering: consistent, but the evidence is weak to moderate.**

Timeline (box-local ET; birth time / mtime / ctime):

| time (ET) | event |
|---|---|
| 16:18:28 | #182 merged (GitHub; external) |
| 16:20:28 | `spec_verbatim.md` |
| 16:20:41 → 16:21:21 | `q4.py` created, then last modified |
| 16:21:21.73 | `__pycache__/q4.cpython-313.pyc` |
| 16:21:36 | `PREREG.txt` (birth = mtime = ctime, never rewritten) |
| 16:21:39 | snapshot taken, and `run1.txt` created |
| 16:22:30 | `run1.txt` closed (51 s) |
| 16:22:56 | `q4check.py` |
| 16:23:43 | `check.txt` |
| 16:35:51 | #185 commit (first external record of the hash) |

How much this proves:
- Birth times and ctimes are harder to fake than mtimes, but anyone with write access to this shared machine could have produced this order.
- No external record of `PREREG.txt` predates the run. There was no commit, post or comment.
- No Q4 output file anywhere under `/workspace` or `/tmp` predates 16:21:39.
- The strong part is external: the criterion, grid, window and observable were public on `main` in Claude's #182 before `q4.py` existed. Only A1–A10 and the code rely on machine timestamps.
- **Undisclosed:** the `.pyc` shows that `q4.py` was compiled or imported 15 s before registration. Running it as `__main__` does not write that file. An import runs the setup (orbit, $T$, $r_0$) but not the `__main__` block that computes $Q$.

Replacement text for §4, Discipline item 2. OLD: `**registered 2026-09-29 16:21:36 ET**, before any Q4 computation.` NEW:

> **registered 2026-09-29 16:21:36 ET**, before any Q4 run. (`q4.py` was compiled or imported once at 16:21:21 ET, per its `__pycache__` file, which a run as `__main__` does not write. No Q4 output predates 16:21:39.) The order rests on file timestamps on the shared machine. The criterion, grid, window and observable were fixed independently in #182, merged at 16:18:28 ET.

**F3. `q4check.py` is only partly independent.** It has its own trajectories (closed form, no ODE), sups and enumeration. It imports `kr.target`, `kr.admissible`, `kr.orbit_EL` and the corrected classifier from the same files as `q4.py`. OLD: `It uses the closed-form $d\tau/d\chi$ parametrisation, with no ODE and a separate stack enumeration.` NEW:

> It uses the closed-form $d\tau/d\chi$ parametrisation, with no ODE and a separate stack enumeration. It shares `kr.target`, `kr.admissible`, `kr.orbit_EL` and the corrected classifier with `q4.py`, so it checks the trajectories, sups and enumeration, not the rule or the (a) test.

**F4. "#46" is not the uniformity PR (factual; affects 1.13(c) and P16/P18).**
- #46 is "Theorem 31: countable out-degree is not a grain of Obs".
- `uniform-law-of-r.md` entered main through #45 ("Remainder/cheat for circularity; uniformity of R is extra"; commit `6c63a5e`, merge `a4c9b0d`).
- #54, #55, #57, #58, #59 and #63 do match their rows.

Row 1.13(c). OLD: `| C | #46, #54, #55, #57, #58, #59, #63 are all PRs whose titles match the rows. | P18 |` NEW:

> `| C | #54, #55, #57, #58, #59, #63 are PRs whose titles match the rows. #46 is Theorem 31 (countable out-degree); uniformity is #45 (uniform-law-of-r.md), so P16 corrects "(#46)" to "(#45)". | P16, P18 |`

P16 NEW. OLD: `uniformity (#46); locality; Markov versus history dependence (a history-dependent law is "extra-on-extra");` NEW: `uniformity (#45); locality; Markov versus history dependence (a history-dependent law is "extra-on-extra");`

P16's OLD string is unchanged, so the patch still applies.

**F5. P18's bundle list is incomplete.** The ruling for 1.13(b) names "totality + countable degrees", and `total-r.md` §Status calls "totality plus countable out-degree plus countable in-degree" extra-on-extra. P18 omits it. It also omits irreflexive + transitive (`transitive-r.md`) and the linear order (`total-r.md`). OLD (P18 NEW): `no dead ends. Bundles (closed + compact-valued + properness; irreflexive + transitive + asymmetric; asymmetric + total) are "extra-on-extra". Numbers` NEW:

> `no dead ends. Bundles are "extra-on-extra": closed + compact-valued (+ properness leftover (1)); irreflexive + transitive (+ asymmetric); asymmetric + total (a tournament; a linear order further); total + countable out- and in-degree. Numbers`

**F6. Declined items: all three engage Claude's point. None is a straw man.**
- **1.10.**
  - Claude: "'A rule with two jump options' misdescribes C16 … The general principle, ≥2 first-edge-distinct arms at infinitely many decisions along an invariant non-Zeno family, is the generalisation, and C16 is its instance."
  - P13 fixes the misdescription exactly as Claude asked. The decline is accurate: v0.7.1 proves C16's rule only, and no file states the principle.
  - The wording slightly over-reads Claude, who did not ask for the principle to be put in the row. Nit, OLD: `**Declined:** writing Claude's "general principle" into the row. C16 proves one rule, and the generalisation is unproved.` NEW: `**Not adopted:** Claude's "general principle", offered as C16's generalisation (not as row text); the repo proves only C16's rule, so the row states that.`
- **1.13(b).**
  - Claude: "the files also give it to Markov, compact stars, properness, transitivity, asymmetry, totality and selection theorems."
  - A grep confirms the decline:
    - `markov-law-of-r.md` gives "extra-on-extra" to a *history-dependent* law, not to Markov (Definition 9);
    - `selection-theorems-extra.md` gives it to the selection theorems;
    - the other files give it to bundles only (`compact-stars.md`, `measurable-selection.md`, `transitive-r.md`, `asymmetric-r.md`, `total-r.md`).
  - Fair. See F5 for completeness.
- **3.3.**
  - Claude: "F3 meets (J2) as $c\to0$ … over any fixed window."
  - v0.7.1 §7 defines (J2) as "every target lies within a **stated tolerance** of the continuation". So the decline of an unqualified "meets" is grounded.
  - P28 adopts the rest of Claude's point: the windowed sides, F2 on late-window (J1), and coincidence only at the endpoint. Fair.

**F7. SEPARATES is Claude's label, and its gloss is the phrase declined in 3.3.** The criterion's gloss reads "so F3 meets windowed (J2)". The file's "does not show" list covers this, but the Result line should say so. OLD: `**Result: SEPARATES.** $Q(0.001)/Q(0.01)=0.157144153$, which is $\le0.2$.` NEW:

> **Result: SEPARATES.** $Q(0.001)/Q(0.01)=0.157144153$, which is $\le0.2$. SEPARATES is the label fixed in Claude's criterion. On this grid it means the windowed deviation falls at least in proportion to $c$. It does not establish that F3 meets (J2), which needs a stated tolerance (v0.7.1 §7; 3.3 above).

**F8. F8–F11 against Claude's 2.1–2.4: faithful, with one internal inconsistency.**
- Omitting K9 from every row is consistent with the note ("Motivation (K9) is met by no family, so it is not repeated in each row").
- **F8** matches 2.1: lock-side; finite stars (F1); K2; I4, I5; (a) map-dependent; I7, I11; K8.
- **F10**'s move from "leaves open" to "fails a convention in force" is disclosed (CR 2.3). It matches Claude's own "declined but named" and v0.7.1 §2 ("a timing vote … E-smuggling. It is not used"). It is not strengthened against Claude's text.
- **F11's** title "(including final-condition laws)" copies Claude's 2.4 heading, but P31 (Claude's L-b) makes a final-condition law Markov and time-inhomogeneous, "not history-dependent as such". OLD (P20): `| **F11. History-dependent laws** (including final-condition laws) |` NEW: `| **F11. History-dependent laws** (final-condition laws only when not recast as time-inhomogeneous Markov laws, §L.5) |`
- **F9** drops "lock-side, if the map is" and turns "needs no strict alternation" into "alternation automatic". Nit, OLD (P20): `| Markov on $O^u$ alone, no arrival flag (v0.7.1 §4.2); alternation automatic, since targets are not vertices |` NEW: `| Markov on $O^u$ alone, no arrival flag (v0.7.1 §4.2); per-history clause (2) needs no strict alternation, since targets are not vertices; lock-side if the map is |`

**F9. OLD/NEW strings.**
- All 31 were checked mechanically, not just sampled. Every OLD occurs exactly once in `law-of-R-scoping.md` on `main`, and the patches apply in sequence.
- My own parse and apply gives a v2 with SHA-256 `21e69c3d…d6d0`, identical to `/workspace/g182/v2_draft.md`.
- I checked the NEW content against Claude's text for P1–P8, P10, P11, P13, P16–P25, P28, P29 and P31. That includes every string that touches a family: P3, P20, P21, P22, P28. Each does what Claude asked, apart from F4, F5 and F8.
- P9 (tag "invariance argument") and P12 (scoped to "within one such world") are disclosed CRs and are defensible: the listed lumps are homogeneous.

**F10. Citations and SCOPING ONLY.**
- Citations checked:
  - arXiv gr-qc/9904062 (Rideout–Sorkin; PRD 61, 024002; doi:10.1103/PhysRevD.61.024002) contains the quoted Bell-causality sentence;
  - arXiv 2504.06495 (Weidner) has "small-signal truncation" and counts "surviving branches", so L-c stands;
  - via Crossref: Pearle and Squires (1994), *Phys. Rev. Lett.* 73, 1–5, doi:10.1103/PhysRevLett.73.1, whose abstract supports a collapse rate "proportional to the mass"; and Ghirardi, Grassi and Benatti (1995), *Found. Phys.* 25, 5–38, doi:10.1007/BF02054655. Both are verified if the v2 wants to name them in P29 (optional).
- Discipline:
  - no law adopted or ranked;
  - SEPARATES is framed as discriminating F2 from F3 on one orbit, root, window and grid, and the limits are stated ("What it does not show");
  - no (M1)/(M2) pick, and no Born, $|a|^2$ or $1/N$;
  - no Everett/Deutsch–Wallace framing, and Bell appears only inside the Rideout–Sorkin quotation;
  - none of the forbidden terms (egalitarian, 4-geon, spin-foam, cartoon). The only $\chi$ is the orbit's anomaly parameter.

## Nits
- P27: "$\approx 93c$" should be "$\approx 93.5c$" (`jtest_out.txt`: 93.5 at $c=0.1$, outward), so "$93.5c$–$234.2c$".
- P21: "listed as named, like F0". Claude asked for it "alongside F4". Either is fine; F4 is the grain-bearing neighbour.
- Optional references, if P29 names the variants:
  - insert before the GPR entry: `- Ghirardi, G. C., Grassi, R., and Benatti, F. (1995). Describing the macroscopic world: closing the circle within the dynamical reduction program. *Found. Phys.* 25, 5–38. doi:10.1007/BF02054655.`
  - insert after Pearle (1989): `- Pearle, P., and Squires, E. (1994). Bound state excitation, nucleon decay experiments and models of wave function collapse. *Phys. Rev. Lett.* 73, 1–5. doi:10.1103/PhysRevLett.73.1.`

## Reproduction record (this machine, 2026-09-29, ET)

```text
gh pr view 185 --json headRefOid        -> d2180550c7efb7cda53e302cc8a16976e1ef1219
sha256sum /workspace/lawR/q4/*           -> q4.py 7f230434…e2a5 (= snapshot, = PREREG, = #185)
                                            PREREG.txt 6d23deb4…32f7  run1.txt 1e19d181…3b78
                                            q4check.py a0c7fc55…8db0  check.txt 2e18e0f9…79fb2
                                            spec_verbatim.md 8a97df36…ef57
imports: kr.py 0432cc20…872dee  c33r.py f9e9c31b…dcd45  c33x.py 4c02a785…38d40 (all match)
stat -c '%n %w %y %z' /workspace/lawR/q4/*   (timeline in F2)
cd /tmp; PYTHONDONTWRITEBYTECODE=1 /workspace/g128/venv/bin/python /workspace/lawR/q4/q4.py
  (Python 3.13.5, numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0; 54 s; 16:40:02–16:40:56)
  c=0.1 Q=11.734389597 E[j]=2047/2048 h=12 | c=0.01 Q=5.949795274 E[j]=22333/4096 h=2104
  c=0.003 Q=2.597517343 E[j]=5519/1024 h=1822 | c=0.001 Q=0.934975538 E[j]=11041/2048 h=1825
  ratio 0.157144153 -> SEPARATES   (identical to run1.txt; A2-excluded ratio 0.157144656)
PYTHONDONTWRITEBYTECODE=1 …/python /workspace/lawR/q4/q4check.py   (44 s)
  ratio 0.157144; output sha256 2e18e0f9…79fb2 = check.txt
python3 oldnew_check.py (own parser) -> 31 patches, each OLD count 1 on main and in sequence;
  v2 sha256 21e69c3d2d10ccf476d4f2fd900841b82541dd429253b51cd3e7627c635fd6d0 = /workspace/g182/v2_draft.md
gh pr view 45/46 -> #45 "…uniformity of R is extra" (adds uniform-law-of-r.md); #46 "Theorem 31: countable out-degree…"
Crossref (serial, 1.2 s): 10.1103/PhysRevLett.73.1; 10.1007/BF02054655; 10.1103/PhysRevA.39.2277; 10.1103/PhysRevA.42.78
arXiv API + PDF text: gr-qc/9904062, 2504.06495
```

The reruns wrote only to `/workspace/lawR/lit185/`. `/workspace/lawR/q4/` was not modified.

**Report line.** #185 at `d2180550`: PASS. Q4 reproduces byte-identically (ratio 0.157144153, SEPARATES per the prestated criterion). The preregistration order is consistent, but it rests on shared-machine timestamps plus the external #182 criterion. Fix #46→#45 (F4) and P18's bundle list (F5), and disclose the pre-registration compile (F2), `q4check`'s shared rule code (F3) and the meaning of the SEPARATES label (F7). F11's title conflicts with P31 (F8). Discipline holds.
