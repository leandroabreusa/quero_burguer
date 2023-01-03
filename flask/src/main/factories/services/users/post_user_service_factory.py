from src.services.users.post_user_service import (
    PostUserServiceInterface,
    PostUserService,
)
from src.main.factories.infra.repositories.burguer_schema.users import users_repository_factory


def make() -> PostUserServiceInterface:
    return PostUserService(user=users_repository_factory.make())
