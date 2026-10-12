# Creative batch 04 (Creative Lead; proposal, do not merge)

**Status.** Proposal only; exploration only, under David's ruling of 2026-10-12 3:14 PM ET (relayed via Physics Lead, not signed): "Yes, Creative Lead may propose ideas that relax the analytic/geodesic lock, as exploration only." Nothing goes into `versions/` or `papers/`. Charter: `notes/creative/charter.md`. Hypotheses H1–H5: `batch-03.md`. Citations are **unchecked** unless marked "verified per #342".

**Rules for every set.**
- R-a: an independent physical reason.
- R-b: it names which of H1–H5 it breaks.
- R-c: no continuum of options, and no law of $R$ by fiat.
- R-d: no measure sneaked in.
- R-e: it survives the objections already recorded in #334, #336, #338, #341 and #342: atypical hits, a continuum, a law of $R$ in disguise, borrowed quantisation, and options that vanish instead of forking.

## Result: no set survives

Every candidate below fails at least one rule on self-check, so batch 04 proposes **zero sets**. I am not proposing a set I can't defend. Relaxing the lock removes one barrier (Prop 3.2 / Cor 3.1), but the other recorded objections still bite every candidate found.

## Plain-language summary (one minute)

David allowed us to bend the two rules that kept every path from forking: smooth (analytic) worlds, and travellers in free fall. I tried eight ways of bending them. Each one either gives too many options (a smooth spread of possible futures, the "anything goes" end) or gives a few clean options at places a traveller essentially never reaches. In some, the options simply disappear instead of splitting. The two physical cases closest to a clean fork, bouncing off a wall versus passing through it, and continuing past a Cauchy horizon, were both closed off by results we already have. The lesson: the lock was not the only obstacle. A workable idea has to make a *few* options appear at places *every* traveller crosses, and nothing on the current list does that.

## Candidates checked (all dropped)

| # | Candidate | Breaks | Physical reason (R-a) | Fails | Why |
|---|---|---|---|---|---|
| D1 | $C^{1,\alpha}$ metrics (Hartman–Wintner 1951, verified per #342) | H3 | **No**: the class is chosen to break uniqueness (batch-03) | R-a, R-c | Non-Lipschitz (Peano-type) non-uniqueness gives a continuum of geodesics, not a few. |
| D2 | Matter frame (Ricci eigenvector; Stephani et al. 2003, Hall 2004, verified per #342) | H2 | Yes (observers comove with matter) | R-c, R-e | At a symmetric degeneracy the frames are a continuum (#342 R2), on codim-2 sets (#341). At the codim-1 Segre transition to a complex pair (via a null-degenerate type; unchecked) the timelike frame *vanishes*: no fork. Undefined in vacuum. |
| D3 | Weyl canonical frame (vacuum fix for D2; Petrov type I, unchecked) | H2 | Partly | R-e | Finitely many canonical frames would be discrete, but each sheet continues uniquely along a path. Sheets meet only where Weyl eigenvalues coincide: complex codim 1 = real codim 2, so rarely hit (#336, #341). |
| D4 | Self-force with the tail term (Mino–Sasaki–Tanaka 1997; Quinn–Wald 1997, unchecked) | H2 | Yes | R-c | With the whole past in the state (memory), the reduced-order motion is unique: no fork. With a memoryless state, the unknown past is a continuum (#342 R1, #341). |
| D5 | Lattice / causal network (Myrheim 1978, Brightwell–Gregory 1991, verified per #342) | H1, H3, H4 | Partly | R-c, R-e | Ties are two-point problems; the endpoint is a law of $R$ in disguise (#341). The initial-value continuation is unique on a regular lattice. Exact ties on an irregular one are non-generic. The ℓ→0 count diverges (#338, #341). |
| D6 | Fork at a Cauchy horizon: world = maximal globally hyperbolic development (Choquet-Bruhat–Geroch 1969; Chruściel–Isenberg 1993, verified in #332) | H1 (world definition) | Yes (initial data determine exactly the MGHD) | R-c, R-e | In the analytic class, `papers/patch-edge.md` Theorem 7 ("If two members both extend the geodesic analytically through $\tau_\partial$, they share the same continuation") leaves no fork for a given geodesic. In $C^\infty$ the extensions are a continuum. Generic Cauchy horizons are also unstable (strong cosmic censorship; unchecked). |
| D7 | Transmit-or-reflect at a wall with a metric jump (Weierstrass–Erdmann corner conditions give two roots; unchecked) | H3 | Weak: Einstein's equations need a continuous metric (Geroch–Traschen 1987, verified in #332) | R-a, R-e | Walls are hit typically (#336 (e)), and two roots are discrete, the closest miss. But for a continuous (Israel-type) metric the corner condition keeps $p$ continuous, so no reflection. Any smoothing of the jump (the charter's k→∞ route) restores unique transmission. Partial reflection is a wave effect, so it would borrow quantisation (#339). |
| D8 | Topology change through a "trousers" crotch (Geroch, Sorkin; unchecked) | H3, H4 | Partly | R-e | Each geodesic from the waist enters exactly one leg, fixed by its position. Only crotch-point geodesics (codim ≥2) are undetermined. |

Also considered and not tabled: signature change (Hartle–Hawking, Ellis et al. 1992; unchecked). The signature-change surface lies in the past, so it is not met by future-directed observers. Free data on a null hypersurface (impulsive waves): a continuum.

## What would pass (target for batch 05)

A mechanism that combines (1) a branch locus of codimension 1, so hits are typical (#336 (e)); (2) a finite number of options there, fixed by geometry or topology, so no continuum and no fiat; and (3) stability under smoothing (k→∞) and no wave/quantum borrowing. D7 shows (1) and (2) together are possible on paper, but it fails (3). Batch 05 should search for (3) directly.
