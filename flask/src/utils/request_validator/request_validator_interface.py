from abc import ABC, abstractmethod
from typing import Union
from marshmallow import Schema


class RequestValidatorInterface(ABC):
    @abstractmethod
    def __init__(self, schema_instance: Schema):
        pass

    @abstractmethod
    def validate(self, request_params: dict) -> tuple[bool, Union[dict, str]]:
        pass
