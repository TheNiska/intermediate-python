import weakref

s1 = {1, 2, 3}
s2 = s1

def bye():
    print('object has benn destroyed')

ender = weakref.finalize(s1, bye)

del s1
s2 = 'spam'

