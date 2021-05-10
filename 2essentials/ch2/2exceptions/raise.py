def bad_fun1(n):
    raise ZeroDivisionError


try:
    bad_fun1(0)
except ArithmeticError:
    print("What happened? An error?")

print("THE END.")
#############################################


def bad_fun2(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise # it will raise the same exception, useful for distributed exception handling


try:
    bad_fun2(0)
except ArithmeticError:
    print("I see!")

print("THE END.")