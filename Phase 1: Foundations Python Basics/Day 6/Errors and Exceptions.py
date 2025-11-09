# Error 

# An error is a mistake in the code that prevents it from running correctly.
# There are different types of errors in Python, including syntax errors and exceptions.
# Syntax Error
# A syntax error occurs when the code is not written in the correct format.
# Example of a syntax error:
# print("Hello, World!"
# This will raise a SyntaxError because the closing parenthesis is missing.
# To fix it, add the missing parenthesis:
print("Hello, World!")
# Exceptions
# An exception is an error that occurs during the execution of the code.
# Example of an exception:
def divide_numbers(a, b):
    return a / b
try:
    result = divide_numbers(10, 0)
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
# In this example, trying to divide by zero raises a ZeroDivisionError.
# We handle the exception using a try-except block to prevent the program from crashing.
# You can also handle multiple exceptions:
def access_list_element(lst, index):
    return lst[index]
my_list = [1, 2, 3]
try:
    element = access_list_element(my_list, 5)
    print("Element:", element)
except IndexError:
    print("Error: Index out of range!")
except Exception as e:
    print("An unexpected error occurred:", e)
# In this example, trying to access an out-of-range index raises an IndexError.

# Finally, you can use the finally block to execute code regardless of whether an exception occurred or not:

try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found!")
finally:
    print("Execution completed.")


# In this example, the finally block will always execute, whether or not an exception occurred.