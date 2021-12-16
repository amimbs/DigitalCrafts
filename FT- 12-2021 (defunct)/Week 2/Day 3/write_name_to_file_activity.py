# user_name = input("Please type your full name: ")

# with open("guest.txt", "w") as file:
#     file.write(user_name) 

# # Append to a file
# with open("todo.txt", "a") as file:
#     file.write("clean car") # every time you edit this you it will print a new line and append to the file
#     file.write("\n")

# Appending to a file Activity 2
# q and enter will quit

# # user_responses = []

# # while True:
# #     choice = input("Press 1 to enter a response or q to quit: ")
# #     if choice == "1":
# #         user_repsonse = input("Why do you like programming?: ")
# #         user_responses.append(user_repsonse)
# #     elif choice == "q":
# #         break



# # with ("love_programming.txt", "a") as file:
# #     file.write(user_responses[user_repsonse])

# Above code did not work



# while True:
#     friend_name = input("Enter your friend's name: ")
#     if friend_name == "q":
#         break

#     with ("friends", "a") as file:
#         file.write(friend_name)
#         file.write("\n")

# Read a file

# with open("todo.txt") as file: # the file mist exist for this code to w
#     content = file.read()
#     print(content)

# with open("todo.txt") as file:
#     # file.readlines will return you an array containing each line
#     lines = file.readlines()
#     print(lines)


# Activity 3 - Reading from a file

#     Ask user for input for their favorite dish. And write the name of the dish in the file.

#     You will read our favorite dishes file and display them on the screen

# file = open("favorite_dish.txt", "w")

# # while True:
# #     favorite_dish = input("Enter your favorite dish: ")
# #     if favorite_dish == "q":
# #         break

# #     with ("favorite_dish.txt", "a") as file:
# #         file.write(favorite_dish)
# #         file.write("\n")

# #     with ("favorite_dish.txt") as file:  
# #         content = file.read()
# #         print(content)    



# # file = open("favorite_dish.txt", "w")


# # while True:
# #     favorite_dish = input("Enter your favorite dish: ")
# #     if favorite_dish == "q":
# #         break

# #     with ("favorite_dish.txt", "a") as file:
# #         file.write(favorite_dish)
# #         file.write("\n")


# # with ("favorite_dish.txt") as file:  
# #     content = file.read()

# # print(content)    
