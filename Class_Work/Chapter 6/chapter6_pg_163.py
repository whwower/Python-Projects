#6.5
rivers = {
	'Nile' : 'Egypt',
	'Bangala' : 'Zim',
	'Tokwe' : 'Masvingo'
}
for key, value in rivers.items():
	print(f"{key} runs in {value}")
print("\n")
for river in rivers.keys():
	print(river)
print("\n")
for country in rivers.values():
	print(country)
print("\n")

#6.6
favourite_languages = {
	'Peter' : 'Java',
	'Enock' : 'C',
	'Manex' : 'Python'
}
my_people = ['Manex', 'Shingie']
for person in my_people:
	if person in favourite_languages.keys():
		print(f"\nThanks {person} for taking the poll")
	else:
		print(f"\n{person}, please take our poll")