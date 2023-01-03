from src.services.delivery_fee.get_delivery_fee_service import (
    GetDeliveryFeeService,
    GetDeliveryFeeServiceInterface,
)
from src.main.factories.infra.repositories.burguer_schema.delivery_fee import delivery_fee_repository_factory

def make() -> GetDeliveryFeeServiceInterface:
    return GetDeliveryFeeService(delivery_fee=delivery_fee_repository_factory.make())
