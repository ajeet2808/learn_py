# A literal is data whose values are determined by the literal itself.
# 123 - literal
# c - not a literal

#string
print("1", type("1")) 
print("I like \"Monty Python\"")
print('I like "Monty Python"')
print("I'm Monty Python.")

#integers
print(1,type(1))

#floats
print(1.1,type(1.1))
print(.4) #0.4
print(4.) #4.0
print(4.0) #40

#scientific notation
print(3E8) #300000000.0
print(3E-8) #0.00000003

#readablity
print(100_000)
print(-100_000)

#octal (preceded by zero-o)
print(0o123) #83 in decimal

#hexadecimal
print(0x123) # 291 in decimal

#booleans
print(True)
print(False)
print(True > False)
print(True < False)

#None (the absence of a value)- same as null in other languages
print(None)