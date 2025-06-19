#Notification — структура одного уведомления

from datetime import datetime

class Notification:
    def __init__(self, notif_id, message, recipient_id, priority="normal"):
        self.id = notif_id
        self.message = message
        self.recipient_id = recipient_id
        self.created_at = datetime.now().isoformat()
        self.is_read = False
        self.priority = priority  # напр. "normal", "important"

    def send(self):
        """Возвращает структуру уведомления (для добавления получателю)"""
        return {
            "id": self.id,
            "message": self.message,
            "recipient_id": self.recipient_id,
            "created_at": self.created_at,
            "is_read": self.is_read,
            "priority": self.priority
        }

    def mark_as_read(self):
        """Отметить уведомление как прочитанное"""
        self.is_read = True
