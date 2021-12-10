print("This program will tell you if a number is even or odd")

# Initalize and define our even/odd function
def find_number():
    if (user_number % 2) == 0:
        # the return here should end this function, else it'll return odd??
        return "even"
    return "odd"

user_number = (input("Please enter a whole number: "))

# Executing the function so long as the user input a whole number
try:
    user_number = int(user_number)
    numbertype = find_number()
    print("Your number is", numbertype, ".")

# Error handling using NameError so that python shows why the code does not execute
except NameError:
    print(NameError)
