
def calculate_completion(completed, total):
    """Calculate the task completion percentage."""
    if total <= 0:
        return 0

    if completed < 0 or completed > total:
        raise ValueError("Invalid task count")

    return round((completed / total) * 100, 2)


def format_task(title, subject):
    """Format a task description."""
    return f"{title.strip()} - Subject: {subject.strip()}"


def get_task_priority(due_in_days):
    """Return a priority label based on the due date."""
    if due_in_days < 0:
        return "Overdue"
    elif due_in_days <= 2:
        return "High"
    elif due_in_days <= 7:
        return "Medium"
    else:
        return "Low"
