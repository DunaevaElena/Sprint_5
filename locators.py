from selenium.webdriver.common.by import By

class TestLocators:
    NAME_INPUT = (By.XPATH, ".//*[.='Имя']/input")
    EMAIL_INPUT = (By.XPATH, ".//*[.='Email']/input")
    PASSWORD_INPUT = (By.XPATH, ".//*[.='Пароль']/input")
    REGISTER_BUTTON = (By.XPATH, ".//*[.='Зарегистрироваться']")
    INCORRECT_PASSWORD_TEXT = (By.XPATH, ".//*[.='Некорректный пароль']")
    PROFILE_BUTTON = (By.XPATH, ".//*[.='Личный Кабинет']")
    RESTORE_PASSWORD_TEXT = (By.XPATH, ".//*[.='Восстановить пароль']")

    LOGIN_BUTTON = (By.XPATH, ".//*[.='Войти в аккаунт']")
    SUBMIT_BUTTON = (By.XPATH, ".//*[.='Войти']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//*[.='Личный Кабинет']")
    LOGOUT_BUTTON = (By.XPATH, ".//*[.='Выход']")

    AUTH_LINK = (By.CLASS_NAME, "Auth_link__1fOlj")

    RESTORE_PASSWORD_LINK = (By.XPATH, ".//*[.='Восстановить пароль']")
    RESTORE_PASSWORD_PAGE_TEXT = (By.XPATH, ".//*[.='Восстановление пароля']")

    CONSTRUCTOR_TAB = (By.XPATH, ".//*[contains (text(), 'Конструктор')]")
    BURGER_CONSTRUCTION_TEXT = (By.XPATH, ".//*[.='Соберите бургер']")
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")

    LOGIN_BUTTON2 = (By.XPATH, ".//*[.='Войти']")

    LOGOUT_BUTTON2 = (By.XPATH, "//li[@class='Account_listItem__35dAP']//button[text()='Выход']")
    LOGIN_PAGE_BUTTON = (By.XPATH, ".//*[.='Войти']")

    SAUCES_TAB = (By.XPATH, ".//*[.='Соусы']")
    FILLINGS_TAB = (By.XPATH, ".//*[.='Начинки']")
    BUNS_TAB = (By.XPATH, ".//*[.='Булки']")
    CURRENT_SAUCES = (By.XPATH, "//span[text()='Соусы']/ancestor::div[contains(@class, 'current')]")
    CURRENT_FILLINGS = (By.XPATH, "//span[text()='Начинки']/ancestor::div[contains(@class, 'current')]")
    CURRENT_BUNS = (By.XPATH, "//span[text()='Булки']/ancestor::div[contains(@class, 'current')]")