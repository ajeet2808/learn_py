class Classy:
    pass

class Plassy(Classy):
    pass

if __name__ == "__main__":
    print(Classy.__name__) # __name__ is available only on class not on instances
    obj = Classy()
    print(type(obj).__name__) # type will give class of object
    print(type(obj)()) #creating object without knowing the class 
    print(Plassy.__bases__)
    print(Classy.__bases__)