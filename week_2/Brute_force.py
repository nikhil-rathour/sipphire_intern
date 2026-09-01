# 6.6 Brute Force Algorithm
# Brute Force is a simple problem-solving approach that checks
# all possible solutions until the correct solution is found.


# Brute Force Example - Finding an Element in an Array

numbers = [10, 20, 30, 40, 50]

target = 30

for number in numbers:

    if number == target:
        print(f"target found = {number}")


# Brute Force Example - Finding a Number Using Index

numbers = [10, 20, 30, 40, 50]

target = 40

for i in range(len(numbers)):

    if numbers[i] == target:
        print(f"target found at index = {i}")


# Brute Force Example - Finding Duplicate Elements

numbers = [10, 20, 30, 20, 40, 10]

for i in range(len(numbers)):

    for j in range(i + 1, len(numbers)):

        if numbers[i] == numbers[j]:
            print(f"duplicate = {numbers[i]}")


# Brute Force Example - Finding Two Numbers Whose Sum Matches a Target

numbers = [2, 7, 11, 15]

target = 9

for i in range(len(numbers)):

    for j in range(i + 1, len(numbers)):

        if numbers[i] + numbers[j] == target:
            print(f"number 1 = {numbers[i]}")
            print(f"number 2 = {numbers[j]}")


# Brute Force Example - Checking a Password

correct_password = "python123"

password = input("Enter password: ")

if password == correct_password:
    print("Password is correct")
else:
    print("Password is incorrect")


# Brute Force Summary
#
# Brute Force checks all possible options.
# It is simple and easy to understand.
# It can be slow when the amount of data becomes large.
#
# Example:
#
# Searching for a value in an array:
#
# [10, 20, 30, 40, 50]
#          ↓
# Check 10
# Check 20
# Check 30
# Check 40
# Check 50
#
# The algorithm continues until the required value is found.