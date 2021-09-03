#11.1
def city_string(city_name, country, population = ''):
	"""Create a string with city details"""
	if population:
		city_info = f"{city_name}, {country} - population {population}"
	else:
		city_info = f"{city_name}, {country}"
	
	return city_info

