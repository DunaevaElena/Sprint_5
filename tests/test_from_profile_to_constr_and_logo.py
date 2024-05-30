
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

class TestProfileToConstructor:
    def test_click_to_constructor(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("elena_dunaeva9999@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_TAB).click()
        assert WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(TestLocators.BURGER_CONSTRUCTION_TEXT))

    def test_click_to_logo(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("elena_dunaeva9999@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        driver.find_element(*TestLocators.LOGO).click()
        assert WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(TestLocators.BURGER_CONSTRUCTION_TEXT))
