"""S5 structure-only toy (batch 28). Classical, no weights, no measure, no Born input.
2D flat plane, idealised seam-glued micro-handle (#408-style, not analytic):
mouths are disks of radius a centred at M1, M2 (|M1-M2| <= 2*ell, so both lie in a common ell-ball).
A straight-line test particle entering mouth 1 exits mouth 2 at the mapped point with its direction
rotated by the gluing twist theta (theta=0: untwisted translation gluing), and vice versa.
Emitter at origin, coarse launch direction +x fixed by Rec0 to angular resolution tau/R.
Detectors: N_det apertures of width Delta on the line x=R, centred at y_j = j*Delta.
Outputs which detector index each (world, sub-ell launch datum) reaches. No counting of worlds."""
import numpy as np
ell=1.0; a=0.3; R=1e4; Delta=50.0; tau=10.0; N=21
M1=np.array([5.0,0.0]); M2=np.array([5.0,1.6])           # mouths in a common ell-ball (|M1-M2|=1.6<=2ell)
def rot(v,t): c,s=np.cos(t),np.sin(t); return np.array([c*v[0]-s*v[1], s*v[0]+c*v[1]])
def hit_disk(p,d,c):
    q=p-c; b=q@d; disc=b*b-(q@q-a*a)
    if disc<0: return None
    s=-b-np.sqrt(disc); return s if s>1e-9 else None
def run(y0,phi,theta,maxpass=50):
    p=np.array([0.0,y0]); d=np.array([np.cos(phi),np.sin(phi)]); n=0
    while n<maxpass:
        hits=[(s,i) for i,c in enumerate((M1,M2)) if (s:=hit_disk(p,d,c)) is not None]
        if not hits: break
        s,i=min(hits); x=p+s*d; src,dst=((M1,M2),(M2,M1))[i]; t=theta if i==0 else -theta
        p=dst+rot(x-src,t); d=rot(d,t); p=p+1e-7*d; n+=1   # exit at mapped point, rotated direction
    if d[0]<=0: return None,n                                # never reaches x=R
    y=p[1]+(R-p[0])/d[0]*d[1]; j=int(np.round(y/Delta))
    return (j if abs(y-j*Delta)<=Delta/2 and abs(j)<=N//2 else None), n
print(f"ell={ell} a={a} R={R} Delta={Delta} tau={tau} M1={M1} M2={M2}")
for theta in [0.0,0.005,0.02,0.1,0.5,np.pi/2]:
    res={}
    for y0 in np.linspace(-0.5,0.5,201):                     # sub-ell launch offsets
        for phi in np.linspace(-0.4*tau/R,0.4*tau/R,5):     # direction within Rec0's resolution
            j,n=run(y0,phi,theta); res.setdefault(j,0); res[j]=1
    print(f"theta={theta:.4f}: detectors reached (None = no detector) = {sorted(res,key=lambda x:(x is None,x))}")
