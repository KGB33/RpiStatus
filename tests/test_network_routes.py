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
    assert False


def test_ip(test_client):
    """
    When the `/network/ip` endpoint is called,
    assert that the response maches the internal ip address of the host
    """
    assert False
