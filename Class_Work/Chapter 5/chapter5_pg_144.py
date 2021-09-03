#5.8
usernames = ['admin', 'secretary', 'receiptionist', 'accounts', 'cleaner']
for username in usernames:
	if username == 'admin':
		print(f"\nHello {username}, would you like to see status report?")
	else:
		print(f"\nHello {username}, thank you for logging in again")

#5.9
usernames = []
if usernames:
	for username in usernames:
		if username == 'admin':
			print(f"\nHello {username}, would you like to see status report?")
		else:
		    print(f"\nHello {username}, thank you for logging in again")
else:
	print("WE need to find some users")

#5.10
current_users = ['john', 'sam', 'peter', 'ray', 'tim', 'sandra']
new_users = ['Rob', 'Joe', 'John', 'RAY', 'Marvelous']
for new_user in new_users:
	new_user = new_user.lower()
	if new_user in current_users:
		print("\nYou need to enter a new username")
	else:
		print("\nThe username is available")

#5.11
my_list = list(range(1, 10))
for number in my_list:
	if number == 1:
		print('\n1st')
	elif number == 2:
		print('2nd')
	elif number == 3:
		print('3rd')
	elif number == 4:
		print('4th')
	elif number == 5:
		print('5th')
	elif number == 6:
		print('6th')
	elif number == 7:
		print('7th')
	elif number == 8:
		print('8th')
	else:
		print('9th')