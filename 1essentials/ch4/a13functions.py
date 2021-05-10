# positional and keyword arguments
def add(a, b,c):
    print("sum = ", a + b + c)

add(1,3,4)
add(a=1,b=2,c=3)
add(1,c=2,b=3)

# forcing keyword arguments (* as first argument)
def add_again(*,a,b,c):
    print("sum = ",a+b+c)

# add_again(1,3,4) throws error
add_again(b=2,c=1,a=1)

# default value
def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

introduction("Bob")
introduction("Bob","Chi")


def strange_function(n):
    if(n % 2 == 0):
        return True

print(strange_function(19))
print(strange_function(18))