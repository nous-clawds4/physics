"""Geometry independent check of batch 15 (#382). Symbolic NEC + exact extrema/thresholds."""
import sympy as sp, mpmath as mp
t,x,th,ph=sp.symbols('t x theta phi',real=True); m,k,L=sp.symbols('m k L',positive=True)
R2=x**2+k**2; R=sp.sqrt(R2)
def G_mixed(gtt,gxx,RR):
    co=[t,x,th,ph]; g=sp.diag(-gtt,gxx,RR**2,RR**2*sp.sin(th)**2); gi=g.inv()
    Gam=[[[sp.simplify(sum(gi[a,d]*(sp.diff(g[d,b],co[c])+sp.diff(g[d,c],co[b])-sp.diff(g[b,c],co[d])) for d in range(4))/2) for c in range(4)] for b in range(4)] for a in range(4)]
    def Ric(b,c): return sp.simplify(sum(sp.diff(Gam[a][b][c],co[a])-sp.diff(Gam[a][b][a],co[c])+sum(Gam[a][a][d]*Gam[d][b][c]-Gam[a][c][d]*Gam[d][b][a] for d in range(4)) for a in range(4)))
    Rc=sp.Matrix(4,4,lambda b,c:Ric(b,c)); S=sp.simplify(sum(gi[a,a]*Rc[a,a] for a in range(4)))
    return sp.simplify(gi*Rc-S/2*sp.eye(4))
A=1-2*m/R
G=G_mixed(A,1/A,R)
rho=sp.simplify(-G[0,0]/(8*sp.pi)); pr=sp.simplify(G[1,1]/(8*sp.pi))
nec=sp.simplify(rho+pr)
print("symmetric toy: 8pi(rho+p_r) =",sp.factor(sp.simplify(8*sp.pi*nec)))
print(" at throat:",sp.simplify(8*sp.pi*nec.subs(x,0)),"; m=1,k=3:",sp.N(8*sp.pi*nec.subs({x:0,m:1,k:3})))
print(" large-x 8pi(rho+p_r) ~",sp.series(sp.simplify(8*sp.pi*nec.subs({m:1,k:3})),x,sp.oo,6))
print(" 8pi rho =",sp.factor(sp.simplify(8*sp.pi*rho)))
I=sp.integrate(sp.simplify(nec*4*sp.pi*R2),(x,-sp.oo,sp.oo))
print(" integral (rho+p_r) 4pi R^2 dx =",sp.simplify(I),"; m=1,k=3:",sp.N(I.subs({m:1,k:3})))
Ie=sp.integrate(sp.simplify(nec*4*sp.pi*R2/sp.sqrt(A)),(x,-sp.oo,sp.oo)) if False else None
# Ellis (m=0) reference
G0=G_mixed(sp.Integer(1),sp.Integer(1),R); n0=sp.simplify((-G0[0,0]+G0[1,1])/(8*sp.pi))
print("pure Ellis: 8pi(rho+p_r) =",sp.simplify(8*sp.pi*n0),"; integral 4piR^2 dx =",sp.integrate(sp.simplify(n0*4*sp.pi*R2),(x,-sp.oo,sp.oo)))
# exact potential and thresholds
mp.mp.dps=30
def V(xx,LL,mm=1,kk=3):
    RR=mp.sqrt(xx**2+kk**2); return (1-2*mm/RR)*(1+LL**2/RR**2)
for LL in [3.8,5]:
    dV=lambda xx:mp.diff(lambda y:V(y,LL),xx)
    xo=mp.findroot(dV,10 if LL<4 else 21); xb=mp.findroot(dV,3 if LL<4 else 1.8)
    Vo,Vb,V0=V(xo,LL),V(xb,LL),V(0,LL)
    print(f"L={LL}: well x={mp.nstr(xo,8)} V={mp.nstr(Vo,8)}; barrier x={mp.nstr(xb,8)} V={mp.nstr(Vb,8)}; throat V={mp.nstr(V0,8)}")
    if Vb<1:
        print("  thresholds (fixed L, xdot=dx/dtau):",mp.nstr(mp.sqrt(Vb-Vo),8),mp.nstr(mp.sqrt(1-Vo),8))
        # physical impulse: local radial boost of proper speed v in comoving frame -> E,L scale by gamma
        Ao=1-2/mp.sqrt(xo**2+9)
        Ec=mp.sqrt(Vo)
        def f(v,target):
            g=1/mp.sqrt(1-v**2); E2=(g*Ec)**2
            if target=='bar':
                Lp=g*LL; dVp=lambda y:mp.diff(lambda z:V(z,Lp),y); xbp=mp.findroot(dVp,xb); return E2-V(xbp,Lp)
            return E2-1
        vb=mp.findroot(lambda v:f(v,'bar'),0.2); ve=mp.findroot(lambda v:f(v,'esc'),0.3)
        print("  physical boost (proper speed in orbit frame) thresholds:",mp.nstr(vb,8),mp.nstr(ve,8))
