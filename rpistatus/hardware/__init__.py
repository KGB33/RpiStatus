from flask import Blueprint

bp = Blueprint("hardware", __name__)

from rpistatus.hardware import routes
