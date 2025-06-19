import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.student import Student
from models.parent import Parent
from data.database import users, id_counters

# Создает ученика
student = Student(
    _id=id_counters["user"],
    full_name="Aziza Qodirova",
    email="aziza@edu.uz",
    password_hash="hash123",
    grade="8-A",
    subjects={"Math": 1}
)
users[student._id] = student
id_counters["user"] += 1

# Добавляет уведомление ученику
student.add_notification("Bugun uyga vazifa yuklandi")

# Создает родителя
parent = Parent(
    _id=id_counters["user"],
    full_name="Dildora Qodirova",
    email="dildora@edu.uz",
    password_hash="hash456",
    children_ids=[student._id]
)
users[parent._id] = parent
id_counters["user"] += 1

# Родитель проверяет оценки, задания и уведомления
print("Baholar:", parent.view_child_grades(student._id))
print("Topshiriqlar:", parent.view_child_assignments(student._id))
print("Xabarnomalar:", parent.receive_child_notification(student._id))
