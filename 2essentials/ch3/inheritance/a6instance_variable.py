# Testing properties: instance variables.
class Super:
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12

if __name__ == "__main__":
    obj = Sub()

    print(obj.subVar)
    print(obj.supVar)


# When you try to access any object's entity, Python will try to (in this order):

# find it inside the object itself;
# find it in all classes involved in the object's inheritance line from bottom to top;
# If both of the above fail, an exception (AttributeError) is raised.