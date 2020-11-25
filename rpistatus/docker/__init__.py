from flask import Blueprint

bp = Blueprint("docker", __name__)

from rpistatus.docker import routes
