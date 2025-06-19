#Assignment — учебное задание, связанное с учителем, классом и предметом

from datetime import datetime

class Assignment:
    def __init__(self, assignment_id, title, description, deadline, subject, teacher_id, class_id):
        self.id = assignment_id
        self.title = title
        self.description = description
        self.deadline = deadline  # строка: "2025-06-20"
        self.subject = subject
        self.teacher_id = teacher_id
        self.class_id = class_id
        self.submissions = {}  # {student_id: content}
        self.grades = {}       # {student_id: grade}

    def add_submission(self, student_id, content):
        """Добавляет ответ ученика"""
        self.submissions[student_id] = content

    def set_grade(self, student_id, grade):
        """Ставит оценку за задание"""
        if student_id in self.submissions:
            self.grades[student_id] = grade
        else:
            print(f"[!] Student {student_id} has not submitted this assignment.")

    def get_status(self):
        """Возвращает текущую статистику выполнения"""
        return {
            "submitted_count": len(self.submissions),
            "graded_count": len(self.grades),
            "ungraded_students": list(set(self.submissions) - set(self.grades))
        }
