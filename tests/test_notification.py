import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.notification import Notification
from data.database import notifications

# Создает уведомление
notif = Notification(
    notif_id=1,
    message="Sizga yangi baho qo‘yildi",
    recipient_id=22,
    priority="important"
)

# Отправляет
notif_data = notif.send()
notifications.append(notif_data)

# Показывает отправленное уведомление
print("Uvedomlenie:", notif_data)

# Отмечает как прочитанное
notif.mark_as_read()
print("Status (после mark_as_read):", notif.is_read)
