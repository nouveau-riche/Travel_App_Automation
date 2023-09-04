import pytest

@pytest.mark.flaky(reruns=5)
@pytest.mark.usefixtures("setup_appium_connection")
class BaseTest:
    pass
