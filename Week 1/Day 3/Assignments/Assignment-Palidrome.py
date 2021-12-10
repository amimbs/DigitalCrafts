print("This program checks if a word you entered is a palidrome.")

# Define palidome function
def check_if_palidrome(string):
    length = len(string)
    first_letter = 0
    last_letter = length - 1

    #boolean that'll lead to print
    is_palidrome = True
    
    # compares the first letter to the last letter, if both are equal, increments from the first letter and deincrements from the last ltter and compares again until finished
    while (first_letter < last_letter):
        if (string[first_letter] == string[last_letter]):
            first_letter = first_letter + 1
            last_letter = last_letter - 1
        else:
            is_palidrome = False
            break
    return(is_palidrome)

string = input("What word do you want checked?: ")

is_palidrome = check_if_palidrome(string)

if(is_palidrome):
    print("It is a palidrome")
else:
    print("The word is not a palidrome.")