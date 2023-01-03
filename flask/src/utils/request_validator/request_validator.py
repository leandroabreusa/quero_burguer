from typing import Union
from marshmallow import Schema
from src.utils.request_validator.request_validator_interface import (
    RequestValidatorInterface,
)


class RequestValidator(RequestValidatorInterface):
    def __init__(self, schema_instance: Schema):
        self.schema_instance = schema_instance

    def validate(self, request_params: dict) -> tuple[bool, Union[dict, str]]:
        try:
            return (True, self.schema_instance.load(request_params))

        except Exception as error:
            print(error)
            # return (False, str(error))
            return (False, eval(str(error)))
