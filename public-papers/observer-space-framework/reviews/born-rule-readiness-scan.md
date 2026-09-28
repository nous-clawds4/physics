**SCOPING ONLY, NOT A CLAIM.**

# Born-rule readiness, addendum: the continuous-response scan

Author: Geometry
Date: 2026-09-28
Scope: runs the "one cheap next test: continuous response" of `reviews/born-rule-readiness.md` §3 (merged in #159, d8f35a2), using that note's setup, outcome, computation and PASS/FAIL criterion as written. None of them was changed after seeing results. No paper or essay edits. No choice of (M1)/(M2) or T1/T2/T3. No law of $R$. No Born rule and no $|a|^2$. The only $1/N$ is (M1)'s EPP1 factor $1/|A|$, computed as the named (M1) option alongside (M2), not tuned to anything. The Kretschmann rule is used as stated and is **not** adopted. Paper 1's object is untouched, and type (ii) stays abandonable.

---

## 1. Readings fixed before the full-grid run

The note's spec was implemented literally. Where it left room, these readings were fixed before the 201-germ run. Only a single-germ timing check at $r_p=10$ had been run by then.

1. **"Every bound decision" vs "somewhere".** The PASS clause asks for $|A|=3$ "at every bound decision". The FAIL clause voids the test if $|A|\ne3$ "somewhere". In this tree the two coincide. A history whose jump target is classified plunge, unbound or degenerate leaves the bound sector and takes no further decision, so every decision is a bound decision. $|A|$ was logged at every decision node.
2. **"Still bound".** The chosen arm's orbit is classified `'bound'` by the classifier (`kr.classify`, hardened as in §1.1). Plunge, unbound and `'degenerate'` all count as not bound. Continuing always stays bound.
3. **Depth and arrival.** Depth counts decisions. A jump-reached state does not branch (arrival rule (A), as the note uses it). The history runs along the target orbit's segment to its other turning point, where the next decision is taken. Continuing likewise moves to the other turning point of the current orbit.
4. **(M1).** $w_n^{M1}$ is the sum, over bound depth-$n$ nodes, of $\prod 1/|A|$ along the path, computed as an exact rational.
5. **(M2).** The cut $C_n$ is the depth-$n$ nodes plus the dead-end leaves at depths $<n$ (v0.6 §7, dead ends kept). A history that jumps to a non-bound orbit at decision $k$ is a leaf at depth $k$. $w_n^{M2}=b_n/|C_n|$, where $b_n$ is the number of bound depth-$n$ nodes. It is also an exact rational.
6. **Memoisation.** The memo key is the exact turning-point state $(r,E,L)$ plus the remaining depth. This is equivalent to the note's "memoised on the orbit $(r_{\min},r_{\max})$" together with which turning point one is at, and it does not affect results.
7. **Grid and start.** $r_p=\mathrm{round}(9.00+0.01k,2)$ for $k=0,\dots,200$ and $r_a=20$. Each starting orbit is asserted `'bound'` with turning points $(r_p,20)$. The history starts at periastron. The start at periastron is taken as segment-arrived, so it is a decision with three arms.
8. **Weights are compared exactly**, as `Fraction`s. "Takes at least two values" means two unequal rationals.

Cheap other readings, both reported below:
- (a) count `'degenerate'` targets as still bound (§4);
- (b) (M2) over survivors only, without dead ends. This is not the note's convention and is trivially $\equiv1$, since every surviving node is bound, so it is uninformative.

After the first full run, two bookkeeping-only edits were made to the script:
- the diagnostic target-kind log is now reset per germ (it had accumulated across germs in a worker);
- a stricter assertion now checks that each decision point is a turning point of its orbit.

The rerun gave identical $w^{M1}$, $w^{M2}$, $b_n$ and $|C_n|$ for all 201 germs and all $n$. The pinned hash is that of the edited script.

### 1.1 Classifier

`kr.classify`'s $10^{-9}$ root tolerance misread near-circular and large-$r$ targets. The classifier was hardened (root ordering, with 40-digit roots near coincidence; `scan_robust.py`, Pins), and all figures below use it. It relabels 77 of the 1,505,887 distinct jump targets (69 plunge → bound, 8 degenerate → bound). No value for $n\le5$ changes. Values at 31 germs change for some $n\ge6$.

## 2. Result: PASS, as the note defines it

- **3-arm check.** It holds. $|A|=3$ (min 3, max 3) at every one of the 1,663,466 decision nodes across the 201 germs and depths 1–10: 7,934 to 8,679 per germ, equal to $1+\sum_{n<10}b_n$. The test is not voided.
- **Weights.** Both are constant across the grid for $n=1,2,3$. Both first take two values at $n=4$. For every $n\ge4$, both take several values.
- **Read.** The note's criterion is: *"PASS: for some $n\le10$, $w_n^{M1}$ or $w_n^{M2}$ takes at least two values across the grid, with $|A|=3$ at every bound decision."* That is met, first at $n=4$, for (M1) and (M2) separately. **Read: PASS.** PASS here means only that the two-values condition is met; each response is a step function at finite $n$ (§2.1, §5).
- **Sampling cross-check.** This is not part of the test. `sim.py 0.1 stated 200000 10 7 cross` at $r_p=10$ gives "still bound after 10 decisions" $=0.2301\pm0.0009$. The exact value is $13569/59049=0.2298$.

### 2.1 Distinct values, ranges and change counts

At finite $n$, $w_n^{M1}=b_n/3^n\in3^{-n}\mathbb Z$, because $|A|=3$ everywhere. The script asserts this at every germ. So $w_n^{M1}$ is a step function of $r_p$ with grain $3^{-n}$. $w_n^{M2}=b_n/|C_n|$ has a germ-dependent denominator.

| $n$ | $3^n$ | # distinct $w^{M1}$ | $w^{M1}$ range ($b/3^n$) | # distinct $w^{M2}$ | $w^{M2}$ range ($b/\lvert C_n\rvert$) | adjacent grid pairs (of 200) where $w^{M1}$ / $w^{M2}$ changes |
|---|---|---|---|---|---|---|
| 1 | 3 | 1 | 3–3 /3 (1.0000–1.0000) | 1 | 3/3 – 3/3 (1.0000–1.0000) | 0 / 0 |
| 2 | 9 | 1 | 6–6 /9 (0.6667–0.6667) | 1 | 6/9 – 6/9 (0.6667–0.6667) | 0 / 0 |
| 3 | 27 | 1 | 16–16 /27 (0.5926–0.5926) | 1 | 16/21 – 16/21 (0.7619–0.7619) | 0 / 0 |
| 4 | 81 | 2 | 39–40 /81 (0.4815–0.4938) | 2 | 39/53 – 40/53 (0.7358–0.7547) | 1 / 1 |
| 5 | 243 | 5 | 104–109 /243 (0.4280–0.4486) | 5 | 104/131 – 109/133 (0.7939–0.8195) | 4 / 4 |
| 6 | 729 | 7 | 265–284 /729 (0.3635–0.3896) | 7 | 265/339 – 284/351 (0.7817–0.8091) | 6 / 6 |
| 7 | 2187 | 18 | 709–763 /2187 (0.3242–0.3489) | 20 | 709/869 – 763/919 (0.8159–0.8303) | 26 / 27 |
| 8 | 6561 | 46 | 1846–2027 /6561 (0.2814–0.3089) | 54 | 1846/2289 – 2027/2445 (0.8065–0.8290) | 70 / 71 |
| 9 | 19683 | 99 | 4944–5430 /19683 (0.2512–0.2759) | 121 | 4944/5981 – 5430/6499 (0.8266–0.8355) | 133 / 136 |
| 10 | 59049 | 151 | 12970–14426 /59049 (0.2196–0.2443) | 180 | 12970/15869 – 14232/17085 (0.8173–0.8330) | 181 / 188 |

Grain example: at $n=4$ the whole response is a single step of $1/81$ in (M1), from $39/81$ to $40/81$.

### 2.2 Representative germs: $b_n$ / $|C_n|$

Here $w_n^{M1}=b_n/3^n$ and $w_n^{M2}=b_n/|C_n|$. At $n=2$ every germ has $6/9$.

| $r_p$ | $n=1$ | $n=3$ | $n=4$ | $n=5$ | $n=6$ | $n=8$ | $n=10$ |
|---|---|---|---|---|---|---|---|
| 9.00 | 3 / 3 | 16 / 21 | 39 / 53 | 104 / 131 | 265 / 339 | 1847 / 2289 | 12989 / 15879 |
| 9.25 | 3 / 3 | 16 / 21 | 39 / 53 | 104 / 131 | 265 / 339 | 1853 / 2287 | 13074 / 15919 |
| 9.50 | 3 / 3 | 16 / 21 | 39 / 53 | 105 / 131 | 268 / 341 | 1894 / 2315 | 13417 / 16227 |
| 9.75 | 3 / 3 | 16 / 21 | 39 / 53 | 105 / 131 | 269 / 341 | 1904 / 2321 | 13519 / 16321 |
| 10.00 | 3 / 3 | 16 / 21 | 39 / 53 | 105 / 131 | 269 / 341 | 1906 / 2321 | 13569 / 16345 |
| 10.25 | 3 / 3 | 16 / 21 | 40 / 53 | 107 / 133 | 279 / 347 | 1973 / 2385 | 13942 / 16799 |
| 10.50 | 3 / 3 | 16 / 21 | 40 / 53 | 108 / 133 | 281 / 349 | 1996 / 2413 | 14189 / 17069 |
| 10.75 | 3 / 3 | 16 / 21 | 40 / 53 | 108 / 133 | 281 / 349 | 1997 / 2413 | 14224 / 17081 |
| 11.00 | 3 / 3 | 16 / 21 | 40 / 53 | 109 / 133 | 284 / 351 | 2027 / 2445 | 14426 / 17359 |

The full sets of distinct values for every $n$ are in the appendix.

## 3. Where the weights change, and why

Every change is a threshold where some jump target at some depth crosses the boundary of the bound sector. Across the grid, the branch count is always 3 and only the kinds of the targets change. The first changes were located by diffing the depth-$n$ trees of adjacent germs, and their thresholds were found by bisection in $r_p$ (`scan_aux/mech.py`, `thr.py`, `margin.py`). Path labels list the arms taken: c = continue, + / − = the outward / inward jump.

| threshold $r_p^*$ (bisected) | path (flipping arm is last) | flip | mechanism | first affects |
|---|---|---|---|---|
| 9.337366 | `+++++` (depth 5) | unbound → bound | the target's $E$ crosses 1 at $r\approx67.47$. Just above $r_p^*$ the target orbit is bound with apastron $\sim10^5$–$10^6$ | $n=5$ (and later) |
| 10.122518 | `+++c+` (depth 5) | unbound → bound | the target's $E$ crosses 1 at $r\approx28.70$ | $n=5$ |
| 10.124163 | `+++-` (depth 4) | plunge → bound | at $r\approx71.23$ the target's $E^2$ drops below the barrier peak $V_{\max}$, so an inner turning point (periastron $\approx4.1$–$4.2$) appears | $n=4$ (the only $n=4$ change) |
| 10.270854 | `+++--` (depth 5) | plunge → bound | the target radius ($\approx4.48$) crosses the barrier-peak (unstable circular) radius. It stops being the apastron of a plunge and becomes the periastron of a bound orbit (apastron $\approx18.8$). Exactly at $r_p^*$ it is classified `'degenerate'` (measure zero, not a grid point) | $n=5$ |
| 10.951380 | `+c+++` (depth 5) | unbound → bound | the target's $E$ crosses 1 at $r\approx36.74$ | $n=5$ |

- **Margins at the neighbouring grid points** are far above double precision:
  - $E^2-V_{\max}=+2.3\times10^{-4}$ and $-3.2\times10^{-4}$ at 10.12 and 10.13 for `+++-`;
  - $E-1$ is between $9\times10^{-7}$ and $5\times10^{-6}$ in magnitude for the three unbound → bound flips;
  - the target sits $-0.0021$ and $+0.022$ from the barrier-peak radius at 10.27 and 10.28 for `+++--`.

  The $n=4$ and $n=5$ changes that carry the PASS read are therefore not rounding artefacts. The single $n=4$ change and the four $n=5$ changes fall in the grid intervals (10.12, 10.13), (9.33, 9.34), (10.12, 10.13), (10.27, 10.28) and (10.95, 10.96). The interval (10.12, 10.13) contains two thresholds.
- **$n=6$** adds two more change intervals from new depth-6 flips: (9.56, 9.57) and (10.23, 10.24). Both are plunge → bound, of the same barrier-crossing kind. In (9.33, 9.34), which already changes at $n=5$, the $n=6$ step is $265\to268$.
- **Direction.** For $n\le6$ every flip goes non-bound → bound as $r_p$ increases, so $w_n^{M1}$ and $w_n^{M2}$ are nondecreasing in $r_p$. From $n=7$ onward flips occur in both directions, and neither weight is monotone. At $n=10$, (M1) has 128 up-steps and 53 down-steps.
- **Number of steps.** The count of adjacent germ pairs where (M1) changes grows with depth: 1, 4, 6, 26, 70, 133, 181 of 200 for $n=4,\dots,10$.
- **(M1) vs (M2).** They have identical change points for $n\le6$. At $n=7$, 8, 9 and 10, (M2) has 1, 1, 3 and 7 extra change points, where $b_n$ is unchanged but $|C_n|$ changes because a dead end moved to a different depth. There is no pair where (M1) changes and (M2) does not. As the note says, whether they respond differently is a readout, not a choice. Nothing here chooses between them.

## 4. Caveats (none affects the read)

- **Degenerate targets.** The classifier returns `'degenerate'` for jump targets in 2 germs, all at depth $\ge8$ (`scan_aux/degen_robust.py`):
  - 9.34: depths 8 and 10 (four distinct targets at $r\approx4.7$–$5.2\times10^9$);
  - 10.27: depth 10 (one target at $r\approx1.40\times10^7$).

  All have $E=1$ to within $10^{-7}$–$10^{-10}$ and $\dot r^2=O(10^{-16})$ at the target, yet the target lies $1.0$–$5.6\times10^{-6}$ (relative) from the nearest root. There the target radius is fixed only to about $10^{-6}$, so the label is at the resolution of the arithmetic.

  Under reading 2 (literal) these are not bound. Under the other reading (a), they count as still bound at their depth and, having no other turning point, take no further decision. Reading (a) changes numerators at those 2 germs, by at most 28 at $n=10$, but leaves the number of distinct values and the min/max of both weights identical for every $n$. The first degenerate arm is at depth 8, while the read is fixed at $n=4$.
- **Near-circular target at 10.85.** One target at germ 10.85 ($r\approx17.708$, reached by an inward jump from $r\approx21.227$) has two roots within $1$–$2\times10^{-7}$ (relative). It is classified bound, but perturbing $E$ and $L$ by 2 ulp flips it between bound and degenerate, so 10.85's values for $n\ge7$ are not fixed at double precision. With that target taken as degenerate, 10.85's $b_7,\dots,b_{10}$ are 750, 1991, 5322, 14164 instead of 751, 1994, 5336, 14203. Each count of distinct values then moves by at most 1, each change count by at most 2, and every min/max is unchanged. The only other target with two roots closer than $10^{-6}$ (germ 9.46, gap $4.9\times10^{-7}$) keeps its label under the same perturbation.
- **States at large radius.** Bound orbits just below $E=1$, with apastron $\gtrsim10^5$, appear as destinations, for example after the depth-5 unbound → bound flips in §3. Their later jump targets are classified from the roots, at 40 digits where two roots come within $10^{-6}$. Of the 77 relabelled targets (§1.1), 71 are at $r>10^4$. Apart from the 10.85 target, each of the 77 lies closer to its root than 1% of the smallest root gap. The $n=4,5$ changes above do not depend on any of this, since their margins were checked.
- **Scope.** All of this is on one instance: an unmotivated rule, one orbit family, a picture outcome, and finite depth.

## 5. What this does and does not show (the note's wording)

The note says: *"PASS would show that weights are counting at a grain set by $R$ and that a germ parameter can enter through tree shape alone. It would **not** show Born, $|a|^2$ or interference: the rule is unmotivated, the outcome is a picture, and at finite $n$ every $w_n^{M1}\in3^{-n}\mathbb Z$, so continuous response exists only as a limit (premise 4's grain problem, concretely). Whether (M1) and (M2) respond differently is a readout, not a choice."*

On this instance, then:
- The germ parameter $r_p$ enters the weights of $X_n$ only through which jump targets land in the bound sector. Every decision has exactly three arms.
- At each finite $n$, both responses are step functions of $r_p$: (M1) on the $3^{-n}$ grain, and (M2) with a germ-dependent denominator $|C_n|$. This scan does not show that a continuous limit exists; it shows only that the number of steps grows with $n$.
- The scan does not bear on Born, $|a|^2$, interference, any law of $R$, or the choice between (M1) and (M2). The note's gating order (§3, gates 1–6) is unchanged by it.

## Pins

- **Script:** `/workspace/born/pins/scan.py` (Geometry's box), SHA-256 `9aba5992d28327a84cd8803b997f6798ec3310c5772cba78bb26449ca331d5d3`.
  - It imports `kr.py` (`/workspace/g154/kr.py`, SHA-256 `0432cc20f56afbc3ad862b16de8f825bf9e1d4a490cde07ad8e5740f9d872dee`, the same file pinned in the note) with `THROAT='cross'`.
  - Fixed parameters: $c=0.1$, rule as stated, $r_a=20$, grid $9.00{:}0.01{:}11.00$ (201 germs), $n_{\max}=10$.
  - Exact enumeration; no randomness and no seed.
- **Hardened classifier:** `/workspace/born/pins/scan_robust.py`, SHA-256 `ff8dfb25f5e0787897674b0420872ba503adbd9805d8245aa12967788439c4e6`. It replaces `kr.classify` in `scan.py` by `classify2` and audits every distinct jump target. Runtime about 10.5 min on 4 processes, audit included.
- **Output:** `/workspace/born/pins/scan_out_robust.json`, SHA-256 `cb0dd047e27ca753e95372665c32d21d31d543999c553c730796a98b07958de6`. Per germ it holds $w^{M1}_n$, $w^{M2}_n$, $b_n$, $|C_n|$, $|A|$ min/max, the decision count, the first-decision targets and the target audit. It supersedes `scan_out.json` (`10c5899d…e7b9`, from the unhardened `kr.classify`).
- **Diagnostics** (not part of the test), in `/workspace/born/pins/scan_aux/`:

  | file | SHA-256 |
  |---|---|
  | `mech.py` | `ab66ab80…6137` |
  | `thr.py` | `b5dd96ff…ed98` |
  | `margin.py` | `78a46605…0228` |
  | `degen.py` | `608d297a…0f46` |
  | `tab.py` | `8677db38…c7c2` |
  | `tab_robust.py` | `e6d67062…d058` |
  | `degen_robust.py` | `ac4c65aa…7572` |

- **Cross-check:** `/workspace/g154/sim.py`, SHA-256 `df306f17…e035`, with seed 7 and $N=200000$. This is sampling, used only as a check on the enumeration.

---

## Appendix: all distinct weight values, per $n$

(M1) values are listed as numerators over $3^n$. (M2) values are listed as reduced fractions.


**n = 1.** (M1), 1 values, numerators over $3^{1}=3$: 3.  
(M2), 1 values (reduced): 1.

**n = 2.** (M1), 1 values, numerators over $3^{2}=9$: 6.  
(M2), 1 values (reduced): 2/3.

**n = 3.** (M1), 1 values, numerators over $3^{3}=27$: 16.  
(M2), 1 values (reduced): 16/21.

**n = 4.** (M1), 2 values, numerators over $3^{4}=81$: 39, 40.  
(M2), 2 values (reduced): 39/53, 40/53.

**n = 5.** (M1), 5 values, numerators over $3^{5}=243$: 104, 105, 107, 108, 109.  
(M2), 5 values (reduced): 104/131, 105/131, 107/133, 108/133, 109/133.

**n = 6.** (M1), 7 values, numerators over $3^{6}=729$: 265, 268, 269, 278, 279, 281, 284.  
(M2), 7 values (reduced): 265/339, 268/341, 269/341, 278/347, 279/347, 281/349, 284/351.

**n = 7.** (M1), 18 values, numerators over $3^{7}=2187$: 709, 710, 718, 719, 720, 721, 722, 737, 738, 739, 740, 750, 751, 752, 759, 760, 761, 763.  
(M2), 20 values (reduced): 709/869, 737/903, 710/869, 246/301, 148/181, 739/903, 718/877, 240/293, 740/903, 719/877, 721/879, 720/877, 722/879, 750/911, 751/911, 752/911, 759/919, 760/919, 761/919, 763/919.

**n = 8.** (M1), 46 values, numerators over $3^{8}=6561$: 1846, 1847, 1848, 1849, 1850, 1851, 1852, 1853, 1855, 1856, 1857, 1858, 1882, 1888, 1889, 1890, 1892, 1893, 1894, 1895, 1901, 1902, 1904, 1905, 1906, 1907, 1910, 1911, 1959, 1960, 1961, 1963, 1964, 1966, 1969, 1973, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2019, 2022, 2027.  
(M2), 54 values (reduced): 1846/2289, 1847/2289, 88/109, 1849/2289, 1850/2289, 617/763, 1852/2289, 1851/2287, 17/21, 1852/2287, 1853/2287, 1855/2287, 1856/2287, 1857/2287, 1858/2287, 1882/2313, 1888/2315, 1889/2315, 378/463, 1894/2317, 1893/2315, 1895/2317, 1892/2313, 1894/2315, 631/771, 379/463, 1901/2319, 634/773, 1904/2321, 1905/2321, 1907/2323, 1906/2321, 1910/2323, 1911/2323, 1960/2379, 1959/2377, 1961/2379, 1963/2381, 1964/2381, 1966/2381, 1969/2383, 1994/2413, 105/127, 1994/2411, 1996/2413, 1973/2385, 1997/2413, 1999/2415, 1998/2413, 400/483, 2022/2441, 2019/2437, 674/813, 2027/2445.

**n = 9.** (M1), 99 values, numerators over $3^{9}=19683$: 4944, 4946, 4948, 4949, 4951, 4952, 4953, 4956, 4958, 4959, 4960, 4961, 4962, 4963, 4964, 4965, 4966, 4968, 4970, 4974, 5027, 5041, 5043, 5044, 5046, 5053, 5056, 5059, 5060, 5062, 5064, 5065, 5066, 5069, 5075, 5076, 5079, 5080, 5081, 5083, 5084, 5085, 5096, 5098, 5099, 5100, 5101, 5102, 5103, 5104, 5105, 5106, 5107, 5110, 5111, 5112, 5113, 5120, 5121, 5122, 5124, 5204, 5209, 5211, 5213, 5221, 5222, 5224, 5229, 5230, 5234, 5235, 5236, 5237, 5238, 5307, 5308, 5310, 5321, 5331, 5332, 5333, 5334, 5335, 5336, 5337, 5338, 5339, 5340, 5341, 5342, 5343, 5344, 5345, 5389, 5390, 5399, 5407, 5430.  
(M2), 121 values (reduced): 4944/5981, 4946/5983, 5204/6295, 5234/6331, 4948/5985, 4952/5989, 5235/6331, 707/855, 5209/6299, 4951/5987, 4948/5983, 5211/6301, 4953/5989, 5236/6331, 5027/6077, 1652/1997, 5213/6301, 992/1199, 5238/6331, 4959/5993, 451/545, 5041/6091, 1681/2031, 5222/6309, 5221/6307, 4958/5989, 4963/5995, 4960/5991, 4962/5993, 5224/6309, 4966/5997, 5044/6091, 4963/5993, 4968/5999, 1682/2031, 993/1199, 4970/6001, 5229/6313, 4964/5993, 4966/5995, 5046/6091, 5230/6313, 5237/6321, 1658/2001, 4968/5995, 5053/6097, 5056/6099, 5053/6095, 5075/6121, 5059/6101, 5076/6121, 1769/2133, 5060/6101, 5062/6103, 1693/2041, 5308/6399, 1013/1221, 5080/6123, 5064/6103, 5066/6105, 590/711, 5081/6123, 5069/6107, 391/471, 5084/6123, 1695/2041, 5321/6405, 5096/6129, 5098/6131, 5099/6131, 5100/6131, 5102/6133, 485/583, 5101/6131, 5102/6131, 5104/6133, 5389/6475, 1777/2135, 5103/6131, 1068/1283, 154/185, 5332/6405, 5104/6131, 5106/6133, 5331/6403, 5341/6415, 5333/6405, 5105/6131, 5110/6137, 5340/6413, 5107/6133, 5337/6409, 5342/6415, 254/305, 5399/6483, 269/323, 5336/6407, 5341/6413, 314/377, 5112/6137, 5337/6407, 5339/6409, 5336/6405, 5113/6137, 5338/6407, 5340/6409, 5341/6409, 5336/6403, 5335/6401, 5120/6143, 5336/6401, 5121/6143, 5338/6403, 5407/6485, 5122/6143, 5124/6145, 5342/6405, 1781/2135, 1069/1281, 5344/6403, 5430/6499.

**n = 10.** (M1), 151 values, numerators over $3^{10}=59049$: 12970, 12983, 12989, 12991, 12995, 13003, 13010, 13013, 13025, 13026, 13039, 13050, 13052, 13053, 13055, 13060, 13062, 13063, 13064, 13067, 13071, 13072, 13073, 13074, 13076, 13082, 13097, 13112, 13123, 13125, 13126, 13143, 13277, 13332, 13333, 13334, 13336, 13345, 13346, 13353, 13378, 13399, 13405, 13408, 13411, 13412, 13417, 13418, 13419, 13420, 13430, 13432, 13463, 13466, 13480, 13481, 13484, 13485, 13487, 13490, 13493, 13494, 13496, 13497, 13517, 13519, 13530, 13533, 13535, 13538, 13539, 13548, 13549, 13551, 13552, 13553, 13554, 13558, 13559, 13561, 13563, 13566, 13569, 13571, 13572, 13573, 13612, 13613, 13615, 13627, 13628, 13630, 13843, 13845, 13846, 13859, 13862, 13882, 13889, 13896, 13919, 13920, 13942, 13943, 13945, 13950, 13957, 14114, 14117, 14125, 14127, 14152, 14179, 14180, 14181, 14188, 14189, 14191, 14192, 14193, 14194, 14195, 14199, 14200, 14201, 14202, 14203, 14204, 14205, 14206, 14207, 14210, 14211, 14213, 14214, 14215, 14222, 14224, 14225, 14228, 14229, 14230, 14231, 14232, 14233, 14235, 14345, 14347, 14367, 14369, 14426.  
(M2), 180 values (reduced): 12970/15869, 12983/15875, 12989/15879, 12991/15881, 12995/15883, 13003/15889, 13010/15893, 1183/1445, 13025/15903, 4342/5301, 13039/15911, 870/1061, 13055/15917, 13060/15921, 13064/15925, 13067/15927, 13072/15931, 13052/15905, 13053/15905, 13060/15911, 1866/2273, 13063/15911, 13071/15917, 13073/15919, 13074/15919, 13076/15919, 13082/15921, 13097/15929, 13112/15935, 13277/16131, 13123/15941, 13125/15941, 13126/15941, 337/409, 4444/5391, 13333/16173, 13334/16173, 13336/16173, 13346/16183, 13345/16179, 4451/5395, 13378/16201, 13417/16235, 13418/16235, 1915/2317, 13419/16235, 13408/16221, 2686/3249, 13420/16231, 13417/16227, 13399/16203, 13432/16237, 13411/16211, 13412/16211, 13463/16271, 13466/16273, 13480/16281, 13481/16281, 2697/3257, 13484/16283, 13485/16283, 13490/16289, 13487/16285, 13517/16321, 13493/16291, 13846/16717, 13494/16291, 13519/16321, 13496/16293, 4499/5431, 13496/16291, 13530/16327, 13862/16727, 13859/16723, 13843/16703, 13882/16749, 13533/16327, 13845/16703, 13535/16329, 13539/16331, 13889/16753, 13538/16329, 4513/5443, 1233/1487, 13896/16757, 34/41, 13572/16363, 13549/16335, 13571/16361, 13548/16333, 13573/16363, 13552/16337, 4517/5445, 13553/16337, 14114/17013, 13554/16337, 14117/17015, 13558/16341, 1043/1257, 13558/16339, 13919/16773, 13561/16341, 13942/16799, 14125/17019, 13920/16771, 13945/16801, 4709/5673, 13569/16345, 14152/17047, 13571/16347, 13943/16795, 1550/1867, 13573/16347, 13957/16807, 14369/17299, 13612/16385, 13613/16385, 14193/17083, 1945/2341, 14180/17067, 14179/17065, 4727/5689, 13613/16383, 2723/3277, 2841/3419, 14426/17359, 14205/17093, 14207/17095, 14188/17069, 2842/3419, 13627/16393, 14189/17069, 14214/17099, 14191/17071, 14213/17097, 13628/16393, 14192/17071, 4738/5699, 14367/17281, 14195/17073, 14345/17253, 13630/16393, 14194/17071, 14347/17255, 14195/17071, 14200/17077, 14199/17071, 14201/17073, 14200/17071, 1578/1897, 14201/17071, 2029/2439, 14204/17073, 14206/17075, 14211/17081, 14203/17071, 14213/17083, 14214/17083, 4737/5693, 4738/5693, 14224/17091, 14215/17079, 14215/17077, 14222/17083, 14224/17085, 14233/17095, 2845/3417, 14230/17091, 14222/17081, 14231/17091, 14228/17087, 14230/17089, 14224/17081, 14229/17087, 14231/17089, 279/335, 2033/2441, 4745/5697, 14232/17087, 4744/5695.
