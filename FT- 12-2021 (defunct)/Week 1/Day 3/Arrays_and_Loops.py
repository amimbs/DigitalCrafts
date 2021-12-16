#Array and loops

# Empty ARRAY
# friends = []

friends = ["John", "David", "Ya Boi", "Chad", "Brad"]

# An array can have difference data types
things = [3.14, True, 'John, "Chad']

# How to access the array, arrays are indexed at zero
friends[2] # 'Alex'
friends[3] # 'Ya Boi'

friend_name = friends[2]

print(friend_name)

# Error Index out of range
# friends[7]

# Print all the elements of an array

#Iterate through the array
print(friends[0:-1])
# or
for index3 in range(0,4):
    print(friends[index3])

# loops

# for loops

for index in range(1,10):
    print(index)
    #because we started at 1, it will always be one less than our final argument

for index2 in range(1, 101):
    if index2 % 2 == 0:
        print("Even")
    else:
        print("Odd")

# what if we didn't want to keep changing the index because the array gets longer and longer
print(len(friends))

for index4 in range(0, len(friends)):
    print(friends[index4])

# for foreach loop 
    # friends = ["John", "David", "Ya Boi", "Chad", "Brad"]
print ("FOR - FOREACH LOOP")
for friend in friends:
    print(friend)

# numbers = []

# for index in range[1,5]:
    # number = int(input("Enter number: "))
    # numbers.append(number)

# Loop in reverse order
# the range function takes a start point, and end point, and an increment
print("Loops in reverse order")
for index5 in range((len(friends) - 1), -1, -1):
    print(friends[index5])

#we can also start at the 0 point and only list every other number
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for index6 in range(0, len(numbers), 2):
    print(numbers[index6])