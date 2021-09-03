
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#15.6

# Create a D6 and a D10.
die_1 = Die(8)
die_2 = Die(8)

#Make some rolls, and store them in a list
results = []
for roll_num in range(1_000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

#Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

#Visualize the results
x_values = list(range(2, max_result+1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D8 dice 1000 times',
	xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')


#15.7

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6 and a D10.
die_1 = Die()
die_2 = Die()
die_3 = Die()

#Make some rolls, and store them in a list
results = []
for roll_num in range(50_000):
	result = die_1.roll() + die_2.roll() + die_3.roll()
	results.append(result)

#Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

#Visualize the results
x_values = list(range(3, max_result+1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling three D6 50000 times',
	xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_d6.html')


#15.18
# Create a D6 and a D10.
die_1 = Die()
die_2 = Die()

#Make some rolls, and store them in a list
results = []
for roll_num in range(50_000):
	result = die_1.roll() * die_2.roll()
	results.append(result)

#Analyze the results.
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

#Visualize the results
x_values = list(range(2, max_result+1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of multiplying rolling a D6 and a D6 50000 times',
	xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_multiply.html')