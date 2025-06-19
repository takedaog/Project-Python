# Симулирует базу данных с использованием словарей и списков

# Users: ключ - ID, значение - экземпляр User или подкласса (Student, Teacher, и т.п.)
users = {}

# Assignments: ключ - ID, значение - объект Assignment
assignments = {}

# Grades: список объектов Grade
grades = []

# Notifications: список словарей
notifications = []

# Schedules: ключ - class_id, значение - список расписаний
schedules = {}

# ID-счетчики (для генерации уникальных ID вручную)
id_counters = {
    "user": 1,
    "assignment": 1,
    "grade": 1,
    "notification": 1
}
