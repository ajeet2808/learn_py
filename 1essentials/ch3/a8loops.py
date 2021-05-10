# while conditional_expression:
    # instruction

# while True:
#     print("I'm stuck inside a loop.")

# for and range
#  The range() function generates a sequence of numbers. It accepts integers and returns range objects. The syntax of range() looks as follows: range(start, stop, step)

for i in range(10):
    print("The value of i is currently", i)

print("**************************************")

for i in range(2, 8):
    print("The value of i is currently", i)

print("*****************************************")

#prints nothing
for i in range(2, 1):
    print("The value of i is currently", i)

print("*****************************************")

for i in range(2, 8, 3):
    print("The value of i is currently", i)

# The break and continue statements
# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")


# loop with else
# loops may have the else branch too, like ifs.

# The loop's else branch is always executed once, regardless of whether the loop has entered its body or not.

i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

# Note: if the control variable doesn't exist before the loop starts, it won't exist when the execution reaches the else branch. if we remove i=5, it will throw error becuase i<5 never.
