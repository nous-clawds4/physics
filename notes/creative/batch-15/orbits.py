"""Batch 15: timelike geodesics around Ellis / Ellis-Bronnikov drainhole throats.
Metric: ds^2 = -A dt^2 + A^{-1}[dx^2 + (x^2+k^2) dOmega^2],  A = exp(2 g),
g(x) = -(m/k)(pi/2 - arctan(x/k)).  m=0: pure (massless) Ellis.  x in R, throat region near x=0.
Equatorial geodesics: A tdot = E, (x^2+k^2) A^{-1} phidot = L, and
xdot^2 = E^2 - V,  V(x) = A (1 + A L^2/(x^2+k^2))   (from -1 = -E^2/A + xdot^2/A + L^2 A/(x^2+k^2)).
Circular orbits: V'=0; stable iff V''>0.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

def A(x,m,k): return np.exp(-2*(m/k)*(np.pi/2-np.arctan(x/k)))
def V(x,L,m,k):
    a=A(x,m,k); return a*(1+a*L**2/(x**2+k**2))
def dV(x,L,m,k,h=1e-6): return (V(x+h,L,m,k)-V(x-h,L,m,k))/(2*h)
def d2V(x,L,m,k,h=1e-4): return (V(x+h,L,m,k)-2*V(x,L,m,k)+V(x-h,L,m,k))/h**2

def extrema(L,m,k,xs=np.linspace(-200,200,400001)):
    d=dV(xs,L,m,k); out=[]
    for i in np.where(np.sign(d[:-1])!=np.sign(d[1:]))[0]:
        x0=brentq(dV,xs[i],xs[i+1],args=(L,m,k)); out.append((x0,V(x0,L,m,k),d2V(x0,L,m,k)))
    return out

def rhs(s,y,L,m,k):
    x,xd,ph=y
    # xddot = -V'/2 (affine parameter, from xdot^2 = E^2 - V)
    return [xd,-0.5*dV(x,L,m,k),A(x,m,k)**2*L/(x**2+k**2)]

def run(x0,xd0,L,m,k,T=4000):
    sol=solve_ivp(rhs,[0,T],[x0,xd0,0],args=(L,m,k),rtol=1e-10,atol=1e-12,max_step=1.0)
    return sol

if __name__=="__main__":
    k=1.0
    print("== pure Ellis m=0: V = 1 + L^2/(x^2+k^2) ==")
    for L in [0.5,1,2,4]:
        print(" L=%g extrema:"%L,[(round(a,4),round(b,5),'stable' if c>0 else 'unstable') for a,b,c in extrema(L,0,k)])
    for m in [0.1,0.3]:
        print("== Ellis-Bronnikov m=%g k=%g;  A(+inf)=1, A(-inf)=%.4f =="%(m,k,np.exp(-2*np.pi*m/k)))
        Ls=np.linspace(0.2,12,119); isco=None
        for L in Ls:
            ex=extrema(L,m,k); st=[e for e in ex if e[2]>0]
            if st and isco is None: isco=(L,st)
        print(" first L with a stable circular orbit:",round(isco[0],3),[(round(a,4),round(b,5)) for a,b,c in isco[1]])
        for L in [2,4,6,8]:
            print(" L=%g extrema:"%L,[(round(a,3),round(b,5),'stable' if c>0 else 'unstable') for a,b,c in extrema(L,m,k)])
    # numeric confirmation + kick thresholds for m=0.3
    m=0.3; L=6.0
    ex=extrema(L,m,k); print("\n== m=0.3, L=6 classes ==",ex)
    stab=[e for e in ex if e[2]>0]; unst=[e for e in ex if e[2]<0]
    xs,Vs,_=stab[-1]; xu,Vu,_=max(unst,key=lambda e:e[1]) if unst else (None,None,None)
    print(" stable circular x=%.4f V=%.6f; barrier x=%s V=%s; V(-inf)=%.6f"%(xs,Vs,xu,Vu,np.exp(-2*np.pi*m/k)))
    # perturbation: small radial velocity -> bounded oscillation (basin)
    for dv in [1e-3,1e-2]:
        s=run(xs,dv,L,m,k); print(" perturb xdot=%g: x range [%.4f, %.4f]"%(dv,s.y[0].min(),s.y[0].max()))
    # impulsive radial kick: threshold E^2 = Vbarrier  =>  xdot0^2 = Vu - Vs
    if xu is not None:
        thr=np.sqrt(Vu-Vs); print(" radial-kick threshold xdot0 = sqrt(Vbar - Vcirc) = %.6f"%thr)
        for f in [0.98,1.02]:
            s=run(xs,-f*thr,L,m,k,T=3000); print("  kick %.2f*thr inward: final x=%.2f, min x=%.2f"%(f,s.y[0][-1],s.y[0].min()))
    # matched-return record: count throat crossings (sign changes of x) and periapsis passages
    def crossings(s): x=s.y[0]; return int(np.sum(np.sign(x[:-1])!=np.sign(x[1:])))
    print(" throat crossings ref (no kick): ",crossings(run(xs,1e-3,L,m,k)))
