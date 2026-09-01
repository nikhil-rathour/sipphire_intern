
# 6.5 Key Value Pairs
# Key-value pairs store data using a key and its corresponding value.
# In Python, dictionaries are used for key-value pairs.

student = {
    "name": "Nikhil",
    "age": 21,
    "course": "Python",
    "marks": 85
}

print(f"student = {student}")


# Accessing Values Using Keys

student = {
    "name": "Nikhil",
    "age": 21,
    "course": "Python"
}

print(f"name = {student['name']}")
print(f"age = {student['age']}")
print(f"course = {student['course']}")


# Adding a New Key-Value Pair

student = {
    "name": "Nikhil",
    "age": 21
}

student["course"] = "Python"

print(f"student = {student}")


# Updating a Value

student = {
    "name": "Nikhil",
    "age": 21,
    "marks": 80
}

student["marks"] = 90

print(f"student = {student}")


# Removing a Key-Value Pair

student = {
    "name": "Nikhil",
    "age": 21,
    "course": "Python"
}

del student["course"]

print(f"student = {student}")


# Traversing Key-Value Pairs

student = {
    "name": "Nikhil",
    "age": 21,
    "course": "Python"
}

for key, value in student.items():
    print(f"{key} = {value}")
