# 3. Operators - Operators are symbols used to perform operations on values and variables.


# 3.1 Arithmetic Operators - Used to perform mathematical operations.

a = 10
b = 3

print(f"Addition = {a + b}")
print(f"Subtraction = {a - b}")
print(f"Multiplication = {a * b}")
print(f"Division = {a / b}")
print(f"Floor Division = {a // b}")
print(f"Modulus = {a % b}")
print(f"Exponentiation = {a ** b}")


# 3.2 Assignment Operators - Used to assign and update values in variables.

x = 10

x += 5
print(f"x += 5 = {x}")

x -= 3
print(f"x -= 3 = {x}")

x *= 2
print(f"x *= 2 = {x}")

x /= 4
print(f"x /= 4 = {x}")

x //= 2
print(f"x //= 2 = {x}")

x %= 3
print(f"x %= 3 = {x}")

x **= 2
print(f"x **= 2 = {x}")


# 3.3 Comparison Operators - Used to compare two values.
# The result is either True or False.

a = 10
b = 20

print(f"Equal = {a == b}")
print(f"Not Equal = {a != b}")
print(f"Greater Than = {a > b}")
print(f"Less Than = {a < b}")
print(f"Greater Than or Equal = {a >= b}")
print(f"Less Than or Equal = {a <= b}")


# 3.4 Logical Operators - Used to combine multiple conditions.

age = 21
has_id = True

print(f"AND = {age >= 18 and has_id}")
print(f"OR = {age >= 18 or has_id}")
print(f"NOT = {not has_id}")


# 3.5 Identity Operators - Used to check whether two variables refer to the same object.

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(f"a is b = {a is b}")
print(f"a is not c = {a is not c}")


# 3.6 Membership Operators - Used to check whether a value exists in a sequence.

fruits = ["Apple", "Mango", "Banana"]

print(f"Apple in fruits = {'Apple' in fruits}")
print(f"Orange in fruits = {'Orange' in fruits}")
print(f"Orange not in fruits = {'Orange' not in fruits}")


# 3.7 Bitwise Operators - Used to perform operations on binary numbers.

a = 10
b = 3

print(f"Bitwise AND = {a & b}")
print(f"Bitwise OR = {a | b}")
print(f"Bitwise XOR = {a ^ b}")
print(f"Bitwise NOT = {~a}")
print(f"Left Shift = {a << 1}")
print(f"Right Shift = {a >> 1}")


# 3.8 Conditional Expression (Ternary Operator)
# Used to write a simple if-else condition in one line

age = 21

status = "Adult" if age >= 18 else "Minor"


print(f"status = {status}")