"""Batch 15 toy 2 (not a known exact solution; exotic matter assumed): symmetric two-mouth
wormhole with positive mass seen from both sides.  ds^2 = -A dt^2 + A^{-1}dx^2 + R^2 dOmega^2,
A = 1 - 2m/sqrt(x^2+k^2), R^2 = x^2+k^2, need k > 2m.  Then V = A(1+L^2/R^2), xdot^2 = E^2 - V
(A^{-1} dx^2 radial normalisation absorbed: A^{-1} xdot^2 ... we use proper equation
A^{-1} xdot^2 = E^2/A - 1 - L^2/R^2  =>  xdot^2 = E^2 - V)."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
m,k=1.0,3.0
A=lambda x: 1-2*m/np.sqrt(x*x+k*k)
V=lambda x,L: A(x)*(1+L*L/(x*x+k*k))
dV=lambda x,L,h=1e-6:(V(x+h,L)-V(x-h,L))/(2*h)
d2=lambda x,L,h=1e-4:(V(x+h,L)-2*V(x,L)+V(x-h,L))/h**2
def ext(L,xs=np.linspace(-300,300,600001)):
    d=dV(xs,L);o=[]
    for i in np.where(np.sign(d[:-1])!=np.sign(d[1:]))[0]:
        x0=brentq(dV,xs[i],xs[i+1],args=(L,));o.append((round(x0,4),round(V(x0,L),6),'stable' if d2(x0,L)>0 else 'unstable'))
    return o
print("m=%g k=%g  A(throat)=%.4f"%(m,k,A(0)))
for L in [0,2,3,4,5,6]: print(" L=%g:"%L,ext(L))

def classes(L):
    e=ext(L); mins=sorted({(x,v) for x,v,t in e if t=='stable'}); maxs=sorted({(x,v) for x,v,t in e if t=='unstable'})
    return mins,maxs
def rhs(s,y,L): x,xd,ph=y; return [xd,-0.5*dV(x,L),L/(x*x+k*k)]
def run(x0,xd0,L,T=4000): return solve_ivp(rhs,[0,T],[x0,xd0,0],args=(L,),rtol=1e-10,atol=1e-12,max_step=0.5)
def cross(s): x=s.y[0]; return int(np.sum(np.sign(x[:-1])!=np.sign(x[1:])))
for L in [3.8,5.0]:
    mins,maxs=classes(L); Vb=max(v for x,v in maxs) if maxs else None
    print("\nL=%g wells (x,V):"%L,mins," barriers:",maxs)
    xo=max(x for x,v in mins); Vo=V(xo,L)
    print(" outer well x=%.3f V=%.6f; barrier V=%.6f; escape V=1"%(xo,Vo,Vb))
    if Vb<1:
        thr=np.sqrt(Vb-Vo); esc=np.sqrt(1-Vo)
        print(" radial kick from outer circular orbit: thread threshold %.6f, escape threshold %.6f"%(thr,esc))
        for lab,v in [("0.9 thr",0.9*thr),("1.1 thr",1.1*thr),("mid",0.5*(thr+esc)),("1.1 esc",1.1*esc)]:
            r=run(xo,-v,L); print("  kick %-8s: x in [%.2f, %.2f], throat crossings=%d"%(lab,r.y[0].min(),r.y[0].max(),cross(r)))
        v0=0.5*(thr+esc)
        for dv in [-1e-3,1e-3]:
            r=run(xo,-(v0+dv),L); print("  threading orbit perturbed %+g: crossings=%d"%(dv,cross(r)))
        r=run(xo,1e-3,L); print("  reference (tiny kick): crossings=%d, x in [%.2f,%.2f]"%(cross(r),r.y[0].min(),r.y[0].max()))
    else:
        esc=np.sqrt(1-Vo); print(" barrier above 1: outer wells and throat well are separated for all bound energies; escape threshold %.6f"%esc)
        r=run(0.0,0.05,L); print("  throat-trapped orbit (x0=0, xdot=0.05): x in [%.3f,%.3f], crossings=%d"%(r.y[0].min(),r.y[0].max(),cross(r)))
        for v in [0.9*esc,1.1*esc]:
            r=run(xo,-v,L); print("  inward kick %.4f from outer: x in [%.2f,%.2f], crossings=%d"%(v,r.y[0].min(),r.y[0].max(),cross(r)))
