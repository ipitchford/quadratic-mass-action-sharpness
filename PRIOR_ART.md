# Bounded prior-art audit: quadratic (3,5,3) networks and all-dimensional sharpness

Search date: 2026-10-04 (Europe/London). Researcher: prior_art subagent. Intended contribution: an explicit chemical realization attaining four positive nondegenerate equilibria, with an exact proof, extended to n+1 equilibria in n species. Status: **BOUNDED UNCERTAINTY** for chemical-realization priority, but **EXACT PRIOR-ART COLLISION** for the all-dimensional quadratic polynomial chain and its alternating-product scalar mechanism: Phillipson–Rojas (2013), Theorem 1.6. No prior chemical realization was found in the sources/searches below. This is not an absolute novelty clearance.

## Frozen scope and translations

There exist five reactions on three species, with nonnegative integer source/product stoichiometries, every source of total molecularity at most two, stoichiometric rank three, and one vector of positive rate constants yielding four distinct positive equilibria with nonsingular Jacobian. Products have no imposed molecularity bound. Stability is not part of this claim.

The mass-action coefficient matrix is C=Gamma*diag(k), with sources as columns of S and ODE C*x^(S^T). In the cited CRN papers A=S^T. In the fewnomial papers the homogenized exponent matrix has columns (1,S_j), and a Gale circuit vector b satisfies S*b=0 and sum(b)=0. Positive diagonal reaction scaling and species permutation preserve the relevant root count; an arbitrary coefficient matrix need not be chemically realizable.

## Primary sources inspected

1. Murad Banaji and Elisenda Feliu, *Positive equilibria in mass action networks: geometry and bounds*, Journal of Mathematical Biology **93**, article 37 (2026), DOI [10.1007/s00285-026-02429-8](https://link.springer.com/article/10.1007/s00285-026-02429-8). Full HTML inspected, especially definitions, Theorem 5.5, Remarks 5.4–5.8. Theorem 5.5 supplies the upper bound four for this target. Remark 5.8 states the authors did not obtain attainment for (3,5,3), while inheritance yields at least three. Remark 5.7 restricts possible extremal source topologies. No conclusion about subsequent literature follows merely from this open-question statement.

2. Murad Banaji, Balazs Boros, Josef Hofbauer, *Bifurcations in planar, quadratic mass-action networks with few reactions and low molecularity*, Nonlinear Dynamics **112**(23), 21425–21448 (2024), DOI [10.1007/s11071-024-10068-1](https://link.springer.com/article/10.1007/s11071-024-10068-1); [arXiv:2406.13451v1](https://arxiv.org/html/2406.13451v1), 19 June 2024. Full HTML inspected around Theorem 12, Theorem 18/Lemma 20, and Remark 38. The closest explicit construction is X+Y→X→0→5X+Y, 2Y→X+4Y. Remark 38 gives this network, without numerical rate constants. Generic cusp exclusion does not preclude three positive equilibria.

3. Murad Banaji, *On the computation of fold and cusp bifurcations in mass action networks via dual equations*, [arXiv:2609.07265v1](https://arxiv.org/html/2609.07265v1), 7 September 2026. Full-text relevant results and closing discussion inspected. Proposition 33 discusses few-reaction full-rank bifurcation restrictions; its following discussion still points to the planar three-equilibrium example. I found no four-equilibrium (3,5,3) construction in this paper. The author's [publication list](https://muradbanaji.github.io/publications/) was also checked for a newer directly relevant work.

4. Boulos El Hilany, *Characterization of circuits supporting polynomial systems with the maximal number of positive solutions*, Discrete & Computational Geometry **58**(2), 355–370 (2017), DOI [10.1007/s00454-017-9897-4](https://doi.org/10.1007/s00454-017-9897-4); [arXiv:1603.01813v1 PDF](https://arxiv.org/pdf/1603.01813), 6 March 2016, 13 pages. Theorem 1.1 characterizes circuit supports admitting n+1 positive solutions for unrestricted real coefficient matrices through inequalities on affine relation coefficients. This does not impose CRN product/nonnegative-production constraints.

5. Frederic Bihan, Alicia Dickenstein, Jens Forsgard, *Optimal Descartes’ rule of signs for systems supported on circuits*, Mathematische Annalen **381**, 1283–1307 (2021), DOI [10.1007/s00208-021-02216-4](https://link.springer.com/article/10.1007/s00208-021-02216-4); [arXiv:2010.09165v2 PDF](https://arxiv.org/pdf/2010.09165), 25 May 2022, 21 pages. Definitions 2.1–2.3 and Theorem 2.4 were inspected. The positive-root bound is one plus the sign variation of partial sums of affine-relation coefficients, ordered by coefficient-kernel Gale rows. Collinear rows must be grouped. Maximal positive circuits and Gale reduction are established methods, not novel contributions of this project.

6. Frederic Bihan, *Maximally positive polynomial systems supported on circuits*, Journal of Symbolic Computation **68**, 61–74 (2015), DOI [10.1016/j.jsc.2014.09.003](https://www.sciencedirect.com/science/article/pii/S0747717114000716). Abstract and sections 3.2–3.3 available text inspected. The primitive affine-relation coefficient pattern with magnitudes one/two and the associated maximally positive circuit problem are prior art. A chemically admissible realization is a separate restriction.

7. Kaitlyn Phillipson and J. Maurice Rojas, *Fewnomial systems with many roots, and an Adelic Tau Conjecture*, Contemporary Mathematics **605**, 45–71 (2013), DOI [10.1090/conm/605/12111](https://doi.org/10.1090/conm/605/12111). Inspected [arXiv:1011.4128v5](https://arxiv.org/pdf/1011.4128), 6 November 2012, 23 pages; original preprint 18 November 2010. Theorem 1.6 (p. 3), its proof (p. 14), and Lemma 1.8 (pp. 3, 14–15) provide an explicit quadratic chain supported on n+2 monomials, with exactly n+1 positive nondegenerate roots at epsilon=1/4. Reversing variable order gives precisely the support of the present all-dimensional reaction chain. Their real-root proof also uses a reciprocal relation and alternating signs. This is the closest algebraic prior art and should be prominently credited. The primary abstract/PDF supplies author/title/version; published volume/pages/DOI also cross-checked in a SIAM journal reference list. The originating 2026 full HTML contains no occurrence of “Phillipson”.

Provenance timing: the Banaji–Feliu version-of-record page gives receipt 27 October 2025, revision 10 June 2026, acceptance 21 June 2026, publication 17 August 2026. The Banaji follow-up preprint was submitted 7 September 2026. This audit was performed on 4 October 2026; neither current status nor priority can be inferred from the older source's open-question wording alone.

## Exact prior-example reconstruction

Using reaction order X+Y→X, X→0, 0→5X+Y, 2Y→X+4Y, the source matrix is S=((1,1,0,0),(1,0,0,2)) and Gamma=((0,-1,5,1),(-1,0,1,2)). The steady-state eliminant is

    k1*k4*y^3 - 2*k2*k4*y^2 + 5*k1*k3*y - k2*k3.

Independent exact calculation gives a rational positive control k=(1,199/100,1,1). The monic cubic is y^3-(199/50)y^2+5y-199/100, with discriminant 429723/6250000>0. All three roots are positive because all roots are real and p(-y)<0 for y>=0. The Jacobian determinant at a steady state is p'(y), hence nonzero. More generally k=(1,a,1,1) has discriminant -(a-2)*(a+2)*(32*a^2-125), positive when sqrt(125/32)<a<2.

## Source caveat

The 2026 HTML Remark 5.6 says quadratic rank-one networks forbid multiple positive nondegenerate equilibria. That wording conflicts with BBH2024 Theorem 18/Lemma 20 and the elementary example 0→X, X→0, 2X→3X. BBH2024 Corollary 19 makes that exclusion for **bimolecular** networks. Do not rely on Remark 5.6 without checking the version-of-record PDF or seeking clarification. This does not affect the independent quartic construction or the separately stated target question.

## Fingerprints and candidate-family rerun

The exact support universe is {0,X,Y,Z,2X,2Y,2Z,X+Y,X+Z,Y+Z}. Independent SymPy enumeration of its 252 five-element subsets found 12 full-affine-rank supports with primitive affine-relation degree four, in two species-permutation orbits:

* (0,X,2Y,X+Z,Y+Z), b=(-1,2,-1,-2,2).
* (X,Y,2X,2Z,Y+Z), b=(2,-2,-1,-1,2).

For the coefficient multiset {2,2,-2,-1,-1}, the only order permitting three sign changes of nonfinal partial sums, up to overall sign/reversal and exchange of identical entries, is (-1,2,-2,2,-1). Its partial sums are (-1,1,-1,1,0).

The parent supplied the candidate family

    0→N(N-1)X+Y+(N-1)Z; X→0; 2Y→3Y; X+Z→2X; Y+Z→2Z
    k=(1/N,N,N/K,1,1/N).

Its claimed eliminant is P=(t+1)^2*(t+N^2)^2-K*t*(t+N)^2. This audit independently expanded that expression and identified the scaled reciprocal symmetry t↔N^2/t. Three exact fingerprints (descending polynomial coefficients) are:

| N | K | Coefficients |
|---|---|---|
| 6 | 4801/48 | (1,-1249/48,963/4,-3747/4,1296) |
| 7 | 145 | (1,-45,568,-2205,2401) |
| 8 | 200 | (1,-70,1153,-4480,4096) |

For N=7,K=145, P/t^2=q^2-45q+470 with q=t+49/t; both q-roots (45±sqrt(145))/2 exceed 14. The quartic-solving device is classical reciprocal-polynomial algebra. This audit is not the network proof review; the parent/independent reviewer must verify the ODE-to-eliminant map and Jacobian.

The rational fingerprint is F_N(t)=(t+1)^2*(t+N^2)^2/[t*(t+N)^2]. For an ordinary-series fingerprint, t*F_7(t) after t=7u is ((7u+1)^2*(u+7)^2)/(u+1)^2, numerator coefficients (49,700,2598,700,49) in ascending order and primitive denominator (1,2,1). Its first twelve coefficients are (49,602,1345,-2592,3888,-5184,6480,-7776,9072,-10368,11664,-12960). From index five onward they satisfy c_j+2c_(j-1)+c_(j-2)=0; the tail is an elementary alternating arithmetic progression and is not itself a distinct novelty claim.

## Search query log

All queries were executed on 2026-10-04 through web search. These are bounded keyword/formula searches, not exhaustive scholarly-database citation exports.

| Family | Exact queries | Outcome |
|---|---|---|
| Origin and status | `"quadratic" "(3,5,3)" equilibria`; `"Positive equilibria in mass action networks" "four"`; `"Banaji" "Remark 38"` | Originating paper and BBH2024 located. |
| Count aliases | `"three species" "five reactions" "four" equilibria`; `"quadratic" "four positive" "equilibria" Banaji`; `"four" "steady states" "five reactions"`; `"four positive equilibria" "quadratic" chemical`; `"four positive steady states" "quadratic"` | No matching target resolution found; some higher-dimensional/higher-reaction biochemical models and unrelated dynamical systems returned. |
| Current author work | `"Banaji" "equilibria" "2026" "bounds"` | September 2026 dual-equation follow-up located and inspected. |
| Sparse algebra alias | `"five monomials" "positive solutions" circuit quadratic`; `"Descartes" "chemical" "circuits" Bihan`; `"Characterization of circuits" "maximal number" positive solutions`; `"Optimal Descartes" circuits Bihan Forsgard 2021`; `"Maximally positive polynomial systems supported on circuits" quadratic` | Circuit-characterization and optimal Descartes literature located; establishes methodological prior art. |
| Support and relation | `"mass action" "X+Z" "Y+Z" "2Y" "equilibria"`; `"positive" "circuits" "1, 2, -2, 2, -1"`; `"quadratic" "0, 1" "maximally positive"`; `"three" "quadratic" "chemical" "maximally positive"` | No exact chemically admissible construction found. |
| Candidate exact formula | `"(t+1)" "(t+49)" "145" polynomial`; `"2205" "2401" "568" polynomial`; `"t^4" "45t^3" "2401"`; `"2205" "2401" "145" "equilibria"` | No relevant exact-formula collision found. |
| Candidate network | `"42X" "6Z" reaction equilibria`; `"42 X" "6 Z" "mass"`; `"five-reaction" "four" equilibria`; `"mass action" "four" "equilibria" "7"` | No candidate network collision found. |
| Broader sharpness | `"(n,n+2,n)" "sharp"`; `"quadratic" "n+2" "n+1" "sharp" chemical`; `"quadratic mass action" "four" "positive" equilibria 2026` | Original question/relevant earlier literature returned; no general quadratic-CRN attainment result found. |
| Reciprocal alias | `"reciprocal quartic" "positive roots" chemical`; `"mass action" "sqrt" "reciprocal"` | Reciprocal quartic reduction is classical; returned chemistry uses were not the target network. |
| Sequence/OEIS | `"49, 602, 1345" "2592"`; `"49,602,1345" site:oeis.org`; `"2592, 3888, 5184, 6480, 7776" site:oeis.org` | No matching OEIS result found through indexed web search. Direct exhaustive OEIS/API lookup was not performed. |
| General-dimension rerun | `"quadratic" "networks" "n+1" "equilibria"`; `"mass-action" "n+2" "positive solutions" sharp`; `"mass action" "equilibria" "bound" "attained"`; `"quadratic" "chemical reaction" "arbitrary" "equilibria"`; `"reaction" "maximally positive"`; `"chemical" "circuits" "n+1" "positive solutions"`; `"quadratic" "Gale" "chain" "equilibria"`; `"mass action" "sharpness" "all" "dimensions"`; `"Characterization of circuits" "chemical reaction"`; `"n+1 positive" "quadratic" "reaction"`; `"sharpness" "quadratic" "mass-action"` | No all-dimensional chemical construction located; redirected to explicit fewnomial constructions. |
| Algebraic backward chain | `"Bihan" "Maximally positive" "pdf"`; `"Maximally positive polynomial systems" "arxiv"`; `"Phillipson" "Rojas" "Fewnomial systems with many roots" arxiv` | Bihan's discussion identified Phillipson–Rojas as the explicit maximal-root chain. Direct full-PDF inspection confirmed the same support. |
| Chemical bridge collision check | `"Phillipson" "Rojas" "chemical"`; `"Fewnomial Systems with Many Roots" "mass"`; `"mass action" "Phillipson"`; `"quadratic" "equilibria" "Phillipson"`; `"15" "16" "Phillipson" "Rojas"`; `"mass action" "n+1" "Phillipson"`; `"Fewnomial systems with many roots" "reaction network"`; `"240X" "15Y" equilibria` | No matching chemical realization found. A 2014 REU abstract about binomial-system CRN applications appeared, but it is not this chain/claim. |

Cross-domain aliases considered: sparse polynomial/circuit systems and Gale duality (algebraic geometry); signed matroids and positive circuits (combinatorics); kinetic polynomial realization (chemical physics); toric/monomial model intersections and feasibility (optimization/statistics); deterministic mean-field stationary states versus stationary distributions (probability). These last stochastic objects are not identified with deterministic equilibria and no stochastic claim is made. No harmonic-analysis/representation-theory identity was suggested by the formulas; the reciprocal polynomial is the only simpler classical alias found.

## Adjudication and limits

* **Chemical existence statement / explicit realization:** BOUNDED UNCERTAINTY; no earlier matching construction found in inspected primary sources and recorded queries. Permitted: “This construction attains the bound asked about in Remark 5.8.” Avoid “first-ever” or “proved historically novel.”
* **Gale reduction, circuit constraints, scalar root counting:** COLLISION with established methods; cite the relevant sources when used. No method novelty claim.
* **Classical reciprocal quartic reduction:** established elementary algebra; no novelty claim.
* **Exact computational certificate/replay:** local contribution, subject to independent verification elsewhere in the project.
* **All-dimensional quadratic chain and alternating-product reduction:** EXACT PRIOR-ART COLLISION with Phillipson–Rojas (2013), Theorem 1.6/Lemma 1.8. The explicit reaction realization below is derived here from those equations; cite their theorem rather than describe arbitrary quadratic n+1-root attainment as new.
* **All-dimensional chemical sharpness conclusion:** BOUNDED UNCERTAINTY; no earlier chemical-realization result located. Permitted: “A mass-action realization of the Phillipson–Rojas extremal chain attains the upper bound in every dimension.” Claiming the first quadratic polynomial chain or first alternating-product proof would be false.

Missingness: no author enquiry was made or authorized; no exhaustive MathSciNet/zbMATH/Scopus/WoS citation search; no non-English full-text sweep; not all cited supplementary notebooks were inspected; web indexing may lag. Source HTML/PDF was inspected through the browsing tool. A sandboxed curl attempt could not resolve arxiv.org, so this audit did not retain or hash local PDF bytes and does not claim a source-archive certificate.

The required novelty-gate worked failure case was read. The all-dimensional rerun above found a substantial collision that changed the attribution. Rerun this audit if the work claims product-molecularity minimality, bifurcation/stability novelty, or another reduced normal form.

## Independently derived chemical bridge to the prior polynomial chain

This section records a new calculation in the audit, not a claim made by Phillipson–Rojas. Fix n>=2. Define s_i=16^(n-i)/4 for 1<=i<=n, s_(n+1)=0, and B_i=4(s_i-s_(i+1)). Thus B_i=15*16^(n-i-1) for i<n and B_n=1. The network is

    0 -> sum_i B_i X_i,             rate 1/4;
    X_1 -> 0,                       rate s_1;
    X_i+X_(i+1) -> 2X_i (i<n),       rate s_(i+1) if i<n-1, and 1 if i=n-1;
    2X_n -> 3X_n,                    rate 1.

Let u=x_n^2, v_1=s_1*x_1, v_i=s_i*x_(i-1)*x_i for 2<=i<n, and v_n=x_(n-1)*x_n. Its vectorfield has components f_i=s_i-s_(i+1)-v_i+v_(i+1) for i<n and f_n=s_n-v_n+u. Define g_i=v_i-s_i-u. Then f_i=-g_i+g_(i+1) for i<n, f_n=-g_n: an invertible constant row transformation with determinant (-1)^n. After dividing rows by their positive rates, g=0 is the reverse-variable Phillipson–Rojas system. Consequently its positive root count and nonsingular Jacobians carry over exactly. The reaction vectors -e_1, e_i-e_(i+1) span R^n, so stoichiometric rank is n. All sources are quadratic and all products have nonnegative integer coefficients. Total inflow product molecularity is 16^(n-1).

Exact symbolic spot-checks n=2,...,8 verified f_i=-g_i+g_(i+1), positive integer B_i, and the rate formula. These are checks of the general displayed identity, not substitutes for its proof.

The fuller derivation is distributed in `supplement/phillipson-rojas-bridge.md`; a second exact symbolic calculation for n=2,...,12 checked the scaled reversed source equations directly. Journal metadata was also cross-checked against [Rojas's author publication list](https://people.tamu.edu/~rojas/cvpub.pdf). Additional metadata queries were `site.ams.org "Fewnomial systems with many roots" "12111"` and `site.math.tamu.edu "Fewnomial systems with many roots" "605"`. Direct DOI resolution through the browser returned an internal error; the DOI string is independently present in a SIAM primary-paper reference list.

| n | Inflow product B | Rates in displayed reaction order |
|---|---|---|
| 2 | (15,1) | (1/4,4,1,1) |
| 3 | (240,15,1) | (1/4,64,4,1,1) |
| 4 | (3840,240,15,1) | (1/4,1024,64,4,1,1) |

For n=1, the elementary separate network 0->X, X->0, 2X->3X at rates (2,3,1) has xdot=(x-1)(x-2), hence two positive simple equilibria. Its elementary status must not be framed as new.
