from notes.main import bp


@bp.route("/")
@bp.route("/index")
def index():
    return "RaspberryPi is Connected and Running.", 200
