cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
# cars.sort()
# cars.sort(reverse=True)
# print(cars)

print("Here is the sorted list")
print(sorted(cars))

print(cars)

cars.reverse()

print(cars)

length = len(cars)
print(length)

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

car = 'Audi'
car == 'Audi'

print(car.lower() == 'audi')
