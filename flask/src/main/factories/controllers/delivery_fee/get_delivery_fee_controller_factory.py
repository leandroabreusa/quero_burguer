from src.presentation.controllers.delivery_fee.get_delivery_fee_controller import (
    GetDeliveryFeeController,
)
from src.domain.controller import Controller
from src.main.factories.http import http_responses_factory
from src.main.factories.services.delivery_fee import (
    get_delivery_fee_service_factory,
)


def make() -> Controller:
    return GetDeliveryFeeController(
        http_responses=http_responses_factory.make(),
        get_delivery_fee_service=get_delivery_fee_service_factory.make(),
    )
