# 1 for Loop - Used to repeat a block of code for each item in a sequence.

for i in range(1, 6):
    print(f"Number = {i}")


# 2 for Loop with a List - Used to access each item in a list.

fruits = ["Apple", "Mango", "Banana"]

for fruit in fruits:
    print(f"Fruit = {fruit}")


# 3 for Loop with a String - Used to access each character in a string.

name = "Nikhil"

for character in name:
    print(f"Character = {character}")


# 4 for Loop with range() - Used to generate a sequence of numbers.

for i in range(1, 11):
    print(f"Number = {i}")


# 5 while Loop - Repeats a block of code as long as the condition is True.

i = 1

while i <= 5:
    print(f"Number = {i}")
    i += 1


# 6 break Statement - Stops the loop immediately.

for i in range(1, 11):

    if i == 5:
        break

    print(f"Number = {i}")


# 7 continue Statement - Skips the current iteration and continues with the next iteration.

for i in range(1, 6):

    if i == 3:
        continue

    print(f"Number = {i}")


# 7 pass Statement - Does nothing and is used as a placeholder.

age = 21

if age >= 18:
    pass
else:
    print("Minor")


# 8 Nested for Loop - A loop inside another loop.

for i in range(1, 4):

    for j in range(1, 4):
        print(f"i = {i}, j = {j}")


# 9 Nested while Loop - A while loop inside another while loop.

i = 1

while i <= 3:

    j = 1

    while j <= 3:
        print(f"i = {i}, j = {j}")
        j += 1

    i += 1