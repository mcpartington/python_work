#3-4
dinnerGuests = ['jules verne', 'cassie', 'orville peck']

print(f"you're the coolest, would you like to come to dinner {dinnerGuests[2].title()} ?")
print(f"I'd love to show you things that have been invented {dinnerGuests[0].upper()}, woudld you come to dinner?")
print(f'hi {dinnerGuests[1]} ! would you come to dinner plz?')
print(f'{dinnerGuests[0]} cannot make it!')

dinnerGuests[0] = 'jess gring'

print(f'{dinnerGuests[0].title()} you are now invited!')

print(f'{dinnerGuests } I''ve found a bigger table! more guests!')

dinnerGuests.insert(0 , 'amelie')
dinnerGuests.insert(1, 'zero')
dinnerGuests.append('tom hanks')

print(f'{dinnerGuests} glad you all can make it!')

print(f'so sorry, table is late, only 2 can come!')

print(f'{dinnerGuests.pop()} so sorry, next time!')
print(f'{dinnerGuests.pop()} so sorry, next time!2')
print(f'{dinnerGuests.pop()} so sorry, next time!3')
print(f'{dinnerGuests.pop()} so sorry, next time!4')

print(f'{dinnerGuests}, feel free to come any time after 6!')

del(dinnerGuests[-1])
del(dinnerGuests[-1])

#3-9
print(f'{len(dinnerGuests)}')

