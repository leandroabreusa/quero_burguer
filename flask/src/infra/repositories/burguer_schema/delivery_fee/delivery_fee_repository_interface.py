from abc import abstractmethod, ABC
from typing import Union
from src.infra.database.no_relational.no_relational_database import NoRelationalDatabase

class DeliveryFeeRepositoryInterface(ABC):
    @abstractmethod
    def __init__(self, no_relational_db: NoRelationalDatabase):
        pass

    @abstractmethod
    def update(self, value: float) -> Union[dict, bool]:
        pass

    @abstractmethod
    def find(self) -> Union[dict, bool]:
        pass