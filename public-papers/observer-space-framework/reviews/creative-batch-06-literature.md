# Literature prior-art and taste pass: Creative batch 06 (#348)

**Reviewer:** Literature. **Date:** 2026-10-12. **Record type:** review record; applies nothing; do not merge.

**Heads.** #348 head `68396c6`, based on `creative/batch-05` (`d33d1d3`); files `notes/creative/batch-06.md` and the ledger. main `e41412b`. No earlier review of #348 exists.

**Attribution.** David's 3:28 and 3:30 PM ET words are quoted in the batch and the ledger, and recorded as relayed, not signed.

**Marks.**
- **V-text:** text or abstract checked this session.
- **V-meta:** bibliographic data and topic only.

## Verdict: HOLD

Fixes:
- **R1 (substantive):** the two continuations in L24 carry the *same* state sequence.
- **R2:** "exactly $e$" is fixed by a rule, not by the geodesic equation.
- **R3:** the L23 measure point.

The topology claims (cover, monodromy, non-regularity, cone angle $2\pi e$) are correct.

## R1: the forked futures are not different states

- Every germ on either continuation "depends only on its base point and velocity", as the batch itself says, and **both continuations project to the same base geodesic $\beta$**. So they carry identical germs at every $\tau$ off $\Sigma$, after $a$ as well as before it.
- After $y_{23}$, the sheet-2 branch, under the same lift rule, again continues along $\beta$ with the same germs. The only difference is an extra instant with no state (a gap at $\tau_a$), or, if no rule applies, an *end* at $\tau_a$.
- $P(O)$ is the abstract maximal simply connected continuation (Thm B), so it does not see $\Sigma$. Under Paper 1's split criterion ("the first $\tau$ at which those patches disagree") the two never split. A gap-or-end difference is the nested-prefix pattern of Geometry's #345 caveat, and `papers/patch-edge.md` already says "The hitchhiker story is dead at the boundary too".
- Non-regularity of the cover changes the sheet labels, not the states. Both the #324 argument and the non-regular construction land in the same place.

## Literature

**Geodesics and waves through cone points and branch loci.**
- Diffraction from a cone point sends a wave into every direction, a continuum. The geometric (non-diffractive) directions are the near-miss limits. Sources:
  - Sommerfeld, *Math. Ann.* 47 (1896) 317 (V-meta).
  - Cheeger & Taylor, "On the diffraction of waves by conical singularities I, II", *CPAM* 35 (1982) 275–331, 487–529 (V-meta).
  - Ford & Wunsch, "The diffractive wave trace on manifolds with conic singularities", *Adv. Math.* 304 (2017) 1330–1385 (V-text, abstract).
- On flat surfaces with cone angle $>2\pi$, a path through the cone point is locally length-minimising iff both angles are $\ge\pi$. That is an interval of directions, as the batch says; standard for translation and half-translation surfaces (V-meta).
- **The near-miss limits are always just the two extreme directions** (angle exactly $\pi$ on one side). For cone angle $2\pi e$, the $e$ lifts sit at $\pi,3\pi,\dots,(2e-1)\pi$. So for $e=2$ the two lifts are exactly the two limits. **For $e\ge3$ the $e-2$ middle lifts are not near-miss limits**, which settles the batch's "unchecked for $e\ge3$" negatively.
- Translation surfaces:
  - Kerckhoff, Masur & Smillie, "Ergodicity of billiard flows and quadratic differentials", *Ann. Math.* 124 (1986) 293–311 (V-text: bibliographic data and zbMATH review; unique ergodicity in almost every direction is V-meta).
  - Saddle-connection directions are countable and dense (Masur, *Duke Math. J.* 53 (1986) 307, V-meta).
  - This is the exact flat-surface analogue of B1: "hit a cone point" directions are dense and meagre (countable), while minimal, dense trajectories are generic. B1 has a theorem-level analogue.

**Cosmic strings and excess angles.**
- Vilenkin, *PRD* 23 (1981) 852; Hiscock, *PRD* 31 (1985) 3288; Gott, *ApJ* 288 (1985) 422 (V-meta).
- In 2+1 dimensions a point mass is a cone, and negative mass gives an excess angle: Deser, Jackiw & 't Hooft, *Ann. Phys.* 152 (1984) 220 (V-meta).
- A $4\pi$ cone needs deficit $8\pi G\mu=-2\pi$, i.e. tension $\mu=-1/(4G)$: a negative-tension string. Negative-mass strings appear in lensing studies, e.g. Cramer et al., *PRD* 51 (1995) 3117 (V-meta). The batch's "negative-tension-like source" is right.

**Singular structure.**
- Conical singularities are quasi-regular: Ellis & Schmidt, *GRG* 8 (1977) 915 (V-text abstract, #339). That class "includes an idealized cosmic string" (V-text abstract, #339).
- Strings are not Geroch–Traschen distributions: *PRD* 36 (1987) 1017 (V-text, #332 R3). The batch cites this correctly.

**Genericity.**
- Thom transversality (e.g. Abraham & Robbin, *Transversal Mappings and Flows*, 1967; Guillemin & Pollack, *Differential Topology*, 1974; V-meta).
- #336 (a)/(d): the hitting set is meagre and null at every finite $\ell$. B1 restates this correctly, and B2 restates #336 (f) correctly.

**Riemann existence.** A branched cover with given monodromy exists: the Riemann existence theorem (e.g. Forster, *Lectures on Riemann Surfaces*, GTM 81, V-meta). Monodromy $(1\,2),(2\,3)$ generates $S_3$, so the cover is transitive and connected. $|S_3|=6\neq3$, so it is non-regular. Correct.

## Measure and framing

- **R3 (L23).** The ledger's own L23 says that "any physical restriction that makes the compatible futures countable also chooses the measure". With a topological count $e$, Paper 1 §6 ("If distinct evolutions are countable, counting is the unique reasonable measure on observer space") gives $1/e$ per sheet, i.e. **1/2 per sheet**, by default. "Nothing is weighted" is therefore not measure-neutral. The default weight must be named, not denied. (By R1 the two continuations are not distinct evolutions anyway, so in L24 the count is currently 1.)
- **Everett risk (#332 N1): high.**
  - A fork into sheets inside one host is the branching-spacetime picture (Belnap 1992; McCabe 2005, V-text #332).
  - B2's "which torn piece is the observer" is the self-locating-uncertainty problem of Everettian probability (Sebens & Carroll, *BJPS* 69 (2018) 25, V-meta).
  - That is the Carroll–Sebens framing the guardrails exclude. It may be flagged as a hazard but must not be borrowed.

## Verdicts

| Item | (a) Known? | (b) Killed in the record? | (c) Sneaks the answer in? |
|---|---|---|---|
| **L24** existence | Yes: branched covers, cone geodesics and diffraction (above). | **Effectively, yes (R1).** Identical germs on both continuations; gap or end only (patch-edge; Geometry's #345 caveat; #324). | The count $e$ comes from a rule (R2); 1/2 per sheet by L23 / §6 (R3). |
| **L25** typicality | Yes: dense and meagre hitting is the translation-surface picture (KMS 1986; Masur 1986); the open condition for tubes is #336 (f). | B1 is not killed: it is a restatement plus a plausible density sketch. B2 owes #336 (f) C1–C3, and its tube collides with Paper 1's jet/patch lock (#339). | **B2: Everett / Carroll–Sebens hazard.** Typicality itself is measure-free (topological). |

## Strings

**Each OLD occurs once at `68396c6`** (`batch-06.md`, except the last, which is in `ledger.md`).

**R1**

OLD:
~~~
- So the two state sequences differ from $a$ onward. Germs before $a$ are equal: every germ depends only on its base point and velocity, since the projection is a local isometry. **The difference first shows at the second seam, not right after the fork.**
~~~
NEW:
~~~
- But the two state sequences do not differ as states. Every germ depends only on its base point and velocity, since the projection is a local isometry, and both continuations project to the same base geodesic $\beta$. So they carry identical germs at every $\tau$ off $\Sigma$, before and after $a$. The only difference is a gap (or, without a rule, an end) at the second seam, which is the nested-prefix pattern, not a split of patches (Paper 1's criterion; `papers/patch-edge.md`).
~~~

OLD:
~~~
an aimed path forks into $e=2$ sheets with different futures (second seam on one branch only)
~~~
NEW:
~~~
an aimed path forks into $e=2$ sheets carrying identical germs (second seam on one branch only gives a gap or end, not a different state; #348 review R1)
~~~

**R2**

OLD:
~~~
- So the options are **a whole number, $e=2$**, read off the cycle length of $\sigma_0$. This is topology, not a choice.
~~~
NEW:
~~~
- So, under the lift rule below, the options are **a whole number, $e=2$**, read off the cycle length of $\sigma_0$. The number is topology; that only these $e$ directions count is a rule (diffraction from a cone point populates a continuum of directions).
~~~

OLD:
~~~
Limits of near-miss geodesics give only two of the candidate directions in general; for $e=2$ these are exactly the two lifts, so here the rule and the limit agree (unchecked for $e\ge3$).
~~~
NEW:
~~~
Limits of near-miss geodesics give only the two extreme directions (angle exactly $\pi$ on one side); for $e=2$ these are exactly the two lifts, so here the rule and the limit agree. For $e\ge3$ they disagree: the lifts sit at $\pi,3\pi,\dots,(2e-1)\pi$, and the $e-2$ middle lifts are not near-miss limits.
~~~

**R3**

OLD:
~~~
- **L23 trap.** Nothing is weighted.
~~~
NEW:
~~~
- **L23 trap.** No weight is written, but by L23 and Paper 1 §6 a countable set of $e$ distinct continuations would default to counting ($1/e$ each); that default must be named, not denied.
~~~

## Guardrails

Clean, except the framing hazard above:
- No forbidden Greek letter or its TeX macro.
- No Born, $|a|^2$ or $1/N$ result.
- No topology, (M1) or (A) pick.
- `versions/` and `papers/` are untouched.
- The Everett / Carroll–Sebens framing is a hazard to flag, not something present.
