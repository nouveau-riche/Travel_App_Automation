import pytest
import allure
from allure_commons.types import AttachmentType
from appium import webdriver

from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

# import shutup; shutup.please()



APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


def create_android_driver():

    # desired_cap = {
    #     "deviceName": '2B131FDH30014G',
    #     "platformName": 'Android',
    #     "platformVersion": "13",
    #     "appium:appPackage": "com.goibibo",
    #     "appium:appActivity": ".common.HomeActivity",
    #     "appium:automationName": "UiAutomator2",
    #     "appium:noReset": True,
    #     "appium:appWaitforLaunch": False,
    # }

    # return webdriver.Remote('http://localhost:4723', desired_cap)

    options = UiAutomator2Options()
    options.device_name = '2B131FDH30014G' 
    options.platform_name = 'Android'
    options.app_package = 'com.goibibo'
    options.app_activity = '.common.HomeActivity'
    options.automation_name = 'UiAutomator2'
    options.no_reset = True
    options.app_wait_for_launch = False

    return webdriver.Remote(f'http://localhost:{APPIUM_PORT}', options)



def create_ios_driver():

    options = XCUITestOptions()
    options.udid = '2B131FDH30014G' 
    options.platform_name = 'iOS'
    options.bundle_id = 'com.goibibo'
    options.automation_name = 'XCUITest'
    options.no_reset = True

    return webdriver.Remote('http://localhost:4723', options)



@pytest.fixture(scope='function')
def setup_appium_connection(request):

    driver = create_android_driver()
    request.cls.driver = driver
    driver.implicitly_wait(8)
    yield driver
    driver.quit()



@pytest.fixture()
def log_on_failure(request, setup_appium_connection):
    yield
    item = request.node
    driver = setup_appium_connection
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
