"""Batch 20: two-route toy on a flat cylinder (one handle direction), test particle, no record.
Cover: flat plane (x,y). World W_L: x ~ x + L. Source at (0,0); screen = line y = D.
A test particle launched at angle theta (from the y axis) moves on a straight line in the cover and
hits the cover screen at X = D tan(theta). In W_L the screen point is x = X mod L, and the deck class
(winding relative to the declared reference 'straight segment in the fundamental strip [0,L)') is
n = floor(X / L).  (1) For a fixed launch, (x, n) as functions of L.  (2) Inverse: given an observed
hit x and the launch, the compatible worlds are L = (X - x)/n, n = 1, 2, ...  (a discrete family).
(3) Arrival time on the static source and screen clocks is D/(v cos theta) in every W_L, so timing does not separate worlds."""
import math
D=10.0; th=math.radians(35); X=D*math.tan(th)
print("launch theta=35 deg, D=10: cover hit X=%.6f"%X)
print("(1) hit x and class n vs gluing L:")
for L in [1.0,1.5,2.0,2.5,3.0,3.5,4.0,5.0,7.0,7.5,8.0]:
    n=math.floor(X/L); print("   L=%-4g x=%.4f  n=%d"%(L,X-n*L,n))
x_obs=X-2*2.5
print("(2) observed hit x=%.4f (true world L=2.5, n=2): compatible L = (X-x)/n:"%x_obs)
print("   ",[round((X-x_obs)/n,4) for n in range(1,9)], "... (and L must exceed x; n=0 needs x=X)")
print("    all with x < L:",[ (n,round((X-x_obs)/n,4)) for n in range(1,9) if (X-x_obs)/n> x_obs])
print("(3) arrival time D/(v cos th) is L-independent: timing carries no world information here.")
# (4) Fixed wrap, launch not recorded (Claude 017 S1): a hit at x fits one launch per route,
# theta_n = arctan((x + n L)/D); with aperture |D tan theta| < L only n = 0 and n = -1 remain.
L=2.5; x=X-2*L
cands=[(n,math.degrees(math.atan((x+n*L)/D))) for n in range(-3,4)]
print("(4) fixed L=2.5, hit x=%.4f: launches per route n:"%x, [(n,round(a,2)) for n,a in cands])
print("    within aperture |D tan th| < L:", [(n,round(a,2)) for n,a in cands if abs(x+n*L)<L])
