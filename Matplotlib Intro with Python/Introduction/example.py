import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [2, 4, 6, 8, 7, 6, 5, 4]

plt.plot(x, y, 'b-s')
plt.axis([0, 10, 0, 10])
plt.title("My Title")
plt.xlabel("Horizontal Title")
plt.ylabel("Vertical Title")
plt.show()