# The scope of a name (e.g., a variable name) is the part of a code where the name is properly recognizable.

def scope_test():
    x = 123


scope_test()
# print(x) error

#  A variable existing outside a function has a scope inside the functions' bodies.
def my_function():
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)


#global keyword for scopes
def my_function():
    global var
    var = 2 #possible to modify var only becuase of global var.
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)

