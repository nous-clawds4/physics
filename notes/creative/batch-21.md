# Batch 21: two-slit step 2: whole-world weights vs a self-field, side by side (Creative Lead; do not merge)

**Status.** Exploration only, under David's rulings (all relayed by Physics Lead, not signed). Classical only; test-body limit; no Born rule; no $|a|^2$; no superposition by hand; (M1) untouched at L3; CTCs as exploration only. Citations are unchecked unless verified earlier. Nothing goes into `versions/` or `papers/`. Stacked on batch 20 (#401) and uses #399's definitions. Ledger rows L80–L84. Script: `notes/creative/batch-21/selfforce.py` (output `results.txt`).

**David (8:46 AM ET 2026-10-13, widget answer, relayed by Physics Lead, Physics Lead chat, not signed; verbatim):**
> Explore both escapes side by side in step 2.

---

## For David (plain summary)

- **Setup.** We use the fixed-wrap two-slit case from step 1: one world shape, and a hit that could have come by either of two routes (the direct one, n = 0, or round the wrap the other way, n = −1). Nothing records the route.
- **Baseline, stated first.** Adding a passive which-route counter changes no hit. It only splits the group of compatible worlds by route.
- **Escape A, weights on whole worlds.** Could a rule that weights each world by its full set of possible routes make dark bands? We prove it can't, as long as each world's weight doesn't depend on which slits are open: the pattern with both open is then just a blend of the one-slit patterns, so no spot is darker than both. If the weight *does* depend on which slits are open, dark bands are possible in principle, but only by building the answer into the weight. We found no independent reason for such a weight, so it fails your no-tuning test (LT2).
- **Escape B, the particle's own field.** Give the particle a small charge, so its field goes round the wrap and pushes back on it. We computed it. For a particle moving steadily, the pushes from all the wrapped-around copies cancel exactly, so the path stays straight and the hits spread evenly with no bunching. The bouncing-droplet experiments, which do get patterns, rely on a wave that the droplet keeps re-exciting and that remembers its past. Our field has no such memory.
- **Verdict.** A: no fringes without tuning. B: no fringes in this test model. Both escapes are honestly closed here; the open door is a field with memory, which is a different model.

---

## Starting point (batch 20)

- **Fixed-wrap two-launch case** (#401 Set 2, S1). With $L$ known and θ not recorded, a hit at $x$ fits θ₀ (route $n=0$) and θ₋₁ (route $n=-1$). For $L=2.5$, $x=2.0021$: 11.32° and −2.85° [N, batch 20].
- **S4 classical baseline** (#401, stated in advance). A passive which-route record, e.g. a test-body crossing counter, leaves every hit unchanged and splits only the record class by route. Any change in the hit pattern when a record is added must come from a weighting fixed before the computation (LT2).

---

## Set A: whole-world weights

**Plain summary.** Weights that ignore which slits are open can only blend the one-slit patterns. Dark bands need weights that know which slits are open, and making them do so to produce bands is tuning.

**Setting.** Configuration $C\subseteq\{0,-1\}$ = which routes are open, i.e. which apertures; apertures are test matter in the world (#399 R2). A world $w=(L,\theta)$ with $\theta$ in the open apertures. Its hit $x_w$ is unique and its route $n_w$ is unique (#401 Set 1). A weighting is $p^C(w)\ge0$, fixed in advance. The **hit pattern** is the (finite or σ-additive) sum $I_C(x)=\sum_w p^C(w)\,[x_w=x]$, or its density version.

**Lemma A (no cross term without configuration dependence) [A].** Suppose $p^{\{0,-1\}}(w)=\lambda\,p^{\{n_w\}}(w)$ for every world $w$, with one constant $\lambda>0$. That is, a world's weight with both open is its one-route weight, up to a single normalisation factor. Then
$$I_{\{0,-1\}}=\lambda\,(I_{\{0\}}+I_{\{-1\}}),$$
and with per-configuration normalisation ($\lambda=\tfrac12$ for equal total weights), $\min(I_{\{0\}},I_{\{-1\}})\le I_{\{0,-1\}}\le\max(I_{\{0\}},I_{\{-1\}})$ pointwise. In particular, there is no point $x$ where both one-slit patterns are positive and the two-slit pattern vanishes.
*Proof.* Each world contributes to exactly one route's sum, because one launch gives one route (#401). So the two-route sum splits into the one-route sums. ∎

**Corollary (what a fringe requires).** A dark spot at $x$, with $I_{\{0,-1\}}(x)<\min(I_{\{0\}}(x),I_{\{-1\}}(x))$, requires $p^{\{0,-1\}}(w)<\lambda\,p^{\{n_w\}}(w)$ for some world landing at $x$. So the weight of a world must depend on **which other routes are open**, and, to give bands, on the hit point. Concretely, it must vary with the path difference between θ₀ and θ₋₁ for the same $x$.

**Whole-world weights depending on the topology's route set.**
- With a fixed wrap, the topology's set of routes, $\pi_1=\mathbb Z$, is **the same** in both configurations. So a weight that depends only on the topology is configuration-independent. Lemma A applies, and gives **no fringe**.
- A weight that depends on the **open-aperture set** is configuration-dependent and could make dark spots in principle. To give bands at the right places, it must encode the route-length difference at each $x$, a function with a fringe-shaped profile. **No independent motivation found.** Choosing it because it gives fringes is the LT2 failure (#401 N1). With a phase-like profile, it is $|a|^2$ in disguise, which is excluded.
- Uniform counting by route (the labelled counting conjecture, #399) is configuration-independent, so it also gives **no fringe**.

**With a passive which-route record.** The record splits the record class by route; the hits are unchanged (S4). If the weights are fixed in advance and do not depend on the record's presence, the pattern is unchanged: Lemma A again. If they do depend on it, that is again configuration dependence (the counter is test matter), with the same LT2 verdict.

- **Status: closed without tuning (no-go lemma)** (L80, L81).

## Set B: self-field of a test charge

**Plain summary.** The charge's field comes round the wrap from both sides and cancels. A steadily moving charge feels no net push, so its path is straight and nothing bunches.

**Model.** A test charge $q$ on the flat cylinder $\mathbb R^3$ with $x\sim x+L$ (not gravity: under the lock the self-field must be a test field, #399 §4 item 2). Its field in the quotient is the field of its images at $r+mL\hat x$. No radiation reaction (test model).

**Result [A, N].**
- For uniform motion with any velocity $v$, each image moves with the same velocity, and its field at the particle is the uniform-motion (Heaviside) field from separation $R=-mL\hat x$.
- Images $m$ and $-m$ give equal and opposite forces: $\sin^2\psi$ is the same for $R$ and $-R$, and $\hat R$ flips. So **the net self-force vanishes exactly**.
- Numerically, the sum over $|m|\le2000$ gives zero to machine precision for v = 0, (0.3,0,0), (0,0.5,0), (0.4,0.4,0) and (0.2,0.5,0.3) (`results.txt`).
- So straight lines are self-consistent. The hit $x=D\tan\theta \bmod L$ is strictly monotone in θ within each route (table in `results.txt`): **no bunching into bands.**
- **Where a self-force could act:** only during acceleration (the launch or aperture transit), which is radiation-reaction territory and outside the test model. Charged aperture walls would deflect via their own induced charges. That is a smooth, single-world, configuration-dependent deflection, not bands.

**Comparison with the droplets** (bibliographic only, per #403 and Claude 017).
- Couder–Fort 2006 patterns came from a **driven, persistent guiding wave** that the droplet keeps re-exciting, with path memory: "the droplet is influenced by both slits by virtue of the spatial extent of its guiding wave field" (Pucci et al. 2018, abstract per external review).
- Andersen et al. 2015 and Pucci et al. 2018 did not reproduce single-particle interference.
- Our field is conservative, instantaneous-image and memoryless, so it lacks exactly the ingredient the droplets need.

**With a passive which-route record.** A passive (uncharged, non-interacting) counter changes nothing: same straight paths, same hits. A charged counter is not passive; it deflects smoothly, without bands.

- **Status: closed in this test model** (L82, L83). The open door is a field with memory, a driven or dissipative medium, which is a different, non-test model.

---

## Weak points

1. **Lemma A is for weights fixed per world.** A weighting over *sets* of worlds that is not a sum over worlds (non-additive) is outside it, and is not defined in our framework.
2. **Uniform motion only** in Set B. A transient self-force at launch is not computed (radiation reaction excluded).
3. **Flat cylinder, one handle direction, static.** A curved handle or Misner boost gluing could make image forces non-cancelling. Not computed.
4. **No memory field** was tried. That is the real analogue of the droplets, and a new model would be needed.
5. **The aperture is idealised** (a launch-angle set). Real slits with walls bring image charges and diffraction-free smooth deflection only.

Ledger: L80–L84 (L84 records David's 8:46 AM words).
