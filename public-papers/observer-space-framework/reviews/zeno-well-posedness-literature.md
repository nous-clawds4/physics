# Literature claim check: Zeno well-posedness (#299)

**Verdict: HOLD (narrow).** The mathematics holds. The near-throat self-target, its attraction and the jump counts all reproduce independently, and the script reproduces byte for byte. Three text strings are required:

- R1: David's (Z-ix) reading carries no relay tag.
- R2: a status phrase is quoted from `obs-as-a-space.md` in the wrong sense, and the note does not disclose that Theorem 16 is stated for $\mathrm{Obs}$ rather than for $V$.
- R3: one (Z-ix) sentence is not scoped to C5, and on toys with $z>0$ it is false.

Four optional strings follow (N1–N4).

**Heads read (re-checked before filing).**

- #299 head is `255b845`, one commit on main `af75d21`. Main is unchanged.
- The diff is four added files: the note (1,175 words by `str.split`), `zwp.py`, `run.sh` and `expected/zwp.txt`.
- Paper 1 and v0.9.1 are untouched.
- This file is a one-file PR from `af75d21`. I merged nothing and messaged no one.

## 1. Topology on record

**v0.9.1 names no topology on $V$.** `grep -i topolog` finds only two lines:

- (J2) in §9: "every target lies within a stated tolerance of the continuation in a named topology *on curvelets*, not merely on germs at the vertex";
- §9's product-ansatz hope: "if the measured distinction locks other topology".

Neither puts a topology on $V$. v0.9.1 never cites `obs-as-a-space.md` or Theorem 16 (no match). §5 cites "Prop. 3.2 and Thm 3 of `papers/geodesic-lifts.md`" for curvelets. The note's first table row is accurate.

**Theorem 16** (`papers/obs-as-a-space.md` §3).

- **Statement.** "Let $\mathcal P_F\subset\mathcal P$ be presentations already in Fermi coordinates for their $u$. The restriction of $\sim_L$ to $\mathcal P_F$ is the $O(3)$-action on the spatial frame. $O(3)$ is compact and acts continuously on $\mathcal P_F$ in the inverse-limit topology (and in the analytic inductive-limit topology). The quotient … is therefore Hausdorff … Hence $\mathrm{Obs}$ is in bijection with $\mathcal P_F/O(3)$, and the quotient topology on that slice is a well-defined Hausdorff topology on the set of lumps."
- **The two variants are correct.** §1 of that paper gives the inverse limit, and "the honest analytic topology on germs is the inductive limit".
- **"Stateable, not written" is misattributed.** In §4 of that paper the phrase refers to a neighbourhood-law for $R$ ("A neighborhood-law for type-(ii) $R$ is therefore a possible sentence. It is not adopted."), not to the topology.
- **The theorem is stated for $\mathrm{Obs}$, the set of lumps.** The note reads it as a topology on $V$ ("Its slice fixes $u$, so its points carry $u$"). That reading is defensible, since $\mathcal P_F$ is built from $u$, but it differs from the theorem's own label and is not disclosed (**R2**).
- **Not adopted anywhere.** The theorem is used only to state named extras: `closed-graph-r.md`, `open-graph-r.md`, `compact-stars.md`, `extra-structure.md` (§5) and `fermi-distance.md`.
- **A compatible metric is on record.** `fermi-distance.md` gives "a candidate *Fermi-slice distance* on $\mathrm{Obs}$ … Extra packaging of Theorem 16", with Theorem 24 and "Not adopted". So the note's "Anything else (a metric on $V$ …) would be new" is too broad. A compatible metric is on record and gives the same limits (N1).

**Other citations.**

- **`geodesic-lifts.md` Theorem 3:** "$\gamma:I\to\mathrm{Obs}$ is a real-analytic curve … each projection of $\gamma$ to a finite-order jet space $J^k$ is a real-analytic map". This is a curve notion. The note uses it only for accumulation along a segment (C8), which is within its scope.
- **The closed-graph, open-graph and compact-stars notes:** each opens with "Theorem 16 … Fermi-slice topology … exists" and calls its condition "extra", "Not adopted". The note's "conditions on $R$ … named extras; they give no limit notion of their own" is accurate. The note cites no theorem numbers from them, so there are none to check.

## 2. The examples against Appendix A

- **C5:** "Kretschmann rule, $c=0.01$ outward: $10\to10.108\to10.217\to10.328\to\cdots$, every target a turning point, all at one accumulated $\tau$ (model without (a))". The note matches.
  - The "FD1 option (i), a Lead ruling" pointer is correct. `reviews/zeno-and-born-readiness-pressure-test.md` §3, Zeno FD1: "**Lead ruling (2026-10-11, under David's delegation of 12:34 PM ET; relayed, not signed)**: option (i). §8.2 item 8 is left as written". The note gives it without its form (N3).
- **C7:** "No Zeno on the bound Schwarzschild instance under (A)". As read.
- **C8:** flat FLRW, $H=2+\sin(1/(1-t))$, "$K$ is unbounded as $t\to1$". So order-2 Fermi coefficients diverge, and no limit exists in either variant. As read.
- **Toys.** C35 and V0–V2 carry no germs. As read.

## 3. The near-throat self-target, verified independently

I used my own mpmath code (dps 40), not `zwp.py`.

| $c$ | $r^*$ | $\Delta\ell^*$ | landing from $r^*$ | multiplier |
|---|---|---|---|---|
| 0.1 | $2.000361017638$ | $0.05374304494885$ | lands at $r^*$ ($-4\times10^{-43}$) | $-0.998917208$ |
| 0.01 | $2.0000036084565$ | $0.005372864199895$ | lands at $r^*$ ($-4\times10^{-44}$) | $-0.999989175$ |

- **The values match the note.** The multiplier is the derivative of the through map $\Delta\ell\mapsto\varepsilon(r(\Delta\ell))-\Delta\ell$ at $\Delta\ell^*$. Analytically it is $\tfrac32\varepsilon\sqrt{1-2/r}/r-1$, which gives the same values.
- **Same point as #293 N2.** This is the second $\varepsilon=2\Delta\ell$ root that #293 N2 flagged ($r_0\approx2.000361$). #290 gives it only as the edge of the near-throat window "$2<r_0<2.000361$" and does not call it a self-target.
- **Attracting.** I iterated inward chains under "through" at $c=0.1$ from $r_0=2.0001$, $2.0003$, $2.0005$, $2.001$, $2.002$, $2.01$, $3$ and $10$. Every one converges to $\Delta\ell^*$: $|\Delta\ell-\Delta\ell^*|<1.4\times10^{-11}$ after 20,000 jumps, and $<10^{-13}$ after 25,000. The contraction per jump is about $1-1.08\times10^{-3}$ at $c=0.1$ and $1-1.08\times10^{-5}$ at $c=0.01$, so the slow $c=0.01$ run is expected.
- **The far root is repelling.** The multiplier at $2786.4692$ is $\approx2.007$, as stated.
- **"Modulo which exterior" is necessary and disclosed.** In the late chain every jump crosses the throat: 24,961–24,999 crossings out of 25,000 in my runs. Each crossing swaps exteriors, so with exterior labels kept the chain has two accumulation points. The note says this and calls it "a gauge reading, not picked here".
- **"Any chain" argument.** Convergence of $\Delta\ell_n$ needs steps that tend to 0. A step that does not cross the throat moves $\Delta\ell$ by $\varepsilon\ge\varepsilon(2)>0$. So the late steps are crossings with $\Delta\ell\to\varepsilon/2$. This is sound.

## 4. The mass claim, and the disclosed gaps

- **C5's chains do have mass 0.** Under (M1) a run of $n$ consecutive jumps has weight at most $(2/3)^n$, so the conclusion for (Z-ii), (Z-iii), (Z-vi) and (Z-vii) holds where $z=0$. (Z-0)/(Z-i) is rightly left out: a measure-zero Zeno history already makes weights undefined there (Zeno note, V0).
- **The next sentence is unscoped.** "(Z-ix) changes only which histories item 8 ends" holds for C5. On toys with $z>0$ it is false: C35's $Z$ has mass $1/2$, and the Zeno note's (Z-ix) row gives "With a limit state added at each accumulation point and continued as one history: $1/2$ on all four if clause (2) is read as met by continued histories, undefined if not", which moves C35's (Z-iii) value from $1$ to $1/2$ or to undefined. V0 has $z=0$ (Zeno note; #270 §2). **R3** scopes the sentence to C5.
- **Both gaps are disclosed in the note itself**, not only in the PR body:
  - "For the inductive-limit variant I have not proved that the radii of convergence stay bounded below";
  - "at $c=0.01$ convergence is slower and was not run to the end (pin (2))".

## 5. Scripts, terms, picks and guardrails

**Scripts** (fresh clone at `255b845`):

- Pins match: `zwp.py` `1777f0be425d`, `run.sh` `36afcad10523`, `expected/zwp.txt` `2c5def6dcc2b`.
- `sh run.sh` reproduces `expected/zwp.txt` byte for byte (about 14 s, with a `python` wrapper around Python 3.13.5 and mpmath 1.3.0).
- No secrets and no absolute paths.

**Terms.** Several are used without definition (N2–N4):

- "multiplier";
- "self-target" (#290 (T3) defines the case, not the word);
- "partner" (the Zeno note's N-b) and N-a;
- bare "item 8" (§8.2 item 8).

**Neutrality.**

- "(Z-ix) is not yet well-posed" is a finding, not a pick. The Zeno note's N-a and plan item 2 already mark (Z-ix) ILL. The note says it "becomes well-posed once a notion is named", and its critic questions leave the choice of notion and variant open.
- Nothing is picked on the Zeno readings, the throat convention, F11, gauge or grain.
- (M1) is cited as ruled at L3, relayed, not signed.
- David's (Z-ix) reading is named as David's, but without the relay tag the Zeno note uses ("as relayed by the Physics Lead; not otherwise recorded") (**R1**).

**Guardrails.**

- χ, `\chi`, egalit, cartoon, GRW, 4-geon, spin-foam, Everett, Deutsch, Wallace and Born: 0.
- No $|a|^2$ or 1/N; no law of $R$.
- Paper 1 and v0.9.1 are untouched, and the diff is only the four files.

## Exact strings (file `notes/zeno-well-posedness.md`; each OLD occurs once at `255b845`)

**R1 (required: relay tag on David's reading).**
OLD: `*Standalone note answering the Physics Lead's question on David's (Z-ix) reading, using #297's method.`
NEW: `*Standalone note answering the Physics Lead's question on David's (Z-ix) reading (proposed by David, relayed by the Physics Lead, not signed; `notes/zeno-mass-scoping.md`), using #297's method.`

**R2 (required: Theorem 16's status and domain).**
OLD: `| on record, Hausdorff, "stateable, not written"; not cited by v0.9.1. Its slice fixes $u$, so its points carry $u$ |`
NEW: `| on record and Hausdorff; not adopted, and not cited by v0.9.1 (that paper's "stateable, not written" refers to a neighbourhood-law for $R$, not to the topology). The theorem states it as a topology on $\mathrm{Obs}$, the set of lumps; its slice fixes $u$, so its points carry $u$, and this note reads it as a topology on $V$ |`

**R3 (required: scope to C5).**
OLD: `(Z-ix) changes only which histories item 8 ends.`
NEW: `On C5, (Z-ix) changes only which histories §8.2 item 8 ends. This rests on C5's mass being 0. On toys with Zeno mass $z>0$ (C35 has $z=1/2$), the Zeno note's (Z-ix) row shows that a stipulated limit state can change weights (to $1/2$, or to undefined, depending on how clause (2) is read).`

**N1 (optional: a compatible metric is on record).**
OLD: `Anything else (a metric on $V$, a topology through which a limit may leave the slice) would be new.`
NEW: `A compatible metric is also on record (`papers/fermi-distance.md`: a candidate Fermi-slice distance, "extra packaging of Theorem 16", not adopted); it gives the same limits. Anything else (a metric generating another topology, a topology through which a limit may leave the slice) would be new.`

**N2 (optional: define "multiplier").**
OLD: `with multipliers $-0.99892$ and $-0.99999$, so it is attracting.`
NEW: `with multipliers $-0.99892$ and $-0.99999$ (the derivative at $\Delta\ell^*$ of the through map $\Delta\ell\mapsto\varepsilon(r)-\Delta\ell$), so it is attracting.`

**N3 (optional: Lead-ruling form).**
OLD: `Zeno by item 8 under FD1 option (i), a Lead ruling)`
NEW: `Zeno by §8.2 item 8 under Zeno FD1 option (i), a Lead ruling (2026-10-11, under David's delegation of 12:34 PM ET; relayed, not signed; `reviews/zeno-and-born-readiness-pressure-test.md` §3))`

**N4 (optional: "partner").**
OLD: `So no partner row becomes redundant.`
NEW: `So no partner row (the Zeno note's N-b) becomes redundant.`
