print("This program allows you to discover a person's info at the command prompt. That info can be their name, gender, age, address and phone.")

# user_name =  {"first_name": [], "last_name": []}
# user_name = ["first_name"].append(input("What is your first name? "))
# user_name = ["last_name"].append(input("What is your last name? "))

# print(user_name)

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

user = {"first_name": first_name, "last_name": last_name}

print(f"My name is {user['first_name']}, {user['last_name']}")