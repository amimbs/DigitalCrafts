# Dictionaires

airport_code = "IAH"
airport_name = "Intercontinental Airport"

# Dictionary = {Key: Value}

# Create a dictionary
    # The value of name is Intercontinetal airport, and the value of code, is IAH
airport = {"name": "Intercontinental Airport", "code": "IAH"}

user = {"first_name": "John", "last_name": "Doe", "age": 45}

# how to acess the elements, you need to know the key
print(airport["code"])
    #the key must be in quotes, and it will return the value of the key "code", which is "IAH"


# today's assignment

tasks= []

while True:
    print("Enter 1 to add task: ")
    print("Press q enter to quit: ")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter Title: ")
        priority = input("Enter priority: ")
        task = {"title": title, "priority": priority}
        tasks.append(task)
    elif choice == "q":
        break

print(tasks)