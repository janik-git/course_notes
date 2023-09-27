import numpy as np
import matplotlib.pyplot as plt


def draw_char():
    g = lambda x: x

    xmin = 0
    xmax = 2
    tmax = 1.2
    n = 30
    x0 = np.linspace(xmin, xmax, n)
    x = np.linspace(xmin, xmax, 200)
    # curves are x = x0 + g(x0)*t
    # so for t on the y axis we get t =  (x-x0)/(g(x0)) we add an epsilon to avoid division by 0
    for i in range(n):
        plt.plot(x, (x - x0[i]) / (g(x0[i]) + 1e-16), "k-")

    plt.ylim([0, tmax])
    plt.xlabel("x")
    plt.ylabel("t")
    plt.show()

def draw_task4():
    def t(x,x0):
        if x0 <= 0 :
            return x-x0
        elif 0<x0 and x0<=1:
            return (x-x0)/(1-x0)
        else :
            return 0
    xmin = 0
    xmax = 1
    tmax = 1.2
    n = 30
    x0 = np.linspace(xmin, xmax, n)
    x = np.linspace(xmin, xmax, 200)
    # for t<=1 
    new_t = np.vectorize(t)
    for i in range(n):
        plt.plot(x, new_t(x,x0[i]), "k-")

    xmin = 0
    xmax = 1
    tmax = 1.2
    n = 30
    x = np.linspace(1.2, 2, 200)
    # for t > 1  x >t 
    for i in range(n):
        plt.plot(x, x0[i]*np.ones((200,)), "k-")

    x = np.linspace(1, 1.2, 200)
    # for t > 1  x < t
    for i in range(n):
        plt.plot(x, x, "k-")
    plt.ylim([0, tmax])
    plt.xlabel("x")
    plt.ylabel("t")
    plt.show()

draw_task4()
