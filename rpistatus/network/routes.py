import socket
import subprocess
import json


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
    return socket.gethostname()


@bp.route("/ip")
def ip():
    """
    Returns the ip addresses of the device.

    Using `ip -j addr` returns a Json verson of response
    """
    ips = _get_ip_info(flags=("-j", "-brief",))
    return {"interfaces": ips}

def _get_ip_info(obj="addr", flags=("-j", )):
    """
    Calles `ip -j obj` and returns the parsed json response.

    raises `CalledProcessError` for return codes other than 0.
    """
    info = subprocess.run(["ip", *flags, obj], capture_output=True)
    info.check_returncode()

    return json.loads(info.stdout)

