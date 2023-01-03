from src.infra.repositories.burguer_schema.users.users_repository_interface import ( UsersRepositoryInterface )
from src.infra.repositories.burguer_schema.users.users_repository import ( UsersRepository )
from src.infra.database.no_relational.no_relational_instance import mongo_instance

def make() -> UsersRepositoryInterface:
    return UsersRepository(no_relational_db=mongo_instance.mongo)