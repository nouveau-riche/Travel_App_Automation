import pytest

from pages.home_page import HomePage
from testcases.base_test import BaseTest


def get_data():
    return [['Mumbai'],['Hyderabad'],]

class Test_SearchHotel(BaseTest):

    @pytest.mark.parametrize("city",get_data())
    def test_search_hotel(self,city):
        home = HomePage(self.driver)
        home.goto_hotel().search_hotel(city)
    