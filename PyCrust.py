rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current += 1
# Flopsy
# Mopsy
# Cottontail
# Peter

for rabbit in rabbits:
    print(rabbit)
# Flopsy
# Mopsy
# Cottontail
# Peter

word = 'cat'
for letter in word:
    print(letter)
# c
# a
# t

# Dictionary
accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}
for card in accusation:
    print(card)
# room
# weapon
# person

for value in accusation.values():
    print(value)
# ballroom
# lead pipe
# Col. Mustard

for item in accusation.items():
    print(item)
# ('room', 'ballroom')
# ('weapon', 'lead pipe')
# ('person', 'Col. Mustard')

for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)
# Card room has the contents ballroom
# Card weapon has the contents lead pipe
# Card person has the contents Col. Mustard

cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else:
    print('This is not much of a cheese shop, is it?')
#This is not much of a cheese shop, is it?

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)
# Monday : drink coffee - eat banana - enjoy tiramisu
# Tuesday : drink tea - eat orange - enjoy ice cream
# Wednesday : drink beer - eat peach - enjoy pie

#Creating a dictionary object using zip
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
print(list( zip(english, french) ))
#[('Monday', 'Lundi'), ('Tuesday', 'Mardi'), ('Wednesday', 'Mercredi')]

print(dict( zip(english, french) ))
#{'Monday': 'Lundi', 'Tuesday': 'Mardi', 'Wednesday': 'Mercredi'}

for x in range(0, 3):
    print(x)
# 0
# 1
# 2
print( list(range(0, 3)) )
#[0, 1, 2]
print( list(range(0, 11, 2)) )
#[0, 2, 4, 6, 8, 10]

number_list = []
number_list = list(range(0, 6))
print(number_list)
# [0, 1, 2, 3, 4, 5]

number_list = [number for number in range(1, 6)]
print(number_list)
#[1, 2, 3, 4, 5]

number_list = [number - 1 for number in range(1, 6)]
print(number_list)
#[0, 1, 2, 3, 4]

a_list = [number for number in range(1, 6) if number % 2 == 1]
print(a_list)
#[1, 3, 5]

rows = range(1, 4)
cols = range(1, 3)
for r in rows:
    for c in cols:
        print(r, c)
# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2

cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)
# (1, 1)
# (1, 2)
# (2, 1)
# (2, 2)
# (3, 1)
# (3, 2)

for row, col in cells:
    print(row, col)
# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)
#{'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}

letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)
#{'l': 1, 'r': 1, 't': 2, 's': 1, 'e': 2}

a_set = {number for number in range(1,6) if number % 3 == 1}
print(a_set)
#{1, 4}

number_thing = (number for number in range(1, 6))
print(type(number_thing))
#<class 'generator'>

for number in number_thing:
    print(number)
# 1
# 2
# 3
# 4
# 5

number_list = list(number_thing)
print(number_list)
#[]