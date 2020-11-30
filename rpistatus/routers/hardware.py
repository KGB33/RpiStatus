import psutil

from fastapi import APIRouter

router = APIRouter(prefix="/hardware")


@router.get("/")
def hardware():
    """
    Returns conglomerated hardware stats
    """
    return temps() | cores() | diskfree()


@router.get("/temps")
def temps():
    """
    Returns temps
    """
    return {
        "temps": {
            key: [item._asdict() for item in val]
            for key, val in psutil.sensors_temperatures().items()
        }
    }


@router.get("/cores")
def cores():
    """
    Returns Core utilization,
    blocks for 1 second

    Format:
        { "cores": [{
            "guest":      int,
            "guest_nice": int,
            "idle":       int,
            "iowait":     int,
            "irq":        int,
            "nice":       int,
            "softirq":    int,
            "steal":      int,
            "system":     int,
            "user":       int
            },
            ...
            ]}
    """
    return {
        "cores": [
            core._asdict() for core in psutil.cpu_times_percent(interval=1, percpu=True)
        ]
    }


@router.get("/df")
def diskfree(_all=False):
    """
    Returns disk useage info for each partition.

    If all is False, it returns info for physical partions only

    TODO: set _all to be a queriy paramater
    """
    result = []
    for part in psutil.disk_partitions(all=_all):
        usage = psutil.disk_usage(part.mountpoint)
        result.append(
            {
                "device": part.device,
                "total": usage.total,
                "used": usage.used,
                "free": usage.free,
                "percent": int(usage.percent),
                "type": part.fstype,
                "mountpoint": part.mountpoint,
            }
        )
    return {"devices": result}
