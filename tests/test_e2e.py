import pytest
from pageObjects.home_page import HomePage
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getlogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.get_shop_items()
        cards = checkoutPage.get_card_titles()
        log.info("getting all card titles")
        for card in cards:
            cardName = card.text
            log.info(cardName)
            if cardName == "OnePlus":
                checkoutPage.get_card_button().click()
        successPage = checkoutPage.get_checkout_button()
        confirmPage = successPage.get_success_button()
        log.info("Entering country name as ukr")
        confirmPage.get_country_field().send_keys("ukr")
        self.verify_element_presence("Ukraine")
        # wait = WebDriverWait(self.driver, 10).until(
        # expected_conditions.presence_of_element_located(confirmPage.countryName))
        confirmPage.get_country_name().click()
        confirmPage.get_check_box().click()
        confirmPage.get_purchase_button().click()
        assertion = confirmPage.get_confirmation_text().text
        log.info("Text received from application is " + assertion)
        assert "Success! Thank you! Your" in assertion
