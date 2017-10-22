one_marx = 'Groucho',
print(one_marx) #('Groucho',)

marx_tuple = ('Groucho', 'Chico', 'Harpo') #'Groucho', 'Chico', 'Harpo'
print(marx_tuple)   #('Groucho', 'Chico', 'Harpo')

# tuple unpacking
a, b, c = marx_tuple
print(a, b, c)  #Groucho Chico Harpo

password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
print(password, icecream)   #tuttifrutti swordfish

marx_list = ['Groucho', 'Chico', 'Harpo']
print(tuple(marx_list)) #('Groucho', 'Chico', 'Harpo')