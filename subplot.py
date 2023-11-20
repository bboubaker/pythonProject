import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
x = np.random.randn(10)
y = np.random.randn(10)
z = np.sin(np.sqrt(x**2 + y**2))
print([x, y, z])
#ax.scatter(x, y, z)
ax.plot_surface(x, y, z)
plt.show()
