motorcycles = ['honda', 'yamaha', 'suzuik']

print(motorcycles)

# motorcycles[0] = 'ducati'

# print(motorcycles)

motorcycles.append('ducati')

print(motorcycles)

motorcycles = []

print(motorcycles)

motorcycles.append('honda1')
motorcycles.append('yamaha2')
motorcycles.append('suzuki3')

print(motorcycles)

motorcycles.insert(0, 'ducati')

print(motorcycles)

del motorcycles[0]

print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles.append('suzuki3')
last_owned = motorcycles.pop()
print(f'The last motorcycle I owned was {last_owned.title()}.')

first_owned = motorcycles.pop(0)
print(f'The first motorcycle I owned was {first_owned.title()}.')

motorcycles = ['honda', 'yamaha', 'suzuik']
motorcycles.remove('yamaha')
print(motorcycles)
motorcycles.append('ducati')

print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')
