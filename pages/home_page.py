from pages.base_page import BasePage
from pages.hotel_page import HotelPage
from utilities.generate_log import*


class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)


    def goto_hotel(self):
        self.click('hotels_XPATH')
        return HotelPage(self.driver)
        
