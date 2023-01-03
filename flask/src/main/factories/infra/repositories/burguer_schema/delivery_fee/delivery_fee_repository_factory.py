from src.infra.repositories.burguer_schema.delivery_fee.delivery_fee_repository_interface import ( DeliveryFeeRepositoryInterface )
from src.infra.repositories.burguer_schema.delivery_fee.delivery_fee_repository import ( DeliveryFeeRepository )
from src.infra.database.no_relational.no_relational_instance import mongo_instance

def make() -> DeliveryFeeRepositoryInterface:
    return DeliveryFeeRepository(no_relational_db=mongo_instance.mongo)