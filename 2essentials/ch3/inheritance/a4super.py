class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        super().__init__(name)

if __name__ == "__main__":
    obj = Sub("Andy")

    print(obj)


# The super() function creates a context in which you don't have to (moreover, you mustn't) pass the self argument to the method being invoked - this is why it's possible to activate the superclass constructor using only one argument.

# Note: you can use this mechanism not only to invoke the superclass constructor, but also to get access to any of the resources available inside the superclass.