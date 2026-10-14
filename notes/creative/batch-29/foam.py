"""Batch 29: several seam handles along the path (2D, structure only). Reachability of detectors; no counts of worlds,
no measure, no Born input. Widths/encounter numbers are diagnostics in the launch-offset coordinate, not sizes of W_i.
Host: flat plane tiled by square cells of side s (x > 5 - s/2, all y; for s > 10 the foam also lies behind the emitter). Cell (i,j) holds one handle: mouths are disks of
radius a at c1 = cell centre + u, c2 = c1 + (0, 1.6), with u a fixed pseudo-random offset (hash of i, j) keeping both
disks inside the cell. Cell (0,0) is overridden to the batch-28 handle (M1 = (5,0)); no foam at x < x0 = 5 - s/2. Needs s >= 4
(the override must fit cell (0,0)). Gluing G1 (non-orientable, theta = 0) or mirror (orientable, theta = 0), each with the normal flip;
outward exit asserted. With theta = 0, both gluings are involutive-consistent (mirror inverse = itself, G1 inverse =
identity rotation), so the 2->1 branch is exact (cf. Claude 019 S1).
Launch: from (0, y0), direction angle phi; y0 in [-0.5, 0.5] (sub-l), |phi| <= 0.4 tau/R. Detectors: 21 contiguous
apertures of width Delta at x = R. Outcome per ray: index j, None (crosses x = R outside the array, or leaves x < -s or |y| > 3R),
or 'cap' (no arrival within the step cap: diffusive/unresolved)."""
import numpy as np, sys, json
a=0.3; R=1e4; Delta=50.0; tau=10.0; N=21; D12=np.array([0.0,1.6])
def hashu(i,j,s):
    h1=np.sin(i*12.9898+j*78.233)*43758.5453; h2=np.sin(i*39.3468+j*11.135)*24634.6345
    f1=h1-np.floor(h1); f2=h2-np.floor(h2)
    mx=s/2-a-0.05; my=s/2-0.8-a-0.05              # keep both disks inside the cell (no overlaps)
    return np.stack([(2*f1-1)*mx,(2*f2-1)*my],-1)
def centres(i,j,s):
    """mouth-1 centre of the handle in cell (i,j); cell (0,0) holds M1=(5,0)."""
    x0=5.0-s/2                                     # cell (i,j) = [x0+i s, x0+(i+1) s] x [j s - s/2, j s + s/2]
    cc=np.stack([x0+(i+0.5)*s+0*j, j*s-0.8+0*i],-1) + hashu(i,j,s)   # handle pair centred at cell centre + u
    ov=(i==0)&(j==0)
    cc=np.where(ov[...,None], np.array([5.0,0.0]), cc)
    cc=np.where((i<0)[...,None], np.array([np.nan,np.nan]), cc)      # no foam at x < x0 (emitter side)
    return cc
def trace(y0,phi,s,mode,cap):
    n=len(y0); p=np.stack([np.zeros(n),y0],1).astype(float); d=np.stack([np.cos(phi)+0*y0,np.sin(phi)+0*y0],1)
    out=np.full(n,-99); enc=np.zeros(n,int); act=np.ones(n,bool); steps=np.zeros(n,int)
    x0=5.0-s/2
    for it in range(cap):
        idx=np.flatnonzero(act)
        if len(idx)==0: break
        P=p[idx]; Dd=d[idx]
        i=np.floor((P[:,0]-x0)/s).astype(int); j=np.floor((P[:,1]+s/2)/s).astype(int)
        # candidates: handles in the 3x3 block of cells around the ray (disks can sit near cell edges)
        best=np.full(len(idx),np.inf); bk=np.full(len(idx),-1); bc=np.zeros((len(idx),2)); bo=np.zeros((len(idx),2))
        for di in (-1,0,1):
            for dj in (-1,0,1):
                c1=centres(i+di,j+dj,s); 
                for k,C in ((0,c1),(1,c1+D12)):
                    q=P-C; b=(q*Dd).sum(1); disc=b*b-((q*q).sum(1)-a*a)
                    sh=-b-np.sqrt(np.where(disc>=0,disc,np.nan)); ok=(disc>=0)&(sh>1e-9)&(sh<best)
                    best[ok]=sh[ok]; bk[ok]=k; bc[ok]=C[ok]; bo[ok]=(C+(D12 if k==0 else -D12))[ok]
        # distance to leave the current cell (then re-evaluate neighbours)
        xl=x0+i*s; xr=xl+s; yl=j*s-s/2; yr=yl+s
        with np.errstate(divide='ignore',invalid='ignore'):
            tx=np.where(Dd[:,0]>0,(xr-P[:,0])/Dd[:,0],np.where(Dd[:,0]<0,(xl-P[:,0])/Dd[:,0],np.inf))
            ty=np.where(Dd[:,1]>0,(yr-P[:,1])/Dd[:,1],np.where(Dd[:,1]<0,(yl-P[:,1])/Dd[:,1],np.inf))
        tcell=np.minimum(tx,ty)+1e-9
        # detector plane / leaving the foam slab
        with np.errstate(divide='ignore',invalid='ignore'):
            tR=np.where(Dd[:,0]>0,(R-P[:,0])/Dd[:,0],np.inf)
        hit=bk>=0
        hitfirst=hit&(best<=tcell)&(best<tR)
        arrive=(~hitfirst)&(tR<=tcell)
        move=(~hitfirst)&(~arrive)
        # arrivals
        ia=idx[arrive]; ya=P[arrive,1]+tR[arrive]*Dd[arrive,1]; jj=np.round(ya/Delta).astype(int)
        good=(np.abs(ya-jj*Delta)<=Delta/2)&(np.abs(jj)<=N//2)
        out[ia]=np.where(good,jj,99); act[ia]=False
        # moves
        im=idx[move]; p[im]=P[move]+tcell[move,None]*Dd[move]
        lost=im[(p[im,0]<-s)|(np.abs(p[im,1])>3*R)]; out[lost]=99; act[lost]=False
        # seam passages
        ih=idx[hitfirst]; X=P[hitfirst]+best[hitfirst,None]*Dd[hitfirst]; V=Dd[hitfirst]
        src=bc[hitfirst]; dst=bo[hitfirst]; e=(X-src)/a; e/=np.linalg.norm(e,axis=1)[:,None]; V=V/np.linalg.norm(V,axis=1)[:,None]   # renormalise (rounding)
        refl=V-2*(V*e).sum(1)[:,None]*e
        if mode=='mirror':
            dh=np.array([0.0,1.0]); M=np.eye(2)-2*np.outer(dh,dh); e2=e@M.T; w=refl@M.T
        else: e2=e; w=refl
        assert ((w*e2).sum(1)>=-1e-6).all(), "inward exit"   # tolerance for grazing incidence
        p[ih]=dst+a*e2+1e-9*w; d[ih]=w; enc[ih]+=1
        steps[idx]+=1
    out[act]=-999                                   # cap: no arrival within the step cap
    return out,enc
if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else 'g1'; NY=int(sys.argv[2]) if len(sys.argv)>2 else 4001
    print(f"mode={mode} a={a} R={R} Delta={Delta} grid={NY}x3 offsets in [-0.5,0.5]; reached sets are lower bounds")
    for s in [5.0,10.0,20.0,50.0,110.0,200.0,500.0,2000.0]:
        cap=int(40*R/s)+200
        S=set(); E={}; capped=False
        for phi in np.linspace(-0.4*tau/R,0.4*tau/R,3):
            o,e=trace(np.linspace(-0.5,0.5,NY),phi,s,mode,cap)
            S|=set(o.tolist()); capped|=(o==-999).any()
            for k in set(o.tolist()):
                if k not in (99,-999): E.setdefault(k,set()).update(e[o==k].tolist())
        det=sorted(k for k in S if k not in (99,-999))
        encs=sorted(set().union(*E.values())) if E else []
        lam=s*s/(4*a)
        print(f"s={s:7.1f} l_free~s^2/(4a)={lam:9.1f} (R={R:.0f}): detectors reached {len(det)}/21 {det}; None={99 in S}; "
              f"no-arrival-within-cap={capped}; encounter numbers on arriving paths: min {encs[0] if encs else '-'} max {encs[-1] if encs else '-'}",flush=True)
