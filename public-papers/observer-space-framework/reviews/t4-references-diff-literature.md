# Diff check of #312 (prior work and references in the curvelet-induced topology note) — Literature

**Verdict: HOLD (narrow).** One required string, M1: a verification mark that overstates what was read. The mark error is mine: it came from Literature's `refs.md`, which this PR carries faithfully. One recommended string, G1, for the Gielen–Wise sentence, and one optional string, H1, which adds Hohmann's title. Everything else checks.
**Heads read:** #312 head `4ec5f4e` (one commit), off `8bca97f`. Main is now `c2ff607`; #311 touched only the topology brief, so the base of this note is unchanged. v0.9.1 and v0.10 (merged in #307) read at `c2ff607`.
**Scope:** `notes/curvelet-induced-topology.md` only. Paper 1 and `versions/` are untouched.

## Checks

1. **One file.** The PR changes only `notes/curvelet-induced-topology.md`: 29 insertions and 1 changed line. ✓
2. **Placement sentences.**
   - All three match `refs.md` exactly: §1 "Prior work", §2 after "Shapes", and §6 after "Close variants".
   - The one exception is the declared §6 amendment, "§6's continuous-history variant" → "the continuous-history variant above". It is correct: the sentence now sits inside §6. ✓
3. **Entries.**
   - Entries 1–12, 14, 16 and 17 match `refs.md` character for character, with their marks.
   - 13 (Gielen–Wise) writes out v0.9.1's References entry in full, as `refs.md` asked ("use v0.9.1's existing entry"). It is identical to v0.9.1 l.611 and v0.10 l.614, plus "§3.1 (Reeb flow on observer space)". ✓
   - 15 (Bourbaki) is shortened to "Cited without a section; the location is [U]", matching the declared "e.g. Bourbaki, *General Topology*" in §2. ✓
   - Kurt and Antonelli are left out, as `refs.md` advised. The I-Z revised-edition caveat is kept. ✓
4. **Other changed lines.**
   - The header gains "prior work and references added at main `8bca97f`". This is undeclared but accurate.
   - The References preamble is new. It credits Literature and David's request (5:57 PM ET, relayed, not signed) and defines the three marks as `refs.md` does. ✓
   - Nothing else in the note changed: removing the four insertions and restoring the header leaves it byte-identical to `8bca97f`. ✓
5. **Words.** By `str.split`, 1,683 → 2,417, so +734, as stated. ✓
6. **Guardrails.** The diff adds none of the guardrail terms: no forbidden words, no probability-rule or amplitude-weight claims, and no interpretation-contest framing (checked by search against the base). ✓
7. **Citations in the body.**
   - Five list entries are not cited in the text: Zeeman 1964, the Agrawal–Sinha comment, Dugger, Fajstrup–Rosický and Hohmann.
   - That is acceptable for a "prior work" list. A one-line "further reading" note in the preamble would make it explicit. This is optional.

## M1 (required): entry 6's mark

For Papadopoulos and Papadopoulos 2019, Literature read the arXiv abstract (arXiv:1712.03270), not the paper, so the mark should be [V-meta]. The §6 use, "limit-curve theorems likewise fail", is what the abstract states.

- OLD: `6. [V-text] Papadopoulos, K., Papadopoulos, B. K.,`
- NEW: `6. [V-meta] Papadopoulos, K., Papadopoulos, B. K.,`

## G1 (recommended): the Gielen–Wise sentence in §1

**The firewall on record.** v0.10 §2 is byte-identical to v0.9.1 §2 (`versions/v0.10-changelog.md` §2c):
- FW4, a paragraph of §2, contains the sentence "It is not Stoica, not Gielen–Wise and not Larsson."
- FW15, in the "Does not claim" list, also names Gielen–Wise.

v0.9.1 §4 ("Vertex space") says "Here $u$ sits on a lump, and $V$ is not their 7-manifold". The §12 Gielen–Wise row says "Its points are 4-velocities, not analytic germs; $V$ is not their 7-manifold." The v0.10 text is identical. (The v0.9 changelog numbered the "not Gielen–Wise" sentence FW15. The current numbering is v0.10's.)

**Judgment: yes, it could read as an identification.** "Whose orbits are the jet-level counterpart of the inertial-observer orbits of Gielen and Wise" suggests $V$ is a jet-level version of their observer space. §4 and §12 refuse exactly that.

The mathematical link is real but narrower. For a given analytic spacetime, Thm 3's lift carries each inertial (Reeb-flow) orbit to a curvelet. But Gielen–Wise's space is built on a given spacetime, or abstractly as a Cartan geometry, and its points are 4-velocities.

"Leaf topology of a one-dimensional flow" is also an analogy: $V$ is not given as a manifold, so "formal analogue" is the accurate word.

- OLD: `On $V$ the curvelets do not cross, so the result is the leaf topology of a one-dimensional flow, whose orbits are the jet-level counterpart of the inertial-observer orbits of Gielen and Wise (2013, §3.1).`
- NEW: `On $V$ the curvelets do not cross, so the result is a formal analogue of the leaf topology of a one-dimensional flow. The nearest flow on record is the inertial-observer (Reeb) flow on Gielen and Wise's observer space (2013, §3.1), a different construction: its points are 4-velocities, not analytic germs, and $V$ is not their 7-manifold (§4, §12; §2: "It is not Stoica, not Gielen–Wise and not Larsson", FW4 in `versions/v0.10-changelog.md` §2c).`

This adds 38 words.

## H1 (optional): Hohmann's title

The title was checked against the arXiv:1304.5430 abstract page and the Crossref record for doi:10.1103/PhysRevD.87.124034. Both give "Extensions of Lorentzian spacetime geometry: From Finsler to Cartan and vice versa".

- OLD: `14. [V-meta] Hohmann, M., *Phys. Rev. D* 87, 124034 (2013)`
- NEW: `14. [V-meta] Hohmann, M., "Extensions of Lorentzian spacetime geometry: From Finsler to Cartan and vice versa", *Phys. Rev. D* 87, 124034 (2013)`

This adds 12 words.

Each OLD occurs exactly once at `4ec5f4e`, and all three strings apply cleanly together, for a total of +50 words. None adds a guardrail term.
