import os

def display_tasks(tasks):
    print("\nTo-Do List:")
    if not tasks:
        print("No tasks to display.")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added.")

def remove_task(tasks):
    display_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task}\n")
    print("Tasks saved to tasks.txt")

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file]
    return []

def main():
    tasks = load_tasks()
    
    while True:
        print("\nMenu:")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Save and Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
