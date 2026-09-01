# 4. Conditional Statements - Conditional statements are used to make decisions based on conditions.


# 4.1 if Statement - Executes a block of code when the condition is True.

age = 21

if age >= 18:
    print(f"age = {age}")
    print("Eligible to vote")


# 4.2 if-else Statement - Executes one block when the condition is True and another when it is False.

age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# 4.3 if-elif-else Statement - Used when there are multiple conditions.

marks = 85

if marks >= 90:
    print("Grade = A+")
elif marks >= 80:
    print("Grade = A")
elif marks >= 70:
    print("Grade = B")
elif marks >= 60:
    print("Grade = C")
else:
    print("Grade = F")


# 4.4 Nested if Statement - An if statement inside another if statement.

age = 21
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID is required")
else:
    print("Entry not allowed")