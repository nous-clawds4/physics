"""Batch 29: is a multi-handle cluster a chaotic scatterer? (2D, structure only.)
Cluster: K x K seam handles (G1 or mirror, theta = 0, normal flip, outward exit asserted) on a square lattice of
spacing s0 in an otherwise flat plane. Rays come in from x = -20 along +x with offset y0. Outcome: exit-direction
sector (8 sectors) once its straight line meets no further mouth (Rout and mid are unused). Diagnostic (offset coordinate only,
not a measure): number of outcome changes C(n) on n equally spaced offsets in a fixed window, for n = 10^3..10^6.
Piecewise-smooth map: C(n) saturates. Fractal boundary (chaotic scattering): C(n) ~ n^D with 0 < D < 1, and the
passage number is unbounded near boundaries."""
import numpy as np, sys
a=0.3; D12=np.array([0.0,1.6])
def run(y0,K,s0,mode,cap=4000):
    C1=np.array([[i*s0, j*s0] for i in range(K) for j in range(K)],float); C2=C1+D12
    cen=np.vstack([C1,C2]); partner=np.r_[np.arange(K*K)+K*K, np.arange(K*K)]
    n=len(y0); p=np.stack([-20+0*y0, y0],1); d=np.tile([1.0,0.0],(n,1)); act=np.ones(n,bool); pas=np.zeros(n,int)
    Rout=3*K*s0+25; mid=C1.mean(0)+D12/2
    dh=np.array([0.0,1.0]); M=np.eye(2)-2*np.outer(dh,dh)
    for it in range(cap):
        idx=np.flatnonzero(act)
        if not len(idx): break
        P=p[idx]; V=d[idx]
        q=P[:,None,:]-cen[None]; b=(q*V[:,None,:]).sum(2); disc=b*b-((q*q).sum(2)-a*a)
        sh=-b-np.sqrt(np.where(disc>=0,disc,np.nan)); sh=np.where((disc>=0)&(sh>1e-9),sh,np.inf)
        k=np.argmin(sh,1); sm=sh[np.arange(len(idx)),k]
        esc=~np.isfinite(sm); act[idx[esc]]=False
        h=~esc; ih=idx[h]; kk=k[h]; X=P[h]+sm[h,None]*V[h]; src=cen[kk]; dst=cen[partner[kk]]
        e=(X-src)/a; e/=np.linalg.norm(e,axis=1)[:,None]; W=V[h]; refl=W-2*(W*e).sum(1)[:,None]*e
        if mode=='mirror': e=e@M.T; refl=refl@M.T
        assert ((refl*e).sum(1)>=-1e-9).all(), "inward exit"
        refl/=np.linalg.norm(refl,axis=1)[:,None]
        p[ih]=dst+a*e+1e-9*refl; d[ih]=refl; pas[ih]+=1
    ang=np.arctan2(d[:,1],d[:,0]); sec=np.floor((ang+np.pi)/(2*np.pi)*8).astype(int)%8
    sec[act]=-1
    return sec,pas
if __name__=='__main__':
    print("cluster scattering; outcome = exit sector (8); window y0 in [-1, 1+(K-1)*s0+1.6+1]; counts are offset-coordinate diagnostics")
    for mode in ('g1','mirror'):
        for K,s0 in ((1,4.0),(2,4.0),(3,4.0),(3,2.5)):
            lo,hi=-1.0,1.0+(K-1)*s0+2.6   # window covering every mouth row
            line=[]
            for n in (1000,10000,100000,1000000):
                y=np.linspace(lo,hi,n); out=[run(c,K,s0,mode) for c in np.array_split(y,max(1,n//50000))]
                sec=np.concatenate([o[0] for o in out]); pas=np.concatenate([o[1] for o in out])
                ch=int((np.diff(sec)!=0).sum()); line.append(f"n={n}: C={ch}, max passes={pas.max()}, unexited={(sec<0).any()}")
            print(f"{mode:6s} K={K} s0={s0}: "+"; ".join(line),flush=True)
