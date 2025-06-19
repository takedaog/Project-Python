#Schedule — хранит уроки на день для конкретного класса

class Schedule:
    def __init__(self, schedule_id, class_id, day):
        self.id = schedule_id
        self.class_id = class_id  # напр. "8-A"
        self.day = day            # напр. "Monday"
        self.lessons = {}         # {time: {"subject": ..., "teacher_id": ...}}

    def add_lesson(self, time, subject, teacher_id):
        """Добавить урок в расписание"""
        if time in self.lessons:
            print(f"[!] В это время уже есть урок.")
        else:
            self.lessons[time] = {"subject": subject, "teacher_id": teacher_id}

    def remove_lesson(self, time):
        """Удалить урок из расписания"""
        if time in self.lessons:
            del self.lessons[time]
        else:
            print(f"[!] На {time} урок не найден.")

    def view_schedule(self):
        """Вернуть текущее расписание"""
        return self.lessons
