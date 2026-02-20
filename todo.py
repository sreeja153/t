# ================================
# Console-based To-Do List App
# File: todo.py
# ================================

FILE_NAME = "tasks.txt"


def load_tasks():
    """Load tasks from file into a list"""
    try:
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Save all tasks to file"""
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def view_tasks(tasks):
    """Display all tasks"""
    if not tasks:
        print("\n📭 No tasks available.\n")
        return

    print("\n📋 Your To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()


def add_task(tasks):
    """Add a new task"""
    task = input("✍️ Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added successfully!\n")
    else:
        print("⚠️ Task cannot be empty.\n")


def remove_task(tasks):
    """Remove a task by number"""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        choice = int(input("❌ Enter task number to remove: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"🗑️ Task '{removed}' removed.\n")
        else:
            print("⚠️ Invalid task number.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")


def main():
    tasks = load_tasks()

    while True:
        print("====== TO-DO LIST MENU ======")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        print("=============================")

        choice = input("👉 Choose an option (1-4): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("\n👋 Goodbye! Your tasks are saved.\n")
            break
        else:
            print("⚠️ Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()