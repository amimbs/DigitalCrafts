
# Files

# Writing
# Open(Name of the file, mopdel) by default mode is "r"

# w = writing a file
# r = reading a file
# a = appending mode

file = open("todo.txt", "w")

# write text to the file 
file.write("Mow the lawn")
file.write("Clean the car")


# Always close the file
file.close()

