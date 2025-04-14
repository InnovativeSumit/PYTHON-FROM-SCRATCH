# Global Variable: Declared outside all functions and accessible (and modifiable with 'global' keyword) throughout the program.

global_var = "I am global!"  # Global variable

def show_global():
    print("Inside function:", global_var)

def modify_global():
    global global_var  # Required to modify global variable
    global_var = "I have been changed globally!"

show_global()
modify_global()
show_global()
