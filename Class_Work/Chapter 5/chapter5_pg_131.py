#5.1
favouriteColor = 'white'
print("Is favouriteColor == 'white'? I predict True")
print(favouriteColor == 'white')
print("\nIs favouriteColor == 'red'? I predict False")
print(favouriteColor == 'red')

sport = "soccer"
print("\nIs sport == 'soccer'? I predict True")
print(sport == 'soccer')
print("\nIs sport == 'rugby' I predict False")
print(sport != 'soccer')

friend = 'John'
print("\nIs friend == 'John' I predict True")
print(friend == 'John')
print("\nIs friend == 'Tim' I predict False")
print(friend != 'John')

meal = "pap"
print("\nIs meal == 'pap' I predict True")
print(meal == 'pap')
print("\nIs meal == 'burger' I predict False")
print(meal == 'burger')

age = 25
print("\nAge == 25, I predict True")
print(age == 25)
print("\nIs age > 25, I predict False")
print(age > 25)

#5.2
name = "emmanuel"
print("\nIs name title == 'Emmanuel', I predict True")
print(name.title() == 'Emmanuel')
print("\nIs name != 'Emmanuel', I predict False")
print(name == 'Emmanuel')

name = "emmanuel"
print("\nIs name upper == 'EMMANUEL', I predict True")
print(name.upper() == 'EMMANUEL')
print("\nIs name.upper() == 'Emmanuel', I predict False")
print(name == 'Emmanuel')

age = 20
height = 2
print("\nIs age == 20 and height == 2, I predict True")
print(age == 20 and height == 2)
print("\nIs age > 20 and height == 2, I predict True")
print(height > 20 and height == 2)

my_friends = ['Tobias', 'Last', 'Ian', 'Trust']
old_friend = 'Peter'
new_friend = 'Enock'
if old_friend in my_friends:
	print(f"\n{old_friend}, we have been friend for long")
else:
	print(f"\n{old_friend}, I miss you old friend friend")
if new_friend not in my_friends:
	my_friends.append(new_friend)
	print("\nUpdated friends")
for my_friend in my_friends:
	print(my_friend)
