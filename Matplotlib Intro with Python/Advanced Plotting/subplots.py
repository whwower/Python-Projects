import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3]
y = [1, 2, 3]

fig = plt.figure()
fig.suptitle('Plot Title')

plt.subplot(1, 2, 1)
plt.plot(x, y, color = 'orange')
plt.xlabel('x1')
plt.ylabel('y1')

plt.subplot(1, 2, 2)
plt.plot(x, y, color = 'green')
plt.xlabel('x1')
plt.ylabel('y1')


plt.show()