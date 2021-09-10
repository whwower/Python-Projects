import matplotlib.pyplot as plt 

values = [16, 18, 4, 8]
pielabels = ['Python', 'Ruby', 'Java', 'Perl']
piecolors = ['red', 'orange', 'yellow', 'maroon']
pieexplodes = [0.1, 0.1, 0.1, 0.1]

plt.pie(values, labels = pielabels, explode = pieexplodes, colors = piecolors)
plt.title("Pie Chart")
plt.xlabel("Horizontal title")
plt.ylabel("Vertical title")
plt.legend(loc = "best")
plt.show()