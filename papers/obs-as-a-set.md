# $\mathrm{Obs}$ as a set

David Strayhorn

Take the locked gauge *principle* as far as a definition of $\mathrm{Obs}$ as a set. Do not adopt an abstract $\mathrm{Diff}$/frame quotient of all metrics. Do not treat raw coordinate jets as settled. Do not close gauge by fiat. Do not put a measure on the set. Do not write $\Phi$. Do not adopt the remaining motion revision.

Companions: `papers/analytic-patch-from-jet.md`, `papers/ensemble-labels.md`, `papers/cheat-sheet.md`.

**Status.** The principle plus Theorems A–B determine $\mathrm{Obs}$ as a *set of lumps*: germ-equivalence classes of pointed simply-connected real-analytic Lorentzian patches with a future unit $u$ (Theorem 10). That is not raw jet equality, not $\mathrm{Met}(M)/\mathrm{Diff}(M)$, and not $E(O)$. It does not give $\mathrm{Obs}$ a topology or a manifold structure. Gauge as a home for $\mathrm{Obs}$ *as a space* stays open.

---

## 0. The locked principle

The object is the physical lump: the jet/patch pair $O=(j_\infty,u)\equiv P(O)$. Two presentations of the same lump are the same observer. A diffeomorphism that *moves* the lump is a different observer.

Gauge was left open as neither raw jet equality nor a $\mathrm{Diff}$/frame quotient of spacetime metrics. This note does not pick one of those by fiat. It asks what set $\sim$ and “typicality of many $O$” can even range over, given the principle and Theorems A–B.

---

## 1. Presentations, not observers

**Definition 5 (presentation).** A *presentation* of a lump is either

1. a coordinate infinite jet: $p\in\mathbb{R}^4$, a real-analytic Lorentzian jet $j_\infty$ at $p$, and a future unit timelike $u$ at $p$ (the data of Theorem A, §1), or
2. a pointed simply-connected real-analytic Lorentzian patch $(U,g,p,u)$ realizing such a jet.

Raw coordinate jets are presentations. They are not settled as the points of $\mathrm{Obs}$: a change of coordinates about the same $p$ with the same $u$ is two names for one lump.

---

## 2. Lump equivalence (already in Theorem A)

Theorem A, §2, of `papers/analytic-patch-from-jet.md` already names when two patches are the same lump. Repeat it as a relation on presentations, and give it a symbol so $\sim$ (the individuation cut on *curves*) is not overloaded.

**Definition 6 (lump equivalence).** Write $(U,g,p,u)\;\sim_L\;(U',g',p',u')$ if there exist connected open neighbourhoods $V\ni p$ and $V'\ni p'$ and a real-analytic diffeomorphism $\varphi:V\to V'$ with

$$
\varphi(p)=p',\qquad
d\varphi_p(u)=u',\qquad
\varphi^*g'=g\ \text{on }V.
$$

On coordinate jets: $j_\infty\sim_L j'_\infty$ if the realizing balls of Theorem A are $\sim_L$-equivalent. This is the germ equivalence of Theorem A. It is an equivalence relation. It is a presentation of the same lump. It is not a silent $\mathrm{Diff}$/frame quotient replacing the object, and it is not a topology label of an ensemble member.

The diffeomorphism $\varphi$ is required to send the marked point to the marked point and the marked $u$ to the marked $u'$. A diffeomorphism that *moves* the lump — $\varphi(p)\ne p$ if written as a self-map of one chart, or, equivalently, that is not pointed — is not a witness of $\sim_L$. That is the principle, as a restriction on which maps are allowed to identify presentations.

---

## 3. Theorem 10. $\mathrm{Obs}$ as a set of lumps

**Theorem 10.** Let $\mathcal{P}$ be the set of coordinate presentations of Definition 5(1) with $p=0\in\mathbb{R}^4$ (jets of real-analytic Lorentzian metrics at the origin, plus future unit $u$). Let $\mathrm{Obs}:=\mathcal{P}/{\sim_L}$. Then:

1. *($\mathrm{Obs}$ is a set.)* $\mathcal{P}$ is a set: convergent Lorentzian power series at $0$ in $\mathbb{R}^4$, plus a vector $u$ in the open hyperboloid of the $0$-jet. Analytic diffeomorphism-germs of $(\mathbb{R}^4,0)$ are likewise a set (convergent power series of four coordinate functions). The quotient of a set by a set-sized equivalence relation is a set.
2. *(Canonical bijections of models.)* The following are in canonical bijection, by Theorems A–B:
   - $\mathcal{P}/{\sim_L}$;
   - germ-equivalence classes of pointed simply-connected real-analytic Lorentzian patches (Theorem A uniqueness);
   - isomorphism classes of maximal simply-connected patches $P(O)$ (Theorem B uniqueness).
3. *(Not raw jets.)* The quotient map $\mathcal{P}\to\mathrm{Obs}$ is not injective. Coordinate change about $0$ preserving $u$ identifies presentations and does not identify observers.
4. *(Not $\mathrm{Met}/\mathrm{Diff}$.)* $\mathrm{Obs}$ is not $\mathrm{Met}(M)/\mathrm{Diff}(M)$ for a fixed $4$-manifold $M$, nor a frame quotient of all metrics. Those quotient by maps that need not fix a marked $(p,u)$. They forget the observer. Unpointed geometries are coarser than lumps.
5. *(Not $E(O)$.)* See §4.

**Proof of (1).** A real-analytic jet at $0$ is a power series of a symmetric $2$-tensor with positive radius of convergence and Lorentzian $0$-jet (locked object; Theorem A, §1). The set of such series is a subset of the Fréchet space of formal series, hence a set. $\square$

**Proof of (2).** Theorem A sends a coordinate jet to a germ-unique realizing ball, and sends $\sim_L$ to germ equivalence. Theorem B sends that germ to a unique-up-to-unique-isomorphism maximal simply-connected patch. The three maps are inverse on classes. $\square$

**Proof of (3).** If $\varphi$ is an analytic diffeomorphism-germ of $(\mathbb{R}^4,0)$ with $d\varphi_0(u)=u$ and $j_\infty(\varphi^*g')=j_\infty(g)$, then the two coordinate jets are $\sim_L$-equivalent and need not be equal as tensors in the original coordinates. $\square$

**Proof of (4).** $\mathrm{Diff}(M)$ contains maps with $\varphi(p)\ne p$. Those move the lump. The principle excludes them from $\sim_L$. Dropping $(p,u)$ entirely is a further coarsening. $\square$

So $\sim$ (individuation of curves) ranges over maps $I\to\mathrm{Obs}$ with this $\mathrm{Obs}$. Typicality of many $O$ would range over this same set. Neither fact writes a measure.

---

## 4. Distinguish from $E(O)$

Definition 2 of `papers/ensemble-labels.md`: $E(O)$ is equivalence classes of pairs $(W,\iota)$, $\iota$ a pointed analytic occurrence of the germ $O$ in a spacetime $W$, two pairs equivalent when a pointed analytic isometry $W\to W'$ carries $\iota$ to $\iota'$.

|  | $\mathrm{Obs}$ | $E(O)$ |
|---|---|---|
| An element is | a lump: a $\sim_L$-class of presentations of $(P,p,u)$ | a pointed occurrence of a *given* lump in some $W$ |
| The quotienting maps | pointed germ isometries of the *patch* (fix $(p,u)$) | pointed isometries of the *ambient* $W$, carrying the occurrence |
| Extra topologies | not extra points | the whole point of the label |
| Same Minkowski germ at two points of one $W$ | one point of $\mathrm{Obs}$ (the jets are $\sim_L$) | two occurrences if no pointed isometry of $W$ carries one to the other; or one class if it does |

Close, and not the same. $E(O)$ sits *over* a point of $\mathrm{Obs}$. Its members are not extra observers. Folding $E$ into $\sim$ remains forbidden.

Homogeneous example, named so it is not a vibe: the germ of Minkowski space at the origin with $u=\partial_t$, and the germ at $(1,0,0,0)$ with the parallel $u$, are $\sim_L$-equivalent (translation is a pointed isometry of the patches after recentring). They are one point of $\mathrm{Obs}$. They may be two occurrences in a single $W$ that is Minkowski. That is $E$, not a second lump.

A diffeomorphism of Minkowski that *moves* the basepoint is not a $\sim_L$-witness in a *fixed* chart of presentations at $0$. Once both germs are written as presentations at $0$, translation has already been used as a change of origin, and $\sim_L$ then sees one lump. The principle’s “moves the lump” clause is the exclusion of unpointed $\mathrm{Diff}(M)$ at the stage of presentations; it is not a requirement that isometric homogeneous germs be distinct points of $\mathrm{Obs}$. Distinctness of hitchhikers at different places is a distinction of occurrences and of paths, not of lumps.

---

## 5. What the principle does not identify

- A topology, smooth structure, or analytic structure on $\mathrm{Obs}$. Theorem 3 still does not claim $\mathrm{Obs}$ is an analytic manifold. Curves in $\mathrm{Obs}$ are defined because the *points* are; their analyticity is in the inverse-limit of jets (Theorem 3), not in a manifold atlas on $\mathrm{Obs}$.
- A home for $\mathrm{Obs}$ as a named space (Gielen–Wise $7$-manifold, a jet bundle of a fixed $W$, a frame bundle). That identification would close gauge as a *space*. It is not done.
- A canonical set of representatives in $\mathcal{P}$ (a transversal). Classes are unique up to unique bijection of models; a section of $\mathcal{P}\to\mathrm{Obs}$ is not unique. That is leftover presentation gauge, not a second observer.
- A measure. Typicality of many $O$ still needs a measure on this set, and this note does not write one. Gauge as a space being open is one reason a measure written now would be a measure on a set that is identified only as a set.

**Obstruction (precise).** The principle plus Theorems A–B uniquely determine $\mathrm{Obs}$ as a set of lumps, up to canonical bijection of the three models in Theorem 10(2). They do not uniquely determine $\mathrm{Obs}$ as a space, nor a measure, nor a preferred presentation of each class. Stopping there is the principle taken as far as it goes. Going further is a new hypothesis.

---

## 6. Open

- Gauge as a home for $\mathrm{Obs}$ as a space.
- A measure on $\mathrm{Obs}$.
- $\Phi$; the remaining motion revision, still not adopted.
- Countability of $E(O)$, unchanged.

---

## 7. Report line

- **Proved.** Theorem 10: $\mathrm{Obs}=\mathcal{P}/{\sim_L}$ is a set of lumps; three models are canonically bijective (raw jets at $0$, germ classes, maximal $P(O)$ classes). $\sim_L$ is the germ equivalence of Theorem A, pointed at $(p,u)$.
- **Killed.** Treating raw coordinate jets as the points of $\mathrm{Obs}$. Treating $\mathrm{Met}(M)/\mathrm{Diff}(M)$ (or a frame quotient of all metrics) as $\mathrm{Obs}$. Collapsing $\mathrm{Obs}$ into $E(O)$. Closing gauge as a space by fiat.
- **Open.** $\mathrm{Obs}$ as a space; a measure; $\Phi$.
- **Not done.** A measure; $\Phi$; Born; the remaining motion revision.

---

## References

Strayhorn, D. Theorem: the simply-connected analytic patch from an infinite jet. `papers/analytic-patch-from-jet.md`.

Strayhorn, D. The ensemble $E(O)$ as a labeled object. `papers/ensemble-labels.md`.
