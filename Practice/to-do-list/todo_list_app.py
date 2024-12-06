import json
tasks = []


def display_menu():
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found!")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["completed"] else "❌"
            print(f"{i}. {task['task']} [{status}]")

def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as completed: ")) - 1
        tasks[task_num]["completed"] = True
        print("Task marked as completed!")
    except (ValueError, IndexError):
        print("Invalid task number!")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: ")) - 1
        tasks.pop(task_num)
        print("Task deleted successfully!")
    except (ValueError, IndexError):
        print("Invalid task number!")


def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file)

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    tasks = load_tasks()  # Load saved tasks if any
    
    while True:
        display_menu()
        choice = input("Choose an option: ")
         
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_task_completed(tasks)
        elif choice == "5":
            save_tasks(tasks)  # Save tasks before exiting
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()