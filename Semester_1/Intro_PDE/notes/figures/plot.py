import numpy as np
import matplotlib.pyplot as plt

g = lambda x:x 

xmin = 0
xmax = 2
tmax = 1.2
n = 30
x0 = np.linspace(xmin, xmax, n)
x = np.linspace(xmin, xmax, 200)
# curves are x = x0 + g(x0)*t
# so for t on the y axis we get t =  (x-x0)/(g(x0)) we add an epsilon to avoid division by 0
for i in range(n):
    plt.plot(x, (x-x0[i])/(g(x0[i])+1e-16), 'k-')

plt.ylim([0, tmax])
plt.xlabel('x')
plt.ylabel('t')
plt.show()
