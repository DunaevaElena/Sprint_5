from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

class TestIngredients:
    def test_ingredients_sauces(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SAUCES_TAB).click()
        assert driver.find_element(*TestLocators.CURRENT_SAUCES)

    def test_ingredients_fillings(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.FILLINGS_TAB).click()
        assert driver.find_element(*TestLocators.CURRENT_FILLINGS)

    def test_ingredients_buns(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.FILLINGS_TAB).click()  # Переход к разделу "Начинки"
        assert driver.find_element(*TestLocators.CURRENT_FILLINGS)  # Проверка активности раздела "Начинки"
        driver.find_element(*TestLocators.BUNS_TAB).click()  # Переход к разделу "Булки"
        assert driver.find_element(*TestLocators.CURRENT_BUNS)