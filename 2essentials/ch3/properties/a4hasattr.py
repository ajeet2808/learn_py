class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

if __name__ == "__main__":
    example_object = ExampleClass(1)
    print(example_object.a)

    if hasattr(example_object, 'b'):
        print(example_object.b)

# Don't forget that the hasattr() function can operate on classes, too. You can use it to find out if a class variable is available