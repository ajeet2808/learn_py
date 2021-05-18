# +, -, *, /, //, %, **
print(2+2) #4
print(2-2) #0
print(2*3) #6
print(3/2) #1.5
print(3//2) #1 (integer divison or floor division, rounding always goes to the lesser integer)
print(3//1.5) #2.0
print(3//2.0) #1.0
print(5%3) #2 
print(12 % 4.5) #3.0
print(2**3) #8 (power)


#operator priority and binding
print(2 + 3 * 5)
# The binding of the operator determines the order of computations performed by some operators with equal priority, put side by side in one expression.
print(9 % 6 % 2) # % has left-sided binding. = 1

#highest (1) to the lowest (4) priorities.
# Priority	Operator	
# 1	        +, - (unary)
# 2	        **	
# 3	        *, /, //, %	
# 4	        +, - (binary)
print(2 * 3 % 5)

#parentheses => subexpressions in parentheses are always calculated first.
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

#The exponentiation operator uses right-sided binding, e.g., 2 ** 2 ** 3 = 256.
print(2 ** 2 ** 3)