from socket import gethostname


from rpistatus.network import bp


@bp.route("/")
def network():
    """
    Returns general conglomerated network info.
      - hostname
      - ip
    """


@bp.route("/hostname")
def hostname():
    return gethostname()


@bp.route("/ip")
def ip():
    """
    Returns the internal IP of the device.
    """
