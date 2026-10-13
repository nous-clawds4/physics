# Batch 19: a world-dependent ledger state on a nearby handle or geon (Creative Lead; do not merge)

**Status.** Exploration only, under David's rulings (all relayed by Physics Lead, not signed), including 11:42 PM (in which David equates a fork with a discovery: "In my mind, a fork and a discovery are the same thing."), and the Lead rulings that followed (ledger: a fork is the discovery of which world one is in; the main line stays geon/handle hosts). Classical only; no Born rule, no probability, no measure; (M1) unchanged at L3; CTCs as exploration only. Citations are unchecked unless verified earlier. Nothing goes into `versions/` or `papers/`. Stacked on batch 18 (#393), whose flat example is an exact proof of concept only. Ledger rows L70–L74.

**Goal.** Move #393 onto the main line. The distinguishing detail sits in the global structure of a **nearby** handle or geon, the near region is identical across worlds, and the beacon round trip (#372) reads it out.

---

## For David (plain summary)

- **Can the far side of a nearby handle differ by world?** Not its shape: under the analytic lock, following space through the handle gives one answer, so the far mouth looks the same in every world. What **can** differ is **how the far mouth is glued back**: with a twist, a time shift or a boost. Near the observer, every world is identical; the gluing is the ledger state.
- **Reading it.** Send the beacon through the handle. It comes back changed by the gluing: rotated by a twist, or, in Misner space, blueshifted by the boost (the cleanest read-out). Reading only works while the handle's wrap is still wider than the observer-plus-diary tube. Different gluings give different replies, so the reply tells you which world you're in. That *is* the fork (your 3:19 PM and 11:42 PM point). At first, many worlds share a branch, and each reply narrows it down.
- **Link to time loops.** A static time-shift gluing has time loops at all times; a time machine that switches on later (Morris–Thorne–Yurtsever) needs a growing shift, which is not a fixed gluing. Misner space, the simplest model of the time loops around a geon, is exactly a "boost gluing", and its boost amount is a world-dependent ledger state that a round trip reads before the time loops appear.
- **Persistence.** The gluing is topology plus symmetry. Nothing writes it and nothing erases it, so it stays readable for as long as read-out is possible (in Misner, until the wrap gets too narrow near the horizon).
- **The catches.** The gluing amounts form a continuum (twist angle, time shift, boost) only when the handle has a matching symmetry. For a generic handle there are only isolated choices, or just one. An exact one-universe handle with enough symmetry for these gluings is not known to us, except in flat or Misner-type models. And thin-shell handles are not analytic, so they sit outside the lock.

---

## The tension with L65, stated honestly

L65 (#393): under the lock, the germ fixes the simply connected analytic development $\tilde M$ along every path, including through a nearby handle. So the handle's **far side is the same** in every compatible world. Freedom survives only in:
1. **the deck group Γ**, here **the deck element that closes the handle**, and
2. **the extension** past non-unique continuation points (Cauchy horizons).

A one-universe handle is $W=\tilde M/\Gamma$, with $\Gamma=\langle g\rangle$, where $\tilde M$ is the handle's covering, an infinite chain of copies [A]. Changing $g$ to $g\circ h$, with $h$ an isometry of $\tilde M$ such that $g\circ h$ still acts freely and properly discontinuously and the observer's tube still injects (an analytic isometry fixing an open set is the identity, so the near region is identical because it is a local piece of the same $\tilde M$, not because $h$ fixes it), changes the world but not the germ, provided the observer's tube still embeds. **This is the only way "the far side differs by world" survives the lock.**

---

## Set 1: gluing freedom of a nearby handle (deck element of the handle)

**Plain summary.** The far mouth is glued back with a twist, a time shift or a boost. The near region is identical, the world differs, and a beacon through the handle sees the difference.

| Gluing variant $h$ | Exact? | Near region identical? | Readable by Type O reply? | Notes |
|---|---|---|---|---|
| Rotation $R$ about the mouth axis | exact iff $\tilde M$ has that rotational isometry | yes (if the tube embeds) | **yes**: the returning image or polarization is rotated by $R$ | time-orientable, so Type O |
| Time shift $T$ (static $\tilde M$) | exact iff $\tilde M$ is static; then any CTCs exist at all times (no CTC-free past), and an MTY-type horizon needs a growing shift, which is not a fixed isometry | yes | **yes**: the reply's delay is traversal + $T$ | $T>$ outside light time gives **CTCs** (MTY 1988; Frolov–Novikov 1990; V-text abstracts per #386), exploration only |
| Boost (Misner-like twist) | exact iff $\tilde M$ has a boost isometry | yes | yes, as Doppler and delay | see Set 2 |
| Time-reversing gluing (PT) | exact iff $\tilde M$ has it | yes | **no**: Type F, so a correlation only (#364, #381) | Hadley-type |
| Thin-shell mouth identification with a boost or rotation | a C⁰ metric, **not analytic** | yes | yes | **outside the lock** (thin shells break analyticity); allowed only under the 3:14 relaxation |

- **Exactness.** It needs an exact one-universe handle $\tilde M/\langle g\rangle$ whose cover has the isometries $h$. Flat models (#393) and Misner-type models have them. A static, axially symmetric, analytic, two-mouth, one-universe wormhole solution is **not known to us** (unchecked).
- **Status: live (conditional on an exact symmetric host)** (L70).

## Set 2: Misner space as the geon-host example (exact)

**Plain summary.** Misner space is flat space glued to itself with a boost. The boost amount is a world-dependent ledger state. Before the time-loop horizon, a light signal going round the closed direction comes back with a delay and Doppler shift set by that boost. This is exact, and it is the standard model of the geon's time-loop region.

- **Host** [A; Misner 1967 (unchecked); Hawking–Ellis §5.8 (V-meta per #377)]. The Taub region of 2D Misner space is the Milne wedge $\{T<-|X|\}/\langle B_\beta\rangle$ (closed spacelike circles; the wedges $X^2>T^2$ contain the boost orbits, which are timelike, so their quotient has CTCs), with $B_\beta$ a boost of rapidity β; a 4D version uses $\times\mathbb R^2$. The metric is flat, so the germ is the same for every β, provided the observer's tube injects: its boost-image distance exceeds $2\rho$ at $\tau=0$ [A].
- **Ledger state:** β, the deck element of the closed direction. Different β are non-isometric worlds: the length of the closed spacelike circle at Milne time $t=\sqrt{T^2-X^2}$ is $\beta t$ [A]. The world data is the boost together with its centre and axis relative to the tube, not β alone, since the flat germ fixes neither.
- **Read-out:** a null ray sent round the closed direction returns to a co-moving observer after a delay, at $t_2=t_1e^{-\beta}$ (the $n$-th return at $t_1e^{-n\beta}$), with **both** images blueshifted by $e^{\beta}$ for a co-moving observer [A]. The Doppler factor reads β locally. The delay $t_1(1-e^{-\beta})$ also depends on the distance to the boost centre. Read-out is valid only while the tube injects, $\beta t>2\rho$, which fails strictly before the Cauchy horizon $T=-|X|$ (Milne time $t\to0$). Type O (time-orientable). No CTC is used in the read-out.
- **Beyond the horizon:** CTCs (exploration only). Survival is fixed per extension (#367, #375), and the ledger state β is the same in both extensions. The comoving readers are exactly the geodesics through the boost's fixed point, which are incomplete in both extensions (#375). Readers with $p_\parallel\ne0$ cross into the extension picked by the sign of $p_\parallel$.
- **Status: live (exact, low-dimensional model)** (L71).

## Set 3: beyond the Cauchy horizon of a forming geon (#364, #381)

**Plain summary.** Where the geon forms later, everything up to its horizon is fixed except the gluing (Γ), which is there from the start. Replies that fit before the horizon can already read Γ; beyond it, the world can also continue in more than one way.

- **Exact** (non-unique extension, the general Cauchy-horizon fact, #371). Replies through the geon depend on Γ, which the germ does not fix (#367 (d)). Γ is already present on S (no topology change in a CTC-free, time-orientable development, #380), so replies whose round trip fits inside D(S) read it before $H^+(S)$. If the handle is not traversable inside D(S), the replies are readable only beyond $H^+(S)$ (#364 (d)).
- **The extension choice itself** is read only by survival, a nested prefix (#372 R3). The Γ-dependence is read by replies.
- **Status: live** (L72; it is #372's existing picture, now with Γ as a ledger state).

## Set 4: non-Hausdorff / inequivalent extensions

- Inequivalent extensions are exact, but only beyond the horizon, and read by survival. Non-Hausdorff unions as a mechanism are circular (#379 2B). **Parked** (L73).

---

## Read-out, branching and persistence

- **Beacon read-out** (#372 §2.2). A round trip through the nearby handle returns with (delay, direction, rotation or Doppler, deck label). The read-out map is fixed in advance and gauge-invariant (#390, #392 F1–F3).
- **Branching.** At finite τ a branch is the record class of all worlds (gluings) consistent with the replies so far. It contains many worlds and refines as replies arrive. **The fork is the discovery** of which gluing one is in (David 3:19, 11:42). Classes nest (#372 §2.6).
- **Persistence.** The gluing is part of Γ, which is constant (no topology change for reasonable sources in a CTC-free, time-orientable host; per #380). As re-readability by new beacons, it is **grade G3** on the read-out window (#390, #392, #394 F7). In horizon hosts, that window ends where the tube stops injecting (Misner: $\beta|t|=2\rho$). Stored replies in the diary are graded separately.
- **Status: live** (L74).

---

## Weak points (strongest first)

1. **A continuum of gluings (strongest).** Rotation angle, time shift and boost are continuous parameters, so the compatible worlds are uncountable. But the gluings must be isometries of the fixed cover. Generic analytic data has no Killing fields, so the candidate gluings are discrete or unique, and a continuum occurs only for symmetric covers (#372: continuous families only for symmetric data). So the weakness is that the exact examples are all symmetric, and the symmetric case is uncountable (#394 F8).
2. **No known exact symmetric one-universe handle** beyond flat and Misner-type models. The gluings need isometries of the cover that generic analytic handles lack.
3. **Thin-shell handles are not analytic.** The simplest handle models fall outside the lock.
4. **Time shifts give CTCs** above the light-travel threshold, and generic nearby masses drive the shift (Frolov–Novikov). So the CTC-free regime is non-generic. Above threshold, CTCs first appear at a compactly generated chronology horizon, where renormalized vacuum stress-energy diverges (Kim–Thorne, PRD 43 (1991) 3929); Hawking's chronology protection conjecture (PRD 46 (1992) 603) is quantum and does not bind this classical model, but it is the standard caveat.
5. **Misner is 2D (×ℝ²)** and only a model of the geon's time-loop region, not a Hadley geon.
6. **The extension choice** is readable only by survival (nested prefix).
