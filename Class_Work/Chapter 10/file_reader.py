# with open('pi_digits.txt') as file_object:
# 	contents = file_object.read()
# print(contents.rstrip())

# with open('pi_digits.txt') as file_object:
# 	for line in file_object:
# 		print(line)

# filename = 'pi_digits.txt'
# with open(filename) as file_object:
# 	lines = file_object.readlines()
# for line in lines:
# 	print(line.rstrip())

# filename = 'pi_digits.txt'
# with open(filename) as file_object:
# 	lines = file_object.readlines()
# pi_string = ""
# for line in lines:
# 	pi_string += line.strip()
# birthday = input("Enter you birthday, in the form mmddyy")
# if birthday in pi_string:
# 	print("Your birthday appears in the first milloino digis of pi")
# else:
# 	print("Your birthday does not appear in the first million if pi")
# print(pi_string)
# print(len(pi_string))

# filename = 'programming.txt'
# with open(filename, 'w') as file_object:
# 	file_object.write("Python is the best")
# with open(filename, 'a') as file_object:
# 	file_object.write("\nI also love finding meaning in a large database.\n")
# 	file_object.write("I love creating apps that can run on a browser.\n")

# try:
# 	print(5/0)
# except ZeroDivisionError:
# 	print("You cán't divide by zero")

# print("Give me two ny=umbers and I will divide them")
# print("Enter 'q' to quit")
# while True:
# 	first_number = input("\nFirst number")
# 	if first_number == 'q':
# 		break
# 	second_number = input("\nSecond Number")
# 	if second_number == 'q':
# 		break
# 	try:
# 		answer = int(first_number)/int(second_number)
# 	except ZeroDivisionError:
# 		print("You can't divide by 0!")
# 	else:
# 		print(answer)

# filename = 'alice.txt'
# try:
# 	with open(filename, encoding = 'utf-8') as f:
# 		contents = f.read()
# except FileNotFountError:
# 	print(f"Sorry, the file {filename} does not exist.")
# else:
# 	#Count the approximate number of words in the file
# 	words = contents.split()
# 	num_words = len(words)
# 	print(f"The file {filename} has about {num_words} words")

# def count_words(filename):
# 	"""Count the approximat number of words in the file"""
# 	try:
# 		with open(filename, encoding = 'utf-8') as f:
# 			contents = f.read()
# 	except FileNotFountError:
# 		#print(f"Sorry, the file {filename} does not exist.")
# 		pass
# 	else:
# 		#Count the approximate number of words in the file
# 		words = contents.split()
# 		num_words = len(words)
# 		print(f"The file {filename} has about {num_words} words")

# filename = 'alice.txt'
# count_words(filename)
# print("Continue with program")


# import json

# numbers = [2,3,5,11,13]

# filename = 'numbers.json'
# with open(filename, 'w') as f:
# 	json.dump(numbers, f)


# import json

# filename = 'numbers.json'
# with open(filename) as f:
# 	numbers = json.load(f)
# print(numbers)


# import json

# username = input("What is your name? ")

# filename = 'username.json'
# with open(filename, 'w') as f:
# 	json.dump(username, f)
# 	print(f"We'll remember you when you come back, {username}")
# 	

# import json

# filename = 'username.json'

# with open(filename) as f:
# 	username = json.load(f)
# 	print(f"Welcome back, {username}! ")


# import json
# # Load the username, if it has been stored previously.
# # Otherwise, prompt for the username and store it.
# filename = 'username.json'
# try:
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     username = input("What is your name? ")
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#         print(f"We'll remember you when you come back, {username}!")
# else:
#     print(f"Welcome back, {username}!")

# def greet_user():
# 	"""Greet user by name"""
# 	filename = 'username.json'
# 	try:
# 		with open(filename) as f:
# 			username = json.load(f)
# 	except FileNotFountError:
# 		username = input("What is your name? ")
# 		with open(username, f)
# 		print(f"We'll remember you when you come back {username}!")
# 	else:
# 		print(f"Welcome back {username}")
# greet_user()



def get_stored_username():
	"""get stored username if available"""
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFountError:
		return FileNotFountError
	else:
		return username
def greet_new_user():
	"""Prompt for a new username"""
	username = input("What is your name")
	filename = 'username.json'
	with open(filename, 'w') as f:
	    json.dump(username, f)
	return username
	
def greet_user():
	"""Greet the user by name"""
	username = get_stored_username()
	if username:
		print(f"WElcome back {username}!")
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back again {username}! ")	
greet_user()