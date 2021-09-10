import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 1, 1, 1, 1, 1, 1]
z = [2, 4, 6, 8, 10, 12, 14]

ax.plot(x, y, z)
plt.show()