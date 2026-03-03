
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
        # Acknowledge users command
        print(f"commond type recognised: {user_input}")




if __name__ == "__main__":
    main()
