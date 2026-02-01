import pytest
import allure
from pages.login_page import LoginPage

@allure.feature("Авторизация")
@allure.story("Успешный логин")
def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert login_page.should_be_success_page(), "Успешный логин не прошел"

@allure.feature("Авторизация")
@allure.story("Неверный пароль")
def test_wrong_password(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "wrong_password")
    assert login_page.should_be_error(), "Не появилась ошибка неверного пароля"

@allure.feature("Авторизация")
@allure.story("Заблокированный пользователь")
def test_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce")
    assert login_page.should_be_error(), "Не появилась ошибка заблокированного пользователя"

@allure.feature("Авторизация")
@allure.story("Пустые поля")
def test_empty_fields(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username("")
    login_page.enter_password("")
    login_page.click_login()
    assert login_page.should_have_empty_fields_error(), "Не появилась ошибка пустых полей"

@allure.feature("Авторизация")
@allure.story("Performance glitch user")
def test_performance_glitch_user(driver):
    login_page = LoginPage(driver)
    login_page.login("performance_glitch_user", "secret_sauce")
    assert login_page.should_be_success_page(), "Performance user не залогинился"
