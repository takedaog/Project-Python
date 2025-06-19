import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.assignment import Assignment

task = Assignment(101, "Literature Essay", "Write about Shakespeare", "2025-06-21", "Literature", 5, "9-B")

# Ученик сдает задание
task.add_submission(22, "Hamlet is a tragedy about...")
task.set_grade(22, 5)

print("Статус задания:")
print(task.get_status())
