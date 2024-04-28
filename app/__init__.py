from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
load_dotenv()


db = SQLAlchemy()
migrate = None  # Declare migrate variable

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eldenring.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    global migrate
    migrate = Migrate(app, db)  # Initialize Migrate here

    from .routes import main  # Import routes or other blueprints here to avoid circular imports
    app.register_blueprint(main)

    from . import models  # Ensure models are loaded and associated with db

    return app
