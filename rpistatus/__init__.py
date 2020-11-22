import os
from pathlib import Path

from flask import Flask


BASE_DIR = Path(__file__).parent  # os.path.dirname(os.path.realpath(__file__))


def create_app(config=os.environ["APP_CONFIG"]):
    app = Flask(__name__)
    app.config.from_object(config)

    # ----- Register Blueprints -----
    from rpistatus.main import bp as main_bp

    app.register_blueprint(main_bp, url_prefix="")

    # ----- Register Errors -----

    return app
