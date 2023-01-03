from src.domain.controller import Controller
from flask import Request, Response
from src.main.http.http_responses import HttpResponsesInterface
from src.services.delivery_fee.get_delivery_fee_service import (
    GetDeliveryFeeServiceInterface,
)


class GetDeliveryFeeController(Controller):
    def __init__(
        self,
        http_responses: HttpResponsesInterface,
        get_delivery_fee_service: GetDeliveryFeeServiceInterface,
    ) -> None:
        self.http_responses = http_responses
        self.get_delivery_fee_service = get_delivery_fee_service

    def handle(self, request: Request) -> Response:
        try:
            (status, delivery_fee) = self.get_delivery_fee_service.execute()

            if not status:
                return self.http_responses.bad_request(delivery_fee)

            delivery_fee = { "value": float(str(delivery_fee["value"])) }

            return self.http_responses.success_request(delivery_fee)

        except Exception as error:
            return self.http_responses.server_error(error)
