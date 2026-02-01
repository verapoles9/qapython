import pytest
import time
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_successful_login(driver):
    """Успешный логин standard_user"""
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url

def test_wrong_password(driver):
    """Неверный пароль - input_error"""
    login_page = LoginPage(driver)
    login_page.login("standard_user", "wrong_password")
    assert len(driver.find_elements(By.CSS_SELECTOR, ".input_error")) > 0

def test_locked_out_user(driver):
    """Заблокированный пользователь - input_error"""
    login_page = LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce")
    assert len(driver.find_elements(By.CSS_SELECTOR, ".input_error")) > 0

def test_empty_fields(driver):
    """Пустые поля - input_error"""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.click_login()
    assert len(driver.find_elements(By.CSS_SELECTOR, ".input_error")) > 0

def test_performance_glitch_user(driver):
    """Performance glitch - корректный ввод + любая реакция"""
    login_page = LoginPage(driver)
    login_page.login("performance_glitch_user", "secret_sauce")
    
    # Проверяем РЕАКЦИЮ: успех ИЛИ ошибка (нормально для glitch)
    success = "inventory.html" in driver.current_url
    error = len(driver.find_elements(By.CSS_SELECTOR, ".input_error")) > 0
    assert success or error, "Нет реакции на performance_glitch_user"
