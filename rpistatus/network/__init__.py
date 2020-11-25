from flask import Blueprint

bp = Blueprint("network", __name__)

from rpistatus.network import routes
