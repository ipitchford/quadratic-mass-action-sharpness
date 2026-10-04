# Independent analytic audit

Status: exact calculations below support the constructions; they are not an
independent external peer review.

## Three-species reciprocal family

For an integer N >= 6, take reactions

* 0 -> N(N-1)X + Y + (N-1)Z, rate 1/N;
* X -> 0, rate N;
* 2Y -> 3Y, rate N/K;
* X+Z -> 2X, rate 1;
* Y+Z -> 2Z, rate 1/N.

The differential equations are

    x' = N-1 - N*x + x*z
    y' = 1/N + (N/K)*y^2 - y*z/N
    z' = (N-1)/N - x*z + y*z/N.

Every positive equilibrium is parameterized by t > 0 with

    x = 1 + 1/t,
    y = sqrt(K/t),
    z = (t+N)/(t+1),

and the single equation

    F(t) = (t+1)^2 (t+N^2)^2 / [t(t+N)^2] = K.

Let v = sqrt(t) + N/sqrt(t). Then v >= 2 sqrt(N), and

    sqrt(F(t)) = v + (N-1)^2/v.

Consequently there are exactly four positive simple solutions when

    4(N-1)^2 < K < (N+1)^4/(4N).

This interval is nonempty precisely when N > 3+2sqrt(2). Each of the two
distinct admissible values of v gives two positive values of sqrt(t).

Direct symbolic calculation gives, at these equilibria,

    det J = -(t-N)[t^2 + (4N-N^2-1)t + N^2]
            / [t(t+N^2)(t+1)].

The zeros of the numerator are exactly the critical points of F. Thus all
four equilibria in the open parameter interval are nondegenerate.

For N=7, K=145, the polynomial is

    t^4 - 45t^3 + 568t^2 - 2205t + 2401.

Its positive roots, used only as a numerical cross-check, are approximately
1.8362701237, 3.8932200450, 12.5859826656, and 26.6845271657.
The two values of v are exactly (sqrt(145) +/- 1)/2.

The sharper N=6 example uses products 30X+Y+5Z, 0, 3Y, 2X, 2Z.
Here the four-root interval is 100 < K < 2401/24, and F has critical points
4, 6, 9. An asymmetric variant with integer shifts A,C has logarithmic
derivative numerator

    t^3 + (3A-C-1)t^2 + [A(C+1)-3C]t - AC.

A finite exact scan found no three positive critical points for integer
2 <= A < C < 36; the first pair is A=6,C=36. This finite scan is only a
statement about that particular family, not an optimality claim over CRNs.

## All-dimensional construction audit

For n >= 2, put R=2^(4n+2), s_i=R^(n+1-i), s_(n+1)=0,
A_i=s_i-s_(i+1), and B=sum(k=1..n) 2(-1)^(k-1)k.
Thus B=n+1 for odd n and B=-n for even n. Let C=R^(B-1/2), which is
positive and rational because R is an even power of 2.

Use n+2 reactions: inflow 0 -> sum A_i X_i; X_1 -> 0;
X_i+X_(i+1) -> 2X_i for i=1,...,n-1; and 2X_n -> 3X_n.
All rates are 1 except the last, which has rate 1/C.

At an equilibrium, set t=x_n^2/C. Backward flux balance gives

    x_1=t+s_1,
    x_(i-1) x_i=t+s_i  (i=2,...,n).

The recursion determines all concentrations positively and smoothly from t.
The remaining condition is H(t)=C, where

    H(t)=t^-1 product(k=1..n) (t+R^k)^[2(-1)^(k-1)].

At t=R^j, the power of R in H is B-1 for odd j and B for even j.
Writing each factor as R^max(j,k) times a number in [1,2] shows that the
remaining multiplicative factor lies in [2^(-2n),2^(2n)]. Therefore

    H(R^j)/C <= 1/2 when j is odd,
    H(R^j)/C >= 2 when j is even.

Also H(0+)=infinity; H(infinity)=infinity for odd n and 0 for even n.
There is a root in every interval (0,R), (R,R^2), ...,
(R^(n-1),R^n), (R^n,infinity). Clearing positive denominators gives a
polynomial of degree exactly n+1. Hence these are all roots, every root is
simple, and all n+1 are positive.

For nondegeneracy, introduce the augmented equations

    G_1=x_1-t-s_1,
    G_i=x_(i-1)x_i-t-s_i  (i=2,...,n),
    G_(n+1)=x_n^2/C-t.

The first n equations have triangular x-Jacobian with positive diagonal
(1,x_1,...,x_(n-1)). Their Schur complement in the final equation is the
derivative of t(H(t)/C-1), which at a root is t H'(t)/C != 0. Thus the
augmented system is nonsingular. It is equivalent by invertible equation
operations and elimination of t to the original steady-state system, so
the original n-dimensional Jacobian is nonsingular.

The outflow vector -e_1 and conversion vectors e_i-e_(i+1) are linearly
independent, proving stoichiometric rank n. Sources 0,e_1,e_1+e_2,...,
e_(n-1)+e_n,2e_n have affine rank n.

## Source caveat for the parent manuscript

The live Springer source for DOI 10.1007/s00285-026-02429-8, Theorem 5.5
and Remark 5.8, explicitly discusses the n+1 upper bound and its sharpness
for n >= 3. Its Remark 5.6 appears to claim that quadratic rank-one networks
cannot have multiple positive nondegenerate equilibria. Under the paper's
source-only definition of quadratic, 0->X, X->0, 2X->3X immediately
contradicts that statement for appropriate rates. The construction does
not need the n=1 case; restrict the prospective sharpness theorem to n>=2
or n>=3 unless that apparent source error is investigated separately.
