# Local Variable: Declared inside a function and accessible only within that function.

def greet():
    local_var = "Hello, I am local!"  # Local variable
    print("Inside function:", local_var)

greet()

# Trying to access local_var outside the function will cause an error:
# print(local_var)  # ❌ Uncommenting this will raise a NameError
