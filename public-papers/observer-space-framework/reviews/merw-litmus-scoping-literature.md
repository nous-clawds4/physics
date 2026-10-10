# Literature check: MERW litmus scoping note (#250)

**Verdict: HOLD (narrow).** Two Burda attributions need tightening: the $\psi^2$ density applies only to a symmetric adjacency, and the R4 toy localisation is not Burda et al.'s result. Three strings are recommended and one is optional. All numbers reproduce. **Heads read:** #250 head `ecf9d1b` (`notes/merw-litmus-scoping.md`, 1,104 words by `str.split`), off `f920ca3`. Main is `001dde2` (#248 merged at head `f0bf021`). I read `versions/v0.9-prose.md` and `reviews/born-rule-readiness.md` at `001dde2`. I re-checked the head before filing.

## Findings

- **F1. Burda et al. 2009 (arXiv:0810.4113v2, read in full).**
  - *Setting.* They assume an undirected, finite, connected graph. They write of a particle "hopping randomly from node to node on a given finite, connected graph. The graph is defined by a symmetric adjacency matrix A, with elements A_ij = 1 if i and j are neighboring nodes and A_ij = 0 otherwise."
  - *Construction.* Perron–Frobenius gives $\psi_i>0$. The transition probability is $P_{ij}=A_{ij}\psi_j/(\lambda\psi_i)$, eq. (7). "The stationary distribution of MERW is $\pi^*_i=\psi_i^2$", eq. (9), with detailed balance.
  - *Directed graphs.* The paper says nothing about directed graphs or the left/right eigenvector product.
  - *Quantum framing.* They call the localisation "purely classical in nature, … explained in terms of the Lifshitz states of a certain random operator". They link it to the ground state of a discretised Schrödinger operator. Their only quantum remark is a closing aside on the path-integral formalism ("It would be interesting to [see to] what extent … if one constructed quantum amplitudes using MERW instead of GRW"). The note does not overstate this: it claims no quantum-like look for MERW.
  - *Two attribution defects.*
    - Line 7 states "$\psi^2$ MERW's density" for any "nonnegative irreducible operator". Burda et al. give it only for a symmetric adjacency (string 1).
    - R4 cites "(Burda et al. 2009)" for $P_4$–$K_4$ localisation. Burda et al. show localisation on weakly diluted lattices. The $P_4$–$K_4$ figures are the program's own toy (string 2).
  - O3's "Burda's setting" is fair in spirit. But $\mathcal A+\mathcal A^{\top}$ is the program's own construction, and it has entries 2 on two-way pairs, while Burda et al. assume a 0/1 adjacency (string 3, recommended).
- **F2. Circularity literature.**
  - The note cites no circularity literature and claims none exists. Its only literature is "as v0.9 cites it": Burda 2009, Duda 2011 and Faber 2024, and Duda and Faber are not used in the body.
  - Its anti-route observations are the program's own: positivity excludes cancellation (elementary), and phases are "supplied" by hand on $C_4$ (computed). They need no citation.
  - For existence only, Duda's MERW→Born papers exist: arXiv:1111.2253 (v0.9's entry; its abstract speaks of "a natural intuition of the amplitudes' squares relating to probabilities") and arXiv:0910.2724 (2009–2023 versions, "the Born rule with squares"). I am not proposing additions.
  - The note does not quote or touch the inherited circularity wall (v0.9 §10, Paper 1 §8).
- **F3. Numbers reproduce.** I ran the pinned scripts (hashes match) in my own venv and read the output.
  - **c=0.01:**
    - Robust classifier: 87,356 states, 29,119 orbits, 58,237 SCCs, of which 29,119 are 2-cycles. Each 2-state block $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ contributes eigenvalues $\pm1$, and the rest is acyclic. So eigenvalue 1 has multiplicity 29,119 and $\psi^2$ is undefined.
    - `kr.classify`: 87,357 states and the same 29,119 2-cycles.
  - **Jump shares:** 0.400, 0.381974, 0.381966, 0.308087, 0.137830, 0.011828, 0.005865 at $L=2$–$2000$. $1/\varphi^2=(3-\sqrt5)/2=0.381966$.
  - **Other c=0.01 figures:** $\log_2$ growth 14.185, with a 14-jump concentration of 0.8931 and 0.9909. The two classifiers agree to 6 decimals on shares and to 4 figures on jump laws.
  - **c=0.1:** 3 orbits, chain 1, 0.999, 0.000500 and 0.9995.
  - **Toys:** overlap 0.933865; $P_4$ mass 0.042369, $5.676\times10^{-3}$, $7.604\times10^{-4}$, $1.019\times10^{-4}$; degenerate $P_4\sqcup P_4$; $\mathrm{tr}\,H^4=32, 24, 16$.
  - The positivity inequality holds, since the cross term is $2ab\psi_1\psi_2\ge0$.
- **F4. Pointers check except F5.**
  - v0.9 references:
    - §2's "a named hazard for (M2), not a route taken" (verbatim) and §9's "a hazard for (M2), not a Born claim".
    - The §12 MERW row ("A hazard, not a claim"), and C36, which does not use the phrase.
    - §8.2 item 2 ("jumps that carry no $\tau$") and item 7.
    - §8.4/C26, the §11 open call "Backward-only pairs in R", and the C33 figures (29,119; chain 14).
  - Readiness references: §1.2 ("nowhere, today"; path-integral route out of scope), l.56 ("a hazard, not a route"), gaps 5 and 6, and P7.
- **F5 (recommended): pointer drift after #248 merged.**
  - The LT3 row still lists "(J1)/(J2)" as a waits-on. #248 dropped that pairing from the litmus note (#249 string 2, now on main), so string 4 aligns the row.
  - The Read-at line names #248's superseded head `01e6a35` (string 5).
  - LT1's "can cancel" paraphrases David's "interferes" (string 6, optional).
- **F6. No pick or route.** The note does not decide F-M1: it gives neutral options (i)–(iii) and edits nothing. MERW is not presented as a Born route. There is no Born, $|a|^2$ or $1/N$ result, and no (M1)/(M2), T, Q-D, #139, Z or law-of-R pick.
  - "MERW is a long-path count, an (M2)-side object" restates C36 and §9.
  - The costs cover O2, O3 and O5. O1's costs are in its table row, and O4 has none to list.
- **F7. Critic questions: PASS.** All five are well-posed and unloaded, and they match the body. Q5 openly flags that R2 fails on $L$.
- **F8. Guardrails: PASS.** No banned words, no Everett-vs-Deutsch–Wallace framing, no Bell claim. Paper 1 and `versions/` are untouched, and the note is the only file in the PR.

## OLD/NEW (file `public-papers/observer-space-framework/notes/merw-litmus-scoping.md` at `ecf9d1b`; each OLD occurs once)

1. (required) OLD: `with $\psi^2$ MERW's density (§9).`
   NEW: `with $\psi^2$ MERW's stationary density when the operator is the symmetric adjacency matrix of a finite connected graph, the only case Burda et al. (2009) treat (§9).`
2. (required) OLD: `$P_4$ joined to $K_4$ localises (Burda et al. 2009):`
   NEW: `$P_4$ joined to $K_4$ localises, a toy analogue of the localisation Burda et al. (2009) show on weakly diluted lattices:`
3. (recommended) OLD: `(Burda's setting)`
   NEW: `(Burda et al. assume an undirected graph: a symmetric 0/1 adjacency, finite and connected)`
4. (recommended) OLD: `(M1)/(M2) and the cut; (J1)/(J2); (Z-0)–(Z-v)`
   NEW: `(M1)/(M2), completed versus cut; (Z-0)–(Z-v)`
5. (recommended) OLD: ``notes/born-litmus-test.md` (L3) from #248 at `01e6a35``
   NEW: ``notes/born-litmus-test.md` (L3) as merged in #248 (`001dde2`)``
6. (optional) OLD: `"Amplitude-like" (LT1): $\psi$ superposes, evolves linearly and can cancel.`
   NEW: `"Amplitude-like" (LT1): $\psi$ superposes, evolves linearly and interferes (so it can cancel).`

I applied all six mechanically. Each matches once, and the note goes from 1,104 to 1,152 words.
