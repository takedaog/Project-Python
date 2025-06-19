#Grade — представляет одну оценку ученика по предм ету

from datetime import datetime

class Grade:
    def __init__(self, grade_id, student_id, subject, value, teacher_id, comment=""):
        self.id = grade_id
        self.student_id = student_id
        self.subject = subject
        self.value = value  # например, 5
        self.date = datetime.now().isoformat()
        self.teacher_id = teacher_id
        self.comment = comment

    def update_grade(self, new_value, new_comment=None):
        """Обновляет значение оценки и/или комментарий"""
        self.value = new_value
        if new_comment is not None:
            self.comment = new_comment
        self.date = datetime.now().isoformat()

    def get_grade_info(self):
        """Возвращает словарь с полной информацией об оценке"""
        return {
            "id": self.id,
            "student_id": self.student_id,
            "subject": self.subject,
            "value": self.value,
            "date": self.date,
            "teacher_id": self.teacher_id,
            "comment": self.comment
        }
