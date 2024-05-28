from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestAutorize():
    def test_autorize_akk(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, ".//*[.='Войти в аккаунт']").click()
        driver.find_element(By.XPATH, ".//*[.='Email']/input").send_keys("elena_dunaeva9999@yandex.ru")
        driver.find_element(By.XPATH, ".//*[.='Пароль']/input").send_keys("123456")
        driver.find_element(By.XPATH, ".//*[.='Войти']").click()
        profile = driver.find_element(By.XPATH, ".//*[.='Личный Кабинет']")
        profile.click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[.='Выход']")))
        driver.quit()

    def test_autorize_lk(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, ".//*[.='Личный Кабинет']").click()
        driver.find_element(By.XPATH, ".//*[.='Email']/input").send_keys("elena_dunaeva9999@yandex.ru")
        driver.find_element(By.XPATH, ".//*[.='Пароль']/input").send_keys("123456")
        driver.find_element(By.XPATH, ".//*[.='Войти']").click()
        profile = driver.find_element(By.XPATH, ".//*[.='Личный Кабинет']")
        profile.click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//*[.='Выход']")))
        driver.quit()

    def test_autorize_reg_form(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()
        driver.find_element(By.XPATH, ".//*[.='Email']/input").send_keys("elena_dunaeva9999@yandex.ru")
        driver.find_element(By.XPATH, ".//*[.='Пароль']/input").send_keys("123456")
        driver.find_element(By.XPATH, ".//*[.='Войти']").click()
        profile = driver.find_element(By.XPATH, ".//*[.='Личный Кабинет']")
        profile.click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//*[.='Выход']")))
        driver.quit()

    def test_autorize_forgot_pass(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(By.XPATH, ".//*[.='Восстановить пароль']").click()
        driver.find_element(By.XPATH, ".//*[.='Email']/input").send_keys("elena_dunaeva9999@yandex.ru")
        driver.find_element(By.XPATH, ".//*[.='Восстановить']").click()
        remembered_password_page = driver.find_element(By.XPATH, ".//*[.='Воссановление пароля']")
        assert remembered_password_page
        driver.quit()