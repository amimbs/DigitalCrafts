
class Car: 
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = ""
        self.speed = 0
        self.current_gear = "N"
    # we cand efine the actions a car can take within the class
    # def drive(): #however, in a class if we define a function like this, it WILL NOT work
    def drive(self): # you must pass self into the function so that this propoerty is avaiable to objects
        # we can change multiple propoerties within a nexted function in a Class
        self.speed += 20
        self.current_gear = "D"
        print("Car is driving")

    def change_gear(self, gear):
        self.current_gear = gear
    
    def stop(self):
        self.speed = 0
        self.current_gear = "P"



car = Car("Honda", "Accord")
print("Before driving")
print(car.speed)
print(car.current_gear)


print("\n")

print("After driving")
car.drive()
print(car.speed)
print(car.current_gear)
print("\n")

car.change_gear("R")
print("Reversing")
print(car.current_gear)
print("\n")

car.stop()
print("After stopping")
print(car.speed)
print(car.current_gear)
