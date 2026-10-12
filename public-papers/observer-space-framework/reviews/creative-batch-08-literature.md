# Literature pass: creative batch 08 (L29), PR #354

Reviewer: Literature agent. PR head re-checked: `dbbaaa2` (base `creative/batch-07`). Files: `notes/creative/batch-08.md`, `notes/creative/ledger.md`. Do not merge. Marks: **V-text** = wording read; **V-meta** = bibliographic data verified, content from the standard account.

## 1. Counting lattices and quotients: literature, and order-dependence

| Source | Mark | Relevance |
|---|---|---|
| H.C. Wang, "Topics on totally discontinuous groups" (1972) | V-meta | Finitely many lattices of covolume ≤ V up to conjugacy, excluding $\mathrm{PSL}_2(\mathbb R)$, $\mathrm{PSL}_2(\mathbb C)$-type factors. So it holds for $\mathbb H^n$, $n\ge4$, but **not** $n=3$. |
| Jørgensen–Thurston (Thurston notes 1978–79, ch. 6) | V-meta | In $\mathbb H^3$, volumes are well-ordered (type $\omega^\omega$), but infinitely many manifolds have bounded volume (Dehn-filling limits). So "list by volume" does not give finite counts for general hyperbolic 3-quotients. |
| Borel–Prasad, Publ. Math. IHÉS 69 (1989) 119 | V-meta | Finiteness of arithmetic lattices of bounded covolume, and minimal covolumes. |
| Gromov (1978, Bourbaki/Thurston-era volume bounds); Burger–Gelander–Lubotzky–Mozes, GAFA 12 (2002) 1161, "Counting hyperbolic manifolds" | V-meta | For $n\ge4$: $\log\#\{\mathrm{vol}\le V\}\asymp V\log V$. |
| Belolipetsky–Gelander–Lubotzky–Shalev, Ann. Math. 172 (2010) 2197 | V-meta | Counting arithmetic lattices by covolume. |
| Lubotzky–Segal, *Subgroup Growth* (Birkhäuser 2003) | V-meta | A finitely generated group has finitely many subgroups of each index (M. Hall). The batch's (d) claim is correct. |

**Batch claims checked.**
- For crystal covers, $\Gamma\le G$ has finite index and index ∝ spatial volume ($\mathrm{vol}=[G:\Gamma]\,\mathrm{vol}(G\backslash\tilde M)$), so the index and volume listings coincide. Correct.
- The raw count per branch is infinite. Correct (infinitely many finite-index subgroups).

**Order-dependence: yes, this is a known issue.**
- Ratios $N_b/N$ defined by an exhaustion are natural densities. In general they depend on the exhaustion: index/volume vs word-length bounds on generators give different limits, or no limit at all.
- This is the same structure as the cut-off/measure problem in eternal inflation (V-meta: Freivogel, "Making predictions in the multiverse", CQG 28 (2011) 204007; Vilenkin; Linde), where proportions of infinitely many worlds depend on the regulator.
- Systole is **not** an exhaustion here. For any fixed short loop, infinitely many finite-index $\Gamma$ contain it, so $\#\{\mathrm{sys}\le L\}$ is infinite. See S1.

## 2. Planck bounds, for (f)

- **V-text** (Planck 2015 XVIII, A&A 594 A18, intro and abstract):
  - 2013 XXVI (A&A 571 A26): cubic torus $R_i>0.92\chi_{\rm rec}$ (likelihood); matched circles $R_i>0.94\chi_{\rm rec}$ (99% CL).
  - 2015: $R_i>0.97\chi_{\rm rec}$ (cubic torus) and $>0.56\chi_{\rm rec}$ (slab).
- $R_i$ is the inscribed radius of the fundamental domain (the injectivity radius at the observer for these homogeneous models). Matched circles exist iff $2R_i<2\chi_{\rm rec}$, the last-scattering diameter.
- So cosmic handles shorter than about the last-scattering diameter are excluded for these topologies, while very anisotropic ones are weaker (slab: 0.56). The batch's (f) wording ("observationally constrained") is accurate. No string.

## 3. Standing rule and measure smuggle

- **Rule met:**
  - (i) the label is present verbatim and matches the ledger;
  - (ii) how the worlds become countable is stated (crystal covers, index exhaustion);
  - (iii) inevitability is stated (independence of the exhaustion).
- (M1) is kept separate and unchanged at L3. No weights are computed, and no Born/$|a|^2$ result appears.
- **Disclosure of the listing choice: partial, with one wrong claim.** The "inevitable" bullet correctly says that differing limits make the ordering "a measure by fiat". But the line before it calls index ordering "a geometric quantity, not a free label". That presents the choice of exhaustion as weight-free, and it isn't: volume is geometric, but *choosing* to list by it is a weight choice unless exhaustion-independence is shown.

S1. `notes/creative/batch-08.md`
- OLD: `a geometric quantity, not a free label`
- NEW: `a geometric quantity, but choosing to list by it is itself a weight choice unless the limit is shown to be exhaustion-independent (a known order-dependence: natural density; cf. the eternal-inflation measure problem)`

S2. `notes/creative/batch-08.md`
- OLD: `by index, by volume, by systole, by word length.`
- NEW: `by index (equivalently volume, for crystal covers) and by word length; systole is not an exhaustion, since infinitely many finite-index $\Gamma$ share a given short loop.`

## 4. Conflict with Paper 1

- **Accurate.** `papers/analytic-split.md` (origin/main, V-text): "$\sim$ compares the $\gamma_k$, not the $W_k$. Amplitude does not enter. Topology labels do not enter $\sim$." The batch quotes this exactly.
- The batch says plainly that identical-$\gamma$, different-$\rho$ hosts are distinct here and not in Paper 1, and that the conflict is accepted under working assumption 2, not resolved. Correct.
- C1 names the break with the germ-only state (the jet/patch lock).
- The reduction to Paper 1 for empty records is correct.
- Note (no string): the record is host data, not in the germ. So this is an extension of $\mathrm{Obs}$, not a refinement within the lock. The batch says so.

**David's 3:53 PM working assumptions:**
- Labelled "relayed via Physics Lead, not signed; verbatim; not changes to the paper". The label is correct.
- I could not check the wording against a primary record (none is in the repo). Exactness rests on the relay.

## Guardrails
- No forbidden symbol.
- No Born/$|a|^2$/$1/N$ result: the Born mention is the required conjecture label only.
- No interpretation-camp framing.
- No pick among M1/M2/T-options.
- Paper 1 untouched.
- Quotes are labelled relayed.

## Verdicts
- **Literature:** citations verified (V-meta, with Planck and Paper 1 V-text). Exhaustion-dependence is a known measure ambiguity. One wrong claim: systole as an exhaustion (S2).
- **Counting framing:** obeys the standing rule and smuggles no weights, but the "not a free label" line understates that choosing a listing is a weight choice (S1).
- **Paper 1 conflict:** stated accurately (jet/patch lock and $\sim$); flagged for David, not resolved.
