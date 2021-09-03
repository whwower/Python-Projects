#16.1


import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# for index, column_header in enumerate(header_row):
	# 	print(index, column_header)
	
	# Get dates, and high and low temperatures from this file.
	dates, precipitations = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			precipitation = float(row[3])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:	
			dates.append(current_date)
			precipitations.append(precipitation)
			
# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precipitations, c = 'black', alpha = 0.5)


#Format plot
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall (mm)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()






