"""Batch 25: Set 7 kill check, conducting slit walls. Structure only, test-particle dynamics.
2D electrostatics (line charge q per unit length, translation-invariant in z): a grounded thin conducting plate on
y=0, x in [-Lb,Lb], with slit apertures of width w centred at x=+-a/2 (one slit: only x=-a/2 open). Boundary-element
solve: N collinear panels with constant charge density, collocation at panel centres, kernel -ln r (2 pi eps0 = 1).
For a particle at p the induced density is sigma(p) = -A^{-1} phi_p, and the induced field E(p) acts back on it
(image force; the particle's own field excluded). Nonrelativistic, quasi-static (the induced charge follows the
particle instantaneously), no radiation, test-field limit (#392: no metric back-reaction).
Units: launch speed v0 = 1, and the acceleration is kappa * E~(p) with kappa = q^2/(2 pi eps0 m v0^2) (a length).
Speed and charge enter only through kappa, so scanning kappa scans both.
Source at (0,-Ds), screen at y=D. E(p) is tabulated on a grid and interpolated (vectorised RK4 over all launches).
A launch crossing y=0 on metal, or coming within rmin of the plate, is absorbed.
Output per (a, w, kappa): slit-1 launches absorbed (one / two slits), max |dx_hit| between one and two slits for
slit-1 launches, fold (sign change of dx_hit/dtheta), and the screen histogram test: bins where
I_both < min(I_1, I_2) with both positive (unnormalised counts; uniform launch weighting in theta), and the
number of local minima of I_both - I_1 - I_2 (periodicity check). Convergence: N = 200, 400, 800 panels."""
import numpy as np, sys
from scipy.ndimage import map_coordinates
Lb,Ds,D,rmin=10.0,5.0,10.0,0.02
def panels(a,w,both,N):
    x=np.linspace(-Lb,Lb,N+1); c=0.5*(x[1:]+x[:-1]); h=x[1]-x[0]
    keep=~(np.abs(c+a/2)<w/2)
    if both: keep&=~(np.abs(c-a/2)<w/2)
    return c[keep],h
def field_grid(a,w,both,N,gx,gy):
    c,h=panels(a,w,both,N)
    dx=np.abs(c[:,None]-c[None,:]); A=-h*np.log(np.where(dx>0,dx,1.0)); np.fill_diagonal(A,-h*(np.log(h/2)-1))
    Ai=np.linalg.inv(A)
    X,Y=np.meshgrid(gx,gy,indexing='ij'); P=np.stack([X.ravel(),Y.ravel()],1)
    Ex=np.zeros(len(P)); Ey=np.zeros(len(P))
    for k in range(0,len(P),4000):
        p=P[k:k+4000]; rx=p[:,0][None,:]-c[:,None]; ry=p[:,1][None,:]; r2=np.maximum(rx*rx+ry*ry,1e-8)
        phi=-0.5*np.log(r2)                       # particle potential at panel centres (q = 1)
        sig=-(Ai@phi)*h                            # induced charge per panel
        Ex[k:k+4000]=np.sum(sig*rx/r2,0); Ey[k:k+4000]=np.sum(sig*ry/r2,0)
    return Ex.reshape(X.shape),Ey.reshape(X.shape)
def trajectories(th,a,w,both,kap,F,gx,gy,dt=0.005):
    Ex,Ey=F; n=len(th); p=np.stack([np.zeros(n),-Ds*np.ones(n)],1); v=np.stack([np.sin(th),np.cos(th)],1)
    alive=np.ones(n,bool); xhit=np.full(n,np.nan); g0=np.array([gx[0],gy[0]]); dg=np.array([gx[1]-gx[0],gy[1]-gy[0]])
    def acc(q):
        idx=((q-g0)/dg).T
        return kap*np.stack([map_coordinates(Ex,idx,order=1,mode='nearest'),map_coordinates(Ey,idx,order=1,mode='nearest')],1)
    for _ in range(int(40/dt)):
        if not alive.any(): break
        q=p[alive]; u=v[alive]
        k1v=acc(q); k1x=u; k2v=acc(q+0.5*dt*k1x); k2x=u+0.5*dt*k1v; k3v=acc(q+0.5*dt*k2x); k3x=u+0.5*dt*k2v
        k4v=acc(q+dt*k3x); k4x=u+dt*k3v
        qn=q+dt/6*(k1x+2*k2x+2*k3x+k4x); un=u+dt/6*(k1v+2*k2v+2*k3v+k4v)
        idx=np.where(alive)[0]
        cr=(q[:,1]<0)&(qn[:,1]>=0)
        xc=q[:,0]+(qn[:,0]-q[:,0])*(-q[:,1])/np.where(qn[:,1]!=q[:,1],qn[:,1]-q[:,1],1)
        op=np.abs(xc+a/2)<w/2
        if both: op|=np.abs(xc-a/2)<w/2
        near=(np.abs(qn[:,1])<rmin)&(np.abs(qn[:,0])<=Lb)&~(np.abs(qn[:,0]+a/2)<w/2-rmin)&~(both&(np.abs(qn[:,0]-a/2)<w/2-rmin))
        dead=(cr&~op&(np.abs(xc)<=Lb))|near
        hit=(qn[:,1]>=D)&~dead
        xhit[idx[hit]]=qn[hit,0]
        alive[idx[dead|hit]]=False
        p[idx]=qn; v[idx]=un
    return xhit
def run(a,w,kaps,N,nl=1500,gstep=0.05):
    gx=np.arange(-Lb-2,Lb+2+1e-9,gstep); gy=np.arange(-Ds-0.5,D+0.5+1e-9,gstep)
    F1=field_grid(a,w,False,N,gx,gy); F2=field_grid(a,w,True,N,gx,gy)
    c1=np.arctan((-a/2)/Ds); half=np.arctan((w/2)/Ds)*2.5
    th=np.linspace(c1-half,c1+half,nl)                 # launches around slit 1 (window x 2.5)
    out=[]
    for kap in kaps:
        h1=trajectories(th,a,w,False,kap,F1,gx,gy); h2=trajectories(th,a,w,True,kap,F2,gx,gy)
        ok1,ok2=~np.isnan(h1),~np.isnan(h2); both=ok1&ok2
        dxh=np.nanmax(np.abs(h2[both]-h1[both])) if both.any() else np.nan
        def folds(h):
            g=np.diff(h[~np.isnan(h)]); g=g[np.abs(g)<1.0]; return int(np.sum(np.diff(np.sign(g))!=0))
        # screen patterns: slit-1 launches; slit-2 launches by mirror symmetry
        bins=np.linspace(-12,12,241)
        I1=np.histogram(h1[ok1],bins)[0].astype(float); I2=I1[::-1]
        Ib1=np.histogram(h2[ok2],bins)[0].astype(float); Iboth=Ib1+Ib1[::-1]
        dark=int(np.sum((Iboth<np.minimum(I1,I2))&(I1>0)&(I2>0)))
        dev=Iboth-I1-I2; mins=int(np.sum((dev[1:-1]<dev[:-2])&(dev[1:-1]<dev[2:])&(np.abs(dev[1:-1])>2)))
        out.append(dict(kap=kap,abs1=int((~ok1).sum()),abs2=int((~ok2).sum()),dx=dxh,f1=folds(h1),f2=folds(h2),dark=dark,overlap=int(np.sum((I1>0)&(I2>0))),mins=mins,h1=h1,h2=h2,th=th))
    return out
if __name__=="__main__":
    print("2D grounded thin plate y=0, |x|<=%g; source (0,-%g); screen y=%g; v0=1; absorbed within %g of metal"%(Lb,Ds,D,rmin))
    print("\nConvergence (a=2, w=0.5, kappa=0.01; 50 launches): errors against N=800 for slit-1 launches")
    ref=None; res={}
    for N in (800,400,200):
        o=run(2.0,0.5,[0.01],N,nl=50)[0]; res[N]=o
    R=res[800]; dR=R['h2']-R['h1']
    for N in (200,400):
        m=~np.isnan(res[N]['h2'])&~np.isnan(R['h2'])&~np.isnan(res[N]['h1'])&~np.isnan(R['h1'])
        e=np.abs(res[N]['h2'][m]-R['h2'][m]); dd=np.abs((res[N]['h2']-res[N]['h1'])[m]-dR[m])
        print(f"   N={N}: x_hit error max {e.max():.3e} median {np.median(e):.3e}; error of the one-vs-two-slit shift max {dd.max():.3e} median {np.median(dd):.3e}; absorbed {res[N]['abs2']} vs {R['abs2']}")
    print(f"   N=800 one-vs-two-slit shift itself: max {np.nanmax(np.abs(dR)):.3e} median {np.nanmedian(np.abs(dR)):.3e}")
    print("\nScan (N=400, 1500 slit-1 launches per case, window 2.5x the slit's angular width):")
    print(" a    w    kappa   absorbed 1slit/2slit  max|dx_hit|(2-1)  folds 1slit/2slit  overlap bins  bins I_both<min(I1,I2)  local minima of I_both-I1-I2")
    for a in (2.0,4.0):
        for w in (0.5,1.0):
            for o in run(a,w,[1e-3,1e-2,1e-1],400):
                print(f" {a:<4} {w:<4} {o['kap']:<7g} {o['abs1']:>5}/{o['abs2']:<5}            {o['dx']:.3e}          {o['f1']}/{o['f2']}             {o['overlap']:>4}        {o['dark']:>4}                  {o['mins']}")
