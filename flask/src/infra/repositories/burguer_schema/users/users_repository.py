from typing import Union
from src.infra.database.no_relational.no_relational_database import NoRelationalDatabase
from src.infra.repositories.burguer_schema.users.users_repository_interface import (
    UsersRepositoryInterface,
)
import os
import datetime

class UsersRepository(UsersRepositoryInterface):
    def __init__(
        self,
        no_relational_db: NoRelationalDatabase
    ):
        self.no_relational_db = no_relational_db
        self.collection = "users"

    def insert_error(self, users_data: dict) -> Union[dict, bool]:
        user = self.no_relational_db.find(self.collection, {"relational_db_id": users_data["relational_db_id"]})

        if user:
            error_number = len(user["email_errors"]) + 1

            error_update = users_data["email_errors"][0]

            error_update["error_number"] = error_number
            error_update["created_at"] = datetime.datetime.utcnow()
            error_update["updated_at"] = datetime.datetime.utcnow().timestamp()

            return self.no_relational_db.update(
                self.collection, 
                {"relational_db_id": users_data["relational_db_id"]},
                { 
                    "$set": { 
                        f"email_errors.{error_number-1}.error_number": error_update["error_number"],
                        f"email_errors.{error_number-1}.error_type": error_update["error_type"],
                        f"email_errors.{error_number-1}.error_at": error_update["error_at"],
                        f"email_errors.{error_number-1}.status_code": error_update["status_code"],
                        f"email_errors.{error_number-1}.reason": error_update["reason"],
                        f"email_errors.{error_number-1}.created_at": error_update["created_at"],
                        f"email_errors.{error_number-1}.updated_at": error_update["updated_at"],
                        f"email_errors.{error_number-1}.email": error_update["email"],
                     }  
                }
            )
        else:
            email_errors = []

            error_update = users_data["email_errors"][0]

            error_update["error_number"] = 1
            error_update["created_at"] = datetime.datetime.utcnow()
            error_update["updated_at"] = datetime.datetime.utcnow().timestamp()

            email_errors.append(error_update)

            user = {
                "relational_db_id": users_data['relational_db_id'],
                "uuid": users_data['uuid'],
                "email_errors": email_errors
            }

            return self.no_relational_db.insert(
                self.collection,
                user
            )
