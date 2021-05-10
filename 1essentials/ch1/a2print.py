# Python's syntax is quite specific. Unlike most programming languages, Python requires that there cannot be more than one instruction in a line.

# A line can be empty (i.e., it may contain no instruction at all) but it must not contain two, three or more instructions. This is strictly prohibited.

# Note: Python makes one exception to this rule - it allows one instruction to spread across more than one line (which may be helpful when your code contains complex constructions).

print("The itsy bitsy spider climbed up the waterspout.")
print()
print("Down came the rain and washed the spider out.")

#multiple arugments
print("The itsy bitsy spider" , "climbed up" , "the waterspout.")

#Python strings are delimited with quotes (single or double)
print('The "itsy bitsy spider"',"climbed up", "this 'waterspout'")

#positional and keyword arguments
#any keyword arguments have to be put after the last positional argument (this is very important)
print("My name is", "Python.", end=" ")
print("My name is", "Python.", end="##")
print("My name is", "Python.", end="##\n")
print("My", "name","is", "Python.", sep="_")
print("My", "name","is", "Python.", end="##\n", sep="_")