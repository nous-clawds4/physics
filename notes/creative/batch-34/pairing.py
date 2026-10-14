"""Batch 34 point (3): leftover (unpaired) count vs resultant length |sum e^{i phi}|.
Classical toy, no weights, no Born input. Phases are dots on a circle; a pair is removed
if their phases are opposite within tolerance delta (relative pi), matched greedily
(each dot, in random order, takes the nearest unmatched dot within delta of antipodal).
Families: von Mises phases with concentration kappa (kappa=0 uniform)."""
import numpy as np
rng=np.random.default_rng(34)
def leftover(phi,delta):
    n=len(phi); free=np.ones(n,bool); order=rng.permutation(n)
    for i in order:
        if not free[i]: continue
        d=np.abs(np.angle(np.exp(1j*(phi-phi[i]-np.pi)))); d[~free]=9; d[i]=9
        j=np.argmin(d)
        if d[j]<=delta: free[i]=free[j]=False
    return free.sum()
N=400
print("N=%d"%N)
for delta in (0.05,0.2,0.5):
    rows=[]
    for kappa in (0,0.05,0.1,0.2,0.4,0.8,1.6,3.2):
        for rep in range(20):
            phi=rng.vonmises(0,kappa,N) if kappa>0 else rng.uniform(-np.pi,np.pi,N)
            R=abs(np.exp(1j*phi).sum()); rows.append((R,leftover(phi,delta)))
    a=np.array(rows); m=a[:,0]>5
    s=np.polyfit(np.log(a[m,0]),np.log(a[m,1]),1)[0]
    lo=a[:,1]/np.maximum(a[:,0],1)
    print(f"delta={delta}: log-log slope leftover vs R = {s:.2f}; leftover/R median {np.median(lo[m]):.2f}; min leftover-R {np.min(a[:,1]-a[:,0]):.1f}")
