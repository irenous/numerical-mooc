import numpy as npy
import matplotlib.pyplot as plt

def V(rho, rhomax = 250.0, Vmax = 22.22):
    return Vmax*(1-rho/rhomax)

def F(rho, rhomax = 250.0, Vmax = 22.22):
    return V(rho, rhomax, Vmax)*rho

def solve(rho, Fn, rho_x0, nt, dt, dx, Vmax=22.22):
    for n in range(1, nt):
        rhon = rho.copy()
        rho[1:] = rhon[1:]-dt/dx*(Fn[1:]-Fn[0:-1]) 
        rho[0] = rho_x0
        Fn = F(rho, Vmax=Vmax)

if __name__ == "__main__":
    L = 11000.0

    nx = 51
    dx = L/(nx-1)

    dt = 3.6

    # 3 min avg
    t_to_sim = 180
    nt = int(t_to_sim/dt)
    
    rho = npy.ones(nx)*10.0
    rho[10:20] = 50.0
    Fn = F(rho)

    solve(rho, Fn, 10.0, nt, dt, dx)

    print(npy.mean(V(rho)))

    # 6 min min
    t_to_sim = 360
    nt = int(t_to_sim/dt)
    
    rho = npy.ones(nx)*10.0
    rho[10:20] = 50.0
    Fn = F(rho)

    solve(rho, Fn, 10.0, nt, dt, dx)

    print(npy.amin(V(rho)))

    # 3 min avg and min
    t_to_sim = 180
    nt = int(t_to_sim/dt)
    
    rho = npy.ones(nx)*20.0
    rho[10:20] = 50.0
    Fn = F(rho, Vmax=37.78)

    solve(rho, Fn, 20.0, nt, dt, dx, 37.78)

    print(npy.mean(V(rho,Vmax=37.78)))
    print(npy.amin(V(rho,Vmax=37.78)))

