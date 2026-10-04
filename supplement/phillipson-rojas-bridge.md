# Exact chemical realization of the Phillipson–Rojas chain

Prepared 2026-10-04. This is a proof of the realization map; historical priority remains subject to the bounded audit in [PRIOR_ART.md](../PRIOR_ART.md).

## Source and endpoint convention

Kaitlyn Phillipson and J. Maurice Rojas, *Fewnomial systems with many roots, and an Adelic Tau Conjecture*, Contemporary Mathematics **605**, 45–71 (2013), DOI [10.1090/conm/605/12111](https://doi.org/10.1090/conm/605/12111). Inspected source: [arXiv:1011.4128v5](https://arxiv.org/pdf/1011.4128), 6 November 2012, 23 pages. The arXiv record verifies the authors, title, original submission 18 November 2010, and v5 date. Published volume/pages/DOI were cross-checked through the reference list of the primary SIAM paper [On the Number of Real Zeros of Random Fewnomials](https://epubs.siam.org/doi/10.1137/18M1228682); direct DOI resolution returned a browser-tool internal error. No local PDF checksum is claimed.

Theorem 1.6, p. 3, applies to n>=2. Writing the source variables as w_1,...,w_n, its real specialization epsilon=1/4 is the following system G=(G_1,...,G_n):

    G_1 = w_1*w_2 - (epsilon+w_1^2),
    G_j = w_j*w_(j+1) - (1+epsilon^(2j-3)*w_1^2),  2<=j<=n-1,
    G_n = w_n - (1+epsilon^(2n-3)*w_1^2).

The middle range is empty when n=2. The theorem gives exactly n+1 positive roots with nonsingular Jacobians. The proof appears on p. 14 and invokes Lemma 1.8. Thus the already established positive-root construction and its scalar root mechanism should be attributed to this source.

## Network

Fix n>=2 and put

    s_i = 16^(n-i)/4  (1<=i<=n),   s_(n+1)=0,
    B_i = 4(s_i-s_(i+1)).

Then B_i=15*16^(n-i-1) for i<n and B_n=1. Consider n+2 irreversible reactions, with mass-action monomials x^source (no combinatorial factorial convention):

| Reaction | Rate constant |
|---|---|
| 0 -> B_1 X_1 + ... + B_n X_n | 1/4 |
| X_1 -> 0 | s_1 |
| X_i+X_(i+1) -> 2X_i, 1<=i<=n-2 | s_(i+1) |
| X_(n-1)+X_n -> 2X_(n-1) | 1 |
| 2X_n -> 3X_n | 1 |

The third row denotes n-2 reactions and is empty at n=2. All sources have degree at most two; every product has nonnegative integer stoichiometry; all rates are positive. The n reaction vectors of the outflow and adjacent pairs form the matrix

    (-e_1, e_1-e_2, e_2-e_3, ..., e_(n-1)-e_n),

which has determinant (-1)^n. Therefore the stoichiometric rank is n. The inflow product molecularity is sum B_i=4s_1=16^(n-1); no minimality is claimed.

## Equilibrium equivalence and nondegeneracy

Set u=x_n^2 and denote the fluxes of outflow and adjacent-pair reactions by

    v_1 = s_1*x_1,
    v_i = s_i*x_(i-1)*x_i,       2<=i<=n-1,
    v_n = x_(n-1)*x_n.

The vectorfield f obeys

    f_i = s_i-s_(i+1)-v_i+v_(i+1),  i<n,
    f_n = s_n-v_n+u.

Define h_i=v_i-s_i-u. Direct cancellation gives

    f_i=-h_i+h_(i+1),  i<n;        f_n=-h_n.              (1)

Let J be the n-by-n reversal permutation matrix, let D=diag(s_1,...,s_(n-1),1), and set w=Jx. The source equations above give the exact polynomial identity

    h(x)=D*J*G(Jx).                                         (2)

For clarity, the first row of (2) uses s_1*epsilon^(2n-3)=1. Rows 2<=i<=n-1 use s_i*epsilon^(2n-2i-1)=1. The final row uses s_n=epsilon=1/4, so h_n=x_(n-1)x_n-(epsilon+x_n^2), exactly G_1(Jx). These identities also verify both exceptional endpoints.

Let T be upper bidiagonal with diagonal entries -1 and superdiagonal entries 1. Equations (1)–(2) state

    f(x)=T*D*J*G(Jx).

Every matrix in this identity is constant and invertible, and J maps the positive orthant bijectively to itself. Thus positive zeros of f correspond one-to-one to those of G. Differentiating gives

    Df(x)=T*D*J*DG(Jx)*J,
    det Df(x)=(-1)^n * (product_(i=1)^(n-1) s_i) * det DG(Jx).

The Jacobian determinant is nonzero at every positive root by Phillipson–Rojas Theorem 1.6. Since stoichiometric rank is full, this is exactly CRN nondegeneracy. The network therefore has exactly n+1 positive nondegenerate equilibria.

## Explicit low-dimensional checks

At n=2 the source equations are

    G_1=w_1*w_2-(1/4+w_1^2),
    G_2=w_2-(1+w_1^2/4).

The network is 0->15X_1+X_2 (rate1/4), X_1->0 (rate4), X_1+X_2->2X_1 (rate1), 2X_2->3X_2 (rate1). Its vectorfield is

    f_1=15/4-4x_1+x_1*x_2,
    f_2=1/4-x_1*x_2+x_2^2.

Here h_1=4x_1-4-x_2^2=4G_2(Jx) and h_2=x_1x_2-1/4-x_2^2=G_1(Jx), so f_1=-h_1+h_2 and f_2=-h_2. Eliminating x_1=1+x_2^2/4 gives

    x_2^3-4x_2^2+4x_2-1=(x_2-1)(x_2^2-3x_2+1),

with the three positive simple roots 1,(3-sqrt(5))/2,(3+sqrt(5))/2.

At n=3 the network has inflow product 240X_1+15X_2+X_3 and rates (1/4,64,4,1,1) in the order inflow,outflow,pair1,pair2,autocatalysis. Here

    h=(64x_1-64-x_3^2, 4x_1x_2-4-x_3^2, x_2x_3-1/4-x_3^2)
      =diag(64,4,1)*J*G(Jx).

Independent symbolic checks at n=2,...,8 verified the displayed flux row identity exactly; a second calculation at n=2,...,12 verified h=D*J*G(Jx) against the source equations, including all endpoint exponents. The argument for all n is the displayed general matrix identity, rather than those finite checks.

For n=1, use the separate elementary network 0->X, X->0, 2X->3X with rates (2,3,1). Its vectorfield (x-1)(x-2) gives two positive nondegenerate equilibria. Together, these constructions attain n+1 for every n>=1.

## Attribution boundary

Suggested language: “The general construction is a mass-action realization of the extremal polynomial chain of Phillipson and Rojas [Theorem 1.6]. It yields sharpness of the quadratic n-species, n+2-reaction bound.” The explicit matrix identity supplies the chemical bridge. An earlier written chemical realization was not found in the bounded search, but this negative search result does not establish historical priority.
