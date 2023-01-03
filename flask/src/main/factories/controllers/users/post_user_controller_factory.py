from src.presentation.controllers.users.post_user_controller import (
    PostUserController,
)
from src.domain.controller import Controller
from src.main.factories.http import http_responses_factory
from src.main.factories.services.users import (
    post_user_service_factory,
)
from src.utils.request_validator.request_validator import RequestValidator
from src.presentation.request_schemas.users.post_user_schema import (
    PostUserSchema,
)


def make() -> Controller:
    return PostUserController(
        http_responses=http_responses_factory.make(),
        request_validator=RequestValidator(PostUserSchema()),
        post_user_service=post_user_service_factory.make(),
    )
