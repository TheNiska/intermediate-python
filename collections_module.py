from collections import Counter, namedtuple

# Counter counts elements in iterable
my_str = "aaaabbbccd"
my_counter = Counter(my_str)
print(my_counter)

# Creates class with specified fields
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
