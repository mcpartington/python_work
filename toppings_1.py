available_toppings = ['mushrooms', 'extra cheese', 'olives', 'salami', 'peppers']
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

if 'mushrooms'in requested_toppings:
	print('Adding mushrooms')
if 'pepperoni' in requested_toppings:
	print('Adding peppys')
if 'extra cheese' in requested_toppings:
	print('Added extra cheese')
print("\nFinished making your pizza!")

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f'Adding {requested_topping}.')
	else:
		print(f"sorry bud, {requested_topping}")

	# 	else:
	# print('You sure you want a plain za dude?')
print('pizza finished!')