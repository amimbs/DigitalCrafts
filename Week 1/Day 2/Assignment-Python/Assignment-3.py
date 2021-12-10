#Fizz Buzz

print("This program determine if a number is divisible by 3, 5, or both!")

# Initalize our function as well as prime our print statements
def fizzbuzz():
    if (user_number % 3) == 0 and (user_number % 5) == 0:
        print("Fizz Buzz")
    elif (user_number % 3) == 0:
        print("Fizz")
    elif (user_number % 5) == 0:
        print("Buzz")

# error handling
try:
    user_input = (input("Please input a whole number: "))
    user_number = int(user_input)
    bird_word = fizzbuzz()
except NameError:
    print(NameError)