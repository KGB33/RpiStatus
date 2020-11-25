from rpistatus.hardware import bp


@bp.route("/")
def hardware():
    """
    Returns conglomerated hardware stats
    """


@bp.route("/temps")
def temps():
    """
    Returns core temps
    """


@bp.route("/cores")
def cores():
    """
    Returns Core utilization
    """


@bp.route("/df")
def diskfree():
    """
    returns free space on disk
    """
