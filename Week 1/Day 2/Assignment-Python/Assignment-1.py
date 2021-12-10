print("This program functions as your person calculator")

#Variables
first_number = float(input("Please input your first number: "))
operator = input("Please input the operation you want performed (+, -, *, /): ")
second_number = float(input("Please unput the second number: "))

def calculation():
    if operator == "+":
        print(first_number + second_number)
    elif operator == "-":
         print(first_number - second_number)
    elif operator == "*":
         print(first_number * second_number)
    elif operator == "/":
         print(first_number / second_number)

calculation()