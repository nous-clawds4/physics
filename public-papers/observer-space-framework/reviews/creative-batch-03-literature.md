# Literature prior-art and taste pass: Creative batch 03 (#340)

**Reviewer:** Literature. **Date:** 2026-10-12. **Record type:** review record; applies nothing; do not merge.

**Heads.** #340 head `738674c`, based on `creative/batch-02`; one file, `notes/creative/batch-03.md`. main `e41412b`. No earlier review of #340 exists.

**Marks.**
- **V-text:** text or abstract checked this session.
- **V-meta:** bibliographic data and topic only.

## Verdict: HOLD (narrow)

Two claims are wrong:
- **R1:** the gravitational self-force does not need the acceleration.
- **R2:** Set 2's forks are not discrete.

There is also one record point that applies to all three sets. `papers/geodesic-lifts.md` opens: "Locked starting point: $W$ is real-analytic; observers follow geodesics." Set 1 drops the manifold and analyticity, and Sets 2 and 3 drop "observers follow geodesics" (H2). All three therefore reopen a lock, which is David's call. The same holds for v0.10.1's type-(i) geodesic rule (§5, §8.1) and Paper 1's locked analytic jet.

The Prop. 3.2 quote is exact, and so is "would be a different evolution law" (geodesic-lifts §3).

### Per-set verdicts

| Set | (a) Already known? | (b) Already killed by the record? | (c) Sneaks the answer in or slips in a measure? |
|---|---|---|---|
| 1 Lattice geodesic ties | **Yes.** Non-unique shortest paths on lattices are elementary (taxicab ties). In causal sets, geodesics are longest chains (Myrheim 1978; Brightwell & Gregory, *PRL* 66, 260 (1991), V-meta). | **Not killed; collides with the locks above.** A network drops the manifold, the jet and analyticity, so Paper 1's elementary object has no meaning on it. The ℓ→0 limit must return the CWS singleton (v0.10.1 §8.1), as the batch says. | **Count hazard.** Tie numbers on a regular lattice are combinatorial (binomial). Using them as weights would be a count by fiat (LT2/TT4). Not done yet. |
| 2 Fork where matter frames tie | **Known.** The timelike Ricci eigenvector as the fluid velocity, and the Segre classification of Ricci: Stephani et al., *Exact Solutions of Einstein's Field Equations*, 2nd ed., CUP 2003, Ch. 5; Hall, *Symmetries and Curvature Structure in GR*, World Scientific 2004 (V-meta). | **Collides with H2's lock and with v0.10.1 §4's oriented observer.** $u$ is free data of the state $O^u$ ("together with a future time direction", Paper 1). Reading $u$ off the jet removes it. | **No measure.** But the mechanism is wrong as stated (R2): at a degeneracy the timelike eigenspace is a continuum, not a few frames. That makes it the "anything goes" side, plus the #336 hitting risk. |
| 3 Self-force needs acceleration | **Yes.** The electromagnetic ALD equation is third order. The gravitational MiSaTaQuWa force is a tail (past-history) term in reduced order, not a third-derivative term (R1). | **Effectively killed by the literature.** Reduction of order (Landau–Lifshitz) restores second-order uniqueness. Quinn–Wald also hold that "point particles" are not fundamental objects, which sits badly with a point observer. | **No measure.** A continuum, as the batch says. |

### Citation status (all marked "unchecked" in #340)

| Citation | Bibliography | Holds? |
|---|---|---|
| Abraham–Lorentz–Dirac | Abraham, *Theorie der Elektrizität* II (1905); Lorentz, *The Theory of Electrons* (1909); Dirac, *Proc. R. Soc. A* 167, 148 (1938) (V-meta) | **Yes** for charge: the equation is third order and needs the acceleration. |
| Mino–Sasaki–Tanaka / Quinn–Wald 1997 | MST, *PRD* 55, 3457 (1997); QW, *PRD* 56, 3381 (1997) (V-text, abstracts) | Citation correct. **The claim is wrong for mass (R1).** QW: "In the gravitational case, our final expression for the (reduced order) equations of motion shows that the deviation from geodesic motion arises entirely from a 'tail term'". The tail is the past history (real memory), not the acceleration. |
| Hartman–Wintner 1951 | "On the problems of geodesics in the small", *Amer. J. Math.* 73, 132–148 (1951) (V-meta; content V-text via Sämann–Steinbauer, arXiv:1710.10887). See also Hartman, *Amer. J. Math.* 72, 723 (1950). | **Yes.** For $C^{1,\alpha}$ with $\alpha<1$, geodesics can be non-unique. |
| Causal-set longest chains non-unique | Myrheim, CERN preprint TH-2538 (1978); Brightwell–Gregory 1991 (V-meta) | **Plausible, not verified as a theorem.** Geodesics as longest chains is standard. That they are "typically non-unique" in a sprinkling is reasonable but has no source here. Keep "unchecked". |
| Segre-type change | Stephani et al. 2003 Ch. 5; Hall 2004 (V-meta) | **Partly.** Uniqueness of the timelike eigendirection fails where the timelike eigenvalue becomes degenerate. But the resulting freedom is a continuum (R2). |
| Landau–Lifshitz reduction of order | Landau & Lifshitz, *The Classical Theory of Fields*, 4th ed. (1975) §75 (V-meta); Spohn, *Europhys. Lett.* 50, 287 (2000), critical manifold (V-meta); Gralla, Harte & Wald, *PRD* 80, 024031 (2009), and Gralla & Wald, *CQG* 25, 205009 (2008), for the self-force (V-meta) | **Yes.** Reduction of order restores second-order uniqueness. |
| Runaway pathology | Dirac 1938; Jackson, *Classical Electrodynamics*, 3rd ed., Ch. 16 (V-meta) | **Yes.** Runaways and preacceleration are the textbook pathology. |

### R1 (gravitational self-force)

OLD:
~~~
**Yes:** a body with mass or charge feels a self-force (Abraham–Lorentz–Dirac, unchecked; gravitational self-force, Mino–Sasaki–Tanaka / Quinn–Wald 1997, unchecked)
~~~
NEW:
~~~
**Yes, for charge:** a charged body feels a self-force whose equation is third order (Abraham–Lorentz–Dirac; Dirac, *Proc. R. Soc. A* 167, 148 (1938)). For mass, the gravitational self-force in reduced order is a tail (past-history) term, not an acceleration term (Mino–Sasaki–Tanaka, *PRD* 55, 3457 (1997); Quinn–Wald, *PRD* 56, 3381 (1997))
~~~

OLD:
~~~
A real body with mass disturbs spacetime and is pushed by its own disturbance, the self-force. In the simplest equations for this, knowing where you are and how fast you're moving is not enough: you also need your acceleration, a bit of your past.
~~~
NEW:
~~~
A real charged body is pushed by its own field, the self-force. In the simplest equation for this (the electromagnetic one), knowing where you are and how fast you're moving is not enough: you also need your acceleration. For a body's mass, the self-force instead depends on its whole past path (a "tail"), not on its acceleration.
~~~

### R2 (Set 2 is not discrete)

OLD:
~~~
At special points two candidate frames become equally good, and the rule allows a small, countable number of ways onward.
~~~
NEW:
~~~
At special points the preferred frame stops being unique, and then a whole continuum of frames is equally good (a degenerate eigenvalue has an eigenspace, not a few eigenvectors), so the rule allows a continuum of ways onward unless something else picks one.
~~~

OLD:
~~~
**Beats it at degeneracies, discretely.**
~~~
NEW:
~~~
**Beats it at degeneracies, but with a continuum.**
~~~

OLD:
~~~
Set 2 is the only one with a physical reason, discreteness and branching in motion together;
~~~
NEW:
~~~
Set 2 has a physical reason and branching in motion, but its degeneracies give a continuum, not discreteness;
~~~

### Guardrails

Clean:
- No forbidden Greek letter or its TeX macro.
- No Born, $|a|^2$ or $1/N$ result.
- No Everett framing.
- No topology, (M1) or (A) pick.
- `versions/` and Paper 1 are untouched.
