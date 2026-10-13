# Geometry review of creative batch 16 (PR #385 at ffd602d; do not merge)

Scope: `notes/creative/batch-16.md`, `threading.py`, `results.txt`, ledger rows L54–L59. Exploration only. Sketches are labelled. Earlier reviews: #381 (winding only around a handle; record = deviation from a declared reference; only Type O returns write), #384 (batch 15), #375 (Misner/Taub–NUT).

**Summary.** L54 OK with wording fixes. The L55 numerics reproduce exactly and the formula is now derived, not fitted, but the period is one traversal, not two. L56 OK. L57 is sound, with one real fix: the ledger must enclose exactly one mouth, because a surface around both mouths reads zero from the handle. L58 OK, with "integer" meaning integer differences. Weak point 7 overstates: what flips depends on whether the loop reverses time orientation, total orientation, or both.

## 1. Is the passage count cut- and basepoint-free? (L54): OK with fixes

- Let Σ be the glued throat sphere. In the quotient, mouth A's sphere and mouth B's sphere are one surface. Σ is non-separating, and signed intersection with it is the homomorphism π₁ = ℤ → ℤ (Poincaré dual to the generator of H¹). For **closed** loops, any surface homologous to Σ gives the same count, so the count is cut-free. It is a homology invariant, so it is basepoint-free (ℤ is abelian anyway).
- For an **open** segment the raw count depends on the cut: moving Σ past an endpoint changes it by ±1. Only w(c·c_ref⁻¹), with the reference sharing both endpoint events, is invariant. That is the #381 convention, and the note states it correctly.
- **Signed, not unsigned.** Entering through A (exiting B) counts +1, and entering through B counts −1. In the thin-shell model you cannot enter A and leave by A, because crossing the shell means emerging at B. A tangential graze is not a crossing and counts 0. `threading.py` counts *unsigned* steps (`n+=1`). For the threading orbit every step enters through A, so the count happens to equal the signed count. Say so.
- "Framing-independent" has no content for an integer homology count. Drop it.

Fix (batch-16.md, Set 1, record bullet):
OLD: `is cut-, basepoint- and framing-independent, because $\pi_1=\mathbb Z$ is abelian.`
NEW: `is cut- and basepoint-independent: signed intersection with the throat sphere is the homomorphism $\pi_1=\mathbb Z\to\mathbb Z$, so any homologous cut gives the same value on the closed loop $c\cdot c_{\rm ref}^{-1}$. For an open segment alone the raw count is cut-dependent. Signs: entry through A is +1, entry through B is −1, and a graze is 0 (a body cannot enter A and leave by A).`

## 2. Monodromy of the threading orbit (L55): numerics OK, period fix, mouth gravity open

**Reproduction (pinned).** `threading.py` sha256 `979d4d16b06be0a514f72264ce6002a6398119793b2a0a22b7f06d4728e04691`. Run `cd notes/creative/batch-16 && python3 threading.py | diff - results.txt` at ffd602d. The output is identical (traces 14.000000, 62.000000, 322.000000; 5 traversals).

**Independent derivation [A].** Take a near-axis ray at height y and angle θ that meets A's near side at polar angle φ ≈ y/a. The reflection gluing sends it to B's near side at the same height, y' = y. The normal component of its direction is kept and the tangential component is reflected, so θ' = θ + 2φ = θ + 2y/a. Each mouth is therefore a diverging element with matrix [[1,0],[2/a,1]], equivalent to a convex mirror of radius a. The flight to the next mouth is [[1,L],[0,1]]. The orbit closes after **one** traversal: it enters A, emerges at B's near side heading toward A, and the period is L. Hence

M = [[1, L], [2/a, 1+2L/a]], tr M = 2(1+L/a) > 2, which is hyperbolic.

The script's two-traversal map is M², with tr M² = (tr M)² − 2 = 4(1+L/a)² − 2, giving 14, 62 and 322 for L/a = 1, 3, 8. The per-period eigenvalues are 2±√3 for L/a = 1, so the squares 13.93 and 0.0718 match `results.txt`. The formula is exact for the linearised model, not a fit. The 3D case has two transverse directions, each with this same M by axial symmetry.

**Mouth gravity [sketch, open].** The cut-and-paste construction with flat interior and exterior has no gravity off the shell. The shell carries negative surface energy (NEC violation, of order −1/(4πa)·2 per unit area in G = c = 1 [M]), and that is exactly what defocuses. Replacing the flat exterior with Schwarzschild of mass M>0 (a Visser–Poisson thin shell) adds focusing in the gap through tidal compression toward the on-axis masses. The throat still defocuses, because the Raychaudhuri equation requires it at any throat that violates the NEC. Which effect wins for a closed threading orbit has not been computed here, and I do not claim either way. The static model has no time delay and its identification map is t → t, so a time offset (Set 2) would also change the map. Leave L55 as "dead in the flat model; open with mouth mass".

Fixes:
OLD: `- Equatorial 2D model, linearised return map over one full period (two traversals).`
NEW: `- Equatorial 2D model. One period is one traversal, with M = [[1,L],[2/a,1+2L/a]] and tr M = 2(1+L/a) > 2 (derived, Geometry review of batch 16, §2). The script reports M² (two traversals).`
OLD: `matching $4(1+L/a)^2-2$ [A fit]`
NEW: `equal to $\operatorname{tr}M^2=4(1+L/a)^2-2$ [A, derived]`
Ledger L55 OLD: `return-map trace 4(1+L/a)²−2` NEW: `one-period trace 2(1+L/a) (two-period 4(1+L/a)²−2)`

(Replace "Geometry review of batch 16, §2" with this review's PR number on merge of wording.)

## 3. Flux bookkeeping (L57/L58): sound, one real fix

- Φ_A = ∮⋆F over any sphere homologous to the throat with no charge between it and the throat. Maxwell's equation d⋆F = J makes it an H₂ class off the sources. This is Wheeler's charge without charge [M].
- **A passage changes Φ by exactly q per signed crossing.** Take a Gauss sphere S around mouth A. Φ_S = Φ_throat + (charge in the shell region between S and the throat). A charge q that comes in from outside S, crosses the throat and leaves by B changes Φ_throat by ±q (sign as in §1). Φ_S returns to its pre-passage value plus that change once the charge has left the shell region. Read only while that region is empty of charge.
- **Radiation-proof: yes.** Source-free fields cannot change an H₂ flux. But every charged passage counts, including stray matter, so the record is net charge transported, not passages of one body. ΔΦ = qΔw holds only if the carrier is the only charge that crossed.
- **Both mouths: zero.** With outward normals Φ_B = −Φ_A, so a surface enclosing both mouths sees only the ordinary enclosed charge and nothing of the handle flux. The ledger's Gauss surface must enclose **exactly one** mouth.
- **Integer.** Φ_0 is an arbitrary real, so only differences Φ − Φ_ref ∈ q₀ℤ are integers, given one carrier species. This agrees with the #381 reference convention.

Fixes:
OLD: `(L47/L52: the ledger tube must enclose the mouth).`
NEW: `(L47/L52: the ledger's Gauss surface must enclose exactly one mouth, since a surface around both reads $\Phi_A+\Phi_B=0$ from the handle; read only when no charge sits between the surface and the throat).`
OLD: `The flux is integer-valued, $\Phi_A=\Phi_0+n\,q_0$, only if`
NEW: `The flux difference from the reference is integer-valued, $\Phi_A-\Phi_{\rm ref}=n\,q_0$ (with $\Phi_0$ an arbitrary real), only if`
OLD: `It changes by exactly $q$ when a charge $q$ passes through the mouth, and by nothing else`
NEW: `It changes by exactly $\pm q$ per signed passage of any charge $q$ (stray matter included), and by nothing else`

## 4. Non-time-orientable handle: what flips? (weak point 7): fix [sketch]

The Gauss charge ∮_S ⋆F needs two things: the Hodge star, which needs the total (space×time) orientation or a twisted ⋆F, and an orientation of S. The charge *attributed to a worldline* uses the linking sphere oriented from the total orientation plus the worldline's future direction. There are three cases for the loop through the handle:

- **Preserves both** (the Set 1 reflection gluing is orientation-reversing on the boundary spheres, so the handle is spatially orientable, and the host is time-orientable): nothing flips, and L54–L58 stand.
- **Reverses time orientation but preserves total orientation** (so it also reverses space orientation; the Hadley-type PT loop): ⋆F is global, so the flux number on a fixed S_A is well defined. The future direction flips along the loop, so a carrier of charge q returns read as −q by local convention (Hadley's mechanism [M]). The flux record survives as a number, but "passages × q" becomes sign-ambiguous.
- **Reverses total orientation** (time-only or space-only reversal): ⋆F is twisted, Φ is defined only up to sign around the loop, and the record is a ℤ/2-twisted quantity, valued in |Φ| or a local sign convention.

Charge is T-even and C-odd as a quantum number. The flip here is a statement about orientation conventions along a loop, not about T. Also, under #381 only Type O returns write, so Type F handles cannot write this record anyway.

Fix:
OLD: `A non-time-orientable handle flips charge sign along the loop (Type F, #364), which would make the flux record orientation-dependent. Unchecked.`
NEW: `What flips depends on the loop: if it reverses time orientation but preserves total orientation (Hadley-type), the flux on a fixed mouth sphere stays well defined but a carrier's charge reads as −q after the loop; if it reverses total orientation, $\star F$ is twisted and the flux is defined only up to sign. Type F loops cannot write anyway (#381). Sketch (Geometry review of batch 16).`

## Set 2 (L56): OK
The static host is CTC-free (t is a global time function). MTY and Frolov–Novikov are [M] as marked.
