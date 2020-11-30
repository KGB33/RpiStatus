import os
from pathlib import Path

from fastapi import FastAPI

from .routers import hardware, network, main, docker


BASE_DIR = Path(__file__).parent  # os.path.dirname(os.path.realpath(__file__))


def create_app(config=os.environ["APP_CONFIG"]):
    app = FastAPI()
    # app.config.from_object(config)

    app.include_router(main.router)
    app.include_router(hardware.router)
    app.include_router(network.router)
    app.include_router(docker.router)

    return app


app = create_app()
