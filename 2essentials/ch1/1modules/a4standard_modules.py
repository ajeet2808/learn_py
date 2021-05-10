# dir - Lists all the names provided through a particular module.
import math
import random
import platform
def print_module(module):
    print(f"{module.__name__}\n {dir(module)}")

print_module(math)
print_module(random)
print_module(platform)

print("***********************platform**********************************")
print(platform.platform())
print(platform.platform(0,1)) #platform(aliased = False, terse = False)
print(platform.machine()) #generic name of the processor
print(platform.processor()) #realname
print(platform.system()) #generic name of os
print(platform.version()) #os version
print(platform.python_implementation()) #returns a string denoting the Python implementation 

# returns a three-element tuple filled with:
# the major part of Python's version;
# the minor part;
# the patch level number.
print(platform.python_version_tuple())

#module index : https://docs.python.org/3/py-modindex.html