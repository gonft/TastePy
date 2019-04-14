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

# Functions Are First-Class Citizens


def answer():
    print(42)


answer()


def run_something(func):
    func()


run_something(answer)

print(type(run_something))


def add_args(arg1, arg2):
    print(arg1 + arg2)


print(type(add_args))


def run_somthing_with_args(func, arg1, arg2):
    func(arg1, arg2)


run_somthing_with_args(add_args, 5, 9)


def sum_args(*args):
    return sum(args)


def run_with_positional_args(func, *args):
    return func(*args)


print(run_with_positional_args(sum_args, 1, 2, 3, 4))

# Inner Functions


def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)


print(outer(4, 7))

# Closures


def knight2(saying):
    def inner2():
        return "We are the knight who say: '%s'" % saying
    return inner2


a = knight2('Duck')
b = knight2('Hasenpfeffer')

print(type(a))
print(type(b))

print(a())
print(b())

# Anonymous Functions: the lambda() Function


def edit_story(words, func):
    for word in words:
        print(func(word))


stairs = ['thud', 'meow', 'thud', 'hiss']


def enliven(word):
    return word.capitalize() + '!'


# edit_story(stairs, enliven)
edit_story(stairs, lambda word: word.capitalize() + '!')

# Generators

print(sum(range(1, 101)))


def my_range(first=10, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


print(my_range)

ranger = my_range(1, 5)
print(ranger)

for x in ranger:
    print(x)

# Decorators


def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function


def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function


@square_it
@document_it
def add_ints(a, b):
    return a + b


print(add_ints(3, 5))

# Namespaces and Scope
animal = 'fruitbat'


def print_global():
    print('inside print_global:', animal)


print('at the top level:', animal)
print_global()


def change_local():
    animal = 'wombat'
    print('inside change_local:', animal, id(animal))


change_local()


def change_local_print_global():
    global animal
    animal = 'wombat'
    print('inside change_local_print_global:', animal, id(animal))


print(animal, id(animal))
change_local_print_global()
print(animal, id(animal))

animal = 'fruitbat'


def change_local():
    animal = 'wombat'
    print('locals:', locals())


print(animal)
change_local()
# print('global', globals())

# Handle Errors with try and except

short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print('Need a position between 0 and', len(
        short_list)-1, ' but got', position)

# Make Your Own Exceptions


class UppercaseException(Exception):
    pass


words = ['eeenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        try:
            raise UppercaseException(word)
        except UppercaseException as exc:
            print("UppercaseException:", exc)
