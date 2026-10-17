
from student_utils import (
    calculate_completion,
    format_task,
    get_task_priority,
)

print(format_task("Complete DBMS assignment", "DBMS"))
print("Completion:", calculate_completion(3, 5), "%")
print("Priority:", get_task_priority(2))
