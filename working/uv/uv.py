import numpy as npy
import matplotlib.pyplot as plt

n = 192
Du, Dv, F, k = 0.00016, 0.00008, 0.035, 0.065 
dh = 5/(n-1)
T = 8000
dt = .9 * dh**2 / (4*max(Du,Dv))
nt = int(T/dt)

uvinitial = npy.load('../../lessons/04_spreadout/data/uvinitial.npz')
U = uvinitial['U']
V = uvinitial['V']

def ftcs(U, V, nt, dt, dh):
    for n in range(nt):
        Un = U.copy()
        Vn = V.copy()

        U[1:-1,1:-1] = Un[1:-1,1:-1] + dt*( \
                (Du/(dh**2))*(Un[2:,1:-1] - 4*Un[1:-1,1:-1] + Un[:-2,1:-1] + Un[1:-1,2:] + Un[1:-1,:-2]) \
                - Un[1:-1,1:-1]*(Vn[1:-1,1:-1])**2 + F*(1 - Un[1:-1,1:-1])  )
                
        V[1:-1,1:-1] = Vn[1:-1,1:-1] + dt*( \
                (Dv/(dh**2))*(Vn[2:,1:-1] - 4*Vn[1:-1,1:-1] + Vn[:-2,1:-1] + Vn[1:-1,2:] + Vn[1:-1,:-2]) \
                + Un[1:-1,1:-1]*(Vn[1:-1,1:-1])**2 - (F+k)*Vn[1:-1,1:-1]  )
  
        U[-1,:] = U[-2,:]
        U[:,-1] = U[:,-2]
        U[0,:]= U[1,:]
        U[:,0]= U[:,1]

        V[-1,:] = V[-2,:]
        V[:,-1] = V[:,-2]
        V[0,:]= V[1,:]
        V[:,0]= V[:,1]
        
    return U

u_out = ftcs(U,V,nt,dt,dh)
print(u_out[100,::40])

