from flask import Flask
from flask_cors import CORS
from src.main import register_routes
from gevent.pywsgi import WSGIServer

# Flask inicialization
app = Flask(__name__)

# Basic configuration for flask_limiter library
# limiter_instance.create(app)

# Load the main config file
app.config.from_pyfile("src/main/config.py")

CORS(app)

# Register the main route blueprint
register_routes.execute(app)

http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()
