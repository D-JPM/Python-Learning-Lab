
def main():

    # Dict to store users tasks
    tasks = {}

    # Print instructions
    print("""
        ==== Using the App ====
        Commands:
        - add: Add a new task (you then will be asked to input the task)
        - quit: Close the app
        """)


    # program persistance
    while True:
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
        elif user_input == "list":
            if not tasks:
                print("Your Todo list is empty, nothing to display")
            for task, completed in tasks.items():
                if completed:
                    print(f"{task} Completed")
                else:
                    print(f"{task} Not completed")
        elif user_input == "done":
            task_name = input("Enter task name: ") # Ask for user task and store in var
            if task_name in tasks:    
                tasks[task_name] = True # Add that task to the tasks dict as the key
                print(f"the task {task_name} as been completed")
            else:
                print(f"the {task_name} is not in your Todo list!")

if __name__ == "__main__":
    main()
