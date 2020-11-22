from flask import Blueprint

bp = Blueprint("main", __name__)

from rpistatus.main import routes
