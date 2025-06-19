#Teacher — наследует User, может создавать задания и выставлять оценки

from models.user import User
from models.assignment import Assignment

class Teacher(User):
    def __init__(self, _id, full_name, email, password_hash, subjects, classes):
        super().__init__(_id, full_name, email, password_hash, "Teacher")
        self.subjects = subjects  # напр. ["Math", "Biology"]
        self.classes = classes    # напр. ["8-A", "9-B"]
        self.assignments = {}     # {assignment_id: Assignment объект}

    def create_assignment(self, assignment_id, title, description, deadline, subject, class_id):
        """Создаёт новое задание и добавляет его в список учителя"""
        new_assignment = Assignment(
            assignment_id,
            title,
            description,
            deadline,
            subject,
            self._id,
            class_id
        )
        self.assignments[assignment_id] = new_assignment
        return new_assignment

    def grade_assignment(self, assignment_id, student_id, grade):
        """Выставить оценку студенту за задание"""
        if assignment_id in self.assignments:
            assignment = self.assignments[assignment_id]
            assignment.set_grade(student_id, grade)
        else:
            print(f"[!] Assignment ID {assignment_id} not found.")

    def view_student_progress(self, student):
        """Посмотреть оценки ученика по всем предметам"""
        return student.view_grades()
