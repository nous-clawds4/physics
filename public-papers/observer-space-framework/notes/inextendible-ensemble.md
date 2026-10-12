# Inextendible ensemble: a scoping proposal

**Status:** proposal for David's decision; **not adopted**. Requested by David in Geometry's chat, 10:44–10:48 PM ET on 2026-10-11 (relayed, not signed); P-inext's wording and everything below are Geometry's, not David's. Written at main `dc8d374`. Bare § and C pointers are to v0.10 (`versions/v0.10-prose.md`); nothing in `versions/` or `papers/` is edited. No pick on the topology of $V$ ((T0)–(T4), deferred by David, #315), the throat convention, the law of $R$, (M1) or (A). No new numbers.

## 1. The proposal (P-inext)

Restrict $E_{\mathcal W}(O)$ and $E_M(O)$ (`mathematical-framework.md`; $E(O)$ in `papers/ensemble-labels.md`, Definition 2) to classes $[W,\iota]$ whose $W$ is **analytically inextendible**: there is no real-analytic isometric embedding of $W$ onto a proper open subset of another spacetime of the same class (connected, Hausdorff, second-countable, real-analytic, time-orientable Lorentzian 4-manifold; `ensemble-labels.md` §1).

- *Which inextendibility.* The record does not say. §4: "Whether $E_{\mathcal W}$ should be restricted to inextendible or maximal members is open." C25 calls the cone "inextendible, by a sketch" and names no regularity class; its holonomy argument is a connection argument, so it rules out extensions in which the Christoffel symbols extend continuously (in particular $C^2$ and analytic ones), not $C^0$ ones. Analytic is the class that fits the analytic lock, since members and occurrences are already analytic. It is also the weakest requirement: $C^0$-inextendible implies $C^2$-inextendible implies analytically inextendible, so a $C^0$ requirement would remove more hosts, and its effect on C25's cone is not established here.
- *What it does not change.* $O$, $P(O)$, the curvelet $\gamma_{O^u}$, $V$, $R$ and (a)'s $F(O)$ test are germ-level. P-inext only shrinks the set of hosts. The observer object (jet–patch lock) is untouched.
- *Small mismatch.* `ensemble-labels.md` §1 assumes time-orientable; §4 ("a connected real-analytic Lorentzian 4-manifold") does not. Adoption should fix one class.

## 2. Why

C24: "Minkowski minus the point $\sigma(\tau_0)$: the geodesic ends at $\tau_0$, for every $\tau_0\in(0,\infty)$." Such hosts end lifetimes at arbitrary $\tau$ with no geometric cause, which is why §5 already refuses world-dependent lifetimes ("punching holes makes lifetimes arbitrary"). Every hole-punched host extends by filling the hole, so P-inext removes all of them.

## 3. Costs

1. **Non-uniqueness.** One germ can have several inextendible hosts. In-record: Minkowski and C25's cone both host the flat germ. For analytic continuation of metrics in general, Misner (1967, "Taub-NUT space as a counterexample to almost anything", *Lectures in Applied Mathematics* 8, AMS, 160–169) discusses non-uniqueness of analytic continuation for metrics and gives an inequivalent analytic extension (text checked in NASA CR-70033, the 1965 report the chapter publishes; Chruściel & Isenberg note that many such familiar extensions are in fact isometric), and Chruściel & Isenberg (1993, *Phys. Rev. D* 48, 1616, doi:10.1103/PhysRevD.48.1616) give non-isometric maximal extensions in the Taub family (checked at abstract level; that these extensions are analytic, and so within P-inext's class, is from a secondary survey, Doboszewski 2017, not from the paper's text). P-inext keeps all such hosts and selects no world, so it is not E-smuggling.
2. **C25 survives.** Inextendibility alone does not make the times at which members stop carrying the observer discrete. §5 below adds a curved example.
3. **Global condition on a local object.** It is a condition on all of $W$. That is consistent, since nothing lock-side reads $E$, but it is new structure and would be stated as an adopted condition.
4. **Existence of a host for every germ: owed, expected.** $P(O)$ is a host. Zorn's lemma on chains of analytic isometric open embeddings gives a maximal one, provided the union of a chain stays in the class. Hausdorffness, analyticity and time orientation pass to the union. Second-countability of the union follows from Geroch's theorem (J. Math. Phys. 9, 1739 (1968), Appendix: a connected Hausdorff manifold with a $C^1$ connection has a countable basis), since the union is connected and carries an analytic Lorentzian metric.

## 4. Knock-ons

| Item | Under P-inext | Status (of the analysis, not a decision) |
|---|---|---|
| C24 | True as stated (it is about §4's ensemble "as written"; §6.1's continuum theorem adds "with no inextendibility requirement"), but its example leaves the restricted ensemble; it becomes the motivation. | settled |
| §6.1 continuum theorem, C25 | The conclusion (ensemble-timed vertices mark a continuum) survives, carried by C25 and the example in §5 below. | settled |
| §4 "$E_{\mathcal W}(O)$ is at least a continuum" | Rests on the continuum theorem, i.e. on hole punching. The flat germ keeps a continuum (cones with $\kappa\in(0,1)$, which the holonomy angle distinguishes); a general germ needs a new argument. | changed; owed |
| `ensemble-labels.md` Theorem 4(1) | The proof step "$\iota$ extends along that segment" assumes that the $W$-geodesic from $\iota(p)$ exists for every such $\tau$; C24's host contradicts the statement itself, not only the proof. That fails for hole-punched hosts and, at the given occurrence, also for the inextendible hosts of §5. (2) and (3) are unaffected. | open: needs a hypothesis whatever David decides; not edited here |
| E-smuggling refusal (§4, §10) | Unchanged; no member becomes load-bearing. | settled |
| §5 refusal of world-dependent lifetimes | Still needed: cones make lifetimes arbitrary too (C25, $\rho_0/\sinh\zeta$). If adopted, its reason would cite C25 alongside holes. | changed (wording only) |
| Zeno (§8.2 items 2, 8; C8) | Graph- and germ-level, so no host enters. A singular endpoint ends the curvelet's maximal analytic domain in every host. | unchanged |
| Throat (#297, C37) | The target is germ-level (#297 §2 item 2). P-inext removes the punched-sphere world that #297 §3's completed-world row sets aside ("A world with the sphere punched out lacks the path"). The far exterior does not become mandatory: $X\mapsto-X$ is an isometry of Kruskal that fixes $\partial_T$ and $e_\varphi$, so the far-side target germ also occurs in region I, and a one-exterior host such as Kruskal modulo $(T,X,\Omega)\mapsto(T,-X,-\Omega)$ contains it (that host's inextendibility is not checked here). | unchanged |
| #292 (D1/D2), #305 (T4) | Path- and germ-level; curvelet domains are taken in $P(O)$, not in hosts. | unchanged |

## 5. With P-inext, can $E_M$ change along a curvelet with no jump?

There are two readings, and they get different answers.

- **(H) Per member** (`ensemble-labels.md` Def. 3, hitchhiking): does a host $[W,\iota]$ carry the occurrence from $\tau_a$ to $\tau_b$?
- **(F) Fiber** (Def. 4): is $E_M(O_{\tau_b})=E_M(O_{\tau_a})$ as a collection, with multiplicity?

**(H): yes, still, at a continuum of times, with finite curvature and no jump.** The flat case is C25. A curved case, a sketch at C25's level: take Kruskal with $d\varphi^2$ replaced by $\kappa^2d\varphi^2$, $0<\kappa<1$, axis removed (κ-Kruskal). Off the axis it is locally Schwarzschild $M=1$. In the sphere factor, parallel transport around the latitude circle $\theta$ rotates by $2\pi(1-\kappa\cos\theta)\to2\pi(1-\kappa)\neq0$, so the axis cannot be filled in; $r=0$ is a curvature singularity, and Kruskal is maximal elsewhere. Take a Schwarzschild curvelet with $L\neq0$ and any $\tau_0$ in its Kruskal lifetime by which its orbit has swept an angle less than $\pi$ (both poles are conical, so the geodesic meets one of them once its swept angle reaches that pole's angular distance from $\sigma(0)$, which is below $\pi$). Choose the pole at the angular position of $\sigma(\tau_0)$: the orbit plane contains it, so the geodesic hits the axis at $\tau_0$ and ends there in κ-Kruskal, while in Kruskal it continues. Two inextendible hosts of the same germ disagree on the lifetime, at every such $\tau_0$ (a continuum), with $K=48/r^6$ finite there. This is non-uniqueness at work. In this sense, the earlier "yes" survives P-inext.

**(F): more delicate.**
- *Locally symmetric germs:* $O_\tau$ is constant along the curvelet (§6.1), so the fiber is constant with or without holes. Read as a fiber change, "punctured Minkowski hosts the observer at $\tau_a$ but not $\tau_b$" is wrong: it hosts the same flat germ elsewhere. It is an (H) statement.
- *Without P-inext:* for a germ that occurs only once in a host $N$, removing the closed ray $\{\sigma(\tau):\tau\ge\tau_0\}$ drops $N$ from the fiber for all $\tau\ge\tau_0$, at any $\tau_0$. P-inext removes these hosts.
- *κ-Kruskal:* off-axis germs recur under the local rotations, so every later $O_\tau$ occurs elsewhere and the fiber does not change. Killing-cone and quotient constructions preserve germs in this way.
- *Isolated-instant loss (sketch, not pinned):* take a maximal host $N$ and an analytic timelike 2-surface $\Sigma$ through $\sigma(\tau_0)$ whose linking loop is sent to $1$ by some homomorphism $H_1(N\setminus\Sigma)\to\mathbb Z/2$. The branched double cover $W$ of $N\setminus\Sigma$ is analytic. It is plausibly inextendible, since circles of radius $\epsilon$ about $\Sigma$ have length about $4\pi\epsilon$, which no smooth filling allows. $W$ contains every germ of $N\setminus\Sigma$. If $O_{\tau_0}$ occurs in $N$ only at $\sigma(\tau_0)$, then $W$ drops out of the fiber exactly at $\tau_0$, and $\tau_0$ is arbitrary.
- *Loss over an interval (persistent):* **owed.** It needs an inextendible analytic host that ends the curvelet with bounded geometry and contains none of the later germs anywhere. Cones, quotients and branched covers do not do this. The place to look is non-unique continuation across a Cauchy horizon (Taub–NUT type); that is not checked here.
- *Curvature singularities* end the curvelet's maximal analytic domain itself (C8's FLRW instance is one case). That ends the observer in every host, not membership.

**Answer.** With P-inext, the members that carry the observer still change at a continuum of times with no jump: C25 flat, κ-Kruskal curved, each inextendible by sketch. The fiber $E_M(O_\tau)$ never changes for locally symmetric germs. For generic germs it plausibly loses a host at isolated, arbitrary instants (sketch above). Whether it can lose one over an interval is owed. Either way, P-inext gives no discrete set of change times and does not tie membership changes to jumps.

## 6. Questions for a critic

1. Is analytic inextendibility the right class, and do the C25 / κ-Kruskal holonomy sketches need to become proofs before P-inext rests on them?
2. Should `ensemble-labels.md` Theorem 4(1) be restated with "while the $W$-geodesic exists", and which of (H) and (F) does David mean by $E_M$?
3. Is the branched-cover isolated-instant loss sound (inextendibility, single occurrence of $O_{\tau_0}$), and does any inextendible host realise a persistent fiber loss?
