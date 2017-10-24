empty_set = set()
print(empty_set)

even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)
odd_numbers = {1, 3, 5, 7, 9}
print(odd_numbers)

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)
        # martini
        # black russian
        # white russian
        # screwdriver
print()
for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)
        # black russian
        # screwdriver
print()
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)
        # martini
        # manhattan
        # screwdriver
print()
for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)
        # black russian
        # screwdriver
print()
bruss = drinks['black russian']
wruss = drinks['white russian']

a = {1, 2}
b = {2, 3}

# 교집합 intersection
print(a & b)                #{2}
print(a.intersection(b))    #{2}

print(bruss & wruss)        #{'vodka', 'kahlua'}

# 합집합 union
print(a | b)                #{1, 2, 3}
print(a.union(b))           #{1, 2, 3}

print(bruss | wruss)        #{'kahlua', 'vodka', 'cream'}

# 차집합 difference
print(a - b)                #{1}
print(a.difference(b))      #{1}

print(bruss - wruss)        #set()
print(wruss - bruss)        #{'cream'}

# 대칭 차집합 exclusive
print(a ^ b)                        #{1, 3}
print(a.symmetric_difference(b))    #{1, 3}

print(bruss ^ wruss)                #{'cream'}

# 부분 집합 subset
print(a <= b)           #False
print(a.issubset(b))    #False

print(bruss <= wruss)   #True

# 진부분 집합 proper subset
print(a < b)            #False
print(a < a)            #False
print(a <= a)           #True

print(bruss < wruss)    #True

