# Sharp positive-equilibrium counts in quadratic mass-action networks

**Problem 1 has a constructive affirmative answer.** A quadratic mass-action network with three species, five reactions and stoichiometric rank three can have exactly four distinct positive nondegenerate equilibria. The construction extends to every integer n≥2: n species and n+2 reactions can attain exactly n+1 positive equilibria, all nondegenerate.

This is a **unrefereed publication candidate**. “Quadratic” restricts reactant molecularity to at most two; products may be larger. The contribution is an explicit admissible mass-action realization of the established Phillipson–Rojas polynomial family and its sharpness consequence. It is not a claim to have discovered a new extremal fewnomial family.

The authoritative manuscript representations are [the PDF](paper.pdf) and [its editable LaTeX source](paper.tex). This README is a concise accessible overview, not a replacement proof. The earlier Markdown conversion is excluded from current manuscript navigation because it contains conversion defects.

## A compact explicit answer

Use these five reactions and positive rational rate constants:

| Reaction | Rate constant |
|---|---:|
| X → 0 | 1 |
| Y → 6X + 4Z | 1 |
| 2X → 6Y + 4Z | 1 |
| 2Z → 4Y | 2/3137 |
| Y + Z → 0 | 1 |

The equilibrium calculation reduces to

    Q(t) = -3137 t^4 + 9411 t^3 - 10183 t^2 + 4709 t - 784.

Its signs at 0, 1/2, 5/7, 1, 5 alternate −,+,−,+,−. The four intervening intervals therefore contain four distinct roots. Since Q has degree four, these are all its roots and they are simple. Each gives exactly one positive equilibrium:

    x = (5-t)/(2(7t+1)),
    y = (5-t)(t+1)/(2(7t+1)^2),
    z = 14/(t+1).

The stoichiometric rank is three. At a root, the Jacobian determinant is

    (5-t) Q'(t) / (6274(t+1)(7t+1)^2),

which is nonzero. The [inflow-free proof](supplement/inflow-free-proof.md) supplies the converse reconstruction. Replacing the fourth rate by 1/K gives exactly four positive nondegenerate equilibria when

    1568 < K < 117649/75.

Products have molecularity at most ten; no global minimum is claimed. A separate reciprocal example with N=7 and K=145 has two sinks and two saddles with one unstable direction, in alternating scalar-parameter order. That local bistability result does not establish a global phase portrait or four stable attractors.

## The all-dimensional realization

For every n≥2, take the inflow product coefficients a_i=24·25^(n−i) for i<n and a_n=25. Add X1→0, Xi+Xi+1→2Xi for i<n, and 2Xn→3Xn. All rates are one except the terminal rate 5^[(-1)^n(2n+1)]. The manuscript proves positivity, exhaustive reconstruction, exactly n+1 roots, and nonsingularity of the original equilibrium Jacobian.

Phillipson and Rojas supplied the underlying maximal-root polynomial chain. The [realization bridge](supplement/phillipson-rojas-bridge.md) gives its precise translation into admissible reactions; invertible equation operations preserve equilibria and Jacobian nonsingularity, not dynamics or stability. The [bounded prior-art audit](PRIOR_ART.md) records the attribution and search limits.

## Reproduce and inspect

With Python 3.10+ and SymPy 1.14.0, run from the extracted package directory:

```sh
python3 verify.py --negative-controls
python3 -O verify.py --negative-controls
python3 classify_supports.py
```

Successful verifier runs report `EXACT_CHECKS_PASS` and reject the deliberately corrupted cases. Check counts and exact input hashes belong to the version-specific JSON receipts, rather than to this overview. The finite dimensions checked by the programs corroborate the universal analytic proof; they do not replace it. Acceptance uses exact arithmetic, not floating-point tolerances.

[Replay documentation](REPLAY_RECEIPT.md) distinguishes the included payload receipt from the archive-binding sidecar distributed alongside the revised ZIP. [The proof index](supplement/PROOF_INDEX.md) separates current proofs, alternative arguments and historical audit records. See also [the review response](REVIEW_RESPONSE.md), [assurance](ASSURANCE.md), [claims](CLAIMS.json), [provenance](PROVENANCE.md), and [the agent-readable index](AI_INDEX.md).

The supplied referee-style assessment is recorded as user-provided review material whose author identity and claimed independent checks have not been authenticated. It is not journal acceptance or an official research assessment. Public release, DOI registration and canonical publication readback are separate steps.

## Candidate release identifiers

The planned repository is [quadratic-mass-action-sharpness](https://github.com/ipitchford/quadratic-mass-action-sharpness), with candidate tag `v1.0.0-candidate`. The version DOI [10.5281/zenodo.23146115](https://doi.org/10.5281/zenodo.23146115) is **reserved for this candidate**; the concept identifier is `10.5281/zenodo.23146114`. Reservation is not publication, and these identifiers do not by themselves establish public availability. Final upload and canonical readback are pending.

Planned release assets are `quadratic-mass-action-sharpness-v1.0.0-candidate.zip`, `archive-replay.json`, `paper.pdf`, and `SHA256SUMS`. The ZIP includes `receipts/payload-replay.json`; the external `archive-replay.json` binds the final ZIP hash without a circular self-hash.
