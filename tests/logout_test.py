

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogout():
    def test_logout(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, ".//*[.='Личный Кабинет']").click()
        driver.find_element(By.XPATH, ".//*[.='Email']/input").send_keys("elena_dunaeva9999@yandex.ru")
        driver.find_element(By.XPATH, ".//*[.='Пароль']/input").send_keys("123456")
        driver.find_element(By.XPATH, ".//*[.='Войти']").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, ".//*[.='Личный Кабинет']"))).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, "//li[@class='Account_listItem__35dAP']//button[text()='Выход']"))).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//*[.='Войти']")))

        driver.quit()