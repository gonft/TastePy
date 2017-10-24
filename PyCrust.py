disaster = True
if disaster:
    print("Woe!")
else:
    print("Whee!")
#Woe!

furry = True
small = True
if furry:
    if small:
        print("It's a cat.")
    else:
        print("It's a bear!")
else:
    if small:
        print("It's a skink!")
    else:
        print("It's a human. Or a hairless bear.")
#It's a cat.

color = 'puce'
if color == "red":
    print("It's a tomato")
elif color == "grren":
    print("It's a green pepper")
elif color == "bee purple":
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of the color", color)
#I've never heard of the color puce

x = 7
print(x == 5)                   #False
print(x == 7)                   #True
print(5 < x)                    #True
print(x < 10)                   #True
print(5 < x and x < 10)         #True
print((5 < x) and (x < 10))     #True
print(5 < x or x < 10)          #True
print(5 < x and x > 10)         #False
print(5 < x and not x > 10)     #True

print(5 < x < 10)               #True
print(5 < x < 10 < 999)         #True

some_list = []
if some_list:
    print("There's something in here")
else:
    print("Hey, it's empty!")
#Hey, it's empty!