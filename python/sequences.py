
# Sequences matching
point = (1, 1)
match point:
    case [int(x), int(y)]:
        print("Integer 2d point")
    case [float(x), float(y)]:
        print("Float 2d poind")
    case [int(x), int(y), int(z)]:
        print("Integer 3d point")
    case _:
        print("Not a point")

# Slicing
my_list = list(range(10))
my_tuple = tuple(my_list)

my_list[1:3] = [12, 13]
del my_list[1:3]

my_list += [10]  # this doesn't change id of my_list because it's mutable
my_tuple += (10, )  # this do

print(my_list, my_tuple, sep='\n')

s = bytearray(b'\x11\x22')
mem = memoryview(s)
print(mem[0])
mem[0] = 0x19
print(s.hex())

'''
# Reading data to 'data' without copying
f = open(FILENAME, 'rb')
data = bytearray(os.path.getsize(FILENAME))
f.readinto(data)
'''


# flat sequence vs container sequence test
def test_sequences():
    # arrays faster when need to pop or insert

    from timeit import timeit
    from array import array

    arr = array('b', (x & 15 for x in range(100000)))
    lst = [x & 15 for x in range(100000)]

    def func(arr):
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                arr[i] = arr[i] // 2
                arr.insert(i, 10)
            else:
                arr[i] = arr[i] * 2
                if i != 0:
                    arr.pop(i)

    t1 = timeit(stmt="func(arr)", globals=locals(), number=2)
    t2 = timeit(stmt="func(lst)", globals=locals(), number=2)
    print(f"Array time: {t1}. List time: {t2}")


test_sequences()

