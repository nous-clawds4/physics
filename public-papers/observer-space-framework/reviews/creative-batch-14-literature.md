# Literature pass: creative batch 14 (L43–L47), PR #379

Reviewer: Literature agent. PR head recorded: `0ceaf85` (base `creative/measurement-model-v0`). Files: `notes/creative/batch-14.md`, `charter.md`, `ledger.md`. Do not merge. Marks: **V-text** = wording read (abstract or text); **V-meta** = bibliographic data verified (Crossref), content from the standard account.

## 1. Topology-change theorems: exact hypotheses

| Source | Mark | Hypotheses and result | Batch's statement |
|---|---|---|---|
| Geroch, "Topology in General Relativity", J. Math. Phys. 8 (1967) 782 | V-meta (statement V-text via Gibbons's restatement: compact $M$, non-singular Lorentz metric "which we shall assume time-orientable", spacelike boundary; "there exist many such pairs … but they all contain closed timelike curves") | Compact interpolating region, time-orientable, compact spacelike boundaries. Topology change implies CTCs. The escapes are CTCs **or non-time-orientability**. | Correct as far as it goes. It omits the non-time-orientable escape, which David's 4:16 PM exploration allowance also covers. Note only. |
| Tipler, "Singularities and causality violation", Ann. Phys. 108 (1977) 1; PRL 37 (1976) 879 | V-meta; characterised V-text by Borde's abstract | Topology change in a compact region is incompatible with Einstein's equation under energy and generic conditions. Per Borde (V-text): "Like Tipler's result, it makes no assumptions about geodesic completeness; i.e., it does not permit topology change even at the price of singularities". | **Wrong (S1):** "produces a singularity" misstates it. The result forbids the change outright. |
| Borde, "Topology change in classical general relativity", gr-qc/9406053 | V-text (abstract) | "Causally compact" interpolating spacetimes, any dimension. Topology change brings causality violation. For dimensions ≥ 3 it "cannot satisfy Einstein's equation (with a reasonable source)". Kinematically possible without a field equation. | **Imprecise (S2):** "non-compact settings" should be "causally compact", a wider class than compact. |
| Gibbons & Hawking, "Selection rules for topology change", CMP 148 (1992) 345; "Kinks and topology change", PRL 69 (1992) 1719 | V-text (CMP abstract); PRL V-meta | Compact region, Lorentz metric, SL(2,ℂ) spin structure: "impossible to create a single wormhole … but it is kinematically possible to create such wormholes in pairs". The invariant is the mod-2 Kervaire semi-characteristic. The kink version counts wormholes plus kinks mod 2. | Correct ("mod-2 condition on created handles"). |

**Do these close 2A (topology-changing write via CTCs)?**
- **Not by Geroch.** It permits topology change with CTCs or non-time-orientability, both allowed in geon hosts as exploration only (David 4:16 PM).
- **Yes, dynamically, under energy conditions.** Tipler and Borde forbid it with Einstein's equation and a reasonable source, whatever happens to CTCs, and Borde's result holds in dimension ≥ 3 for causally compact regions. So 2A survives only with sources that violate those energy conditions, or outside causal compactness.
- **Gibbons–Hawking:** with fermions (a spin structure), a single handle per write is forbidden kinematically. Handles must come in pairs.
- The batch parks 2A on cost grounds (CTCs at the observer, one per bit). That is consistent. The theorems add a stronger reason: "Parked; also forbidden for reasonable sources (Tipler, Borde)". Its weak point 6 is now answered.

## 2. EKT multiplicity and Hadley geons

- **It does not transfer by any result we know.** EKT (PRD 44 (1991) 1077, V-text abstract per #365) treat a nonrelativistic billiard ball in a traversable-wormhole time machine. A Hadley geon (Hadley 1997/2000, V-text per #362) is a non-time-orientable, CTC-bearing particle region with no worked metric: Hadley 1997 notes "it is not known whether such solutions exist".
- Weak point 1 is accurate. The transfer is an assumption.

## 3. Bound multi-geon configurations

- Wheeler, "Geons", Phys. Rev. 97 (1955) 511 (V-meta): electromagnetic geons, unstable or leaking in the standard account.
- Brill & Hartle, Phys. Rev. 135 (1964) B271 (V-meta): gravitational geons by self-consistent field averaging.
- Anderson & Brill, "Gravitational geons revisited", PRD 56 (1997) 4824 (V-meta): long-lived but not exactly stable, in the standard account.
- **No stable bound configuration of several geons is known to us.** Weak point 2 is accurate.

## 4. Prior art the batch should cite

- **Gravitational-wave memory.**
  - Zel'dovich & Polnarev, Sov. Astron. 18 (1974) 17 (V-meta);
  - Braginsky & Thorne, Nature 327 (1987) 123 (V-meta);
  - Christodoulou, "Nonlinear nature of gravitation and gravitational-wave experiments", PRL 67 (1991) 1486 (V-meta).

  The memory effect is a permanent change in the separation of free test masses after a burst. That is prior art for Set 3's "relative positions" record, and it is a **continuum** record, as the batch says. I found no GR literature on an integer winding-number memory.
- **Topological censorship.** Friedman, Schleich & Witt, PRL 71 (1993) 1486 (V-text abstract): "in a globally hyperbolic, asymptotically flat spacetime satisfying the null energy condition, every causal curve from $\mathscr I^-$ to $\mathscr I^+$ is homotopic to a topologically trivial curve". This is the central constraint on *probing* topology with signals.
  - The round trip escapes it only because geon hosts fail global hyperbolicity (CTCs; no Cauchy surface, #371) or violate the energy condition.
  - The batch should say which. Note, no string.
- **Non-linear gravitational waves through wormholes:** no verified source found. The batch's "open; too hard to check now" stands.

## 5. Winding-count write (Set 3): overclaim

- A bound body orbiting a ledger geon **crosses any cut once per orbit under free motion**. So its integer winding count advances by itself and is not a stored datum.
- A kick generically changes the orbit's phase and period (continuous). The difference from the unkicked count then grows with time instead of settling at an integer.
- A discrete, stable record needs a capture-type invariant instead: *which* closed homotopy class the body ends up trapped in, e.g. bound to geon A vs geon B vs unbound. That holds only if those classes are dynamically stable.
- "Discrete and stable for free" is wrong as stated (S3–S5).

## 6. Strings (each OLD occurs once at 0ceaf85)

S1. `notes/creative/batch-14.md`
- OLD: `Tipler 1977: with the weak energy condition and generic conditions, topology change produces a singularity (no CTC-free, non-singular route).`
- NEW: `Tipler 1977 (Ann. Phys. 108, 1; PRL 37 (1976) 879): with Einstein's equation, energy and generic conditions, topology change in a compact region is forbidden outright, "even at the price of singularities" (as characterised in Borde 1994's abstract, V-text; Tipler V-meta).`

S2. `notes/creative/batch-14.md`
- OLD: `Borde 1994: extends the singularity/causality obstruction to non-compact settings.`
- NEW: `Borde 1994 (gr-qc/9406053, V-text abstract): for "causally compact" interpolating spacetimes (wider than compact), topology change brings causality violation, and in dimension ≥ 3 cannot satisfy Einstein's equation with a reasonable source; it is kinematically possible without a field equation.`

S3. `notes/creative/batch-14.md`
- OLD: `Discreteness is for free (ℤ). Stability holds because, between kicks, the winding changes only if the body crosses the cut, which free motion does at definite times.`
- NEW: `The winding is an integer, but free orbital motion crosses the cut once per orbit, so the raw count advances by itself and a kick changes the orbit's phase and period continuously. A discrete, stable record needs a capture-type invariant instead: which closed homotopy class the body ends up bound in (e.g. bound to geon A vs geon B vs unbound), and only if those classes are dynamically stable (unchecked).`

S4. `notes/creative/batch-14.md`
- OLD: `The whole-number version gives a record that is discrete and stable for free.`
- NEW: `A whole-number record works only if a kick moves a body into a different stable trapped orbit (e.g. around a different geon); a plain winding count keeps ticking on its own.`

S5. `notes/creative/ledger.md`
- OLD: `discrete and stable for free`
- NEW: `discrete only via capture into stable homotopy classes of bound orbits (raw winding advances under free motion; #380)`

## Guardrails
- No forbidden symbol (none in this file).
- No Born/$|a|^2$/$1/N$ result; the batch is structure-only.
- No Everett framing.
- No pick among M1/M2/T-options or on CTCs. 2A's status is reported, not ruled.
- Paper 1 untouched.
- David's 7:45 PM words are labelled relayed, not signed, verbatim, and identical in the batch and ledger. I cannot check them against a primary record. No geon ruling is claimed.

## Verdicts
- **Topology-change theorems:** Geroch and Gibbons–Hawking are stated correctly. Tipler is misstated (S1) and Borde is imprecise (S2).
  - 2A is not closed by Geroch (CTCs or non-time-orientability are allowed), but it is closed by Tipler and Borde for reasonable sources.
  - Under Gibbons–Hawking, single-handle writes are forbidden when there is a spin structure.
- **L43 (interacting carrier):** consistent with Friedman–Morris and EKT. The transfer to Hadley geons is unshown (weak point 1). Survives.
- **L44 (ledger geons, fixed topology):** survives. No known stable bound multi-geon configuration exists (weak point 2).
- **L45 (topology-changing write):** parked correctly, and further forbidden for reasonable sources.
- **L46 (winding write):** overclaimed (S3–S5). It survives only as capture into stable bound classes. The exact-real position record has prior art in gravitational-wave memory.
- **L47 (ledger in state):** consistent with #336. Survives.
- **Missing prior art:** topological censorship (FSW 1993) and gravitational-wave memory.
