import pytest
from ..pages.login_page import LoginPage
from ..utils.driver import create_driver


@pytest.fixture(scope='session', autouse=True)
def setup_teardown():
    driver = create_driver('chrome') # Используем Chrome браузер
    yield driver
    driver.quit()


def test_successful_login(setup_teardown):
    """Тест успешного логина"""
    page = LoginPage(setup_teardown)
    page.open("https://www.saucedemo.com")
    page.enter_username("standard_user")
    page.enter_password("secret_sauce")
    page.click_login_button()
    assert "/inventory.html" in page.get_current_url(), "URL не соответствует ожидаемому"


def test_invalid_password_login(setup_teardown):
    """Тест неудачного логина с неправильным паролем"""
    page = LoginPage(setup_teardown)
    page.open("https://www.saucedemo.com")
    page.enter_username("standard_user")
    page.enter_password("wrong_password")
    page.click_login_button()
    assert page.is_error_message_displayed(), "Ошибка не отображается"


def test_locked_user_login(setup_teardown):
    """Тест блокировки аккаунта"""
    page = LoginPage(setup_teardown)
    page.open("https://www.saucedemo.com")
    page.enter_username("locked_out_user")
    page.enter_password("secret_sauce")
    page.click_login_button()
    assert page.is_error_message_displayed(), "Сообщение об ошибке не появилось"


def test_empty_fields_login(setup_teardown):
    """Тест попытки войти с пустыми полями"""
    page = LoginPage(setup_teardown)
    page.open("https://www.saucedemo.com")
    page.click_login_button()
    assert page.is_error_message_displayed(), "Ошибка не отображается"


def test_performance_glitch_user_login(setup_teardown):
    """Тестирование пользователя с задержками"""
    page = LoginPage(setup_teardown)
    page.open("https://www.saucedemo.com")
    page.enter_username("performance_glitch_user")
    page.enter_password("secret_sauce")
    page.click_login_button()
    assert "/inventory.html" in page.get_current_url(), "Переход не выполнен"
