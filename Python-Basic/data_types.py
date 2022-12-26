
# %%
# Variable examples

int = 1
float = 1.5
string = "string"
list = [1, 2, 3, 4, 5]
tuple = (1, 2, 3, 4, 5)
dictionary = {"key1":"bK3h%UJd&", "key2":"Jl1&oPa"}
set = {1, 1, 1, 2, 2, 2, 3, 3, 3}

# %%
# .format examples

name = "Matheus"
age = 19

print("My name is {} and my age is {}.".format(name, age))
# or
print("My name is {one} and my age is {two}, yes {two}.".format(one=name, two=age))

# %%
# Select characters at string

my_name = "Matheus Tecchio"
print(my_name[:6])
print(my_name[1:])
print(my_name[1:6])

# %%
# List examples

my_list = ["a", "b", "c", "d"]
print(my_list[1:3])

my_list.append("ADD")       # Add object on list
print(my_list)

my_list[1] = "REPLACE"      # Replace object on list
print(my_list)

#%%
# Tuple examples

my_tuple = (1, 2, 3, 4, 5)
my_tuple[1] = "REPLACE"     # ERROR, because tuples are immutable

# %%
# Dictionary examples

keys = {"key1":"bK3h%UJd&", "key2":"Jl1&oPa"}
print(keys["key1"])

keys["key1"] = "NEWbK3h%UJd&"
print(keys["key1"])