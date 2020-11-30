import pytest

from rpistatus import create_app
from rpistatus.config import Testing

from fastapi.testclient import TestClient


@pytest.fixture(scope="session")
def test_client():
    app = create_app(Testing)
    testing_client = TestClient(app)

    yield testing_client
