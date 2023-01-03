from abc import ABC, abstractmethod
from typing import Any


class Service(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def execute(self, data: Any) -> tuple[bool, dict]:
        pass
