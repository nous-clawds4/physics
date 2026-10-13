"""Batch 22: returning echoes. Charged test particle on the flat cylinder R^3, x ~ x+L (c=1).
Unperturbed path: at rest at origin for t<0; prescribed launch, constant acceleration along direction
theta (angle from the +y axis toward +x) from rest to speed v over time tau; optional slit kick: a
transverse velocity change dv_s spread over tau at screen-ward distance y_s; then free flight to the screen y=D.
Self-force at O(eps), eps = q^2/(4 pi eps0 m c^2) (a length): the retarded Lienard-Wiechert fields of the images
(m != 0) evaluated on the unperturbed path. The local (m=0) self-force is Landau-Lifshitz reduced order; it is
nonzero only during prescribed accelerations, where it is absorbed into the launcher (prescribed motion), and zero in
free flight. First-order deflection: dv/dt = eps (F - v (v.F)) / gamma with F = E + v x B per unit q, integrated to y=D.
Output: dx_hit/eps vs theta, the relative density change delta = -(d dx_hit/d theta)/(D sec^2 theta) per unit eps,
and the theta-period of its oscillation."""
import numpy as np, sys
def path(theta,v,tau,T,dt,ys=None,dvs=0.0):
    t=np.arange(-0.0,T+dt,dt); n=len(t)
    e=np.array([np.sin(theta),np.cos(theta)]); p=np.array([-np.cos(theta),np.sin(theta)])
    a=np.zeros((n,2)); a[t<tau]=e*(v/tau)
    V=np.zeros((n,2)); R=np.zeros((n,2)); ts=None
    for i in range(1,n):
        if ys is not None and ts is None and R[i-1,1]>=ys: ts=t[i-1]
        if ts is not None and t[i]<ts+tau: a[i]=p*(dvs/tau)
        V[i]=V[i-1]+0.5*(a[i-1]+a[i])*dt; R[i]=R[i-1]+0.5*(V[i-1]+V[i])*dt
    return t,R,V,a
def image_force(t,R,V,A,L,M):
    def interp(tq,X): return np.stack([np.interp(tq,t,X[:,k],left=X[0,k]) for k in range(2)],-1)
    F=np.zeros((len(t),2))
    ms=np.array([m for m in range(-M,M+1) if m]); 
    tt=t[:,None]*np.ones(len(ms))[None]
    lo=tt-(np.abs(ms)*L+t.max()*2)[None]; hi=tt.copy()
    shift=np.stack([ms*L,0*ms],-1)[None]
    for _ in range(60):
        mid=0.5*(lo+hi); rr=R[:,None,:]-(interp(mid,R)+shift)
        g=tt-mid-np.linalg.norm(rr,axis=-1); lo=np.where(g>0,mid,lo); hi=np.where(g>0,hi,mid)
    tr=0.5*(lo+hi); rr=R[:,None,:]-(interp(tr,R)+shift); Rn=np.linalg.norm(rr,axis=-1)
    nvec=rr/Rn[...,None]; b=interp(tr,V); bd=interp(tr,A)
    # 3-vectors (z=0)
    z=lambda X: np.concatenate([X,np.zeros(X.shape[:-1]+(1,))],-1)
    n3,b3,bd3=z(nvec),z(b),z(bd); k=1-np.sum(n3*b3,-1)
    E=(n3-b3)*(1-np.sum(b3*b3,-1))[...,None]/(k**3*Rn**2)[...,None] \
      + np.cross(n3,np.cross(n3-b3,bd3))/(k**3*Rn)[...,None]
    E=E.sum(1)-0; B=np.cross(n3,(np.cross(n3-b3,bd3)/(k**3*Rn)[...,None]+(n3-b3)*(1-np.sum(b3*b3,-1))[...,None]/(k**3*Rn**2)[...,None])).sum(1)
    v3=z(V); F3=E+np.cross(v3,B); return F3[:,:2]
def deflection(theta,v,tau,L,D,dt,M,ys=None,dvs=0.0):
    T=D/(v*np.cos(theta))+tau+1
    t,R,V,A=path(theta,v,tau,T,dt,ys,dvs); F=image_force(t,R,V,A,L,M)
    g=1/np.sqrt(1-np.sum(V*V,1)); dv=(F-V*np.sum(V*F,1)[:,None])/g[:,None]
    DV=np.cumsum(dv,0)*dt; DX=np.cumsum(DV,0)*dt
    i=np.searchsorted(R[:,1],D); vx,vy=V[i]; return DX[i,0]-vx/vy*DX[i,1]
if __name__=="__main__":
    D=10.0; dt=0.01; tau=0.2
    for (L,v,ys,dvs) in [(2.5,0.5,None,0),(2.5,0.3,None,0),(1.25,0.5,None,0),(5.0,0.5,None,0),(2.5,0.5,5.0,0.05)]:
        M=int((D/v+5)/L)+2
        th=np.radians(np.linspace(-10,20,121)); dx=np.array([deflection(a,v,tau,L,D,dt,M,ys,dvs) for a in th])
        dens=-np.gradient(dx,th)/(D/np.cos(th)**2)
        s=np.sign(dens-dens.mean()); zc=np.where(np.diff(s)!=0)[0]
        per=2*np.degrees(np.mean(np.diff(th[zc]))) if len(zc)>2 else float('nan')
        print(f"L={L} v={v} tau={tau} slit_kick={'none' if ys is None else f'y_s={ys},dv={dvs}'} M={M}")
        print(f"   dx_hit/eps: min {dx.min():.4g} max {dx.max():.4g};  delta/eps: min {dens.min():.4g} max {dens.max():.4g}; sign changes {len(zc)}; mean theta-period {per:.3g} deg")
        print("   theta(deg), dx/eps, delta/eps:", " ".join(f"({np.degrees(a):.1f},{b:.3g},{c:.3g})" for a,b,c in list(zip(th,dx,dens))[::12]))
        print(f"   eps at which delta first reaches -1 (caustic, bands; out of first-order validity): {1/abs(dens.min()):.3g}")
