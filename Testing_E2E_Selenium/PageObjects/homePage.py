from selenium.webdriver.common.by import By

from PageObjects.checkOutPage import CheckOut


class HomePage:
    shop = (By.LINK_TEXT, "Shop")

    def __init__(self, driver):
        self.driver = driver

    def click_on_shop(self):
        self.driver.find_element(*HomePage.shop).click()
        return CheckOut(self.driver)

