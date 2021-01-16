def test_index(test_client):
    """
    Given a running RPiStatus app,
    Assert that the `/` endpoint returns a 200 status code
    """
    response = test_client.get("/")
    assert response.status_code == 200


def test_ps(test_client):
    """
    When the `/ps` route is called,
    Assert that a Json object with the expected headers is returned.
    """
    response = test_client.get("/ps")
    assert response.status_code == 200

    assert list(response.json().keys())[0].isdigit()
    assert set(list(response.json().values())[0].keys()) == {
        "cpu_percent",
        "memory_percent",
        "name",
        "status",
        "username",
    }
