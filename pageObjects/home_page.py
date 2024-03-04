from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.checkout_page import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, "name")
    mail = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.XPATH, "//body/app-root[1]/form-comp[1]/div[1]/form[1]/input[1]")
    submit = (By.CLASS_NAME, "btn btn-success")
    gender = (By.ID, "exampleFormControlSelect1")
    submitText = (By.CLASS_NAME, "alert-success")
    birthDate = (By.NAME, "bday")

    def get_shop_items(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_mail(self):
        return self.driver.find_element(*HomePage.mail)

    def get_password(self):
        return self.driver.find_element(*HomePage.password)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def get_birth_date(self):
        return self.driver.find_element(*HomePage.birthDate)

    def get_submit_text(self):
        return self.driver.find_element(*HomePage.submitText)