# This program attempts to convert the string into an integer using the int() function,
# if a valueError is raised, the code inside the 'except' block will execute - printing the error message.

string = "Hello"
try:
    num = int(string)
except ValueError:
    print("The string is not a number")



