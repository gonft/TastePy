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