# Powerful slices
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)


# Its output is [1].
# The start and end parameters are optional when performing a slice:
# omitting both start and end makes a copy of the whole list
#  [:] is able to produce a brand new list.

# One of the most general forms of the slice looks as follows:

# my_list[start:end]

# A slice of this form makes a new (target) list, taking elements from the source list - the elements of the indices from start to end - 1.


# Slices - negative indices
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)



# del instruction is able to delete more than just a list's element at once - it can delete slices too
# Note: in this case, the slice doesn't produce any new list!

my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list) #??


# my_list = [10, 8, 6, 4, 2]
# del my_list # it will delete the list variable itself
# print(my_list) #?? error



# The in and not in operators
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)


#conditional expression - a way of selecting one of two different values based on the result of a Boolean expression.
#expression_one if condition else expression_two
#it is not a conditional instruction. Moreover, it's not an instruction at all. It's an operator.
the_list = []
for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)
print(the_list)

compre_list = [1 if x%2== 0 else 0 for x in range(10)]
print(compre_list)