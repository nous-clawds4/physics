# Creative batch 13: outcome = branch, and who survives (Creative Lead; proposal, do not merge)

**Verdicts applied:** Literature #371 (S1–S6), Geometry #370.

**Status.** Exploration only, under David's 3:14 PM ruling, his 3:53 PM memory working assumption, his 4:16 PM geon-host approval and his 4:17 PM hypothesis. Main line (David, 4:28 PM ET, relayed by Physics Lead, Physics Lead chat, not signed; ledger): "No, I like the original idea of the signal sent out by the observer. I can wrap my head around that." and "a fork in the observer's future (a branch in observer space) is exactly what we are looking for." So the signal round trip stays the main line, with no observer-through-the-loop set. Structure only: no probabilities. Nothing goes into `versions/` or `papers/`. Citations are **unchecked** unless verified by #362, #364, #365, #367 or #368. Everything is a sketch.

## For David (one minute)

**Is the measurement result the same as the branch?** Almost. With memory in the observer's state, what the observer has recorded and where it is never contradict each other. The two notions nest neatly. At any finite time, though, one recorded result can still cover several possible worlds that haven't yet revealed their differences, much as one echo can come from several universes that only differ further out. As time goes on and more echoes arrive, the result narrows toward a single branch. In the simplest cases (3D crystals, exact directions) it gets there in finite time. We could simply *define* a branch as "what has been recorded", which makes "result = branch" automatic. That is a fine bookkeeping choice, but it proves nothing, so we keep both notions. **Who survives past the horizon?** In the textbook examples, which continuation an observer gets through is fixed by its own motion (for example, which way it is circling). So surviving is not a fork. The fork is in *which world*, and given the world, survival is determined. Observers that look trapped in one Taub–NUT continuation get through in the other; only a negligible special set gets through neither. For Hadley's geons this is not yet worked out. A geon that has always existed has no "before" to compare from, but worlds can still be compared through the observer's state and diary.

---

## (A) Outcome = branch in the germ+record state

**Definitions** (a host $W$ compatible with $\hat O(0)$; L29).
- **State history** to $\tau$: $\hat O_W|_{[0,\tau]}=(O_W(t),\rho_W(t))_{t\le\tau}$.
- **State branch at $\tau$:** $[W]^{S}_\tau=\{W': \hat O_{W'}|_{[0,\tau]}=\hat O_W|_{[0,\tau]}\}$.
- **Record class (outcome) at $\tau$:** $[W]^{R}_\tau=\{W':\rho_{W'}|_{[0,\tau]}=\rho_W|_{[0,\tau]}\}$.
- **Full branch:** $[W]^S_\infty=\bigcap_\tau[W]^S_\tau$, i.e. hosts with identical state histories for all time.

**Facts (sketch; Geometry's answer, made precise).**
1. **Nesting, no crossing.** $[W]^S_\tau\subseteq[W]^R_\tau$, because the state includes the record. So the record and state partitions nest. In the augmented state, #367's case (d) (same germ, different reply) is a *state* difference and no longer crosses anything.
2. **The outcome is coarser than the branch at finite $\tau$.**
   - $[W]^R_\tau$ can contain several full branches: hosts with different Γ, or different off-path geometry, that share germ and record up to $\tau$.
   - Examples: #355 (shared short elements); #359 ($\mathbb Z^3$ rank 2: 9, 19, 29 worlds with share 1 before full rank). Under the analytic lock the open data are Γ and the extension (#370).
   - So **the outcome at $\tau$ is an equivalence class of branches**.
3. **Refinement.** $[W]^R_{\tau'}\subseteq[W]^R_\tau$ for $\tau'>\tau$: outcomes refine monotonically toward the full branch.
   - **Broadened (#370).** For any **cocompact** Γ in a known cover with exact displacement records, Γ is fixed, and certifiably so, once $\tau$ exceeds the displacements of a generating set and about twice the quotient diameter. This fails for non-cocompact Γ and for angle-only records. Homogeneous covers need care (the stabiliser). The $n\le3$ crystal case (#359) is a special instance.
   - **Corrected (#370).** Under the analytic lock, the germ fixes the cover everywhere already at $\tau=0$, except past points of non-unique extension. What stays open is Γ and the extension. "Off-path geometry is never fixed" holds only in the **smooth** case, outside the causal past.

**Should "branch" be redefined at finite $\tau$ as the record class?**
- L29 already used that rule ("same branch at τ iff records match up to τ"). Under it, **outcome = branch holds by definition**.
- **Tautology or cheat?** It is a tautology, and as a convention it is acceptable. The record rule was fixed in batch 08, before this question, from David's 3:53 memory ruling, so it was not tuned to this target. It would be a **cheat** under the litmus prior-inputs test (LT2) if offered as *evidence* that measurement outcomes are branches.
- It also hides the substantive question: can the germ diverge while the record does not (a branch without outcome; batch 12 (2)(a))?
- **Prior art (#371).** Closest is Belnap 1992 (outcomes = classes of not-yet-split histories). Gell-Mann–Hartle, Zurek and Wallace are cited as prior art only, not as framing.
- **Recommendation.** Keep both named: **record branch** (= outcome, by definition) and **state branch** (germ+record). Report claims about their relation as facts 1–3, not as a definition.

## (B) Observer survival beyond Misner

**Misner (Geometry's computation, #367; not a verified source).** In each extension, timelike observers crossing the horizon are exactly those with one sign of winding. Survival is **determined by the observer's own data** given the extension, so it is not a fork.

**Taub–NUT (sketch; Misner 1967 "counterexample to almost anything", Hawking–Ellis §5.8; unchecked).**
- The Taub region has a compact $S^3$ Cauchy horizon with closed null generators.
- There are two inequivalent analytic extensions (the two NUT regions).
- The Misner-like dichotomy is expected: geodesics cross into a given extension according to the sign of a conserved quantity along the Hopf-fibre direction.
- **In addition**, within each extension, the geodesics of the other sign are **imprisoned**: they spiral toward the horizon in a compact set and are incomplete there, but they cross in the other extension (the non-Hausdorff union is **not** complete: the comoving zero-momentum geodesics continue in neither extension (Misner–Taub 1969 §II C, relayed from external review, V-meta; confirmed by computation, #377), so no union of the two is complete; the reported completeness of a non-Hausdorff maximal extension, Hájíček 1971, is unchecked; corrected per #375 and Claude job 013 R5). Only a measure-zero zero-momentum set is incomplete in both.
- *Correction note (per #375 and Claude job 013 R5, as worded in #372 OP13):* Taub–NUT has no boost fixed point, but its comoving (zero-momentum) geodesics play that role: they continue in neither extension (Misner–Taub 1969, §II C, relayed from external review, V-meta; confirmed by computation, #377), so they stay incomplete in any union of the two extensions. An earlier version of this batch said the non-Hausdorff union is geodesically complete; that overstated it.
- Non-isometry of the Taub–NUT extensions is verified (#332). The dichotomy is **unverified** (Misner–Taub 1969, unchecked).

**Compactly generated Cauchy horizons (sketch; Hawking 1992 chronology protection; unchecked).**
- These horizons contain closed or past-imprisoned null generators (Hawking 1992). Non-unique extension beyond them is the **general Cauchy-horizon fact**, not Hawking 1992's result (#371).
- For analytic extensions, the germ at a crossing fixes the extension locally. So **given an extension, whether a geodesic crosses is a function of its data**.
- Across extensions it varies. Survival is therefore a function of (extension, observer data): **determined within each world**, varying between worlds.
- That fits "branch A = world A". Dropout is not an arm (v0.10.1 §6.2). **Non-existence of an extension** for a geodesic is likewise dropout, not an arm (#370).

**Hadley-type geon hosts (open).**
- If a geon *forms* (CTCs appearing after a globally hyperbolic era), its chronology horizon is compactly generated. The observer must cross it to receive a reply (#364 (d)), and the analysis above applies (unchecked).
- If the geon is **eternal** (Hadley 2000's $S^2\times\mathbb R$ world tube, V-text per #362, with CTCs for all time), there is **no Cauchy surface** $S$ (any spacetime with CTCs is not globally hyperbolic, and no achronal slice can pass through the chronology-violating region; non-time-orientability is a further obstruction). **Comparison still works (#370).** $E_{\mathcal W}$ and $E_M$ are defined by germs, so the anchor is germ + record. Only #346's agreement-region argument and #364 (d)'s timing claim need $D(S)$, and those must be restated for eternal geons.

**Answer (B).** In all the cases checked, survival is determined by the observer's own data within each extension. What varies is the extension, i.e. the world. In Taub–NUT, as in Misner, imprisonment is relative to the extension; only a measure-zero set survives in none. Hadley hosts are open. Eternal geons have no Cauchy surface, but the germ+record comparison still applies (#370).

## Weak points

1. (A) rests on the L29 record model, including #355's caveats (beacon switch-on, exact reals).
2. Under the lock, only Γ and the extension stay open (#370). Smooth off-path geometry outside the causal past is never fixed.
3. The Taub–NUT dichotomy is unverified (Misner–Taub 1969). Non-isometry is verified (#332), and relative imprisonment is per #371.
4. Hawking 1992 is from memory. Non-unique extension is the general Cauchy-horizon fact (#371).
5. Hadley hosts: survival is unanalysed. Eternal geons have no Cauchy surface (#371), so #346 and #364 (d) timing must be restated (#370).
6. The record-class redefinition must not be used as evidence (LT2).
