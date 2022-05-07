#4-1 
pizzas = ['peppy' , 'saus''n''mushrom', 'white pie']

for pizza in pizzas:
	print(f'I fuckin love {pizza.title()}')

print(f'{pizzas[0]} can be a lil spicy')
print(f'but dont forget, {pizzas[1]} is real tasty')
print(f'its not my fave, but {pizzas[2]} is good with sauce on the side')

#4-3

for value in range(1, 21):
	print(value)

million = [value for value in range(1, 1_000_001)]

print(max(million))
print(min(million))
print(sum(million))

odds = [value for value in range(1, 21, 2)]

print(odds)

threes = []
for value in range(1, 11):
	threes.append(value*3)

for value in threes:
	print(value)

cubes = [value**3 for value in range(1, 11)]

for value in cubes:
	print(value)


