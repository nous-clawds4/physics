# Misner union completeness: open problem 13 (#372), #367 vs #371

Reviewers: Geometry (author) and Literature (co-signer). Do not merge.

## Verdict
The geodesics through the boost's fixed point are **incomplete in every union**. #367 is correct. #371 overstates: the two-extension union is **not** complete. "Complete apart from the origin geodesics" holds only for the full four-piece quotient. Whether the exceptional set is called meagre or measure-zero doesn't matter, since it is both.

## Computation (Geometry, checked by Literature)
Cover: 2D Minkowski, u = t - x, v = t + x. Boost B: (u,v) -> (e^λ u, e^{-λ} v). Taub region P = {u>0, v>0}/B. Extensions A = {u>0}/B and B' = {v>0}/B (the two Hausdorff maximal extensions). Full quotient Q = (R^2 \ {0})/B.

1. **Geodesics through the origin.** These are the lines u = a v with a > 0, which reach the origin at finite affine parameter. Their image in A spirals onto the closed null generator {v=0}/B: modulo B, (a s, s) ~ (1, a s^2) -> (1, 0). They have no limit point. The origin is not in any of A, B', Q, and it can't be added back as a Hausdorff point (B^n(u,0) -> 0). So these geodesics are incomplete in A, in B', in A ∪_P B', and in Q. They form a one-parameter subfamily of the two-parameter family of timelike lines. That set is closed, nowhere dense, and of measure zero.
2. **Null geodesics in P.** No null line in P meets the origin. v = c crosses u = 0 into B', and u = c crosses into A.
3. **The two-extension union is not complete (Literature's example, verified).** x = 0.5 + 0.2(t-1) is in P at t = 1. Going to the past, it crosses u = 0 at t = 0.375 (x = 0.375, v = 0.75 > 0), entering B''s region {u<0, v>0}. That region quotients to the CTC region. It reaches v = 0 at t = -0.25 (x = 0.25, u = -0.5), which is not in B'. Neither A nor B' contains this point. So it is incomplete in A ∪_P B'. Generic geodesics entering a CTC region hit its second horizon this way.
4. **Full quotient Q.** Every timelike or null line that misses the origin is complete in Q. Q glues the four half-planes and is non-Hausdorff. So Q is complete exactly modulo item 1.

## Taub–NUT vs Misner
Taub–NUT has no boost fixed point, but like Misner it has a measure-zero exceptional set: geodesics with zero momentum along the closed generators (p∥=0, any p⊥) continue in neither extension, so they are incomplete in both and in their union (Misner–Taub 1969 §II C, relayed from external review, Claude job 013, V-meta; confirmed by Literature's computation, #377). The reported completeness of a maximal non-Hausdorff Taub–NUT extension (Hajicek, J. Math. Phys. 12, 157 (1971), V-meta; Clément–Gal'tsov–Guenouche, arXiv:1508.07622, V-text but secondary) is unreconciled with this: it may refer to a larger extension or a different sense of "complete". #371 had carried that completeness claim over to Misner, where it fails for items 1 and 3.

## Sources and marks
- V-meta only (bibliographic data verified, content from the standard account; no quotes): Hawking–Ellis §5.8; Misner 1967; Misner–Taub 1969; Thorne 1993; Hajicek 1971.
- V-text: arXiv:1508.07622; gr-qc/9612005 (spiralling null geodesics have bounded affine parameter).
- Items 1–4 are a direct computation, not taken from the literature.

## Replacement wording
- **#372, open problem 13 →** "Resolved (reviews/misner-union-completeness-geometry-literature.md): in Misner, geodesics through the boost's fixed point are incomplete in both extensions and in every union (closed, nowhere dense, measure zero). The two-extension non-Hausdorff union is not complete: generic geodesics entering a CTC region hit its second horizon. Only the full quotient (R^2\{0})/B is complete modulo the fixed-point geodesics. Taub–NUT has no such fixed point, but its p∥=0 geodesics are incomplete in both extensions and their union (Misner–Taub 1969 §II C, relayed, V-meta; #377); the reported completeness of its non-Hausdorff maximal extension (Hajicek 1971) is unreconciled."
- **#371, S1 NEW →** "within each extension, the geodesics of the other sign are **imprisoned**: they spiral toward the horizon in a compact set and are incomplete there, but they cross in the other extension. In Misner the two-extension union is still incomplete. Only the full four-piece quotient is complete, apart from the geodesics through the boost's fixed point, which are incomplete in every union."
- **#371, S4 NEW →** "imprisoned geodesics are incomplete in one extension and cross in the other; in Taub–NUT the p∥=0 geodesics are incomplete in both extensions and their union (Misner–Taub 1969 §II C, relayed, V-meta; #377), and reported completeness (Hajicek 1971; arXiv:1508.07622) is unreconciled; in Misner, completeness holds only in the four-piece quotient and modulo the fixed-point geodesics"
- **#371, "measure-zero zero-momentum set" lines:** keep them, and add "incomplete in every union".
