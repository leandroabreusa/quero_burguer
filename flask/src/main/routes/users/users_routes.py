from flask import Blueprint, request
from src.main.factories.controllers.users import (
    post_user_controller_factory,
)

users_routes = Blueprint("users_routes", __name__)

@users_routes.route("/", methods=["POST"])
def insert():
    post_user_controller = (
        post_user_controller_factory.make()
    )

    return post_user_controller.handle(request)
