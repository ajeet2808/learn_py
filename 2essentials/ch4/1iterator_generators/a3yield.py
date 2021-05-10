def fun(n):
    for i in range(n):
        yield i

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

def fibonacci(n):
    num1 = num2 = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            ret = num1 + num2
            num1, num2 = num2, ret
            yield ret

if __name__ == "__main__":
    for i in fun(10):
        print(i,end=",")
    print()

    # generators can be used in 'in' context
    for n in powers_of_2(11):
        print(n,end=",")
    print()

    #generators can be used in list comprehensions as well
    powers_of_2_list = [x for x in powers_of_2(11)]
    print("comprehension",powers_of_2_list)

    # generator to list
    gen_to_list = list(powers_of_2(11))
    print("gen_to_list", gen_to_list)

    fib10 = [x for x in fibonacci(10)]
    print('fib10', fib10)
    print('type of fibonacci(n) =>', type(fibonacci(10)))