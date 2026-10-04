# Agent-readable research index

Release status: **unrefereed publication candidate**. This package answers the three-species, five-reaction quadratic mass-action existence question and constructs n+1 positive nondegenerate equilibria with n species and n+2 reactions for every n≥2. Products are unrestricted. This index is navigation, not a proof certificate.

## Current authoritative material

- [README](README.md): concise accessible explanation, explicit example and replay commands.
- [Manuscript PDF](paper.pdf) and [TeX source](paper.tex): authoritative manuscript representations. Do not substitute the defective earlier Markdown conversion.
- [Claims](CLAIMS.json), [status](STATUS.md) and [assurance](ASSURANCE.md): mathematical scope and publication, checking and review boundaries.
- [Proof index](supplement/PROOF_INDEX.md): final proofs versus alternative arguments, historical audits and superseded rates.
- [Prior-art audit](PRIOR_ART.md) and [citation audit](CITATION_AUDIT.md): inspected source versions, attribution and search limits.
- [Phillipson–Rojas realization](supplement/phillipson-rojas-bridge.md), [general proof](supplement/general-proof.md), and [inflow-free proof](supplement/inflow-free-proof.md): supporting exact derivations.
- [Examples](examples.json) and [verifier](verify.py): exact inputs and checks; run with `--negative-controls` in ordinary and optimized modes.
- [Replay documentation](REPLAY_RECEIPT.md), [normal receipt](receipts/normal.json), and [optimized receipt](receipts/optimized.json): actual execution evidence; consult their hashes and version fields.
- [Support classifier](classify_supports.py) and [classification output](receipts/source-supports.json): finite source-support enumeration, not a classification of reaction networks.
- [Review response](REVIEW_RESPONSE.md): supplied assessment provenance, action-by-action disposition and any remaining release checks.
- [Provenance](PROVENANCE.md), [licenses](LICENSES.md) and [manifest](MANIFEST.sha256): identity, reuse and exact-byte boundaries.

## Historical supporting records

[The manuscript audit](review/manuscript-audit.md), [independent derivations](review/independent-derivations.md), [analytic audit](review/analytic-audit.md), and [earlier audit replay](receipts/internal-audit-replay.json) are retained internal history. Their version-specific PASS statements and hashes do not certify subsequent revisions. The proof index explains which portions remain useful as alternative derivations.

The finite program dimensions do not computationally prove the universal theorem. The manuscript supplies that proof. Invertible equation transformations preserve the equilibrium set and nonsingularity, not dynamics. The supplied referee-style report has unverified reviewer identity and is not journal acceptance or an official research-assessment decision. No public release or DOI outcome is established by this index.
