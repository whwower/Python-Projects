#4.3
for value in range(1, 21):
	print(value)
print("")

#4.4
million_numbers = list(range(1, 1_000_001))
for value in million_numbers:
	print(value)
print()

#4.5
a_million = list(range(1, 1_000_001))
print(max(a_million))
print(min(a_million))
print(sum(a_million))
print("")

#4.6
for value in range(1, 20, 2):
	print(value)
print("")

#4.7
for value in range(3, 31, 3):
	print(value)
print("")

#4.8
cubes = []
for value in range(1, 11):
	cubes.append(value ** 3)
print(cubes)
print("")

#4.9
cubes = [value ** 3 for value in range(1,11)]
print(cubes)