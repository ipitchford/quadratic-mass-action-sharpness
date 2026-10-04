# Proof and evidence index

The PDF and TeX manuscript are authoritative. This index distinguishes mathematical arguments from checking history; a PASS in a historical record applies only to its identified version.

## Current proof material

| File | Role and scope |
|---|---|
| [Manuscript PDF](../paper.pdf), [TeX](../paper.tex) | Complete theorem, realization, examples and promoted supplementary consequences. |
| [General proof](general-proof.md) | Uniform R=25 construction for n≥2; positive reconstruction, exact count and original-Jacobian nonsingularity. |
| [Phillipson–Rojas bridge](phillipson-rojas-bridge.md) | Direct realization at epsilon=1/4 with its own stated rates; this is an alternative exact realization, not the R=25 data set. Equilibrium equivalence does not imply dynamical equivalence. |
| [Inflow-free proof](inflow-free-proof.md) | Five-reaction example, converse reconstruction and exact interval 1568<K<117649/75 for fourth rate 1/K. |
| [Prior-art audit](../PRIOR_ART.md) | Attribution and bounded literature evidence, not a mathematical or exhaustive-priority certificate. |

The manuscript denotes the inflow-free inverse fourth rate by L; the supplement and supplied review call the same parameter K. It is independent of the reciprocal-family K.

The reciprocal N=7, K=145 example and its local bistability belong to the manuscript. The N=6, K=4801/48 choice is a smaller-inflow alternative within that family, not a proof of global molecularity minimality. The epsilon=1/4 bridge and the R=25 uniform family use distinct rate vectors; do not interchange their data.

## Alternative derivations and historical internal audits

| Record | How to use it |
|---|---|
| [Independent derivations, sections A and C–D](../review/independent-derivations.md) | Alternative exact arguments for the reciprocal family, local bistability, final fixed-base construction and second example. References to working-directory paths describe provenance rather than supplied files. |
| Independent derivations, section B | Historical dimension-dependent choice R=2^(4n+2), superseded by the manuscript's simpler R=25 choice. Valid alternative reasoning, not the final family definition. |
| [Analytic audit](../review/analytic-audit.md) | Historical reciprocal-family calculations and earlier dimension-dependent construction. The source caveat and old parameters are not the final theorem statement. |
| [Manuscript audit](../review/manuscript-audit.md) | Historical v1 audit. The initial request for better attribution was resolved in v1; later revisions require their own evidence. Its file hashes are historical, not hashes of the current revised manuscript. |
| [Internal audit replay](../receipts/internal-audit-replay.json) | Version-specific historical execution record. |
| TARGET.yaml intake status | Historical task specification; current release status is in STATUS.md. |
| Earlier Markdown manuscript conversion | Defective, non-authoritative historical conversion; intentionally excluded from current navigation. |

## Current computational and supplied-review evidence

[The verifier](../verify.py) checks exact identities and negative controls; [the classifier](../classify_supports.py) enumerates source supports only. [Replay documentation](../REPLAY_RECEIPT.md) explains included receipts and the external archive-binding sidecar. Computational counts and ranges apply to the executed versions identified by those receipts.

[The review response](../REVIEW_RESPONSE.md) records the user-provided referee-style assessment, whose reviewer identity and claimed execution provenance have not been authenticated here. This supplied assessment and the internal agent audits are not journal acceptance or official research assessment.
