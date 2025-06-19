import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.student import Student
from models.grade_model import Grade
from data.database import users, id_counters

# Создание ученика
student = Student(
    _id=id_counters["user"],
    full_name="Malika Karimova",
    email="malika@edu.uz",
    password_hash="hash456",
    grade="9-A",
    subjects={"Math": 1}
)
users[student._id] = student
id_counters["user"] += 1

# Добавляет оценки
grade1 = Grade(1, student_id=student._id, subject="Math", value=5, teacher_id=10)
grade2 = Grade(2, student_id=student._id, subject="Math", value=4, teacher_id=10)

# Сохраняет как значения
student.grades = {"Math": [grade1.value, grade2.value]}

# Тест
student.submit_assignment(101, "My solution")
print("Grades:", student.view_grades("Math"))
print("Average grade:", student.calculate_average_grade())
