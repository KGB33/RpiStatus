import pytest

from rpistatus import create_app
from rpistatus.config import Testing


@pytest.fixture(scope="session")
def test_client():
    flask_app = create_app(Testing)
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()
