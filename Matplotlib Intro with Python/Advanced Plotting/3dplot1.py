import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

x1 = np.random.rand(100)
x2 = np.random.rand(100)
x3 = np.random.rand(100)


ax.scatter(x1, x2, x3, s = 20, color = 'red', marker = '^')

plt.show()