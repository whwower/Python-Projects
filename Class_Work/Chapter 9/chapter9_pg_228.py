#9.2
class Restaurant:
	"""Model a restaurant object"""

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"The restaurant {self.restaurant_name} offers {self.cuisine_type}")

	def open_restaurant(self):
		print(f"{self.restaurant_name} is currently open")

restaurant = Restaurant('Nandos', 'traditional')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("\n")

#9.3
class Users:
	def __init__(self, first_name, last_name, age, race):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age 
		self.race = race

	def describe_user(self):
		print(f"{self.first_name} {self.last_name} is {self.age} year old person of race {self.race}")

	def greet_user(self):
		print(f"Good morning {self.first_name} {self.last_name}")

user_1 = Users('Mary', 'Marios', 23, 'African')
user_1.describe_user()
user_1.greet_user()
user_2 = Users('Denis', 'Simbs', 25, 'African')
user_2.describe_user()
user_2.greet_user()