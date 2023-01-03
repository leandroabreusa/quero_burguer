from flask import Blueprint
from src.infra.database.no_relational.no_relational_instance import mongo_instance
from src.main.routes.delivery_fee.delivery_fee_routes import delivery_fee_routes
from src.main.routes.users.users_routes import users_routes

# Main blueprint creation
routes_blueprint = Blueprint("routes_blueprint", __name__)

routes_blueprint.register_blueprint(
    delivery_fee_routes, url_prefix="/delivery_fee"
)

routes_blueprint.register_blueprint(
    users_routes, url_prefix="/users"
)

@routes_blueprint.before_request
def before_request():
    mongo_instance.connect()


@routes_blueprint.after_request
def after_request(response):
    mongo_instance.close()
    return response
