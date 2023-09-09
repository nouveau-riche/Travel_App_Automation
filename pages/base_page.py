from appium.webdriver.common.appiumby import AppiumBy

from utilities.generate_log import*
from utilities.config_reader import read_config

logger = log()

class BasePage:

    def __init__(self,driver):
        self.driver = driver


    def click(self,locator):
        if(str(locator).endswith('_XPATH')):
            self.driver.find_element(AppiumBy.XPATH,read_config('locators',locator)).click()
        elif(str(locator).endswith('_ACCESSIBILITYID')):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,read_config('locators',locator)).click()
        elif(str(locator).endswith('_ID')):
            self.driver.find_element(AppiumBy.ID,read_config('locators',locator)).click()
        logger.info("Clicked on an element" + str(locator))    


    def clickIndex(self,locator,index):
        if(str(locator).endswith('_XPATH')):
            self.driver.find_elements(AppiumBy.XPATH,read_config('locators',locator))[index].click()
        elif(str(locator).endswith('_ACCESSIBILITYID')):
            self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID,read_config('locators',locator))[index].click()
        elif(str(locator).endswith('_ID')):
            self.driver.find_elements(AppiumBy.ID,read_config('locators',locator))[index].click()     
        logger.info("Clicked on an element" + str(locator) + f"with index {index}")    
        

    def type(self,locator,value):
        if(str(locator).endswith('_XPATH')):
            self.driver.find_element(AppiumBy.XPATH,read_config('locators',locator)).send_keys(value)
        elif(str(locator).endswith('_ACCESSIBILITYID')):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,read_config('locators',locator)).send_keys(value)
        elif(str(locator).endswith('_ID')):
            self.driver.find_element(AppiumBy.ID,read_config('locators',locator)).send_keys(value)
        elif(str(locator).endswith('_CLASS')):
            self.driver.find_element(AppiumBy.CLASS_NAME,read_config('locators',locator)).send_keys(value)
        logger.info("Typing an element" + str(locator) + f" value is {value}")    


    def getText(self,locator):
        if(str(locator).endswith('_XPATH')):
            return self.driver.find_element(AppiumBy.XPATH,read_config('locators',locator)).text
        elif(str(locator).endswith('_ACCESSIBILITYID')):
            return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,read_config('locators',locator)).text
        elif(str(locator).endswith('_ID')):
            return self.driver.find_element(AppiumBy.ID,read_config('locators',locator)).text
        logger.info("Getting text from an element" + str(locator))    