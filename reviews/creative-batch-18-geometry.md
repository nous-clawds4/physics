# Geometry review: Creative batch 18 (PR #393, head 6acc5a0) — do not merge

**Verdict: sound in substance, nine must-fixes.** Several exact ledger states (flat quotients) do fit one observer state, and read-out by wrap-around returns is correct, Type O, and nests. But four claims overreach: (i) "no test-field limit" (the observer itself must be a test body); (ii) "branch = world" (false at finite τ before certification); (iii) the compatible family is larger than rest-frame lattices (boosted lattices, nine further flat quotients); (iv) the far-handle flux is not "excluded" outright, only adds no freedom beyond Γ. The branching here is discovery, not a fork, and the note should say so.

## Checks

1. **L65 (only Γ and extension vary).** Agrees with #370 (A): developing-map uniqueness fixes the simply connected analytic development; worlds are quotients of extensions. OK.
2. **Tube embedding.** For a free, properly discontinuous Γ, the tube of radius ρ about the worldline embeds isometrically iff every nontrivial deck element moves each point of the worldline by more than 2ρ. For lattices this is ℓ_min > 2ρ. OK. For screw-motion groups, use the minimal displacement on the worldline, not ℓ_min of the translation subgroup.
3. **Self-gravity (must-fix F1).** A self-gravitating observer of mass m > 0 cannot sit in a static flat T³: on a compact slice, the integrated Gauss/Hamiltonian constraint leaves no static solution with net mass. Even linearised, the periodic Green's function gives a Λ-dependent tidal field at the observer. Under the lock, a massive observer's germ therefore already distinguishes lattices. The example is exact for the ledger, but the observer and its flashes are test bodies.
4. **Compatible family (F2).** Any discrete group of spacelike translations spanning a spacelike 3-plane gives a flat, time-orientable, CTC-free quotient with the same germ. In other words, a lattice at rest in a frame moving relative to the observer: 9 parameters, not 6. The other nine compact flat 3-manifolds (Bieberbach; 6 orientable in total, counting T³) also qualify when the displacement condition holds.
5. **Holonomy (F3).** Levi-Civita holonomy is trivial for every torus, so the "rotated return" exists only for the nine non-torus quotients (rotations by π, 2π/3, π/2, π/3; mirror images in the 4 non-orientable ones). There it is readable classically by comparing the returning flash's image orientation or polarisation frame. The flat U(1) Wilson loop is correctly called classically unreadable.
6. **Far-handle flux (F4).** The argument "F = 0 on the tube ⇒ F ≡ 0" is right. But "excluded" is too strong: a uniform field on T³ is harmonic and analytic (b₂ = 3), so it is allowed. Since it is nonzero on the tube, it is fixed on the cover by the germ, and its flux through each 2-cycle is determined by germ + Γ. So it adds no ledger freedom beyond Γ, and it is not excluded.
7. **Read-out.** A ray emitted along g returns after |g| (a one-way trip to the observer's image, not radar), arriving from −ĝ. A directed beacon returns only if aimed exactly along a lattice vector, so the read-out needs isotropic flashes (F9). Type O holds trivially: the spacetime T³×ℝ (and every quotient listed) is time-orientable, with no CTC and no geon needed. OK.
8. **Branch vs world (F5).** At time τ, the record shows exactly the vectors g with |g| ≤ τ − τ_e (and the absence of shorter ones). All worlds that agree on that short-vector part share a branch, uncountably many of them. Once τ exceeds the generator lengths plus about twice the covering radius, any further vector would already have returned, so Λ is certified (#370) and the branch is one world. "Branch = world" is therefore false at finite τ before certification and true after it, for cocompact Γ only. Uniqueness of extension holds here (globally hyperbolic and complete), so the extension adds nothing.
9. **Discovery vs fork (F6).** Nothing in any world splits. What branches is the observer-plus-record state: the compatible world set shrinks as replies arrive (#372 R2). That is the framework's definition of branching and is consistent with well-posedness (each world's evolution is unique). It should be stated, not presented as a physical fork.
10. **Persistence (F7).** Γ is permanent. Under #390 as amended by #392 (F1–F3: per world, correct over the whole interval, read from the observer's state), G3 holds for re-readability: a new flash re-derives g on any later interval longer than |g|. That is not storage, and a stored reply in the diary is graded separately.
11. **Countability (F8).** The worlds form a continuum (9 real parameters for lattices, plus continuous families for the other quotients). Any outcome counting needs countability as an input (e.g. Γ inside a fixed discrete group). The note says this; F8 makes it explicit.
12. **Misner/Taub–NUT parked.** Consistent with #367/#375 (read by survival only). OK.

## Must-fixes (exact OLD/NEW; each OLD occurs once in its file at 6acc5a0)

**F1** (`notes/creative/batch-18.md`)
OLD: `**No test-field limit is needed for the ledger state itself** (see Set 2).`
NEW: `**The ledger state needs no test-field limit (it contains no ledger matter); the observer and its flashes are still test bodies** (see Set 2).`

**F1b** (`notes/creative/batch-18.md`)
OLD: `Metric flat, $T_{ab}=0$, **exact vacuum, no test-field limit.**`
NEW: `Metric flat, $T_{ab}=0$, **exact vacuum for the ledger, with the observer and its flashes as test bodies.** A self-gravitating observer of mass $m>0$ has no static flat $T^3$ solution (compact slice), and its images' tidal field at the tube depends on Λ, so under the lock a massive observer's germ would already tell the lattices apart.`

**F2** (`notes/creative/batch-18.md`)
OLD: `3. Each $W_\Lambda$ is time-orientable`
NEW: `3. The compatible family is larger than rest-frame lattices: any discrete group of spacelike translations spanning a spacelike 3-plane (a lattice moving relative to the observer), and any of the nine other compact flat 3-manifold groups whose deck elements all move the observer's worldline by more than $2\rho$, give the same observer state.
4. Each $W_\Lambda$ is time-orientable`

**F3** (`notes/creative/batch-18.md`)
OLD: `**Included in Γ.**`
NEW: `**Included in Γ.** It is trivial for every torus (pure translations); it is nontrivial, and readable from the returning image's orientation, only in the nine non-torus flat quotients (rotations by π, 2π/3, π/2, π/3; mirrored in the four non-orientable ones).`

**F4** (`notes/creative/batch-18.md`)
OLD: `and the lock excludes it [A].`
NEW: `and so a field vanishing on the tube is excluded [A]. A field nonzero on the tube is allowed (e.g. a uniform harmonic field on $T^3$, $b_2=3$), but it is then fixed on the cover by the germ and its flux through each 2-cycle is determined by germ plus Γ: it adds no ledger freedom beyond Γ.`

**F5** (`notes/creative/batch-18.md`)
OLD: `That is exactly "branch A = world A", with branches that only split, never merge.`
NEW: `Before enough replies are in, one branch holds many worlds (all patterns agreeing on the wraps shorter than the elapsed time); in a closed wrapped universe, after a finite certification time each branch is one world. Branches only split, never merge.`

**F5b** (`notes/creative/ledger.md`)
OLD: `branch A = world A, with nesting`
NEW: `branch = record class (many worlds); one world per branch only after certification (cocompact Γ); nested`

**F6** (`notes/creative/batch-18.md`)
OLD: `- **Status: live** (L67).`
NEW: `- **Discovery, not fork.** Each world is fixed whole from the start and nothing in it splits. What branches is the observer-plus-record state, whose compatible world set shrinks as replies arrive (#372 R2). This fits well-posedness: every world's evolution is unique.
- **Status: live** (L67).`

**F7** (`notes/creative/batch-18.md`)
OLD: `**Grade G3** for the ledger state, not just G2.`
NEW: `**Grade G3 for the ledger state Γ, as re-readability:** judged per world on the observer's read-out (#390 with #392 F1–F3), each $g$ is re-derived by a new flash on any later interval longer than $|g|$. This is not storage; a stored reply in the diary is graded separately.`

**F8** (`notes/creative/batch-18.md`)
OLD: `Flat lattices form a continuous moduli space`
NEW: `Flat lattices form a continuous moduli space (6 real parameters modulo rotation, 9 with moving lattices, plus continuous families for the other flat quotients), so the compatible worlds are uncountable and no outcome counting is available without an extra input`

**F9** (`notes/creative/batch-18.md`)
OLD: `It needs repeated beacon emission`
NEW: `It needs repeated isotropic flashes (a directed beacon returns only if aimed exactly along a lattice vector)`
