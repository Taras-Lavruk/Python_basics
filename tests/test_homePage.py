import pytest

from TestData.home_page_data import HomePageData
from pageObjects.home_page import HomePage
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class TestTwo(BaseClass):

    def test_home_page(self, get_data):
        log = self.getlogger()
        homePage = HomePage(self.driver)
        log.info("First name is " + get_data["firstname"])
        homePage.get_name().send_keys(get_data["firstname"])
        homePage.get_mail().send_keys(get_data["mail"])
        homePage.get_password().send_keys(get_data["password"])
        self.select_text_option(homePage.get_gender(), get_data["gender"])
        homePage.get_checkbox().click()
        homePage.get_birth_date().send_keys(get_data["bday"])

        message = homePage.get_submit_text().text
        print(message)
        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_homepage_data)
    def get_data(self, request):
        return request.param
