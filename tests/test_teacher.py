import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.teacher import Teacher
from models.assignment import Assignment
from data.database import users, assignments, id_counters

# Создает учителя
teacher = Teacher(
    _id=id_counters["user"],
    full_name="Shavkat Oqilov",
    email="shavkat@edu.uz",
    password_hash="tchr123",
    subjects=["Algebra"],
    classes=["9-B"]
)
users[teacher._id] = teacher
id_counters["user"] += 1

# Учитель создает задание
assignment = teacher.create_assignment(
    assignment_id=id_counters["assignment"],
    title="Kvadrat tenglamalar",
    description="Yechimni toping",
    deadline="2025-06-22",
    subject="Algebra",
    class_id="9-B"
)
assignments[assignment.id] = assignment
id_counters["assignment"] += 1

# Ставит оценку (вручную указываем student_id)
teacher.grade_assignment(assignment.id, student_id=2, grade=5)

# Выводит информацию
print("Assignments:", teacher.assignments)
print("Grades for assignment:", teacher.assignments[assignment.id].grades)
