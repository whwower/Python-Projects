import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# for index, column_header in enumerate(header_row):
	# 	print(index, column_header)

	brights, lons, lats, hover_texts = [], [], [], []
	for row in reader:
		bright = float(row[2])
		lon = row[1]
		lat = row[0]
		day_night = row[12]
		brights.append(bright)
		lons.append(lon)
		lats.append(lat)
		hover_texts.append(day_night)

#Map the fires
data = [{
	'type': 'scattergeo',
	'lon': lons,
	'lat': lats,
	'text': hover_texts,
	'marker': {
	'size': [bright/20 for bright in brights],
	'color': brights,
	'colorscale': 'Viridis',
	'reversescale': True,
	'colorbar': {'title': 'Brightness'},
	},
}]
my_layout = Layout(title= 'Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')