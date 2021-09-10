import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [1, 2, 4, 8, 16]

x2 = [1, 2, 3, 4, 5]
y2 = [1, 3, 9, 13, 16]

x3 = [1, 2, 3, 4, 5]
y3 = [2, 4, 6, 8, 10]

plt.plot(x1, y1, 'r-', label = 'test')
plt.plot(x2, y2, 'b-s', label = 'assignment')
plt.plot(x3, y3, 'g-o', label = 'exam')
plt.legend(loc = 'best')

plt.title("My Title")
plt.xlabel("Horizontal Label")
plt.ylabel("Vertical Label")
plt.show()