import numpy as npy
import matplotlib.pyplot as plt


def func(t, v, mp0):
    mp = mp0 - t*20
    if mp < 0 :
        mp = 0

    v_ = -9.81 - (0.5*1.091*npy.pi*0.25*0.15*v*npy.abs(v))/(50+mp)
    if t < 5 :
        v_ = v_ +(20*325)/(50+mp)

    return v_

def stop(h, v, step):
    h.append(h[-1] + v[-1]*step) #v[-1] ou v[-2] ? : on prend la vitesse de cette itération est celle d'avant ?

    return (h[-1] < 0)

def solve(x, y, f_func, stop_func, dx):
    i = 0
    while True :
        x.append(x[i] + dx)
        y.append(y[i] + dx*f_func(x[i], y[i]))

        if stop_func(x, y, i) :
            break

        i = i + 1

if __name__ == "__main__":
    t = [0]
    h = [0]
    v = [0]

    solve(t, v, lambda x, y: func(x, y, 100), lambda x, y, i: stop(h, y, 0.001), 0.001)

    print("Temps et vitesse du retour au sol :", t[-1], v[-1])
    print("Hauteur max et temps :", max(h), t[h.index(max(h))])
    print("Vitesse max, temps et hauteur :", max(v), t[v.index(max(v))], h[v.index(max(v))])

    plt.plot(t,h)
    plt.plot(t,v)
    plt.show()

