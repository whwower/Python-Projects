#PEP 8 COMPLIANCE
print("The code below was written in compliance with the PEP 8")
print("")

#4.10
pizzas = ['veggie', 'meat', 'cheese', 'BBQ', 'buffalo']
print(f"The first three items in the list are: ")
for pizza in pizzas[:3]:
	print(pizza)
print("")
print("Three items from the middle of the list are")
#get the middle position
middle = int(len(pizzas)/2)
for pizza in pizzas[middle-1:middle+2]:
	print(pizza)
print("")
print("The last three items of the list are")
for pizza in pizzas[-3:]:
	print(pizza)
print("")

#4.11
my_pizzas = ['veggie', 'meat', 'cheese', 'BBQ']
friend_pizzas = my_pizzas[:]
my_pizzas.append('hawaiian')
friend_pizzas.append('pepperoni')
print("My favourite pizzas are:")
for pizza in my_pizzas:
	print(pizza)
print("My friend's favourite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)
print("")

my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli']
friend_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream']
print("My favourite foods are:")
for my_food in my_foods:
	print(my_food)
print("My friend's favourite food are:")
for friend_food in friend_foods:
	print(friend_food)

