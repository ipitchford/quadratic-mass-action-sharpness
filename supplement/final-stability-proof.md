# Final exact local-stability proof

Version 2 publication candidate, 4 October 2026. This is a final proof for the reciprocal example (N=7,K=145), rather than a historical search record. The parameter (K) here belongs to that reciprocal family; the inverse fourth rate of the inflow-free family is denoted (L) in the revised manuscript.

## Reaction system and equilibria

The five reactions are

\[
0\to42X+Y+6Z,\quad X\to0,\quad2Y\to3Y,\quad
X+Z\to2X,\quad Y+Z\to2Z,
\]

with rate constants ((1/7,7,7/145,1,1/7)). Their original mass-action vector field is

\[
f_1=6-7x+xz,\quad f_2=\frac17+\frac7{145}y^2-\frac17yz,
\quad f_3=\frac67-xz+\frac17yz.
\]

Every positive equilibrium is uniquely represented by

\[
x=\frac{t+1}{t},\quad
y=\frac{(t+1)(t+49)}{t(t+7)},\quad
z=\frac{t+7}{t+1},
\]

where (t>0) is a root of

\[
P(t)=t^4-45t^3+568t^2-2205t+2401.
\]

There is exactly one simple root in each of

\[
(1,2),\quad(3,4),\quad(12,13),\quad(26,27).
\]

The endpoint-value pairs are ((720,-81),(-236,45),(709,-576),(-4905,2644)). Four disjoint sign changes and degree four establish the exact count and simplicity. In particular, every equilibrium parameter has (t>1).

## Original Jacobian and exact coefficients

The concentration Jacobian is

\[
J=\begin{pmatrix}
-7+z&0&x\\
0&-z/7+14y/145&-y/7\\
-z&z/7&-x+y/7
\end{pmatrix}.
\]

At a root of (P), use

\[
145=\frac{(t+1)^2(t+49)^2}{t(t+7)^2}.
\]

Then (det(lambda I-J)=lambda^3+a(t)lambda^2+b(t)lambda+c(t)), where

\[
a(t)=\frac{49t^3+2623t^2+14363t-2107}{7(t+1)(t+7)(t+49)},
\]

\[
b(t)=\frac{2(25t^5+1031t^4+2941t^3+8785t^2+21854t+9604)}
{7t(t+1)^2(t+7)(t+49)},
\]

\[
c(t)=\frac{(t-7)(t^2-22t+49)}{t(t+49)(t+1)}.
\]

The rational identity

\[
ab-c=\frac{U(t)}{49t(t+1)^3(t+7)^2(t+49)^2}
\]

has numerator

\[
\begin{aligned}
U(t)={}&2401t^8+230424t^7+6455174t^6+46202960t^5\\
&+126203376t^4+338658376t^3+655594618t^2\\
&+252969360t-117649.
\end{aligned}
\]

These are exact characteristic coefficients of the chemical Jacobian at equilibrium. They are not inferred from the earlier fewnomial system: invertible operations on equations preserve zeros and nonsingularity, but do not in general preserve eigenvalues or stability.

## Strict Hurwitz inequalities

All denominators above are strictly positive for (t>1). The numerator of (b) has only positive coefficients. The only negative constant term in the numerator of (a) is dominated by (14363t), and that of (U) is dominated by (252969360t). Consequently (a>0), (b>0), and (ab-c>0) throughout (t>1).

For a polynomial-based certificate, substitution (t=u+1) gives the following strictly positive coefficient lists in descending powers:

| Numerator | Coefficients after (t=u+1) |
|---|---|
| Numerator of (a) | (49,2770,19756,14928) |
| Numerator of (b), including its factor 2 | (50,2312,14630,48088,104992,88480) |
| (U) | (2401,249632,8135370,89907364,462278696,1442804256,2992553344,3356325248,1426199040) |

The determinant identity at a root is

\[
\det J=-\frac{P'(t)}{145t(t+7)},\qquad
c(t)=-\det J=\frac{P'(t)}{145t(t+7)}.
\]

Since (P) is monic with four simple ordered roots, its derivative has signs (-,+,-,+) at them. Thus (c) has those same four signs.

At roots 2 and 4, (a,b,c>0) and (ab>c). The cubic Routh–Hurwitz criterion puts every eigenvalue in the open left half-plane. These equilibria are hyperbolic sinks and are locally asymptotically stable.

At roots 1 and 3, the characteristic coefficients have signs (+,+,+,-), so Descartes' rule of signs gives exactly one positive real eigenvalue (ho), counting multiplicity. The remaining two eigenvalues have sum (-a-ho<0) and product (-c/ho>0). If they are real, both are strictly negative; if they are a conjugate pair, both have strictly negative real part. These equilibria are hyperbolic saddles with exactly one unstable direction.

## Conclusion and scope

The four positive equilibria, in increasing (t), have types **saddle, sink, saddle, sink**. This proves local bistability for the stated chemical system: two distinct positive equilibria attract nearby positive initial conditions. It does not establish global convergence, classify every attractor, determine basin boundaries, or imply experimental or thermodynamic realizability. No stability classification is claimed for every member of the reciprocal family or for the general-dimensional chain.
