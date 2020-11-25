import os
from pathlib import Path

from flask import Flask


BASE_DIR = Path(__file__).parent  # os.path.dirname(os.path.realpath(__file__))


def create_app(config=os.environ["APP_CONFIG"]):
    app = Flask(__name__)
    app.config.from_object(config)

    # ----- Register Blueprints -----
    from rpistatus.main import bp as main_bp
    from rpistatus.hardware import bp as hardware_bp
    from rpistatus.network import bp as network_bp
    from rpistatus.docker import bp as docker_bp

    app.register_blueprint(main_bp, url_prefix="")
    app.register_blueprint(hardware_bp, url_prefix="/hardware")
    app.register_blueprint(network_bp, url_prefix="/network")
    app.register_blueprint(docker_bp, url_prefix="/docker")

    # ----- Register Errors -----

    return app
