class Fib:
    def __init__(self, n):
        self.__n = n
        self.__count = 0
        self.__num1 = 1
        self.__num2 = 1
    def __iter__(self):
        return self
    
    def __next__(self):
        self.__count += 1
        if self.__count > self.__n:
            raise StopIteration
        if self.__count in [1,2]:
            return 1
        ret = self.__num1 + self.__num2
        self.__num1, self.__num2 = self.__num2, ret
        return ret

if __name__ == "__main__":
    fib = Fib(10)
    fib10 = [x for x in fib]
    fib10again = [x for x in fib]
    print(fib10, fib10again)

    fib = Fib(10)
    for i in fib:
        print(i,end=",")