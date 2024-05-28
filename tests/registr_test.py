from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.fixtures import Fixtures


class TestRegistr(Fixtures):
    def test_registration(self, login_generate, pass_generate):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.XPATH, ".//*[.='Имя']/input").send_keys("Елена")
        email = login_generate
        driver.find_element(By.XPATH, ".//*[.='Email']/input").send_keys(email)
        password = pass_generate
        driver.find_element(By.XPATH, ".//*[.='Пароль']/input").send_keys(password)
        driver.find_element(By.XPATH, ".//*[.='Зарегистрироваться']").click()
        url_after = "https://stellarburgers.nomoreparties.site/login"
        assert url_after
        driver.quit()

    def test_registration_incorrect_email(self, login_generate, pass_generate):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.XPATH, ".//*[.='Имя']/input").send_keys("Елена")
        email = login_generate
        driver.find_element(By.XPATH, ".//*[.='Email']/input").send_keys(email)
        driver.find_element(By.XPATH, ".//*[.='Пароль/input']").send_keys("123")
        driver.find_element(By.XPATH, ".//*[.='Зарегистрироваться']").click()
        assert ValueError("Invalid password")
        driver.quit()



