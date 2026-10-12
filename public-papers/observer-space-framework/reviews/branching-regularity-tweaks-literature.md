# Edge-of-P literature kill-pass: `notes/branching-regularity-tweaks.md` (#331)

**Reviewer:** Literature. **Date:** 2026-10-12. **Record type:** review record. It applies nothing. Do not merge until the Lead says so.

**Heads.** #331 head `f740df4` (open, one file), main `2b215ec`. No earlier review of #331 exists (no PR, no `reviews/branching*` file).

**Provenance.** This puts on the record the kill-pass verdict already sent to Chief of Staff, "PASS with notes (R1–R4, N1)". I re-read every item against the note at `f740df4` and against the sources. Changes from that summary are listed in §8.

**Marks.**
- **V-text:** wording or content checked this session, against the source text or its published abstract.
- **V-meta:** bibliographic data and topic checked only. Text not re-read.

## Verdict: PASS with notes

- **No injection.** Nothing in the note puts the Born rule in by hand. There is no Everett, Wallace or Carroll–Sebens framing; the note contains none of those names.
- **No prior owner.** Hadley, Stoica and Gielen–Wise are already set apart in Paper 1 (V-meta, via the record). None of them states "deterministic stretches with discrete branch points" as the motion rule for an observer.
- **The notes:**
  - R1–R4 are literature corrections.
  - N1 is a framing hazard.
  - N2 and N3 are quote-accuracy fixes, newly found in this pass.
- None of these blocks the note as a proposal.

## 1. "Agree for a stretch, then diverge" (candidate C) is standard GR

The structure itself is textbook. Past a Cauchy horizon, extensions of a maximal globally hyperbolic development are not unique:
- Choquet-Bruhat & Geroch, *Commun. Math. Phys.* 14 (1969) 329–335 (V-meta).
- Taub–NUT and Misner space; Chruściel & Isenberg, *Phys. Rev. D* 48 (1993) 1616–1628. Abstract: "in the Taub and Gowdy families there are nonisometric maximal extensions … spacetimes that have an arbitrarily large number of nonisometric maximal extensions" (V-text, abstract).
- Earman, *Bangs, Crunches, Whimpers, and Shrieks* (OUP 1995) (V-meta).

The note should say that the shape is borrowed (R2 string).

## 2. R1: the Gevrey citations do not back the Einstein claim

- **What the cited papers cover.** Colombini–De Giorgi–Spagnolo, *Ann. SNS Pisa* (4) 6 (1979) 511–559, treat second-order hyperbolic equations "avec des coefficients qui ne dépendent que du temps". Colombini–Jannelli–Spagnolo, *ibid.* (4) 10 (1983) 291–312, give Gevrey well-posedness for "a non-strictly hyperbolic equation with coefficients depending on time" (both V-text: titles and introduction or keywords). These are linear scalar equations with $t$-only coefficients. They are not quasilinear systems, and they are not Einstein's equations. The note itself discloses that it has not verified a Gevrey theorem for Einstein.
- **Gevrey is not what produces the divergence.** The bump argument works in any non-quasianalytic class, $C^\infty$ included. Smooth well-posedness with finite propagation speed already gives it.
- **Constraints.** A local change of Cauchy data has to keep satisfying the constraint equations. Corvino, *Commun. Math. Phys.* 214 (2000) 137–189, and Corvino & Schoen, *J. Differential Geom.* 73 (2006) 185–217, do exactly this kind of localized gluing (V-meta). Whether it works inside $G^s$ is unverified.

## 3. R2: does Chruściel–Isenberg already branch with no word changed? Checked; the answer is no for motion

The Taub–NUT and polarized-Gowdy extensions are analytic. Doboszewski's survey says the Taub–NUT and Gowdy extensions are analytic (V-meta for analyticity; V-text for non-isometry). So **host** non-uniqueness beyond a Cauchy horizon already exists in the analytic class.

It does **not** give branching of an observer's continuation. Analytic continuation along a single curve is unique, and the note's own §0 says so ("Analytic continuation along a single path has no monodromy"). A curvelet entering one extension has one germ continuation. The different extensions are different hosts, so in the framework they are relative-ensemble alternatives ($E(O)$), not branch points of motion.

R2 is therefore a context sentence, not a new branching mechanism.

## 4. R3: a string is not a distributional (delta) source

Geroch & Traschen, *Phys. Rev. D* 36 (1987) 1017–1031: "shells of matter—but neither point particles nor strings—can be described by metrics in this class" of metrics with distributional curvature (V-text, abstract). This is codimension 2, which is candidate A's $\Sigma$. So "a delta source" overstates what is defined. Vilenkin 1981 is correctly cited for the metric (V-meta).

## 5. R4: A's amplitude hook is borrowed quantum structure

The structure is: functions on the cover, which pick up a representation of $\pi_1$ under monodromy. This is the standard construction of quantum mechanics on multiply connected spaces:
- Schulman, *Phys. Rev.* 176 (1968) 1558–1569 (V-meta).
- Laidlaw & DeWitt, *Phys. Rev. D* 3 (1971) 1375–1378: "there are as many distinct propagators as there are scalar representations of the associated fundamental group" (V-text, abstract).

The note offers the construction only as "the only hook a later LT1 claim could use", which is not an injection. It should be marked as borrowed, though: a later LT1 claim built on it would import quantum structure rather than derive it. **Watch item.**

## 6. N1: framing hazard (Everett-style branching spacetimes)

Spacetimes that branch at discrete points are the usual way the literature models indeterminism and Everett-style branching in a relativistic setting:
- Belnap, "Branching space-time", *Synthese* 92 (1992) 385–434 (V-meta).
- McCabe, "The topology of branching universes", *Found. Phys. Lett.* 18 (2005) 665–676; keywords include "many-worlds interpretation" (V-text, abstract and keywords).

The note uses no such framing. If any candidate is pursued, Paper 1 and the versions must not borrow that reading. No string is proposed; this is a watch item.

## 7. N2 and N3 (new in this pass): quote accuracy

- **N2.** The v0.6 banner quote in §3 is not verbatim. The source bolds its first sentence and continues "…cannot create a branching edge; the CWS singleton comes from…". The note ends the quote with a full stop.
- **N3.** §1 says "(verbatim …)", but it drops the "(David's Tn)" labels. It also drops LT2's closing parenthesis "(the motivation clause; this is the contrast with Paper 1's trivial scheme)". The LT wording is David's as relayed, so it should either be marked as abridged or restored.

## 8. Changes from the summary sent to Chief of Staff

- **R2:** resolved. Chruściel–Isenberg gives analytic host non-uniqueness but no branching of motion, because continuation along a curve is unique. It becomes a context string (§3), not an open check.
- **R1:** "the divergence already happens with smooth data" is kept, sharpened to "any non-quasianalytic class". The Corvino–Schoen citation is marked V-meta.
- **N2 and N3** were added: two quote-accuracy fixes found on re-reading.
- **Source marks:**
  - Stoica, Hadley and Gielen–Wise: V-meta, via Paper 1's discussion.
  - Choquet-Bruhat–Geroch, Earman, Belnap, Corvino–Schoen and Schulman: V-meta.
  - Text not re-read this session for any of these.
- R3, R4 and N1 are unchanged in substance.

## 9. Strings (each OLD occurs once in `notes/branching-regularity-tweaks.md` at `f740df4`)

**R1**

OLD:
~~~
and Gevrey regularity is a natural class for hyperbolic Cauchy problems (Colombini, De Giorgi, Spagnolo, *Ann. Sc. Norm. Sup. Pisa* (4) 6, 511–559 (1979); Colombini, Jannelli, Spagnolo, *ibid.* (4) 10, 291–312 (1983)). Hence a Gevrey Cauchy datum can be altered by a Gevrey bump outside any given region,
~~~
NEW:
~~~
and Gevrey classes are natural for some hyperbolic Cauchy problems (Colombini, De Giorgi, Spagnolo, *Ann. Sc. Norm. Sup. Pisa* (4) 6, 511–559 (1979); Colombini, Jannelli, Spagnolo, *ibid.* (4) 10, 291–312 (1983); both are linear equations with time-dependent coefficients, not the Einstein equations). The bump argument needs only a non-quasianalytic class, so smooth data already give it; Gevrey adds nothing to the divergence. Any altered datum must still satisfy the constraint equations (localized gluing: Corvino 2000; Corvino–Schoen 2006, for smooth data; not verified within $G^s$). Granting that, a Cauchy datum can be altered by a bump outside any given region,
~~~

**R2**

OLD:
~~~
That is a genuine "agree on a stretch, then diverge" structure, and the divergence is caused by data, which is EKT-like in spirit (global, not local).
~~~
NEW:
~~~
That is a genuine "agree on a stretch, then diverge" structure, and the divergence is caused by data, which is EKT-like in spirit (global, not local). The structure is standard GR: extensions past a Cauchy horizon are non-unique (Choquet-Bruhat–Geroch 1969; Taub–NUT; Chruściel–Isenberg, *Phys. Rev. D* 48, 1616 (1993), with analytic examples; Earman 1995). In the analytic case this is non-uniqueness of the host, not of an observer's continuation, which stays unique along a curve (§0).
~~~

**R3**

OLD:
~~~
(distributional curvature, a delta source, so the analytic vacuum record gets a source term)
~~~
NEW:
~~~
(curvature concentrated on $\Sigma$, so the analytic vacuum record gets a source term; a codimension-2 string source is not well defined as a distribution in the Geroch–Traschen class, *Phys. Rev. D* 36, 1017 (1987))
~~~

**R4**

OLD:
~~~
monodromy representations do superpose linearly on functions over the cover, which is the only hook a later LT1 claim could use.
~~~
NEW:
~~~
monodromy representations do superpose linearly on functions over the cover, which is the only hook a later LT1 claim could use. That construction is borrowed quantum structure (quantum mechanics on multiply connected spaces: Schulman 1968; Laidlaw–DeWitt 1971), so a claim built on it would import, not derive, amplitudes.
~~~

**N2**

OLD:
~~~
"Finite $k$ is not the HOLE escape. Truncated-jet matching is vacuous at $k=1$ between distinct lumps, prohibitive at $k\ge2$ for curvature-changing jumps, and cannot create a branching edge."
~~~
NEW:
~~~
"**Finite $k$ is not the HOLE escape.** Truncated-jet matching is vacuous at $k=1$ between distinct lumps, prohibitive at $k\ge2$ for curvature-changing jumps, and cannot create a branching edge; …"
~~~

**N3**

OLD:
~~~
## 1. The test (verbatim, `notes/born-litmus-test.md`, L3)
~~~
NEW:
~~~
## 1. The test (`notes/born-litmus-test.md`, L3; David's wording as relayed, abridged: the "(David's Tn)" labels and LT2's closing parenthesis are omitted)
~~~

## Report line

Literature on #331 at `f740df4`: **PASS with notes**.
- No Born rule by hand, and no Everett, Wallace or Carroll–Sebens framing.
- R1: the Gevrey citations do not cover Einstein; Gevrey is not what produces the divergence; the constraints still have to be satisfied.
- R2: analytic host non-uniqueness, not branching of motion.
- R3: Geroch–Traschen; soften "delta source".
- R4: borrowed quantum structure; watch item.
- N1: Everett-style branching framing hazard; watch item.
- N2 and N3: quote accuracy.
