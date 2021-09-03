#10.12
import json

def print_favourite_number():
	"""Access the file favourite number from json"""
	file_name = 'my_number_file.json'
	try:
		with open(file_name) as f:
			favourite_number = json.load(f)
	except FileNotFoundError:
		favourite_number = input("Please enter your favourite number")
		with open(file_name, 'w') as f:
			json.dump(favourite_number, f)
			print(f"We will remember your number {favourite_number}!")
	else:
		print(f"I know your favorite number! It’s {favourite_number}")

print_favourite_number()