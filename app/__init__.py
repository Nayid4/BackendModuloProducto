from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from app.infrastructure.database import models
        db.create_all()

        from app.interfaces.routes import bp
        app.register_blueprint(bp)

    return app