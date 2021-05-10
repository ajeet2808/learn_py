from a3stack import Stack
class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
    
    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)
    
    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

if __name__ == "__main__":
    stack_object = AddingStack()

    for i in range(5):
        stack_object.push(i)
    print("sum",stack_object.get_sum())

    for i in range(5):
        print(stack_object.pop())



# create counting stack
# create queue