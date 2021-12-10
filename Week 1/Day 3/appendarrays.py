# append/add to an array

animals = []

#adding to an array
animals.append("cat")
animals.append("dog")
animals.append("horse")
animals.append("mouse")
animals.append("chicken")

#insert item at a specifical location
animals.insert(0, "Lion")

print(animals)

#remove item from an array
animals.remove("cat")
print(animals)

#remove an animal based on an index
del animals[3]

#update an item
animals[2] = "Zebra"
print(animals)

#while loop

#while condition
    #body of the loo

counter = 0
while counter < 10:
    print("Hello")
    counter = 11

shopper_list_items = []

while True:
    item = input("What do you want to buy: ")
    shopper_list_items.append(item)

    choice = input("Press q to quit or any key to continue: ")
    if choice == "q":
        break

#want to print it vertically?
#for item in shopper_list_items:
    #print(item)

#we can also enumerate it
for index in range(0, len(shopper_list_items)):
    print(f"{index + 1}. {shopper_list_items[index]}")


