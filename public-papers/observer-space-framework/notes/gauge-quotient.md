# Gauge quotient: a scoping proposal

**Status:** proposal for David's decision; **not adopted**. Requested by David in Geometry's chat, 11:07–11:08 PM ET on 2026-10-11 (relayed, not signed). The wording of the proposal (Q) and everything below are Geometry's, not David's. Written at main `85f385d`. Bare § and C pointers are to v0.10.1 (`versions/v0.10.1-prose.md`, in review). The §4 identity sentences ("Lump identity", "Oriented observer") and §7's "which exterior" sentence are byte-identical in v0.9.1, v0.10 and v0.10.1. Nothing in `versions/` or `papers/` is edited, and there are no new numbers.

This note picks nothing on the topology of $V$ ((T0)–(T4), deferred by David, #315), the throat convention, the law of $R$, (M1), (A), or inextendibility (#320, pending). The one place where adopting (Q) would touch #315 is flagged in §2.

## 1. The proposal (Q), and what the record already says

**(Q).** An observer state is a class of pointed coordinate data $(j^\infty_p g,\,u)$, with $u$ future unit timelike at $p$. Two such data are the same state iff some germ of real-analytic diffeomorphism $\varphi$ with $\varphi(p)=p'$ satisfies $\varphi^*g'=g$ near $p$ and $d\varphi_p(u)=u'$; that is, $u$ is pushed forward.

- **Jet-group form.** Letting the formal jet group act on coordinate jets gives the same classes (sketch). A formal $\hat\varphi$ with $\hat\varphi^*j'=j$ carries formal geodesics to formal geodesics. So it is the Taylor series of $\exp'_{p'}\circ d\hat\varphi_p\circ\exp_p^{-1}$, which is convergent. Its pullback metric has the same jet as $g$, so by analyticity the two agree near $p$.
- **Equivalently,** these are Riemann-normal-coordinate jets in an orthonormal frame, modulo $O^{+}(1,3)$ acting on the frame, which moves the jet and $u$ together.

**The record already states this.**
- **Paper 1** (`papers/observer-space-ontology.md`): "Gauge is settled as physics, not as a coordinate recipe. The object is that jet/patch pair, the lump. Two presentations of the same lump are the same observer. A diffeomorphism that moves the lump is a different observer."
- **`papers/obs-as-a-set.md`:**
  - Definition 6 ($\sim_L$) is (Q) word for word: $\varphi(p)=p'$, $d\varphi_p(u)=u'$, $\varphi^*g'=g$. It is stated "on coordinate jets" too.
  - Theorem 10(2) puts $\mathcal P/{\sim_L}$ in canonical bijection with the "germ-equivalence classes of pointed simply-connected real-analytic Lorentzian patches". So **(Q) coincides with Theorem 10**.
  - "Moves the lump" is defined there as "not pointed", which (Q) excludes.
- **§4:**
  - "Two presentations that differ by a pointed analytic diffeomorphism renaming the same local patch are the same *lump*. Gauge is this identity."
  - $O^u$ is the class of triples under pointed analytic diffeomorphisms that carry $u$: "**$u$ is taken modulo the isotropy of the germ**".
- **§7:** "“Which exterior” is not a property of the target, since $V$ consists of germs modulo pointed diffeomorphism."

**What is left open in the record** is gauge as a *space* or named home, not gauge as identity:
- `papers/obs-as-a-set.md`: "Gauge as a home for $\mathrm{Obs}$ *as a space* stays open."
- `papers/obs-as-a-space.md`: "Gauge as a *named home* … stays open."
- `public-essays/mathematical-foundations/versions/v0.3.md`: "Gauge beyond germ isotropy is open (v0.6 §2)."
- The one live identity-level alternative is #297 §3's row "Gauge: "which exterior" kept", which #301 lists as (T3).

**Two quotients that should not be confused.**
- (Q) is the **diffeomorphism quotient**. It acts on the jet and $u$ together, and the only freedom it leaves in $u$ is the germ's isotropy.
- A **frame quotient on $u$ alone** (Lorentz acting on $u$ with the jet held fixed) is a different and coarser identification. It would identify every $O^u$ at one lump, collapse $V$ toward $\mathrm{Obs}$, and erase the oriented split, curvelets and C9's count. The record rejects frame quotients of all metrics (Theorem 10(4)). (Q) is not one, and nothing here proposes one.

So (Q) is the record's working identity. Adopting it would record it as David's ruling and close the one identity-level alternative (labels kept).

## 2. What (Q) settles

| Place | Under (Q) |
|---|---|
| #297 §3, gauge rows | The far-exterior through-throat target **is** the near-side turning-point state at $r'$ ($X\mapsto-X$, $\theta\mapsto\pi-\theta$). Existence never turned on gauge; only identifications did. |
| #301 (T3) | (Q) is (T3)'s "identify" side, which is "v0.9.1's stated identity". **Adopting (Q) decides (T3)**, an item that #315 keeps on record under the topology deferral. (Q) adopts no topology, but the ruling should say whether it means to decide (T3). |
| #299 inward "through" chains | "only modulo "which exterior"" goes away: the two accumulation points are one germ, the near-throat $r^*$. Whether that germ is a *limit* still needs a topology, which is deferred. Under (T4) there is still none (#301). |
| #305 (T4) gauge cases | Unchanged. "No curvelet crosses regions I/III". |
| #318 S3 / v0.10.1 P13 clauses | The three statements (#290 A6, §11's "iff $r'=r_0$", the Proposition's "The exception is real") hold without the "(on §4's identification …)" hedge. On a labels-kept $V$ the exception fails (a) (#318). S4 holds on either reading, since $K$ separates the lumps. |
| (a) / $F(O)$ | Defined on lumps, so unchanged. Under (Q), the S3 exception passes (a). |
| $R$, Kretschmann rule | Built from $K$, $\nabla K$, $u$ and continuation along a geodesic, all natural under pointed isometries, so well defined on classes. A source's isotropy fixes its target class. |
| #292 D1/D2 | "D1 and D2 coincide on the Kretschmann rule … under either throat convention" holds as written. The near-throat self-target still carries no decision. On a labels-kept $V$ there would be no self-targets at all. |
| $E_{\mathcal W}$, $E_M$, $E(O)$ | Def. 2 already identifies pairs under pointed isometries. An occurrence of one presentation composed with $\varphi$ is an occurrence of the other, so $E$ is a function of the class. Sibling multiplicity $M(W,O)$ is untouched. |
| C9, C10, C28, C33, C37 | Already stated "modulo isotropy" or on §4's identity. Unchanged. |

## 3. Costs

1. **Singular quotient.** The isotropy of $(j,u)$ jumps between strata, so the classes form an orbifold-like stratified set, not a manifold.
   - Flat (and the locally symmetric germs, at their own isotropy): $O(3)$.
   - A Schwarzschild radial germ: $O(2)$.
   - A Schwarzschild turning point with $v\ne0$: $\mathbb Z/2$ (the reflection $\theta\mapsto\pi-\theta$ that fixes $e_\varphi$).
   - A generic germ: trivial.

   Theorem 16's Fermi-slice $/O(3)$ topology is Hausdorff on this set, but no manifold structure is claimed anywhere. Any topology option, measure or $C^k(\mathrm{Obs})$ must handle the strata. This is a cost to every option in #301, not a pick among them.
2. **Counts.** $R\subset V\times V$, so $\lvert B_R\rvert$ counts classes. That is already the record's convention (C9: 3 unquotiented, 2 modulo isotropy).
   - *Merged arms on the Kretschmann rule: none.* Both arms keep $v$ and land on turning points (#290 T1), and A6 says a turning-point germ is fixed by $(r,u^r,v)$. The outward target has $\Delta\ell=\Delta\ell(r_0)+\varepsilon$. The inward target has $\Delta\ell(r_0)-\varepsilon$, or $\varepsilon-\Delta\ell(r_0)$ through the throat. Equal radii would need $\Delta\ell(r_0)=0$ or $\varepsilon=0$, and neither holds for $r_0>2$ and $c>0$. (This is algebra, so nothing is pinned.)
   - *Self-loops.* The identification is what makes the far self-target (2786.4692 at $c=0.1$, #290) and the near-throat $r^*$ self-targets. Both are already on record under §4.
   - Countability of stars only improves under a quotient.
3. **$u$ stays physical.** Only the isotropy acts on $u$. At a germ with trivial isotropy, distinct $u$ are distinct states.
4. **One wording tension.** Paper 1: "One jet can sit in more than one global topology. The resulting patches agree to all orders at the point and are not the same lump." Under (Q) and Theorem 10 they are one state, and the difference lives in $E(O)$ ("Those extra patches are the relative ensemble"). So Paper 1's "lump" in that sentence must mean the grown patch.

## 4. Knock-ons

| Item | Status (of the analysis, not a decision) |
|---|---|
| Identity of states (§4, Paper 1, Theorem 10) | settled (unchanged; (Q) is the record's identity) |
| "Which exterior" kept: #297 §3 row, #301 (T3) | changed: closed if (Q) is adopted as stated; flagged against #315 |
| #299 inward chains | changed: one candidate limit germ; existence still awaits a topology |
| P13 / S3 hedges in v0.10.1 | changed: removable if adopted (no `versions/` edit here) |
| $R$, Kretschmann rule, (a), D1/D2, C-rows, $E$ | settled (well defined; no arm merges) |
| Gauge as a named space, a measure, $C^k(\mathrm{Obs})$ | still open (stratified quotient) |
| Paper 1 "not the same lump" sentence | still open (wording) |

## 5. Questions for a critic

1. Should adopting (Q) decide (T3) explicitly, or should (T3)'s labels-kept side stay on record as a rejected-for-now alternative under #315?
2. Is the formal-to-convergent sketch in §1 (formal isometries as exponential-map conjugates) enough, or should `papers/obs-as-a-set.md` be cited only in its analytic-germ form?
3. Does the stratified quotient (isotropy $O(3)$, $O(2)$, $\mathbb Z/2$, trivial) block any option in #301 outright, or only cost each one equally?
