import random

import pytest

class Fixtures:
    @pytest.fixture(scope="function", autouse=False)
    def login_generate(self):
        login = f"elena_dunaeva9{random.randint(100, 990)}@yandex.ru"
        return login

    @pytest.fixture(scope="function", autouse=False)
    def pass_generate(self):
        password = f"{random.randint(10, 90)}qw{random.randint(100, 900)}"
        return password


