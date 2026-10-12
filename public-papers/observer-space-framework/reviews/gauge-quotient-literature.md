# Literature claim check: `notes/gauge-quotient.md` (#324)

**Reviewer:** Literature. **Date:** 2026-10-12. **Record type:** review record. It applies nothing. Do not merge until the Lead says so.

**Heads read, re-checked before filing:**
- #324 head `f7335fd` (unchanged), open, one file, written at main `85f385d`.
- main `2b215ec`. The commits since `85f385d` touch none of the files quoted below except the v0.10.1 status (N4).

**Existing reviews.** None on main or in an open PR: no `reviews/gauge-quotient*` file and no other PR on this note. An unpushed local draft of this review (branch `literature-gauge-quotient`) was reused and re-verified; two of its items (a quote flag and a Theorem 16 flag) did not survive re-checking and are dropped.

**Rules.** I pick no topology ((T0)–(T4)), no throat convention, no law of $R$, and nothing on (M1) or (A). I decide nothing on (Q).

**Verdict: HOLD (narrow).** Two fixes are needed:
- **R1:** the claimed Paper 1 "tension" is not a tension. Paper 1's sentence is about the relative ensemble, not about gauge.
- **R2:** neutrality on (T3). The note states only the cost of quotienting as such, not #301's cost of the "identify" side.

Claims (a) and (c) are confirmed. Claim (b) is correctly flagged for David. Claim (d) is right in substance, but "orbifold-like" is loose (S1). Attribution and the guardrails are clean.

## 1. Claim (a): (Q) is already the record's identity

Every quote in the note was matched on main; all are exact except "word for word" (N1).
- **Paper 1** (`papers/observer-space-ontology.md`): "Gauge is settled as physics, not as a coordinate recipe. The object is that jet/patch pair, the lump. Two presentations of the same lump are the same observer. A diffeomorphism that moves the lump is a different observer." Exact.
- **`papers/obs-as-a-set.md` Definition 6.** It has $\varphi(p)=p'$, $d\varphi_p(u)=u'$, $\varphi^*g'=g$ on connected open neighbourhoods $V\ni p$, $V'\ni p'$. That is (Q) in substance; it is stated with neighbourhoods rather than germs, so "word for word" overstates (N1). The source's wording is "On coordinate jets", capitalised.
- **"Moves the lump"** is defined as "$\varphi(p)\ne p$ if written as a self-map of one chart, or, equivalently, that is not pointed". Correct.
- **Theorem 10(2)** gives "germ-equivalence classes of pointed simply-connected real-analytic Lorentzian patches". Exact, so **(Q) = $\mathcal P/{\sim_L}$**, confirmed.
- **Theorem 10(4)** rejects "a frame quotient of all metrics", since "Those quotient by maps that need not fix a marked $(p,u)$". The note's "frame quotient on $u$ alone" moves $u$ with the jet fixed, so it is such a map class and the citation holds.
- **v0.10.1 §4.** "Two presentations that differ by a pointed analytic diffeomorphism renaming the same local patch are the same *lump*. Gauge is this identity." and "**$u$ is taken modulo the isotropy of the germ**" are both exact. The "Lump identity" and "Oriented observer" lines are byte-identical in v0.9.1, v0.10 and v0.10.1 (same hash), as the note says.
- **v0.10.1 §7.** "is not a property of the target, since $V$ consists of germs modulo pointed diffeomorphism." is exact and byte-identical in the three versions.
- **The open items:**
  - obs-as-a-set: "Gauge as a home for $\mathrm{Obs}$ *as a space* stays open."
  - obs-as-a-space: "Gauge as a *named home*".
  - MF v0.3: "Gauge beyond germ isotropy is open (v0.6 §2)."
  - #297: "Gauge: "which exterior" kept".

  All exact.
- **Jet-group and normal-coordinate forms.** Labelled a sketch. A formal isometry carries formal geodesics to formal geodesics, so in normal coordinates it is linear and fixed by its 1-jet; the residual group is the time-orientation-preserving Lorentz group on the frame. That is consistent with Theorem 10(3) and with Theorem 16's Fermi-slice $O(3)$, which is the stabiliser of $u$.
- **Conclusion.** (Q) is the identity the record already states, at the level of sets. What stays open on the record is gauge as a space or named home, as the note says.

## 2. Claim (b): (Q) decides #301 (T3) — David's call

- **The record.** #301 (`notes/topology-decision-brief.md`) says (T3) "is not a topology but a choice of what the points are", and that its identify side "is v0.9.1's stated identity". So adopting (Q) as a ruling closes (T3)'s labels-kept side. The note says so in bold ("**Adopting (Q) decides (T3)**") and flags it against #315: "the ruling should say whether it means to decide (T3)". Critic question 1 puts the choice to David. **Flag for David: deciding (T3) is his call.** Nothing in the note or in this review makes it.
- **Consistency with #315.** #315's ruling, as recorded in #301: "no topology on $V$ is adopted … and options (T0)–(T4) stay on record for later". The note adopts no topology and says that (Q) "adopts no topology". Two points for the ruling:
  - Deciding (T3) would take one item off a list that #315 keeps "on record for later", so it amends #315's record, not just v0.10.1. That is why it needs David, as the note says.
  - Under the deferral (#301's (T0) row: "The history ends at its accumulation; no limit is asked for"), "(T3)'s question does not arise" for #301's worked Zeno example. So deciding (T3) now would move no Zeno outcome; it changes only the identity-level rows (#297 §3, the P13/S3 hedges, D1/D2 self-targets). The note's #299 row is consistent with this ("Whether that germ is a *limit* still needs a topology, which is deferred").
- **Neutrality (R2).**
  - §1 ends "So (Q) is the record's working identity", which is accurate; #301 says the same.
  - But the note's costs (§3) are costs of quotienting as such: strata, counts, and $u$.
  - #301 states one cost per side of (T3), and the note omits the "identify" side's: "Identifying merges two states that a completed spacetime separates (regions I and III); keeping labels needs a $V$ finer than §4's." (exact).
  - For a proposal that would decide (T3), both costs belong in front of David. R2 quotes #301's line in the (T3) row.
- **The rows that depend on (T3)** (#297 §3, #299, #318 S3/S4, D1/D2) are stated "under (Q)", and they agree with their sources.
- **The #299 quote** "only modulo "which exterior"" is exact (`notes/zeno-well-posedness.md`, inward-chain paragraph). The two accumulation points sit around the near-throat self-target $r^*=2.00036101764$ at $c=0.1$ (#299). Note that #299 also has "The far self-target $r^*=2786.4692$" in the same paragraph; the note's "near-throat $r^*$" names the right one.

## 3. Claim (c): no Kretschmann arms merge

**Confirmed (algebra; nothing pinned).**
- Both arms keep $v$ and land on turning points (#290 T1).
- "the germ is determined by $(r,u^r,v)$ up to isometry" is exact (#290 A6; also in #299). With a turning point ($u^r=0$) and $v$ kept, two targets are one class under (Q) iff they have equal $r$.
- **Radii.** Outward: $\Delta\ell(r_0)+\varepsilon$. Inward: $\Delta\ell(r_0)-\varepsilon$, or $\varepsilon-\Delta\ell(r_0)$ through the throat. Equality forces $\varepsilon=0$ or $\Delta\ell(r_0)=0$; neither holds for $r_0>2$, $c>0$. At $\varepsilon=\Delta\ell(r_0)$ the inward target sits at the throat sphere, still a different radius.
- **C9's 3-versus-2** (flat lump) is the record's existing isotropy convention, as the note says.

## 4. Claim (d): a stratified, "orbifold-like" quotient

**The isotropy groups listed are right** (stabiliser of $(j,u)$ among local isometries fixing $p$, preserving time orientation):
- **Flat with $u$:** $O(3)$, the stabiliser of $u$ in the orthochronous Lorentz group.
- **Schwarzschild, $u$ radial (or static):** $O(2)$, rotations and reflections about the radial axis. The point-fixing time reflection reverses $u^t$, so it is excluded.
- **Turning point with $v\ne0$:** $\mathbb Z/2$, the reflection $\theta\mapsto\pi-\theta$ (in the plane of $e_r,e_\varphi$). $\varphi\mapsto-\varphi$ flips $v$; combining it with time reflection makes $u$ past-directed. Neither is in the isotropy.
- **Generic germ:** trivial.
- **The parenthesis** "the locally symmetric germs, at their own isotropy" sits next to "$O(3)$" and can be read as giving them $O(3)$. They need not have it (N3).

**Theorem 16** (`papers/obs-as-a-space.md`) says the Fermi-slice quotient "is therefore Hausdorff whenever $\mathcal{P}_F$ is" and ends "the quotient topology on that slice is a well-defined Hausdorff topology on the set of lumps". The note's "Hausdorff on this set" matches the last sentence. Checked, no change.

**Literature** (analogues; none is about pointed analytic jets). Marks: V-text = wording or content checked against the source text this session; V-meta = bibliographic data and section/topic checked, text not re-read.
- **Orbit-type stratification for proper / compact actions.** J. J. Duistermaat & J. A. C. Kolk, *Lie Groups*, Universitext, Springer 2000, Ch. 2 "Proper Actions", §2.3 "Slices", §2.7 "The Stratification by Orbit Types" (p. 111) (V-meta, table of contents). M. J. Pflaum, *Analytic and Geometric Study of Stratified Spaces*, LNM 1768, Springer 2001 (V-meta).
  - This fits each finite jet level on the Fermi slice: $O(3)$ is compact and acts linearly on $J^k$ (Theorem 16's proof: "continuous linear action on each $J^k$").
  - On the inverse limit no slice or stratification theorem is established in the record, and the note claims no manifold structure. That is right.
- **Slices for non-free actions.** R. S. Palais, "On the existence of slices for actions of non-compact Lie groups", *Ann. of Math.* 73 (1961) 295–323 (V-text, introduction): for a Lie group $G$, "the Cartan G-spaces are precisely those G-spaces with compact isotropy groups for which there is a slice through every point." All isotropy groups in the note are compact, so the slice picture is the standard one at each finite level.
- **Metrics modulo diffeomorphisms, stratified by symmetry.** J.-P. Bourguignon, "Une stratification de l'espace des structures riemanniennes", *Compositio Math.* 30 (1975) 1–41 (V-text, §1.1 and Théorème VI.4): metrics on a fixed compact $M$ modulo $\mathcal D$, stratified by the conjugacy class of the isometry group. D. G. Ebin, "The manifold of Riemannian metrics", *Proc. Sympos. Pure Math.* 15 (AMS 1970) 11–40, gives the slice theorem used there (V-meta).
- **Lorentzian analogue.** A. E. Fischer, J. E. Marsden & V. Moncrief, "The structure of the space of solutions of Einstein's equations. I. One Killing field", *Ann. IHP A* 33 (1980) 147–194 (V-text, p. 148): "The set E has (nontrivial) quadratic, i.e., conical singularities near spacetimes with Killing fields."
- **Orbifolds.** I. Satake, "On a generalization of the notion of manifold", *PNAS* 42 (1956) 359–363 (V-meta): locally a quotient of $\mathbb R^n$ by a **finite** group.

These support "singular at symmetric germs". But an orbifold needs finite isotropy, and here it is $O(3)$ or $O(2)$ at flat and radial germs. So "orbifold-like" is accurate only on the $\mathbb Z/2$ and trivial strata. S1 states it as an orbit-type stratification. The global-metric results (Bourguignon, Ebin, FMM) are for compact manifolds or compact Cauchy surfaces, not pointed germs, so they are analogues only.

## 5. The Paper 1 "tension" (R1)

Geometry's suspicion is right: the sentence concerns non-simply-connected patches (the relative ensemble), not gauge.
- **What Paper 1 says.** "One jet can sit in more than one global topology. The resulting patches agree to all orders at the point and are not the same lump. Those extra patches are the relative ensemble, not a second elementary observer. A macroscopic observer, a human, is the jet with the patch allowed to grow, the continuation run separately in each topology."
- **What its lump is.** "The patch is the jet written as a lump of spacetime", and the patch is "the unique simply-connected real-analytic patch determined by that jet". The novelty paragraph: "the infinite jet is the unique simply-connected analytic patch; extra topologies are a relative ensemble, not a second elementary observer". And: "The tree does not branch because an ambient four-manifold has two topology labels. It branches when the simply-connected analytic patches disagree."
- **So "the resulting patches"** are the jet's continuations grown in each global topology. Agreeing to all orders at the point, their simply-connected germs coincide by analyticity; what differs is the grown, in general non-simply-connected, patch. Those are $E(O)$ members, not presentations of the lump.
- **(Q) and Theorem 10 make the same separation.** Theorem 10(2) works with simply-connected patches and "isomorphism classes of maximal simply-connected patches $P(O)$", and Theorem 10(5) is "(Not $E(O)$.)".
- **Conclusion.** The sentence is not about gauge, and (Q) leaves it true as written. The note's "Under (Q) and Theorem 10 they are one state" conflates the patches with the jet: the jet is one state, the patches are not. No Paper 1 wording change is needed, and Paper 1 is not to be edited in any case.

## 6. Attribution and guardrails

- **Attribution.** "Requested by David in Geometry's chat, 11:07–11:08 PM ET on 2026-10-11 (relayed, not signed). The wording of the proposal (Q) and everything below are Geometry's, not David's." There is no David quote, so no quote needs checking against his words; nothing is recorded as signed. Status: "proposal for David's decision; **not adopted**". The knock-on table keys its marks as "of the analysis, not a decision". #315's quoted ruling is not re-quoted in the note.
- **Guardrails.**
  - The forbidden Greek letter and its TeX macro: 0 in the note, 0 in the PR body.
  - No Born, $|a|^2$ or $1/N$ result; no Everett-versus-Deutsch–Wallace framing; no law of $R$.
  - Nothing picked on (T0)–(T4), the throat, (M1) or (A); (T3) is flagged, not picked.
  - `papers/`, `versions/` and Paper 1 are untouched (diff is one file under `notes/`).
  - The note is 1,487 words.
- **Stale pointers since `85f385d`** (N4): v0.10.1 is now the current draft (P14), and #320 was adopted (#328, relayed, not signed).

## 7. Strings (each OLD occurs once in `notes/gauge-quotient.md` at `f7335fd`)

**R1 (required; Paper 1)**

OLD:
~~~
4. **One wording tension.** Paper 1: "One jet can sit in more than one global topology. The resulting patches agree to all orders at the point and are not the same lump." Under (Q) and Theorem 10 they are one state, and the difference lives in $E(O)$ ("Those extra patches are the relative ensemble"). So Paper 1's "lump" in that sentence must mean the grown patch.
~~~
NEW:
~~~
4. **No tension with Paper 1.** Paper 1: "One jet can sit in more than one global topology. The resulting patches agree to all orders at the point and are not the same lump. Those extra patches are the relative ensemble, not a second elementary observer." The patches there are the jet's continuations grown in each global topology, in general not simply connected; Paper 1's lump is the unique simply-connected patch ("the infinite jet is the unique simply-connected analytic patch; extra topologies are a relative ensemble"). So the sentence separates relative-ensemble members from the lump, as Theorem 10 does (10(2) on simply-connected patches; 10(5) "Not $E(O)$"). It concerns non-simply-connected patches, not gauge, and (Q) leaves it true as written.
~~~

OLD:
~~~
| Paper 1 "not the same lump" sentence | still open (wording) |
~~~
NEW:
~~~
| Paper 1 "not the same lump" sentence | settled (about grown, non-simply-connected patches in the relative ensemble, not gauge; Paper 1 unchanged) |
~~~

**R2 (required; neutrality on (T3))**

OLD:
~~~
(Q) adopts no topology, but the ruling should say whether it means to decide (T3).
~~~
NEW:
~~~
(Q) adopts no topology, but the ruling should say whether it means to decide (T3). #301 states the cost on each side: "Identifying merges two states that a completed spacetime separates (regions I and III); keeping labels needs a $V$ finer than §4's."
~~~

**S1 (suggested; stratification)**

OLD:
~~~
so the classes form an orbifold-like stratified set, not a manifold.
~~~
NEW:
~~~
so the classes form a set stratified by isotropy (orbit) type, not a manifold, and not an orbifold where the isotropy is $O(3)$ or $O(2)$ (orbifolds need finite isotropy). At each jet level on the Fermi slice the residual $O(3)$ is compact and acts linearly (`papers/obs-as-a-space.md` Theorem 16), the standard setting for orbit-type stratification; no such result is claimed on the inverse limit.
~~~

**N1 (Definition 6)**

OLD:
~~~
Definition 6 ($\sim_L$) is (Q) word for word:
~~~
NEW:
~~~
Definition 6 ($\sim_L$) is (Q) in substance (stated with connected neighbourhoods $V\ni p$, $V'\ni p'$ rather than germs):
~~~

OLD:
~~~
It is stated "on coordinate jets" too.
~~~
NEW:
~~~
It is also stated "On coordinate jets".
~~~

**N3 (isotropy list)**

OLD:
~~~
Flat (and the locally symmetric germs, at their own isotropy): $O(3)$.
~~~
NEW:
~~~
Flat: $O(3)$ (other locally symmetric germs have their own isotropy, not always $O(3)$).
~~~

**N4 (stale pointers; optional, since the note records "Written at main `85f385d`")**

OLD:
~~~
Bare § and C pointers are to v0.10.1 (`versions/v0.10.1-prose.md`, in review).
~~~
NEW:
~~~
Bare § and C pointers are to v0.10.1 (`versions/v0.10.1-prose.md`, now the current draft, P14).
~~~

OLD:
~~~
inextendibility (#320, pending)
~~~
NEW:
~~~
inextendibility (#320, adopted by David, relayed, not signed; #328)
~~~

**PR body (not a file).** "orbifold-like" and the Paper 1 "wording tension" should follow S1 and R1.

## Report line

Literature on #324 at `f7335fd`: **HOLD (narrow)**.
- **(a)** confirmed: (Q) = obs-as-a-set Def. 6 / Theorem 10 = Paper 1's lump principle = §4 and §7 (N1 only).
- **(b)** (Q) decides (T3). Correctly flagged as David's call, consistent with #315 (no topology adopted; under the deferral (T3) moves no Zeno outcome). R2 needed for neutrality.
- **(c)** confirmed: no Kretschmann arms merge.
- **(d)** right in substance; the literature supports singular orbit-type strata at symmetric germs, but it is not an orbifold where the isotropy is $O(3)$ or $O(2)$ (S1).
- **R1:** Paper 1's "not the same lump" concerns non-simply-connected relative-ensemble patches, not gauge; no tension.
- **Attribution and guardrails:** clean.
