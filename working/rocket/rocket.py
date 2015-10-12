import numpy as npy
import matplotlib.pyplot as plt

def mpdot(t):
    if t < 5.0 :
        return -20.0
    else:
        return 0.0

def f(t, u, mpdot_func, ms = 50.0, g = -9.81, rho = 1.091, r = 0.5, ve = 325, CD = 0.15):
    u_ = npy.zeros(3)

    # Mass u_[0]
    u_[0] = mpdot_func(t)
    
    # Height u_[1]
    u_[1] = u[2]

    # Speed u_[2]
    u_[2] = g - (0.5*rho*npy.pi*(r**2)*CD*u[2]*npy.abs(u[2]))/(ms+u[0]) - (u_[0]*ve)/(ms+u[0])

    return u_

def stop(t, u, i):
    return (u[1,i] < 0)

def solve(t, u, f_func, stop_func, dt):
    i = 0
    while True :
        u[:,i+1] = u[:,i] + dt*f_func(t[i], u[:,i])

        if stop_func(t, u, i) :
            return i

        i = i + 1

if __name__ == "__main__":
    t_to_sim = 40.0
    dt = 0.1

    t = npy.linspace(0, t_to_sim, int(t_to_sim/dt))
    u = npy.zeros((3, int(t_to_sim/dt)))
    u[0, 0] = 100.0

    i = solve(t, u, lambda t, u: f(t, u, mpdot), stop, dt)

    print("Temps et vitesse du retour au sol :", t[i], u[2, i])
    hmax = npy.amax(u[1,:])
    hmax_i = npy.argmax(u[1,:])
    print("Hauteur max et temps :", hmax, t[hmax_i])
    vmax = npy.amax(u[2,:])
    vmax_i = npy.argmax(u[2,:])
    print("Vitesse max, temps et hauteur :", vmax, t[vmax_i], u[1, vmax_i])

    plt.plot(t, u[0,:])
    plt.plot(t, u[1,:])
    plt.plot(t, u[2,:])
    plt.show()

