#tuples are immutable
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)

empty = ()
t1 = tuple((1, 2, "string"))
one_ele = (1,) # here comma (,) is rquired to make it tuple
print(type((1))) #int
print(type((1,))) #tuple

#accesing tuple - same as list but cannot modify as it's immutable.
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

print(len(my_tuple))
print(10 in my_tuple)
print(10 not in my_tuple)

for elem in my_tuple:
    print(elem)


#adding & multiplying tuples (similar to string)
t1 = (1,2)
t2 = (3,4)
ta = t1+t2
tm = t1*2

#adding elements in tuple (will create a new tuple not modify the exising one)
t = (1,)
t += (2,) # (1,2)
t += (3,) # (1,2,3)

#tuple to list
l = list(t) # [1,2,3]

#unpacking tuple
tup = 1, 2, 3
a, b, c = tup
print(a * b * c)

