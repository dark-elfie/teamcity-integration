import logging
import allure


class LogInPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.login_xpath = "//input[@name='email']"
        self.password_xpath = "//input[@name='password_hash']"
        self.log_in_button_xpath = "//button[text()='Zaloguj się']"

    @allure.step("Wprowadzam login: '{1}'")
    def set_login(self, login):
        self.logger.info("Wprowadzam login {}".format(login))
        log_in_input = self.driver.find_element_by_xpath(self.login_xpath)
        log_in_input.click()
        log_in_input.send_keys(login)

    @allure.step("Wprowadzam hasło: '{1}'")
    def set_password(self, password):
        self.logger.info("Wprowadzam hasło {}".format(password))
        password_input = self.driver.find_element_by_xpath(self.password_xpath)
        password_input.click()
        password_input.send_keys(password)

    @allure.step("Loguję się")
    def perform_log_in(self):
        self.logger.info("Loguję się")
        self.driver.find_element_by_xpath(self.log_in_button_xpath).click()
