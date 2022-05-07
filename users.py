users = ['admin', 'max', 'cassie', 'jess', 'eli']
# users = []


if users:
	for user in users:
		if user == 'admin':
			print('hello administrator, who would you like to ban?')
		else:
			print(f'hello, {user} enjoy your session on the web!')				
else:
	print('We need to find some users!')



current_users = ['admin', 'max', 'cassie', 'jess', 'eli']
new_users = ['jackie', 'obi', 'siri', 'CaSsie']


for user in new_users:
	if user.lower() in current_users:
		print("sorry, pick a different name")
	else:
		print("welcome to the system!")

# print(new_users)

numbies = [1 , 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbies:
	if num == 1:
		print(f'{num}st')
	if num == 2:
		print(f'{num}nd')
	if num == 3:
		print(f'{num}rd')
	if num >= 3:
		print(f'{num}th')