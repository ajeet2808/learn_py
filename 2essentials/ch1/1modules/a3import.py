pi = 3.14
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(sin(pi / 2)) # pi and sin defined by us.

from math import sin, pi # imported from math module, this will supersede pi, sin defined by us

print(sin(pi / 2))

##########################################
from datetime import * # import everthing from module

##########################################
import math as m # import module as alias, now m will be used instead of math, original module name is not accessible after aliasing
print(m.sin(m.pi))


###########################################
from math import pi as PI, sin as sine
print(sine(PI))