
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators


class TestAutorize:
    def test_autorize_akk(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("elena_dunaeva9999@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*TestLocators.SUBMIT_BUTTON).click()
        profile = driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON)
        profile.click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGOUT_BUTTON))

    def test_autorize_lk(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("elena_dunaeva9999@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*TestLocators.SUBMIT_BUTTON).click()
        profile = driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON)
        profile.click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGOUT_BUTTON))

    def test_autorize_reg_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.AUTH_LINK).click()
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("elena_dunaeva9999@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*TestLocators.SUBMIT_BUTTON).click()
        profile = driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON)
        profile.click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGOUT_BUTTON))

    def test_autorize_forgot_pass(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*TestLocators.RESTORE_PASSWORD_LINK).click()
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("elena_dunaeva9999@yandex.ru")
        driver.find_element(*TestLocators.RESTORE_PASSWORD_PAGE_TEXT).click()
        remembered_password_page = driver.find_element(*TestLocators.RESTORE_PASSWORD_PAGE_TEXT)
        assert remembered_password_page
