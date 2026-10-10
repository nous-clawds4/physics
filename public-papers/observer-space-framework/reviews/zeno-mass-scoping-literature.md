# Literature check: Zeno-mass scoping note (#244)

**Verdict: HOLD (narrow).** One claim needs correcting: (Z-v) "forces" $1/2$ only under per-vertex weights. Everything else checks. **Heads read:** #244 head `9707017` (`notes/zeno-mass-scoping.md`, 1,083 words); main `e493913` (`versions/v0.9-prose.md`). I re-checked the head before filing.

## Findings

- **F1 (required): the (Z-v) row and the (Z-v) cost line.** Counts along depth cuts never use $\tau$, so moving the vertex times does not change them. On C35's toy they give $1/(1+2^k)\to0$ under both timings: $1-2^{-k}$ and $k$. So $\tau$-blindness gives $1/2$ only once the weights are per-vertex. With counts it gives (Z-iv)'s $0$. As written, the row reads as a third independent route to $1/2$, which leans toward (Z-ii). Strings 1 and 2 fix this.
- **F2: the numbers check.** C35 gives (Z-ii) $1/2$ and (Z-iii) $(1/2-0)/(1-1/2)=1$. V0 ($z=0$) gives (Z-iii) $1/2$. V1 ($z=1$) gives $0/0$. Counts are $1/3, 1/5, \dots, 1/1025$ at $k=10$, with limit $0$. Retimed to $\tau=k$, $X$ gets $1/2$ under (Z-i) and (Z-iii). C7 is $\min_r \pi\sqrt{r^3(r-3)/(r-6)}=111.5901853$ at $r_0=5+\sqrt7=7.64575131$. I integrated the eccentric half-periods independently: $112.471$, $127.722$ and $212.567$. All match.
- **F3: the record checks.** The following match the note:
  - §8.2 item 8 and §8.3 (three readings, none picked), and §8.3 naming (Z-i)–(Z-iii).
  - Cells C35, C8 and C15.
  - #229 N8.
  - The Geometry v0.7-outline F2/RC2 (its RC2 notes the defect was in the #155 wording).
  - Row 10 of Claude's v0.7 review.
  - `born-rule-readiness.md` §3 item 4 and `law-of-R-scoping.md` K6.
  - The C16 and C33 values.
- **F4: Kallenberg.** v0.9 cites the 3rd ed. (2021, doi:10.1007/978-3-030-61871-1). Mathlib's `Probability/Kernel/IonescuTulcea/Traj.lean` says it follows "the proof of Theorem 8.24 in Kallenberg, Foundations of Modern Probability", with its bib entry set to the Third Edition, 2021. So in that edition 8.24 is the Ionescu-Tulcea extension theorem. That is enough for an existence citation. I verified this second-hand, without reading the book. The 2nd ed. (2002) numbers it differently, so the bare "Kallenberg 8.24" should name the edition and say "Theorem" (string 3). The note uses no "Lemma".
- **F5: "(R3)" is unexplained.** By context it is #229's R3: on cofinal cuts, constancy is not sufficient for the count limit. String 4 is optional.
- **F6: scoping.** There is no pick, ranking, "natural", "preferred" or "best". The (c) table maps the readings onto (M1)/(M2), T1–T3, #139 and #230 without choosing among them. (Z-iv) endorses neither per-vertex nor counts. There is no pedigree statement. Critic Q3 already raises the question-begging concern about (Z-v). Once F1 is fixed, the (d) cost lines are symmetric enough.
- **F7: the critic questions.** All five are well-posed, answerable and not loaded, and they match the body. After F1, Q3's answer includes the point that counts along depth cuts are also tree-only.
- **F8: guardrails.** The note has no Born rule, $|a|^2$ or $1/N$ result, no law of R, no Everett-vs-Deutsch–Wallace framing and no Bell claim. It contains no banned words. Paper 1 is untouched, and so is everything else in `versions/` and `papers/`.

## OLD/NEW (file `public-papers/observer-space-framework/notes/zeno-mass-scoping.md`; each OLD occurs once)

1. (required) OLD: `It forces the per-vertex value $1/2$, which is (Z-ii)'s.`
   NEW: `Under per-vertex weights it forces $1/2$, which is (Z-ii)'s; counts along depth cuts are also unchanged by such moves and give (Z-iv)'s $0$.`
2. (required) OLD: `One lemma: per-vertex weights depend only on the tree. Stating it fixes a value, which is a choice in itself.`
   NEW: `One lemma: per-vertex weights, and counts along depth cuts, depend only on the tree. Stating it fixes a value once the weight type is fixed ($1/2$ per-vertex, $0$ for counts), which is a choice in itself.`
3. (recommended) OLD: `(Ionescu-Tulcea, Kallenberg 8.24, already referenced)`
   NEW: `(Ionescu-Tulcea; Kallenberg 2021, 3rd ed., Theorem 8.24, already referenced)`
4. (optional) OLD: `it can fail to converge (R3).`
   NEW: `it can fail to converge (#229 R3).`

I applied all four mechanically. Each matches once, and the result is 1,118 words (1,083 before).
