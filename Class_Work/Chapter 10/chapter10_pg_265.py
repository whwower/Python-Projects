#10.3
name = input("Enter your name")
file_name = 'guests.txt'
with open(file_name, 'a') as file_object:
	file_object.write(name)

#10.4
def guest_book():
	
	while True:
		name = input("Please enter your name")
		if name == 'q':
			break
		else:
			print(f"Greetings {name}, welcome\n")
			file_name = 'guest_book.txt'
			with open(file_name, 'a') as file_object:
				file_object.write(name)

guest_book()