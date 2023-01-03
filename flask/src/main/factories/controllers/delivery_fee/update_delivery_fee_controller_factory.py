from src.presentation.controllers.delivery_fee.update_delivery_fee_controller import (
    UpdateDeliveryFeeController,
)
from src.domain.controller import Controller
from src.main.factories.http import http_responses_factory
from src.main.factories.services.delivery_fee import (
    update_delivery_fee_service_factory,
)
from src.utils.request_validator.request_validator import RequestValidator
from src.presentation.request_schemas.delivery_fee.update_delivery_fee_schema import (
    UpdateDeliveryFeeSchema,
)


def make() -> Controller:
    return UpdateDeliveryFeeController(
        http_responses=http_responses_factory.make(),
        request_validator=RequestValidator(UpdateDeliveryFeeSchema()),
        update_delivery_fee_service=update_delivery_fee_service_factory.make(),
    )
