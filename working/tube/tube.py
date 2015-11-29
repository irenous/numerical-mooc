# We import the libraries we will need
import numpy as npy

# We define the relation function
def f_u(u, gamma = 1.4):
    f_u = npy.empty(u.shape)

    f_u[:,0] = u[:,1]
    f_u[:,1] = (u[:,1]**2)/u[:,0] + (gamma - 1)*(u[:,2] - 0.5*((u[:,1]**2)/u[:,0]))
    f_u[:,2] = (u[:,2] + (gamma - 1)*(u[:,2] - 0.5*((u[:,1]**2)/u[:,0])))*(u[:,1]/u[:,0])

    return f_u
    
# Simulation conditions
dx = .25
nx = 81

dt = .0002
t_to_sim = .01
nt = int(t_to_sim/dt)

# Initial conditions
ICL = npy.array([1, 0, 100000])
ICR = npy.array([.125, 0, 10000])

u0 = npy.empty((nx,3))
u0[0:40, 0] = ICL[0]
u0[40:81, 0] = ICR[0]
u0[0:40, 1] = ICL[0]*ICL[1]
u0[40:81, 1] = ICR[0]*ICR[1]
u0[0:40, 2] =  ICL[2]/(1.4 - 1) + 0.5*ICL[0]*ICL[1]**2
u0[40:81, 2] = ICR[2]/(1.4 - 1) + 0.5*ICR[0]*ICR[1]**2

# Solve function
def solve(u_t0, f, dt, dx, nt):
    u = u_t0.copy()
    unh = u_t0.copy()

    for n in range(1, nt):
        un = u.copy()
        Fn = f(un)

        # Predictor
        unh[:-1] = 0.5*(un[1:]+un[:-1]) - 0.5*dt/dx*(Fn[1:]-Fn[:-1])
        Fnh = f(unh)

        # Corrector
        u[1:] = un[1:] - dt/dx*(Fnh[1:]-Fnh[:-1]) 
        u[0] = u_t0[0]

    return u

u_out_2_5 = solve(u0, f_u, dt, dx, nt)[50,:]

print("Density : ", u_out_2_5[0])
print("Velocity : ", u_out_2_5[1]/u_out_2_5[0])
print("Pressure : ", (u_out_2_5[2] - 0.5*(u_out_2_5[1]/u_out_2_5[0])**2)*(1.4 - 1))

