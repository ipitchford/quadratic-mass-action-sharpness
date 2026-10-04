> Historical internal audit. Workspace paths mentioned below describe the original run and are not distributed artifacts. The current proof is in `paper.tex`; historical verifier evidence is retained in `receipts/internal-audit-replay.json`. Revised evidence is indexed by `REPLAY_RECEIPT.md`.

# Independent adversarial audit

Auditor: `proof_audit`. Date: 2026-10-04. The pasted problem specification was read directly. The conclusions below were derived independently from the proposed reactions; they do not rely on a numerical solver or on an external upper-bound theorem.

## A. Three-species construction: PASS

Let N be an integer at least 6 and suppose

\[
4(N-1)^2<K<\frac{(N+1)^4}{4N}.
\]

The five proposed reactions are

\[
0\to N(N-1)X+Y+(N-1)Z,\quad X\to0,\quad
2Y\to3Y,\quad X+Z\to2X,\quad Y+Z\to2Z
\]

with rates \(1/N,N,N/K,1,1/N\), respectively. Their mass-action system, using rate monomials \(1,x,y^2,xz,yz\), is

\[
\begin{aligned}
f&=N-1-Nx+xz,\\
g&=N^{-1}+Ny^2/K-yz/N,\\
h&=(N-1)/N-xz+yz/N.
\end{aligned}
\]

All five reactants have molecularity at most two. All product complexes have nonnegative integer coefficients. All rates are positive. The reaction vectors of reactions 2, 3 and 4 are \((-1,0,0),(0,1,0),(1,0,-1)\), whose determinant is 1. Thus the stoichiometric rank is exactly three, and nondegeneracy is ordinary Jacobian nonsingularity.

### Exhaustive reconstruction

At any positive equilibrium, the first and third equations imply

\[
xz=Nx-(N-1),\qquad yz=N^2x-(N^2-1).
\]

The second equation also gives \(yz=1+N^2y^2/K>1\). Therefore \(x>1\). Define \(t=1/(x-1)>0\). Every positive equilibrium must have

\[
x=\frac{t+1}{t},\quad z=\frac{t+N}{t+1},\quad
y=\frac{(t+1)(t+N^2)}{t(t+N)}.
\]

The remaining equation becomes \(y^2=K/t\), or

\[
F(t)=K,\qquad F(t)=\frac{(t+1)^2(t+N^2)^2}{t(t+N)^2}.
\]

Conversely, every positive root of this scalar equation produces a strictly positive equilibrium by the displayed formulas. No positive equilibrium is excluded, and distinct t give distinct x.

### Four roots throughout the stated parameter interval

Put \(u=\sqrt t\), \(v=u+N/u\). Then \(v\ge 2\sqrt N\), and

\[
\sqrt{F(t)}=v+\frac{(N-1)^2}{v}.
\]

For N at least 6, \(N-1>2\sqrt N\). The function \(v+(N-1)^2/v\) decreases strictly on \([2\sqrt N,N-1]\) and increases strictly on \([N-1,\infty)\). Its minimum is \(2(N-1)\) and its value at the left endpoint is \((N+1)^2/(2\sqrt N)\). The strict K inequalities thus produce exactly two distinct v, both larger than \(2\sqrt N\) and neither equal to \(N-1\). Each gives exactly two positive distinct u from \(u^2-vu+N=0\). Hence there are exactly four distinct positive t. Neither map has zero derivative at any of them, so \(F'(t)\ne0\).

### Exact nondegeneracy

The actual Jacobian is

\[
J=\begin{pmatrix}
-N+z&0&x\\
0&-z/N+2Ny/K&-y/N\\
-z&z/N&-x+y/N
\end{pmatrix}.
\]

After equilibrium reconstruction and substitution \(K=F(t)\), direct exact algebra gives

\[
\det J=-\frac{t(t+N)^3}{(t+N^2)^2(t+1)^2}F'(t).
\]

Equivalently,

\[
\det J=-\frac{(t-N)\,[t^2+(4N-N^2-1)t+N^2]}{t(t+N^2)(t+1)}.
\]

Every denominator and every prefactor outside F' is strictly positive. Thus all four positive equilibria are nondegenerate.

### Concrete witness N=7, K=145

The parameter inequalities are \(144<145<4096/28\). The scalar polynomial is exactly

\[
P(t)=t^4-45t^3+568t^2-2205t+2401.
\]

Dividing by \(t^2\) and setting \(q=t+49/t\) gives

\[
P(t)/t^2=q^2-45q+470.
\]

Its two q roots are \((45\pm\sqrt{145})/2\), both strictly above 14 (for the smaller one, use \(\sqrt{145}<17\)). Each therefore yields two distinct positive t. The four disjoint rational isolating intervals can be taken as

\[
(1,2),\quad(3,4),\quad(12,13),\quad(26,27).
\]

The polynomial signs at the eight endpoints are respectively

\[
720,-81;\quad -236,45;\quad709,-576;\quad-4905,2644.
\]

Each interval contains at least one root by continuity; degree four shows exactly one in each and shows that every root is simple. Numerical roots, solely as an orientation aid, are approximately 1.8362701237, 3.8932200450, 12.5859826656 and 26.6845271657.

### Optional exact dynamical extension: two sinks and two index-one saddles

For N=7, write \(\det(\lambda I-J)=\lambda^3+a\lambda^2+b\lambda+c\). At an equilibrium parameter t,

\[
a=\frac{49t^3+2623t^2+14363t-2107}{7(t+1)(t+7)(t+49)},
\]

\[
b=\frac{2(25t^5+1031t^4+2941t^3+8785t^2+21854t+9604)}{7t(t+1)^2(t+7)(t+49)},
\]

\[
c=\frac{(t-7)(t^2-22t+49)}{t(t+49)(t+1)}.
\]

Moreover \(ab-c\) has positive denominator
\(49t(t+1)^3(t+7)^2(t+49)^2\) and numerator

\[
2401t^8+230424t^7+6455174t^6+46202960t^5+
126203376t^4+338658376t^3+655594618t^2+252969360t-117649.
\]

For every \(t>1\), a, b and \(ab-c\) are strictly positive: their sole negative constant terms are dominated already by their linear terms. On the four isolating intervals c has signs \(-,+,-,+\), respectively. Routh-Hurwitz therefore proves that equilibria 2 and 4 are asymptotically stable (all eigenvalues have strictly negative real part). At equilibria 1 and 3, Descartes' rule gives exactly one positive real eigenvalue; the other two have positive product and negative sum, hence negative real parts. These are hyperbolic saddles with one unstable direction. This proves local bistability, without asserting a global basin decomposition or excluding other attractors.

## B. Extension to every dimension: PASS

For an integer \(n\ge1\), put

\[
R=2^{4n+2},\qquad s_i=R^{n+1-i}\ (1\le i\le n),\qquad s_{n+1}=0,
\]

\[
A_i=s_i-s_{i+1},\quad B=2\sum_{k=1}^n(-1)^{k-1}k
=\begin{cases}n+1&n\text{ odd},\\-n&n\text{ even},\end{cases}
\quad C=R^{B-1/2}.
\]

Every A_i is a positive integer and C is a positive rational number, because \(\sqrt R=2^{2n+1}\). Consider the n+2 reactions

\[
0\to\sum_{i=1}^n A_iX_i,\qquad X_1\to0,\qquad
X_i+X_{i+1}\to2X_i\ (1\le i<n),\qquad 2X_n\to3X_n.
\]

All rates are 1 except the last, which has rate \(1/C\). Every reactant has molecularity at most two. The vectors \(-e_1\) and \(e_i-e_{i+1}\), \(1\le i<n\), are linearly independent; hence the rank is n. For n=1 the transfer list is empty and the construction still consists of exactly three distinct reactions.

### Equilibrium reconstruction is bijective

Let \(w_1=x_1\), \(w_i=x_{i-1}x_i\) for \(2\le i\le n\), and \(t=x_n^2/C>0\). The equilibrium equations are

\[
0=A_i-w_i+w_{i+1}\ (i<n),\qquad 0=A_n-w_n+t.
\]

Back substitution gives \(w_i=t+s_i\), whence

\[
x_1=t+s_1,\qquad x_i=\frac{t+s_i}{x_{i-1}}\ (2\le i\le n).
\]

Every positive t reconstructs a unique positive x. The sole remaining condition is

\[
H(t)=C,\qquad H(t)=\frac{x_n(t)^2}{t}
=\frac1t\prod_{k=1}^n(t+R^k)^{2(-1)^{k-1}}.
\]

Conversely this condition makes t the actual final reaction flux and gives every steady-state equation. Distinct t give distinct \(x_1\).

### Exact root count

For j from 1 through n, put

\[
E_j=-j+2\sum_{k=1}^n(-1)^{k-1}\max(j,k).
\]

Here \(E_1=B-1\), and \(E_{j+1}-E_j=(-1)^{j+1}\), so E_j is B-1 for odd j and B for even j. Factoring each \(R^j+R^k\) by \(R^{\max(j,k)}\) gives a residual factor between 1 and 2. Consequently

\[
2^{-2n}R^{E_j}\le H(R^j)\le2^{2n}R^{E_j}.
\]

Because \(\sqrt R=2^{2n+1}>2^{2n}\), these inequalities imply strictly

\[
H(R^j)<C\quad(j\text{ odd}),\qquad H(R^j)>C\quad(j\text{ even}).
\]

Also \(H(t)\to\infty\) as \(t\downarrow0\). As \(t\to\infty\), H tends to infinity for odd n and to zero for even n. There is therefore a positive root in each of the n+1 disjoint intervals

\[
(0,R),(R,R^2),\ldots,(R^{n-1},R^n),(R^n,\infty).
\]

Clearing the strictly positive denominator gives

\[
P_n(t)=\prod_{k\text{ odd}}(t+R^k)^2
-Ct\prod_{k\text{ even}}(t+R^k)^2.
\]

For odd n, the two summands have degrees n+1 and n; for even n they have degrees n and n+1. Thus P_n has degree exactly n+1. Its n+1 distinct positive roots exhaust its roots, and each is simple. In particular \(H'\ne0\) at every root. This is an exact existence, exhaustion and simplicity proof, valid for every n≥1.

### Exact Jacobian determinant

Let \(A=D_x(w_1,\ldots,w_n)\). This is lower bidiagonal with diagonal \(1,x_1,\ldots,x_{n-1}\), so \(\det A=\prod_{j=1}^{n-1}x_j>0\). For n=1 the empty product equals 1. Along the reconstructed curve, \(Ax'(t)=\mathbf1\).

Define \(G_i(x)=w_i(x)-x_n^2/C-s_i\). The actual vector field is
\(f_i=-G_i+G_{i+1}\) for i<n and \(f_n=-G_n\). The determinant of this linear transformation is \((-1)^n\). Also

\[
D_xG=A-\mathbf1(2x_n/C)e_n^T.
\]

The matrix determinant lemma gives

\[
\det D_xG=\det A\left(1-\frac{2x_nx_n'}C\right).
\]

At an equilibrium \(x_n^2=Ct\), differentiation of \(x_n(t)^2=tH(t)\) yields
\(2x_nx_n'=C+tH'(t)\). Hence

\[
\boxed{\det D_xf=(-1)^{n+1}\frac{tH'(t)}C\prod_{j=1}^{n-1}x_j.}
\]

All factors apart from H' are nonzero, and H' is nonzero at every equilibrium. Thus all n+1 equilibria are nondegenerate.

## C. Simplified fixed-base all-dimensional construction: PASS

The full proof in `work/general-dimension/proof.md` was read directly after the independent audit above. Its fixed choice R=25 is valid for every n≥1 (the displayed source-facing theorem there states n≥2). Set s_i, A_i and B as above, but now with R=25; take final rate

\[
k=5^{(-1)^n(2n+1)},\qquad C=1/k=25^{B-1/2}.
\]

At the n+2 test points \(t=25^j\), \(0\le j\le n+1\), the tropical exponent is B for even j and B-1 for odd j. Each correction factor is \(1+25^{-|j-h|}\). At most one factor is 2; the others have their increments summing to at most \(2\sum_{d\ge1}25^{-d}=1/12\). The elementary product inequality \(\prod(1+a_i)\le(1-\sum a_i)^{-1}\) bounds their product by 12/11. Since exponents are ±2, the entire correction lies between 121/576 and 576/121. These bounds lie strictly between 1/5 and 5, as \(576<605\). Consequently \(H(25^j)-C\) is positive for even j and negative for odd j.

The n+1 intervals \((25^j,25^{j+1})\), \(0\le j\le n\), therefore each contain a root. The same exact degree n+1 argument proves that these roots are exhaustive and simple, and the same determinant formula proves nondegeneracy. All roots are greater than 1; no appeal to asymptotics is necessary for this stronger construction.

The alternate nondegeneracy argument in the general-dimensional proof also passes: for monomial coordinates \(u_1=x_1,u_i=x_{i-1}x_i\), the first n-1 rows of the linearized equilibrium map force any kernel vector to be constant; its last row equals \(aktH'(t)\), forcing that constant to be zero. This is a coordinate change of the equilibrium map, and composition with the nonsingular concentration-to-monomial Jacobian preserves nonsingularity.

## D. Second three-species source-support construction: PASS

The construction agent supplied a second network, here reconstructed explicitly from its stoichiometric matrix:

\[
X\to0,\quad Y\to6X+4Z,\quad2X\to6Y+4Z,\quad
2Z\to4Y,\quad Y+Z\to0.
\]

Its rates are \(1,1,1,2/3137,1\). Its source complexes are distinct and quadratic. The determinant of its first three reaction vectors is 28, so it has rank three. The mass-action system is

\[
f_1=-x+6y-2x^2,\quad
f_2=-y+6x^2+8z^2/3137-yz,\quad
f_3=4y+4x^2-4z^2/3137-yz.
\]

At a positive equilibrium, f_1=0 and f_2+2f_3=0 imply

\[
y=x(1+2x)/6,\qquad z=7(1+14x)/(3(1+2x)).
\]

Define \(t=(5-2x)/(1+14x)\). Initially \(-1/7<t<5\), and the inverse reconstruction is

\[
x=\frac{5-t}{2(7t+1)},\quad
y=\frac{(5-t)(t+1)}{2(7t+1)^2},\quad z=\frac{14}{t+1}.
\]

With

\[
P(t)=3137t(5-t)(t+1)^2-784(7t+1)^2
=-3137t^4+9411t^3-10183t^2+4709t-784,
\]

and \(D=3137(t+1)^2(7t+1)^2\), exact substitution gives \(f(\phi(t))=(0,-2P/D,P/D)\). For \(-1/7<t\le0\), the first term in P is nonpositive and its second is strictly negative; thus P<0. Therefore every positive equilibrium has \(0<t<5\), and conversely every P-root in that interval gives a positive equilibrium.

At \(t=0,1/2,5/7,1,5\), the polynomial values are exactly

\[
-784,\quad81/16,\quad-6624/2401,\quad16,\quad-1016064.
\]

The four alternating-sign intervals inside (0,5) force four distinct roots, and degree four shows exhaustion and simplicity. At each root, independent exact Jacobian algebra gives

\[
\det J=\frac{(5-t)P'(t)}{6274(t+1)(7t+1)^2}\ne0.
\]

This verifies exactly four nondegenerate positive equilibria for the second construction. The classification of its source support into a particular equivalence orbit is not part of this audit.

## Scope and unresolved external checks

The exact constructions and counts pass this mathematical audit. They do not themselves prove an upper bound for every admissible network; any claim of universal sharpness must cite and check the source theorem and its hypotheses. Nor does this audit certify novelty, bibliographic priority, review by an external human, publication, deployment, or public availability. The general-dimensional result asserts n+1 equilibria in the displayed n+2-reaction family; it does not assert n+1 stable equilibria.
