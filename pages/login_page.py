from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    SUCCESS_TITLE = (By.CSS_SELECTOR, ".title")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"

    @allure.step("Открытие страницы логина")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Ввод логина: {username}")
    def enter_username(self, username):
        self.find_element(self.USERNAME_FIELD).send_keys(username)

    @allure.step("Ввод пароля: {password}")
    def enter_password(self, password):
        self.find_element(self.PASSWORD_FIELD).send_keys(password)

    @allure.step("Нажатие кнопки Login")
    def click_login(self):
        self.find_element(self.LOGIN_BUTTON).click()

    @allure.step("Логин с данными {username}/{password}")
    def login(self, username, password):
        self.open()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    @allure.step("Проверка успешного логина")
    def should_be_success_page(self):
        return self.wait_for_url("inventory.html") and \
               self.find_element(self.SUCCESS_TITLE).text == "Products"

    @allure.step("Проверка ошибки логина")
    def should_be_error(self):
        error = self.find_element(self.ERROR_MESSAGE)
        return "Epic sadface" in error.text

    @allure.step("Проверка пустых полей")
    def should_have_empty_fields_error(self):
        error = self.find_element(self.ERROR_MESSAGE)
        return "Username is required" in error.text or "Password is required" in error.text
