import random
from functools import partial

class BingoCage:
    def __init__(self, items):
        # shallow copy in order to not change arguments
        self._items = list(items)
        
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
    
    def __call__(self):
        return self.pick()



def keyword_only(*, a, b):
    return int(a) + int(b)

def pos_only(a, b, /):
    return int(a) + int(b)

if __name__ == '__main__':
    a, b = input('Enter a and b: ').split()
    res1 = keyword_only(a=a, b=b)
    tenex = partial(pos_only, 10)
    res2 = tenex(b)
    print(res1, res2)





