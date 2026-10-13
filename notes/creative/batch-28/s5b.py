"""S5 rerun (batch 28), valid exterior-to-exterior seam gluings. Replaces the void s5.py
(wrong-side emergence: direction not normal-flipped; kept as a record).
Same host/detector parameters as s5.py. Mouth k: disk radius a at M_k; boundary point x = M_src + a e.
Gluings (theta = extra rotation of the seam):
  g1     : e' = R_theta e,        w' = R_theta d,          then flip normal: w' -> w' - 2(w'.e')e'
           (same seam point; non-orientable handle)
  mirror : e' = R_theta M e,      w' = R_theta M d (M = reflection along dhat = (M2-M1)/|M2-M1|),
           then the same normal flip (orientable handle)
Exit point M_dst + a e', direction pointing out of mouth dst (asserted).
Structure only: prints the SET of detector indices reached on a finite grid (a lower bound). No frequencies."""
import numpy as np, sys
ell=1.0; a=0.3; R=1e4; Delta=50.0; tau=10.0; N=21
M1=np.array([5.0,0.0]); M2=np.array([5.0,1.6]); dh=(M2-M1)/np.linalg.norm(M2-M1)
NY=int(sys.argv[1]) if len(sys.argv)>1 else 10001; NPHI=int(sys.argv[2]) if len(sys.argv)>2 else 11
def rot(v,t): c,s=np.cos(t),np.sin(t); return np.array([c*v[0]-s*v[1], s*v[0]+c*v[1]])
def hit_disk(p,d,c):
    q=p-c; b=q@d; disc=b*b-(q@q-a*a)
    if disc<0: return None
    s=-b-np.sqrt(disc); return s if s>1e-9 else None
def emerge(x,src,dst,d,theta,mode):
    e=(x-src)/a
    if mode=='mirror': e=e-2*(e@dh)*dh; d=d-2*(d@dh)*dh
    e2=rot(e,theta); w=rot(d,theta); w=w-2*(w@e2)*e2
    p=dst+a*e2; assert w@e2>=-1e-12, "inward exit"; return p,w
def run(y0,phi,theta,mode,maxpass=200):
    p=np.array([0.0,y0]); d=np.array([np.cos(phi),np.sin(phi)]); n=0
    while n<maxpass:
        hits=[(s,i) for i,c in enumerate((M1,M2)) if (s:=hit_disk(p,d,c)) is not None]
        if not hits: break
        s,i=min(hits); x=p+s*d; src,dst=((M1,M2),(M2,M1))[i]; t=theta if i==0 else -theta
        p,d=emerge(x,src,dst,d,t,mode); p=p+1e-9*d; n+=1
    if n==maxpass: return 'trapped'
    if d[0]<=0: return None
    y=p[1]+(R-p[0])/d[0]*d[1]; j=int(np.round(y/Delta))
    return j if abs(y-j*Delta)<=Delta/2 and abs(j)<=N//2 else None
key=lambda x:(isinstance(x,str), x is None, x if isinstance(x,int) else 0)
print(f"ell={ell} a={a} R={R} Delta={Delta} tau={tau} M1={M1} M2={M2} grid={NY}x{NPHI} (sets are lower bounds)")
for mode in ('g1','mirror'):
    for theta in [0.0,0.005,0.02,0.1,0.5,np.pi/2]:
        S=set(run(y0,phi,theta,mode) for y0 in np.linspace(-0.5,0.5,NY) for phi in np.linspace(-0.4*tau/R,0.4*tau/R,NPHI))
        print(f"{mode:6s} theta={theta:.4f}: {sorted(S,key=key)}",flush=True)
