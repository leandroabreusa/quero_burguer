from flask import Blueprint, request
from src.main.factories.controllers.delivery_fee import (
    get_delivery_fee_controller_factory,
    update_delivery_fee_controller_factory,
)

delivery_fee_routes = Blueprint("delivery_fee_routes", __name__)


@delivery_fee_routes.route("/", methods=["GET"])
def get():
    get_delivery_fee_controller = get_delivery_fee_controller_factory.make()

    return get_delivery_fee_controller.handle(request)


@delivery_fee_routes.route("/", methods=["PUT"])
def update():
    update_delivery_fee_controller = (
        update_delivery_fee_controller_factory.make()
    )

    return update_delivery_fee_controller.handle(request)
