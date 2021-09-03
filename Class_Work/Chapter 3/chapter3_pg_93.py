#3.8
locations = ['Joburg', 'Pretoria', 'Grahamstown', 'East London', 'Port Elizabeth']
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse = True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse = True)
print(locations)

#3.9
guests = ['John', 'Sam', 'Tim']
print(len(guests))

#3.10
students = ['John', 'Joe', 'Tim', 'Ray']
students.append('Blessing')
print(students)
students.insert(0, 'Brain')
print(students)
deregistered = students.pop()
print(students)
students.remove('John')
print(students)
students.sort(reverse = True)
print(students)
print(sorted(students))
students.reverse()
print(students)