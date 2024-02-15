class TaskForm:
    def __init__(self):
        self.task_name = input("Enter Task Name: ")
        self.task_description = input("Enter Task Description: ")

    def display(self):
        print("\nTask Information:")
        print(f"Task Name: {self.task_name}")
        print(f"Task Description: {self.task_description}")