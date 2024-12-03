from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.connection import db_connection_handler
from src.main.routes.pf_routes import pf_route_bp
from src.main.routes.pj_routes import pj_routes_bp

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(pf_route_bp)
app.register_blueprint(pj_routes_bp)
