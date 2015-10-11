import numpy as npy
import matplotlib.pyplot as plt

def f(t, u, ms = 50.0, g = -9.81, rho = 1.091, r = 0.5, ve = 325, CD = 0.15, mpdot = 20):
    u_ = npy.zeros(3)

    # Mass u_[0]
    if t < 5 :
        u_[0] = -mpdot
    
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
    dt = 0.1

    t = npy.linspace(0, 40, int(40/dt))
    u = npy.zeros((3, int(40/dt)))
    u[0, 0] = 100

    i = solve(t, u, f, stop, dt)

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

