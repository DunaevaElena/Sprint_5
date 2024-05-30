
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

class TestRegistr:
    def test_registration(self, driver, login_generate, pass_generate):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.NAME_INPUT).send_keys("Елена")
        email = login_generate
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(email)
        password = pass_generate
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()
        url_after = "https://stellarburgers.nomoreparties.site/login"
        assert url_after

    def test_registration_incorrect_email(self, driver, login_generate):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.NAME_INPUT).send_keys("Елена")
        email = login_generate
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("000")
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.INCORRECT_PASSWORD_TEXT))

