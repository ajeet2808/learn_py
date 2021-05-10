class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val

if __name__ == "__main__":
    print(ExampleClass.__dict__)
    example_object = ExampleClass(2)

    print(ExampleClass.__dict__)
    print(example_object.__dict__) # no instance variables
