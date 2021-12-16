print("This program will tell you if a number you input is Prime or not")

number = int(input("Enter the number you're curious about: "))

#Function prompts the user and calls our is_it_prime function

def is_it_prime(number):
    #check if the number is 2, if it is, return true because 2 is a prime number
    if number == 2:
        print("2 is a prime number")
        return True
    #check if a number can be divided by 2 until 0 or if it's less than 1. If so, it is not prime
    elif number <= 1:
        print(f"{number} must be greater than 1")
    else:
        for index in range(2, number):
            if number % index == 0:
                print(f"{number} is not prime")
            print(f"{number} is prime")
            return True

is_it_prime(number)


