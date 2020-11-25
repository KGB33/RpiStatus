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
    Note: Use `df -B1` to get bytes.

    Returns a Json list of `disk` objects, each disk object has
        Filesystem:   string
        Size:         int (bytes)
        Used:         int (bytes)
        Avalable:     int (bytes)
        Capacity:     int (0 - 100)
        MountedOn:    string

    Each response will have at least one disk object
    """
