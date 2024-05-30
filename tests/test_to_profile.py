
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

class TestProfile:
    def test_profile(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        profile = driver.find_element(*TestLocators.PROFILE_BUTTON)
        profile.click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.RESTORE_PASSWORD_TEXT))