def menu():
    print("\n--- To Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Completed")
    print("5. Exit")


# ---------- ADD TASK ----------
def add_task():
    task = input("Enter a new task: ")

    with open("task.txt", "a") as file:   # "a" → append mode
        file.write(task + ",False\n")     # store task with status False

    print("Task added successfully!")


# ---------- VIEW TASKS ----------
def view_tasks():
    try:
        with open("task.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks found.")
            return

        for index, task in enumerate(tasks, start=1):
            name, status = task.strip().split(",")

            mark = "✓" if status == "True" else " "

            print(f"{index}. {name} [{mark}]")

    except FileNotFoundError:
        print("No task file found.")


# ---------- DELETE TASK ----------
def delete_task():
    try:
        with open("task.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks to delete.")
            return

        for index, task in enumerate(tasks, start=1):
            name, status = task.strip().split(",")
            print(f"{index}. {name}")

        delete_num = int(input("Enter task number to delete: "))

        if 1 <= delete_num <= len(tasks):
            tasks.pop(delete_num - 1)

            with open("task.txt", "w") as file:
                file.writelines(tasks)

            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

    except FileNotFoundError:
        print("No task file found.")


# ---------- MARK TASK COMPLETED ----------
def mark_completed():
    try:
        with open("task.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks available.")
            return

        for index, task in enumerate(tasks, start=1):
            name, status = task.strip().split(",")
            print(f"{index}. {name}")

        complete_num = int(input("Enter task number to mark complete: "))

        if 1 <= complete_num <= len(tasks):
            name, status = tasks[complete_num - 1].strip().split(",")
            tasks[complete_num - 1] = name + ",True\n"

            with open("task.txt", "w") as file:
                file.writelines(tasks)

            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except FileNotFoundError:
        print("No task file found.")


# ---------- MAIN PROGRAM LOOP ----------
while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        mark_completed()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
