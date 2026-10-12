# Measurement model v0: consolidation (Creative Lead; do not merge)

**Fidelity passes applied:** Geometry #373 (11 non-OK claims), Literature #374 (S1, S2).

**Status.** A consolidation note only. **No new physics**: every claim below is carried from a batch, review or ledger row, cited inline. It is exploration under David's relaxations (§3), and not a change to the paper. Nothing goes into `versions/` or `papers/`. Citation status is as recorded in the source rows; anything not marked verified there is unchecked. Most results are sketches, as their sources say.

---

## 1. For David (plain language)

**What we have.** An observer that can remember (your 3:53 ruling) keeps a diary of signals it receives. It sends a signal out; the signal goes into a particle's tiny time loop (a Hadley geon) and comes back (your 4:17 idea). We call this **backscattering** (4:37 naming; the precise term is "round trip"). What comes back is written in the diary, and that is the measurement. Because the reply lands beyond a horizon, we do not assume the usual particle-physics in/out description (no unitary S-matrix).

Free fall stays perfectly predictable inside each possible world. The branching comes from *which world we are in*. Worlds that look identical to the observer now can send back different replies, or give the observer different futures. That is exactly "a fork in the observer's future", the target you named at 4:28. The fundamental group (the handle structure) is part of what distinguishes those worlds (L28/L29).

**Some details that survived review.**
- Only signals that come back "the right way round" in time count as replies (Type O). The others are just correlations (Type F) (#364).
- Where the geon forms after a period with a Cauchy surface, replies can only arrive after the observer has passed that horizon (#364 (d), sketch). Beyond it, whether the observer continues is fixed by its own motion within each world (Misner: Geometry's own computation, #367; Taub–NUT unverified). Stopping is not a branch (#367, #370, #371).
- What the observer has recorded so far may still cover several possible worlds, and it narrows toward one as more replies arrive. For worlds with a closed repeating structure (cocompact Γ in a known cover) and exact displacement records, it narrows to exactly one in a finite time (#370, sketch; homogeneous covers need care).
- Worlds are compared through the observer's state and diary. That still works when the geon has always existed and there is no "starting moment" (#370).

**What is not done.**
- Probabilities are deliberately parked. Counting worlds is only a labelled conjecture.
- How the memory is physically stored is open.
- The time-loop puzzle has infinitely many consistent solutions, which needs sorting out.
- A plain light signal is probably too simple: it seems to need to interact with something in the loop.
- Some Taub–NUT details are unverified.
- The nearest earlier ideas in the literature are Hadley's 1997 4-geon causal link between apparatus and preparation (for the measurement) and Belnap's 1992 branching picture (for outcomes as classes of branches).

---

## 2. The model

### 2.1 State: germ + record
- The state is $\hat O(\tau)=(O(\tau),\rho(\tau))$: the oriented germ (modulo isotropy, #324) plus a record of received signals. Each entry has an arrival proper time, an emission stamp and isotropy-invariant direction data.
- The record only grows (L28, L29; batch 08; David's 3:53 memory working assumption).
- **Well-posedness (#355).** It needs a beacon or body and exact-real records. Records are continuous arrival curves per deck element. A definite beacon switch-on time is needed for the split at $\tau^*$. The isotropy-angle gauge is valid but lossy.

### 2.2 Measurement = beacon round trip through the geon's CTC (plain name: backscattering)
- **Naming (David 4:37, paraphrased by Physics Lead).** "Backscattering" is the plain-language name, and "round trip" is the precise defined term. **Caveat:** the return lands beyond the observer's Cauchy horizon, so no unitary in/out S-matrix is assumed.
- The beacon signal leaves $\gamma$, enters the geon region $G$, which contains CTCs (Hadley 1997, V-text per #362), and returns into the observer's time-oriented record (David 4:17; L36; batch 11).
- The definition is new, though its ingredients are known. The closest prior art is Hadley 1997 (#365).

### 2.3 Type O / Type F returns
- The classification is well-posed and homotopy-invariant, set by $w_1$ of the closed loop. **Type O is the double-cover repair, not new** (#364 (a)).
- Non-trivial Type O homotopy classes exist (topologically) iff ker w1 ≠ {1}; there is no non-trivial Type O class if π1 = Z/2. Whether Hadley geons realise any of them by a causal curve through the CTC region is unchecked (#364 (b)).
- Type F returns are recorded as correlations, not measurements (batch 11).

### 2.4 Branching beyond the observer's Cauchy horizon
- If the host has a slice S before the geon, no reply can reach an observer still inside D⁺(S) (#364 (d), sketch; Hawking–Ellis §6.5 unverified). Measurements then happen beyond the observer's Cauchy horizon, where the observer's own path can depend on the extension. Without such an S (eternal geons) this timing result does not apply (#370).
- Where the germ diverges there, that **is** the branching sought (Physics Lead's framing, batch 12; David 4:28: "a fork in the observer's future (a branch in observer space) is exactly what we are looking for").

### 2.5 Survival vs dropout

**Misner space.**
- Within each extension, survival is fixed by the geodesic's own data. It is determined, not a fork (Geometry's computation, #367; not a verified source).
- Geodesics through the boost's fixed point are incomplete in both extensions and in **every** union. The non-Hausdorff union of the two extensions is **not complete**: it covers only the full $(\mathbb R^2\setminus\{0\})/B$, apart from those geodesics, which form a meagre set (topological; no measure adopted). (#367; resolution by Literature via Physics Lead; ledger.)

**Taub–NUT.**
- Non-isometric maximal extensions exist (Chruściel–Isenberg 1993, V-meta, abstract only, per #332/#368). The abstract also notes that many familiar extensions are isometric.
- The dichotomy and the imprisoned geodesics are unverified (Misner–Taub 1969).
- The completeness result for the Taub–NUT union is Hájíček 1971 (Literature via Physics Lead; unchecked here).

**General.**
- Non-unique extension is the general Cauchy-horizon fact (#371).
- **Dropout**, i.e. ending or non-existence of an extension, is **not an arm** (v0.10.1 §6.2; #370).
- Survival is determined within each world and varies between worlds (L38, L42; Misner by Geometry's computation, #367; Taub–NUT and Hadley hosts unverified).

### 2.6 Record branch vs state branch
- The state branch $[W]^S_\tau$ sits inside the record class $[W]^R_\tau$ (the outcome). The partitions nest and do not cross (#369, L41).
- At finite $\tau$ the outcome is an equivalence class of branches, refining as $\tau$ grows (#369; #355; #359).
- Defining "branch" as the record class makes outcome = branch true by definition. That is a convention, not evidence (LT2). Both notions stay named (L41).
- Prior art: Belnap 1992 is closest (#371).

### 2.7 Single-branch certification
- For any cocompact Γ in a known cover with exact displacement records, Γ is fixed, and certifiably so, once $\tau$ exceeds a generating set's displacements and about twice the quotient diameter, provided the record identifies each deck element from its arrival (#370, sketch; this supersedes #359's 'n ≤ 3').
- This fails for non-cocompact Γ and for angle-only records. Homogeneous covers need care (the stabiliser) (#370).
- Under the analytic lock, the germ fixes the cover at $\tau=0$ except past non-unique extension points. What stays open is Γ and the extension (#370). In the smooth case (relaxed lock), geometry outside J⁻(γ(τ)) is never fixed by germ and record (#346, #370).

### 2.8 Comparing worlds
- $E_{\mathcal W}$ and $E_M$ are defined by germs (v0.10.1 §4), so worlds are compared by germ + record.
- This works for eternal geons, which have **no Cauchy surface** (#371). Only #346's agreement-region argument and #364 (d)'s timing need $D(S)$ (#370).

---

## 3. Relaxed locks and rulings (verbatim, as recorded in the ledger)

All are relayed and none is signed. The attribution is quoted exactly as the ledger records it. All rows are verbatim except 4:37 PM, which is Physics Lead's paraphrase.

| Time (ET, 2026-10-12 unless stated) | Lock / topic | David's words (as in the ledger) | Attribution as recorded |
|---|---|---|---|
| 3:14 PM | Analytic/geodesic lock may be relaxed (exploration only) | Yes, Creative Lead may propose ideas that relax the analytic/geodesic lock, as exploration only. | Ruling (David Strayhorn, 2026-10-12 3:14 PM ET, relayed via Physics Lead, not signed) |
| 3:19 PM | Reframing: branch A = world A | I want to see if I understand. You say that an observer in free fall has exactly one way to continue, so anything that branches turns out to be uncertainty about which world we’re in, not a fork in the observer’s own path. Are you saying this is a good thing or a bad thing? The best case scenario is that exactly what you describe. Within any one world, there is deterministic free fall without branching. Within observer space, branching happens due to uncertainty over which world we’re in. Branch A means the observer is in world A; branch B means the observer is in world B. Within world A or world B, branching doesn’t occur. | Reframing (David Strayhorn, 2026-10-12 3:19 PM ET, relayed via Physics Lead, not signed; verbatim) |
| 3:28 PM | Special aim | What’s wrong with special aim? If our desired style of branching can happen by special aim, then that’s still progress, right? | David on special aim (2026-10-12, relayed via Physics Lead, not signed; verbatim) |
| 3:30 PM | Revive sheets | Yes, revive sheets. Maybe you need special aim to hit the patches. On the other hand, maybe you need special aim to miss them! Is the glass half empty or half full? | David on special aim (2026-10-12, relayed via Physics Lead, not signed; verbatim) |
| 3:43 PM | (M1) question; branches as geometries | Can you explain in simple terms what M1 means? Are we saying the weight is proportional to the number of worlds? If so, that is acceptable. I do not consider that to be circular reasoning. Also, if branching coincides with different geometries in each branch, that has always been my intuition: branch A means geometry (fundamental group) A, B means B, and so on. Somehow, the local state teaches the observer something about the global state. Which seems impossible, but only because we haven’t yet figured out how to make it possible. | David on (M1) and branches as geometries (2026-10-12 3:43 PM ET, relayed via Physics Lead, not signed; verbatim) |
| 3:47 PM | Counting and the Born rule (conjecture only) | Counting doesn’t make it circular. If counting produces the Born rule, that’s not circular. That’s the goal. It is acceptable for us to conjecture that the count produces the Born Rule, and that’s circular if we stop our work, but that’s an intermediate step in our work. The next step will be to look for a reason that the Born rule is inevitable, inescapable, at which point we stop putting it in by hand. | David on counting and the Born rule (2026-10-12 3:47 PM ET, relayed via Physics Lead, not signed; verbatim) |
| 3:53 PM | Memory (working assumption) | Memory: yes, let’s run with that. But we will need eventually to consider how the memory is stored - is it part of the state itself? - but for now let’s just say yes, it can remember received signals. | Working assumptions for exploration (David Strayhorn, 2026-10-12 3:53 PM ET, relayed by Physics Lead, Physics Lead chat, not signed; verbatim; not changes to the paper) |
| 3:53 PM | Splitting with identical patches (working assumption) | (On splitting with identical patches) "Again, let’s say yes and see where that takes us." | Working assumptions for exploration (David Strayhorn, 2026-10-12 3:53 PM ET, relayed by Physics Lead, Physics Lead chat, not signed; verbatim; not changes to the paper) |
| 4:03 PM | Focus on successes; probabilities later | Let’s focus on our successes. I am encouraged by the fact that branching can happen at all, and that the fundamental group can play a part. We shouldn’t worry yet about the precise probabilities, especially considering that we have not yet created a model of how the observer can measure the position of an external particle. | David on focus (2026-10-12 4:03 PM ET, relayed by Physics Lead, Physics Lead chat, not signed; verbatim) |
| 4:06 PM | Geons not ruled out | Rule out geons? I don’t recall ruling out geons. I like Hadley’s 4-geons. | David on geons (2026-10-12 4:06 PM ET, relayed by Physics Lead, Physics Lead chat, not signed; verbatim) |
| 4:16 PM | CTCs and non-time-orientability in geon hosts | Yes, allow CTCs and non-time-orientability in geon hosts, as exploration only. | Geon hosts: CTCs and non-time-orientability (David, 4:16 PM ET 2026-10-12, in Physics Lead's chat, relayed by Physics Lead, not signed, answering "Should worlds containing geon particles be allowed to have time loops, as Hadley requires?"; verbatim) |
| 4:17 PM | Central hypothesis: signal round trip | Hmm, maybe that’s what it means to observe a particle? A signal goes from the observer to the particle’s CTC and comes back to the observer, communicating information about the particle’s state? | Central hypothesis (David, 2026-10-12 4:17 PM ET, relayed by Physics Lead, Physics Lead chat, not signed; verbatim) |
| 4:28 PM | Signal sent by the observer; fork is the target | No, I like the original idea of the signal sent out by the observer. I can wrap my head around that. / a fork in the observer's future (a branch in observer space) is exactly what we are looking for. | Signal round trip is the main line (David, 4:28 PM ET 2026-10-12, relayed by Physics Lead, Physics Lead chat, not signed; verbatim) |
| 4:37 PM | Naming: "backscattering" | (paraphrase) Use "backscattering" as the plain-language name for the measurement round trip; keep "round trip" as the precise defined term. | Naming (David, 4:37 PM ET 2026-10-12, relayed by Physics Lead, Physics Lead chat, not signed; paraphrased by Physics Lead; verbatim words not supplied) |
| 2026-10-10, L3 | (M1) unchanged | Record (M1) as my choice at L3, strong opinion, weakly held, open to reversal if the analysis turns against it. | v0.10.1 §11 open-calls row: "Ruled (M1) by David, 2026-10-10, at L3; relayed, not signed" |

---

## 4. Open problems (as flagged in the reviews)

1. **Where the memory is stored.** Is it part of the state itself? (David 3:53; ledger open item.) The non-local state breaks the germ-only definition (#352).
2. **Probabilities are parked** (David 4:03). Counting appears only as "conjecture: count gives Born (to be derived, not assumed)" (ledger standing rule). (M1) is unchanged at L3. Counting results stand: degenerate 0/1 shares in crystal covers (L30, L31; #358, #359).
3. **EKT infinity.** EKT found infinitely many self-consistent solutions (#365).
   - Countable generically, by isolated fixed points in traversal classes (L40, sketch).
   - Continuous families arise for data invariant under a continuous symmetry, and possibly from continuous internal degrees of freedom such as spin or inelasticity (unverified) (#367). Generic isolation assumes transversality of the actual EKT map (unverified).
   - Lossev–Novikov "jinn" loops are a second source of multiplicity (#368).
4. **Exact-real records and a beacon/body** are needed for well-posedness (#355).
5. **An interacting beacon is needed.** Friedman et al. 1990 is verified from the abstract only (#364 (c)): linear fields behave benignly in the wormhole examples, and interacting systems can have multiple solutions. Linear uniqueness (Friedman & Morris) was unverified in #364; its status in #365 is as recorded there. Non-benign spacetimes may misbehave even for linear fields. L36 needs matter (#364 (c)).
6. **Taub–NUT:** the dichotomy is unverified (Misner–Taub 1969; #370).
7. **Outcome vs branch at finite τ:** the outcome is coarser. Branch-without-outcome can occur (L39, L41).
8. **Split rule vs Paper 1:** the record split conflicts with Paper 1's $\sim$ ("Topology labels do not enter"). It is accepted under David's 3:53 working assumption 2, not resolved (batch 08 (b)).
9. Eternal geons: #346's first-divergence argument and #364 (d)'s timing do not apply (no D(S)); replies are not barred before any horizon. Ensemble comparison by germ + record is unaffected (#370).
10. **Hadley survival:** unanalysed for Hadley hosts (L42).
11. **Framing hazards:** keep clear of Everett-style branching (#332 N1; Sebens–Carroll flagged in #350). The non-Hausdorff union is a low-priority note only (#367): the Misner union forks no single geodesic; under the lock the branches share germs along the path (#367).
12. **Prior art:** Belnap 1992 (outcomes as classes of not-yet-split histories). Also Hájíček 1971, McCabe 2005, Earman 2008, Placek–Belnap / Müller (#368, #371).
13. **Resolved: #367 vs #371** (Literature via Physics Lead; ledger). #367 is right. Misner fixed-point geodesics are incomplete in every union, so the union of the two extensions is not complete; it covers only the full $(\mathbb R^2\setminus\{0\})/B$, apart from those geodesics. The Taub–NUT completeness result is Hájíček 1971. §2.5 is split by spacetime accordingly.
