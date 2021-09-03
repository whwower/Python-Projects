#4.1
pizzas = ['veggie', 'meat', 'cheese', 'BBQ']
for pizza in pizzas:
	print(f"I like {pizza} pizzas")
print(f"I like {pizzas[0]} pizza the most")
print(f"followed by the {pizzas[1]} pizza")
print(f"followed by the {pizzas[2]} pizza")
print(f"followed by the {pizzas[3]} pizza")
print("I really love pizza!")
print()

#4.2
animals = ['cow', 'sheep', 'goat']
for animal in animals:
	print(animal.title())
print(f"{animals[0].title()} has the best meat")
print(f"{animals[1].title()} has faty meat")
print(f"{animals[2].title()} likes bushes")
print("All the animals feed on vegitation")