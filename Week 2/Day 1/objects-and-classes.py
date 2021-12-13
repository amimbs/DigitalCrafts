

# classes
# blue print

from typing import ClassVar


# Car car is a class/blueprint in this example
# - model
# - make 
# - vin
# - color 

# person - the class here is a person/blueprint
# - height 
# - weight 
# - age
# - hair_color 


# creating BMW using Car Blueprint

# BMW:
# - Model: Series 3
# - Make =  BMW
# - Vin = 345
# - Color = blue


# Table 
# - material
# - width
# - height 
# - cost 
# - shape

# Cherry Wood Table 
# - wood
# - 4 feet 
# - 4 feet 
# - 200 
# - square 

###################################################################################################################################################################################################

# Car car is a class/blueprint in this example
# - model
# - make 
# - vin
# - color


# class is simply a blue print that defines using properties. And can be used to define something concrete aka objects

# name of class should always being with Capital
#Letter
class Car:
#     def __init__(self): # this is called the initializor constructor used to create and object of it's above class
#         #pass # this means we're not ready to add the hardcode
#         # self represents the object of the car class in the below example: my_car (line 67). So we can create new catagories for our blueprint
#         self.make = ""
#         self.model = ""
#         self.color = "Red" # if we assign a value in the constructor, the value you assign will be default

# # creating an instance/object of Car class
# my_car = Car() # we must call the consturctor and pass our object to it
# my_car.make = "Honda"
# my_car.model =  "Accord"
# # if we pass a property into our constructor that doesn't exist, it will assign it but it will not be available to other objects. Porpoerties must be defined in the init
# # my_car.vin = "3445"

# another_car = Car()
# another_car.make = "Toyota"
# another_car.model = "Camry"

# What if in order to create Car object we must padd in the make and model?:

    def __init__(self, make, model):
        self.make = make
        self.model = model

car = Car("Hoda", "Accord")
print(car.make)
print(car.model)

#Create a class called customer. Must pass in first name and last name

class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        # what happens if we initialize property that's not party of our argument? Answer: YOU MUST USE SELF SO THAT IT'S AVAIBLE TO ALL OBJECTS
        # full_name = first_name + " " + last_name
        self.full_name = first_name + " " + last_name
        self.age = 18 # doesn't matter that age isn't part of the init argument because here you're just making all the objects default to 18
        self.plan = "Bronze" # we can changes these values in the objects (line 100)

customer = Customer("Andrew", "Mimbs")
customer.plan = "Silver Plan"
print(customer.first_name)
print(customer.last_name)
print(customer.full_name)
print(customer.plan)

another_customer = Customer("Jane", "Doe")
print(another_customer.first_name)
print(another_customer.last_name)
print(another_customer.full_name)

# what happens if we try to just print an object?
# print(customer) - doesn't work python will display the memory address

class Table:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        material = ""

table = Table(100, 200)
table.material = "Oak Wood"


