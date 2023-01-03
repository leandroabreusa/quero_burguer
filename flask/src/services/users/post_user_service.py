from abc import abstractmethod
from src.domain.service import Service
from src.infra.repositories.burguer_schema.users.users_repository_interface import UsersRepositoryInterface

class PostUserData:
    pass


class PostUserServiceInterface(Service):
    @abstractmethod
    def __init__(self, user: UsersRepositoryInterface) -> None:
        pass

    @abstractmethod
    def execute(self, user: PostUserData) -> tuple[bool, dict]:
        pass


class PostUserService(PostUserServiceInterface):
    def __init__(self, user: UsersRepositoryInterface) -> None:
        self.user = user

    def execute(self, user_data: PostUserData) -> tuple[bool, dict]:
        post_user = self.user.insert_error(user_data)

        if not post_user:
            return (False, "Failed to post user")

        return (True, post_user)
