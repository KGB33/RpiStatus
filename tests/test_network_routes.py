import socket


def test_network(test_client):
    """
    When the `/network` endpoint is called,
    Assert that a Json object with the expected keys is returned
    """
    response = test_client.get("/network/")
    assert response.status_code == 200

    assert set(response.json().keys()) == {"ips", "hostname"}


def test_hostname(test_client):
    """
    When the `/network/hostname` endpoint is called,
    Assert that the response matches `socket.gethostname()`
    """
    response = test_client.get("/network/hostname")
    assert response.status_code == 200
    assert response.json() == {"hostname": socket.gethostname()}


def test_ip(test_client):
    """
    When the `/network/ip` endpoint is called,
    assert that the the returned json structure maches
    """
    response = test_client.get("/network/ip")
    assert response.status_code == 200

    assert type(response.json()["ips"]) == list
    assert set(response.json()["ips"][0].keys()) == {"name", "type", "addresses"}
