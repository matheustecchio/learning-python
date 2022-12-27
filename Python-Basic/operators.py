#%%
# Arithmetic Operators

x = 20
y = 10

print( x +  y)   # Addition
print( x -  y)   # Subtraction
print( x *  y)   # Multiplication
print( x /  y)   # Division
print( x %  y)   # Modulus
print( x ** y)   # Exponentiation
print( x // y)   # Floor division

#%%
# Comparison Operators

x = 20
y = 10

print(x == y)   # Equal
print(x != y)   # Not equal
print(x < y)    # Greater than
print(x > y)    # Less than
print(x <= y)   # Greater than or equal to
print(x >= y)   # Less than or equal to

#%%
# Logical Operators

x = 20
y = 10

print(x > y and (y * 2) != x)  # And
print(x > y or (y * 2) != x)   # Or
print(not(x < y))              # Not

#%%
# Identity Operators

x = 10
y = 10.0

print(x is y)       # Is
print(x is not y)   # Is not

#%%
# Membership Operators

list = ["Laptop", "Mouse", "Keyboard"]

print("Laptop" in list)     # In
print("Mouse" not in list)  # Not in

#%% 
# Boolean examples

print(1 < 2)
print(1 < 1)
print(1 == 1)
print(1 >= 1)
