empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'Jonh', 'Terry', 'Terry', 'Michael']

another_empty_list = list()

print(weekdays)         #['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(big_birds)        #['emu', 'ostrich', 'cassowary']
print(first_names)      #['Graham', 'Jonh', 'Terry', 'Terry', 'Michael']
print(list('cat'))      #['c', 'a', 't']

a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))    #['ready', 'fire', 'aim']

birthday = '1/6/1952'
print(birthday.split('/'))  #['1', '6', '1952']

splitme = 'a/b//c/d///e'
print(splitme.split('/'))   #['a', 'b', '', 'c', 'd', '', '', 'e']
splitme = 'a/b//c/d///e'
print(splitme.split('//'))  #['a/b', 'c/d', '/e']

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0])    #Groucho
print(marxes[1])    #Chico
print(marxes[2])    #Harpo

print(marxes[-1])    #Harpo
print(marxes[-2])    #Chico
print(marxes[-3])    #Groucho

marxes.append('Zeppo')
print(marxes)   #['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.extend(others) #or marex += other
print(marxes)   #['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo', 'Karl']

del marxes[-2]  #or marxes.remove('Gummo')
print(marxes)   #['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.insert(-1,'Gummo')
print(marxes)   #['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo', 'Karl']
marxes.pop()    #equal marxes.pop(-1)
print(marxes)   #['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo']
print(marxes.index('Harpo'))    #2
print(', '.join(marxes))    #Groucho, Chico, Harpo, Zeppo, Gummo

a = [1, 2, 3]
b = a.copy(a)
c = list(a)
d = a[:]