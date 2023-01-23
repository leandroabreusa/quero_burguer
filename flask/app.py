from flask import Flask
from flask_cors import CORS
from src.main import register_routes

# Flask inicialization
app = Flask(__name__)

# Basic configuration for flask_limiter library
# limiter_instance.create(app)

CORS(app)

# Register the main route blueprint
register_routes.execute(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(5000))
