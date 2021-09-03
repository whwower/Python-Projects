#9.7
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

class Admin(Users):
	def __init__(self, first_name, last_name, age, race):
		super().__init__(first_name, last_name, age, race)
		self.priviledges = priviledges

	def show_priviledges(self, priviledges):
		print("\nHere are the adimistrator's priviledges")
		for priviledge in priviledges:
			print(priviledge)

priviledges = ["can add post", "can delete post", "can ban user"]
admin_1 = Admin('Elvis', 'Morelife', 25, 'African')
admin_1.show_priviledges(priviledges)

#9.9
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

class Admin(Users):
	def __init__(self, first_name, last_name, age, race):
		super().__init__(first_name, last_name, age, race)
		self.priviledges = Priviledges()

class Priviledges:
	def show_priviledges(self, priviledges):
		print("\nHere are the adimistrator's priviledges using the Priviledges class")
		for priviledge in priviledges:
			print(priviledge)

priviledges = ["can add post", "can delete post", "can ban user"]
admin_2 = Admin('Elvis', 'Morelife', 25, 'African')
admin_2.priviledges.show_priviledges(priviledges)