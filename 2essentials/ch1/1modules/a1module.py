# A file containing Python definitions and statements, which can be later imported and used when necessary.
#a module is identified by its name - name of the file

import math #math is name of module supplied by python by default
import sys
# import math,sys # this is also correct but not readable.

# namespace - space where some names (of function, variable, class etc) exists and does not conflit to each other.


#accessing member of a module (modulename.membername)
print(math.pi)


# we are defining our own sin and pi which is in our namespace NOT conflicting with members of math module.
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))