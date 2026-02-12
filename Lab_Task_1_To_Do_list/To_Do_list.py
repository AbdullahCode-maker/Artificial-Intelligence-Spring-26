class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
        print("Task added")
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed")
        else:
            print("Task not found")
    def display(self):
        print("Your Tasks:", self.tasks)
obj = ToDoList()
while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter task to add: ")
        obj.add_task(task)
    elif choice == "2":
        task = input("Enter task to remove: ")
        obj.remove_task(task)
    elif choice == "3":
        obj.display()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")