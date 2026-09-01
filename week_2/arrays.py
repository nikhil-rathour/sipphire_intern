
# 6.2 Arrays - An array is a collection of elements stored together.
# In Python, lists are commonly used as arrays.

numbers = [10, 20, 30, 40, 50]

print(f"numbers = {numbers}")
print(f"first element = {numbers[0]}")
print(f"last element = {numbers[-1]}")


# Adding Elements to an Array

numbers = [10, 20, 30]

numbers.append(40)

print(f"numbers = {numbers}")


# Removing Elements from an Array

numbers = [10, 20, 30, 40]

numbers.remove(30)

print(f"numbers = {numbers}")


# Updating Array Elements

numbers = [10, 20, 30, 40]

numbers[1] = 25

print(f"numbers = {numbers}")


# Traversing an Array

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(f"number = {number}")


# Finding the Length of an Array

numbers = [10, 20, 30, 40, 50]

print(f"length = {len(numbers)}")


# Finding the Maximum and Minimum Value

numbers = [10, 50, 20, 80, 30]

print(f"maximum = {max(numbers)}")
print(f"minimum = {min(numbers)}")


# 6.3 Single Dimensional Array
# A single dimensional array stores elements in a single row or sequence.

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(f"number = {number}")


# 6.4 Multi Dimensional Array
# A multi dimensional array stores data in rows and columns.
# In Python, nested lists are commonly used.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"matrix = {matrix}")


# Accessing Multi Dimensional Array Elements

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"first row = {matrix[0]}")
print(f"first element = {matrix[0][0]}")
print(f"middle element = {matrix[1][1]}")
print(f"last element = {matrix[2][2]}")


# Traversing a Multi Dimensional Array

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for value in row:
        print(f"value = {value}")