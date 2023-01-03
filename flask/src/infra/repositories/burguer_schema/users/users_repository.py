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
        user = self.no_relational_db.find_specific_database(str(os.environ.get("MONGO_DATABASE")), self.collection, {"relational_db_id": users_data["relational_db_id"]})

        if user:
            user = user[0]

            error_number = len(user["email_errors"]) + 1

            users_data["email_error"]["error_number"] = error_number
            users_data["email_error"]["created_at"] = datetime.datetime.utcnow()
            users_data["email_error"]["updated_at"] = datetime.datetime.utcnow()

            user["email_errors"].append(users_data["email_error"])

            return self.no_relational_db.update_specific_database(
                str(os.environ.get("MONGO_DATABASE")), 
                self.collection, 
                { {"relational_db_id": users_data["relational_db_id"]} },
                { 
                    "$set": { "email_errors": user["email_errors"] }  
                }
            )
        else:
            email_errors = []

            users_data["email_error"]["error_number"] = 1
            users_data["email_error"]["created_at"] = datetime.datetime.utcnow()
            users_data["email_error"]["updated_at"] = datetime.datetime.utcnow()

            email_errors.append(users_data["email_error"])

            user = {
                "relational_db_id":{"$numberInt":f"{users_data['relational_db_id']}"},
                "uuid":f"{users_data['uuid']}",
                "email_errors": email_errors
            }

            return self.no_relational_db.insert_specific_database(
                str(os.environ.get("MONGO_DATABASE")),
                self.collection,
                user
            )
