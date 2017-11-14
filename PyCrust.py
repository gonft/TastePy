# Functions

# Specify Default Parameter Values
def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken'))
# {'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'pudding'}
def buggy(arg, result=[]):
    result.append(arg)
    print(result)

buggy('a')  # ['a']
buggy('b')  # ['a', 'b']

# Gather Positional Arguments with *
def print_args(*args):
    print('Positional argument tuple:', args)

print_args()
# Positional argument tuple: ()

print_args(3, 2, 1, 'wait!', 'uh...')
# Positional argument tuple: (3, 2, 1, 'wait!', 'uh...')

def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Nedd this one too:', required2)
    print('All the rest:', args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustanche wa')
# All the rest: ('scarf', 'monocle', 'mustanche wa')

# Gather Positional Arguments with **

def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')
# Keyword arguments: {'wine': 'merlot', 'entree': 'mutton', 'dessert': 'macaroon'}

# Docstrings

def echo(anythings):
    'echo returns its input argument'
    return anythings

def print_if_ture(thing, check):
    '''
    Prints the first argment if a second argment is true
    :param thing: thing
    :param check: bool parameter
    :return: none
    '''
    if check:
        print(thing)

help(echo.__doc__)
# 'echo returns its input argument'.