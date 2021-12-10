def perfect_squares(lower, upper):

    #initialize a variable to store our sum of perfect squares
    result = 0
    
    #for loop to go through our range provided by the user. Includes the last number. If you forget the +1
    # the range function will not check the upper number
    for i in range(lower, upper + 1):
        j = 1
        while j * j <= i:
            if j * j == i:
                result = result + 1
            j = j + 1
        i = i + 1
    return result
lower = int(input("input lowest number: "))
upper =  int(input("Input highest number: "))

print(f"The the number of squares is {perfect_squares(lower, upper)}")