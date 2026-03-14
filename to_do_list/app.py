def menu():
    print("\n---- TO DO LIST ----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task Completed")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Add Task Selected")

    elif choice == "2":
        print("View Tasks Selected")

    elif choice == "3":
        print("Delete Task Selected")

    elif choice == "4":
        print("Mark Task Completed Selected")

    elif choice == "5":
        print("Exiting program")
        break

    else:
        print("Invalid choice")
