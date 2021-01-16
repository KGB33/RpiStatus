import psutil

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
@router.get("/index")
async def index():
    # TODO: Change RaspberryPi to hostname
    return "RaspberryPi is Connected and Running.", 200


@router.get("/ps")
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
