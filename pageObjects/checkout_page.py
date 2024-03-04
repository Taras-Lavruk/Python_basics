from selenium.webdriver.common.by import By

from pageObjects.success_page import SuccessPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
    cardTitles = (By.XPATH, "//div[@class='card h-100']/div/a")
    cardTitle = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    cardButton = (By.XPATH, "//div[@class='card h-100']/div/div/button")
    checkoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def get_card_titles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitles)

    def get_card_title(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def get_card_button(self):
        return self.driver.find_elements(*CheckoutPage.cardButton)

    def get_checkout_button(self):
        self.driver.find_element(*CheckoutPage.checkoutButton).click()
        successPage = SuccessPage(self.driver)
        return successPage
