from flask import Flask
from flask_cors import CORS
from blueprints import (
    users
)


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = 'jashshshsdjfhsf_jsd455asdsKsks'
    CORS(app)
    app.register_blueprint(users.bp)
    

    return app
