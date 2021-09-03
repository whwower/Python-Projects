# print("Hello python world")
# message = "Hell Python World"
# print(message)
# message = "Hello Python Crash Course World"
# print(message)
# message = "ada lovelace"
# print(message.title())
# favourite_Number = 25
# print(favourite_Number)
# bicycles = ['trek', 'cannondale', 'specialized']
# print(bicycles)
# print(bicycles[2])
# print(bicycles[2].title())
# message = f"My first bicycle was a {bicycles[1].title()}"
# print(message)

# motorcyles = ['honda', 'yamaha', 'suzuki']
# print(motorcyles)
# motorcyles.append('ducati')
# print(motorcyles)
# motorcyles[0] = 'fit'
# print(motorcyles)
# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)
# motorcycles.insert(0, 'ducati')
# print(motorcycles)
# del motorcycles[0]
# print(motorcycles)
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)
# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)
# firstOwned = motorcycles.pop(0)
# print(f"The first motorcyle I owned was a {firstOwned.title()}")
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.reverse()
# print(cars)
# print(len(cars))
# magicians = ['alice', 'david', 'carolica']
# for magician in magicians:
# 	print(magician)
# for magician in magicians:
# 	print(f"{magician.title()}, that was great trick!")
# pizzas = ['meat', 'BBQ', 'hawaiian', 'buffalo']
# for pizza in pizzas:
# 	print(f"I like, {pizza.title()}, pizza")
# print("I really love pizza")
# for values in range(1,7):
# 	print(values)
# numbers = list(range(1,6))
# print(numbers)
# even_numbers = list(range(2, 11, 2))
# print(even_numbers)
# odd_numbers = list(range(, 11, 5))
# print(odd_numbers)
squares = []
# for value in range(1, 11):
# 	square = value**2
# 	squares.append(square)
# print(squares)
# squares = [value**2 for value in range(1,11)]
# print(squares)
# for value in range(1, 21):
# 	print(value)
# numbers = list(range(1, 10000001))
# for number in numbers:
# 	print(number)
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# for player in players[:3]:
# 	print(player.title())
# my_foods = ['pizza', 'falafel', 'carrot cake']
# my_foods.append('cannoli')
# friends_foods = my_foods[:]
# friends_foods.append('ice cream')
# print("My favourite foods are:")
# print(my_foods)
# print("\nMy friend's favourite foods are:")
# print(friends_foods)
# dimensions = (10,20)
# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
# 	if car == 'bmw':
# 		print(car.upper())
# 	else:
# 		print(car.title())
# 5.1
# favouriteColor = 'white'
# print("Is favouriteColor == 'white'? I predict True")
# print(favouriteColor == 'white')

# print("\nIs favouriteColor == 'red'? I predict False")
# print(favouriteColor == 'red')

# age = 12
# if age < 4:
# 	price = 0
# elif age < 18:
# 	price = 25
# elif age < 65:
# 	price = 40
# else:
# 	price = 65
# print(f"Your admission cost is ${price}")

# alien_color = 'green'
# if alien_color == 'green':
# 	print("You earned 5 points")

# alein_color = 'red'
# if alein_color == 'green':
# 	print("You earned 5 points")
# elif alein_color != 'green':
# 	print("You earned 10 points")
# 5.4
# alein_color = 'red'
# if alein_color == 'green':
# 	print("You earned 5 points")
# else:
# 	print("You earned 10 points")
# 5.5
# alien_color = 'red'
# if alien_color == 'green':
# 	print("You got 5 points")
# elif alien_color == 'yellow':
# 	print("You earned 10 points")
# elif alien_color == 'red':
# 	print("You earned 15 point")
# else:
# 	print("You have no points")

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheess']
# for requested_topping in requested_toppings:
# 	print(f"Adding {requested_topping}")
# print("\nFinished making your pizza")

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheess']
# if requested_toppings:
# 	for requested_topping in requested_toppings:
# 		if requested_topping == 'green peppers':
# 			print("Sorry, we are out of green peppers now")
# 		else:
# 			print(f"Adding {requested_topping}")
# 	print("\nFinished making your pizza")
# else:
# 	print("Are you sure you want a plain pizza?")


# requested_toppings = []
# if requested_toppings:
# 	for requested_topping in requested_toppings:
# 		if requested_topping == 'green peppers':
# 			print("Sorry, we are out of green peppers now")
# 		else:
# 			print(f"Adding {requested_topping}")
# 	print("\nFinished making your pizza")
# else:
# 	print("Are you sure you want a plain pizza?")

# 5.8
# staffs = ['admin', 'secretary', 'consultant', 'personnel', 'cleaner']
# for staff in staffs:
# 	if staff == 'admin':
# 		print("Hello admin, would you like to see our status report")
# 	else:
# 		print(f"Hello {staff}, thank you for logging in again")

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'fast'}
# print(f"Original position: {alien_0['x_position']}")
# # Move alien to the right
# # Determine how far to move alien based on the current speed
# if alien_0['speed'] == 'slow':
# 	x_increment = 1;
# elif alien_0['speed'] == 'medium':
# 	x_increment = 2
# else:
# 	#This must be a fast alien
# 	x_increment = 3

# #The new position is the old position plus the increment
# alien_0['x_position'] = alien_0['x_position'] + x_increment

# print(f"New position: {alien_0['x_position']}")


# alien_0 = {'color' : 'green', 'points' : 5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)

# favourite_language = {
# 	'jen' : 'python',
# 	'sarah' : 'c',
# 	'edward' : 'ruby',
# 	'phil' : 'python'
# }
# language = favourite_language['edward'].title()
# print(f"Edward's favourite language is {language}")

# favourite_language = {
#  	'jen' : 'python',
#  	'sarah' : 'c',
#  	'edward' : 'ruby',
#  	'phil' : 'python'
#  }
# print_value = favourite_language.get('joe','No such name.')
# print(print_value)

# user_0 = {
# 	'username' : 'efermi',
# 	'first' : 'enrico',
# 	'last' : 'fermi'
# }
# for key, value in user_0.items():
# 	print(f"\nKey: {key}")
# 	print(f"Value: {value}")

# favourite_language = {
#  	'jen' : 'python',
#  	'sarah' : 'c',
#  	'edward' : 'ruby',
#  	'phil' : 'python'
#  }
# friends = ['phil', 'sarah']
# for name in favourite_language.keys():
#  	print(name.title())
#  	if name in friends:
#  		language = favourite_language[name].title()
#  		print(f"\t{name.title()}, I see you love {language}")

# favourite_language = {
#     'jen' : 'python',
#     'sarah' : 'c',
#     'edward' : 'ruby',
#     'phil' : 'python'
#  }
# if 'erin' not in favourite_language.keys():
#     print('Erin, please take our poll')

# favourite_languages = {
#     'jen' : 'python',
#     'sarah' : 'c',
#     'edward' : 'ruby',
#     'phil' : 'python'
# }
# for name in sorted(favourite_languages.keys()):
#     print(f"{name.title()}, thank yo for taking the poll")

# favourite_languages = {
#     'jen' : 'python',
#     'sarah' : 'c',
#     'edward' : 'ruby',
#     'phil' : 'python'
# }
# print("The following languages have been mentioned")
# for language in favourite_languages.values():
#     print(language)
# for language in set(favourite_languages.values()):
#     print(language.title())

# languages = {'python', 'ruby', 'python', 'c', 'c', 'c'}
# print(languages)

# alien_0 = {'color' : 'green', 'points' : '5'}
# alien_1 = {'color' : 'yellow', 'points' : '10'}
# alien_2 = {'color' : 'red', 'points' : '15'}

# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

# #Make an empty list for storing aliens
# aliens = []
# #mke 30 green aliens
# for alien_number in range(30):
#     new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
#     aliens.append(new_alien)

# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
# for alien in aliens[:5]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = 15


# #show first 5 aliens
# for alien in aliens[:5]:
#     print(alien)
# print('...')
# #Show how many aliens have been created
# print(f"Total number of aliens: {len(aliens)}")


# pizza = {
#     'crust' : 'thick',
#     'toppings' : ['mushroom', 'etra cheese']
# }
# #Summarise the order
# print(f"You ordered  a {pizza['crust']} - crust pizza with the following toppings:")
# for topping in pizza['toppings']:
#     print("\t" + topping)

# favourite_languages = {
#     'jen' : ['python', 'ruby'],
#     'sarah' : ['c'],
#     'edward' : ['ruby', 'go'],
#     'phil' : ['python', 'haskell'],
# }
# for name, languages in favourite_languages.items():
#     if len(languages) == 1:
#         print(f"\n{name.title()}'s favourite languages is:")
#     elif len(languages) > 1:
#         print(f"\n{name.title()}'s favourite languages are:")
#     for language in languages:
#         print(f"\t{language.title()})")

# users = {
#     'aeistein' : {
#         'first' : 'albert',
#         'last' : 'aeistein',
#         'location' : 'princeton'
#     },
#     'mcurie' : {
#         'first' : 'marie',
#         'last' : 'curie',
#         'location' : 'paris'
#     }
# }
# for username, user_info in users.items():
#     print(f"\nUsername: {username}")
#     full_name = f"{user_info['first']} {user_info['last']}"

#     location = user_info['location']

#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")

# message = input("Tell me something, and I will repeat it back to you:")
# print(message)

# name = input("Please enter your name: ")
# print(f"\nHello {name}!")

# prompt = "If you tell us who you are we can personalize the message you see"
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello {name}!")

# age = input("How old are you? ")
# age = int(age)
# if age >= 18:
#     print("You are old enough to vote")
# else:
#     print("You are too young to vote")

# prompt = "\nTell me something, I will repeat it to you:"
# prompt += "\nEnter 'quit'to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)
    
# prompt = "\nTell me something, I will repeat it to you:"
# prompt += "\nEnter 'quit'to end the program. "
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# prompt = "\nTell me something, I will repeat it to you:"
# prompt += "\nEnter 'quit'to end the program. "
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}")

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# unconfirmed_users = ['alice', 'brian', 'candice']
# confirmed_users = []
# # Verify each user until there are no more unconfirmed users.
# # Move each verified user into the list of confirmed users.
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print(f"Verifying user {current_user.title()}")
#     confirmed_users.append(current_user)
# # Display all confirmed users.
# print("\nThe following users have been confirmed: ")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

# responses = {}
# #Set a flag to indiacte that polling is active
# polling_active = True
# while polling_active:
#     #prompt for a person's name and respone
#     name = input("\nWhat is your name?")
#     response = input("Which mountain would you like to climb one day?")
#     #Store response in the dictionary
#     responses[name] = response
#     #Find out if anyone else is going to take the poll
#     repeeat = input("Would you like to let another person respond? (yes/no)")
#     if repeeat == 'no':
#         polling_active = False
# #Polling is complete. Show tthe rresults.
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}")

# def greet_user(username):
#     """Display a simple greeting"""
#     print(f"Hello {username.title()}!")
# greet_user('jesse')

# def describe_pet(pet_name = 'noname', animal_type = 'dog'):
#     """Display information about pet"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}")
# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')
# describe_pet(pet_name = 'harry')

# def get_formatted_name(first_name, last_name):
#     """REturn a full name neatly"""
#     full_name = f"{first_name} {last_name}"
#     return full_name
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# def get_formatted_name(first_name, last_name, middle_name = None):
#     """Get a full name neatly formatted"""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name('jini', 'hendrix')
# print(musician)
# musician = get_formatted_name('jini', 'hendrix', 'lee')
# print(musician)
# print(get_formatted_name('jini', 'hendrix', 'lee'))

# def build_person(first_name, last_name, age = None):
#     """Return a dictionar of information about a person"""
#     person = {'first': first_name, 'last' : last_name}
#     if age:
#         person['age'] = age
#     return person
# musician = build_person('jini', 'hendrix' , age = 27)
# print(musician)

# def get_formatted_name(first_name, last_name):
#     """Return a full name neatly formatted"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello {formatted_name}")


# def greet_users(names):
#     """Print a simple greeting to each user in the list. """
#     for name in names:
#         msg = f"Hello , {name.title()}"
#         print(msg)
# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)

# def print_models(unprinted_designs, completed_models):
#     """Simulate printing each design, until none are left.
#     Move each design to completed_models after printing
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)
# def show_completed_models(completed_models):
#     """Show all the models that were printed"""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user"""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
# user_profile = build_profile('albert', 'eitein',
#     location = 'princeton',
#     field = 'physics'
#     )
# print(user_profile)

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f"\n Making a {size}-inch pizza with the following {len(toppings)} toppings:")

    for topping in toppings:
        print(f"- {topping}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')