from rpistatus.docker import bp


@bp.route("/")
def docker():
    """
    "general docker info", whatever that means.
    """


@bp.route("/ps")
def ps():
    """
    Returns running docker containers
    """


@bp.route("/logs/<container_name>")
def logs(container_name):
    """
    Returns the logs for the provided container.
    """
