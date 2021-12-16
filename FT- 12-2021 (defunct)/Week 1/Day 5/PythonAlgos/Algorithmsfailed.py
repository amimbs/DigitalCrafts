# Return the number of perfect squares between 2 intergers a and b, inclusive

lower_limit = int(input("Enter the lowest number: "))
upper_limit = int(input("Enter the highest number: "))

#we deifne a variable to hold the number we're checking the perfect square of. 
# THe range fucntion excludes the number after the first comma. Sof if we want our program to include our
# second input in this case we should do +1 to our stop argument
for num in range(lower_limit, upper_limit+1):
    #result is a variable that will hold the sum of the total number of positive square roots we find
    result = 0
    #find the perfect positive divisor of num at each step
    # i is our variable holding the value up to num going all the way to the end
    for i in range(1, num):
        if (num % i) == 0:
            # if the number divided by an interger up to it's vale is a perfect square, then add that result to results
            result = result + 1
    # if the num is = to the result sum then that is a perfect square
    if num == result:
        print(num)
        
