import time
from selenium.webdriver.common.by import By

from PageObjects.checkOutPage import CheckOut
from PageObjects.homePage import HomePage
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getlogger()
        homepage = HomePage(self.driver)
        log.info("Entering into the shop page")
        checkoutpage = homepage.click_on_shop()
        log.info("viewing mobiles and selecting mobiles with text")
        checkoutpage.visibility_of_phones("Nokia Edge")
        checkoutpage.visibility_of_phones("Samsung Note 8")
        log.info("Checking out")
        confirmpage = checkoutpage.checkout_1and2()
        log.info("Entering country name")
        confirmpage.country_sendkeys("Ame")
        time.sleep(3)
        log.info("matching country name")
        self.visibilityoftext("United States of America")
        confirmpage.purchase()
        log.info("getting final success message")
        final_message = confirmpage.successtext()
        assert ("Success! Thank you!") in final_message
        time.sleep(3)
