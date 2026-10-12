# Literature claim check: `notes/inextendible-ensemble.md` (#320)

**Reviewer:** Literature. **Date:** 2026-10-11. **Record type:** review record. It applies nothing. Do not merge until the Lead says so.

**Heads read, re-checked before filing:**
- #320 head `9ccbfbc`, open, written at `dc8d374`.
- main `85f385d`. Since `dc8d374`, these have merged:
  - #319 (`notes/turning-type-lemma.md`, which the note does not cite);
  - #317 and #321 (v0.10.1 prose, changelog and README, and the Literature panel);
  - #322 (queue).

  None of them touches a file the note cites: v0.10 is still `20b73d791c46…`, and C24 and C25 are unchanged. v0.10.1 carries C24, C25 and the quoted §4, §5 and §6.1 text byte-identical, so the readings below also hold there.

**Existing reviews.** I found no existing review of #320, and no file `reviews/inextendible-ensemble*`.

**Rules.** I pick no topology ((T0)–(T4)), no throat convention, no law of $R$, and nothing on (M1) or (A). I decide nothing on P-inext, and I message no one.

**Verification marks:**
- **V-text:** checked against the source's own text.
- **V-meta:** checked only against an abstract or a secondary source.

**Verdict: HOLD (narrow).** One mathematical overstatement must be fixed (R1, κ-Kruskal "at any $\tau_0$"). Everything else passes, with suggested strings (S1–S4) and nits (N1–N6). Attribution, neutrality and the guardrails are clean.

## 1. Literature

**Misner 1967.** "Taub-NUT space as a counterexample to almost anything", in *Relativity Theory and Astrophysics I* (ed. J. Ehlers), *Lectures in Applied Mathematics* 8, AMS, 160–169.
- **The citation** is correct: title, editor, series, volume and pages, confirmed via INSPIRE and Hawking–Ellis's citation.
- **The text** (**V-text**, read in NASA CR-70033, the 1965 Maryland technical report of the same title, which the chapter publishes). Point 5 of Misner's list is "the non-uniqueness of analytic continuation for metrics". He says it occupies the rest of the talk.
  - He gives "one maximal analytic extension of Taub space".
  - He writes "To exhibit non-uniqueness we first introduce a new coordinate system".
  - He then gives, for a 2-dimensional model on the cylinder (his Eq. (32)), "an inequivalent analytic extension".
  - So the note's "discusses non-uniqueness" is accurate.
- **Caveats.**
  - I read the report, not the AMS chapter, so any differences between the two are unchecked.
  - Chruściel & Isenberg (abstract) show that "many of the familiar extensions are isometric". So Misner's "inequivalent" extensions are not, on their own, non-isometric hosts. The note does not claim they are. S1 adds a clause.

**Chruściel & Isenberg 1993.** *Phys. Rev. D* 48, 1616–1628, doi:10.1103/PhysRevD.48.1616, "Nonisometric vacuum extensions of vacuum maximal globally hyperbolic spacetimes".
- **The citation** is correct. The pages are 1616–1628.
- **The full text** is not reachable. The author's PDF link (homepage.univie.ac.at/…/Chrusciel_isenberg_prd.pdf) returns 404, there is no archived copy, and there is no arXiv version (it was a Garching preprint, MPA 727). So I mark it **V-meta**.
- **What the abstract (APS) says:** "in the Taub and Gowdy families there are nonisometric maximal extensions … in the latter family … an arbitrarily large number". The note's "non-isometric maximal extensions in the Taub family (checked at abstract level)" is therefore accurate and honestly marked.
- **What a secondary survey says** (Doboszewski 2017, "Non-uniquely extendible maximal globally hyperbolic spacetimes in classical general relativity", §11.2–11.3, which cites the paper):
  - the Taub non-isometric pair is built by gluing a past and a future NUT extension;
  - "In case of Taub-NUT and polarised Gowdy, extensions are analytic".
  - This bears directly on P-inext's class, so S1 records it, also as **V-meta**.
- **Equivalence relation.** C–I's non-isometric extensions are inequivalent under any isometry. That includes `ensemble-labels.md` Def. 2's pointed isometries, so they are inequivalent members there too. The note's use is sound.

**Added citation (S2), V-text.** Geroch, "Spinor structure of space-times in general relativity. I", *J. Math. Phys.* 9, 1739 (1968), Appendix:
- "Theorem: Let M be a (connected, Hausdorff) 4-manifold with a $C^\infty$ metric of signature (+,−,−,−). Then the topology of M has a countable basis."
- Footnote 34: "Every n-manifold with a $C^1$ connection has a countable basis."

This supplies the step that §3 item 4 marks "owed". The union of a chain of open embeddings is connected, because every member contains $P(O)$. It is Hausdorff, as the note says. It carries an analytic Lorentzian metric. So it is second countable. Zorn's set-theoretic bookkeeping (chains of isomorphism classes) is standard and not checked here.

## 2. The record

**Readings of C24 and C25** (v0.10, Appendix A). Both rows are byte-identical in v0.9.1, so every reading below holds for v0.9.1 too.
- **C24.** The quote "Minkowski minus the point $\sigma(\tau_0)$: the geodesic ends at $\tau_0$, for every $\tau_0\in(0,\infty)$" is exact. The knock-on row's other quote, "as written, with no inextendibility requirement", is from §6.1's continuum theorem. C24's own claim reads "under §4's ensemble as written (§6.1)" (N1).
  - The reading is right: C24 stays true, and its host leaves the restricted ensemble.
- **C25.**
  - "inextendible, by a sketch" is exact.
  - "names no regularity class" is true.
  - The holonomy argument controls extensions whose connection extends continuously, which covers $C^2$ and analytic extensions.
  - "$\rho_0/\sinh\zeta$" is exact.
  - "Inextendibility alone does not restore discreteness" is C25's claim, and the note keeps it.
- **Other quotes:**
  - §4's "Whether $E_{\mathcal W}$ should be restricted to inextendible or maximal members is open." is exact.
  - §5's "punching holes makes lifetimes arbitrary" is exact.
  - §4's "is at least a continuum" rests on "the continuum theorem of §6.1", as the note says.
  - §4's spacetime is "a connected real-analytic Lorentzian 4-manifold". `ensemble-labels.md` §1 adds Hausdorff, second-countable and time-orientable. So the "small mismatch" is real.
- **Regularity direction.** $C^0$-inextendible ⇒ $C^2$-inextendible ⇒ analytically inextendible is correct, since an analytic extension is a $C^2$ one. So "analytic is the weakest requirement" is right.
- **Throat row.**
  - #297 §2 item 2 is quoted faithfully ("any analytic world containing a neighbourhood of the path gives the same germ").
  - The "sphere punched out" text is a remark in #297 §3's completed-world row, not a row of its own (N3).
  - $X\mapsto-X$ fixes $\partial_T$ and $e_\varphi$, and the one-exterior quotient's inextendibility is marked unchecked. Both are fine.
- **C8 pointer.** C8 is the No-Zeno row. Its FLRW instance shows a curvelet ending at a curvature blow-up, but it does not state the general sentence (N2).

## 3. The `ensemble-labels.md` Theorem 4(1) finding

**The theorem's text:** "If $[W,\iota]\in E_\gamma(O)$, then for every $\tau$ in the interior of the lifetime of $\sigma_O$ in $P(O)$, the same $W$ contains $O_\tau$ (the jet of $g_W$ at $\sigma_O(\tau)$)."

**The proof:** "analytic continuation along $\sigma_O$ inside $P(O)$ is unique, so $\iota$ extends along that segment and $W$ contains every $O_\tau$".

**The gap.** Uniqueness of continuation does not give existence in $W$. The step needs the $W$-geodesic from $\iota(p)$ to exist for every such $\tau$, which is what the note means by "$W$ contains the image of $\sigma_O$".

**The note's finding is confirmed, and it is slightly stronger than a proof gap.** C24's host contradicts the *statement*:
- Take Minkowski minus $\sigma(\tau_0)$, with $\tau_0$ inside the short segment.
- It is in $E_\gamma(O)$.
- It lacks "the jet of $g_W$ at $\sigma_O(\tau)$" for $\tau\ge\tau_0$, because that point is not in $W$.

The flat germ occurs elsewhere in that host, but the theorem's parenthetical fixes the point. So the theorem needs a hypothesis, as the note's table says ("open: needs a hypothesis whatever David decides"), and the PR body's "proof gap" undersells it. (2) and (3) are unaffected. The note edits nothing in `papers/`, which is right. S4 sharpens the row.

## 4. The sketches

**C25 and κ-Kruskal are labelled.** "A curved case, a sketch at C25's level" is clear, and so is critic question 1.
- **The holonomy claim.** On $d\theta^2+\kappa^2\sin^2\theta\,d\varphi^2$, transport around the latitude circle rotates by $2\pi(1-\kappa\cos\theta)$, which tends to $2\pi(1-\kappa)\ne0$. That is correct.
- **One overstatement (R1).** Rescaling $d\varphi$ makes *both* poles conical, so the axis is the two rays $\theta=0,\pi$.
  - A Schwarzschild orbit developed into κ-Kruskal runs along a meridian.
  - It meets one of the two poles after sweeping an angle $\theta_0$ or $\pi-\theta_0$ (where $\theta_0$ is the pole's colatitude from $\sigma(0)$). Both are below $\pi$.
  - If the orbit sweeps more than $\pi$ by $\tau_0$, then putting the pole at $\sigma(\tau_0)$ puts the antipodal pole at a point the orbit reaches earlier, so the geodesic ends there.
  - So the construction gives ending times only where the swept angle is below $\pi$. That set is still a continuum, so the (H) answer stands. But "any $\tau_0$ in its Kruskal lifetime" and "at any $\tau_0$" are false as written.
- **Also.** "Kruskal is maximal elsewhere" does not by itself make κ-Kruskal inextendible, since κ-Kruskal is not an open subset of Kruskal. It is part of the sketch, and S3 carries "by sketch" into the Answer.

**Branched double cover.** It is labelled "sketch, not pinned", and inextendibility is "plausibly". The (F) bullet and the Answer ("plausibly … (sketch above)") do not overstate it.
- A double cover of $N\setminus\Sigma$ that is nontrivial on the linking loop needs a homomorphism $H_1(N\setminus\Sigma)\to\mathbb Z/2$ that sends the loop to $1$. "Generates a $\mathbb Z$" is not enough on its own (N4).
- Germs of $W$ are germs of $N\setminus\Sigma$ (local isometry), so "drops out exactly at $\tau_0$" follows under the stated single-occurrence hypothesis.
- **Persistent loss** is marked "owed", and the pointer to Taub–NUT-type non-unique continuation agrees with Misner and with C–I.

## 5. Attribution and neutrality

- **Attribution.** David's request is tagged "Requested by David in Geometry's chat, 10:44–10:48 PM ET on 2026-10-11 (relayed, not signed)". No words are quoted as David's, and nothing is recorded as signed. N6 adds that P-inext's wording is Geometry's.
- **Neutrality.**
  - The Status says "proposal for David's decision; **not adopted**".
  - "Adoption should fix one class" and "If adopted …" leave the choice open.
  - The class argument (analytic fits the lock, and is the weakest requirement) is a reason, not a pick.
  - (H) and (F) are put to David as a question (critic question 2).
  - The table's "settled" means that the analysis has no open question. A reader could take it as a decision, and N5 adds a one-word key.
  - Nothing is picked on (T0)–(T4), #315, the throat, the law of $R$, (M1) or (A).
- **Guardrails.**
  - The forbidden Greek letter and its TeX macro: 0 in the note. The PR body's last line contains the letter itself ("No …"), but that is not a file.
  - There is no Born, $|a|^2$ or 1/N result, no Everett-versus-Deutsch–Wallace framing, and no law of $R$.
  - Paper 1, `papers/` and `versions/` are untouched. The PR adds one file, 1,516 words.

## 6. Strings (each OLD occurs once in `notes/inextendible-ensemble.md` at `9ccbfbc`)

**R1 (required; κ-Kruskal times)**

OLD: `and any $\tau_0$ in its Kruskal lifetime.`
NEW: `and any $\tau_0$ in its Kruskal lifetime by which its orbit has swept an angle less than $\pi$ (both poles are conical, so the geodesic meets one of them once its swept angle reaches that pole's angular distance from $\sigma(0)$, which is below $\pi$).`

OLD: `disagree on the lifetime, at any $\tau_0$,`
NEW: `disagree on the lifetime, at every such $\tau_0$ (a continuum),`

**S1 (suggested; literature levels)**

OLD: `discusses non-uniqueness`
NEW: `discusses non-uniqueness of analytic continuation for metrics and gives an inequivalent analytic extension (text checked in NASA CR-70033, the 1965 report the chapter publishes; Chruściel & Isenberg note that many such familiar extensions are in fact isometric)`

OLD: `give non-isometric maximal extensions in the Taub family (checked at abstract level).`
NEW: `give non-isometric maximal extensions in the Taub family (checked at abstract level; that these extensions are analytic, and so within P-inext's class, is from a secondary survey, Doboszewski 2017, not from the paper's text).`

**S2 (suggested; the owed citation)**

OLD: `Second-countability of the union is the step for which a citation is owed for the analytic case; it is not checked here.`
NEW: `Second-countability of the union follows from Geroch's theorem (J. Math. Phys. 9, 1739 (1968), Appendix: a connected Hausdorff manifold with a $C^1$ connection has a countable basis), since the union is connected and carries an analytic Lorentzian metric.`

**S3 (suggested; Answer)**

OLD: `C25 flat, κ-Kruskal curved.`
NEW: `C25 flat, κ-Kruskal curved, each inextendible by sketch.`

**S4 (suggested; Theorem 4(1) row)**

OLD: `The proof step "$\iota$ extends along that segment" assumes $W$ contains the image of $\sigma_O$.`
NEW: `The proof step "$\iota$ extends along that segment" assumes that the $W$-geodesic from $\iota(p)$ exists for every such $\tau$; C24's host contradicts the statement itself, not only the proof.`

**N1 (C24 quote source)**

OLD: `(it is about §4's ensemble "as written, with no inextendibility requirement")`
NEW: `(it is about §4's ensemble "as written"; §6.1's continuum theorem adds "with no inextendibility requirement")`

**N2 (C8 pointer)**

OLD: `end the curvelet's maximal analytic domain itself (C8)`
NEW: `end the curvelet's maximal analytic domain itself (C8's FLRW instance is one case)`

**N3 (#297 §3)**

OLD: `P-inext removes #297 §3's "sphere punched out" row.`
NEW: `P-inext removes the punched-sphere world that #297 §3's completed-world row sets aside ("A world with the sphere punched out lacks the path").`

**N4 (branched cover)**

OLD: `whose linking loop generates a $\mathbb Z$ in $H_1(N\setminus\Sigma)$`
NEW: `whose linking loop is sent to $1$ by some homomorphism $H_1(N\setminus\Sigma)\to\mathbb Z/2$`

**N5 (neutrality key)**

OLD: `| Item | Under P-inext | Status |`
NEW: `| Item | Under P-inext | Status (of the analysis, not a decision) |`

**N6 (attribution)**

OLD: `(relayed, not signed). Written at main`
NEW: `(relayed, not signed); P-inext's wording and everything below are Geometry's, not David's. Written at main`

## Report line

Literature on #320 at `9ccbfbc`: **HOLD (narrow)**.
- **R1:** κ-Kruskal ends the geodesic only at times before the orbit sweeps an angle $\pi$, because both poles are conical. That is still a continuum, so the (H) answer stands.
- **Literature:**
  - Misner is V-text (via the 1965 report): non-uniqueness of analytic continuation, with an inequivalent analytic extension.
  - Chruściel–Isenberg is V-meta (abstract; the full text is unreachable), and the note's use is accurate. Analyticity is also V-meta (secondary).
  - Geroch 1968 (V-text) discharges the owed second-countability step.
- **Theorem 4(1):** the finding is confirmed, and C24's host contradicts the statement, not only the proof.
- **Record:** the C24 and C25 readings are correct for v0.10 and v0.9.1.
- **Attribution and neutrality:** clean.
- **Guardrails:** clean.
