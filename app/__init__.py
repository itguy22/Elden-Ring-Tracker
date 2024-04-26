from flask import Flask
from .routes import main  # Corrected from 'zone_blueprint' to 'main'

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)  # Register 'main', not 'zone_blueprint'
    return app
