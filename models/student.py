# Student: наследует User и реализует методы для сдачи заданий и просмотра оценок

from models.user import User

class Student(User):
    def __init__(self, _id, full_name, email, password_hash, grade, subjects):
        super().__init__(_id, full_name, email, password_hash, "Student")
        self.grade = grade  # напр. "9-A"
        self.subjects = subjects  # напр. {"Math": 2, "History": 3}
        self.assignments = {}  # {assignment_id: "submitted" или "pending"}
        self.grades = {}  # {"Math": [4, 5], "History": [3]}

    def submit_assignment(self, assignment_id, content):
        """Отправить задание"""
        # Простой пример: как "submitted"
        self.assignments[assignment_id] = {
            "status": "submitted",
            "content": content
        }

    def view_grades(self, subject=None):
        """Посмотреть оценки (все или по конкретному предмету)"""
        if subject:
            return self.grades.get(subject, [])
        return self.grades

    def calculate_average_grade(self):
        """Рассчитать среднюю оценку по всем предметам"""
        total = 0
        count = 0
        for marks in self.grades.values():
            total += sum(marks)
            count += len(marks)
        return round(total / count, 2) if count > 0 else None
