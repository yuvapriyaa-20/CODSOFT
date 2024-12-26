#To do list
class Todolist:
    def __init__(self):
        self.tasks = []
    def add_task(self,task):
        self.tasks.append({"task": task, "status":"Pending"})
        print(f"Task '{task}' added successfully")
    def view_task(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("\nYour To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}.{task['task']} - {task['status']}")
    def update_task(self,task_number):
        if 0 < task_number <=len(self.tasks):
            self.tasks[task_number - 1]["status"] = "Completed"
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")
    def delete_task(self,task_number):
        if 0 < task_number <=len(self.tasks):
            removed_task = self.tasks.pop(task_number -1)
            print(f"Task '{removed_task ['task']}' deleted successfully.")
        else:
            print("Invalid task number.")
    def clear_tasks(self):
        self.tasks.clear()
        print("All tasks cleared successfully.")
def main():
    todo_list  =  Todolist()
    while True:
        print("\n---To-Do List Menu---")
        print("1.Add Task")
        print("2. View Tasks")
        print("3.Update Task Status")
        print("4.Delete Task")
        print("5.Clear All Tasks")
        print("6.Exit")
        try:
            choice = int(input("Choose an option:"))
            if choice ==1:
                task = input("Enter the task description:")
                todo_list.add_task(task)

            elif choice ==2:
                todo_list.view_task(task_number)
            elif choice ==3:
                task_number = int(input("Enter the task number to update:"))
                todo_list.update_task(task_number)
            elif choice ==4:
                task_number = int(input("Enter the task number to delete:"))
                todo_list.delete_task(task_number)
            elif choice ==5:
                confirm = input("Are you sure you want to clear all tasks?(yes/no):").lower()
                if confirm =="yes":
                    todo_list.clear_tasks()
            elif choice ==6:
                print("Exiting To-Do List application. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid operation.")
        except ValueError:
            print("Invalid input. Please enter a number.")
if __name__ == "__main__":
    main()
    
