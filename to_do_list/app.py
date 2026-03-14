import json

def menu():
    print("\n--- To Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Completed")
    print("5. Exit")


def load_tasks():
    try:
        with open("task.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    with open("task.json", "w") as file:
        json.dump(tasks, file, indent=4)


def add_task():
    tasks = load_tasks()
    task = input("Enter a new task: ")

    tasks.append({
        "task": task,
        "completed": False
    })

    save_tasks(tasks)
    print("Task added successfully!")


def view_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        mark = "✓" if task["completed"] else " "
        print(f"{index}. {task['task']} [{mark}]")


def delete_task():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['task']}")

    try:
        delete_num = int(input("Enter task number to delete: "))

        if 1 <= delete_num <= len(tasks):
            tasks.pop(delete_num - 1)
            save_tasks(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def mark_completed():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['task']}")

    try:
        complete_num = int(input("Enter task number to mark completed: "))

        if 1 <= complete_num <= len(tasks):
            tasks[complete_num - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


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
