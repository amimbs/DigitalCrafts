print("This program will tell you if a number is even or odd")

# Initalize and define our even/odd function
def find_number():
    if (user_number % 2) == 0:
        numbertype = "even"
    else:
        numbertype = "odd"
    return numbertype

# Executing the function so long as the user input a whole number
try:
    user_input = (input("Please enter a whole number: "))
    user_number = int(user_input)
    numbertype = find_number()
    print("Your number is", numbertype, ".")

# Error handling using NameError so that python shows why the code does not execute
except NameError:
    print(NameError)
