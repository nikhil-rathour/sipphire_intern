# 6. Data Structures & Algorithms
# Data Structures are used to organize and store data.
# Algorithms are step-by-step instructions used to solve a problem.


# 6.1 Strings - A string is a sequence of characters.

name = "Nikhil"
message = "Hello Python"

print(f"name = {name}")
print(f"message = {message}")


# Accessing String Characters

name = "Nikhil"

print(f"first character = {name[0]}")
print(f"second character = {name[1]}")
print(f"last character = {name[-1]}")


# String Length - len() is used to find the length of a string.

name = "Nikhil"

print(f"length = {len(name)}")


# String Slicing - Used to extract a part of a string.

name = "Nikhil"

print(f"first three characters = {name[0:3]}")
print(f"characters from index 2 = {name[2:]}")
print(f"characters before index 4 = {name[:4]}")


# Common String Methods

name = "nikhil rathour"

print(f"uppercase = {name.upper()}")
print(f"lowercase = {name.lower()}")
print(f"title = {name.title()}")
print(f"capitalized = {name.capitalize()}")
print(f"replace = {name.replace('nikhil', 'Nikhil')}")
print(f"count = {name.count('i')}")


# Checking String Content

name = "Nikhil"

print(f"starts with N = {name.startswith('N')}")
print(f"ends with l = {name.endswith('l')}")
print(f"contains h = {'h' in name}")