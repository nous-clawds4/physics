# Geometry quick verdict: creative batch 10 (#360) — do not merge

**Read at:** #360 head `32aacd9` (`notes/creative/batch-10.md`), main `e41412b`.

**Record type:** rough review. Applies nothing. Neutral on David's open calls. Structure only: no probabilities, no counting (David, 4:03 PM ET). Geons are not ruled out (David, 4:06 PM ET). This review only states the conditions under which they fit the current host class. All arguments are sketches. **(U)** marks a claim from memory that was not checked.

**Verdicts.**
- **(1) L33, Hadley 4-geon.** Ill-posed as stated, because "received signal" fails across a time-orientation flip. It also conflicts with #352: deck elements must preserve time orientation and must not create CTCs. It can be made well-posed only by changing the host class.
- **(2) L34, position as gluing.** Confirmed: under the lock, the uncertain datum is exactly the pointed Γ. A "mouth location" is a choice of fundamental domain, not geometry, so the set measures $\pi_1$ and not an external particle.
- **(3) L35, radar.** Consistent with #346, and it adds nothing to *when* the first split happens. Radar cannot split hosts while the observer is inside $D^+(S)$. The splits form a continuum unless there is a grain. Reflection needs matter or a wave effect.
- **Not flagged** for a full note.

## (1) L33: Hadley 4-geon

- **Source.** Hadley, "The logic of quantum mechanics derived from classical general relativity", *Found. Phys. Lett.* 10, 43 (1997) (U); the batch also leaves it unchecked. As I recall (U), the 4-geons are not time-orientable and contain closed timelike curves. Literature should confirm both points before anything relies on them.
- **Observer state.** The state is fine locally. $u$ is a future unit timelike vector, which needs a time orientation only near $\gamma$. The worldline can sit in a time-orientable open set, so the germ and $u$ are defined there.
- **The record is the problem.** A beacon signal that goes through an orientation-reversing loop comes back **past-directed** relative to the observer's local orientation. A past-directed null geodesic ending at $\gamma(s)$ is, in the local orientation, a signal *leaving* the observer into its future. So "received at $s$" is undefined for exactly the returns the batch wants as the geon's "character". That is an ill-posed term (well-posedness principle). Note also that the flip is in time orientation. The batch's "reversed handedness" would require space-orientation reversal, which is a different property.
- **Conflict with #352.** #352 requires deck elements to preserve time orientation and forbids any $\gamma\ne1$ with $\gamma x\in I^+(x)$. A non-time-orientable quotient breaks the first condition. If the geon has CTCs, it breaks the second. Under the current conditions such hosts are outside the compatible class.
- **#320, inextendible hosts.** Regions with CTCs are typically bounded by a (compactly generated) chronology or Cauchy horizon. Analytic examples exist (Misner space (U)), so analyticity and CTCs can coexist. But extensions across such horizons are typically non-unique (#352 (1); Chruściel–Isenberg 1993, verified in #332). Inextendibility can hold while still leaving the host ambiguous beyond the horizon. Whether a Hadley 4-geon spacetime is analytic and inextendible is (U).
- **Ways to make it well-posed.** Any of these would do. None is recommended; the choice is David's.
  - (a) Work in the time-orientable double cover, where "received" is defined. That changes the host, and the geon becomes a different object.
  - (b) Keep only returns that stay in the time-orientable region, which drops the geon's "character".
  - (c) Drop #352's two conditions for geon hosts, which reopens CTC consistency (EKT-type).

## (2) L34: position as gluing

- **Confirmed, with the #352 caveat.** Continuation from $P(O)$ fixes a universal cover $\tilde M$, possibly one of several maximal ones. Positions of features in $\tilde M$ relative to $\tilde p$ are fixed. A given Γ fixes the pointed quotient $(\tilde M/\Gamma,[\tilde p])$. The uncertainty is therefore exactly the pointed Γ, which is the #355 count object.
- **Non-unique extensions** can also change *which* features exist beyond a Cauchy horizon. That is a second uncertain datum, which the batch does not list.
- **"Mouth" is not geometry in an analytic quotient.** $\tilde M$ has no mouths. A handle is purely Γ, and a "mouth pair" is just the boundary of a chosen fundamental domain. What is geometric is the set of deck translates $g\tilde p$. So "partner-mouth position" means "displacement of a deck element". Set 2 is L28's self-echo renamed: it measures $\pi_1$ and its embedding, not the position of an external particle. The batch's own structural observation says the same, and that is accurate.
- **"Exact isometry between mouth neighbourhoods."** This is automatic for quotients ($\Gamma\subset\mathrm{Isom}(\tilde M)$). The real cost is L27's: the cover itself has to be symmetric.

## (3) L35: radar in a smooth host

- **Radar sees only the past cone.** The record at $\tau$ depends only on the host geometry in $J^-(\gamma(\tau))$, together with the beacon test field, which is determined there.
- **No split while inside $D^+(S)$.** For $q\in D^+(S)$, $J^-(q)\cap J^+(S)\subset D^+(S)$ (standard; Hawking–Ellis §6.5 (U)). Hosts that agree on $D(S)$ therefore give identical radar records as long as $\gamma$ stays in $D^+(S)$. Records can first differ only after $\gamma$ crosses $H^+(S)$. That is exactly #346's first-divergence locus.
- **What radar adds.** It changes *what* is recorded after the crossing, not *when* hosts first differ. #346's caveat carries over unchanged: the agreement region's boundary is null only given unique continuation across timelike surfaces, which is unverified for smooth vacuum.
- **Discrete or continuum?** A continuum. Smooth hosts form a continuum (#346 (1)), and the record entries are real-valued. A resolution would be a grain (#355 (e)). The batch says positions "can be a continuum", which is accurate. Counting is parked.
- **Reflection.** In geometric optics a ray does not reflect off curvature. It returns only through lensing round a loop or through a caustic. Genuine back-scattering is a wave effect (#339 hazard) or needs matter or a junction. The batch flags this too.

**Citations.** Hadley 1997 (U); Misner space (U); Hawking–Ellis §6.5 (U); Chruściel–Isenberg 1993 (V, #332). In-repo: #320, #324, #346, #352, #355.
