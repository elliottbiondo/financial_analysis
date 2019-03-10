from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(0, 40, 0.5)
Y = np.arange(5, 10, 0.1)
X, Y = np.meshgrid(X, Y)
zs = np.array([np.power(1. + y/100, x) for x, y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)


# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.plasma, rstride=5, cstride=5,
                       linewidth=1, antialiased=True)
## Customize the z axis.
ax.set_zlim(1, 45)
ax.set_xlabel("Time (years)")
ax.set_ylabel("Annual Rate of Return (%)")
ax.set_zlabel("Value of a \$1 investment in 2018 (\$)")
plt.show()
