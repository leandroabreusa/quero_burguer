from abc import ABC, abstractmethod
from pymongo import database
from typing import Any


class NoRelationalDatabase(ABC):
    @abstractmethod
    def __init__(self, connection_uri: str):
        pass

    @abstractmethod
    def connect(self) -> database.Database:
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass

    @abstractmethod
    def retry_connection(self) -> None:
        pass

    @abstractmethod
    def insert(self, collection: str, data: dict) -> Any:
        pass

    @abstractmethod
    def insert_specific_database(
        self, database: str, collection: str, data: dict
    ) -> Any:
        pass
    
    @abstractmethod
    def update(self, collection: str, query: dict, new_values: dict) -> Any:
        pass

    @abstractmethod
    def update_specific_database(
        self, database: str, collection: str, query: dict, new_values: dict
    ) -> Any:
        pass

    @abstractmethod
    def find(
        self, collection: str, query: dict
    ) -> Any:
        pass

    @abstractmethod
    def find_specific_database(
        self, database: str, collection: str, query: dict
    ) -> Any:
        pass
