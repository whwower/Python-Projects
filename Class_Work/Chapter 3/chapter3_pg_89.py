# 3.4
guests = ['John', 'Sam', 'Tim']
print(f"{guests[0]}, you are invited for dinner")
print(f"{guests[1]}, you are invited for dinner")
print(f"{guests[2]}, you are invited for dinner")

#3.5
guests = ['John', 'Sam', 'Tim']
print(f"{guests[0]} can't make it")
guests[0] = "Michael"
print(f"{guests[0]}, you are invited for dinner")
print(f"{guests[1]}, you are invited for dinner")
print(f"{guests[2]}, you are invited for dinner")

#3.6
guests = ['John', 'Sam', 'Tim']
#print(f"{guests[0]} can't make it")
guests[0] = "Michael"
print(f"{guests[0]}, I have found a bigger space")
print(f"{guests[1]}, I have found a bigger space")
print(f"{guests[2]}, I have found a bigger space")
guests.insert(0, 'Trevor')
guests.insert(2, 'Joe')
guests.append('Ben')
print(f"{guests[0]}, you are invited for dinner")
print(f"{guests[1]}, you are invited for dinner")
print(f"{guests[2]}, you are invited for dinner")
print(f"{guests[3]}, you are invited for dinner")
print(f"{guests[4]}, you are invited for dinner")
print(f"{guests[5]}, you are invited for dinner")

#3.7
guests = ['John', 'Sam', 'Tim']
#print(f"{guests[0]} can't make it")
guests[0] = "Michael"
guests.insert(0, 'Trevor')
guests.insert(2, 'Joe')
guests.append('Ben')
print("I can only invite two people for dinner")
removed = guests.pop()
print(f"{removed}, I'm sorry I can't invite you for dinner")
removed = guests.pop()
print(f"{removed}, I'm sorry I can't invite you for dinner")
removed = guests.pop()
print(f"{removed}, I'm sorry I can't invite you for dinner")
removed = guests.pop()
print(f"{removed}, I'm sorry I can't invite you for dinner")
print(f"{guests[0]}, you are still invited")
print(f"{guests[1]}, you are still invited")
del guests[0]
del guests[0]
print(guests)