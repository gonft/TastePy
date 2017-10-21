poem = '''There was a Young Lady of Norway,
    Who casually sat in a doorway;
    When the door squeezed her flat,
    She exclaimed, "What of that?"
    This courageous Young Lady of Norway.'''

print(poem)

# There was a Young Lady of Norway,
#     Who casually sat in a doorway;
#     When the door squeezed her flat,
#     She exclaimed, "What of that?"
#     This courageous Young Lady of Norway.


start = 'Na' * 4 + '\n'
middle = 'Hey' * 3 + '\n'
end = 'Goodbye.'
print( start + start + middle + end)

# NaNaNaNa
# NaNaNaNa
# HeyHeyHey
# Goodbye.

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[:])       #abcdefghijklmnopqrstuvwxyz
print(letters[20:])     #uvwxyz
print(letters[10:])     #klmnopqrstuvwxyz
print(letters[12:15])   #mno
print(letters[-3:])     #xyz
print(letters[18:-3])   #stuvw
print(letters[-6:-2])   #uvwx
print(letters[::7])     #ahov
print(letters[4:20:3])  #ehknqt
print(letters[19::4])   #tx
print(letters[:21:5])   #afkpu
print(letters[::-1])    #zyxwvutsrqponmlkjihgfedcba
