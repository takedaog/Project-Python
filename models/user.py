#User, наследует AbstractRole
#система уведомлений (добавить, просмотреть, удалить)

from models.abstract_role import AbstractRole
from datetime import datetime

class User(AbstractRole):
    def __init__(self, _id, full_name, email, password_hash, role):
        super().__init__(_id, full_name, email, password_hash)
        self.role = role  # Student, Teacher, etc.
        self._notifications = []  #{'id': int, 'message': str, 'created_at': str}

    def get_profile(self):
        """Возвращает профиль пользователя"""
        return {
            "id": self._id,
            "name": self._full_name,
            "email": self._email,
            "role": self.role,
            "created_at": self._created_at
        }

    def update_profile(self, full_name=None, email=None):
        """Обновляет имя и/или email"""
        if full_name:
            self._full_name = full_name
        if email:
            self._email = email

    def add_notification(self, message):
        """Добавить уведомление"""
        notification = {
            'id': len(self._notifications) + 1,
            'message': message,
            'created_at': datetime.now().isoformat()
        }
        self._notifications.append(notification)

    def view_notifications(self):
        """Посмотреть все уведомления"""
        return self._notifications

    def delete_notification(self, notification_id):
        """Удалить уведомление по ID"""
        self._notifications = [
            n for n in self._notifications if n['id'] != notification_id
        ]
