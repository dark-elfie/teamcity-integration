import pytest
from pages.log_in_page import LogInPage
import allure


@pytest.mark.usefixtures("setup")
class TestLogIn:

    @allure.title("Zaloguj jako administrator")
    def test_log_in_admin(self, setup):
        self.driver.get("https://agrii-tms.x-one.dev/login")
        log_in_page = LogInPage(self.driver)
        log_in_page.set_login("skowalska@x-one.com.pl")
        log_in_page.set_password("123456789")
        log_in_page.perform_log_in()
