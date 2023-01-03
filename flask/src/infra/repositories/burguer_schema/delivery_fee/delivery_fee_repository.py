from typing import Union
from src.infra.database.no_relational.no_relational_database import NoRelationalDatabase
from src.infra.repositories.burguer_schema.delivery_fee.delivery_fee_repository_interface import (
    DeliveryFeeRepositoryInterface,
)
import datetime
import os
from dotenv import load_dotenv
from bson import Decimal128


class DeliveryFeeRepository(DeliveryFeeRepositoryInterface):
    def __init__(self, no_relational_db: NoRelationalDatabase):
        self.no_relational_db = no_relational_db
        self.collection = "delivery_fee"

    def update(self, value: float) -> Union[dict, bool]:
        date = datetime.datetime.utcnow()

        return self.no_relational_db.update(
            self.collection, 
            { "selected_fee": 1 },
            { 
                "$set": { "value": Decimal128(str(value)) },
                "$setOnInsert": { "fee_at": date }  
            }
        )

    def find(self) -> Union[dict, bool]:
        return self.no_relational_db.find(
            self.collection,
            { "selected_fee": 1 }
        )
