import time

from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckOut:
    def __init__(self, driver):
        self.driver = driver

    phones_view = (By.CSS_SELECTOR, "div[class='card h-100']")
    phone_match_text = (By.CSS_SELECTOR, "h4 a")
    click_on_phone = (By.CSS_SELECTOR, "div button")
    checkout1 = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkout2 = (By.XPATH, "//button[@class='btn btn-success']")

    def visibility_of_phones(self, phone_name):
        phones = self.driver.find_elements(*CheckOut.phones_view)
        for phone in phones:
            if phone.find_element(*CheckOut.phone_match_text).text == phone_name:
                phone.find_element(*CheckOut.click_on_phone).click()
    def checkout_1and2(self):
        self.driver.find_element(*CheckOut.checkout1).click()
        self.driver.find_element(*CheckOut.checkout2).click()
        return ConfirmPage(self.driver)
