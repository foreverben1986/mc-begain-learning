import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import lib.linearRegression_data_read as xlsR
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


data = xlsR.readXls("data1.xlsx","data1")
x = []
y = []
z = []
for dataItem in data:
    x.append(dataItem[0])
    y.append(dataItem[1])
    z.append(dataItem[2])

X = np.array(x)
Y = np.array(y)
Z = np.array(z)
X, Y = np.meshgrid(x, y)
R = 20 * X + 10 * Y 
R = R  + 20
mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, label='parametric curve')

# Plot the surface.
surf = ax.plot_surface(X, Y, R, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-300, 300)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

ax.legend()

plt.show()
