from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogout():
    def test_logout(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, ".//*[.='Личный Кабинет']").click()
        driver.find_element(By.XPATH, ".//*[.='Email']").send_keys("elena_dunaeva9999@yandex.ru")
        driver.find_element(By.XPATH, ".//*[.='Пароль']").send_keys("123456")
        driver.find_element(By.XPATH, ".//*[.='Выход']").click()
        driver.quit()