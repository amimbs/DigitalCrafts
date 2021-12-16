
# modules

# import our module
# import utils
import calculator


# we can also import our module as a variable if we're tired of writing it all the time
import utils as u

# you can also imort the entirity of the utils.py file so that you dont have to prefix each funciton you need. Bare in mind this is dangerous tho. The astrix means everything
# from utils import *

print("Enter 1 for palidrome: ")
print("Enter 2 for even/odd: ")
print("Enter 3 for prime: ")

choice = int(input("Enter choice: "))

#implement one of the functions we wrote in our utils.py file

# utils.is_palidrome("cat")
print(calculator.add(1,5))

# using the variable to call the utility function
u.is_palidrome("cat")

