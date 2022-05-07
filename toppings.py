requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
	print('Hold the anchovies!')

answer = 17

if answer != 42: 
	print('That is not the correct answer. Please try again!')

if answer <= 21 and answer >= 5:
	print('you got it!') 

banned_users = ['andrew' , 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(f"{user.title()} , you can post a response if you wish.")

game_active = True
can_edit = False

car = 'Subaru'

print("Is car == 'Subaru'? I predict True.")
print(car == 'Subaru')

