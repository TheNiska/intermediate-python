import sys
import timeit
'''Datatype like list but immutable.'''
'''A tuple is a collection which is ordered and unchangeable.'''

'''
Tuples has only two built-in methods:
    1) count()
    2) index()
'''

tup = ("Denis", 28, False)
some_list = [255, 0, 0]

red = tuple(some_list)  # creates tuples from iterable
print(f"Red is {red} and type is {type(red)}")

nums = (1, 4, 9, 16)
a, b, c, d = nums  # a way to unpack
print("Unpacking to variables: ", a, b, c, d)

a, *others = nums  # unpacking with asterix
print(others, ' || type =', type(others))  # type list

nums_tup = nums
nums_lst = [1, 4, 9, 16]
print("Size of tuple: ", sys.getsizeof(nums_tup), "bytes")
print("Size of list: ", sys.getsizeof(nums_lst), "bytes")


lst_time = timeit.timeit(stmt="[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]",
                         number=1000000)
tup_time = timeit.timeit(stmt="(0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100)",
                         number=1000000)
print("List time: ", lst_time)
print("Tuple time: ", tup_time)
