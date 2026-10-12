# Geometry quick verdict: creative batch 02 (#337) — do not merge

**Read at:** #337 head `fed0225` (`notes/creative/batch-02.md`, stacked on #333), main `e41412b`, #336 (`notes/sheets-seam-hitting.md`). **Record type:** rough review; applies nothing; neutral on David's open calls. **Goal (batch-02 framing):** branching of one traveller's *motion*, discrete, with a count fixed by the host, no CTCs, no smuggled measure; and specifically to remove #336 (f)'s costs C1–C3.

**Ranking.** Set 1 > Set 2 > Set 3, as the Creative Lead ranked them. **None is flagged for a full note.** In all three, what branches is which host (or which microscopic arrangement) we are in, not the motion: the fine host fixes a unique curvelet (`papers/geodesic-lifts.md` Prop 3.2/Thm 3), and continuation along one path has no monodromy.

## Answer to Set 1's question to Geometry

*Question:* with seams at spacing ℓ, does a tube with $r_0\gg\ell$ meet seams at a rate that is a function of $r_0/\ell$ alone, and is any quantity finite as $r_0/\ell\to\infty$?

*Answer:* **No branching quantity has a finite limit; the set dies by its own test.** Take timelike seams (string worldsheets) with spatial line density $1/\ell^2$, and a tube moving at relative speed $v$ (rough count, not a theorem).
- The number of seams inside the tube at one instant grows like $(r_0/\ell)^2$. The number of new seam encounters per tube-crossing time $r_0/v$ also grows like $(r_0/\ell)^2$. Per unit proper time the rate is about $v\,r_0/\ell^2$, which depends on $r_0$ and ℓ separately. All of these diverge.
- The only finite quantities are densities per unit cross-section or per unit volume. Those equal the host's own $1/\ell^2$ and carry no branching information.
- The net sheet data around the tube boundary is a product of about $(r_0/\ell)^2$ monodromy elements.
  - For a periodic lattice, the product is a deterministic function of $r_0$ that oscillates and has no limit.
  - For $n$-sheeted covers it is a word in a finite permutation group. It tends to the uniform distribution on the subgroup generated, but **only if the seam arrangement is random**. That randomness is a measure on arrangements, so it is smuggled (#336 (a) measure flag; TT4).
  - For conical deficits, the deficits add. Once the total exceeds 2π the exterior is no longer a cone (Gott 1985 bounds the string mass per length), so the coarse description itself fails.

## Set 1: The tube is the coarse-graining scale

**Rigorous?** Not yet. "The coarse-grained state at the scale where the microscopic topology averages out" needs a definition, and the candidate in TT1 ("smallest radius above which the region is simply connected") is never satisfied when seams or handles have spacing ℓ and $r_0\gg\ell$: a larger tube encloses more loops, not fewer. **Where it breaks.** Besides the missing limit above, a coarse-grained state that fails to determine its successor is **epistemic branching**: the fine host fixes one curvelet (Prop 3.2), and the coarse state's successors are its compatible fine hosts. That is the #336 conclusion again, an ensemble fact and not branching of motion. Replacing the germ by a tube (C2) also breaks the germ-based observer space, the gauge quotient (#324: jets modulo diffeomorphism germs fixing $p$; a tube has no base point) and the inextendibility condition stated for germs' hosts (#320). **Gains.** It would answer C1 if a limit existed; none does. C3 is untouched.

## Set 2: Handles inside the tube

**Rigorous?** The one geometric reading offered, holonomy of the tube's frame around a non-contractible loop, is well defined, but it is a single group element fixed by the host. A consistency condition on it has exactly one solution in free fall, which is #334's objection to batch-01 Set 3 carried over. **Where it breaks.** Several solutions appear only for fields living on the tube with twisted boundary conditions, i.e. sectors labelled by representations of $\pi_1$. That is Schulman 1968 / Laidlaw–DeWitt 1971 (#332 R4), borrowed quantum structure, so TT4 fails if it is used. It also inherits Set 1's undefined tube and Set 1's divergence: the number of enclosed handles grows like $(r_0/\ell)^3$ in a 3-d section for handles at spacing ℓ (rough count). **Gains.** A discrete count fixed by $\pi_1$, but of sectors over the host, not of motions.

## Set 3: Where the observer's patch runs out

**Rigorous?** Yes, but as a fact about $M$. $P(O)$ is simply connected and abstract. Its developing map into $M$ along the curvelet fails to be injective exactly where deck transformations identify points. That gives an injectivity-radius-type scale, which is the deck group of $M$: the "which quotient is the real world" choice from the ant discussion. **Where it breaks.** Continuation along one path is unique (#331 §0; #336 setting), so nothing forks at that scale. The "ways of continuing the patch" are the different quotients, i.e. different hosts in $E(O)$. Under #324, germ-isometric copies are already identified. It is ensemble structure only, as the batch itself anticipated. **Gains.** Every traveller in a world with handles reaches the scale, so "hitting" is typical, but what is reached is a property of the host and not a branch point.

**Citations.** Gott, *Astrophys. J.* 288, 422 (1985) (checked against the abstract in #336); Schulman 1968 and Laidlaw–DeWitt 1971 as given in #332 R4. The counting estimates are rough and unproved.
