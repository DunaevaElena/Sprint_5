from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

class TestLogout:
    def test_logout(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("elena_dunaeva9999@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*TestLocators.LOGIN_BUTTON2).click()
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(TestLocators.LOGOUT_BUTTON2)).click()
        assert WebDriverWait(driver, 3).until(EC.element_to_be_clickable(TestLocators.LOGIN_PAGE_BUTTON))

