
def main():

    # Dict to store users tasks
    tasks = {}


    # program persistance
    while True:
        # Print instruction
        print("type 'quit' to end app")
        # Get user task
        user_input = input("Enter command type: ")
        # Check user input is quit
        if user_input == "quit":
            print("You have closed the App")
            break
        # if the command is 'add'
        elif user_input == "add":
            task_name = input("Enter task name: ") # Ask for user task and store in var
            tasks[task_name] = False # Add that task to the tasks dict as the key
            print(f"the task {task_name} as been added to your Todo list")

if __name__ == "__main__":
    main()
