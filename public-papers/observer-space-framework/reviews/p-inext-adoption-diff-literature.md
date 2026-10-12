# Literature diff check: P-inext adoption (#328)

**Reviewer:** Literature. **Date:** 2026-10-11/12. **Record type:** review record. It applies nothing. Do not merge until the Lead says so.

**Scope.** Diff only: #328 head `0bb8c2d` against its base `07e060d`. main is now `7292f22`, which differs from `07e060d` only by `reviews/inextendible-ensemble-literature.md` (#323), so there is no overlap with #328.

**Existing reviews.** None of #328.

**Verdict: PASS with notes**, conditional on one string. The gap-1 string G1 below should land in #328, because it is the same theorem.

## 1. Quotes, labels and the L3 record

- **Both David quotes are byte-identical** to the parent's relay:
  - 11:54 PM ET: "Let's go ahead and adopt it."
  - 11:52 PM ET: "I'm inclined to adopt it, unless there's some blocking reason that I'm not thinking of".
- **Labels.** Each quote is tagged "(relayed, not signed)". "signed" appears only in "not signed".
- **L3.** The adoption is recorded as "**adopted at L3** (strong opinion, weakly held)". The original request line (10:44–10:48 PM, relayed, not signed) is kept. So is the attribution "P-inext's wording and everything below are Geometry's, not David's".
- **Provenance.** "Written at main `dc8d374`; adoption recorded at main `07e060d`." Correct.

## 2. Status line: open items

The Status line names exactly two open items, both "not ruled":
- **Critic question 2's (H)/(F)** choice for $E_M$ (§5, §6).
- **The time-orientability class mismatch.** The note says "`ensemble-labels.md` §1 assumes time-orientable, §4 does not". §1's standing assumption does say "time-orientable" (line 28). It is marked "on which Physics Lead is not ruling tonight".

The scope sentence ("the adoption edit changes only `papers/ensemble-labels.md` Theorem 4(1)") matches the diff, provided G1 is read as part of Theorem 4(1) (see §5).

## 3. Theorem 4(1) knock-on row

The row is marked "fixed by the adoption edit". Its description of the new hypothesis matches the applied text word for word ("the $W$-geodesic from $\iota(p)$ with initial velocity $\iota_*u$ is defined").

## 4. The five OLD strings, and nothing else

The diff touches two files and three lines, with five replaced spans:
- `ensemble-labels.md`: the hypothesis insertion and the tail ("and the $W$-geodesic is defined").
- The note: the Status opening, the "Written at … Bare" provenance span, and the Theorem 4(1) row status.

Each OLD occurs once at `07e060d`:
- `in $P(O)$, the same $W$ contains`: 1
- `constant along $\gamma_O$ while $\sigma_O$ remains in $P(O)$.`: 1
- `proposal for David's decision; **not adopted**`: 1
- ``Written at main `dc8d374`. Bare``: 1
- `open: needs a hypothesis whatever David decides; not edited here`: 1

Nothing else changed:
- Theorem 4(2)–(4), the proofs and the rest of both files are byte-identical.
- No `versions/` file and no Paper 1 file is touched.

**Guardrails.** All clean:
- 0 of the forbidden Greek letter.
- No Born, $|a|^2$ or 1/N result, no Everett-versus-DW framing, and no law of $R$.
- No pick on (T0)–(T4), the throat convention, (M1) or (A).
- The note is 1,810 words.

## 5. Ruling on gap 1: fix in #328 (yes)

**The problem.** The proof of (1) still ends "so $\iota$ extends along that segment and $W$ contains every $O_\tau$". Against the new hypothesis, that over-claims: for C24's host, $W$ does not contain $O_\tau$ past the hole. So the proof now proves more than the statement and is false as written.

**The fix.** It is a one-clause repair in the same theorem, so it belongs in #328. The PR body's "The proof of (1) is not edited" should then be dropped.

**G1 (required)**, in `papers/ensemble-labels.md`. OLD occurs once at `0bb8c2d`:

OLD: `so $\iota$ extends along that segment and $W$ contains every $O_\tau$.`
NEW: `so $\iota$ extends along that segment for as long as the $W$-geodesic from $\iota(p)$ with initial velocity $\iota_*u$ is defined, and $W$ contains $O_\tau$ for every such $\tau$.`

## 6. Gaps 2 and 3 (deferred): accurate, and deferral is fine

**Gap 2.** `versions/v0.10.1-prose.md` line 173 still reads "Whether $E_{\mathcal W}$ should be restricted to inextendible or maximal members is open." After the L3 adoption this is stale.
- Confirmed.
- Deferral is fine. #328 edits no `versions/` file, and the version text is frozen until the next version pass.

**Gap 3.** Two places still show the old wording:
- Note §6, critic question 2 (line 60), still asks "Should `ensemble-labels.md` Theorem 4(1) be restated with "while the $W$-geodesic exists"…".
- `reviews/inextendible-ensemble-literature.md` (#323, now on main) lines 78 and 80 quote the pre-#328 theorem and proof.

Both confirmed. Deferral is fine:
- The #323 quotes are historical records of the text at `9ccbfbc`, so they should not be edited.
- The (H)/(F) half of question 2 stays open in any case.
- Optionally, a later pass can mark the Theorem 4(1) half "answered by #328".
