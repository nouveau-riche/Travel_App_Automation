from pages.base_page import BasePage
from utilities.scroll_utils import ScrollUtil


class HotelPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def search_hotel(self,city):
        self.click('search_ID')
        self.type('search_text_ID',city)
        self.clickIndex('open_searched_item_ID',0)
        self.click('search_button_ID')
        
        self.driver.implicitly_wait(10)
        ScrollUtil.swipeUp(2,self.driver)
        ScrollUtil.scrollToTextByAndroidUIAutomator("Hotel Nirmal Mahal", self.driver)
        

