# Logical Operators Example in One Code
x = 10
y = 5
z = 15
# AND operator
print("AND Operator:")
if x > 5 and y < 10:
    print("Both conditions are True")  # True
# OR operator
print("\nOR Operator:")
if x < 5 or z > 10:
    print("At least one condition is True")  # True
# NOT operator
print("\nNOT Operator:")
is_logged_in = False
if not is_logged_in:
    print("User is not logged in")  # True
# Combined logic
print("\nCombined Logic:")
age = 20
has_ticket = True
if age >= 18 and has_ticket:
    print("You can enter the concert!")  # True
else:
    print("Entry not allowed.")
