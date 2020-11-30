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
    expected = {"critical", "high", "current", "label"}

    result = test_client.get("/hardware/temps")
    assert result.status_code == 200

    sensor = result.json()["temps"][list(result.json()["temps"].keys())[0]][0]
    print(sensor)

    assert set(sensor.keys()) == expected


def test_cores(test_client):
    """
    When the `/cores` endpoint is called,
    Assert that it returns a Json object with the expected headers.
    """
    expected = {
        "guest",
        "guest_nice",
        "idle",
        "iowait",
        "irq",
        "nice",
        "softirq",
        "steal",
        "system",
        "user",
    }

    result = test_client.get("/hardware/cores")
    assert result.status_code == 200

    core = result.json()["cores"][0]

    assert set(core.keys()) == expected


def test_diskfree(test_client):
    """
    When the `/df` endpoint is called,
    Assert that it returns a Json object with the expected headers.

    """
    expected = {"device", "total", "used", "free", "percent", "type", "mountpoint"}

    result = test_client.get("/hardware/df")
    assert result.status_code == 200

    disk = result.json()["devices"][0]

    assert set(disk.keys()) == expected
