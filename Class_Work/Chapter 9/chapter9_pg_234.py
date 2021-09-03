class Users:
	def __init__(self, first_name, last_name, age, race):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age 
		self.race = race
		self.login_attempts = 0

	def describe_user(self):
		print(f"{self.first_name} {self.last_name} is {self.age} year old person of race {self.race} has {self.login_attempts} attempts")

	def greet_user(self):
		print(f"Good morning {self.first_name} {self.last_name}")

	def increment_login_attempts(self, logs):
		if logs > 0:
			self.login_attempts += logs 
		else:
			print("Log ins can't be negative")

	def reset_login_attempts(self):
		self.login_attempts = 0

user_1 = Users('Mary', 'Marios', 23, 'African')
user_1.describe_user()
user_1.greet_user()
user_1.increment_login_attempts(2)
user_1.describe_user()
user_1.increment_login_attempts(2)
user_1.describe_user()
user_1.reset_login_attempts()
user_1.describe_user()