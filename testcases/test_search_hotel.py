from pages.home_page import HomePage
from testcases.base_test import BaseTest


class Test_SearchHotel(BaseTest):

    def test_search_hotel(self):
        home = HomePage(self.driver)
        home.goto_hotel().search_hotel('Delhi')
    