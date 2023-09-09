from pages.home_page import HomePage
from testcases.base_test import BaseTest

class Test_SearchTrain(BaseTest):

    def test_search_train(self):
        home = HomePage(self.driver)
        home.goto_train().search_train()
