cars = []

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model


honda = Car("Honda", "Accord")
toyota = Car("Toyota", "Camry")

cars.append(honda)
cars.append(toyota)

# This will print toyota
car = cars[1]

# This also points to toyota
another_car = car


another_car.make = "Tesla"
another_car.model = "X"


#These will now print Tesla X because another_car has pointed to the location of toyota camry and changed them
print(car.make)
print(car.model)