# Literature pass: creative batch 09 (L31), PR #357

Reviewer: Literature agent. PR head re-checked: `75111ac` (base `creative/batch-08`). Files: `notes/creative/batch-09.md`, `batch-09/shares.py`, `batch-09/results.txt`, ledger L31. Do not merge. Marks: **V-text** = wording read; **V-meta** = bibliographic data verified, content from the standard account.

**No wrong claims found; no OLD/NEW strings.**

## 1. Subgroup growth and L31

| Source | Mark | Bearing |
|---|---|---|
| Lubotzky–Segal, *Subgroup Growth*, Birkhäuser (2003) | V-meta | Standard reference. |
| Grunewald–Segal–Smith, Invent. Math. 93 (1988) 185 | V-meta | $\zeta_{\mathbb Z^n}(s)=\prod_{i=0}^{n-1}\zeta(s-i)$, so $\#\{\Gamma:[\mathbb Z^n:\Gamma]\le N\}\sim c_nN^n$: polynomial growth. |
| M. Hall, Canad. J. Math. 1 (1949) 187 | V-meta | Free groups: $a_n(F_r)\sim n(n!)^{r-1}$, super-exponential. |
| Mednykh (1979); Müller–Puchta, J. London Math. Soc. 66 (2002) 623 | V-meta | Surface groups: super-exponential, about $(n!)^{2g-2}$. |

**The batch's mechanism is right.** For $\mathbb Z^2$, subgroups containing a fixed primitive vector number $\asymp N^{n-1}$ against $N^n$ in total, so the share tends to 1 at rate $1/N$. That matches the data and weak point 2.

**Note on L31 (no string).**
- "A host class whose record-consistent counts grow like the total (not $\mathbb Z^n$)" is stated as a need, not a prediction. So it is fine as written.
- But the literature suggests that faster growth alone does not help. In free groups, a random index-$n$ subgroup contains a fixed $g\ne1$ with probability $O(1/n)\to0$: Nica, Random Struct. Algorithms 5 (1994) 703 (V-meta), via fixed points of word maps on random permutations.
- So for free and surface groups, the proportion of subgroups containing a given element still tends to zero. The 0/1 degeneracy is expected to persist, and L31's first escape is unlikely from growth rate alone. Its second escape, records that stay ambiguous at full rank, is untouched by this.

## 2. Is the 0/1 degeneracy known?

Yes, structurally.
- Cutoff-defined shares over a countable infinity are natural densities. A class of density zero gets share 0, and its complement gets 1.
- Natural density is finitely but not countably additive, and there is no uniform probability on $\mathbb N$. This is standard (V-meta), so a class of measure zero under the exhaustion gets 0 however it is listed.
- The cosmology analogue is the measure problem, where the growing cutoff hands the whole share to the class that grows fastest:
  - Guth, "youngness paradox" (Phys. Rep. 333 (2000) 555; J. Phys. A 40 (2007) 6811), V-meta;
  - Tegmark, "What does inflation really predict?", JCAP 0504 (2005) 001, V-meta;
  - Bousso–Freivogel–Yang, "Boltzmann babies in the proper time measure", PRD 77 (2008) 103514, V-meta.
- The batch's result is a clean instance of this. Citing it as known would strengthen L31. Optional.

## 3. Standing rule and the $E_{\mathcal W}$ labelling

- **Rule met:**
  - label present verbatim;
  - countability stated (finite-index sublattices by HNF, finite at each $N$);
  - inevitability stated (listing-independence, honestly flagged as trivial).
- (M1) is kept separate and not used.
- The **$E_{\mathcal W}$ quote** matches v0.10.1 §4 exactly (origin/main, V-text).
- Counting each $\Gamma$ with the observer pinned at the origin is a count over pointed worlds. That labelling is correct.
- The abelian remark (conjugation is trivial, so pointed and unpointed counts differ only by point-group symmetry) is correct, and the non-abelian gap is disclosed.

## 4. Overclaim

None found.
- Results are stated as exact counts within a sketched model.
- "Born-like structure does not appear" is a negative.
- The full-rank sketch is correct as far as it goes: a proper overlattice of $L_0$ adds a coset representative of length ≤ the covering radius of $L_0$, which is ≤ $\tfrac{\sqrt n}{2}\max|b_i|$. It is marked unchecked beyond the 2D example.
- Listing agreement is explicitly called trivial, and finite-cutoff differences are disclosed.

## Spot-check of results.txt

I re-ran `shares.py` functions at head:
- $\mathbb Z^2$, $N=20$: 339 subgroups ($=\sum_{n\le20}\sigma(n)$, as the zeta function predicts), with the empty-record class at 300 worlds and share 0.760, and the 19-world classes at 0.947. Exact match.
- $\mathbb Z^3$, $N=10$: 737. Match.
- The listing comparison draws from index ≤ 400. The covering-radius ≤ 10 and word-length ≤ 12 lattices have covolume ≤ about 260 and ≤ 144 respectively, so the truncation is harmless.

## Guardrails
- No forbidden symbol.
- No Born/$|a|^2$/$1/N$ result. The $1/N$ here is a convergence rate of counting shares, not a probability rule.
- No interpretation-camp framing.
- No pick among M1/M2/T-options.
- Paper 1 untouched.
- David's words are referenced as relayed, not signed.

## Verdicts
- **Literature:** citations verified (V-meta; v0.10.1 V-text). The 0/1 degeneracy is a known natural-density / cutoff-measure phenomenon. Free-group growth likely does not escape it (note, no string).
- **Standing rule and $E_{\mathcal W}$:** met; labelling correct.
- **Framing:** no overclaim; results.txt reproduces.
