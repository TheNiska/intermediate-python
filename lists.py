nums = [4, 2, 9, 10, 15, 40, 1, -3]
empty_list = list()

# list can hold different data types
different_types = ["one", 2, True]

# Lists methods --------------------------------------------------------------
length = len(nums)  # length of the list
nums.append(10)  	# appendiing to the end of the list

position = 1
element = 2
nums.insert(position, element)  # inserting element 2 in position 1
last = nums.pop()  # returns and removes the last item
third = nums.pop(2)  # returns and removes third item
nums.remove(15)  # removes the first matching element
different_types.clear()  # removes all elements from the list

num_of_ten = nums.count(10)  # the number of elements
idx_of_ten = nums.index(10)  # the index of the first element
nums.reverse()  # reverse the list
nums.sort()     # sorts the list in place
nums.sort(reverse=True)  # sort descending
new_nums = sorted(nums)  # creates new  sorted list

one_to_four = [1, 2, 3, 4]
cp = one_to_four.copy()  # copy
# ----------------------------------------------------------------------------

# lists comprehension
a = [1, 2, 3, 4, 5]
squares = [i * i for i in a]

print(squares)
print(nums)
print(num_of_ten)
