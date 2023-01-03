from src.services.delivery_fee.update_delivery_fee_service import (
    UpdateDeliveryFeeServiceInterface,
    UpdateDeliveryFeeService,
)
from src.main.factories.infra.repositories.burguer_schema.delivery_fee import delivery_fee_repository_factory


def make() -> UpdateDeliveryFeeServiceInterface:
    return UpdateDeliveryFeeService(delivery_fee=delivery_fee_repository_factory.make())
