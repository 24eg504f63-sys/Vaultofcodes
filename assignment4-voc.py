# ==============================
# Personal To-Do List Application
# ==============================

import json
import os

# ------------------------------
# Task Class
# ------------------------------
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False  # Task status

    def mark_completed(self):
        """Mark the task as completed"""
        self.completed = True


# ------------------------------
# File Handling Functions
# ------------------------------
FILE_NAME = "tasks.json"

def save_tasks(tasks):
    """Save tasks to a JSON file"""
    with open(FILE_NAME, "w") as file:
        json.dump([task.__dict__ for task in tasks], file, indent=4)


def load_tasks():
    """Load tasks from a JSON file"""
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        task_list = json.load(file)
        tasks = []
        for data in task_list:
            task = Task(
                data["title"],
                data["description"],
                data["category"]
            )
            task.completed = data["completed"]
            tasks.append(task)
        return tasks


# ------------------------------
# Display Tasks
# ------------------------------
def view_tasks(tasks):
    """Display all tasks"""
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\n--- Your Tasks ---")
    for index, task in enumerate(tasks, start=1):
        status = "✔ Completed" if task.completed else "❌ Not Completed"
        print(f"{index}. {task.title}")
        print(f"   Description: {task.description}")
        print(f"   Category   : {task.category}")
        print(f"   Status     : {status}\n")


# ------------------------------
# Add New Task
# ------------------------------
def add_task(tasks):
    """Add a new task"""
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category (Work/Personal/Urgent): ")

    task = Task(title, description, category)
    tasks.append(task)
    print("\nTask added successfully!\n")


# ------------------------------
# Mark Task as Completed
# ------------------------------
def complete_task(tasks):
    """Mark a task as completed"""
    view_tasks(tasks)

    try:
        task_num = int(input("Enter task number to mark as completed: "))
        tasks[task_num - 1].mark_completed()
        print("\nTask marked as completed!\n")
    except (IndexError, ValueError):
        print("\nInvalid task number!\n")


# ------------------------------
# Delete Task
# ------------------------------
def delete_task(tasks):
    """Delete a task"""
    view_tasks(tasks)

    try:
        task_num = int(input("Enter task number to delete: "))
        tasks.pop(task_num - 1)
        print("\nTask deleted successfully!\n")
    except (IndexError, ValueError):
        print("\nInvalid task number!\n")


# ------------------------------
# Main Menu
# ------------------------------
def main():
    tasks = load_tasks()  # Load saved tasks

    while True:
        print("==== TO-DO LIST MENU ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("\nTasks saved. Exiting application.")
            break
        else:
            print("\nInvalid choice! Try again.\n")


# ------------------------------
# Program Execution Starts Here
# ------------------------------
if __name__ == "__main__":
    main()
