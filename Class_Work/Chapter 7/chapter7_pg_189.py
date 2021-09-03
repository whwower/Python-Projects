#7.9
sandwich_orders = ['meat', 'pastrami', 'fish', 'egg','pastrami', 'veggie', 'pastrami']
finished_sandwiches = []
for sandwich_order in sandwich_orders:
	print("\nI made your {sandwich_order} sandwich")

print("\nFinished_sandwiches:")
while sandwich_orders:
	current_order = sandwich_orders.pop()
	finished_sandwiches.append(current_order)
for finished_sandwich in finished_sandwiches:
	print(f"\n{finished_sandwich}")

#7.9
sandwich_orders = ['meat', 'pastrami', 'fish', 'egg','pastrami', 'veggie', 'pastrami']
print("Deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
finished_sandwiches = []
for sandwich_order in sandwich_orders:
	print("\nI made your {sandwich_order} sandwich")

print("\nFinished_sandwiches:")
while sandwich_orders:
	current_order = sandwich_orders.pop()
	finished_sandwiches.append(current_order)
for finished_sandwich in finished_sandwiches:
	print(f"\n{finished_sandwich}")	

#7.10
dream_vacations = []
response = True
while response:
	dream_place = input("If you could visit one place in the world, where would you go?")
	dream_vacations.append(dream_place)
	another_place = input("Would you want to vist another place? (yes/no)")
	if another_place == 'no':
		response = False
for dream_vacation in dream_vacations:
	print(dream_vacation)