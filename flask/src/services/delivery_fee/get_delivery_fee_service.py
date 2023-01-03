from abc import abstractmethod
from src.domain.service import Service
from src.infra.repositories.burguer_schema.delivery_fee.delivery_fee_repository_interface import DeliveryFeeRepositoryInterface

class GetDeliveryFeeServiceInterface(Service):
    @abstractmethod
    def __init__(self, delivery_fee: DeliveryFeeRepositoryInterface) -> None:
        pass

    @abstractmethod
    def execute(self) -> tuple[bool, dict]:
        pass


class GetDeliveryFeeService(GetDeliveryFeeServiceInterface):
    def __init__(self, delivery_fee: DeliveryFeeRepositoryInterface) -> None:
        self.delivery_fee = delivery_fee

    def execute(self) -> tuple[bool, dict]:
        delivery_fee = self.delivery_fee.find()

        if not delivery_fee:
            return (False, "Failed to get delivery fee")

        return (True, delivery_fee)
