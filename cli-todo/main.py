
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

        # split words for single line command logic
        words = user_input.split()
        
        # if user inputs nothing 
        if not words:
            continue
        
        # Check user input is quit
        if user_input == "quit":
            print("You have closed the App")
            break
        
        # if the command is 'add'
        elif words[0] == "add": 
            # Joine all words back together expect for first words as it's the command
            task_name = " ".join(words[1:])
            if not task_name:
                print("You need to enter a task name")
            else:
                tasks[task_name] = False
                print(f"the task [{task_name}] as been added to your Todo list")

            
        
        # if the command is 'list'    
        elif user_input == "list":
            if not tasks:
                print("Your Todo list is empty, nothing to display")
            for task, completed in tasks.items():
                if completed:
                    print(f"{task} Completed")
                else:
                    print(f"{task} Not completed")
        
        # if the command is 'done'
        elif user_input == "done":
            task_name = input("Enter task name: ") # Ask for user task and store in var
            if task_name in tasks:    
                tasks[task_name] = True # Add that task to the tasks dict as the key
                print(f"the task {task_name} as been completed")
            else:
                print(f"the {task_name} is not in your Todo list!")
        
        # if the command is 'remove'
        elif user_input == "remove":
            task_name = input("Enter task name: ") # Ask for user task and store in var
            if task_name in tasks:    
                tasks.pop(task_name)
                print(f"the task {task_name} as been removed")
            else:
                print(f"the {task_name} is not in your Todo list!")


if __name__ == "__main__":
    main()
