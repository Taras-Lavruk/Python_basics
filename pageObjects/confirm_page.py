from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    countryField = (By.ID, "country")
    countryName = (By.LINK_TEXT, "Ukraine")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseButton = (By.XPATH, "//input[@class='btn btn-success btn-lg']")
    confirmationText = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def get_country_field(self):
        return self.driver.find_element(*ConfirmPage.countryField)

    def get_country_name(self):
        return self.driver.find_element(*ConfirmPage.countryName)

    def get_check_box(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def get_purchase_button(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def get_confirmation_text(self):
        return self.driver.find_element(*ConfirmPage.confirmationText)
