from selenium import webdriver
from selenium.webdriver.common.by import By


class TestIngredients():
    def test_ingredients(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, ".//*[.='Соусы']").click()
        driver.find_element(By.XPATH, ".//*[.='Начинки']").click()
        driver.find_element(By.XPATH, ".//*[.='Булки']").click()
        driver.quit()
