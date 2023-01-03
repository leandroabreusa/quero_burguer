from abc import ABC, abstractmethod
from flask import Request, Response


class Controller(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def handle(self, request: Request) -> Response:
        pass
