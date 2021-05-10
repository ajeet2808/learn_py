# Testing properties: class variables.
class Super:
    supVar = 1


class Sub(Super):
    subVar = 2


if __name__ == "__main__"
    obj = Sub()

    print(obj.subVar)
    print(obj.supVar)
