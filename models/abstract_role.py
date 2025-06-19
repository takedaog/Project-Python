#класс, от которого наследуются все роли

from abc import ABC, abstractmethod
import datetime

class AbstractRole(ABC):
    def __init__(self, _id, full_name, email, password_hash):
        self._id = _id
        self._full_name = full_name
        self._email = email
        self._password_hash = password_hash
        self._created_at = datetime.datetime.now().isoformat()

    @abstractmethod
    def get_profile(self):
        pass

    @abstractmethod
    def update_profile(self, full_name=None, email=None):
        pass
