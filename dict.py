'''Dictionary items are ordered, changeable, and does not allow duplicates.'''

d = {'a': 1, 'b': 2, 'c': 3}

d.popitem()
print(d)

alph = {}
ch = 'a'
num = ord('a')
while ch != '{':
    alph[ch] = num
    num += 1
    ch = chr(num)

print(alph)
