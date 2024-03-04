from selenium.webdriver.common.by import By

from pageObjects.confirm_page import ConfirmPage


class SuccessPage:
    def __init__(self, driver):
        self.driver = driver

    successButton = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def get_success_button(self):
        self.driver.find_element(*SuccessPage.successButton).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
