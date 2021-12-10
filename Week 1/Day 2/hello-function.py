# Function -Lines of code that serve a common/particular purpose

first_name = "John"
last_name = "Doe"
customer_id = "123456"

# in python define a function you must start it with def
def display_user_info():
    print(f"{customer_id}")
    print(f"My first name is {first_name} and my last name is {last_name}")

# after defining the function, you must call it after the fact for it to execute
display_user_info()

# functions can take arguments as well
def greet(name, age):
    print(f"Hello {name} and my name is {age}")

greet("John", 35)

def add(a, b):
    answer = a + b
    return answer

#return sends the value from the function to the left hand side, so if you want it to appear, you must have a left hand side assignment
result = add(2, 5)
print(result)

def calculate_overdraft_fees(amount):
    return amount * 0.10

overdraft_fee = calculate_overdraft_fees(100)
print(overdraft_fee)

# tuple - means muliple values
#def get_airport_name_and_code():
    #return ("Intercontinental Airport", "IAH")

#(airport_name, airport_code) = get_airport_name_and_code()

#Optional Arguments
def greet_user(name, age = 21):
    print(name)
    print(age)

greet_user("Alex Doe") #age = 21
greet_user("Mary Doe", 54) # age = 54

#CONDITIONS

user_age = 16
citizen = "US"

if user_age >= 18:
    print("User is older than 18")
elif user_age < 18 and citizen == "AUS": # instead of and you can use or, so that as long as one of the conditionals is met, the line will execute. Note == is comparison and = is assignment
    print("User is younger than 18 and citizen of AUS")
else: 
    print("Conditions are not met")
