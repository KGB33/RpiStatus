from socket import gethostname

from rpistatus.main import bp


@bp.route("/")
@bp.route("/index")
def index():
    return "RaspberryPi is Connected and Running.", 200


@bp.route("/hostname")
def hostname():
    return gethostname()
