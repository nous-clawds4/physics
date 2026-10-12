# Creative batch 13: outcome = branch, and who survives (Creative Lead; proposal, do not merge)

**Status.** Exploration only, under David's 3:14 PM ruling, his 3:53 PM memory working assumption, his 4:16 PM geon-host approval and his 4:17 PM hypothesis. Main line (David, 4:28 PM ET, relayed by Physics Lead, Physics Lead chat, not signed; ledger): "No, I like the original idea of the signal sent out by the observer. I can wrap my head around that." and "a fork in the observer's future (a branch in observer space) is exactly what we are looking for." So the signal round trip stays the main line, with no observer-through-the-loop set. Structure only: no probabilities. Nothing goes into `versions/` or `papers/`. Citations are **unchecked** unless verified by #362, #364, #365, #367 or #368. Everything is a sketch.

## For David (one minute)

**Is the measurement result the same as the branch?** Almost. With memory in the observer's state, what the observer has recorded and where it is never contradict each other. The two notions nest neatly. At any finite time, though, one recorded result can still cover several possible worlds that haven't yet revealed their differences, much as one echo can come from several universes that only differ further out. As time goes on and more echoes arrive, the result narrows toward a single branch. In the simplest cases (3D crystals, exact directions) it gets there in finite time. We could simply *define* a branch as "what has been recorded", which makes "result = branch" automatic. That is a fine bookkeeping choice, but it proves nothing, so we keep both notions. **Who survives past the horizon?** In the textbook examples, which continuation an observer gets through is fixed by its own motion (for example, which way it is circling). So surviving is not a fork. The fork is in *which world*, and given the world, survival is determined. A few observers in Taub–NUT are trapped and survive in no continuation. For Hadley's geons this is not yet worked out.

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
   - Examples: #355 (shared short elements); #359 ($\mathbb Z^3$ rank 2: 9, 19, 29 worlds with share 1 before full rank).
   - So **the outcome at $\tau$ is an equivalence class of branches**.
3. **Refinement.** $[W]^R_{\tau'}\subseteq[W]^R_\tau$ for $\tau'>\tau$: outcomes refine monotonically toward the full branch.
   - They reach it at finite $\tau$ only in special cases. For $n\le3$ crystal covers with exact-vector records, the record fixes Γ once $\tau$ reaches the largest successive minimum (#359).
   - Off-path geometry beyond any finite past is never fixed at finite $\tau$.

**Should "branch" be redefined at finite $\tau$ as the record class?**
- L29 already used that rule ("same branch at τ iff records match up to τ"). Under it, **outcome = branch holds by definition**.
- **Tautology or cheat?** It is a tautology, and as a convention it is acceptable. The record rule was fixed in batch 08, before this question, from David's 3:53 memory ruling, so it was not tuned to this target. It would be a **cheat** under the litmus prior-inputs test (LT2; the request says "T2") if offered as *evidence* that measurement outcomes are branches.
- It also hides the substantive question: can the germ diverge while the record does not (a branch without outcome; batch 12 (2)(a))?
- **Recommendation.** Keep both named: **record branch** (= outcome, by definition) and **state branch** (germ+record). Report claims about their relation as facts 1–3, not as a definition.

## (B) Observer survival beyond Misner

**Misner (#367, verified).** In each extension, timelike observers crossing the horizon are exactly those with one sign of winding. Survival is **determined by the observer's own data** given the extension, so it is not a fork.

**Taub–NUT (sketch; Misner 1967 "counterexample to almost anything", Hawking–Ellis §5.8; unchecked).**
- The Taub region has a compact $S^3$ Cauchy horizon with closed null generators.
- There are two inequivalent analytic extensions (the two NUT regions).
- The Misner-like dichotomy is expected: geodesics cross into a given extension according to the sign of a conserved quantity along the Hopf-fibre direction.
- **In addition**, some geodesics are **imprisoned**: incomplete in **both** extensions and confined to a compact set. Those observers survive in no extension.
- Whether the dichotomy is exactly as in Misner is **unverified** (#367).

**Compactly generated Cauchy horizons (sketch; Hawking 1992 chronology protection; unchecked).**
- These horizons contain closed or past-imprisoned null generators, and extensions beyond them are non-unique.
- For analytic extensions, the germ at a crossing fixes the extension locally. So **given an extension, whether a geodesic crosses is a function of its data**.
- Across extensions it varies. Survival is therefore a function of (extension, observer data): **determined within each world**, varying between worlds.
- That fits "branch A = world A". Dropout is not an arm (v0.10.1 §6.2).

**Hadley-type geon hosts (open).**
- If a geon *forms* (CTCs appearing after a globally hyperbolic era), its chronology horizon is compactly generated. The observer must cross it to receive a reply (#364 (d)), and the analysis above applies (unchecked).
- If the geon is **eternal** (Hadley 2000's $S^2\times\mathbb R$ world tube, V-text per #362, with CTCs for all time), there may be **no Cauchy surface** $S$ at all. Then "$D^+(S)$", the shared past and "beyond the horizon" are undefined, and the framework's compatible-host comparison needs another anchor (e.g. the observer's own chronological region $U$).

**Answer (B).** In all the cases checked, survival is determined by the observer's own data within each extension. What varies is the extension, i.e. the world. Some Taub–NUT observers survive in none. Hadley hosts are open, and eternal geons break the Cauchy-surface setup.

## Weak points

1. (A) rests on the L29 record model, including #355's caveats (beacon switch-on, exact reals).
2. "Never fixed at finite τ" for off-path geometry is a sketch.
3. The Taub–NUT dichotomy and imprisoned geodesics are from memory, unchecked.
4. Hawking 1992's structure is from memory.
5. Hadley hosts: survival is unanalysed, and eternal geons may have no Cauchy surface.
6. The record-class redefinition must not be used as evidence (LT2).
