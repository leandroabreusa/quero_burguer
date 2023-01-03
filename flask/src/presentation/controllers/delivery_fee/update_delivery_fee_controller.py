from src.domain.controller import Controller
from flask import Request, Response
from src.main.http.http_responses import HttpResponsesInterface
from src.services.delivery_fee.update_delivery_fee_service import (
    UpdateDeliveryFeeServiceInterface,
)
from src.utils.request_validator.request_validator_interface import (
    RequestValidatorInterface,
)
import json


class UpdateDeliveryFeeController(Controller):
    def __init__(
        self,
        http_responses: HttpResponsesInterface,
        request_validator: RequestValidatorInterface,
        update_delivery_fee_service: UpdateDeliveryFeeServiceInterface,
    ) -> None:
        self.http_responses = http_responses
        self.request_validator = request_validator
        self.update_delivery_fee_service = update_delivery_fee_service

    def handle(self, request: Request) -> Response:
        try:
            data = json.loads(request.get_data())

            (validate_resp, data) = self.request_validator.validate(data)
            if not validate_resp:
                return self.http_responses.bad_request(
                    {"error": "Invalid/Missing params", "message": data}
                )

            if not data:
                return self.http_responses.bad_request("Nothing to update")

            (status, delivery_fee) = self.update_delivery_fee_service.execute(data)

            if not status:
                return self.http_responses.bad_request({})

            return self.http_responses.success_request({})

        except Exception as error:
            return self.http_responses.server_error(error)
