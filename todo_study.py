import os # import os module so that we can use functions inside
FILE = "tasks.txt" # set the file name used to store the task list
def load_tasks(): # create a function to load all tasks from the file
    if not os.path.exists(FILE): # check whether file exists
        return [] # if the file does not exist, return an empty list
    with open(FILE, "r") as f: # if the FILE exists, open it in read mode
        return [line.strip() for line in f.readlines()] # read each line, and remove extra spaces/newlines

def save_tasks(tasks): # create a function to save tasks to the file
    with open(FILE, "w") as f: # open file in write mode
        for task in tasks: # loop through each task in the list
            f.write(task + "\n") # write each task to the file on a new line

def show_menu(): # create a function to show the menu
    print("\n==== TO-DO LIST ====") # print 1st line in the menu
    print("1. View Tasks") # print 2nd line in the menu
    print("2. Add Task") # print the 3rd line in the menu
    print("3. Delete Task") # print the 4th line in the menu
    print("4. Exit") # print the 5th line in the menu
    return input("Choose an option: ") # ask user to enter a choice

tasks = load_tasks() # load the task and store them in the variable
while True: # keep looping until the program is stopped with break
    choice = show_menu() # show the menu and store the user's choice
    if choice == "1": # if the user enters 1
        if not tasks: # if the task list is empty
            print("No tasks found.") # print a message saying there are no tasks
        else: # otherwise
            for i, task in enumerate(tasks, start=1): # go through the tasks one by one with numbers
                print(f"{i}. {task}") # print the task number and the task
    elif choice == "2": # if the user enters '2'
        task = input("Enter new task: ") # ask the user to enter a new task
        tasks.append(task) # add the new task to the list
        save_tasks(tasks) # save the updated task list to the file
        print("Task added!") # tell the user the task was added
    elif choice == "3": # if the user enters '3'
        num = int(input("Enter task number to delete: ")) # ask which task number to delete and convert it to an integer
        if 1 <= num <= len(tasks): # check if the number is within the valid range
            removed = tasks.pop(num - 1) # # remove the chosen task from the list
            save_tasks(tasks) # save the updated task list to the file
            print(f"Deleted: {removed}") # show which task was deleted
        else: # if the number is not in the valid range
            print("Invalid task number.") # tell the user the number is invalid
    elif choice == "4": # if the user enters 4
        print("Goodbye!") # tell the user the program is ending
        break # stop the while loop
    else: # if the user enters something else
        print("Invalid choice.") # tell the user the choice is invalid
