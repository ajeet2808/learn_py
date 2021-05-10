# list starts with an open square bracket and ends with a closed square bracket
number = [] #empty list
numbers = [10, 5, 7, 2, 1]

# The elements inside a list may have different types. Some of them may be integers, others floats, and yet others may be lists.

mixed = ["Some string", 10, 10.5, True, [1,"a"]]

# Indexing lists
# starts with index zero
numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("New list content: ", numbers)  # Current list content.

# Accessing list content
print(numbers[0])
print(numbers)

# The len() function
print(len(numbers))


# Removing elements from a list
# Any of the list's elements may be removed at any time - this is done with an instruction named del (delete). Note: it's an instruction, not a function.

del numbers[1]
print(len(numbers))
print(numbers)

# Negative indices are legal
# An element with an index equal to -1 is the last one in the list.
print(numbers[-1])


# Adding elements to a list: append() and insert()
# list.append(value)
# list.insert(location, value)

numbers.insert(1, 333)
print(numbers) #[111, 333, 7, 2, 1]

#for with list
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)