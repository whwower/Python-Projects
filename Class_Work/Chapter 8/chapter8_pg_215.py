#8.12
# def added_sandwich_items(*added_items):
# 	print("\nHere is the list of items to be added")
# 	for added_item in added_items:
# 		print(added_item)
# added_sandwich_items('cheese', 'meat', 'sausage')

#8.13
def build_profile(name, surname, **user_info):
	user_info['first_name'] = name
	user_info['last_name'] = surname
	return user_info

print("\nHere is the user profile: ")
user_profile = build_profile('Leona', 'Green', 
	location = 'Randburg',
	age = 25
	)
print(user_profile)