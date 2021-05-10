print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

#input with argument
anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")

# NOTE
# result of the input() function is a string.

#Typecasting int() and float().
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

#String Concatenation
# Don't forget - if you want the + sign to be a concatenator, not an adder, you must ensure that both its arguments are strings.
print("abc" + "123")

# Replication
print("abc_"*3)


# to string
str(10)