#an anonymous function
# lambda parameters: expression

two = lambda: 2 # parameterless
sqr = lambda x: x * x # one parameter
pwr = lambda x, y: x ** y # two parameters

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))


# map(function, list)
list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()

#filter(function, list)
from random import randint
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)