from pages.base_page import BasePage


class TrainPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    def search_train(self):
        self.click('select_station_XPATH')
        self.type('enter_source_station_XPATH','Hyderabad')
        self.click('open_source_suggested_station_XPATH')
        self.type('enter_destination_station_XPATH','Gwalior')
        self.click('open_destination_suggested_station_XPATH')
        self.click('change_date_XPATH')
        self.click('select_journey_date_XPATH')
        self.click('search_trains_XPATH') 



