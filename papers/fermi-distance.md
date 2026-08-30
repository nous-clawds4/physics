# Fermi-slice distance is a continuous scale

David Strayhorn

Can a distance on the Fermi-slice topology serve as a clock or a slice for type (ii)? If it is just a continuous scale, it dies the way Theorems 17–18 kill neighborhoods and continuous invariants. Do not adopt a metric scale. Do not put $1/N$. Do not lock a grain. Do not write $\Phi$. Do not write a law of $R$. Paper 1 not rewritten.

Companions: `papers/obs-as-a-space.md`, `papers/neighborhood-uncountable.md`, `papers/grain-not-from-invariants.md`.

**Status.** Theorem 24: any metric (or continuous scale) compatible with the Fermi-slice topology fails as a finite slice and as a generation. Rounding it is a grain. Not a claim that no metric exists. Not adopted.

---

## 0. What the topology already is

Theorem 16: Fermi presentations modulo compact $O(3)$ give a Hausdorff topology on $\mathrm{Obs}$. Neighborhoods of lumps exist. Open balls minus $\gamma_O$ are uncountable (Theorem 17). Continuous $f:\mathrm{Obs}\to\mathbb{R}^n$ on a connected open yield one class or a continuum (Theorem 18).

The inverse-limit topology on $J^\infty$ is metrizable. Compact $O(3)$ acts continuously on the Fermi slice $\mathcal{P}_F$. A quotient metric
$$
d([x],[y])\;=\;\inf_{g\in O(3)}\,d_{\mathcal{P}_F}(x,g\cdot y)
$$
is then a candidate *Fermi-slice distance* on $\mathrm{Obs}$. Any metric generating the same topology, or any $d:\mathrm{Obs}\times\mathrm{Obs}\to[0,\infty)$ continuous in that topology, is the same kind of scale. Extra packaging of Theorem 16, not a new lock-side functor.

---

## 1. Theorem 24. Continuous scale, not a slice or a clock

**Theorem 24.** Let $d$ be a metric generating the Fermi-slice topology, or merely a function $\mathrm{Obs}\times\mathrm{Obs}\to\mathbb{R}$ continuous in that topology. None of the following is a nonempty finite typicality set of delayed forks, nor a generation of type-(ii) targets:

1. an open ball $\{O':d(O,O')<\varepsilon\}$ for $\varepsilon>0$;
2. a metric sphere $\{O':d(O,O')=c\}$;
3. a sublevel set of $d(O,\cdot)$ on a nonempty connected open.

Rounding $d$ to $k$ decimals (or to a mesh $\delta$) is a grain, the same kind of choice as $d$-decimal truncation, and is not adopted.

**Proof.** (1) Open balls are Fermi-slice neighborhoods. Theorem 17: $U\setminus\gamma_O$ is uncountable. Type-(ii) targets in a ball are not a finite slice. (2)–(3) For fixed $O$, $f(O')=d(O,O')$ is continuous $\mathrm{Obs}\to\mathbb{R}$. Theorem 18 on a nonempty connected open: one class or a continuum of values. A single value-class (a sphere, or $\{f=0\}$) in an open that is not a singleton is a continuum, not a nonempty finite typicality set of delayed forks. A generation $g:V\to\mathbb{N}$ is a discrete rank; a continuous scale is not. $\square$

**Not claimed.** No metric on $\mathrm{Obs}$ exists. Theorem 16 already gives a Hausdorff topology; a compatible metric is extra packaging. The empty set and a singleton $\{O_{\mathrm{Mink}}\}$ are finite; they are trivial and are not a typicality set of delayed forks.

**As a clock.** $d(O,O')$ is not hitchhiker $\tau$ (that lives on $\gamma_O$). It is not proper-time-in-some-$W$ (that is $E$-smuggling when used off the curvelet). A continuous scale does not rank type-(ii) edges.

Locally finite one-step out-neighborhoods of a law of $R$ remain finite slices and remain extra (Theorem 19; Theorem 22 as restated on PR #26). Distance does not supply that law.

---

## 2. Report line

- **Proved.** Theorem 24: Fermi-slice distance is a continuous scale. Balls, spheres, and sublevels fail as finite slices and as a generation. Rounding is a grain.
- **Not claimed.** No metric exists.
- **Killed.** Adopting a metric scale as lock-side clock or slice.
- **Open.** The law of $R$; a discrete slice, if any; whether to abandon type (ii).

---

## References

Strayhorn, D. Observer space as a space. `papers/obs-as-a-space.md`.

Strayhorn, D. Neighborhoods are not a countable $N$. `papers/neighborhood-uncountable.md`.

Strayhorn, D. Grain is not a readout of continuous invariants. `papers/grain-not-from-invariants.md`.
