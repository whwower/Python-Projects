#15.1 i

import matplotlib.pyplot as plt 

#Create the x-axix and the y-axis values
x_values = range(1, 6)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, color = 'red', s = 10)

#Create title, x-axis and y-axis for the plot
ax.set_title('Cubic Numbers', fontsize = 24)
ax.set_xlabel('Value', fontsize = 14)
ax.set_ylabel('Cube', fontsize = 14)

#Set tick parameters for the plot
ax.tick_params(axis = 'both', labelsize = 24)

#Set the range for each axis
ax.axis([0, 6, 0, 220])
plt.show()

#15.1 ii
#import matplotlib.pyplot as plt 

#Create the x-axix and the y-axis values
x_values = range(1, 18)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, color = 'red', s = 10)

#Create title, x-axis and y-axis for the plot
ax.set_title('Cubic Numbers', fontsize = 24)
ax.set_xlabel('Value', fontsize = 14)
ax.set_ylabel('Cube', fontsize = 14)

#Set tick parameters for the plot
ax.tick_params(axis = 'both', labelsize = 24)

#Set the range for each axis
ax.axis([0, 20, 0, 5_200])
plt.show()


#15.2
#import matplotlib.pyplot as plt 

#Create the x-axix and the y-axis values
x_values = range(1, 18)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, s = 10)

#Create title, x-axis and y-axis for the plot
ax.set_title('Cubic Numbers', fontsize = 24)
ax.set_xlabel('Value', fontsize = 14)
ax.set_ylabel('Cube', fontsize = 14)

#Set tick parameters for the plot
ax.tick_params(axis = 'both', labelsize = 24)

#Set the range for each axis
ax.axis([0, 20, 0, 5_200])
plt.show()
