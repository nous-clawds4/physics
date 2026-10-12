# Literature pass 2: measurement model v0 (#372), after Claude job 013

Reviewer: Literature agent. The brief names head `957ea4b`; the PR head re-checked is **`3ac2abc`**. That is one commit later, touching the ledger and charter only (the 5:00 PM row). The note is identical at both. Do not merge. Marks: **V-text** = wording read by us; **V-meta** = bibliographic or secondary only; **computed** = our own calculation.

## Results

1. **Misner–Taub 1969 (Sov. Phys. JETP 28, 122): stays V-meta, "relayed from external review".**
   - I could not read the text: the JETP archive was unreachable and there is no arXiv copy.
   - Claude's reading is not our V-text. The note's §2.5 dichotomy bullet labels it correctly ("relayed from external review (Claude job 013), pending Literature confirmation").
   - Three other places quote it as if checked, with no label: S1–S3 below. The ledger has the same problem (S4).
   - **Content check (computed, item 6):** the §II C claim is right.
2. **Hawking–Ellis §5.8 and §6.5: V-meta.** Not reachable.
   - The note's "Hawking–Ellis's non-Hausdorff extension = $(\mathbb R^2\setminus\{0\})/B$" is confirmed secondarily (V-text) by Rieger's abstract: "enlarging across both sides simultaneously yields the punctured Minkowski plane modulo the same boost action, producing the standard non-Hausdorff extension".
   - §6.5 is marked "unverified" in the note. Correct.
3. **Hájíček, J. Math. Phys. 12 (1971) 157: V-meta** (from Clément–Gal'tsov–Guenouche's reference list; I could not resolve the DOI). The note's "unchecked" is correct.
4. **Geroch 1968:** not cited in the note at this head (ledger L3/L5 cite Geroch–Traschen and Choquet-Bruhat–Geroch, unchanged). Nothing to check.
5. **Rieger, "Coverings and Non-Hausdorff Extensions of Misner Spacetime", arXiv:2402.09312v3 (4 Apr 2026): V-text** (abstract and §§5–6 read).
   - Prop. 6.4: every inextendible geodesic in each $E_n$ is complete or reaches a missing preimage of the fixed point $Q$. The proof (lift to the flat covering; straight lines) is elementary and correct. It matches #375's computation.
   - Prop. 5.5: maximality is only "within the class of analytic manifold extensions obtained by taking a connected covering … lifting the boost action". The note's "infinitely many further non-Hausdorff maximal extensions" is acceptable if "maximal" is read in that restricted class.
   - **Plausible.** It is a preprint, and the note says so.
6. **Taub–NUT, $p_\parallel=0$, $p_\perp\neq0$ (computed).**
   - Metric near the horizon: $-U^{-1}dt^2+4l^2U(d\psi+\cos\theta\,d\phi)^2+(t^2+l^2)d\Omega^2$, with conserved $p_\parallel=4l^2U(\dot\psi+\cos\theta\dot\phi)$.
   - The extensions use $\psi_\pm=\psi\pm\int dt/(2lU)$.
   - If $p_\parallel=0$, then $\dot\psi$ stays finite, while $\dot t\sim\sqrt{U}$ (whatever $p_\perp$ is). So $d\psi_\pm/dt\approx\pm1/(2lU)$, and $\psi_\pm$ diverges logarithmically at finite affine parameter in **both** extensions.
   - If $p_\parallel\neq0$, then $\dot t\to\pm|p_\parallel|/2l$, and the divergent terms cancel for exactly one sign: that extension is crossed.
   - **So a geodesic with $p_\parallel=0$ continues in neither extension, for any $p_\perp$.** The reviewer's reading is confirmed. This is our computation, not V-text of Misner–Taub.
7. **S-matrix wording (§1, §2.2).**
   - §1 is consistent: classical model, and an in→out map may fail to exist or to be unique.
   - §2.2 has two errors:
     - (a) the heading says "citations unchecked by us", but Friedman–Papastamatiou–Simon and Kay–Radzikowski–Wald abstracts are V-text by Literature;
     - (b) the classical linear-field map is credited to Friedman et al. 1990 ("benign", an existence result) instead of Friedman–Morris 1991/1997 (uniqueness on a restricted class, V-meta).
   - FPS's abstract (V-text): "The scattering of free quantum fields is well defined on a class of asymptotically flat spacetimes with closed timelike curves … the S matrix is unitary as well … the unitarity relations are not satisfied for interacting fields". The note's free/interacting sentence is correct.
   - KRW wording is correct. See S5 and S6.
8. **5:00 PM row.** It is verbatim-labelled and relayed, not signed, and identical across the note, ledger and charter. I can't check it against a primary record.
   - "follows inevitability" reads like a slip for "inevitably". Since the row is verbatim, keep it (optionally add "[sic]"). It is not an error for us to change.
   - It records a guiding constraint, not a geon ruling. (M1) stays at L3.

## Strings (each OLD occurs once at 3ac2abc)

S1. `notes/creative/measurement-model-v0.md`
- OLD: `cannot be continued across [the horizons] in either of the two space-times" (Misner–Taub 1969, §II C)`
- NEW: `cannot be continued across [the horizons] in either of the two space-times" (Misner–Taub 1969, §II C; quotation relayed from external review, Claude job 013, V-meta for us; content confirmed by Literature's own computation, #377)`

S2. `notes/creative/measurement-model-v0.md`
- OLD: `twice" (Misner–Taub 1969, §III)`
- NEW: `twice" (Misner–Taub 1969, §III; relayed from external review, Claude job 013; V-meta for us)`

S3. `notes/creative/measurement-model-v0.md` (open problem 13)
- OLD: `continue in neither extension (Misner–Taub 1969, §II C)`
- NEW: `continue in neither extension (Misner–Taub 1969, §II C, relayed from external review, V-meta; confirmed by computation, #377)`

S4. `notes/creative/ledger.md`
- OLD: `continue in neither extension (Misner–Taub 1969, §II C)`
- NEW: `continue in neither extension (Misner–Taub 1969, §II C, relayed from external review, V-meta; confirmed by computation, #377)`

S5. `notes/creative/measurement-model-v0.md`
- OLD: `**S-matrix (Literature, relayed; citations unchecked by us).**`
- NEW: `**S-matrix (Literature, relayed; FPS and KRW abstracts V-text, the rest V-meta).**`

S6. `notes/creative/measurement-model-v0.md`
- OLD: `For classical linear fields an in-to-out map is known only on "benign" spacetimes (Friedman et al. 1990; #364 (c)).`
- NEW: `For classical linear fields an in-to-out map exists and is unique on a restricted class of CTC spacetimes (Friedman & Morris, PRL 66 (1991) 401 and CMP 186 (1997) 495, V-meta); Friedman et al. 1990 show only that wormhole spacetimes are "benign" (no constraint on the data; abstract V-text, #365).`

## Guardrails
- No forbidden symbol.
- No Born/$|a|^2$/$1/N$ result. "Quantum statistics" appears only in David's verbatim 5:00 PM words.
- No Everett framing.
- No pick among M1/M2/T-options or on CTCs.
- Paper 1 untouched.
- No David geon ruling is claimed.
