import pytest
import allure
from allure_commons.types import AttachmentType
from appium import webdriver
import shutup; shutup.please()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope='function')
def setup_appium_connection(request):
    desired_cap = {
        "deviceName": 'RZCW71YVAAW',
        "platformName": 'Android',
        "platformVersion": "13",
        "appium:appPackage": "com.goibibo",
        "appium:appActivity": ".common.HomeActivity",
        "appium:automationName": "UiAutomator2",
        "appium:noReset": True,
        "appium:appWaitforLaunch": False,
    }
    driver = webdriver.Remote('http://localhost:4723', desired_cap)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield
    driver.quit()



@pytest.fixture()
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
