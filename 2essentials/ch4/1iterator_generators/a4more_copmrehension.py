the_list = [1 if x % 2 == 0 else 0 for x in range(10)] # square brackets makes a list
the_generator = (1 if x % 2 == 0 else 0 for x in range(10)) # parenthesis makes a generator

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()

print(len(the_list))
print(len(the_generator))


#######################################################
# can be created only when needed

for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print()

for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print()