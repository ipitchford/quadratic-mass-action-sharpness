# Assurance and limits

Release status: **unrefereed publication candidate**. The package presents a complete constructive mathematical argument, accompanied by internal exact checks. Publication status is separate from mathematical status; this document does not assert journal acceptance, an authenticated external peer review, or an official research-assessment rating.

## Mathematical scope

For every integer n≥2, the displayed quadratic mass-action network has n species, n+2 reactions, rank n, and exactly n+1 distinct positive equilibria, all with nonsingular Jacobian. “Quadratic” concerns the source complexes; products are unrestricted nonnegative integer complexes. In particular, the requested three-species case is affirmative.

The earlier extremal polynomial family is due to Phillipson and Rojas. The contribution claimed here is its explicitly admissible chemical realization and the resulting sharpness conclusion, together with the compact examples. The literature search is bounded and does not certify exhaustive historical priority.

The inflow-free example has maximum product molecularity ten and the exact one-rate interval 1568<K<117649/75. The reciprocal N=7, K=145 example has two locally asymptotically stable equilibria and two hyperbolic saddles with one unstable direction. These statements do not supply a global phase portrait, a general robustness-volume calculation or a molecularity optimum.

## Evidence and version boundaries

- The PDF and TeX are the authoritative manuscript representations. The README provides an accessible overview; the defective earlier Markdown conversion is not authoritative.
- The analytic proof establishes positive converse reconstruction, strict alternating signs, exhaustiveness, simplicity and nonsingularity of the original Jacobian. Finite-dimensional program runs corroborate this proof.
- The distributed verifier checks exact identities and deliberately corrupted controls. Normal and optimized runs must agree. Consult the included receipts for the actual count, dimensions, runtime versions, hashes and outcomes of each executed run.
- The earlier v1 verifier reported 472 checks. Its historical audit receipts cannot certify later manuscript or code bytes. Current replay evidence and final archive verification must be read with their recorded hashes.
- Internal agent derivations and manuscript audits are supporting checks, not organizationally independent external peer review. The [proof index](supplement/PROOF_INDEX.md) identifies historical versions and superseded rate choices.
- A supplied referee-style assessment reports additional independent checking. It is user-provided AI/referee-style review material; its author identity and reported execution provenance have not been independently authenticated here. The assessment is not journal acceptance or an official REF decision. Its recommendations and disposition are recorded in [REVIEW_RESPONSE.md](REVIEW_RESPONSE.md).
- Original v1 archive bytes are retained unchanged. The revised candidate is a separate artifact. The included payload receipt and the external final-archive sidecar serve different purposes; see [REPLAY_RECEIPT.md](REPLAY_RECEIPT.md).

Both internal verification implementations and the supplied review's reported independent implementation use SymPy; no computer-algebra-engine independence or proof-assistant formalization is claimed. Source PDFs were inspected as described in the citation audit, but no checksum-verified archive of every external source is claimed.

No global product-molecularity lower bound, four stable attractors, conservativity, thermodynamic detailed balance, experimental chemistry, exhaustive historical priority, or public publication is inferred from these results. The n=1 source caveat is documented in [PRIOR_ART.md](PRIOR_ART.md) and is not needed for the stated n≥2 theorem.
