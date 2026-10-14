"""Batch 16: stability of the closed geodesic threading a one-universe thin-shell handle.
Model (Visser-type thin-shell, flat outside, static, no time offset => no CTC): in R^2 (equatorial
plane), remove discs of radius a centred at (+-D/2, 0) and identify their boundaries by the
reflection x -> -x.  A straight ray hitting mouth A at point p re-emerges at the mirror point on B
with direction reflected (x-component flipped).  Composed with the mirror map, one traversal acts
like a specular reflection off a convex circle: the 'threading' orbit along the axis is a 2-mirror
billiard between convex mirrors.  We compute its linearised return map numerically and its trace.
"""
import numpy as np
def hit(p,d,c,a):
    # first intersection of ray p+t d (t>1e-9) with circle centre c radius a; None if missing
    q=p-c; b=np.dot(q,d); cc=np.dot(q,q)-a*a; disc=b*b-cc
    if disc<0: return None
    for t in sorted([-b-np.sqrt(disc),-b+np.sqrt(disc)]):
        if t>1e-9: return t
    return None
def step(p,d,D,a):
    """Enter mouth A (or B) at h; emerge from the other mouth at q = c' + R(h - c), R = diag(-1,1).
    Normal component (inward at entry) becomes outward at exit; tangential part maps by R."""
    R=np.array([-1.,1.]); cs={'A':np.array([D/2,0.]),'B':np.array([-D/2,0.])}
    best=None
    for k,c in cs.items():
        t=hit(p,d,c,a)
        if t is not None and (best is None or t<best[0]): best=(t,k)
    if best is None: return None
    t,k=best; c=cs[k]; c2=cs['B' if k=='A' else 'A']; h=p+t*d
    nin=(c-h)/a; dn=np.dot(d,nin); dt=d-dn*nin
    q=c2+R*(h-c); nout=(q-c2)/a
    return q, dn*nout+R*dt, k
def return_map(y,th,D,a):
    # start at x=0 line, transverse offset y, angle th to +x; follow 2 traversals, back to x=0
    p=np.array([0.,y]); d=np.array([np.cos(th),np.sin(th)])
    for _ in range(2):
        r=step(p,d,D,a)
        if r is None: return None
        p,d,_=r
        # move to x=0 plane
        t=-p[0]/d[0]; p=p+t*d
    return p[1], np.arctan2(d[1],d[0]) if d[0]>0 else np.arctan2(d[1],-d[0])
if __name__=="__main__":
    a=1.0
    for D in [3.0,5.0,10.0]:
        e=1e-7; J=np.zeros((2,2)); base=return_map(0,0,D,a)
        for j,(dy,dt) in enumerate([(e,0),(0,e)]):
            r=return_map(dy,dt,D,a); J[:,j]=[(r[0]-base[0])/e,(r[1]-base[1])/e]
        tr=np.trace(J); L=D-2*a
        print("D=%g (gap L=%g): return-map trace=%.6f (|tr|>2 => unstable), eigenvalues %s"%(D,L,tr,np.round(np.linalg.eigvals(J),5)))
    # winding record bookkeeping: count signed traversals for a perturbed threading orbit
    D=5.0; p=np.array([0.,1e-4]); d=np.array([1.,0.]); n=0
    for i in range(60):
        r=step(p,d,D,a)
        if r is None: break
        p,d,c=r; n+=1
    print("perturbed threading orbit (offset 1e-4, D=5): traversals before missing the mouths = %d"%n)
