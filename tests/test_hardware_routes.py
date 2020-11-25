def test_hardware(test_client):
    """
    When the `/hardware` end point is called,
    Assert that it returns a Json object with the expected headers.
    """
    assert False


def test_temps(test_client):
    """
    When the `/temps` endpoint is called,
    Assert that it returns a Json object with the expected headers.
    """
    assert False


def test_cores(test_client):
    """
    When the `/cores` endpoint is called,
    Assert that it returns a Json object with the expected headers.
    """
    assert False


def test_diskfree(test_client):
    """
    When the `/df` endpoint is called,
    Assert that it returns a Json object with the expected headers.

    """
    expected = {"Filesystem", "Size", "Used", "Avalable", "Capacity", "MountedOn"}

    result = test_client.get("/hardware/df")
    assert result.status_code == 200

    disk = result.json()[0]

    assert set(disk.keys()) == expected

    assert type(disk["Filesystem"]) == str
    assert type(disk["Size"]) == int
    assert type(disk["Used"]) == int
    assert type(disk["Avalable"]) == int
    assert type(disk["Capacity"]) == int
    assert type(disk["MountedOn"]) == str

    assert 0 <= disk["Capacity"] <= 100
