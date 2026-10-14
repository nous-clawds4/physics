"""Batch 24: Set 2 first kill check. Structure only, no weights. CTC exploration only.
2D, nonrelativistic hard-sphere billiard (EKT-style, Echeverria-Klinkhammer-Thorne PRD 44 (1991) 1077),
in an offset-mouth host (#385 L56): two circular mouths A, B of radius s; a ball whose centre reaches the
circle of B at point B+s e, time t, velocity w, re-emerges at A+s e at time t-T with the same velocity
(idealised mouth: pure translation by d=B-A plus a time shift -T, no rotation, no lensing).
Equal masses, ball radius r, elastic collisions. Barrier y=yb with slits (point-like crossing test; a ball
hitting the barrier outside an open slit is absorbed, which ends that path; walls do not reflect).
Histories enumerated (one traversal at most):
 H0 'trivial': launch line, no self-collision. Consistent iff (a) the ray misses B, or
    (b) it enters B and the emerging older ball (from A at t_b - T with v0) never touches the younger ball.
 H1 'one collision': the older ball (exits A with w) hits the younger at t_c; the younger is deflected to w,
    enters B and becomes the older one. Elastic equal-mass contact gives w = v0 + k n, older leaves with v0,
    and the loop closes iff w T = d + 2 r n. Then n is parallel to u = v0 - d/T, k = 2r/T - |u| < 0 (approach),
    and t_c is a free parameter: the consistent H1 histories form intervals in t_c (a continuum, an artefact
    of the idealised translation mouth). For each t_c the script checks: younger path [0,t_c] passes the
    barrier only at open slits, no earlier contact, no mouth entry; younger post-collision ray reaches B
    unblocked; t_e = t_b - T < t_c; older pre-collision path from A+s e passes the barrier only at open slits.
Output: per host and slit configuration, launches with consistent H0, number of H1 intervals, and launches
whose structure (H0 ok?, number of H1 intervals) differs between one slit and two slits open."""
import numpy as np
r,s,yb,hw=0.1,0.5,2.0,0.15
SL={1:-0.6,2:0.6}
def cross_ok(p,q,open_):
    if (p[1]-yb)*(q[1]-yb)>0 or p[1]==q[1]: return True
    x=p[0]+(q[0]-p[0])*(yb-p[1])/(q[1]-p[1])
    return any(abs(x-SL[k])<hw for k in open_)
def ray_circle(p,v,c,R):
    f=p-c; a=v@v; b=2*f@v; cc=f@f-R*R; D=b*b-4*a*cc
    if D<0: return None
    t=(-b-np.sqrt(D))/(2*a); return t if t>1e-9 else None
def min_dist(p1,v1,p2,v2,t0,t1):  # positions p+v t
    dp=p1-p2; dv=v1-v2; tt=np.clip(-(dp@dv)/(dv@dv) if dv@dv>0 else t0,t0,t1)
    return np.linalg.norm(dp+dv*tt)
def analyse(theta,A,B,T,open_,tmax=40.0,ntc=600):
    v0=np.array([np.sin(theta),np.cos(theta)]); x0=np.zeros(2); d=B-A
    # H0
    tB=ray_circle(x0,v0,B,s); tA=ray_circle(x0,v0,A,s)
    if tA is not None and (tB is None or tA<tB): h0='multi'      # enters A first: not enumerated
    elif tB is None: h0=True
    else:
        P=x0+v0*tB
        if not cross_ok(x0,P,open_): h0=True                     # absorbed before mouth
        else:
            e=(P-B)/s; te=tB-T; Q=A+s*e
            # older ball from Q at te with v0 until blocked; younger on [0,tB]
            t0,t1=max(0,te),tB
            # older path is blocked at barrier crossing (if any) outside open slits
            ty=(yb-Q[1])/v0[1] if v0[1]!=0 else -1
            if ty>0 and not cross_ok(Q,Q+v0*(ty+1e-6),open_): t1=min(t1,te+ty)
            h0 = not (t1>t0 and min_dist(x0,v0,Q-v0*te,v0,t0,t1)<2*r)
    # H1
    u=v0-d/T; nu=np.linalg.norm(u); ints=0; meas=0.0
    if nu>2*r/T:
        n=u/nu; k=2*r/T-nu; w=v0+k*n
        good=np.zeros(ntc,bool); tcs=np.linspace(1e-3,tmax,ntc)
        for i,tc in enumerate(tcs):
            Y=x0+v0*tc
            if not cross_ok(x0,Y,open_): continue
            ta=ray_circle(x0,v0,A,s); tb0=ray_circle(x0,v0,B,s)
            if (ta is not None and ta<tc) or (tb0 is not None and tb0<tc): continue
            dtb=ray_circle(Y,w,B,s)
            if dtb is None: continue
            P=Y+w*dtb
            if not cross_ok(Y,P,open_): continue
            ta2=ray_circle(Y,w,A,s)
            if ta2 is not None and ta2<dtb: continue
            tb=tc+dtb; te=tb-T
            if not te<tc: continue
            e=(P-B)/s; Q=A+s*e; C=Y+2*r*n
            if np.linalg.norm(Q+w*(tc-te)-C)>1e-6: continue          # loop closure check
            if not cross_ok(Q,C,open_): continue
            if min_dist(x0,v0,Q-w*te,w,max(0,te),tc-1e-6)<2*r-1e-9: continue
            good[i]=True
        ints=int(np.sum(np.diff(np.r_[0,good.astype(int)])==1)); meas=good.sum()*(tcs[1]-tcs[0])
    return h0,ints,meas
if __name__=="__main__":
    B=np.array([-1.8,6.0])
    hosts=[(np.array(a),T) for a in [(-4.2,10.0),(3.0,8.0),(1.0,12.0),(-1.8,-3.0),(4.0,0.5)] for T in (8.0,15.0)]
    th=np.radians(np.linspace(-40,40,161))
    print("r=%g s=%g barrier y=%g slits x=%s half-width %g; B=%s; launch from origin, unit speed"%(r,s,yb,SL,hw,B))
    tot=0
    for A,T in hosts:
        res={c:[analyse(a,A,B,T,c) for a in th] for c in ((1,),(1,2))}
        diff=[(np.degrees(a),res[(1,)][i],res[(1,2)][i]) for i,a in enumerate(th) if res[(1,)][i][:2]!=res[(1,2)][i][:2]]
        def summ(c): R=res[c]; return "H0 ok %d, H0 fails %d, multi %d, launches with H1 %d, max H1 intervals %d"%(sum(x[0] is True for x in R),sum(x[0] is False for x in R),sum(x[0]=='multi' for x in R),sum(x[1]>0 for x in R),max(x[1] for x in R))
        print(f"\nhost A={A.tolist()} T={T}:\n  slit 1 only : {summ((1,))}\n  slits 1+2   : {summ((1,2))}\n  launches whose structure differs: {len(diff)}")
        for dd in diff[:6]: print(f"     theta={dd[0]:.1f}: one slit (H0,#H1,meas)={dd[1][0]},{dd[1][1]},{dd[1][2]:.2f}; two slits={dd[2][0]},{dd[2][1]},{dd[2][2]:.2f}")
        def slit_of(a):
            x=yb*np.tan(a); return [k for k in SL if abs(x-SL[k])<hw]
        d1=[dd for dd in diff if slit_of(np.radians(dd[0]))==[1]]
        print(f"  of these, launches whose own line crosses slit 1 (the nontrivial case): {len(d1)}; crossing slit 2 (trivially blocked when closed): {sum(1 for dd in diff if slit_of(np.radians(dd[0]))==[2])}")
        tot+=len(d1)
        ex=[dd for dd in diff if dd[1][0] is True and dd[2][0] is False]
        print(f"  launches where opening slit 2 makes H0 inconsistent: {len(ex)}; with H0 failing and no H1 in two-slit (zero solutions): {sum(1 for dd in ex if dd[2][1]==0)}")
    print("\ntotal slit-1 launches (over hosts) whose structure depends on slit 2:",tot)
