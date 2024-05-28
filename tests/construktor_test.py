from selenium import webdriver
from selenium.webdriver.common.by import By


class TestIngredients():
    def test_ingredients(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, ".//*[.='Соусы']").click()
        assert driver.find_element(By.XPATH, "//span[text()='Соусы']/ancestor::div[contains(@class, 'current')]")
        driver.find_element(By.XPATH, ".//*[.='Начинки']").click()
        assert driver.find_element(By.XPATH, "//span[text()='Начинки']/ancestor::div[contains(@class, 'current')]")
        driver.find_element(By.XPATH, ".//*[.='Булки']").click()
        assert driver.find_element(By.XPATH, "//span[text()='Булки']/ancestor::div[contains(@class, 'current')]")
        driver.quit()
