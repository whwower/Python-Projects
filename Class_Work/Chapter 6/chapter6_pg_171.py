#6.7
my_self = {'name' : 'Manex', 'surname' : 'Tonz', 'age' : 25, 'city' : 'Randburg'}
friend = {'name' : 'Irene', 'surname' : 'Nyasha', 'age' : 28, 'city' : 'Midrand'}
stranger = {'name' : 'God', 'surname' : 'Mama', 'age' : 21, 'city' : 'Uzumba'}

people = [my_self, friend, stranger]
for person in people:
	full_name = f"{person['name']} {person['surname']}"
	print(full_name)
print("\n")	

#6.9
favourite_places = {
	'peter' : ['Capetown', 'Harare', 'Durban'],
	'manex' : ['Joburg', 'Capetown'],
	'tim' : ['Pretoria', 'Harare']
}
for people, favourite_place in favourite_places.items():
	print(f"The favourite places for {people} are: ")
	for place in favourite_place:
		print(place)

#6.11
cities = {
	'Harare' : {'country' : 'Zimbabwe', 'population' : 5_000_000, 'fact' : 'landlocked'},
	'Durban' : {'country' : 'south africa', 'population' : 3_000_000, 'fact' : 'seaport'},
	'Lusaka' : {'country' : 'Zambia', 'population' : 4_000_000, 'fact' : 'seaport'}
}
for city, details in cities.items():
	print(f"\nCity : {city}")
	description = f"{details['country']} has an estimated population of {details['population']} and is a {details['fact']} city"
	print(description)