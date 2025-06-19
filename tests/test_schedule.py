import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.schedule import Schedule
from data.database import schedules, id_counters

# Создает новое расписание
schedule = Schedule(
    schedule_id=id_counters["assignment"],
    class_id="9-A",
    day="Monday"
)
id_counters["assignment"] += 1

# Добавляет уроки
schedule.add_lesson("08:00", "Math", teacher_id=10)
schedule.add_lesson("09:00", "History", teacher_id=11)

# Удаляет один
schedule.remove_lesson("10:00")  # должен сказать что такого нет
schedule.remove_lesson("08:00")  # удаляет

# Сохраняет расписание в хранилище
schedules[schedule.class_id] = schedule

# Вывод
print("Расписание для 9-A на Monday:")
for time, lesson in schedule.view_schedule().items():
    print(f"{time}: {lesson['subject']} (Teacher ID: {lesson['teacher_id']})")
