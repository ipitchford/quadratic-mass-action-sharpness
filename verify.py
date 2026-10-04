#!/usr/bin/env python3
"""Exact checks. The all-dimensional theorem is proved in paper.tex, not by this finite run.

Run: python3 verify.py --data examples.json --negative-controls
Requires Python 3.10+ and SymPy 1.14.0. No assert statements are used.

Supplementary translation, rate-window and stability checks incorporate the
formulas and checking approach in the supplied 4 October 2026 referee audit
(reviewer_independent_checks.py and ADDITIONAL_VERIFIED_RESULTS.md). Both use
SymPy: this distributed verifier is not an independent algebra engine or a
proof-assistant formalisation.
"""
import argparse
import copy
import json
import platform
from pathlib import Path
import sympy as S

COUNT = 0

def require(condition, message):
    global COUNT
    COUNT += 1
    if not condition:
        raise ValueError(message)

def zero(expr, message):
    require(S.cancel(expr) == 0, message)

def check_example(d):
    t,x,y,z = S.symbols('t x y z')
    local = dict(t=t,x=x,y=y,z=z)
    src,prod = S.Matrix(d['source']),S.Matrix(d['product'])
    rates = [S.Rational(v) for v in d['rates']]
    require(src.shape == prod.shape == (3,5), 'three species and five reactions')
    require(all(v.is_Integer and v>=0 for v in list(src)+list(prod)), 'nonnegative integer complexes')
    require(all(sum(src[:,j])<=2 for j in range(5)), 'quadratic sources')
    require(all(src[:,j]!=prod[:,j] for j in range(5)), 'nontrivial reactions')
    require(all(k>0 for k in rates), 'positive rate constants')
    gamma=prod-src
    require(gamma.rank()==3, 'rank three')
    mon=S.Matrix([S.prod(v**src[i,j] for i,v in enumerate((x,y,z))) for j in range(5)])
    f=gamma*S.diag(*rates)*mon
    P=S.Poly.from_list([S.Rational(c) for c in d['polynomial_descending']],t).as_expr()
    require(S.degree(P,t)==4, 'quartic degree')
    require(S.gcd(P,S.diff(P,t))==1, 'quartic squarefree')
    phi={v:S.sympify(expr,locals=local) for v,expr in zip((x,y,z),d['equilibrium_map'])}
    expected=[S.sympify(expr,locals={**local,'P':P}) for expr in d['residuals']]
    for a,b in zip(f,expected): zero(a.subs(phi)-b,'ODE residual identity')
    points=[S.Rational(v) for v in d['test_points']]
    values=[P.subs(t,v) for v in points]
    require([int(S.sign(v)) for v in values]==d['expected_signs'],'exact root brackets')
    det=f.jacobian((x,y,z)).det().subs(phi)
    expected_det=S.sympify(d['det_at_root'],locals={**local,'Pprime':S.diff(P,t)})
    numerator,denominator=S.fraction(S.cancel(det-expected_det))
    require(S.rem(numerator,P,t)==0,'Jacobian certificate modulo quartic')
    # Maps and determinant denominators have no zeros inside the domain.
    lo,hi=map(S.sympify,d['domain'])
    for expression in list(phi.values())+[expected_det/S.diff(P,t)]:
        den=S.fraction(S.cancel(expression))[1]
        roots=S.Poly(den,t).intervals()
        require(all(not (lo < b and a < hi) for (a,b),mult in roots),'no denominator zero in domain')
    require(S.Poly(P,t).count_roots(lo,hi)==4,'independent Sturm root count')
    return {'name':d['name'],'rank':3,'roots':4,'polynomial':str(P),
            'exact_test_values':[str(v) for v in values],
            'jacobian_identity':'PASS','max_product_molecularity':max(map(int,[sum(prod[:,j]) for j in range(5)]))}

def check_dimension(n,R=25):
    require(n>=2,'dimension at least two')
    q=S.sqrt(R)
    require(q.is_Integer,'square geometric ratio')
    shifts=[R**(n-i) for i in range(n)]+[0]
    a=[shifts[i]-shifts[i+1] for i in range(n)]
    rate=q**((-1)**n*(2*n+1)); C=1/rate
    source=S.zeros(n,n+2); product=S.zeros(n,n+2)
    product[:,0]=S.Matrix(a); source[0,1]=1
    for i in range(n-1):
        source[i,i+2]=source[i+1,i+2]=1; product[i,i+2]=2
    source[-1,-1]=2; product[-1,-1]=3
    gamma=product-source
    require(all(v>=0 and v.is_Integer for v in product),'integer product complexes')
    require(all(sum(source[:,j])<=2 for j in range(n+2)),'quadratic general sources')
    require(len(set(tuple(source[:,j]) for j in range(n+2)))==n+2,'distinct sources')
    require(abs(gamma[:,1:n+1].det())==1,'unimodular rank certificate')
    t=S.Symbol('t')
    p=S.prod((t+R**r)**2 for r in range(1,n+1,2))-C*t*S.prod((t+R**r)**2 for r in range(2,n+1,2))
    P=S.Poly(p,t)
    require(P.degree()==n+1,'general polynomial degree')
    require(S.gcd(P,P.diff()).degree()==0,'general polynomial squarefree')
    signs=[]
    for j in range(n+2):
        test=S.Integer(R)**j
        H=S.prod((test+R**r)**(2*(-1)**(r-1)) for r in range(1,n+1))/test
        signs.append(int(S.sign(H-C)))
        require(signs[-1]==(-1)**j,'general exact alternating signs')
        u=[test+s for s in shifts[:-1]]; x=[u[0]]
        for i in range(1,n): x.append(u[i]/x[-1])
        f=list(gamma*S.Matrix([1]+u+[rate*x[-1]**2]))
        require(all(v==0 for v in f[:-1]),'general telescoping balances')
        zero(f[-1]-rate*test*(H-C),'general terminal residual')
    return {'dimension':n,'rank':n,'reactions':n+2,'simple_positive_roots':n+1,'signs':signs}

def reaction_field(variables, reactions):
    """Build a vector field from separately entered (source, product, rate) data."""
    gamma = S.Matrix.hstack(*(S.Matrix(b)-S.Matrix(a) for a,b,k in reactions))
    flux = S.Matrix([k*S.prod(x**e for x,e in zip(variables,a))
                     for a,b,k in reactions])
    return gamma, gamma*flux

def prior_family_field(variables, r):
    n=len(variables)
    r=S.Integer(r)
    d=[r**(2*n-2*i-1) for i in range(1,n)]+[1/r]
    inflow=[r*(d[i]-d[i+1]) for i in range(n-1)]+[S.Integer(1)]
    empty=(0,)*n
    first=[0]*n; first[0]=1
    reactions=[(empty,tuple(inflow),1/r),(tuple(first),empty,d[0])]
    for i in range(n-1):
        source=[0]*n; source[i]=source[i+1]=1
        product=[0]*n; product[i]=2
        rate=d[i+1] if i<n-2 else S.Integer(1)
        reactions.append((tuple(source),tuple(product),rate))
    source=[0]*n; source[-1]=2
    product=[0]*n; product[-1]=3
    reactions.append((tuple(source),tuple(product),S.Integer(1)))
    return reaction_field(variables,reactions)[1],d

def check_prior_translation(n, epsilon=S.Rational(1,4)):
    """Corroborate the named realisation proposition, including n=2."""
    variables=S.symbols('y1:'+str(n+1))
    reverse=list(reversed(variables))
    chemical,d=prior_family_field(variables,4)
    original=[reverse[0]*reverse[1]-epsilon-reverse[0]**2]
    original += [reverse[j-1]*reverse[j]-1-epsilon**(2*j-3)*reverse[0]**2
                 for j in range(2,n)]
    original.append(reverse[-1]-1-epsilon**(2*n-3)*reverse[0]**2)
    scaled=[d[i]*original[n-1-i] for i in range(n-1)]+[original[0]]
    transformed=S.Matrix([scaled[i+1]-scaled[i] for i in range(n-1)]
                         +[-scaled[-1]])
    for expr in chemical-transformed:
        zero(expr,'Phillipson-Rojas epsilon=1/4 chemical translation')
    return {'dimension':n,'epsilon':str(epsilon),'coordinate_order':'reversed',
            'identity':'PASS','scope':'equilibria and Jacobian nonsingularity; not stability'}

def check_main_scaling(n, common_factor=125):
    variables=S.symbols('y1:'+str(n+1))
    chemical,_=prior_family_field(variables,5)
    exponents=[2*n-i+1 if i%2 else -i for i in range(1,n)]
    exponents.append(n+2 if n%2 else 1-n)
    x=[S.Integer(5)**e*y for e,y in zip(exponents,variables)]
    shifts=[S.Integer(25)**(n+1-i) for i in range(1,n+1)]+[S.Integer(0)]
    flux=[x[0]]+[x[i-1]*x[i] for i in range(1,n)]
    flux.append(S.Integer(5)**((-1)**n*(2*n+1))*x[-1]**2)
    for i in range(n):
        zero(shifts[i]-shifts[i+1]-flux[i]+flux[i+1]-common_factor*chemical[i],
             'R=25 positive coordinate scaling to prior r=5 family')
    return {'dimension':n,'coordinate_exponents_base_5':exponents,
            'common_equation_factor':common_factor,'identity':'PASS'}

def check_b_rate_family(claimed_derivative=None, claimed_upper=S.Rational(117649,75)):
    x,y,z,t,L=S.symbols('x y z t L')
    reactions=[((1,0,0),(0,0,0),S.Integer(1)),
               ((0,1,0),(6,0,4),S.Integer(1)),
               ((2,0,0),(0,6,4),S.Integer(1)),
               ((0,0,2),(0,4,0),1/L),
               ((0,1,1),(0,0,0),S.Integer(1))]
    gamma,f=reaction_field((x,y,z),reactions)
    flux_shape=S.Matrix([2*(7*t+1),2*(t+1),5-t,2*t,28])
    require(gamma*flux_shape==S.zeros(3,1),'inflow-free parameter flux kernel')
    phi={x:(5-t)/(2*(7*t+1)),y:(5-t)*(t+1)/(2*(7*t+1)**2),z:14/(t+1)}
    Q=L*t*(5-t)*(t+1)**2-392*(7*t+1)**2
    denominator=L*(t+1)**2*(7*t+1)**2
    for actual,expected in zip(f.subs(phi),(0,-2*Q/denominator,Q/denominator)):
        zero(actual-expected,'inflow-free general-rate residual')
    curve=392*(7*t+1)**2/(t*(5-t)*(t+1)**2)
    derivative=392*(t-1)*(2*t-1)*(7*t-5)*(7*t+1)/(t**2*(t-5)**2*(t+1)**3)
    if claimed_derivative is not None:
        derivative=S.sympify(claimed_derivative,locals={'t':t})
    zero(S.diff(curve,t)-derivative,'inflow-free rate-curve derivative')
    lower=S.Integer(1568)
    require(curve.subs(t,S.Rational(1,2))==lower,'inflow-free first minimum')
    require(curve.subs(t,1)==lower,'inflow-free second minimum')
    require(curve.subs(t,S.Rational(5,7))==claimed_upper,'inflow-free intermediate maximum')
    require(S.limit(curve,t,0,dir='+')==S.oo,'inflow-free left endpoint divergence')
    require(S.limit(curve,t,5,dir='-')==S.oo,'inflow-free right endpoint divergence')
    samples=[S.Rational(1,4),S.Rational(3,5),S.Rational(6,7),S.Integer(2)]
    require([int(S.sign(derivative.subs(t,a))) for a in samples]==[-1,1,-1,1],
            'inflow-free rate-curve derivative interval signs')
    zero(Q.subs(L,lower)+392*(2*t-1)**2*(t-1)**2,
         'inflow-free lower endpoint has two double roots')
    upper_poly=S.Poly(Q.subs(L,claimed_upper),t)
    require(S.gcd(upper_poly,upper_poly.diff()).monic()==S.Poly(t-S.Rational(5,7),t),
            'inflow-free upper endpoint has exactly one double root')
    require(upper_poly.count_roots(0,5)==3,'inflow-free upper endpoint distinct positive roots')
    require(lower<S.Rational(3137,2)<claimed_upper,'inflow-free example lies inside exact rate window')
    require(claimed_upper-lower==S.Rational(49,75),'inflow-free exact rate-window width')
    require((claimed_upper-lower)/lower==S.Rational(1,2400),
            'inflow-free relative width of specified rate slice')
    # Check nonsingularity for the whole rate family on its equilibrium curve.
    det=f.jacobian((x,y,z)).det().subs(phi)
    expected_det=(5-t)*S.diff(Q,t)/(2*L*(t+1)*(7*t+1)**2)
    zero((det-expected_det).subs(L,curve),'inflow-free general-rate on-shell determinant')
    return {'fourth_rate':'1/L','four_simple_positive_equilibria_iff':
            [str(lower),str(claimed_upper)],'absolute_width':'49/75',
            'relative_width_to_lower_endpoint':'1/2400','derivative':str(derivative),
            'scope':'one specified rate slice; no full-parameter robustness or cusp claim'}

def positive_after_shift(expr,t):
    """A sufficient exact positivity certificate on t>1, using u=t-1>0."""
    u=S.Symbol('u')
    numerator,denominator=S.fraction(S.cancel(expr))
    for part in (numerator,denominator):
        coefficients=S.Poly(S.expand(part.subs(t,u+1)),u).all_coeffs()
        require(all(v>0 for v in coefficients),'Routh-Hurwitz positive coefficients on t>1')

def check_reciprocal_stability(claimed_a=None):
    x,y,z,t,K,lam=S.symbols('x y z t K lambda')
    reactions=[((0,0,0),(42,1,6),S.Rational(1,7)),
               ((1,0,0),(0,0,0),S.Integer(7)),
               ((0,2,0),(0,3,0),7/K),
               ((1,0,1),(2,0,0),S.Integer(1)),
               ((0,1,1),(0,0,2),S.Rational(1,7))]
    _,f=reaction_field((x,y,z),reactions)
    phi={x:(t+1)/t,y:(t+1)*(t+49)/(t*(t+7)),z:(t+7)/(t+1)}
    curve=(t+1)**2*(t+49)**2/(t*(t+7)**2)
    original_characteristic=f.jacobian((x,y,z)).charpoly(lam)
    coefficients=[S.cancel(v.subs(phi).subs(K,curve))
                  for v in original_characteristic.all_coeffs()]
    require(coefficients[0]==1,'original chemical characteristic polynomial is monic')
    a_expected=(49*t**3+2623*t**2+14363*t-2107)/(7*(t+1)*(t+7)*(t+49))
    if claimed_a is not None:
        a_expected=S.sympify(claimed_a,locals={'t':t})
    b_expected=2*(25*t**5+1031*t**4+2941*t**3+8785*t**2+21854*t+9604)/(7*t*(t+1)**2*(t+7)*(t+49))
    c_expected=(t-7)*(t**2-22*t+49)/(t*(t+49)*(t+1))
    for actual,expected in zip(coefficients[1:],(a_expected,b_expected,c_expected)):
        zero(actual-expected,'original chemical Routh-Hurwitz coefficient identity')
    a,b,c=coefficients[1:]
    for expression in (a,b,a*b-c):
        positive_after_shift(expression,t)
    P=S.Poly((t+1)**2*(t+49)**2-145*t*(t+7)**2,t)
    c_from_derivative=P.diff().as_expr()/(145*t*(t+7))
    numerator=S.fraction(S.cancel(c-c_from_derivative))[0]
    require(S.rem(numerator,P.as_expr(),t)==0,
            'characteristic constant term equals quartic derivative at equilibria')
    brackets=[(1,2),(3,4),(12,13),(26,27)]
    bracket_values=[]
    for left,right in brackets:
        bracket_values.append([str(P.eval(left)),str(P.eval(right))])
        require(left>=1 and P.eval(left)*P.eval(right)<0,'stability roots bracketed above one')
    require(P.degree()==4 and S.gcd(P,P.diff()).degree()==0,
            'stability quartic has four simple ordered roots')
    # A monic degree-four polynomial crosses with signs (-,+,-,+) at its
    # four simple real roots. The positive denominator transfers these to c.
    return {'parameters':{'N':7,'K':145},'characteristic_coefficients':
            [str(S.factor(v)) for v in (a,b,c)],
            'a_b_ab_minus_c_positive_for':'t>1; exact shifted-coefficient certificates',
            'brackets':brackets,'bracket_values':bracket_values,
            'constant_term_signs_in_root_order':[-1,1,-1,1],
            'classification':['index-one saddle','sink','index-one saddle','sink'],
            'scope':'original chemical Jacobian; local stability only, no global convergence claim'}

def negative_controls(data):
    cases=[]
    d=copy.deepcopy(data[0]);d['rates'][2]='1';cases.append(('wrong rate',lambda:check_example(d)))
    # Bind separate objects so each mutation is independently exercised.
    e=copy.deepcopy(data[1]);e['product'][0][1]=5;cases.append(('wrong product',lambda e=e:check_example(e)))
    g=copy.deepcopy(data[0]);g['polynomial_descending'][-1]+=1;cases.append(('wrong eliminant',lambda g=g:check_example(g)))
    h=copy.deepcopy(data[1]);h['equilibrium_map'][2]='13/(t+1)';cases.append(('wrong reconstruction',lambda h=h:check_example(h)))
    cases.append(('insufficient geometric separation',lambda:check_dimension(3,R=4)))
    cases.append(('wrong prior-family epsilon',lambda:check_prior_translation(2,S.Rational(1,5))))
    cases.append(('wrong common equation scaling',lambda:check_main_scaling(3,common_factor=124)))
    cases.append(('wrong rate-curve derivative',lambda:check_b_rate_family(claimed_derivative='0')))
    cases.append(('wrong rate-window maximum',lambda:check_b_rate_family(claimed_upper=S.Integer(1569))))
    cases.append(('wrong chemical characteristic coefficient',lambda:check_reciprocal_stability(claimed_a='1')))
    cases.append(('false Routh-Hurwitz positivity',lambda:positive_after_shift(1-S.Symbol('t'),S.Symbol('t'))))
    rejected=[]
    for name,run in cases:
        try: run()
        except ValueError as exc: rejected.append({'mutation':name,'rejected_by':str(exc)})
        else: raise RuntimeError('Negative control was accepted: '+name)
    return rejected

def main():
    p=argparse.ArgumentParser();p.add_argument('--data',default=str(Path(__file__).with_name('examples.json')))
    p.add_argument('--max-n',type=int,default=12);p.add_argument('--negative-controls',action='store_true')
    args=p.parse_args(); data=json.loads(Path(args.data).read_text())
    result={'examples':[check_example(d) for d in data],
            'finite_general_checks':[check_dimension(n) for n in range(2,args.max_n+1)],
            'prior_family_translation':[check_prior_translation(n) for n in range(2,args.max_n+1)],
            'R25_prior_family_scaling':[check_main_scaling(n) for n in range(2,args.max_n+1)],
            'inflow_free_rate_family':check_b_rate_family(),
            'reciprocal_example_stability':check_reciprocal_stability()}
    if args.negative_controls: result['negative_controls']=negative_controls(data)
    result.update(status='EXACT_CHECKS_PASS',checks_executed=COUNT,
                  python=platform.python_version(),sympy=S.__version__,
                  universal_scope='Theorem proved in paper.tex; finite checks do not establish all n.',
                  supplementary_check_provenance='Formulas and checking approach from supplied 2026-10-04 referee audit; common SymPy backend, no algebra-engine independence claimed.')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
