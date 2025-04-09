# app.py
from flask import Flask
from flask_cors import CORS
from extensions import db, migrate
from models.models import Appearance, Guest, Episode

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register your routes here if any

    return app
