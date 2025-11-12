# 1calculator function

def calulator(a,b,symbol) :
    if symbol == "+" :
        return a + b
    elif symbol == "-" :
        return a - b
    elif symbol == "*" :
        return a * b
    elif symbol == "/" :
        return a / b
    else :
        return "Invalid symbol"

a = input("Enter first number: ")
b= input ("Enter second number: ")
symbol = input("Enter symbol (+, -, *, /): ")
result = calulator(float(a), float(b), symbol)
print("Result: ", result)
# Simple calculator function that performs basic arithmetic operations based on user input.
# It takes two numbers and an operator symbol as input and returns the result of the operation.

# Exception handling in the calculator function

def calculator_with_exception(a, b, option):
    try:
        if option == "1":
            return a + b
        elif option == "2":
            return a - b
        elif option == "3":
            return a * b
        elif option == "4":
            return a / b
        else:
            return "Invalid option"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"

a = input("Enter first number: ") 
b= input ("Enter second number: ")
option = input("Enter option (1: +, 2: -, 3: *, 4: /): ")
result = calculator_with_exception(float(a), float(b), option)
print("Result: ", result)