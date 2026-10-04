> Historical internal audit. Workspace paths mentioned below describe the original run and are not distributed artifacts. The current proof is in `paper.tex`; historical verifier evidence is retained in `receipts/internal-audit-replay.json`. Revised evidence is indexed by `REPLAY_RECEIPT.md`.

# Manuscript and Phillipson--Rojas realization audit

Date: 2026-10-04. Auditor: proof_audit.

## Current final audit: PASS

The final attribution revision was read directly, limited to the changed abstract, introduction, direct-realization section, and bibliography. The new text explicitly credits the Phillipson--Rojas polynomial family, states the exact relationship of the uniform chain to it, distinguishes chemical realization from a new abstract fewnomial construction, and identifies the inspected source version. The earlier attribution correction is resolved.

The direct-realization section is mathematically correct: the rates, constants, reversal, positive equation scalings, and invertible row-difference transformation all agree with the independent derivation below. The n=2 edge case is valid with an empty interior-transfer index range. No mathematical or attribution correction remains from this audit. No manuscript edits were made by this auditor.

Exact versions reviewed and freshly checked:

| File | SHA-256 |
|---|---|
| outputs/quadratic-five-reaction/paper.tex | `add7201cc251fdf13a7c6e2acde04d510c42301961fee4c4fe91fd25e0eef798` |
| outputs/quadratic-five-reaction/verify.py | `f58b600a22fd065fa7e861e6f53d23de64ed11156926b27a730e2bfbea01da88` |
| outputs/quadratic-five-reaction/examples.json | `c36638c8f13e18934095a1f04cb656f5df1e76c696e2f29b08b02ff8cb832d7c` |

The verifier source was reviewed and a new local run of `python3 outputs/quadratic-five-reaction/verify.py --negative-controls` completed successfully. Receipt: `work/proof-audit-final-verifier.json`. Result: `EXACT_CHECKS_PASS`, 472 checks, Python 3.14.7, SymPy 1.14.0. Both three-species examples passed, dimensions n=2 through n=12 passed, and all five specified negative controls were rejected.

Verifier scope is supplementary, as the manuscript states. It checks the supplied exact identities, ranks, brackets, polynomial root counts, and finite-dimensional formulas; the manuscript supplies positivity, exhaustiveness, and the uniform all-n argument. In particular, the exact displayed reconstruction maps are positive on their domains, and their determinant prefactors are nonzero there, as checked analytically. This is an internal independent audit, not external peer review, exhaustive priority clearance, or publication approval.

## Historical initial review (superseded attribution status)

Initial audited manuscript: outputs/quadratic-five-reaction/paper.tex, SHA-256
`2daab461e1b0461a5246ec5739c45a8d017848cba2bd28e79d9a172fce912ef5`.
No manuscript edits were made by this auditor.

## Mathematical verification

The current manuscript's all-dimensional proof passes, including the uniform correction bound, the n+1 finite isolating intervals, polynomial degree and simplicity, and the augmented-Jacobian nondegeneracy proof. In particular its assertion f_i=E_(i+1)-E_i is valid even for i=n, and its block Jacobian has the displayed zero final column and bottom-right entry -1.

The reciprocal-quartic proof passes. Its determinant formula -P'(t)/(Kt(t+N)) agrees with the independent determinant formula in proof-audit.md.

The inflow-free example passes. Its positive-kernel parameterization is exact and exhaustive, its four rational sign brackets are correct, and its determinant equals (5-t)Q'(t)/(6274(t+1)(7t+1)^2) at every Q-root. The determinant coefficient is strictly positive throughout the feasible t interval. The manuscript no longer contains the faulty elimination argument identified by the root agent.

## Material attribution correction

The manuscript version audited here does not cite Phillipson--Rojas and must add that close prior art. Its underlying all-dimensional polynomial family is equivalent to theirs after positive diagonal coordinate scaling, coordinate reversal, and invertible linear row operations. Attribution merely to scalar-reduction or geometric-separation methods understates the relationship. The chemically admissible integer-product realization can still be presented as the task-specific contribution, with bounded rather than exhaustive novelty claims.

Primary source read directly: Phillipson--Rojas, *Fewnomial Systems with Many Roots, and an Adelic Tau Conjecture*, arXiv:1011.4128v5, Theorem 1.6:
https://arxiv.org/html/1011.4128v5

The theorem explicitly treats every n≥2, gives the stated quadratic chain, and permits epsilon=1/4 with exactly n+1 positive nondegenerate roots.

## Exact direct mass-action realization of the source family

Write original source variables as z_1,...,z_n and reverse them by y_i=z_(n+1-i). Put r=4, epsilon=1/r. For i<n set

    d_i=r^(2n-2i-1),

and d_n=1/r. Define fluxes

    w_1=r^(2n-3)y_1,
    w_i=r^(2n-2i-1)y_(i-1)y_i  (2≤i≤n-1),
    w_n=y_(n-1)y_n,

and H_i=w_i-d_i-y_n^2.

For i<n, H_i is r^(2n-2i-1) times the corresponding reversed Phillipson--Rojas equation. H_n is exactly their first equation. Thus H is obtained from their polynomial map by an invertible row scaling and reversal.

Set B_i=15*16^(n-i-1) for i<n and B_n=1. The reactions

    0 -> sum_i B_i Y_i                    rate 1/4,
    Y_1 -> 0                             rate 4^(2n-3),
    Y_i+Y_(i+1) -> 2Y_i (1≤i≤n-2)        rate 4^(2n-2i-3),
    Y_(n-1)+Y_n -> 2Y_(n-1)              rate 1,
    2Y_n -> 3Y_n                         rate 1

have vector field

    f_i=H_(i+1)-H_i (i<n),   f_n=-H_n,

because B_i/4=d_i-d_(i+1) for i<n and B_n/4=d_n. This row operation has determinant (-1)^n, hence is invertible. The coordinate reversal is also invertible. Positive equilibria and Jacobian nonsingularity transfer exactly from the source theorem. All products are nonnegative integer complexes and all reactants are quadratic; the outflow and chain transfer vectors already give rank n. For n=2 the first pair range is empty and the final pair remains a single reaction.

For n=3 the network is precisely

    0 -> 240X+15Y+Z    rate 1/4,
    X -> 0            rate 64,
    X+Y -> 2X         rate 4,
    Y+Z -> 2Y         rate 1,
    2Z -> 3Z          rate 1.

Its vector field is (60-64X+4XY, 15/4-4XY+YZ, 1/4-YZ+Z^2). The three reversed and scaled source equations are H_1=64X-64-Z^2, H_2=4XY-4-Z^2, H_3=YZ-1/4-Z^2, and the displayed row differences give the field exactly.

## Relationship of the manuscript R=25 family itself to the source family

The same direct-realization algebra works for an arbitrary positive r, with epsilon=1/r. Now take r=5. In reversed source coordinates y, put x_i=r^(e_i)y_i, where for i<n

    e_i=2n-i+1 for odd i,  e_i=-i for even i,

and

    e_n=n+2 for odd n,  e_n=1-n for even n.

Then the manuscript's constants satisfy s_i=r^3 d_i, all its nonterminal fluxes equal r^3 times the source-realization fluxes, and its terminal flux satisfies k_n x_n^2=r^3 y_n^2. Thus its entire polynomial vector field is r^3 times the source realization after this positive diagonal substitution. This proves exact family equivalence at epsilon=1/5. The manuscript's uniform estimates supply a self-contained proof at that value; the source's explicitly stated special value epsilon=1/4 is enough for the separate direct realization above.
