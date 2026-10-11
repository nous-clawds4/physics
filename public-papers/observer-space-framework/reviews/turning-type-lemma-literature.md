# Literature claim and record check: the turning-type lemma note (#290)

**Verdict: HOLD (narrow).** The mathematics holds, and every number I reran reproduces. Four text strings are needed (R1–R4). R1 matters most. #203's own derivation bullet already carries the throat proviso, so "refuted" applies only to the unqualified form of the lemma. Six optional strings (N1–N6) follow.

**Heads read:** #290 head `86e50c1` (one commit, one file, `notes/turning-type-lemma.md`, +161 lines, 2,119 words by `str.split`), base main `4d1fb11`. Current main is `6fb1566`: #283, #284 and #289 have merged since. C30, C31, C33, C37 and C38 are byte-identical in v0.9.1 at `4d1fb11` and `6fb1566`, so the note's pointers are unaffected. This file is a one-file PR from `6fb1566`. I merged nothing and messaged no one.

## 1. Pointers and record

- **Throat convention.** v0.9.1 §7 (line 226 ff.) gives two conventions. The **proposed default** is "continue through it", with the same static-frame speed and $\ell(r')-\ell(2)=\varepsilon-(\ell(r)-\ell(2))$. The **named alternative** makes the target undefined ($m=1$ there). There is no third convention. **The refutation is under the proposed default, not under a non-default convention.** The note says so plainly ("Under the proposed default ("continue through") it is refuted"). It labels "stop" as v0.9.1 does, as the named alternative, and recommends neither. That is neutral.
- **C37.** The thresholds 705.155 / 69,303.7 and the near-throat windows 2.00145 / 2.0000144 match the C37 Appendix A cell exactly.
- **C33.** The C33 cell gives 29,119 orbits, 14,478 stuck, $m\le1$ at every turning point ($c=0.01$), chain 14, and maximum apastron 23.24 ($c=0.1$) and 25.37 ($c=0.01$). The note's figures match.
- **C30, C31.** Lock-side (a) and the outward and inward edges at the $r=10$ periastron are as cited.
- **C38.** $dK/d\tau=-288M^2u^r/r^7$ supports "$dK/d\tau\propto u^r$".
- **"#238".** #238 is the merged C37 near-horizon-window PR (#235 N9), as cited.
- **"Prop. 3.2 of `papers/geodesic-lifts.md`".** This resolves from the repository root (not under `public-papers/`), and Proposition 3.2 is the unique-curvelet result, as used in A5.
- **$B_R$ and $F(O)$.** Both are defined in v0.9.1 §3 (§8.2 for $F(O)$).
- **"The brief's `g183/c33r.py`".** No such file exists on the box (confirmed). "The brief" is not in this repository; the v0.10 plan (#285, open) names no script. See N5.
- **#203's statement** (`reviews/v0.8-prose-claude-pressure-test.md`, merged in #203 at `00fc4ab`) comes in two forms:
  - Derivation bullet: "the edge into the orbit's radial range (outward at a periastron, inward at an apastron) keeps the source's turning type. Its orbit then lies wholly beyond the target, and it fails (a) at every turning point of every orbit, for every $c$, **provided the jump does not reach the throat**."
  - Summary ("The precise correct claim"): "at every turning point, the edge into the orbit's radial range fails (a)", with the corollary that C33's $m\le1$ is a theorem. It has **no** proviso. The v0.10 plan's item 1 (#285) restates this unqualified form for bound orbits.
- **What the note does with #203.** The note proves the proviso form, adding only the disclosed hypotheses: non-circular source, and the $\varepsilon=\Delta\ell$ case excluded. It also extends the result past the proviso: under *through* the lemma still holds when $\Delta\ell\le\varepsilon\le2\Delta\ell$ (equality excluded), and under *stop* it holds vacuously. The counterexample refutes only the unqualified form. The note never mentions #203's proviso, and "refuted" / "the #203 lemma, corrected" reads as if #203 itself was wrong as stated. **R1** fixes this.
- **Quotation.** Line 28 quotes #203 as "lands inside the orbit's radial range". That phrase occurs nowhere in the repository (`git grep` on `6fb1566`). #203's words are "the edge into the orbit's radial range (outward at a periastron, inward at an apastron)", which defines the edge by direction. **R2** fixes this.

## 2. Terms (well-posedness)

- Turning point, turning type, interior side, the jump, the into-range and away edges, the throat, $c^*$, (a), $m$ and bound source are all defined in §1, before the theorem.
- Circular orbits are excluded explicitly, so turning type is defined wherever it is used. $c^*$ is defined at its first use.
- The verdict paragraphs (lines 7–11) use $\varepsilon$, $\Delta\ell$, $m$, turning type, interior side, *stop* and *through* before §1. That is acceptable for a summary with a pointer (N1).
- Undefined in the note: $p$ and $e$ (line 36 and §4), $\delta$ (§4, near-circular), and "apo-plunge" (line 59). See N2 and R4.
- **Corollary wording.** Under *stop*, or at $\varepsilon=\Delta\ell$, the inward edge is **undefined**, not failing. The corollary's "It fails at every apastron except …" therefore asserts a failure for an edge that does not exist. **R3** fixes this.

## 3. Reproduction

All scripts are on the shared box under `/workspace/g286`, `/workspace/g201` and `/workspace/g168`. None is in the repository or the PR. Every pin matches sha256 (first 12 hex digits). `g201/census.py` = `97659775a495` and `g201/r1.py` = `edd8c89b2216`; the note gives only 8 digits for these two (N4).

- **Independent mpmath check** (my own script, dps 40, not reusing `tt.py`), for the source $r_0=3000$, $v=0.0015$, $c=0.1$:
  - $E=0.99966773572$, $L=4.50000506$, periastron $7.4107410$.
  - Inward through-throat target $r'=3227.2161034$, range $[9.1941635,\,3227.2161]\ni3000$, so it passes (a). The outward target is $9241.5617390$. So $m=2$, as claimed.
- **Thresholds**, from $\varepsilon=2\Delta\ell$:

  | $c$ | $r_0$ | $r_0c^2$ |
  |---|---|---|
  | 0.1 | 2786.469200 | 27.865 |
  | 0.05 | 11,103.119 | 27.758 |
  | 0.01 | 277,152.5785 | 27.7153 |
  | 0.001 | 27,712,846.58 | 27.71285 |

  The product tends to $4\sqrt{48}=27.71281$. The scaling claim holds; "about $27.7/c^2$" is the $c\to0$ limit, and it is 27.87 at $c=0.1$. Derivation: $\Delta\ell\sim r$ for large $r$, and $c\,r^{3/2}/48^{1/4}=2r$ gives $r=4\sqrt{48}/c^2$.
- **Where 705 comes from.** It is the C37 throat bound at $c=0.1$, from $\varepsilon=\Delta\ell$: $705.15498$. The $c=0.01$ bound is $69{,}303.706$.
- **$c^*$** $=1.5572089$ at $r=3.2698263$. ✓
- **Pinned runs, all byte-identical to the stored outputs:**
  - `proof286.py`: the sympy identities, all True.
  - `throat286.py`.
  - `census286.py 0.1` and `0.01`: 3 and 29,119 orbits, 14,478 stuck, 0 passing into-range edges.
  - `censusf286.py 0.1` and `0.01`: these reproduce the rows; maximum apastron $25.3669$ at $c=0.01$, which is C33's 25.37.
  - `boundary286.py`.
  - `sample286.py 20000 20000`, seed 286: S1 30,553 / 31,756 / 8,244 / 1,203 / 9,447, and S2 352 beyond, 346 pass, 345 with $m=2$. All as stated.
  - The script's default $N$ is 4,000, so the invocation must be stated (N6).
  - Not rerun: the $c=0.001$ capped census, for memory. The stored `out_censusf_0.001.txt` and `prog_0.001.txt` give 4,140,195 orbits at depth 21, 8,254,910 at depth 22, 8,280,390 into-range edges, 0 passing, and maximum apastron 20.7284, as stated.
- **Line 59.** The bullet "Not every beyond-landing passes" gives as its example $r_0=1000$, $v=0.0045$. That target lands **inside** (189.87 < 1000) after passing through the throat, since $\Delta\ell<\varepsilon<2\Delta\ell$. It is not a beyond-landing. The failing beyond-landings are S2's 6 of 352 (3 with a type change). **R4** fixes this.

## 4. Corollary and C33

- **Does C33's $m\le1$ become a theorem?** Yes, under the stated hypotheses.
  - The rule has two edges per vertex, and C38 makes vertices exactly the turning points. Fewer than two (a)-admissible edges means $m\le1$.
  - At $c=0.01$ every reachable turning point has apastron $\le25.37$. That is below both the throat bound $69{,}303.7$ and the exception bound $277{,}152.58$.
  - No reachable orbit can have a turning point in the near-throat windows. A passing target's range contains its source radius, which is greater than 4.
- **What it rests on.** It rests on one computed fact, the maximum apastron. The note says so.
- **Which bound applies.** The note cites "below $705.155$ and $69{,}303.7$". At $c=0.01$ only $69{,}303.7$ applies; 705.155 is the $c=0.1$ bound, where the maximum is 23.24 (N3). So "25.37 < 705", as relayed, is the wrong pairing. The c=0.01 comparison is 25.37 < 69,303.7, and the c=0.1 one is 23.24 < 705.155. Both hold.
- **Counts.** The note is careful not to claim C33's counts. §5 lists the counts, chain 14, acyclicity, transience, countability and the jump-count law as not implied, and gives the reason (decisions recur every radial period).

## 5. F11 and guardrails

- **F11.** No paper text is proposed and no F11 pick is made. v0.9.1 is untouched. The PR body cites #285 (open) only as the source of the question.
- **Forbidden words.** None: egalit, cartoon, GRW, 4-geon, spin-foam, χ and `\chi` all count 0.
- **Other guardrails:**
  - No Born, $|a|^2$ or 1/N claim.
  - No Everett-vs-Deutsch–Wallace framing.
  - No law of $R$ ("It sets no law").
  - Paper 1 untouched, no v0.9.1 pins changed, nothing recorded as signed.
- **Literature (optional).** The separatrix $p=6+2e$ and the bound-orbit facts $r_p>4$, $r_a>6$ are standard. Cutler, Kennefick & Poisson, Phys. Rev. D 50, 3816 (1994) is the usual citation. Nothing else is clearly needed.

## Exact strings (file `notes/turning-type-lemma.md`; each OLD occurs once at `86e50c1`)

**R1 (required: scope against #203's proviso).**
OLD: `Under the proposed default ("continue through") it is **refuted** at apastra with $\varepsilon(r_0)>2\Delta\ell(r_0)$.`
NEW: `Under the proposed default ("continue through") its unqualified form is **refuted** at apastra with $\varepsilon(r_0)>2\Delta\ell(r_0)$. #203's derivation bullet carries the proviso "provided the jump does not reach the throat" (`reviews/v0.8-prose-claude-pressure-test.md`), and in that form the lemma holds without exception. The refuted form is the unqualified one in #203's "precise correct claim" and in item 1 of the v0.10 plan (#285).`

**R2 (required: misquote).**
OLD: `This is #203's "lands inside the orbit's radial range" read by direction; the two readings differ only in the throat exception below.`
NEW: `This is #203's "edge into the orbit's radial range (outward at a periastron, inward at an apastron)", which #203 defines by direction. Reading "into the range" as where the target lands differs from it only in the throat exception below.`

**R3 (required: undefined is not failing).**
OLD: `It fails at every apastron except under *through* with $\varepsilon(r_0)>2\Delta\ell(r_0)$.`
NEW: `At every apastron it fails (a) or is undefined (under *stop* when the path meets the sphere, and at $\varepsilon=\Delta\ell$), except under *through* with $\varepsilon(r_0)>2\Delta\ell(r_0)$.`

**R4 (required: the example is not a beyond-landing).**
OLD: `- **Not every beyond-landing passes.** Example: $r_0=1000$, $v=0.0045$, $c=0.1$, where $\varepsilon<2\Delta\ell$, so the target lands inside at $189.87$ (apo-plunge) and fails.`
NEW: `- **Not every beyond-landing passes.** In S2 (§4), 6 of 352 beyond-landings fail, 3 of them with a change of type. A through-throat path can also land inside: at $r_0=1000$, $v=0.0045$, $c=0.1$, $\Delta\ell<\varepsilon<2\Delta\ell$, so the target lands inside at $189.87$ (the apastron of a plunging orbit) and fails.`

**N1 (optional: terms before §1).**
OLD: `Scripts and pins are in §5.*`
NEW: `Terms used before §1 (turning type, interior side, $\varepsilon$, $\Delta\ell$, $m$, *stop*, *through*) are defined there. Scripts and pins are in §5.*`

**N2 (optional: undefined symbols).**
OLD: `Then $p>6+2e$, so`
NEW: `Then $p>6+2e$, where $p$ is the semi-latus rectum and $e$ the eccentricity ($r_{p,a}=p/(1\pm e)$), so`
OLD: `near-circular ($\delta$ down to $10^{-40}$)`
NEW: `near-circular ($r_{p,a}=r_c(1\mp\delta)$, $\delta$ down to $10^{-40}$)`

**N3 (optional: the right bound per $c$).**
OLD: `That value lies below $705.155$ and $69{,}303.7$, so no reachable path reaches the throat and the result holds under either convention.`
NEW: `That value lies below $69{,}303.7$, the $c=0.01$ throat bound (C37), so no reachable path reaches the throat and the result holds under either convention. At $c=0.1$ the maximum apastron is $23.24<705.155$.`

**N4 (optional: pins at 12 digits).**
OLD: ``| `g201/census.py` | `97659775` |`` NEW: ``| `g201/census.py` | `97659775a495` |``
OLD: ``| `g201/r1.py` | `edd8c89b` |`` NEW: ``| `g201/r1.py` | `edd8c89b2216` |``

**N5 (optional: where the scripts are; the unnamed brief).**
OLD: `**Pins** (sha256, first 12 hex digits):`
NEW: `**Pins** (sha256, first 12 hex digits; the scripts are under `/workspace/` on the shared box, not in this repository):`
OLD: ``The brief's `g183/c33r.py` does not exist;``
NEW: ``The task brief (not in this repository) names `g183/c33r.py`, which does not exist;``

**N6 (optional: invocation).**
OLD: ``(`sample286.py`, seed 286, $N=20{,}000$ per scheme)``
NEW: ``(`sample286.py 20000 20000`, seed 286, $N=20{,}000$ per scheme; the script's default is 4,000)``

The same scope point applies to the PR body's "Apastra, where it is refuted" bullet: "the lemma fails" there should read "the lemma's unqualified form fails".

## Addendum (2026-10-11): fix pass on #290 and the #285 follow-on

**Heads read (re-checked before filing):**

| PR | from | to | state |
|---|---|---|---|
| #290 | `86e50c1` | `295ff19` | open, not merged |
| #285 | `0987418` | `fc42262` (commits `73fef02`, `0da7aa1`, `fc42262`) | open, not merged |

Main is `6fb1566`. I merged nothing and messaged no one.

### #290 (`86e50c1` → `295ff19`): PASS with notes

**Strings.** Every #291 string is applied:

- **R1–R4, N1, N2 (both), N3 and N6** match their NEW text exactly.
- **N4.** Both `g201` pins now have 12 digits (`97659775a495` and `edd8c89b2216`), under the repository names `census.py` and `r1.py`.
- **N5, first string.** It is replaced by a pin legend: "sha256 of the committed files … in [`turning-type-lemma-scripts/`](turning-type-lemma-scripts/) next to this note". This deviation is disclosed and sound, because the scripts are now in the repository and the link resolves.
- **N5, second string.** It matches exactly, followed by a disclosed sentence: the `g168/c33r.py` pointer is superseded by the committed `c33r.py`.
- **CKP citation.** "(Cutler, Kennefick & Poisson, Phys. Rev. D 50, 3816 (1994))" is verbatim and placed on the $p>6+2e$, $r_p>4$, $r_a>6$ sentence.
- **Headline.** It reads "the lemma holds as #203 states it, with the throat proviso, and extends up to $\varepsilon\le2\Delta\ell$. Only the unqualified form is refuted." That is accurate.
- **PR body.** It applies the PR-body scope note ("the lemma's unqualified form fails").

**Text outside the strings and the headline.** Four other lines changed. They are knock-ons of the R1 rescope, and the PR body covers them only as "the verdict is rescoped". All four are accurate:

- **Line 7.** It now reads: "Past the sphere the inward edge is undefined under the named alternative ("stop"); under the proposed default ("continue through") it still fails (a) up to $\varepsilon\le2\Delta\ell(r_0)$ ($\varepsilon=\Delta\ell$ excluded)." This agrees with (T2) and (T3).
- **Corollary heading.** "(the #203 lemma: the proviso form, extended)".
- **Counterexample heading.** "(to the unqualified form; the exception is real)".
- **Census pointer.** "`census.py` (with `r1.py`, both from the box's `g201`)".

Nothing else in the note changed (`git diff --word-diff`).

**Scripts** (`notes/turning-type-lemma-scripts/`, from a fresh clone at `295ff19`):

- **Hashes.** All 12 sha256 prefixes match the pin table.
- **Changes from the box originals.**
  - `tt.py`, `proof286.py`, `census.py`, `r1.py` and `kr.py` are byte-identical to `/workspace/g286`, `g201` and `g154`.
  - The five changed g286 files differ only in their import or path line: `throat286`, `boundary286`, `sample286`, `census286` and `censusf286`. The hard-coded `/workspace/...` path becomes the script's own directory.
  - `c33r.py` and `c33x.py` also differ from `g168`, only in path lines (two in `c33r.py`, one in `c33x.py`). The README discloses this ("path lines only"), although the PR's "five changed hashes" count covers only the g286 files.
- **Secrets and box paths.** A scan finds no `/workspace`, `/home`, token, key or password strings.
- **Outputs.** All 10 expected outputs reproduce. I ran each from `/tmp` and compared after removing run-time fields:
  - `proof286`, `throat286` and `boundary286`;
  - `sample286 20000 20000`;
  - `census286` at 0.1 and 0.01;
  - `censusf286` at 0.1, 0.01 and `0.001 22` (65 s; 8,254,910 orbits, 0 into-range passes, maximum apastron 20.7284);
  - `c33r 0.01`, which gives the exact C33 jump-count law.
- **One reproduction detail.** `censusf286.py` prints its BFS progress to stderr, and `expected/` holds stdout only. The outputs match exactly when stdout alone is compared (optional string S1).

**Guardrails.**

- χ, `\chi` and the other forbidden tokens: 0. The one new "signed" is "signed proper distance" in `tt.py`, a mathematical term.
- No Born, $|a|^2$ or 1/N claim.
- F11 stays open. The throat conventions keep v0.9.1's labels (proposed default and named alternative), and neither is recommended.
- v0.9.1 and Paper 1 are untouched.

### #285 (`0987418` → `fc42262`, `notes/v0.10-plan.md`): PASS with notes

The diff is two lines: item 1's table row and the "Next substantive physics question" paragraph. Nothing else changed.

- **Item 1.** It now carries "provided the jump does not reach the throat (#203's proviso; #290: holds in that form and extends up to $\varepsilon\le2\Delta\ell$; only the unqualified form is refuted)". This is accurate to #290 at `295ff19`. The row does not say that #290 is under review, while the paragraph below it does (optional P1).
- **C33 claims.** Both now name only $m\le1$: "C33's $m\le1$ … becomes a theorem, with the throat proviso, up to $\varepsilon\le2\Delta\ell$; transience and countability are not proved by it and still need their own argument" and "turns C33's $m\le1$ … from computed into proved". This matches #290 §5 on transience and countability. #290 §5 also notes that the theorem gives C33's $m\le1$ only together with one computed fact, the maximum apastron 25.37. "From computed into proved" leaves that out (optional P2).
- **Risk cell.** The pre-existing cell "Low (0 of >19,000 edges pass)" is unchanged. It is now dated, because 8,244 sampled beyond-landings pass under *through*. I flag it only and give no string, since it is outside this diff.
- **F11 and guardrails.** No F11 pick: "stays a Lead/David call (#230 F11)" is unchanged. No forbidden tokens; no Born, $|a|^2$ or 1/N claim; nothing recorded as signed.

### Strings (all optional; each OLD occurs once at the head named)

**S1** (#290, `notes/turning-type-lemma-scripts/README.md`)
OLD: ``The expected outputs are in `expected/`; lines that report a run time in seconds will differ.``
NEW: ``The expected outputs in `expected/` are stdout only (`censusf286.py` prints its BFS progress to stderr); lines that report a run time in seconds will differ.``

**P1** (#285, `notes/v0.10-plan.md`)
OLD: `(#203's proviso; #290: holds in that form`
NEW: `(#203's proviso; #290, under review: holds in that form`

**P2** (#285)
OLD: `from computed into proved.`
NEW: `from computed into proved, given one computed C33 fact (the maximum apastron, #290 §5).`
