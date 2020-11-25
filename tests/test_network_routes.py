import socket

def test_network(test_client):
    """
    When the `/network` endpoint is called,
    Assert that a Json object with the expected keys is returned
    """
    assert False


def test_hostname(test_client):
    """
    When the `/network/hostname` endpoint is called,
    Assert that the response matches `socket.gethostname()`
    """
    response = test_client.get("/network/hostname")

    assert response.status_code == 200
    assert response.data.decode() == socket.gethostname()



def test_ip(test_client):
    """
    When the `/network/ip` endpoint is called,
    assert that the the ip maches
    """
    response = test_client.get("/network/ip")

    assert response.status_code == 200
    assert response.data.decode() == socket.gethostbyname(socket.gethostname())
