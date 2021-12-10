# today's assignment

# print(tasks)
def print_list(task_list):
    print("----------------------------------------------------")

    for i in range(0,len(task_list)): 
        print(f"Task: {i + 1} {task_list[i]['title']} Priority: {task_list[i]['priority']}")
        
    print("----------------------------------------------------")

# initalize the list
tasks = []

while True:
    print("Enter 1 to add task: ")
    print ("Enter 2 to delete a task")
    print("Enter 3 to view all tasks")
    print("Press q enter to quit: ")
    choice = input("Enter choice: ")
    if choice == "1":
        title = input("Enter Title: ")
        priority = input("Enter priority: ")
        task = {"title": title, "priority": priority}
        tasks.append(task)
    elif choice == "2":
        completed = input("Enter the Title of the task you've completed: ")
        # -1 because we were falling out of the list
        for i in range(0, len(tasks) - 1):
            if tasks[i]['title'] == completed:
                print(f"Task: {tasks[i]['title']} completed") 
                del tasks[i]
    elif choice == "3":
        print_list(tasks)
    elif choice == "q":
        break


