"""Batch 29: smooth analytic throat (2D Ellis neck ds^2 = dr^2 + (r^2 + a^2) dphi^2, r in R), geodesics integrated
numerically (scipy solve_ivp, DOP853, rtol 1e-11). This is a two-sheet neck, NOT a handle (a smooth analytic handle
is not computed). Emitter on sheet r > 0 at r = r_E, far from the throat; the ray is launched toward the throat with
impact parameter b (unit speed, angular momentum L = b). It is reflected (b > a: stays on sheet 1) or transmitted
(b < a: goes to sheet 2, recorded as 'other sheet'). For reflected rays, the asymptotic outgoing direction is read
off at r = r_out and the ray is continued straight (sheet 1 is flat to O(a^2/r^2) there) to a detector line at
distance R from the emitter, with 21 contiguous apertures of width Delta. Structure only: reached sets on a grid of b
(lower bounds). Check: numerical sweep vs the closed form 2K(a/b) (reflected), K = complete elliptic integral."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import ellipk
a=0.3; R=1e4; Delta=50.0; N=21; rE=60.0; rout=60.0
def geo(t,y):
    r,ph,pr=y; rho2=r*r+a*a
    return [pr, b_glob/rho2, r*b_glob**2/rho2**2]     # p_phi = L = b conserved; pr' = r L^2 / rho^4
def sweep(b):
    global b_glob; b_glob=b
    y0=[rE,0.0,-np.sqrt(max(1-b*b/(rE*rE+a*a),0))]
    ev=lambda t,y: abs(y[0])-rout-1e-6; ev.terminal=True; ev.direction=1
    sol=solve_ivp(geo,[0,1e4],y0,method='DOP853',rtol=1e-11,atol=1e-13,events=ev)
    r,ph,pr=sol.y[:,-1]; return r,ph
# asymptotic picture: incoming ray on sheet 1 along the direction of -x (toward the throat at the origin) from
# (rE,0) with offset b; after the encounter the outgoing direction angle (lab frame) is pi + sweep_total - ... :
# we use the standard relation: deflection = (total phi swept, corrected for the finite rE, rout) - pi.
def finite_corr(b): return np.arcsin(min(b/np.sqrt(rE*rE+a*a),1))+np.arcsin(min(b/np.sqrt(rout*rout+a*a),1))
print(f"a={a} rE={rE} rout={rout} R={R} Delta={Delta}")
# 1. check against the closed form (asymptotic sweep) at large rE is approximate; report the finite-r sweep + correction
for eps in (1e-1,1e-2,1e-4,1e-6):
    b=a*(1+eps); r,ph=sweep(b); tot=ph+finite_corr(b)
    print(f"b=a(1+{eps:g}): numerical sweep(+finite-r corr)={tot:.6f}  closed 2K(a/b)={2*ellipk((a/b)**2):.6f}")
# 2. reachability: emitter E, throat T at distance dET = rE along +x from E... detectors beyond, along the
#    deflected direction. Outgoing direction angle in the frame where the ray came in along +x: psi = pi - deflection'
#    with deflection' = tot - pi, so the outgoing direction makes angle (pi - tot) + pi ... we take lab angle
#    alpha_out = tot - pi measured from the reversed incoming axis; detectors sit back along -x? To keep the
#    statement frame-free we place the detector array on the line at distance R from the throat, perpendicular to
#    the direction delta0 = 0 (straight-through direction, i.e. +x continued), and record which aperture the
#    outgoing straight ray crosses.
reached=set(); other=False
bs=np.r_[a*(1+np.logspace(-9,0,4000)), a*(1-np.logspace(-9,-0.01,500))]
for b in bs:
    r,ph=sweep(b)
    if r<0: other=True; continue
    tot=ph+finite_corr(b); defl=tot-np.pi          # deflection from straight-through
    # outgoing ray: starts near the throat (impact offset b), direction angle defl (mod 2 pi) from +x
    ang=(defl+np.pi)%(2*np.pi)-np.pi
    if np.cos(ang)<=0: reached.add(None); continue
    y=b+R*np.tan(ang); j=int(np.round(y/Delta))
    reached.add(j if abs(y-j*Delta)<=Delta/2 and abs(j)<=N//2 else None)
print("reflected rays (sheet 1): detectors reached", sorted([k for k in reached if k is not None]), "None" if None in reached else "", "| transmitted rays exist:",other)
