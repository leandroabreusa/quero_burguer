from abc import abstractmethod, ABC
from typing import Union
from src.infra.database.no_relational.no_relational_database import NoRelationalDatabase

class UsersRepositoryInterface(ABC):
    @abstractmethod
    def __init__(self, no_relational_db: NoRelationalDatabase):
        pass

    @abstractmethod
    def insert_error(self, users_data: dict) -> Union[dict, bool]:
        pass