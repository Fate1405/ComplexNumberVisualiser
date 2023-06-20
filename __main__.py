import numpy as np
from matplotlib import pyplot as plt
from CNum import CNum
from mpl_toolkits import mplot3d

plt.style.use("fivethirtyeight")

def f(a: float, b: float = 0) -> float:

    res = CNum(a, b)

    return (res * res).mag()

g = np.vectorize(f)

x = np.arange(-10, 10, 0.1)
y = np.arange(-10, 10, 0.1)

X, Y = np.meshgrid(x, y)

Z = g(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')

plt.xlabel("Real")
plt.ylabel("Imaginary")

ax.plot_surface(X, Y, Z)

ax.set_zlabel("Magnitude of Output")

plt.show()