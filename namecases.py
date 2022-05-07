name1 = "maxwell"

message	= f"Hello, {name1} you can program, you can do it! get a new job!"

print(message)

noCap = name1.lower()
print(noCap)
allCaps = name1.upper()
print(allCaps)
titleName = name1.title()
print(titleName)

quote = 'jules verne once said: "I am the light"'

famousGuy = 'jules verne'
message = f'{famousGuy.title()} once said: "I am the light"'
print(message)

cName = "   cassie woolhiser "

print(cName.lstrip())
print(cName.rstrip())
print(cName.strip())