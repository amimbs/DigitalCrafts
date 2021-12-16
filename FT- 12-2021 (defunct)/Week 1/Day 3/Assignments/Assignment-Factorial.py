number = int(input("Enter the number you want the factorial of: "))

def factorial(number):
    fact = 1
    if number < 0:
        print("Cannot calculate the factorial of a negative number")
    elif number == 0:
        print (f"the factorial of {number} is 1")
    else:
        for index in range(number, 0, -1):
            fact = fact*index
        print(f"The factorial of {number} is {fact}")

(factorial(number))



