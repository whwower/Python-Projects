#8.9
messages = ['How are you?', 'This is my friend', 'Let us go to town', 'Randburg my place']
def show_messages(messages):
	for message in messages:
		print(message)
show_messages(messages)

#8.10
messages = ['How are you?', 'This is my friend', 'Let us go to town', 'Randburg my place']
sent_msgs = []

def sent_messages(messages, sent_msgs):
	while messages:
		current_message = messages.pop()
		print(f"Sending message: {current_message}")
		sent_msgs.append(current_message)

def print_messages(sent_msgs):
	"""Show all messages which were sent for printing"""
	print("\nHere is the initial list of messages")
	for message in messages:
		print(message)
	print("\nHere is a list of printed messages")
	for sent_msg in sorted(sent_msgs):
		print(sent_msg)

sent_messages(messages, sent_msgs)
print_messages(sent_msgs)

#8.11
messages = ['How are you?', 'This is my friend', 'Let us go to town', 'Randburg my place']
sent_msgs = []

def sent_messages(messages, sent_msgs):
	while messages:
		current_message = messages.pop()
		print(f"Sending message: {current_message}")
		sent_msgs.append(current_message)

def print_messages(sent_msgs):
	"""Show all messages which were sent for printing"""
	print("\nHere is the initial list of messages")
	for message in messages:
		print(message)
	print("\nHere is a list of printed messages")
	for sent_msg in sorted(sent_msgs):
		print(sent_msg)

sent_messages(messages[:], sent_msgs)
print_messages(sent_msgs)