import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.student import Student
from data.database import users, id_counters

new_student = Student(
    _id=id_counters["user"],
    full_name="Ali Valiyev",
    email="ali@edu.uz",
    password_hash="hashed123",
    grade="8-A",
    subjects={"Math": 1, "Biology": 2}
)

users[new_student._id] = new_student
id_counters["user"] += 1

print(f"Foydalanuvchi saqlandi: {new_student.get_profile()}")
