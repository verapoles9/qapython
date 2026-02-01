from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_url(self, url_part):
        """Проверяет URL"""
        with allure.step(f"Проверка URL содержит {url_part}"):
            try:
                self.wait.until(EC.url_contains(url_part))
                return True
            except TimeoutException:
                return False

    def find_element_safe(self, locator, timeout=3):
        """Находит элемент с коротким ожиданием или без"""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return self.driver.find_element(*locator)
