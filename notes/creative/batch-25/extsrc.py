"""Batch 25 extended-source scan (Set 7 dark-band test with overlapping one-slit patterns).
Same model as walls.py (imported unchanged): 2D grounded thin plate, BEM, R0 = 1, quasi-static image force,
kappa = q^2/(2 pi eps0 m v0^2). The point source is replaced by a source segment y=-Ds, |x|<=S, with
S = f * S_min, S_min = (a - w)(Ds + D)/(2D), f in {1.5, 3} (fixed margins; with straight lines the one-slit
patterns then overlap). Launches: uniform source positions x uniform theta over the angles that reach slit 1
(+- one slit width), a histogram convention, not a probability rule. Slit-2 launches by mirror symmetry
(the source is symmetric). Screen bins 0.1 wide. In overlap bins (I_1 > 0 and I_2 > 0):
z = (min(I_1, I_2) - I_both) / sqrt(I_both + min(I_1, I_2)) (Poisson convention); a dark bin needs z > 3.
Periodicity: local minima of dev = I_both - I_1 - I_2 with |dev| > 3 sigma, and the largest nonzero
FFT peak of dev over the overlap region relative to its mean amplitude."""
import numpy as np
from walls import field_grid, Lb, Ds, D, rmin
from scipy.ndimage import map_coordinates
def traj(x0,th,a,w,both,kap,F,gx,gy,dt=0.005):
    Ex,Ey=F; n=len(th); p=np.stack([x0,-Ds*np.ones(n)],1); v=np.stack([np.sin(th),np.cos(th)],1)
    alive=np.ones(n,bool); xhit=np.full(n,np.nan); g0=np.array([gx[0],gy[0]]); dg=np.array([gx[1]-gx[0],gy[1]-gy[0]])
    def acc(q):
        idx=((q-g0)/dg).T
        return kap*np.stack([map_coordinates(Ex,idx,order=1,mode='nearest'),map_coordinates(Ey,idx,order=1,mode='nearest')],1)
    for _ in range(int(40/dt)):
        if not alive.any(): break
        idx=np.where(alive)[0]; q=p[idx]; u=v[idx]
        k1v=acc(q); k1x=u; k2v=acc(q+0.5*dt*k1x); k2x=u+0.5*dt*k1v; k3v=acc(q+0.5*dt*k2x); k3x=u+0.5*dt*k2v
        k4v=acc(q+dt*k3x); k4x=u+dt*k3v
        qn=q+dt/6*(k1x+2*k2x+2*k3x+k4x); un=u+dt/6*(k1v+2*k2v+2*k3v+k4v)
        cr=(q[:,1]<0)&(qn[:,1]>=0)
        xc=q[:,0]+(qn[:,0]-q[:,0])*(-q[:,1])/np.where(qn[:,1]!=q[:,1],qn[:,1]-q[:,1],1)
        op=np.abs(xc+a/2)<w/2
        if both: op|=np.abs(xc-a/2)<w/2
        near=(np.abs(qn[:,1])<rmin)&(np.abs(qn[:,0])<=Lb)&~(np.abs(qn[:,0]+a/2)<w/2-rmin)&~(both&(np.abs(qn[:,0]-a/2)<w/2-rmin))
        dead=(cr&~op&(np.abs(xc)<=Lb))|near; hit=(qn[:,1]>=D)&~dead
        xhit[idx[hit]]=qn[hit,0]; alive[idx[dead|hit]]=False; p[idx]=qn; v[idx]=un
    return xhit
def case(a,w,kaps,N,fs=(1.5,3.0),ns=60,nt=200):
    gx=np.arange(-Lb-2,Lb+2+1e-9,0.05); gy=np.arange(-Ds-0.5,D+0.5+1e-9,0.05)
    F1=field_grid(a,w,False,N,gx,gy); F2=field_grid(a,w,True,N,gx,gy); res=[]
    Smin=(a-w)*(Ds+D)/(2*D)
    for f in fs:
        S=f*Smin; xs=np.linspace(-S,S,ns); X0=[];TH=[]
        for x0 in xs:
            lo=np.arctan((-a/2-w-x0)/Ds); hi=np.arctan((-a/2+w-x0)/Ds)
            X0+= [x0]*nt; TH+=list(np.linspace(lo,hi,nt))
        X0=np.array(X0); TH=np.array(TH); bins=np.arange(-15,15.0001,0.1)
        for kap in kaps:
            h1=traj(X0,TH,a,w,False,kap,F1,gx,gy); h2=traj(X0,TH,a,w,True,kap,F2,gx,gy)
            I1=np.histogram(h1[~np.isnan(h1)],bins)[0].astype(float); I2=I1[::-1]
            B=np.histogram(h2[~np.isnan(h2)],bins)[0].astype(float); Ib=B+B[::-1]
            ov=(I1>0)&(I2>0); m=np.minimum(I1,I2); sig=np.sqrt(np.maximum(Ib+m,1))
            z=np.where(ov,(m-Ib)/sig,-np.inf); dark=int(np.sum(z>3)); zmax=float(z[ov].max()) if ov.any() else np.nan
            dev=Ib-I1-I2; sd=np.sqrt(np.maximum(Ib+I1+I2,1))
            d=dev[ov]; s_=sd[ov]
            mins=int(np.sum((d[1:-1]<d[:-2])&(d[1:-1]<d[2:])&(np.abs(d[1:-1])>3*s_[1:-1]))) if len(d)>2 else 0
            if len(d)>8:
                sp=np.abs(np.fft.rfft(d-d.mean()))[1:]; fft=float(sp.max()/max(sp.mean(),1e-12))
            else: fft=np.nan
            res.append(dict(f=f,S=S,kap=kap,ov=int(ov.sum()),dark=dark,zmax=zmax,mins=mins,fft=fft,maxdev=float(np.max(np.abs(d)/s_)) if len(d) else np.nan,ntr=int((~np.isnan(h2)).sum())))
    return res
if __name__=="__main__":
    import sys
    print("Extended-source scan; source segment |x|<=S at y=-%g, screen y=%g; N=400 panels; R0=1 grounded plate; 60 source points x 200 angles per case"%(Ds,D))
    print(" a    w    f    S      kappa  transmitted(2 slits)  overlap bins  dark bins (z>3)  max z  max|dev|/sigma  dev minima>3sigma  FFT peak/mean")
    for a in (2.0,4.0):
        for w in (0.5,1.0):
            for o in case(a,w,[1e-3,1e-2,1e-1],400):
                print(f" {a:<4} {w:<4} {o['f']:<4} {o['S']:<6.3f} {o['kap']:<6g} {o['ntr']:>8}              {o['ov']:>4}          {o['dark']:>3}          {o['zmax']:6.2f}   {o['maxdev']:6.2f}          {o['mins']:>3}               {o['fft']:.2f}")
    print("\nSpot check N=800 (a=2, w=1, f=1.5, kappa=0.1):")
    o=case(2.0,1.0,[0.1],800,fs=(1.5,))[0]
    print(f"   overlap bins {o['ov']}, dark bins {o['dark']}, max z {o['zmax']:.2f}, max|dev|/sigma {o['maxdev']:.2f}, dev minima {o['mins']}")
