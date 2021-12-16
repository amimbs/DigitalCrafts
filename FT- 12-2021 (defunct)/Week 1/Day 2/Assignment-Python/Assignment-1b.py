print("This program functions as your personal calculator")

#initalize calculator functions
def addition():
        sum = (first_number + second_number)
        print(sum)

def subtraction():
        difference = (first_number - second_number)
        print(difference)

def multiplication():
        product = (first_number * second_number)
        print(product)

def division():
        quotient = (first_number / second_number)
        print(quotient)

def valid():
    return operator in ["+", "-", "*", "/"]

# User inputs variables
first_number = float(input("Please input your first number: "))
operator = input("Please input the operation you want performed (+, -, *, /): ")
second_number = float(input("Please unput the second number: "))        

# Checks user inputs and return an error
if valid():
    if operator == "+":
        addition()
    elif operator == "-":
        subtraction()
    elif operator == "*":
        multiplication()
    elif operator == "/":
        division()
else:
    print("Invalid Input")   








