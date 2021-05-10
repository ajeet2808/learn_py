import module
import counted_module
prod = counted_module.prod_list([1,2,3])
print("prod", prod)
print("call count",counted_module.__counter)
print(counted_module.prod_list([5,6,7]))
print("call count ", counted_module.__counter)