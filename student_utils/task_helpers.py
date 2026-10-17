
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
