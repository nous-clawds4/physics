# Claim and math check: curvelet-induced topology (#305)

**Heads read (re-checked before filing):** #305 head `72d92f6` (commits `7ece683`, `72d92f6`; open, not merged); main `76e9ace`. **Verdict: HOLD (narrow).** The mathematics holds: the partition, the three component shapes, Hausdorffness, the jump classification and the limit proposition. The numerics reproduce exactly, and I confirmed them independently. Three strings are required:
- R1 and R2 are relay tags for David's question and for (Z-ix).
- R3 scopes "in effect (T0)".

R4 corrects a mislabelled sentence about self-targets. N1–N6 are optional.

**Scope.** Four files: `notes/curvelet-induced-topology.md` (1,505 words, str.split) and `notes/curvelet-induced-topology-scripts/` (`cit.py`, `run.sh`, `expected/cit.txt`). Paper 1 and v0.9.1 are untouched.

## 1. Partition, final topology, component shapes

**Sources.** `papers/geodesic-lifts.md`:
- **Prop. 3.2:** "There is a unique geodesic $\sigma_O$ in $P(O)$ with that initial $(p,u)$, and a unique analytic curvelet $\gamma_O$ … Every geodesic lift of $O$ in every $W\in E(O)$ coincides with $\gamma_O$ on a common positive interval."
- **Cor. 3.1:** "If $\gamma$ and $\gamma'$ agree on a subinterval of positive length, then they agree on every connected interval on which both remain defined."
- **Thm 3:** "real-analytic as a map into the inverse limit (a Fréchet space of jets)".

**Partition.** This holds. If two maximal curvelets pass through $Q$, both shifted curves are geodesic lifts starting at an occurrence of $Q$ with $Q$'s $u$. So each agrees with $\gamma_Q$ on a positive interval (Prop. 3.2), and then on the whole common domain, in both directions (Cor. 3.1). Every point of $V$ lies on exactly one maximal curvelet: its own $\gamma_Q$, with $\tau=0$ inside the open maximal domain (§5, §6.1). Curvelets that overlap on an interval coincide.
- The "star" of isolated meetings that Theorem 2 allows (geodesic-lifts §3) is excluded in $V$, as the note says, because $u$ is part of the point.
- The shift property needs the maximal domain to be intrinsic to the curve rather than to a world. §5 says "A world-dependent lifetime is not used". Maximal analytic continuation of a one-variable curve along $\mathbb R$ is unique. So $I_{\gamma(s)}=I-s$ holds, as the note states (its item 2, "not written").

**Final topology.** The note's definition is the standard one: $U$ is open iff every curvelet preimage is open. That is the finest topology making every curvelet continuous.
- Each component $C$ is clopen, because a curvelet's preimage of $C$ is either empty or its whole domain.
- Every curvelet in $C$ is a shift or restriction of the maximal $\gamma$, and shifts are homeomorphisms of $\mathbb R$. So $C$ carries the quotient topology $I/{\sim}$, and $\mathcal T_\gamma=\bigsqcup_C I_C/{\sim}$. Confirmed.

**Injectivity.** Curvelets need not be injective, and the note does not assume they are. If $\gamma(s)=\gamma(t)$ with $s<t$, the shift property gives $(t-s)$-periodicity and $I=\mathbb R$, since a nonempty open interval invariant under a nonzero translation is $\mathbb R$. The components are then $\mathbb R/P$, where $P$ is the period group.
- $P=\{0\}$ gives an interval (possibly all of $\mathbb R$).
- $P=T\mathbb Z$ gives a circle.
- $P=\mathbb R$ gives a point.

**Circles are not closed timelike geodesics.** They come from $V$'s identity (germs modulo pointed analytic diffeomorphism, §4). A non-circular bound Schwarzschild orbit returns to the same element of $V$ after one radial period, because a rotation maps the state at $\tau+T$ to the state at $\tau$. This is confirmed by C6, line 546: "revisited along a segment one radial period ($400.528$) later". A closed timelike geodesic in some world would also give a circle, but none is on record.

**Killing orbits are points, not circles.** A geodesic that is the orbit of a one-parameter isometry group (Schwarzschild circular orbits; ESU great circles; flat and de Sitter space) has $\gamma(\tau)=\gamma(0)$ for every $\tau$ as an element of $V$. So it is a point component, and the note lists exactly these. It is consistent with v0.9.1 §6.1 line 208, "circular orbits have $K\circ\gamma$ constant and no vertex", and with C21, where the slice omits the circular locus. "A point component has no slice points" is therefore right: $V^\tau$ needs $s\circ\gamma$ non-constant (line 200).

## 2. Dense periods

This is the note's own argument, and it is disclosed as "mine, not on record". It is sound once two standard steps are added. It also settles the irrational-winding worry: the case where the period group is dense but not all of $\mathbb R$ cannot occur.
- For each order $k$, let $f_k(\tau)$ be the $O(3)$-invariant polynomials of the Fermi jet coefficients (with $u$) at $\sigma(\tau)$. Re-centring Fermi coordinates at $\sigma(\tau)$ shifts only $x^0$, so the coefficients are those of Thm 3 and are analytic in $\tau$.
- $p$ is a period iff $f_k(\tau+p)=f_k(\tau)$ for all $k$ and $\tau$. The "if" direction needs two steps the note does not write:
  - (i) For a compact group acting linearly, polynomial invariants separate orbits. This is a standard fact (e.g. Onishchik–Vinberg, *Lie Groups and Algebraic Groups*, or Schwarz 1975 for smooth invariants).
  - (ii) Agreement in each finite order $k$ needs a rotation $g_k$. By compactness of $O(3)$, a limit point $g$ of the $g_k$ matches all orders at once. Since the metric is analytic, the full jet determines the oriented germ.
- So $P$ is the intersection of the period sets of continuous functions, which makes it a **closed** subgroup of $\mathbb R$: $\{0\}$, $T\mathbb Z$ or $\mathbb R$.
- If isometries generate a non-closed subgroup (an irrational winding on a torus of Killing orbits), it makes no difference. The states along the geodesic are then identified by those isometries, so $\gamma$ is constant: a point, not a dense-period non-Hausdorff quotient.
- The final topology therefore never produces the indiscrete $\mathbb R/P$ with $P$ dense. Optional N1 writes the closedness step into the note.

## 3. Gauge

The gauge cases are consistent with v0.9.1 and #301.
- "Fermi normal form modulo $O(3)$ gives back $V$" matches §4's identity.
- "'Which exterior' kept … No curvelet crosses regions I/III" is right: a timelike geodesic cannot pass between the two exteriors. It is consistent with #301 (T3) and with §7's "'Which exterior' is not a property of the target".
- The world-anchored labels and the $\mathrm{Obs}$ bullet are disclosed as not being v0.9.1's $V$.

## 4. The limit proposition and its premises

**Premises.** "Sources in $V^\tau$" is on record (§8.2 item 1). "$V^\tau$ discrete along each curvelet" is on record (§6.1, line 200: "discreteness per curvelet, in its open maximal domain").
- **Finite arm sets** are on record as v0.9.1's default: §9 "Exhaustion", line 415: "The default is finite stars." The note's own reason ("as EPP1's equal shares need") is a gloss, and it overlaps critic Q1. N2 cites the record instead.
- With continuum stars (soft Prop. 13, line 318) the proposition is not claimed, and the note says so.

**Proof.**
- **"If"**: a constant tail converges.
- **"Only if"**:
  - A convergent tail lies eventually in $Q$'s component. Point components have no slice points, so they host no Zeno tail.
  - On an interval or circle, finite arms let the window around $Q$ exclude every other slice point and every target of $Q$'s star except $Q$. So all late decisions are at $Q$, and every non-self arm leaves the window. A segment runs to the next slice point, which lies outside the window (or, on a circle, back at $Q$ after $T>2\delta$).
- This also covers your case of a backward jump along the same curvelet: its target is a star target, so the window excludes it. Even without that choice, each backward jump followed by a segment back to $Q$ costs a fixed positive $\tau$, and only finitely many fit in a Zeno tail. The characterisation "ends by repeating one self-loop at a single $\tau$" is correct.
- **Strict alternation (A).** §8.2 item 2 says "After a type-(ii) jump, a segment of positive proper time is traversed before the next branch decision". So under (A) a repeated self-loop at one $\tau$ is impossible, and no Zeno history converges. The note says self-loop tails need "without (A)", but it uses "(A)" without defining it. N3.

**Self-targets.** One substantive slip, fixed by R4. Under "through", a jump lands on its own source iff $\varepsilon=2D$. That depends only on $r$, so it holds at **every** turning point with $r_0=2786.4692$ or $r_0\approx2.000361$ ($c=0.1$), not just at apastra.
- At a **bound** apastron the germ is recurrent (a circle), so $(Q,Q)$ is type (i) and not in $R$ (§8.2 item 3). This is #292 case 2, which the note itself cites one sentence earlier.
- A genuine self-loop needs a **non-recurrent** turning point. For the C5 speed $v=0.3849$, the $r_0=2786.47$ turning point is a periastron of an unbound orbit ($E=\gamma_v\sqrt{1-2/r_0}\approx1.083>1$). The $r^*$ point is the apastron of a plunging orbit ($r<3$).
- So "apastra" is wrong on both counts. "#290 (T3)" is #290's hypothesis "(T3) $\Delta\ell$ is increasing", which clashes with #301's (T3).

## 5. Numerics

- **Reproduction.** In a fresh clone at `72d92f6`, with `python` pointing to Python 3.13.5 and mpmath 1.3.0, `sh run.sh` gives output **byte-identical** to `expected/cit.txt`.
- **Pins.** All three match: `cit.py` `a19b8a42d22a`, `run.sh` `76c334e5085e`, `expected/cit.txt` `0b896744278f`. There are no secrets or absolute paths.
- **Independent check.** I wrote my own Newton inversion of $\ell$ in $y=\sqrt{r-2}$ (with $d\ell/dy=2\sqrt{2+y^2}$) at 60 digits, and my own root for $r^*$.
  - **Distinct $L$:** 20,001 distinct radii at 50 digits, so 20,001 distinct $L_n=r_n\gamma_v v$.
  - **Gaps:** the minimum radius gap is $6.0\times10^{-16}$, which is $2.5\times10^{-16}$ in $L$.
  - **Distance from $L^*$:** $\min|r_n-r^*|=2.77\times10^{-13}$, which is $1.155\times10^{-13}$ in $L$. So none equals $L^*$.
  - **$r^*$:** $=2.000361017638$.
  - **Convergence in radius:** the chain does converge in $r$. It alternates about $r^*$ with a contraction of about $-0.9989$ per jump, coming within $10^{-6}$ of $r^*$ at $n=6062$. It never lands on $r^*$.
- Distinct $L$ means distinct components (since $L$ is constant along a curvelet), so there is no $\mathcal T_\gamma$ limit. C8 and the outward chain check out (§5).

## 6. Neutrality relative to #301

- **A fifth option, in effect.** $\mathcal T_\gamma$ is a topology on $V$ built only from record objects. #301 lists (T0)–(T3) and says the unlisted alternatives are deferral and "any topology or metric not on record, which #299 §1 says 'would be new'". $\mathcal T_\gamma$ is new to the record but adds no structure, so it is a candidate #301 does not list. The note's §7 presents it as an option, with costs and without a pick.
- **"In effect (T0)" needs scoping (R3).** It is true only for Zeno *limits* on the recorded examples (C5, C8, the toys), and only in that (Z-ix) then takes its partner's value. It is not (T0) as a topology: it defines "exists", makes §5's "discontinuous" a theorem, and differs at self-loop tails.
- **Wording.** The framing does not argue for (T0). "Yes, but it is nearly empty for Zeno" is a finding, not a lean. "Stronger than the Lead's guess" cites a guess that is not on record (N4).
- **Flag only: #301 pointer.** #301's brief (on main) should probably get a pointer to #305 if #305 merges. OLD on main: `The other is any topology or metric not on record, which #299 §1 says "would be new".` I'm not proposing text; that is for Geometry or the Lead.

## 7. Attribution, terms, guardrails

- **David's question.** The note says "the Physics Lead's question, prompted by David". The PR body says "prompted by David's question". Neither gives the relay or signature status the repo uses for David's words. R1.
- **(Z-ix).** It is David's reading but appears untagged. R2.
- **(M1).** Not cited.
- **"Mine".** The note says "This argument is mine". The PR says the note is from the Physics Lead, and the note also refers to "the Lead's guess". The author should be named (N4).
- **Label clashes.** "Yes, and T1" (the separation axiom) sits beside #301's (T1) (N5). "#290 (T3)" is covered by R4.
- **Hedge asymmetry.** The C5 outward table row hedges the identify-exteriors column ("inverse-limit") but not the labels-kept column (N6).
- **Terms.** "(A)" (N3), "N-a", "E-smuggling" and "partner" are used by pointer only. That is acceptable apart from (A).
- **Guardrails.** 0 χ/\chi and 0 forbidden words. No Born, $|a|^2$ or 1/N result; no Everett-vs-DW framing; no law of $R$. Paper 1 and v0.9.1 are untouched.

## Strings (each OLD occurs once in `notes/curvelet-induced-topology.md` at `72d92f6`)

**R1** (required; relay tag)
OLD: `*Answers the Physics Lead's question, prompted by David: can curvelet continuity`
NEW: `*Answers David's question, relayed by the Physics Lead (not signed; the exchange is not recorded in this repository): can curvelet continuity`

**R2** (required; (Z-ix) tag)
OLD: `and (Z-ix) is well-posed but equals its partner on every example on record: in effect (T0).`
NEW: `and (Z-ix) (David's reading, relayed, not signed; `notes/zeno-mass-scoping.md`) is well-posed but equals its partner on every example on record: for Zeno limits on those examples, in effect (T0).`

**R3** (required; scoping)
OLD: `For Zeno it matches (T0) in effect on every recorded example, differing only in defining "exists" and at self-loop tails.`
NEW: `For Zeno limits it matches (T0) in effect on every recorded example (C5, C8, the toys), differing in defining "exists" and at self-loop tails. As a topology it is not (T0): it makes non-self-loop jumps discontinuous and is not on #301's list.`

**R4** (required; self-targets)
OLD: `On the Kretschmann rule under "continue through", self-targets occur only at the $\varepsilon=2\Delta\ell$ apastra ($r_0=2786.4692$ and $\approx2.000361$ at $c=0.1$, #290 (T3)).`
NEW: `On the Kretschmann rule under "continue through", self-targets occur only at turning points with $\varepsilon=2\Delta\ell$ ($r_0=2786.4692$ and $\approx2.000361$ at $c=0.1$; #290, where (T3) is that note's hypothesis "$\Delta\ell$ is increasing", not #301's option). At a recurrent germ (a bound orbit, a circle) the pair is type (i) and not in $R$ (item 3), so a self-loop needs a non-recurrent turning point there: at the C5 speed, the unbound periastron at $r_0=2786.47$ or the plunging apastron at $r^*$.`

**N1** (optional; dense periods)
OLD: `invariants separate orbits of a compact group, so $\gamma$ would be constant. *This argument is mine, not on record.*`
NEW: `invariants separate orbits of a compact group, and by compactness of $O(3)$ one rotation matches every order at once, so $\gamma$ would be constant. The same step shows $P$ is the common period group of continuous functions, hence closed: $\{0\}$, $T\mathbb Z$ or $\mathbb R$, and a dense proper $P$ cannot occur (isometries generating a non-closed subgroup make $\gamma$ constant). *This argument is this note's own, not on record.*`

**N2** (optional; premise on record)
OLD: `Assume finite arm sets (as EPP1's equal shares need)`
NEW: `Assume finite arm sets (v0.9.1's default: "The default is finite stars", §9)`

**N3** (optional; define (A))
OLD: `without (A);`
NEW: `without (A) (strict alternation, §8.2 item 2, under which a jump is always followed by a segment of positive proper time);`

**N4** (optional; unrecorded guess)
OLD: `which is stronger than the Lead's guess: it also covers`
NEW: `which is stronger than the Physics Lead's expectation when posing the question (not recorded in this repository): it also covers`

**N5** (optional; label clash)
OLD: `Yes, and T1 (a disjoint union`
NEW: `Yes, and every point is closed (a disjoint union`

**N6** (optional; hedge symmetry)
OLD: `| C5 outward | not asked; ends | flat germ (inverse-limit) | flat germ | none |`
NEW: `| C5 outward | not asked; ends | flat germ (inverse-limit) | flat germ (inverse-limit) | none |`
