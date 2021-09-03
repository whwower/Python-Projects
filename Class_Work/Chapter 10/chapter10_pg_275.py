#10.6
def checkValueError():
	while True:
		input_1 = input("Enter the first number")
		input_2 = input("Enter the second number")

		
		try:
			total = int(input_1) + int(input_2)
		except ValueError as ve:
			print("One of the values supplied is not a number")
		else:
			print(total)

checkValueError()