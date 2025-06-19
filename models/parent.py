#Parent — наследует User, связывается с детьми и следит за их учебным процессом

from models.user import User
from data.database import users  # используется для доступа к объектам детей по их ID

class Parent(User):
    def __init__(self, _id, full_name, email, password_hash, children_ids):
        super().__init__(_id, full_name, email, password_hash, "Parent")
        self.children = children_ids  # список ID детей (учеников)

    def view_child_grades(self, child_id):
        """Возвращает оценки ребёнка"""
        child = users.get(child_id)
        if child and child.role == "Student":
            return child.view_grades()
        return f"[!] Student with ID {child_id} not found."

    def view_child_assignments(self, child_id):
        """Возвращает список заданий ребёнка"""
        child = users.get(child_id)
        if child and child.role == "Student":
            return child.assignments
        return f"[!] Student with ID {child_id} not found."

    def receive_child_notification(self, child_id):
        """Получить все уведомления, относящиеся к ребёнку"""
        child = users.get(child_id)
        if child and child.role == "Student":
            return child.view_notifications()
        return f"[!] Student with ID {child_id} not found."
