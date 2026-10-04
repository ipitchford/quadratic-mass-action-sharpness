#!/usr/bin/env python3
"""Independent referee checks, 4 October 2026.

No imports from the submitted verifier and no reading of examples.json.
Networks are entered from the displayed reactions; finite checks supplement,
not replace, the analytic all-dimensional proof. SymPy is a shared CAS
backend, so this is independent implementation, not formal verification.
"""
from __future__ import annotations
import hashlib, itertools, json, math, platform, time, sys
from collections import Counter
from fractions import Fraction
from pathlib import Path
import sympy as s

START=time.perf_counter()
HERE=Path(__file__).resolve().parent
COUNT=0
RESULT={"review_date":"2026-10-04","python":platform.python_version(),"sympy":s.__version__,"method":"independently entered reaction data and original checker; common SymPy backend", "checks":{}}

def check(test, label):
    global COUNT
    COUNT+=1
    if not bool(test): raise RuntimeError(label)

def zero(expr, label):
    check(s.cancel(expr)==0,label)

def network(xs,reactions):
    """Reaction tuples are (source, product, rate)."""
    gamma=s.Matrix.hstack(*(s.Matrix(b)-s.Matrix(a) for a,b,k in reactions))
    flux=s.Matrix([k*s.prod(z**e for z,e in zip(xs,a)) for a,b,k in reactions])
    return gamma,gamma*flux

x,y,z,t,N,K=s.symbols('x y z t N K',positive=True)
xs=s.Matrix([x,y,z])
# Proposition 1, symbolic in N and K.
A=[((0,0,0),(N*(N-1),1,N-1),1/N),
   ((1,0,0),(0,0,0),N),((0,2,0),(0,3,0),N/K),
   ((1,0,1),(2,0,0),s.Integer(1)),((0,1,1),(0,0,2),1/N)]
GA,fa=network(xs,A)
phiA={x:(t+1)/t,y:(t+1)*(t+N**2)/(t*(t+N)),z:(t+N)/(t+1)}
P=(t+1)**2*(t+N**2)**2-K*t*(t+N)**2
resA=fa.subs(phiA)
zero(resA[0],'A first balance');zero(resA[2],'A third balance')
zero(resA[1]-N*P/(K*t**2*(t+N)**2),'A residual polynomial')
FA=(t+1)**2*(t+N**2)**2/(t*(t+N)**2)
JrawA=fa.jacobian(xs)
JA=JrawA.subs(phiA)
detA=s.factor(JrawA.det()).subs(phiA)
zero((detA+s.diff(P,t)/(K*t*(t+N))).subs(K,FA),'A on-shell determinant')
zero(t**4/N**4*P.subs(t,N**2/t)-P,'A reciprocal symmetry')
check(GA[:,[1,2,3]].det()!=0,'A rank minor')
P7=s.Poly(P.subs({N:7,K:145}),t)
check(P7.all_coeffs()==[1,-45,568,-2205,2401],'A quartic from reactions')
check(P7.count_roots(0,s.oo)==4,'A positive root count')
check(s.gcd(P7,P7.diff()).degree()==0,'A squarefree')
bracketsA=[(1,2),(3,4),(12,13),(26,27)]
valsA=[]
for a,b in bracketsA:
    av,bv=P7.eval(a),P7.eval(b);check(av*bv<0,'A bracket')
    valsA.append([a,b,str(av),str(bv)])
print('completed: reciprocal_family', file=sys.stderr, flush=True)
RESULT['checks']['reciprocal_family']={'symbolic_parameters':'N,K','positive_roots_example':4,'endpoint_values':valsA,'jacobian_identity':'verified exactly on P=0','rank_minor':str(GA[:,[1,2,3]].det())}

# Stability claim appears in submitted internal derivation note, not the main paper.
# Recompute coefficients from the original vector field, then check its inequalities.
J7=JA.subs(N,7).subs(K,FA.subs(N,7))
lam=s.symbols('lambda')
cfs=[s.factor(v.subs(phiA).subs(N,7).subs(K,FA.subs(N,7))) for v in JrawA.charpoly(lam).all_coeffs()]
a,b,c=cfs[1:]
a_expected=(49*t**3+2623*t**2+14363*t-2107)/(7*(t+1)*(t+7)*(t+49))
b_expected=2*(25*t**5+1031*t**4+2941*t**3+8785*t**2+21854*t+9604)/(7*t*(t+1)**2*(t+7)*(t+49))
c_expected=(t-7)*(t**2-22*t+49)/(t*(t+49)*(t+1))
for got,want in zip((a,b,c),(a_expected,b_expected,c_expected)):zero(got-want,'A stability coefficient')
# Positive polynomial coefficients after t=u+1 prove positivity for t>1.
u=s.symbols('u')
for expr in (a,b,a*b-c):
    num,den=s.fraction(s.cancel(expr))
    for part in (num,den):
        cf=s.Poly(s.expand(part.subs(t,u+1)),u).all_coeffs()
        check(all(v>0 for v in cf),'A Routh-Hurwitz positivity for t>1')
# c = -det(J), whose sign at each root follows the monic simple quartic's
# alternating derivatives: (-,+,-,+). All four root intervals lie above 1.
print('completed: reciprocal_stability', file=sys.stderr, flush=True)
RESULT['checks']['reciprocal_stability']={'a_b_ab_minus_c_positive_for':'t>1, proved by positive coefficients after t=u+1','constant_term_signs_in_root_order':[-1,1,-1,1],'classification':['index-one saddle','sink','index-one saddle','sink'],'scope':'local stability only, not a global phase portrait'}

# Inflow-free network, general terminal rate 1/K.
B=[((1,0,0),(0,0,0),s.Integer(1)),
   ((0,1,0),(6,0,4),s.Integer(1)),((2,0,0),(0,6,4),s.Integer(1)),
   ((0,0,2),(0,4,0),1/K),((0,1,1),(0,0,0),s.Integer(1))]
GB,fb=network(xs,B)
phiB={x:(5-t)/(2*(7*t+1)),y:(5-t)*(t+1)/(2*(7*t+1)**2),z:14/(t+1)}
flux_shape=s.Matrix([2*(7*t+1),2*(t+1),5-t,2*t,28])
check(GB*flux_shape==s.zeros(3,1),'B kernel parameterization')
check(GB.rank()==3,'B full rank')
R=392*(7*t+1)**2/(t*(5-t)*(t+1)**2)
Dexpected=392*(t-1)*(2*t-1)*(7*t-5)*(7*t+1)/(t**2*(t-5)**2*(t+1)**3)
zero(s.diff(R,t)-Dexpected,'B exact rate curve derivative')
check(R.subs(t,s.Rational(1,2))==1568,'B first minimum')
check(R.subs(t,1)==1568,'B second minimum')
check(R.subs(t,s.Rational(5,7))==s.Rational(117649,75),'B maximum')
Q=s.Poly(3137*t*(5-t)*(t+1)**2-784*(7*t+1)**2,t)
fB0=fb.subs(K,s.Rational(3137,2))
DB=3137*(t+1)**2*(7*t+1)**2
resB=fB0.subs(phiB)
for i,goal in enumerate((0,-2*Q.as_expr()/DB,Q.as_expr()/DB)):zero(resB[i]-goal,'B reconstructed residual')
JB=fB0.jacobian(xs).subs(phiB)
detB=s.factor(fB0.jacobian(xs).det()).subs(phiB)
main_det=(5-t)*Q.diff().as_expr()/(6274*(t+1)*(7*t+1)**2)
remainder=2*(t-5)*(7*t+4)*Q.as_expr()/(3137*(t+1)**2*(7*t+1)**3)
zero(detB-main_det-remainder,'B full off-shell determinant identity')
check(Q.count_roots(0,5)==4,'B four roots in allowed domain')
check(s.gcd(Q,Q.diff()).degree()==0,'B squarefree')
points=[s.Integer(0),s.Rational(1,2),s.Rational(5,7),s.Integer(1),s.Integer(5)]
values=[Q.eval(v) for v in points]
check(all(values[i]*values[i+1]<0 for i in range(4)),'B four rational sign brackets')
lo=s.Integer(1568);hi=s.Rational(117649,75)
print('completed: inflow_free', file=sys.stderr, flush=True)
RESULT['checks']['inflow_free']={'rate_window_K':['1568','117649/75'],'rate_convention':'fourth rate is 1/K; supplied example K=3137/2','absolute_width':str(hi-lo),'relative_width_to_lower_endpoint':str((hi-lo)/lo),'Q_coefficients':[str(v) for v in Q.all_coeffs()],'points':[str(v) for v in points],'values':[str(v) for v in values],'off_shell_determinant_identity':'verified','positive_roots':4}

# Independent construction of original Phillipson--Rojas equations and
# chemical vector fields. Test dimension 2 boundary separately in same loop.
bridge_dims=[];scale_dims=[]
for n in range(2,13):
    yy=s.symbols('y1:'+str(n+1))
    zz=list(reversed(yy))
    def chemical(r):
        d=[s.Integer(r)**(2*n-2*i-1) for i in range(1,n)]+[s.Rational(1,r)]
        bi=[r*(d[i]-d[i+1]) for i in range(n-1)]+[s.Integer(1)]
        zero_v=(0,)*n
        out=[0]*n;out[0]=1
        rx=[(zero_v,tuple(bi),s.Rational(1,r)),(tuple(out),zero_v,d[0])]
        for i in range(n-1):
            src=[0]*n;src[i]=src[i+1]=1
            prod=[0]*n;prod[i]=2
            rate=d[i+1] if i<n-2 else s.Integer(1)
            rx.append((tuple(src),tuple(prod),rate))
        src=[0]*n;prod=[0]*n;src[-1]=2;prod[-1]=3
        rx.append((tuple(src),tuple(prod),s.Integer(1)))
        _,ff=network(yy,rx)
        return ff,d
    f4,d4=chemical(4)
    eps=s.Rational(1,4)
    orig=[zz[0]*zz[1]-eps-zz[0]**2]
    for j in range(2,n):orig.append(zz[j-1]*zz[j]-1-eps**(2*j-3)*zz[0]**2)
    orig.append(zz[n-1]-1-eps**(2*n-3)*zz[0]**2)
    GG=[d4[i]*orig[n-1-i] for i in range(n-1)]+[orig[0]]
    expected=s.Matrix([GG[i+1]-GG[i] for i in range(n-1)]+[-GG[-1]])
    for e in f4-expected:zero(e,'PR original equations to reaction vector field')
    bridge_dims.append(n)
    # The main paper's R=25 construction is the r=5 realization up to
    # positive diagonal coordinate scaling and common equation factor 5^3.
    f5,_=chemical(5)
    ee=[(2*n-i+1 if i%2 else -i) for i in range(1,n)]
    ee.append(n+2 if n%2 else 1-n)
    xx=[s.Integer(5)**e*yv for e,yv in zip(ee,yy)]
    ss=[s.Integer(25)**(n+1-i) for i in range(1,n+1)]+[s.Integer(0)]
    vv=[xx[0]]+[xx[i-1]*xx[i] for i in range(1,n)]+[s.Integer(5)**((-1)**n*(2*n+1))*xx[-1]**2]
    for i in range(n):zero(ss[i]-ss[i+1]-vv[i]+vv[i+1]-125*f5[i],'R25 to PR-family scaling')
    scale_dims.append(n)
print('completed: prior_family_translation', file=sys.stderr, flush=True)
RESULT['checks']['prior_family_translation']={'original_PR_equations_to_chemical_vector_field_dimensions':bridge_dims,'main_R25_to_PR_r5_dimensions':scale_dims,'note':'finite identity checks corroborate the symbolic all-dimensional formula; no stability equivalence asserted'}

# Exact finite checks independent of symbolic expression construction.
# Compare positive integer products after cross-multiplication, no floats.
sign_count=0
for n in range(2,51):
    k=Fraction(5)**(((-1)**n)*(2*n+1))
    for j in range(n+2):
        tj=25**j
        numer=math.prod((tj+25**r)**2 for r in range(1,n+1,2))
        denom=tj*math.prod((tj+25**r)**2 for r in range(2,n+1,2))
        diff=k.numerator*numer-k.denominator*denom
        check((diff>0)==(j%2==0) and diff!=0,'general integer sign')
        sign_count+=1
print('completed: integer_sign_spot_checks', file=sys.stderr, flush=True)
RESULT['checks']['integer_sign_spot_checks']={'dimensions':[2,50],'endpoint_comparisons':sign_count,'method':'integer cross multiplication; no CAS and no floating point','uniform_proof':'the analytic correction-factor bound, not these finite tests'}

# All choose(10,5) supports, by signed maximal minors rather than nullspace.
monomials=[(0,0,0),(1,0,0),(0,1,0),(0,0,1),(2,0,0),(0,2,0),(0,0,2),(1,1,0),(1,0,1),(0,1,1)]
degrees=Counter();quartics=[]
for support in itertools.combinations(monomials,5):
    aug=s.Matrix([[1]*5]+[[a[i] for a in support] for i in range(3)])
    w=[(-1)**j*int(aug[:,[i for i in range(5) if i!=j]].det()) for j in range(5)]
    if not any(w):degrees['affinely deficient']+=1;continue
    gcd=math.gcd(*w);w=[v//gcd for v in w]
    check(aug*s.Matrix(w)==s.zeros(4,1),'cofactor affine relation')
    degree=sum(v for v in w if v>0);degrees[str(degree)]+=1
    if degree==4:quartics.append(support)
perms=list(itertools.permutations(range(3)))
def canonical(support):return min(tuple(sorted(tuple(a[p] for p in perm) for a in support)) for perm in perms)
orbits=Counter(canonical(q) for q in quartics)
check(dict(degrees)=={'affinely deficient':24,'2':156,'3':60,'4':12},'support degree counts')
check(sorted(orbits.values())==[6,6],'two support orbits')
print('completed: support_enumeration', file=sys.stderr, flush=True)
RESULT['checks']['support_enumeration']={'number':math.comb(10,5),'degree_counts':dict(degrees),'quartic_orbit_sizes':sorted(orbits.values()),'method':'signed 4x4 cofactors; gcd primitive relation; S3 canonicalization','scope':'source supports only, not full reaction networks or molecularity optimum'}

RESULT['status']='PASS'
RESULT['reported_check_invocations']=COUNT
RESULT['runtime_seconds']=round(time.perf_counter()-START,3)
archive_name='quadratic-five-reaction-proof-package.zip'
archive=next((q for q in (HERE/archive_name,HERE.parent/archive_name) if q.is_file()),None)
RESULT['source_zip_sha256']=hashlib.sha256(archive.read_bytes()).hexdigest() if archive else None
RESULT['archive_hash_scope']='Original archive located and hashed' if archive else 'Original archive absent; mathematical checks require no source files'
RESULT['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
print(json.dumps(RESULT,indent=2,sort_keys=True))
