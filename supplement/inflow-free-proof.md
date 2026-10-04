# A second support orbit attaining four positive equilibria

This is an exact constructive result, independently reducible to elementary
polynomial identities. It concerns nondegenerate equilibria, not stable ones.

## Network and rate constants

In the listed order take

1. X -> 0, rate 1;
2. Y -> 6X + 4Z, rate 1;
3. 2X -> 6Y + 4Z, rate 1;
4. 2Z -> 4Y, rate 2/3137;
5. Y + Z -> 0, rate 1.

Under the convention that a reaction with source 2X has mass-action monomial
x^2 (with any combinatorial factor absorbed into its rate), the vector field is

f1 = -x + 6y - 2x^2,
f2 = -y + 6x^2 + (8/3137)z^2 - yz,
f3 = 4y + 4x^2 - (4/3137)z^2 - yz.

The stoichiometric matrix, with the listed reaction order, is

N = [[-1, 6,-2, 0, 0],
     [ 0,-1, 6, 4,-1],
     [ 0, 4, 4,-2,-1]].

The minor on columns 1,2,4 is 14, so the rank is three. There are exactly
five reactions, all sources have total molecularity at most two, and all
products have total molecularity at most ten. This is the quartic-support
orbit {x,y,x^2,z^2,yz}, distinct under species permutation from
{1,x,y^2,xz,yz}.

## Complete positive-equilibrium parametrization

Let w = (x, y, x^2, (2/3137)z^2, yz)^T be the positive reaction flux vector.
The kernel of N is

w = lambda [2(7t+1), 2(t+1), 5-t, 2t, 28]^T,

where positivity is exactly lambda > 0 and 0 < t < 5. For example,
t = 14 w4/w5 and lambda = w5/28. This expression follows by elementary
linear elimination; hence it covers every positive equilibrium.

Using w3=x^2 and w1=x gives lambda=(5-t)/(4(7t+1)^2). Then

x(t) = (5-t)/(2(7t+1)),
y(t) = (5-t)(t+1)/(2(7t+1)^2),
z(t) = 14/(t+1).

These coordinates are strictly positive on 0<t<5. The remaining flux
identity w4=(2/3137)z^2 is equivalent to

P(t) = 3137 t(5-t)(t+1)^2 - 784(7t+1)^2
     = -3137t^4 + 9411t^3 - 10183t^2 + 4709t - 784 = 0.

Conversely, direct substitution gives

f(phi(t)) = [0,-2P(t)/D(t),P(t)/D(t)]^T,
D(t) = 3137(t+1)^2(7t+1)^2 > 0,

so every root in (0,5) yields a positive equilibrium. The parametrization
is injective because x'(t)=-18/(7t+1)^2<0.

## Four simple roots

Exact values are

P(0) = -784,
P(1/2) = 81/16,
P(5/7) = -6624/2401,
P(1) = 16,
P(5) = -1016064.

The intermediate value theorem provides one root in each of
(0,1/2), (1/2,5/7), (5/7,1), and (1,5). Since P has degree four,
these are all its roots and each is simple. Thus the network has exactly
four positive equilibria.

For orientation only, the roots are approximately
0.435888785981143, 0.631110387069498, 0.806399575471412,
1.12660125147795. Numerical approximations are not used in the proof.

## Jacobian nondegeneracy

Let J = Df. An exact rational-function identity is

det J(phi(t)) = (5-t)P'(t)/(6274(t+1)(7t+1)^2)
             + 2(t-5)(7t+4)P(t)/(3137(t+1)^2(7t+1)^3).

At a root of P, the second term vanishes; the first is nonzero because
0<t<5 and P'(t) is nonzero. Thus all four equilibria are nondegenerate.

A conceptual derivation avoids expanding the determinant. Replace f2 by
f2+2f3, preserving the Jacobian determinant, and eliminate y,z from the
first two equations. Their minor in variables (y,z) is -18y. Along the
resulting curve, f3=P/D and x'(t)=-18/(7t+1)^2. At a root,

det J = (-18y) (df3/dt)/(dx/dt)
      = y P'(t)/(3137(t+1)^2),

which is the displayed formula after substituting y(t).

## Exact one-rate family

Keep the same network and set rates (1,1,1,1/K,1), K>0. The positive
flux circuit becomes

R(t) = 392(7t+1)^2/[t(5-t)(t+1)^2] = K, 0<t<5.

Its derivative factors exactly:

R'(t) = 392(t-1)(2t-1)(7t-5)(7t+1)
        /[t^2(t-5)^2(t+1)^3].

The minima at t=1/2 and t=1 both equal 1568. The intermediate maximum
at t=5/7 equals 117649/75. The function diverges to positive infinity
at both endpoints 0 and 5. Consequently there are exactly four positive
nondegenerate equilibria if and only if

1568 < K < 117649/75.

The chosen K=3137/2 lies strictly in this interval. Below the lower
endpoint there are no positive equilibria; at it there are two double
roots. At the upper endpoint there are three distinct positive roots,
one double. Above it there are two simple positive equilibria. This
classification is for this specified one-parameter rate family.

No claim of globally minimal product size is made.
