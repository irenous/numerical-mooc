import numpy as npy
import matplotlib.pyplot as plt

def f(t, u, ms = 50.0, g = -9.81, rho = 1.019, r = 0.5, ve = 325, CD = 0.15, mpdot = 20):
    u_ = npy.zeros(3)

    # Mass u_[0]
    if t < 5 :
        u_[0] = -mpdot
    else :
        u_[0] = 0
    
    # Height u_[1]
    u_[1] = u[2]

    # Speed u_[2]
    u_[2] = g - (0.5*rho*npy.pi*(r**2)*CD*u[2]*npy.abs(u[2]))/(ms+u[0])
    if t < 5 :
        u_[2] = u_[2] + (mpdot*ve)/(ms+u[0])

    return u_

def stop(t, u, step):
    return (u[1, step] < 0)

def solve(t, u, f_func, stop_func, dt):
    i = 0
    while True :
        t[i+1] = t[i] + dt
        u[:,i+1] = u[:,i] + dt*f_func(t[i], u[:,i])

        if stop_func(t, u, i) :
            break

        i = i + 1

if __name__ == "__main__":
    t = npy.linspace(0, 40, 4000)
    u = npy.zeros((3,4000))
    u[0, 0] = 100

    solve(t, u, lambda t, u: f(t, u), lambda t, u, i: stop(t, u, i), 0.01)

    print("Temps et vitesse du retour au sol :", t[-1], u[2,-1])
    print("Hauteur max et temps :", max(u[1,:])) #, t[h.index(max(h))])
    print("Vitesse max, temps et hauteur :", max(u[2,:])) #, t[v.index(max(v))], h[v.index(max(v))])

    print(u)

    plt.plot(t, u[0,:])
    plt.plot(t, u[1,:])
    plt.plot(t, u[2,:])
    plt.show()

