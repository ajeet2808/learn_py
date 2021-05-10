""" counted_module.py - an example of a Python module. It will count function calls """
__counter = 0

def sum_list(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum

def prod_list(the_list):
    global __counter    
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod

if __name__ == "__main__":
    print("This file is run direclty, so this section is executed where we have tests. If this module is import then this will not execute at all. interesting??")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)