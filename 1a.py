'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added.")

def view_tasks():
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks.")

def delete_task(index):
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
        print("Task deleted.")
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
       
        choice = input("Enter your choice: ")
       
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            index = int(input("Enter task index to delete: "))
            delete_task(index)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

