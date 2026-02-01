from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
import time

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"

    @allure.step("Открытие страницы логина")
    def open(self):
        self.driver.get(self.url)
        time.sleep(2)

    @allure.step("Ввод логина: {username}")
    def enter_username(self, username):
        field = self.find_element_safe(self.USERNAME_FIELD)
        field.clear()
        field.send_keys(username)
        time.sleep(0.5)  # Стабильность

    @allure.step("Ввод пароля: {password}")
    def enter_password(self, password):
        field = self.find_element_safe(self.PASSWORD_FIELD)
        field.clear()
        field.send_keys(password)
        time.sleep(0.5)

    @allure.step("Нажатие кнопки Login")
    def click_login(self):
        button = self.find_element_safe(self.LOGIN_BUTTON)
        button.click()
        time.sleep(3)  # Ждем JS реакцию

    @allure.step("Логин {username}/{password}")
    def login(self, username, password):
        self.open()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
