from datetime import datetime

# Import validation functions
from validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False # set initial value to false (can't add a completed task)
    }

    tasks.append(task)
    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        print ("Invalid task index.")
        return
    
    tasks[index]["completed"] = True
    print("Task marked as complete!")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    if len(tasks)==0:
        print("No tasks available")

    found = False # Set it to false at first

    for i in range(len(tasks)): # loop through the number of tasks
        if tasks[i]["completed"] == False: # checks if complete value for the task at that index is false
            print("\nTask:", i)
            print("Title:", tasks[i]["title"])
            print("Description:", tasks[i]["description"])
            print("Due Date:", tasks[i]["due_date"])
            found = True
    
    if not found:
        print("No pending tasks.")


# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        return 0
    # get total tasks using len()
    total_tasks = len(tasks)
    completed_tasks = 0

    for task in tasks:
        if task["completed"]:
            completed_tasks += 1
    
    # calculate progress as a percentage
    progress = (completed_tasks/total_tasks) * 100
    
    return progress