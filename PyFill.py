empty_dict = {}
print(empty_dict)   #{}

bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses",
}
print(bierce)   #{'day': 'A period of twenty-four hours, mostly misspent', 'positive': "Mistaken at the top of one's voice", 'misfortune': 'The kind of fortune that never misses'}

lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(dict(lol))    #{'a': 'b', 'c': 'd', 'e': 'f'}

lol = [('a', 'b'), ('c', 'd'), ('e', 'f')]
print(dict(lol))    #{'a': 'b', 'c': 'd', 'e': 'f'}

lol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
print(dict(lol))    #{'a': 'b', 'c': 'd', 'e': 'f'}

lol = ['ab', 'cd', 'ef']
print(dict(lol))    #{'a': 'b', 'c': 'd', 'e': 'f'}

lol = ('ab', 'cd', 'ef')
print(dict(lol))    #{'a': 'b', 'c': 'd', 'e': 'f'}

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}
print(pythons)  #{'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael'}
pythons['Gilliam'] = 'Gerry'
print(pythons)  #{'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael', 'Gilliam': 'Gerry'}
pythons['Gilliam'] = 'Terry'
print(pythons)  #{'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael', 'Gilliam': 'Terry'}

some_python = {
    'Graham': 'Chapman',
    'John': 'Cleese',
    'Eric': 'Idle',
    'Terry': 'Gilliam',
    'Michael': 'Palin',
    'Terry': 'Jones',
}
print(some_python)  #{'Graham': 'Chapman', 'John': 'Cleese', 'Eric': 'Idle', 'Terry': 'Jones', 'Michael': 'Palin'}

others = { 'Marx': 'Groucho', 'Howard': 'Moe'}
pythons.update(others)
print(pythons)

first = {'a': 1, 'b': 2}
second = {'b': 'platypus'}
first.update(second)
print(first)    #{'a': 1, 'b': 'platypus'}

print(pythons)  #{'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael', 'Gilliam': 'Terry', 'Marx': 'Groucho', 'Howard': 'Moe'}
del pythons['Marx']
print(pythons)  #{'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael', 'Gilliam': 'Terry', 'Howard': 'Moe'}
del pythons['Howard']
print(pythons)  #{'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael', 'Gilliam': 'Terry'}

pythons.clear()
print(pythons)  #{}

pythons = {}
print(pythons)  #{}