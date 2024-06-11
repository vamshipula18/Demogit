from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    send_letters_country = (By.CSS_SELECTOR, "#country")
    checkbox_fill = (By.CSS_SELECTOR, "label[for='checkbox2']")
    purchase_button= (By.XPATH, "//input[@value='Purchase']")
    successmessage  = alerttext = (By.CSS_SELECTOR, "div[class*='alert']")
    def country_sendkeys(self,text):
        return self.driver.find_element(*ConfirmPage.send_letters_country).send_keys(text)

    def purchase(self):
        self.driver.find_element(*ConfirmPage.checkbox_fill).click()
        return self.driver.find_element(*ConfirmPage.purchase_button).click()

    def successtext(self):
        return self.driver.find_element(*ConfirmPage.successmessage).text



