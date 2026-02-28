from datetime import datetime

def validate_task_title(title):
    if not title:
        raise ValueError ("Title cannot be empty.")
    
def validate_task_description(description):
    if not description:
        raise ValueError ("Description cannot be empty.")   
    
def validate_due_date(due_date):
    if not due_date:
        raise ValueError ("Due date cannot be empty.")