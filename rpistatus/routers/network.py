import socket
import subprocess
import json


from fastapi import APIRouter

router = APIRouter(prefix="/network")


@router.get("/")
def network():
    """
    Returns general conglomerated network info.
      - hostname
      - ip
    """
    return ip() | {"hostname": hostname()}


@router.get("/hostname")
def hostname():
    return socket.gethostname()


@router.get("/ip")
def ip():
    """
    Returns the ip addresses of the device.

    Parses `ip addr -j` to get the ip address of each NIC
    """
    j = _get_ip_info()
    ips = [
        {
            "name": nic["ifname"],
            "type": nic["link_type"],
            "addresses": [addr["local"] for addr in nic["addr_info"]],
        }
        for nic in j
    ]
    return {"ips": ips}


def _get_ip_info(obj="addr", flags=("-j",)):
    """
    Calles `ip -j obj` and returns the parsed json response.

    raises `CalledProcessError` for return codes other than 0.
    """
    info = subprocess.run(["ip", *flags, obj], capture_output=True)
    info.check_returncode()

    return json.loads(info.stdout)
