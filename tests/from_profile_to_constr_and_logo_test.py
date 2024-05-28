from selenium import webdriver
from selenium.webdriver.common.by import By


class TestProfileToConstructor():
    def test_click_to_constructor(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, ".//*[.='Личный Кабинет']").click()
        driver.find_element(By.XPATH, ".//*[.='Email']").send_keys("elena_dunaeva9999@yandex.ru")
        driver.find_element(By.XPATH, ".//*[.='Пароль']").send_keys("123456")
        driver.find_element(By.XPATH, ".//*[.='Войти']").click()
        driver.find_element(By.XPATH, ".//*[.='Личный Кабинет']").click()
        driver.find_element(By.XPATH, ".//*[contains (text(), 'Конструктор')]").click()
        driver.quit()

    def test_click_to_logo(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, ".//*[.='Личный Кабинет']").click()
        driver.find_element(By.XPATH, ".//*[.='Email']").send_keys("elena_dunaeva9999@yandex.ru")
        driver.find_element(By.XPATH, ".//*[.='Пароль']").send_keys("123456")
        driver.find_element(By.XPATH, ".//*[.='Войти']").click()
        driver.find_element(By.XPATH, ".//*[.='Личный Кабинет']").click()
        driver.find_element(By.CLASS_NAME, ".AppHeader_header__logo__2D0X2").click()
        driver.quit()