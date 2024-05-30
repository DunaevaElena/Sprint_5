
import random
from selenium import webdriver
import pytest

@pytest.fixture(scope="function")
def login_generate():
    login = f"elena_dunaeva9{random.randint(100, 990)}@yandex.ru"
    return login

@pytest.fixture(scope="function")
def pass_generate():
    password = f"{random.randint(10, 90)}qw{random.randint(100, 900)}"
    return password

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

