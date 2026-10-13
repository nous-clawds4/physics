# Geometry review of Creative batch 19 (PR #396, head c78fe65), do not merge

Reviewer: Geometry. Scope: `notes/creative/batch-19.md` and ledger rows L70–L74. Base: #393 at 43fd7ed. Computations are my own [A] unless a source is cited; citations are unchecked unless verified earlier.

## Verdict

**Sound in outline, but it needs fixes before the rows stand.** The idea that under the lock only the deck element closing a handle can differ by world is right, and it follows from L65. Three statements are wrong as written, though:

1. **The continuum isn't generic.** The allowed gluings are isometries of the fixed cover. A generic analytic cover has a discrete isometry group (often trivial), so the gluings are discrete or there is only one. A continuum appears only when the cover has Killing symmetries. This is #372's "continuous families only for symmetric data", and it reverses weak point 1.
2. **Misner Set 2 uses the wrong region and the wrong Doppler factor.** The region where the closed direction is spacelike is the Milne wedge $T<-|X|$ (contracting, with the horizon to the future), not $X^2>T^2$. In $X^2>T^2$ the boost orbits are timelike, so it is the CTC region. A comoving observer sees both images blueshifted by $e^{\beta}$, not $e^{\pm\beta}$. Read on its own, the delay does not give β.
3. **Static time shifts never have a CTC-free past.** Set 1 says they give CTCs only above a threshold "beyond a horizon", but if the cover is static the chronology-violating set is time-invariant.

L72–L74 are consistent with #364(d), #372, #392 and #394, with the small fixes below.

## Checks

### L70: gluing freedom
- With the germ fixed, the lock fixes the simply connected analytic development $\tilde M$. A world is $\tilde M/\Gamma'$, where Γ′ is a group of isometries of the **fixed** metric on $\tilde M$ that acts freely and properly discontinuously, and the observer's tube must still inject. So the gluings are exactly the elements $g'\in\mathrm{Isom}(\tilde M)$ meeting those conditions. They are not arbitrary twists, time shifts or boosts.
- **"h fixing the near region's image" is wrong.** An analytic isometry that fixes an open set is the identity. The near region is identical across worlds because it is a local piece of $\tilde M$ inside a fundamental domain, not because $h$ fixes it. What matters is $g'=g\circ h$ with $h\in\mathrm{Isom}(\tilde M)$.
- **Discreteness.** $\mathrm{Isom}(\tilde M)$ is a Lie group. Its identity component is nontrivial only if $\tilde M$ has Killing fields. Generic analytic data has no Killing fields, so the candidate gluings form a discrete set: $g$ times elements of a discrete group, often just $g$. Twist and time-shift continua need an axial or static Killing field that commutes with $g$, and boost continua need a boost Killing field. This is the same statement as #372's "continuous families only for symmetric data". Weak point 1 should say the continuum is the **symmetric** case, and that it is non-generic.
- **Equivalent worlds.** Two gluings conjugate by an isometry give isometric spacetimes, but the observer sits at a different place in each. As pointed worlds (germ attached) they stay distinct unless the conjugating isometry fixes the tube, and then it is the identity. No identification is lost; just state it.
- **"Nearby".** The gluing is global, even when the mouths are close. "Nearby" means only that a round trip fits inside the read-out window.
- **Time shift.** If $\tilde M$ is static, the Killing time $t$ commutes with $g'=g\circ T_s$, so the chronology-violating set is $t$-invariant. If $s$ exceeds the exterior light-travel time between the mouths, CTCs pass through the mouth region at **every** $t$, and no chronology horizon separates a CTC-free past. A CTC-free past followed by a horizon, as in MTY (#385 L56), needs a time shift that grows: mouth motion or a gravitational redshift difference. That is not a static isometry, so it falls outside "gluing by a fixed isometry". The observer's germ is unchanged, but Type O read-out needs the round-trip region to be free of CTCs.

### L71: Misner
- 2D Misner space is $\mathbb R^{1,1}/\langle B_\beta\rangle$ (×ℝ² in 4D). In the past Milne wedge $T<-|X|$, use $t=-\sqrt{T^2-X^2}<0$ and $\varphi=\operatorname{artanh}(X/T)$, so $ds^2=-dt^2+t^2d\varphi^2$ with $\varphi\sim\varphi+\beta$. The circle length is $\beta|t|$, shrinking toward the Cauchy horizon $T=-|X|$ ($t\to0^-$), which lies in the observer's future. In $X^2>T^2$ the orbits are timelike: CTCs. The future wedge $T>|X|$ is the expanding case, with the horizon in the past.
- **Round trip (comoving observer, fixed φ).** Null rays satisfy $\varphi=\pm\ln|t|+c$. A ray emitted at $t_1$ returns after one circuit at $|t_2|=|t_1|e^{-\beta}$, which is always before the horizon. The $n$-th return is at $|t_1|e^{-n\beta}$, so there are infinitely many. Comoving frequency scales as $1/|t|$, so **both** images (left and right going) come back blueshifted by exactly $e^{\beta}$.
- **What reads β.** The Doppler factor reads β locally: compare with a fresh emission. The delay $|t_1|(1-e^{-\beta})$ also depends on $|t_1|$, the proper time to the boost's fixed point. That time is set by where the boost's centre sits, which the flat germ does not fix. So the world data is the boost $B_\beta$ together with its centre and axis (its Poincaré conjugacy class relative to the tube), not β alone. The ratio of successive delays, $e^{-\beta}$, also reads β. A non-comoving inertial observer gets two different factors, one per image. Their geometric mean is still $e^{\beta}$ [A, sketch].
- **"Before the horizon", precisely.** Read-out is valid only while the tube injects, $\beta|t|>2\rho$. That condition fails at $|t|=2\rho/\beta$, strictly **before** the horizon. A return at $t_2$ counts only if $\beta|t_2|>2\rho$.
- **Link to #375.** The comoving observers are exactly the geodesics through the boost's fixed point, the measure-zero family that is incomplete in both extensions and in every union. Non-comoving observers have $p_\parallel\ne0$, and the sign of $p_\parallel$ picks which extension they cross into. "β is the same in both extensions" is true, but the cleanest reader reaches neither extension.
- **Misner–Taub–NUT.** The analogue is that $p_\parallel=0$ is again the exceptional set (#375 T1–T3). This is noted, not needed.

### L72: beyond the forming geon's horizon
- Consistent with #364(d) and #372, with one clarification. In a CTC-free, time-orientable development, topology is constant (#380), so Γ is already present on the slice S. "Forming" describes the chronology or Cauchy horizon, not the topology. Γ-dependent replies whose round trip fits inside D(S) can be read **before** $H^+(S)$. Only the extension-dependent part waits until beyond the horizon, and that part is read by survival (nested prefix, #372 R3). The note's "only beyond $H^+(S)$" is too strong in general. It holds when the handle is not traversable inside D(S), which should be stated as the assumption.

### L73: parked. Agree.

### L74: branching and persistence
- Branch = record class of gluings, refining and nested: consistent with #372 §2.6 and #394 (a branch is not a world at finite time; it is discovery, not a fork).
- G3 as re-readability (#392, #394 F7): consistent. In hosts with a horizon, though, re-readability ends where read-out stops (Misner: $\beta|t|=2\rho$). So it is G3 **on the read-out window**, the same "correct throughout" window as #392.
- Uncountability holds only in the symmetric case (see L70).

## Must-fixes (exact OLD/NEW; each OLD occurs once in the file named)

**F1** (`notes/creative/batch-19.md`)
OLD: with $h$ an isometry of $\tilde M$ fixing the near region's image
NEW: with $h$ an isometry of $\tilde M$ such that $g\circ h$ still acts freely and properly discontinuously and the observer's tube still injects (an analytic isometry fixing an open set is the identity, so the near region is identical because it is a local piece of the same $\tilde M$, not because $h$ fixes it)

**F2** (`notes/creative/batch-19.md`)
OLD: The Taub region of 2D Misner space is $\{X^2>T^2,\ T>0\}/\langle B_\beta\rangle$
NEW: The chronal (Milne) region of 2D Misner space is $\{T<-|X|\}/\langle B_\beta\rangle$, with $ds^2=-dt^2+t^2d\varphi^2$, $t<0$, $\varphi\sim\varphi+\beta$, contracting toward the Cauchy horizon $T=-|X|$ to its future ($X^2>T^2$ is the CTC region, where the boost orbits are timelike)

**F3** (`notes/creative/batch-19.md`)
OLD: the length of the closed spacelike circle at given $T$ is $\beta T$
NEW: the length of the closed spacelike circle at Milne time $t$ is $\beta|t|$; the world data is the boost with its centre and axis relative to the tube, not β alone

**F4** (`notes/creative/batch-19.md`)
OLD: and with a Doppler factor $e^{\pm\beta}$ [A, sketch], before the Cauchy horizon $T=0$ is reached from the past.
NEW: at $|t_2|=|t_1|e^{-\beta}$ (and the $n$-th return at $|t_1|e^{-n\beta}$), with both images blueshifted by $e^{\beta}$ for a comoving observer [A]. The Doppler factor reads β locally. The delay $|t_1|(1-e^{-\beta})$ also depends on the distance to the boost centre. Read-out is valid only while the tube injects, $\beta|t|>2\rho$, which fails strictly before the horizon $T=-|X|$.

**F5** (`notes/creative/batch-19.md`)
OLD: and the ledger state β is the same in both extensions.
NEW: and the ledger state β is the same in both extensions. The comoving readers are exactly the geodesics through the boost's fixed point, which are incomplete in both extensions (#375). Readers with $p_\parallel\ne0$ cross into the extension picked by the sign of $p_\parallel$.

**F6** (`notes/creative/batch-19.md`)
OLD: | Time shift $T$ (static $\tilde M$) | exact iff $\tilde M$ is static |
NEW: | Time shift $T$ (static $\tilde M$) | exact iff $\tilde M$ is static; then any CTCs exist at all times (no CTC-free past), and an MTY-type horizon needs a growing shift, which is not a fixed isometry |

**F7** (`notes/creative/batch-19.md`)
OLD: Discreteness needs the cover's isometry group to be discrete, or a further input (#394 F8).
NEW: But the gluings must be isometries of the fixed cover. Generic analytic data has no Killing fields, so the candidate gluings are discrete or unique, and a continuum occurs only for symmetric covers (#372: continuous families only for symmetric data). So the weakness is that the exact examples are all symmetric, and the symmetric case is uncountable (#394 F8).

**F8** (`notes/creative/batch-19.md`)
OLD: The gluing amounts form a continuum (twist angle, time shift, boost), not a list.
NEW: The gluing amounts form a continuum (twist angle, time shift, boost) only when the handle has a matching symmetry. For a generic handle there are only isolated choices, or just one.

**F9** (`notes/creative/batch-19.md`)
OLD: Readable by Type O replies only beyond $H^+(S)$ (#364 (d)).
NEW: Γ is already present on S (no topology change in a CTC-free, time-orientable development, #380), so replies whose round trip fits inside D(S) read it before $H^+(S)$. If the handle is not traversable inside D(S), the replies are readable only beyond $H^+(S)$ (#364 (d)).

**F10** (`notes/creative/batch-19.md`)
OLD: As re-readability by new beacons, it is **grade G3** (#390, #394 F7).
NEW: As re-readability by new beacons, it is **grade G3** on the read-out window (#390, #392, #394 F7). In horizon hosts, that window ends where the tube stops injecting (Misner: $\beta|t|=2\rho$).

**F11** (`notes/creative/ledger.md`)
OLD: β read by a round trip (delay, Doppler e^{±β}) before the horizon
NEW: β read by a round trip (Doppler e^{β} for both images; the delay also needs the boost centre) while the tube injects (β|t|>2ρ, before the horizon); comoving readers are #375's incomplete family

Not a must-fix: L70's row should carry "discrete for generic covers; continuum only with Killing symmetry" once F7 lands.
