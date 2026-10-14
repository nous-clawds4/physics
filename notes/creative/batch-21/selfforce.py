"""Batch 21 Set B: self-field of a test charge on a flat cylinder (x ~ x + L), test model.
Space R^3 with x identified mod L; a charge q in uniform motion (velocity v, any direction) has images
at r + m L xhat, all moving with the same velocity.  The field of each uniformly moving image at the
particle's present position is the Heaviside (Lienard-Wiechert, uniform-motion) field
   E_m = q (1 - v^2) Rhat / (R^2 (1 - v^2 sin^2 psi)^{3/2}),  R = r - r_m = -m L xhat,
with psi the angle between v and R.  B_m = v x E_m.  Sum the Lorentz force over m = +-1..+-M.
Also: hit positions on the screen y = D vs launch angle (straight lines if the self-force vanishes)."""
import numpy as np
def self_force(v,L=1.0,M=2000):
    v=np.array(v,float); F=np.zeros(3); v2=v@v
    for m in list(range(-M,0))+list(range(1,M+1)):
        R=np.array([-m*L,0,0]); Rn=np.linalg.norm(R); Rh=R/Rn
        s2=1-((v@Rh)**2/v2 if v2>0 else 0)
        E=(1-v2)*Rh/(Rn**2*(1-v2*s2)**1.5)
        F+=E+np.cross(v,np.cross(v,E))
    return F
for v in [(0,0,0),(0.3,0,0),(0,0.5,0),(0.4,0.4,0),(0.2,0.5,0.3)]:
    print("v=%s  net self-force (q^2=1, L=1) = %s"%(v,np.round(self_force(v),12)))
D,L=10.0,2.5
th=np.radians(np.linspace(-6,15,22)); x=np.mod(D*np.tan(th),L); n=np.floor(D*np.tan(th)/L).astype(int)
print("hit x vs launch (deg): strictly monotone within each route; no bunching:")
for a,b,c in zip(np.degrees(th),x,n): print("   %6.2f  x=%.4f  n=%d"%(a,b,c))
