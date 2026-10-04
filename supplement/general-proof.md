# Sharp quadratic reaction networks in every dimension n >= 2

This is a complete constructive proof. The universal upper bound of n+1 is
external (Banaji–Feliu, Theorem 5.5); the construction and its attainment proof
below are independent of that upper bound.

## The network

Fix an integer n >= 2, put R=25, and define

\[
s_i=25^{n+1-i}\quad(1\le i\le n),\qquad s_{n+1}=0,
\qquad A_i=s_i-s_{i+1}.
\]

Thus A_i=24*25^(n-i) for i<n and A_n=25. Consider the n+2 reactions

\[
0\longrightarrow\sum_{i=1}^n A_iX_i,\qquad
X_1\longrightarrow0,\qquad
X_i+X_{i+1}\longrightarrow2X_i\quad(1\le i<n),\qquad
2X_n\longrightarrow3X_n.
\]

Every rate constant is 1 except the final rate constant

\[
k=5^{(-1)^n(2n+1)}.
\]

All product coefficients are nonnegative integers and all rates are positive
rationals. The n+2 source complexes are distinct and quadratic. The reaction
vectors of X_1->0 and the n-1 chain transfers are
-e_1, e_1-e_2, ..., e_(n-1)-e_n. They form a basis of R^n, so the network has
stoichiometric rank n.
The sources 0, X_1, X_1+X_2, ..., X_(n-1)+X_n are affinely independent,
since their nonzero exponent vectors form a triangular matrix with diagonal
entries 1. Thus the source rank is n as well.

## Positive equilibria reduce to one scalar equation

Write

\[
v_1=x_1,\qquad v_i=x_{i-1}x_i\ (2\le i\le n),\qquad
v_{n+1}=kx_n^2.
\]

The differential equations are

\[
\dot x_i=A_i-v_i+v_{i+1}\qquad(1\le i\le n).
\]

At an equilibrium, putting t=v_(n+1)>0, backwards substitution gives exactly

\[
v_i=t+s_i\qquad(1\le i\le n).
\]

Conversely these flux identities determine unique positive concentrations:

\[
x_1(t)=t+s_1,\qquad x_i(t)=\frac{t+s_i}{x_{i-1}(t)}\ (2\le i\le n).
\]

The only remaining identity is k*x_n(t)^2=t. By the recursion,

\[
H(t):=\frac{x_n(t)^2}{t}
=\frac1t\prod_{h=1}^n(t+25^h)^{2(-1)^{h-1}}.
\]

Hence there is a bijection between positive equilibria and positive roots of
H(t)=C, where

\[
B:=2\sum_{h=1}^n(-1)^{h-1}h
=\begin{cases}n+1& n\text{ odd},\\-n&n\text{ even},\end{cases}
\qquad C=\frac1k=25^{B-1/2}.
\]

The equality C=1/k follows from 2B-1=(-1)^(n+1)*(2n+1).

## Uniform elementary product bound

If a_1,...,a_m >=0 and S=sum a_i<1, then

\[
\prod_{i=1}^m(1+a_i)\le\frac1{1-S}.
\]

Indeed 1+a_i <= 1/(1-a_i), and induction gives
product(1-a_i) >= 1-sum a_i: the induction step is
(1-S_prev)(1-a_m)=1-S_prev-a_m+S_prev*a_m >=1-S.

For any integer j in {0,...,n+1}, factor

\[
25^j+25^h=25^{\max(j,h)}(1+25^{-|j-h|}).
\]

At most one factor (the one with h=j, if present) has its second factor equal
to 2. For all the others,

\[
\sum_{\substack{1\le h\le n\\h\ne j}}25^{-|j-h|}
\le2\sum_{d=1}^\infty25^{-d}=\frac1{12}.
\]

Thus the product of all these second factors is at most
2*(12/11)=24/11, including the possible factor 2. Since all exponents in
H's product are either +2 or -2, its correction factor E_j satisfies

\[
\frac{121}{576}\le E_j\le\frac{576}{121}.
\]

The bounds lie strictly between 1/5 and 5, since 605>576.

## Alternating signs and exact root count

The pure power of 25 in H(25^j) has exponent

\[
D_j=-j+2\sum_{h=1}^n(-1)^{h-1}\max(j,h).
\]

Here D_0=B, and for 0<=j<=n,

\[
D_{j+1}-D_j=-1+2\sum_{h=1}^j(-1)^{h-1}
=\begin{cases}-1&j\text{ even},\\1&j\text{ odd}.
\end{cases}
\]

Consequently D_j=B for even j and D_j=B-1 for odd j, throughout
0<=j<=n+1. Therefore

\[
\frac{H(25^j)}C=
\begin{cases}5E_j>1&j\text{ even},\\E_j/5<1&j\text{ odd}.
\end{cases}
\]

By continuity H(t)-C has a root in each of the n+1 disjoint intervals

\[
(25^j,25^{j+1})\qquad (j=0,1,\ldots,n).
\]

Clear the positive denominator and define

\[
P(t)=\prod_{\substack{1\le h\le n\\h\text{ odd}}}(t+25^h)^2
-Ct\prod_{\substack{1\le h\le n\\h\text{ even}}}(t+25^h)^2.
\]

If n is odd, the first term has degree n+1 and the second degree n; if n is
even, the degrees are n and n+1 respectively. Thus P has degree exactly n+1.
The n+1 roots already obtained are distinct, so they exhaust all roots of P,
are simple, and are all positive. The positive equilibria are therefore
exactly n+1 in number.

## Nondegeneracy in the original concentrations

Use positive monomial coordinates

\[
u_1=x_1,\qquad u_i=x_{i-1}x_i\quad(2\le i\le n).
\]

The recursive inverse above shows that x->u is a smooth bijection of the
positive orthant with smooth inverse; its Jacobian is nonsingular. In these
coordinates set phi(u)=k*x_n(u)^2. The equilibrium equations become

\[
F_i(u)=A_i-u_i+u_{i+1}\quad(i<n),\qquad
F_n(u)=A_n-u_n+\phi(u).
\]

Suppose DF(u) has a kernel vector z. The first n-1 rows force
z_1=...=z_n=a. The last row is

\[
a\left(\frac{d}{dt}\phi(t+s_1,\ldots,t+s_n)-1\right)
=a\left(kH(t)+ktH'(t)-1\right)=aktH'(t).
\]

At an equilibrium kH(t)=1, and P'(t) !=0 implies H'(t) !=0, because the
denominator used to clear H-C is strictly positive. Hence a=0; DF has
trivial kernel. The concentration Jacobian is DF(u)*Du(x), also nonsingular.
All n+1 equilibria are nondegenerate.

## Conclusion and scope

For every n>=2 there is a quadratic (n,n+2,n) mass-action network with exactly
n+1 positive equilibria, all nondegenerate. In conjunction with the published
upper bound, n+1 is the sharp maximum. In particular n=3 settles the requested
four-equilibrium problem, and the same construction settles the general-n
sharpness question in Banaji–Feliu Remark 5.8. No claim of stability is made.

This proof does not require numerical root finding or an asymptotic choice of
parameters. The root intervals, reactions, and rates are explicit for every n.
