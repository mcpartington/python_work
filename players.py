players = ['max', 'cassie', 'jess', 'esra', 'mike']

print(players[0:3])

print(players[:3])
print(players[3:])
print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
	print(player)