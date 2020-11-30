from fastapi import APIRouter

router = APIRouter(prefix="/docker")


@router.get("/")
def docker():
    """
    "general docker info", whatever that means.
    """


@router.get("/ps")
def ps():
    """
    Returns running docker containers
    """


@router.get("/logs/<container_name>")
def logs(container_name):
    """
    Returns the logs for the provided container.
    """
