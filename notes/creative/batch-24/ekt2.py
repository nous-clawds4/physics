"""Batch 24 rerun: Set 2 kill check with exterior-to-exterior mouth gluings. Structure only, no weights.
CTC exploration only. 2D, nonrelativistic, equal-mass hard discs (radius r), elastic; absorbing barrier y=yb with
slits (point-like crossing test). Mouths: circles radius s centred A, B; ball centre reaching B+s e at time t with
velocity w (w.e<0) emerges at time t-T as:
  G1 'reflect' : position A+s e,  velocity w - 2(w.e)e         (normal reversed, tangent kept)
  G2 'invert'  : position A-s e,  velocity -w                  (point inversion)
(Both identify exterior with exterior; in 2D both are orientation-reversing handles, noted, not used.)
Hosts with T <= |d| (no CTC) are dropped and listed.
Histories (at most one traversal):
 H0: launch ray, no self-collision; consistent unless the emerging older ball touches the younger one, and it is
     'multi' (not enumerated) if the older ball re-enters a mouth.
 H1: one collision at t_c with contact normal n (young -> old). Unknowns (t_c, alpha, q = w_old.n): the young ball
     leaves with w_p = (v0.t)t + q n, enters B, emerges as (Q, w_em) at t_e = t_b - T; consistency requires
     w_em.n = q and Q + w_em (t_c - t_e) = v0 t_c + 2 r n (3 equations, 3 unknowns; discrete roots), solved by
     scipy.optimize.root from a grid of starts and deduplicated. Each root is then checked: approach, t_e < t_c,
     young pre/post paths and older pre/post paths against both mouth discs and the barrier, no earlier or second
     contact. An older post-collision path that re-enters a mouth makes the history 'multi' (reported, not counted).
Roots do not depend on the slits (the barrier only filters), so they are computed once per launch.
Question: for launches through slit 1 (window ~7.9 deg), does the number of valid H1 roots, or H0 validity,
change when slit 2 opens? Root-count edges in theta are refined by bisection."""
import numpy as np, warnings
from scipy.optimize import root
warnings.filterwarnings("ignore")
r,s,yb,hw=0.1,0.5,2.0,0.15
SL={1:-0.6,2:0.6}; B=np.array([-1.8,6.0])
def cross_ok(p,q,op):
    if (p[1]-yb)*(q[1]-yb)>0 or p[1]==q[1]: return True
    x=p[0]+(q[0]-p[0])*(yb-p[1])/(q[1]-p[1]); return any(abs(x-SL[k])<hw for k in op)
def ray_circle(p,v,c,R):
    f=p-c; a=v@v; b=2*f@v; cc=f@f-R*R; D=b*b-4*a*cc
    if D<0 or a==0: return None
    t=(-b-np.sqrt(D))/(2*a); return t if t>1e-7 else None
def first_mouth(p,v,A,tmax=np.inf):
    hits=[(t,m) for m,c in (("A",A),("B",B)) for t in [ray_circle(p,v,c,s)] if t is not None and t<tmax]
    return min(hits) if hits else None
def emerge(P,w,A,g):
    e=(P-B)/s
    return (A+s*e, w-2*(w@e)*e) if g=="reflect" else (A-s*e, -w)
def mindist(p1,v1,p2,v2,t0,t1):
    if t1<=t0: return np.inf
    dp=p1-p2; dv=v1-v2; tt=t0 if dv@dv==0 else np.clip(-(dp@dv)/(dv@dv),t0,t1); return np.linalg.norm(dp+dv*tt)
def blocked_t(p,v,op):  # time at which a ray is absorbed by the barrier (inf if never)
    if v[1]==0: return np.inf
    t=(yb-p[1])/v[1]
    if t<=1e-9: return np.inf
    return np.inf if cross_ok(p,p+v*(t+1e-6),op) else t
def H1_roots(theta,A,T,g):
    v0=np.array([np.sin(theta),np.cos(theta)])
    def unpack(x):
        tc,al,q=x; n=np.array([np.cos(al),np.sin(al)]); t=np.array([-n[1],n[0]]); return tc,n,t,q
    def F(x):
        tc,n,t,q=unpack(x); Y=v0*tc; wp=(v0@t)*t+q*n
        tb=ray_circle(Y,wp,B,s)
        if tb is None or tc<=0: return [1e3,1e3,1e3]
        P=Y+wp*tb; Q,we=emerge(P,wp,A,g); te=tc+tb-T
        R=Q+we*(tc-te)-(Y+2*r*n); return [we@n-q,R[0],R[1]]
    sols=[]
    for tc0 in (0.5,1.5,3,5,8,12):
        for al0 in np.linspace(0,2*np.pi,12,endpoint=False):
            for q0 in (-1.5,-0.5,0.5,1.5):
                o=root(F,[tc0,al0,q0],method='hybr')
                if o.success and np.max(np.abs(F(o.x)))<1e-9:
                    tc,n,t,q=unpack(o.x); key=(round(tc,6),round(np.arctan2(n[1],n[0]),5))
                    if not any(abs(k[0]-key[0])<1e-5 and abs(np.angle(np.exp(1j*(k[1]-key[1]))))<1e-4 for k,_ in sols): sols.append((key,o.x))
    return v0,[x for _,x in sols]
def check_H1(v0,x,A,T,g,op):
    tc,al,q=x; n=np.array([np.cos(al),np.sin(al)]); t=np.array([-n[1],n[0]])
    Y=v0*tc; wp=(v0@t)*t+q*n; tb=ray_circle(Y,wp,B,s); P=Y+wp*tb; Q,we=emerge(P,wp,A,g); te=tc+tb-T
    C=Y+2*r*n
    if (we-v0)@n>=0 or not te<tc: return "invalid"
    fm=first_mouth(np.zeros(2),v0,A,tc)
    if fm or not cross_ok(np.zeros(2),Y,op): return "invalid"
    fm=first_mouth(Y,wp,A)
    if fm is None or fm[1]!="B" or abs(fm[0]-tb)>1e-7 or not cross_ok(Y,P,op): return "invalid"
    fm=first_mouth(Q+we*1e-6,we,A,tc-te-1e-6)
    if fm or not cross_ok(Q,C,op): return "invalid"
    if mindist(np.zeros(2),v0,Q-we*te,we,max(0,te),tc-1e-6)<2*r-1e-9: return "invalid"
    wo=we-((we-v0)@n)*n   # older post-collision velocity
    if mindist(Y-wp*tc,wp,C-wo*tc,wo,tc+1e-6,tc+tb)<2*r-1e-9: return "invalid"
    fm=first_mouth(C,wo,A,blocked_t(C,wo,op))
    return "multi" if fm else "valid"
def H0(v0,A,T,g,op):
    tb=blocked_t(np.zeros(2),v0,op); fm=first_mouth(np.zeros(2),v0,A,tb)
    if fm is None: return "ok"
    if fm[1]=="A": return "multi"
    t_b=fm[0]; P=v0*t_b; Q,we=emerge(P,v0,A,g); te=t_b-T
    tbl=blocked_t(Q,we,op); 
    if mindist(np.zeros(2),v0,Q-we*te,we,max(0,te),min(t_b,te+tbl))<2*r: return "fails"
    return "multi" if first_mouth(Q+we*1e-6,we,A,tbl) else "ok"
def structure(theta,A,T,g,roots=None):
    v0,X=roots if roots else H1_roots(theta,A,T,g); out={}
    for op in ((1,),(1,2)):
        st=[check_H1(v0,x,A,T,g,op) for x in X]
        out[op]=(H0(v0,A,T,g,op),st.count("valid"),st.count("multi"))
    return out,len(X)
if __name__=="__main__":
    hosts=[(np.array(a),T) for a in [(-4.2,10.0),(3.0,8.0),(1.0,12.0),(-1.8,-3.0),(4.0,0.5)] for T in (8.0,15.0)]
    lo,hi=np.arctan((SL[1]-hw)/yb),np.arctan((SL[1]+hw)/yb)
    print(f"slit-1 launch window {np.degrees(lo):.2f}..{np.degrees(hi):.2f} deg (width {np.degrees(hi-lo):.2f}); r={r} s={s}; B={B.tolist()}")
    th=np.linspace(lo+1e-4,hi-1e-4,33); total=0; anyH1=0; excl=0
    for g in ("reflect","invert"):
        for A,T in hosts:
            dn=np.linalg.norm(B-A)
            if T<=dn: print(f"[{g}] host A={A.tolist()} T={T}: |d|={dn:.3f} >= T: no CTC, dropped"); continue
            S=[structure(a,A,T,g) for a in th]
            diff=[i for i,(o,_) in enumerate(S) if o[(1,)]!=o[(1,2)]]
            nroot=sum(k for _,k in S); v1=sum(o[(1,)][1] for o,_ in S); v2=sum(o[(1,2)][1] for o,_ in S)
            m1=sum(o[(1,)][2] for o,_ in S); f0=sum(o[(1,)][0]=="fails" for o,_ in S)+sum(o[(1,2)][0]=="fails" for o,_ in S)
            ex=sum(1 for o,_ in S for op in o if o[op][0]=="fails" and o[op][1]==0)
            print(f"[{g}] host A={A.tolist()} T={T} (|d|={dn:.2f}): raw roots {nroot}; valid H1 one/two slits {v1}/{v2}; multi(one slit) {m1}; H0 fails {f0}; zero-solution cases {ex}; slit-1 launches with structure differing {len(diff)}")
            # bisection refinement of root-count edges (one slit config) between adjacent grid points
            for i in range(len(th)-1):
                if S[i][0]!=S[i+1][0]:
                    a,b=th[i],th[i+1]; sa=S[i][0]
                    for _ in range(8):
                        m=0.5*(a+b); sm=structure(m,A,T,g)[0]
                        if sm==sa: a=m
                        else: b=m
                    print(f"      edge at theta={np.degrees(0.5*(a+b)):.4f} deg: {S[i][0]} -> {S[i+1][0]}")
            for i in diff: print(f"      DIFF theta={np.degrees(th[i]):.3f}: {S[i][0]}")
            total+=len(diff); anyH1+=v1+v2; excl+=ex
    print(f"\nTOTAL slit-1 launches (all CTC hosts, both gluings) whose structure depends on slit 2: {total}; valid H1 found: {anyH1}; zero-solution cases: {excl}")
