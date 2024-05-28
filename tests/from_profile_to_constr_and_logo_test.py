

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestProfileToConstructor():
    def test_click_to_constructor(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, ".//*[.='Личный Кабинет']").click()
        driver.find_element(By.XPATH, ".//*[.='Email']/input").send_keys("elena_dunaeva9999@yandex.ru")
        driver.find_element(By.XPATH, ".//*[.='Пароль']/input").send_keys("123456")
        driver.find_element(By.XPATH, ".//*[.='Войти']").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, ".//*[.='Личный Кабинет']"))).click()
        driver.find_element(By.XPATH, ".//*[contains (text(), 'Конструктор')]").click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//*[.='Соберите бургер']")))
        driver.quit()

    def test_click_to_logo(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, ".//*[.='Личный Кабинет']").click()
        driver.find_element(By.XPATH, ".//*[.='Email']/input").send_keys("elena_dunaeva9999@yandex.ru")
        driver.find_element(By.XPATH, ".//*[.='Пароль']/input").send_keys("123456")
        driver.find_element(By.XPATH, ".//*[.='Войти']").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, ".//*[.='Личный Кабинет']"))).click()
        driver.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2").click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//*[.='Соберите бургер']")))
        driver.quit()