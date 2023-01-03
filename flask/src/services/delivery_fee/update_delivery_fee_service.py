from abc import abstractmethod
from typing import TypedDict
from src.domain.service import Service
from src.infra.repositories.burguer_schema.delivery_fee.delivery_fee_repository_interface import DeliveryFeeRepositoryInterface


class UpdateDeliveryFeeData(TypedDict):
    pass


class UpdateDeliveryFeeServiceInterface(Service):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def execute(
        self, data: UpdateDeliveryFeeData
    ) -> tuple[bool, dict]:
        pass


class UpdateDeliveryFeeService(UpdateDeliveryFeeServiceInterface):
    def __init__(self, delivery_fee: DeliveryFeeRepositoryInterface) -> None:
        self.delivery_fee = delivery_fee

    def execute(
        self, data: UpdateDeliveryFeeData
    ) -> tuple[bool, dict]:
        update_resp = self.delivery_fee.update(data["value"])

        if not update_resp:
            return (False, "Failed to update delivery fee")

        return (True, update_resp)
