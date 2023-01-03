def execute(app):
    from src.main.routes.routes import routes_blueprint

    app.register_blueprint(routes_blueprint)
