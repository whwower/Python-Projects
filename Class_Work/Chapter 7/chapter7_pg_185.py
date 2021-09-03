#7.4
prompt = "\nEnter a pizza topping"
message = ""
while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(message)

#7.5
prompt = "\nEnter a pizza topping"
active = True
while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
		print(message)
print("\n")

prompt = "\nEnter a pizza topping"
while True:
	message = input(prompt)
	if message == 'quit':
		break
	else:
		print(message)
