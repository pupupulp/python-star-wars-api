from flask import Flask
from flask_alembic import Alembic

from python_star_wars_api.models import db
from python_star_wars_api.apis import api_v1


def create_app():
    app = Flask(__name__)
    app.config.from_object('python_star_wars_api.config.settings')

    db.init_app(app)
    api_v1.init_app(app)
    Alembic(app)

    return app
