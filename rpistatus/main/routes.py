import psutil

from rpistatus.main import bp


@bp.route("/")
@bp.route("/index")
def index():
    return "RaspberryPi is Connected and Running.", 200


@bp.route("/ps")
def ps():
    """
    Returns currently running processes
    """
    return {
        p.pid: p.info
        for p in psutil.process_iter(
            ["name", "status", "username", "memory_percent", "cpu_percent"]
        )
    }
