import pytest

@pytest.mark.flaky(reruns=2)
@pytest.mark.usefixtures("log_on_failure","setup_appium_connection")
class BaseTest:
    pass
