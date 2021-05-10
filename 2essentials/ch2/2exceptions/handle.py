try:
    num1 = int(input("Enter 1st number "))
    num2 = int(input("Enter 2nd number "))
    num = num1/num2
except ZeroDivisionError as ex:
    print("ZeroDivisionError occured:", ex)
except ValueError as ex:
    print("Wrong value entered:", ex)
except (IndexError, KeyError) as ex:
    print("Index or KeyError occoured:",ex)
except Exception as ex:
    print("Something went wrong:", ex)
else:
    print("There was no exception and divsion is: ", num)
finally:
    print("Finally will execute always")