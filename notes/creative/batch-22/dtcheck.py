"""Batch 22 numerical check: is the fine-scale (~1 deg) jitter in delta resolved, or step-size noise?
Same model as echoes.py (L=2.5, v=0.5, tau=0.2, D=10, M=12); theta 0..5 deg in 0.25 deg steps at dt=0.01 and dt=0.005."""
import numpy as np
from echoes import deflection
D=10.0; th=np.radians(np.arange(0,5.01,0.25))
for dt in (0.01,0.005):
    dx=np.array([deflection(a,0.5,0.2,2.5,D,dt,12) for a in th]); d=-np.gradient(dx,th)/(D/np.cos(th)**2)
    print(f"dt={dt}: dx/eps", " ".join(f"{x:.4f}" for x in dx)); print(f"        delta/eps", " ".join(f"{x:.2f}" for x in d))
