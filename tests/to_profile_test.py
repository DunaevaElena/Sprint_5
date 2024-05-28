
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestProfile():
    def test_profile(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        profile = driver.find_element(By.XPATH, ".//*[.='Личный Кабинет']")
        profile.click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[.='Восстановить пароль']")))
        driver.quit()


