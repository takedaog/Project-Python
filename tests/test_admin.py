import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.admin_user import Admin
from models.teacher import Teacher
from data.database import users, id_counters

admin = Admin(
    _id=id_counters["user"],
    full_name="Sardor Abdullaev",
    email="sardor@edu.uz",
    password_hash="adminpass"
)
users[admin._id] = admin
id_counters["user"] += 1

# Добавление учителя
teacher = Teacher(
    _id=id_counters["user"],
    full_name="Javlon Akhmedov",
    email="javlon@edu.uz",
    password_hash="teachpass",
    subjects=["Physics"],
    classes=["9-A"]
)
id_counters["user"] += 1

admin.add_user(teacher)

print("Foydalanuvchilar ro'yxati:")
print(admin.generate_report())

admin.remove_user(teacher._id)

print("O'chirgandan keyin:")
print(admin.generate_report())
