#Admin — наследует User, может добавлять и удалять пользователей, а также создавать отчёты

from models.user import User
from data.database import users

class Admin(User):
    def __init__(self, _id, full_name, email, password_hash, permissions=None):
        super().__init__(_id, full_name, email, password_hash, "Admin")
        self.permissions = permissions if permissions else ["add_user", "remove_user", "generate_report"]

    def add_user(self, user):
        """Добавляет нового пользователя в систему"""
        users[user._id] = user

    def remove_user(self, user_id):
        """Удаляет пользователя по ID"""
        if user_id in users:
            del users[user_id]
        else:
            print(f"[!] User with ID {user_id} not found.")

    def generate_report(self):
        """Простой текстовый отчёт по всем пользователям"""
        report = []
        for user in users.values():
            profile = user.get_profile()
            report.append(f"{profile['id']} - {profile['name']} ({profile['role']})")
        return "\n".join(report)
